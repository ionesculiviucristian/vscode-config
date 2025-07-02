import fs from "fs";
import ejs from "ejs";

let profiles = JSON.parse(fs.readFileSync("./profiles.json", "utf-8"));

const sortProfiles = (a, b) => a.name.toLowerCase().localeCompare(b.name);
const sortExtensions = (a, b) => a.name.toLowerCase().localeCompare(b.name);

profiles = profiles.map((profile) => ({
  ...profile,
  settings: profile.settings
    ? `\n\`\`\`json\n${JSON.stringify(profile.settings, null, 2)}\n\`\`\``
    : "",
}));

ejs.renderFile(
  "./readme/README.ejs",
  { profiles, sortProfiles, sortExtensions },
  {},
  function (err, str) {
    if (err) {
      console.error(err);
      return;
    }
    fs.writeFileSync("README.md", str, "utf-8");
  }
);
