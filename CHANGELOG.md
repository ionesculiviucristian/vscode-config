# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-06-09

- feat: add Windows support
- feat: add new profiles:
  - Go
  - Grafana
- feat: add new extensions:
  - EditorConfig
  - Python Environments
  - templ-vscode
- feat: replace Black Formatter, Flake8 and isort with Ruff
- feat: add support for Vim and Lua
- feat: add json schema validation for profiles and devcontainers
- feat: generate devcontainer profiles
- revert: remove unused or already covered by the editor extensions:
  - CSS Peek
  - Git Blame
  - Git History
  - Gremlins tracker for Visual Studio Code
  - Import Cost
  - JavaScript Booster
  - Learn Vim
- fix: take into account the version when installing extensions
- fix: add dedicated formatters for:
  - go
  - jsonnet
  - php
  - templ
  - toml
  - xml
  - yaml
- fix: replace unmaintained extensions:
  - Todo Tree with Better Todo Tree
  - Better Comments with Better Comments Next
- chore: update various profile settings:
  - prettier activates only when a `.prettierrc.json` is present
  - disable AI features
  - auto-save on focus change

## [1.0.1] - 2025-08-15

- revert: remove React profile and all snippet extensions
- feat: add Vue (legacy) profile

## [1.0.0] - 2025-08-06

- feat: initial release
