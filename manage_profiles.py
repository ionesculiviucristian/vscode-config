import argparse
import importlib.util
import json
import os
import platform
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


class DevContainerConfigCustomizationsVSCode(TypedDict):
    extensions: List[str]
    settings: Settings


class DevContainerConfigCustomizations(TypedDict):
    vscode: DevContainerConfigCustomizationsVSCode


class DevContainerConfig(TypedDict):
    customizations: DevContainerConfigCustomizations


class Manager:
    primary_profile_settings: List[Settings]
    primary_profile: Profile
    profiles_dir: str
    profiles: List[Profile]
    storage_file_path: str

    def __init__(self):
        if platform.system() == "Windows":
            code_path = os.path.join(os.environ["APPDATA"], "Code", "User")
        else:
            code_path = os.path.join(os.path.expanduser("~"), ".config", "Code", "User")
        if not os.path.exists(code_path):
            raise Exception("VS Code configuration directory not found")

        self.profiles_dir = os.path.join(code_path, "profiles")
        if not os.path.exists(self.profiles_dir):
            os.mkdir(self.profiles_dir)

        self.storage_file_path = os.path.join(code_path, "globalStorage", "storage.json")
        if not os.path.exists(self.storage_file_path):
            raise Exception(f"Storage file not found at {self.storage_file_path}")

        with open("./data/profiles.json", "r") as f1:
            self.profiles = json.load(f1)

        self.primary_profile = next(p for p in self.profiles if "primary" in p)

        self.primary_profile_settings = self.merge_profile_settings(self.primary_profile)

    def profile_exists(self, profile: Profile) -> bool:
        with open(self.storage_file_path, "r") as f:
            data = json.load(f)

        created_profiles = data.get("userDataProfiles", [])

        return any(created_profile.get("location") == profile["id"] for created_profile in created_profiles)

    def create_profile(self, profile: Profile) -> None:
        os.makedirs(os.path.join(self.profiles_dir, profile["id"]), exist_ok=True)

        with open(self.storage_file_path, "r") as f:
            data = json.load(f)

        userDataProfile = {"location": profile["id"], "name": profile["name"]}

        if "userDataProfiles" in data:
            data["userDataProfiles"].append(userDataProfile)
        else:
            data["userDataProfiles"] = [userDataProfile]

        with open(self.storage_file_path, "w") as f:
            debug(f"Creating {userDataProfile['name']} profile")
            json.dump(data, f, indent=2)

    def install_profile_extension(self, profile: Profile, extension: Extension) -> None:
        try:
            version = f"@{extension['version']}" if "version" in extension else ""
            debug(f"Installing {extension['id']}{version} extension for {profile['name']} profile")
            subprocess.run(
                ["code", "--profile", profile["name"], "--install-extension", f"{extension['id']}{version}"],
                stdout=subprocess.DEVNULL,
                check=True,
            )
        except subprocess.CalledProcessError as e:
            raise Exception(
                f"An error occurred while installing extension {extension['id']} for profile {profile['name']}: {e}"
            )

    @staticmethod
    def deep_merge(base: Settings, override: Settings) -> Settings:
        result = base.copy()
        for key, value in override.items():
            existing = result.get(key)
            if isinstance(existing, dict) and isinstance(value, dict):
                result[key] = Manager.deep_merge(existing, value)
            else:
                result[key] = value
        return result

    def compile_profile_settings(self, profile: Profile, settings: List[Settings]) -> str:
        result: Settings = {}
        for item in settings:
            result = self.deep_merge(result, item)
        return json.dumps(result)

    def save_profile_settings(self, profile: Profile, settings: List[Settings]) -> None:
        compiled_settings = self.compile_profile_settings(profile, settings)

        with open(f"{self.profiles_dir}/{profile['id']}/settings.json", "w") as f:
            debug(f"Saving settings for {profile['name']} profile")
            json.dump(json.loads(compiled_settings), f, indent=2)

    def merge_profile_settings(self, profile: Profile) -> List[Settings]:
        settings: List[Settings] = []

        if "settings" in profile:
            settings.append(profile["settings"])

        for extension in profile["extensions"]:
            if "settings" in extension:
                settings.append(extension["settings"])

        return settings

    def install_profile(self, profile: Profile, primary_profile: Optional[Profile] = None) -> None:
        if not self.profile_exists(profile):
            self.create_profile(profile)

        if primary_profile:
            shutil.copyfile(
                os.path.join(self.profiles_dir, primary_profile["id"], "extensions.json"),
                os.path.join(self.profiles_dir, profile["id"], "extensions.json"),
            )

        for extension in profile["extensions"]:
            self.install_profile_extension(profile, extension)

        profile_settings = self.merge_profile_settings(profile)

        if primary_profile:
            profile_settings += self.primary_profile_settings

        if "extends" in profile and profile["extends"]:
            for extended in profile["extends"]:
                extended_profile = next(p for p in self.profiles if p["id"] == extended)
                if not extended_profile:
                    debug(f"{profile['name']} extends a missing profile: {extended}")
                    continue
                if "settings" in extended_profile:
                    profile_settings.append(extended_profile["settings"])
                for extended_extension in extended_profile["extensions"]:
                    self.install_profile_extension(profile, extended_extension)
                    if "settings" in extended_extension:
                        profile_settings.append(extended_extension["settings"])

        self.save_profile_settings(profile, profile_settings)

    @staticmethod
    def run_extension_setups(action: str) -> None:
        configs_dir = "./configs"

        for name in sorted(os.listdir(configs_dir)):
            setup_path = os.path.join(configs_dir, name, "setup.py")
            if not os.path.isfile(setup_path):
                debug(f"No setup.py found in {name}, skipping")
                continue

            spec = importlib.util.spec_from_file_location(f"configs.{name}.setup", setup_path)
            if not spec or not spec.loader:
                continue

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            fn = getattr(module, action, None)
            if callable(fn):
                debug(f"Running {action} for {name}")
                fn()

    def install(self) -> None:
        self.install_profile(self.primary_profile)

        other_profiles = [p for p in self.profiles if "primary" not in p]
        for profile in other_profiles:
            self.install_profile(profile, self.primary_profile)

    def uninstall_profile(self, profile: Profile) -> None:
        with open(self.storage_file_path, "r") as f:
            data = json.load(f)

        data["userDataProfiles"] = [p for p in data.get("userDataProfiles", []) if p.get("location") != profile["id"]]

        with open(self.storage_file_path, "w") as f:
            json.dump(data, f, indent=2)

        profile_path = os.path.join(self.profiles_dir, profile["id"])
        if os.path.exists(profile_path):
            debug(f"Removing {profile['name']} profile")
            shutil.rmtree(profile_path)

    def uninstall(self) -> None:
        for profile in self.profiles:
            self.uninstall_profile(profile)

    def save_devcontainer_profile(self, profile: Profile, primary_profile: Optional[Profile] = None) -> None:
        data: DevContainerConfig = {"customizations": {"vscode": {"extensions": [], "settings": {}}}}

        settings = self.merge_profile_settings(profile)

        for extension in profile["extensions"]:
            data["customizations"]["vscode"]["extensions"].append(extension["id"])

        if primary_profile:
            settings += self.primary_profile_settings
            for extension in primary_profile["extensions"]:
                data["customizations"]["vscode"]["extensions"].append(extension["id"])

        if "extends" in profile and profile["extends"]:
            for extended in profile["extends"]:
                extended_profile = next(p for p in self.profiles if p["id"] == extended)
                if not extended_profile:
                    debug(f"{profile['name']} extends a missing profile: {extended}")
                    continue
                if "settings" in extended_profile:
                    settings.append(extended_profile["settings"])
                for extended_extension in extended_profile["extensions"]:
                    data["customizations"]["vscode"]["extensions"].append(extended_extension["id"])
                    if "settings" in extended_extension:
                        settings.append(extended_extension["settings"])

        data["customizations"]["vscode"]["settings"] = json.loads(self.compile_profile_settings(profile, settings))

        with open(f"./devcontainers/{profile['id']}.json", "w") as f:
            json.dump(data, f, indent=2)

    def generate_devcontainer_profiles(self) -> None:
        self.save_devcontainer_profile(self.primary_profile)

        other_profiles = [p for p in self.profiles if "primary" not in p]
        for profile in other_profiles:
            self.save_devcontainer_profile(profile, self.primary_profile)


def main() -> None:
    parser = argparse.ArgumentParser(description="Manage VSCode profiles")
    parser.add_argument("--install", action="store_true", help="Install all profiles")
    parser.add_argument("--uninstall", action="store_true", help="Uninstall all profiles")
    parser.add_argument("--devcontainers", action="store_true", help="Generate devcontainer profiles")
    parser.add_argument("--install-configs", action="store_true", help="Install extension configurations")
    parser.add_argument("--uninstall-configs", action="store_true", help="Uninstall extension configurations")
    args = parser.parse_args()

    manager = Manager()

    if args.install:
        manager.install()
    elif args.uninstall:
        manager.uninstall()
    elif args.devcontainers:
        manager.generate_devcontainer_profiles()
    elif args.install_configs:
        Manager.run_extension_setups("install")
    elif args.uninstall_configs:
        Manager.run_extension_setups("uninstall")
    else:
        print(
            "No action specified. Use --install, --uninstall, --devcontainers, --install-configs or --uninstall-configs"
        )


if __name__ == "__main__":
    main()
