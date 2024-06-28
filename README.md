# Visual Studio Code settings & profiles

```bash
# Install prerequisites
# Arch based distros
sudo pacman -Syu jq
# Debian based distros
sudo apt install jq

# Add Ollama LLMs
curl -fsSL https://ollama.com/install.sh | sh
ollama pull starcoder2:3b
ollama pull llama3:8b
cp ./configs/continue.json ~/.continue/config.json

# Fire it up!
./install
```

## Profiles

- Extended

  - Docker
    - [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
    - [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
  - Git / Gitlab
    - [GitLab Workflow](https://marketplace.visualstudio.com/items?itemName=GitLab.gitlab-workflow)
    - [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
    - [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory)
    - [Git Blame](https://marketplace.visualstudio.com/items?itemName=waderyan.gitblame)
  - Linter / Formatters
    - [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)
    - [Dotenv Official +Vault](https://marketplace.visualstudio.com/items?itemName=dotenv.dotenv-vscode)
    - [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
    - [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml)
    - [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint)
    - [Prettier - Code formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
  - Others
    - [Bookmarks](https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks)
    - [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)
    - [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
    - [Import Cost](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost)
    - [IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode)
    - [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
    - [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)
    - [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
    - [NPM](https://marketplace.visualstudio.com/items?itemName=idered.npm)
    - [Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense)
    - [PlantUML](https://marketplace.visualstudio.com/items?itemName=jebbs.plantuml)
    - [Pretty TypeScript Errors](https://marketplace.visualstudio.com/items?itemName=yoavbls.pretty-ts-errors)
    - [Project Manager](https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager)
    - [SFTP](https://marketplace.visualstudio.com/items?itemName=Natizyskunk.sftp)
    - [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)
    - [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree)
    - [Continue - Codestral, GPT-4o, and more](https://marketplace.visualstudio.com/items?itemName=Continue.continue)
  - Snippets
    - [JavaScript (ES6) code snippets](https://marketplace.visualstudio.com/items?itemName=xabikos.JavaScriptSnippets)
  - Themes
    - [GitHub Theme](https://marketplace.visualstudio.com/items?itemName=GitHub.github-vscode-theme)
    - [Material Icon Theme](https://marketplace.visualstudio.com/items?itemName=PKief.material-icon-theme)

- Experimental
  - [Ansible](https://marketplace.visualstudio.com/items?itemName=redhat.ansible)
  - [CodeSnap](https://marketplace.visualstudio.com/items?itemName=adpyke.codesnap)
  - [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)
  - [Geo Data Viewer](https://marketplace.visualstudio.com/items?itemName=RandomFractalsInc.geo-data-viewer)
  - [Lua](https://marketplace.visualstudio.com/items?itemName=sumneko.lua)
  - [MongoDB for VS Code](https://marketplace.visualstudio.com/items?itemName=mongodb.mongodb-vscode)
  - [OpenAPI (Swagger) Editor](https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi)
  - [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
  - [SQLTools](https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools)
  - [Text Power Tools](https://marketplace.visualstudio.com/items?itemName=qcz.text-power-tools)
  - [XML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml)
- php
  - [Composer](https://marketplace.visualstudio.com/items?itemName=DEVSENSE.composer-php-vscode)
  - [PHP Awesome Snippets](https://marketplace.visualstudio.com/items?itemName=hakcorp.php-awesome-snippets)
  - [PHP Debug](https://marketplace.visualstudio.com/items?itemName=xdebug.php-debug)
  - [PHP Intelephense](https://marketplace.visualstudio.com/items?itemName=bmewburn.vscode-intelephense-client)
- Python
  - [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
  - [Flake8](https://marketplace.visualstudio.com/items?itemName=ms-python.flake8)
  - [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
  - [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)
- Vue
  - [Vue - Official](https://marketplace.visualstudio.com/items?itemName=Vue.volar)

## Testing scenarios

### HTML/CSS/JavaScript/TypeScript/Vue (Vuetify)

```bash
# Install Vuetify prerequisites
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
nvm install 20
nvm use 20

# Create a new Vuetify project
cd ~/Projects
npm create vuetify

# Open the project
code --profile Vue ~/Projects/vuetify-app

# Start serving the app
cd ~/Projects/vuetify-app
npm run dev
```

### Python (Django)

```bash
# Install Django prerequisites
sudo pacman -Syu python-django
curl -sSL https://install.python-poetry.org | python3 -

# Create a new Django project
cd ~/Projects
django-admin startproject django_app
poetry init --no-interaction
poetry config --local virtualenvs.in-project true
poetry add django

# Open the project
code --profile Python ~/Projects/django_app

# Start serving the app
cd ~/Projects/django_app
poetry run python manage.py runserver
```

### php (Laravel)

```bash
# Install Laravel prerequisites
sudo pacman -Syu php
echo 'extension=pdo_sqlite' | sudo tee /etc/php/conf.d/extensions.ini

# Install composer
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('sha384', 'composer-setup.php') === 'dac665fdc30fdd8ec78b38b9800061b4150413ff2e3b6f88543c636f7cd84f6db9189d43a81e5503cda447da73c7e5b6') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"
sudo mv composer.phar /usr/local/bin/composer

# Create a new Laravel project
composer create-project laravel/laravel ~/Projects/laravel-app

# Open the project
code --profile php ~/Projects/laravel-app

# Start serving the app
cd ~/Projects/laravel-app
php artisan serve
```
