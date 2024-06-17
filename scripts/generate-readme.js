import fs from "fs";
import ejs from "ejs";

let profiles = JSON.parse(fs.readFileSync("./data/profiles.json", "utf-8"));

const formatSettings = (settings) =>
  `\n\`\`\`json\n${JSON.stringify(settings, null, 2)}\n\`\`\``;

const sortExtensions = (a, b) => a.name.toLowerCase().localeCompare(b.name);

const slugify = (text) =>
  text
    .trim()
    .toLowerCase()
    .replace(/[^\w\s-]/g, "")
    .replace(/\s+/g, "-");

const sortProfiles = (a, b) => a.name.toLowerCase().localeCompare(b.name);

profiles = profiles.sort(sortProfiles).map((profile) => ({
  ...profile,
  settings: profile.settings ? formatSettings(profile.settings) : "",
  extensions: profile.extensions.sort(sortExtensions).map((extension) => ({
    ...extension,
    url: `https://marketplace.visualstudio.com/items?itemName=${extension.id}`,
    settings: extension.settings ? formatSettings(extension.settings) : "",
  })),
}));

ejs.renderFile(
  "./docs/readme/README.ejs",
  { profiles, slugify },
  {},
  function (err, str) {
    if (err) {
      console.error(err);
      return;
    }
    fs.writeFileSync("README.md", str, "utf-8");
  }
);
