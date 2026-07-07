# BDH Linux 🐧⚡

> An Automated Environment Provisioning Tool for Backend Developers — Built on Arch/Manjaro.
> **"Install once — start coding immediately!"**

![PyPI](https://img.shields.io/pypi/v/bdh-linux)
![License](https://img.shields.io/github/license/BackendDeveloperHub/bdh-linux)
![Platform](https://img.shields.io/badge/platform-Arch%20%7C%20Manjaro-blue)

---

## 🚀 Overview

BDH Linux is a custom developer workspace and automated environment provisioning tool designed to eliminate the hassle of manual configuration. 

**Current Status (Phase 1):** It acts as an advanced automated setup script that securely transforms any fresh Manjaro/Arch system into a full, bloat-free backend workspace in minutes.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🎨 **Cyberpunk Theme** | Sleek dark terminal aesthetic for deep-focus coding |
| 🐍 **Pre-configured Stack** | Python 3.12+, FastAPI, and PostgreSQL ready out of the box |
| 🐳 **Dev Tools Included** | Docker, Git, Neovim, and other essential backend tools configured |
| 🤝 **BDH Custom ZSH** | Tailored shell with Oh My Zsh and Powerlevel10k for maximum productivity |
| ⚙️ **Built-in CLI** | Comes with `bdh-fastapi-new` (via `pipx`) for instant API scaffolding |
| ⌨️ **Power Aliases** | `serve`, `venv`, `gp` and other custom shortcuts to save time |
| ⚡ **Bloat-free OS** | Automated cleanup of bloatware (games, media apps) and orphaned packages |

---

## 🛠️ The Stack

- **Base OS:** Manjaro (Arch-based)
- **Shell:** Custom ZSH + Oh My Zsh
- **Language:** Python 3.12+
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **Containers:** Docker

---

## 📦 Quick Start

```bash
pip install bdh-linux
bdh setup
bdh-linux/
├── configs/      # ZSH settings, aliases, shell prompts
├── packages/     # Essential packages list
├── scripts/      # Automation & installation scripts
├── themes/       # Wallpapers & GTK theme configs
└── cli/          # PyPI CLI source code
👨‍💻 Author
​Prabakaran — BackendDeveloperHub
​GitHub: github.com/BackendDeveloperHub
​PyPI: bdh-linux
