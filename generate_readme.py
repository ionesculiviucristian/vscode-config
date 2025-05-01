import json
from collections import defaultdict

base_extensions_url = "https://marketplace.visualstudio.com/items"

with open("profiles.json", "r") as f1:
    profiles = json.load(f1)

    with open("docs/header.md", "r") as h:
        header = h.read()
    with open("docs/footer.md", "r") as f:
        footer = f.read()

    with open("README.md", "w") as f2:
        f2.write(f"{header}\n")

        profiles.sort(key=lambda x: x["name"].lower())

        for profile in profiles:
            f2.write(f"## {profile['name']} profile\n\n")

            if "settings" in profile:
                f2.write(f"```json\n{json.dumps(profile['settings'], indent=4)}\n```\n\n")

            categories = defaultdict(list)

            for extension in profile["extensions"]:
                category = extension.get("category", "")
                categories[category].append(extension)

            for category, extensions in sorted(categories.items()):
                if category:
                    f2.write(f"### {category}\n\n")

                extensions.sort(key=lambda x: x["name"].lower())

                for extension in extensions:
                    entry = f"- [{extension["name"]}]({base_extensions_url}?itemName={extension['id']})"
                    if "description" in extension:
                        entry += f": {extension['description']}"
                    if "settings" in extension:
                        entry += f"\n\n```json\n{json.dumps(extension['settings'], indent=4)}\n```\n"
                    f2.write(f"{entry}\n")
                f2.write("\n")

        f2.write(f"\n{footer}")
