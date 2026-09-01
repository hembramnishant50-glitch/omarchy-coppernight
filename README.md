<div align="center">

```
 _____                                             _   _   _           _       _
/  __ \                                           | \ | | (_)         | |     | |
| /  \/   ___    _ __    _ __     ___   _ __      |  \| |  _    __ _  | |__   | |_
| |      / _ \  | '_ \  | '_ \   / _ \ | '__|     | . ` | | |  / _` | | '_ \  | __|
| \__/\ | (_) | | |_) | | |_) | |  __/ | |        | |\  | | | | (_| | | | | | | |_
 \____/  \___/  | .__/  | .__/   \___| |_|        \_| \_/ |_|  \__, | |_| |_|  \__|
                | |     | |                                     __/ |
                |_|     |_|                                    |___/
```

# 🌌 Copper Night

### *An Elegant, Deep Indigo & Glowing Copper Theme for Omarchy Quattro*

> *"Where the deep indigo of Tokyo meets the warm, radiant glow of an ember sunset."*

<br/>

[![Version](https://img.shields.io/badge/Version-2.0.0-fab387?style=for-the-badge&logo=git&logoColor=11111b)](https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme)
[![Omarchy Quattro](https://img.shields.io/badge/Omarchy-Quattro-89b4fa?style=for-the-badge&logo=archlinux&logoColor=11111b)](https://omarchy.org/)
[![Hyprland](https://img.shields.io/badge/Hyprland-Ready-a6e3a1?style=for-the-badge&logo=hyprland&logoColor=11111b)](https://hyprland.org)
[![License](https://img.shields.io/badge/License-MIT-f5c2e7?style=for-the-badge&logo=opensourceinitiative&logoColor=11111b)](LICENSE)
[![Stars](https://img.shields.io/github/stars/hembramnishant50-glitch/omarchy-coppernight-theme?style=for-the-badge&color=cba6f7&logo=github&logoColor=11111b)](https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme/stargazers)

<br/>

<a href="#-theme-files">
  <img width="100%" alt="Copper Night Hero Preview" src="https://github.com/user-attachments/assets/1123edd2-2feb-484f-ad2f-b2e7cad416d0" style="border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.5);" />
</a>

<br/>

[✨ Features](#-features) • [⚡ Installation](#-installation) • [📁 Theme Files](#-theme-files) • [🎨 Color Palette](#-color-palette) • [🌐 Web Styles](#-web-userstyles) • [💻 Terminals](#-terminals) • [📦 Editors & Shell](#-editors--shell) • [🚀 Launchers & UI](#-launchers--ui) • [📬 Notifications & OSD](#-notifications--osd) • [🔒 Lock Screen](#-lock-screen)

</div>

---

## ⚡ Installation

Install and apply the theme with one command in **Omarchy**:

```bash
omarchy-theme-install https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme.git
```

To switch to Copper Night anytime:

```bash
omarchy theme set coppernight
```

---

## ✨ Features

- 🌑 **Ultra-Deep Indigo Canvas** (`#11111b`) with smooth contrast and eye-comfort tuning.
- 🌅 **Warm Copper-Orange Accents** (`#fab387`) for borders, focused windows, and primary highlights.
- 🎨 **Pastel Accent Hierarchy** featuring Lite Green (`#a6e3a1`), Lite Pink (`#f5c2e7`), Sky Blue (`#89b4fa`), and Mauve (`#cba6f7`).
- 🪟 **Omarchy Quattro Hyprland Settings** with 14px rounded corners, dual-layer glow borders, active blur (size 6, passes 3), and custom bezier animations (`overshot`, `smoothOut`).
- 💻 **Cross-Terminal Theming** for Alacritty, Ghostty, Foot, and Kitty (all cleaned of hardcoded Catppuccin colors).
- 🌐 **136+ Universal Web Userstyles** via [Stylus.json](Stylus.json) covering YouTube, GitHub, Crunchyroll, CareerWill, Claude, ChatGPT, and more.
- 📊 **Fully-Themed Apps**: Neovim, VSCode, BTOP, GTK 3/4, Chromium flags, and Icon set.
- 🎵 **Discord Vencord Theme** with Coppernight palette.

---

## 📁 Theme Files

<div align="center">

| File | Size | Description |
|------|------|-----------|
| `colors.toml` | 685B | Master palette (background `#11111b`, accent `#fab387`) |
| `hyprland.lua` | 2.2KB | Hyprland WM config (rounding=14, blur, shadows, animations) |
| `gtk.css` | 2.7KB | GTK theming with `border-radius: 14px` |
| `Stylus.json` | 2.7MB | 136+ web userstyles for Chrome/Firefox |
| `youtube-coppernight.user.less` | 19KB | YouTube userstyle |
| `btop.theme` | 1.5KB | BTOP diagnostic monitor colors |
| `neovim.lua` | 156B | Neovim tokyonight colorscheme |
| `vscode.json` | 78B | VSCode theme linkage |
| `alacritty.toml` | 809B | Terminal config (Catppuccin removed) |
| `kitty.conf` | 468B | Terminal config (Catppuccin removed) |
| `ghostty.conf` | 467B | Terminal config (Catppuccin removed) |
| `foot.ini` | 387B | Terminal config (Catppuccin removed) |
| `starship.toml` | 1.1KB | Prompt theme |
| `config.fish` | 1.5KB | Fish shell config |
| `helix.toml` | 4.7KB | Helix editor theme |
| `fastfetch.jsonc` | 3.5KB | Fastfetch system info |
| `cava_theme` | 278B | CAVA visualizer config |
| `vencord.theme.css` | 223B | Discord Vencord theme |
| `ghostty_override.conf` | 1.3KB | Ghostty config override |

</div>

---

## 🎨 Color Palette

<div align="center">

| Swatch | Token | Hex Code | Role & Description |
|:---:|:---|:---:|:---|
| ![#11111b](https://img.shields.io/badge/-%2311111b-11111b?style=flat-square) | **Base / Background** | `#11111b` | Main application & window background |
| ![#181825](https://img.shields.io/badge/-%23181825-181825?style=flat-square) | **Mantle** | `#181825` | Sidebars, panels, and dropdown containers |
| ![#313244](https://img.shields.io/badge/-%23313244-313244?style=flat-square) | **Surface0** | `#313244` | Cards, input fields, inactive borders |
| ![#fab387](https://img.shields.io/badge/-%23fab387-fab387?style=flat-square) | **Copper (Accent)** | `#fab387` | Active borders, focused items, primary fonts |
| ![#cdd6f4](https://img.shields.io/badge/-%23cdd6f4-cdd6f4?style=flat-square) | **Foreground / Text** | `#cdd6f4` | Standard readable text & icons |
| ![#a6e3a1](https://img.shields.io/badge/-%23a6e3a1-a6e3a1?style=flat-square) | **Lite Green** | `#a6e3a1` | Success indicators, strings, active states |
| ![#f5c2e7](https://img.shields.io/badge/-%23f5c2e7-f5c2e7?style=flat-square) | **Lite Pink** | `#f5c2e7` | Special accents, tags, badges, highlights |
| ![#89b4fa](https://img.shields.io/badge/-%2389b4fa-89b4fa?style=flat-square) | **Lite Blue** | `#89b4fa` | URLs, functions, keywords, info dialogs |
| ![#cba6f7](https://img.shields.io/badge/-%23cba6f7-cba6f7?style=flat-square) | **Mauve** | `#cba6f7` | Secondary accent, syntax keywords, operators |
| ![#f38ba8](https://img.shields.io/badge/-%23f38ba8-f38ba8?style=flat-square) | **Red** | `#f38ba8` | Warnings, errors, deletions, critical notices |

</div>

---

## 📁 Theme Structure

```
~/.config/omarchy/themes/coppernight/
├── colors.toml             # Master palette definition
├── hyprland.lua           # Hyprland WM layout, animations & rounding
├── btop.theme             # BTOP diagnostic monitor colors
├── gtk.css                # GTK 3 / GTK 4 interface stylings
├── chromium.theme         # Chromium / Chrome dark flags
├── icons.theme            # Icon pack configuration
├── neovim.lua             # Neovim TokyoNight / Copper colors
├── vscode.json            # VSCode theme linkage
├── Stylus.json            # 136+ browser userstyles backup
├── youtube-coppernight.user.less  # Standalone YouTube Less theme
├── vite.css               # (placeholder for future use)
├── backgrounds/           # High-resolution themed wallpapers (5 images)
├── README.md              # Full theme documentation
├── alacritty.toml         # Terminal config
├── kitty.conf             # Terminal config
├── ghostty.conf           # Terminal config
├── foot.ini               # Terminal config
├── neovim.lua             # Editor config
├── vscode.json            # VSCode theme linkage
├── starship.toml          # Prompt theme
├── config.fish            # Fish shell config
├── helix.toml             # Editor config
├── fastfetch.jsonc        # Fastfetch system info
├── cava_theme             # CAVA visualizer config
├── vencord.theme.css      # Discord Vencord theme
├── ghostty_override.conf  # Ghostty config override
```

---

## 🤝 Contributing

> Love Omarchy? Love Copper Night? Contributions make it shine brighter ✨

We welcome **bug reports**, **new website userstyles**, **wallpapers**, and **UI polish** — every idea counts!

### How to Contribute

1. 🍴 **Fork** this repository
2. 🌿 Create your branch — `git checkout -b feature/my-awesome-tweak`
3. 💾 Commit — `git commit -m 'feat: add my awesome tweak'`
4. 🚀 Push — `git push origin feature/my-awesome-tweak`
5. 🔃 Open a **Pull Request** — describe your change with a preview if possible

Found a bug? Open an [Issue](https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme/issues) — we reply fast 💬

---

---

<div align="center">

### 💖 Crafted with Passion by [Nishant](https://github.com/hembramnishant50-glitch) — with Love for [Omarchy](https://omarchy.org/) 🥰

*“Night falls on Tokyo, lit by an eternal copper spark — made for the Omarchy family, by the Omarchy family.”*  
*Thank you to the Omarchy community for the inspiration, the tools, and the endless rice love 🌸*

<br/>

[![Stars](https://img.shields.io/github/stars/hembramnishant50-glitch/omarchy-coppernight-theme?style=social)](https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme)

</div>