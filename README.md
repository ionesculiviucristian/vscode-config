# VS Code config

```bash
# Install profiles
python manage_profiles.py --install

# Uninstall profiles
python manage_profiles.py --uninstall
```

## List of available profiles

### Enhanced profile

```json
{
    "editor.codeActionsOnSave": {
        "source.addMissingImports": "explicit"
    },
    "editor.fontFamily": "'JetBrainsMonoNL Nerd Font Mono', 'monospace', monospace",
    "editor.fontSize": 18,
    "editor.formatOnPaste": true,
    "editor.formatOnSave": true,
    "editor.linkedEditing": true,
    "editor.stickyScroll.enabled": false,
    "files.autoSave": "afterDelay",
    "files.insertFinalNewline": true,
    "git.enableSmartCommit": true,
    "git.openRepositoryInParentFolders": "always",
    "javascript.preferences.importModuleSpecifier": "non-relative",
    "typescript.preferences.importModuleSpecifier": "non-relative",
    "workbench.startupEditor": "none"
}
```

#### AI

- [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot): Your AI pair programmer
- [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat): AI chat features powered by Copilot

#### Diagnostic

- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens): Improve highlighting of errors, warnings and other language diagnostics

```json
{
    "errorLens.excludeBySource": [
        "cSpell"
    ]
}
```

- [Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost): Display import/require package size in the editor
- [Pretty TypeScript Errors](https://marketplace.visualstudio.com/items?itemName=yoavbls.pretty-ts-errors): Make TypeScript errors prettier and more human-readable in VSCode
- [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree): Show TODO, FIXME, etc. comment tags in a tree view

#### Docker

- [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack): An extension pack that lets you open any folder in a container, on a remote machine, or in WSL and take advantage of VS Code's full feature set

#### Git / Gitlab

- [Git Blame](https://marketplace.visualstudio.com/items?itemName=waderyan.gitblame): See git blame information in the status bar
- [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph): View a Git Graph of your repository, and perform Git actions from the graph
- [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory): View git log, file history, compare branches or commits

#### Linters / Formatters / Sorters

- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker): Spelling checker for source code

```json
{
    "cSpell.diagnosticLevel": "Hint"
}
```

- [DotENV](https://marketplace.visualstudio.com/items?itemName=mikestead.dotenv): Support for dotenv file syntax
- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint): Integrates ESLint JavaScript into VS Code

```json
{
    "editor.codeActionsOnSave": {
        "source.fixAll.eslint": "explicit"
    }
}
```

- [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml): Fully-featured TOML support
- [Gremlins tracker for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=nhoizey.gremlins): Reveals some characters that can be harmful because they are invisible or looking like legitimate ones. Inspired by Sublime Gremlins
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): All you need to write Markdown (keyboard shortcuts, table of contents, auto preview and more)
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint): Markdown linting and style checking for Visual Studio Code
- [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): Code formatter using prettier

```json
{
    "editor.defaultFormatter": "esbenp.prettier-vscode"
}
```

