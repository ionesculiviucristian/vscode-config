# Visual Studio Code settings & profiles

```bash
# Install prerequisites
sudo pacman -Syu jq

# Fire it up!
./install
```

## Profiles

- Extended
  - "github.github-vscode-theme"
  - "esbenp.prettier-vscode"
  - "pkief.material-icon-theme"
  - "ms-azuretools.vscode-docker"
  - "dotenv.dotenv-vscode"
  - "idered.npm"
  - "dbaeumer.vscode-eslint"
  - "ruakr.ftp-kr"
  - "editorconfig.editorconfig"
  - "wix.vscode-import-cost"
  - "tamasfe.even-better-toml"
  - "ritwickdey.LiveServer"
  - "VisualStudioExptTeam.vscodeintellicode"
  - "MS-vsliveshare.vsliveshare"
  - "streetsidesoftware.code-spell-checker"
  - "alefragnani.project-manager"
  - "GitLab.gitlab-workflow"
  - "alefragnani.Bookmarks"
  - "xabikos.JavaScriptSnippets"
  - "yzhang.markdown-all-in-one"
  - "mongodb.mongodb-vscode
  - "jebbs.plantuml"
  - "hediet.vscode-drawio"
  - "humao.rest-client"
  - "christian-kohler.path-intellisense"
  - "eamodio.gitlens"
- Python
  - "ms-python.python"
  - "ms-python.vscode-pylance"
  - "ms-python.flake8"
  - "ms-python.black-formatter"
  - "ms-python.isort"
- php
  - "xdebug.php-debug"
  - "bmewburn.vscode-intelephense-client"
  - "DEVSENSE.composer-php-vscode"
  - "hakcorp.php-awesome-snippets"

## Testing scenarios

#### HTML/CSS/JavaScript/TypeScript/Vue (Vuetify)

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

#### Python (Django)

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

#### php (Laravel)

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
