import argparse
import json
import os
import shutil
import subprocess
from typing import Dict, List, Optional, TypedDict, Union

DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"


def debug(msg: str):
    if DEBUG_MODE:
        print(msg)


Settings = Dict[str, Union[str, int, bool, "Settings"]]


class Extension(TypedDict):
    category: str
    description: str
    id: str
    name: str
    settings: Settings
    version: Optional[str]


class Profile(TypedDict):
    extends: Optional[List[str]]
    extensions: List[Extension]
    id: str
    name: str
    primary: bool
    settings: Settings


class Manager:
    primary_profile_settings: List[Settings]
    primary_profile: Profile
    profiles_dir: str
    profiles: List[Profile]
    storage_file_path: str

    def __init__(self):
        code_path = os.path.join(os.path.expanduser("~"), ".config", "Code", "User")
        if not code_path:
            raise Exception("Code is not installed")

        self.profiles_dir = os.path.join(code_path, "profiles")
        if not os.path.exists(self.profiles_dir):
            os.mkdir(self.profiles_dir)

        self.storage_file_path = os.path.join(code_path, "globalStorage", "storage.json")
        if not os.path.exists(self.storage_file_path):
            raise Exception(f"Storage file not found at {self.storage_file_path}")

        with open("./data/profiles.json", "r") as f1:
            self.profiles = json.load(f1)

        self.primary_profile = next(p for p in self.profiles if "primary" in p)

        self.primary_profile_settings = self.compile_profile_settings(self.primary_profile)

    def profile_exists(self, profile: Profile):
        with open(self.storage_file_path, "r") as f:
            data = json.load(f)

        created_profiles = data.get("userDataProfiles", [])

        return any(created_profile.get("location") == profile["id"] for created_profile in created_profiles)

    def create_profile(self, profile: Profile):
        os.makedirs(os.path.join(self.profiles_dir, profile["id"]), exist_ok=True)

        with open(self.storage_file_path, "r") as f:
            data = json.load(f)

        userDataProfile = {"location": profile["id"], "name": profile["name"]}

        if "userDataProfiles" in data:
            data["userDataProfiles"].append(userDataProfile)
        else:
            data["userDataProfiles"] = [userDataProfile]

        with open(self.storage_file_path, "w") as f:
            json.dump(data, f, indent=2)
        debug(f"Created profile {userDataProfile['name']}")

    def install_profile_extension(self, profile: Profile, extension: Extension):
        try:
            version = f"@{extension['version']}" if "version" in extension else ""
            subprocess.run(
                f"code --profile '{profile['name']}' --install-extension '{extension['id']}{version}' >/dev/null",
                shell=True,
                check=True,
            )
            debug(f"Installed extension {extension['id']} for profile {profile['name']}")
        except subprocess.CalledProcessError as e:
            raise Exception(
                f"An error occurred while installing extension {extension['id']} for profile {profile['name']}: {e}"
            )

    def save_profile_settings(self, profile: Profile, settings: List[Settings]):
        raw_settings = json.dumps(settings)

        result = subprocess.run(
            ["jq", "reduce .[] as $item ({}; . * $item)"], input=raw_settings, capture_output=True, text=True
        )

        if result.returncode != 0:
            raise Exception(f"Failed to compile settings for profile {profile['name']}: {result.stderr.strip()}")

        with open(f"{self.profiles_dir}/{profile['id']}/settings.json", "w") as f:
            json.dump(json.loads(result.stdout), f, indent=2)
        debug(f"Saved settings for profile {profile['name']}")

    def compile_profile_settings(self, profile: Profile):
        settings: List[Settings] = []

        if "settings" in profile:
            settings.append(profile["settings"])

        for extension in profile["extensions"]:
            if "settings" in extension:
                settings.append(extension["settings"])

        return settings

    def install_profile(self, profile: Profile, primary_profile: Optional[Profile] = None):
        if not self.profile_exists(profile):
            self.create_profile(profile)

        if primary_profile:
            shutil.copyfile(
                os.path.join(self.profiles_dir, primary_profile["id"], "extensions.json"),
                os.path.join(self.profiles_dir, profile["id"], "extensions.json"),
            )

        for extension in profile["extensions"]:
            self.install_profile_extension(profile, extension)

        profile_settings = self.compile_profile_settings(profile)

        if primary_profile:
            profile_settings += self.primary_profile_settings

        if "extends" in profile and profile["extends"]:
            for extended in profile["extends"]:
                extended_profile = next(p for p in self.profiles if p["id"] == extended)
                if not extended_profile:
                    debug(f"Extended profile {extended} not found")
                    continue
                if "settings" in extended_profile:
                    profile_settings.append(extended_profile["settings"])
                for extended_extension in extended_profile["extensions"]:
                    self.install_profile_extension(profile, extended_extension)
                    if "settings" in extended_extension:
                        profile_settings.append(extended_extension["settings"])

        self.save_profile_settings(profile, profile_settings)

    def install(self):
        self.install_profile(self.primary_profile)

        other_profiles = [p for p in self.profiles if "primary" not in p]
        for profile in other_profiles:
            self.install_profile(profile, self.primary_profile)

    def uninstall_profile(self, profile: Profile):
        with open(self.storage_file_path, "r") as f:
            data = json.load(f)

        data["userDataProfiles"] = [p for p in data.get("userDataProfiles", []) if p.get("location") != profile["id"]]

        with open(self.storage_file_path, "w") as f:
            json.dump(data, f, indent=2)

        profile_path = os.path.join(self.profiles_dir, profile["id"])
        if os.path.exists(profile_path):
            shutil.rmtree(profile_path)
        debug(f"Removed profile {profile['name']}")

    def uninstall(self):
        for profile in self.profiles:
            self.uninstall_profile(profile)


def main() -> None:
    parser = argparse.ArgumentParser(description="Manage VSCode profiles")
    parser.add_argument("--install", action="store_true", help="Install all profiles")
    parser.add_argument("--uninstall", action="store_true", help="Uninstall all profiles")
    args = parser.parse_args()

    manager = Manager()

    if args.install:
        manager.install()
    elif args.uninstall:
        manager.uninstall()
    else:
        print("No action specified. Use --install or --uninstall")


if __name__ == "__main__":
    main()