- [ShellCheck](https://marketplace.visualstudio.com/items?itemName=timonwong.shellcheck): Integrates ShellCheck into VS Code, a linter for Shell scripts
- [Sort JSON objects](https://marketplace.visualstudio.com/items?itemName=richie5um2.vscode-sort-json): Sorts the keys within JSON objects
- [Sort lines](https://marketplace.visualstudio.com/items?itemName=Tyriar.sort-lines): Sorts lines of text
- [Stylelint](https://marketplace.visualstudio.com/items?itemName=stylelint.vscode-stylelint): Official Stylelint extension for Visual Studio Code

```json
{
    "css.validate": false,
    "less.validate": false,
    "scss.validate": false
}
```

- [Text Power Tools](https://marketplace.visualstudio.com/items?itemName=qcz.text-power-tools): All-in-one solution with 240+ commands for text manipulation: filter lines (grep), remove lines, insert number sequences and GUIDs, sorting, change case, converting numbers, generating fake data and more
- [XML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml): XML Language Support by Red Hat
- [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml): YAML Language Support by Red Hat, with built-in Kubernetes syntax support

```json
{
    "redhat.telemetry.enabled": false
}
```

- [YAML Sort](https://marketplace.visualstudio.com/items?itemName=PascalReitermann93.vscode-yaml-sort): YAML Sort extends VS Code to sort, format and validate YAML files

```json
{
    "vscode-yaml-sort.forceQuotes": true,
    "vscode-yaml-sort.quotingType": "\"",
    "vscode-yaml-sort.sortArrays": true
}
```


#### Other

- [IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode): AI-assisted development
- [JavaScript Booster](https://marketplace.visualstudio.com/items?itemName=sburg.vscode-javascript-booster): Boost your productivity with advanced JavaScript/TypeScript refactorings and commands
- [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense): Visual Studio Code plugin that autocompletes filenames

```json
{
    "javascript.suggest.paths": false,
    "typescript.suggest.paths": false
}
```

- [SFTP](https://marketplace.visualstudio.com/items?itemName=Natizyskunk.sftp): SFTP/FTP sync

#### Snippets

- [JavaScript (ES6) code snippets](https://marketplace.visualstudio.com/items?itemName=xabikos.JavaScriptSnippets): Code snippets for JavaScript in ES6 syntax

#### Themes

- [Catppuccin for VSCode](https://marketplace.visualstudio.com/items?itemName=Catppuccin.catppuccin-vsc): Soothing pastel theme for VSCode

```json
{
    "editor.semanticHighlighting.enabled": true,
    "gopls": {
        "ui.semanticTokens": true
    },
    "terminal.integrated.minimumContrastRatio": 1,
    "window.titleBarStyle": "custom",
    "workbench.colorTheme": "Catppuccin Mocha"
}
```

- [Catppuccin Icons for VSCode](https://marketplace.visualstudio.com/items?itemName=Catppuccin.catppuccin-vsc-icons): Soothing pastel icon theme for VSCode

```json
{
    "workbench.iconTheme": "catppuccin-mocha"
}
```


### Experimental profile

#### Databases

- [MongoDB for VS Code](https://marketplace.visualstudio.com/items?itemName=mongodb.mongodb-vscode): Connect to MongoDB and Atlas directly from your VS Code environment, navigate your databases and collections, inspect your schema and use playgrounds to prototype queries and aggregations
- [SQLTools](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools): Connecting users to many of the most commonly used databases. Welcome to database management done right

#### Docker

- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker): Makes it easy to create, manage, and debug containerized applications

#### Git / Gitlab

- [GitHub Pull Requests](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github): Pull Request and Issue Provider for GitHub
- [GitLab Workflow](https://marketplace.visualstudio.com/items?itemName=GitLab.gitlab-workflow): Official GitLab-maintained extension for Visual Studio Code

#### Linters / Formatters / Sorters

- [Ansible](https://marketplace.visualstudio.com/items?itemName=redhat.ansible): Ansible language support
- [Format in context menus](https://marketplace.visualstudio.com/items?itemName=lacroixdavid1.vscode-format-context-menu): VSCode extension to format multiple files with right click context menu
- [Lua](https://marketplace.visualstudio.com/items?itemName=sumneko.lua): Lua Language Server coded by Lua

#### Other

- [Bookmarks](https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks): Mark lines and jump to them
- [CodeSnap](https://marketplace.visualstudio.com/items?itemName=adpyke.codesnap):  Take beautiful screenshots of your code
- [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio): This unofficial extension integrates Draw.io into VS Code
- [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig): EditorConfig Support for Visual Studio Code
- [Geo Data Viewer](https://marketplace.visualstudio.com/items?itemName=RandomFractalsInc.geo-data-viewer): Geo Data Analytics tool for VSCode IDE with kepler.gl support to generate and view maps
- [Hungry Delete](https://marketplace.visualstudio.com/items?itemName=jasonlhy.hungry-delete): To delete an entire block of whitespace or tab, and reduce the time programmers need to press backspace
- [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer): Launch a development local Server with live reload feature for static & dynamic pages
- [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare): Real-time collaborative development from the comfort of your favorite tools
- [MetaGo](https://marketplace.visualstudio.com/items?itemName=metaseed.metago): vscode cursor move and select; jump, navigation, goto, acejump
- [NPM](https://marketplace.visualstudio.com/items?itemName=idered.npm): Manage npm dependencies from sidebar. Supports npm, yarn, pnpm, bun
- [OpenAPI (Swagger) Editor](https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi): OpenAPI editing, validation and preview in VS Code
- [Peacock](https://marketplace.visualstudio.com/items?itemName=johnpapa.vscode-peacock): Subtly change the workspace color of your workspace. Ideal when you have multiple VS Code instances and you want to quickly identify which is which
- [PlantUML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml): Rich PlantUML support for Visual Studio Code
- [Project Manager](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager): Easily switch between projects

### PHP profile

```json
{
    "[php]": {
        "editor.wordSeparators": "`~!@#%^&*()-=+[{]}\\|;:'\",.<>/?"
    }
}
```

- [Composer](https://marketplace.visualstudio.com/items?itemName=DEVSENSE.composer-php-vscode): All-in-One composer integration, quick actions, commands, automatic installation, tasks, code lenses, diagnostics, and composer.json IntelliSense
- [PHP Awesome Snippets](https://marketplace.visualstudio.com/items?itemName=hakcorp.php-awesome-snippets): A fullset of snippets for PHP devs to boost coding productivity
- [PHP Debug](https://marketplace.visualstudio.com/items?itemName=xdebug.php-debug): Debug support for PHP with Xdebug
- [PHP Intelephense](https://marketplace.visualstudio.com/items?itemName=bmewburn.vscode-intelephense-client): PHP code intelligence for Visual Studio Code

```json
{
    "[php]": {
        "editor.defaultFormatter": "bmewburn.vscode-intelephense-client"
    }
}
```


### Python profile

```json
{
    "[python]": {
        "editor.codeActionsOnSave": {
            "source.organizeImports": "always"
        },
        "editor.defaultFormatter": null,
        "terminal.activateEnvironment": false
    }
}
```

- [Better Jinja](https://marketplace.visualstudio.com/items?itemName=samuelcolvin.jinjahtml): Syntax highlighting for jinja(2) including HTML, Markdown, YAML, Ruby and LaTeX templates
- [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter): Formatting support for Python files using the Black formatter

```json
{
    "black-formatter.args": [
        "--line-length",
        "120"
    ]
}
```

- [Flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8): Linting support for Python files using Flake8

```json
{
    "flake8.args": [
        "--max-line-length=120"
    ]
}
```

- [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort): Import organization support for Python files using isort

```json
{
    "isort.args": [
        "--profile",
        "black"
    ]
}
```

- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance): A performant, feature-rich language server for Python in VS Code
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python): Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more

### React profile

- [ES7+ React/Redux/React-Native snippets](https://marketplace.visualstudio.com/items?itemName=dsznajder.es7-react-js-snippets): Extensions for React, React-Native and Redux in JS/TS with ES7+ syntax. Customizable. Built-in integration with prettier

### Vue profile

```json
{
    "[vue]": {
        "editor.codeActionsOnSave": {
            "source.addMissingImports": "never"
        }
    }
}
```

- [Vue - Official](https://marketplace.visualstudio.com/items?itemName=Vue.volar): Language Support for Vue


## Additional notes

Install pre commit hooks

```bash
pip install pre-commit
pre-commit install
```
