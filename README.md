<div align="center">

```
 ██████╗  ██████╗ ██████╗  ██████╗  ███████╗ ██████╗     ███╗   ██╗ ██╗  ██████╗ ██╗  ██╗ ████████╗
██╔════╝ ██╔═══██╗ ██╔══██╗ ██╔══██╗ ██╔════╝ ██╔══██╗    ████╗  ██║ ██║ ██╔════╝ ██║  ██║ ╚══██╔══╝
██║      ██║   ██║ ██████╔╝ ██████╔╝ █████╗   ██████╔╝    ██╔██╗ ██║ ██║ ██║  ███╗ ███████║    ██║
██║      ██║   ██║ ██╔═══╝  ██╔═══╝  ██╔══╝   ██╔══██╗    ██║╚██╗██║ ██║ ██║   ██║ ██╔══██║    ██║
╚██████╗ ╚██████╔╝ ██║      ██║      ███████╗ ██║  ██║    ██║ ╚████║ ██║ ╚██████╔╝ ██║  ██║    ██║
 ╚═════╝  ╚═════╝ ╚═╝      ╚═╝      ╚══════╝ ╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝
```

# 🌌 Copper Night

> *"Where the deep indigo of Tokyo meets the warm glow of an ember sunset."*

A high-performance **Hyprland** rice for **Omarchy** — a **Tokyo Night** palette  
kissed by a **Copper-Orange** border that glows like a setting sun.

<br>

[![Version](https://img.shields.io/badge/version-1.2-C87941?style=for-the-badge&logo=git&logoColor=white)](https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme)
[![License](https://img.shields.io/badge/license-MIT-7AA2F7?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Hyprland](https://img.shields.io/badge/Hyprland-Rice-565f89?style=for-the-badge&logo=archlinux&logoColor=white)](https://hyprland.org)
[![Omarchy](https://img.shields.io/badge/Made%20for-Omarchy-1E1E2E?style=for-the-badge&logo=archlinux&logoColor=white)](https://omarchy.org/)
[![Stars](https://img.shields.io/github/stars/hembramnishant50-glitch/omarchy-coppernight-theme?style=for-the-badge&color=BB9AF7&logo=starship&logoColor=white)](https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme/stargazers)

</div>

---

<div align="center">

<img src="preview.png" width="100%" alt="Copper Night desktop preview">

</div>

---

## ▸ 📸 Gallery

<div align="center">

| | |
|:---:|:---:|
| <img src="https://github.com/user-attachments/assets/74b6b030-6181-4f01-a142-0a56e4046b14" width="100%"> | <img src="https://github.com/user-attachments/assets/94cdb423-e93f-4498-9f0c-a60f7ba3ed0f" width="100%"> |
| <img src="https://github.com/user-attachments/assets/10b7736e-0035-4659-aec4-eff0d3d2fa01" width="100%"> | <img src="https://github.com/user-attachments/assets/16bef38a-b05b-4b98-8da7-eb614974d2d3" width="100%"> |
| <img src="https://github.com/user-attachments/assets/cfb9a3e2-c1ba-4a9c-ac66-248c5705d8eb" width="100%"> | <img src="https://github.com/user-attachments/assets/ab64aa85-bfb6-4b89-8574-3a6e83230cc0" width="100%"> |
| <img src="https://github.com/user-attachments/assets/ccf2cc6d-b891-4ec3-9605-a2d1805fff1b" width="100%"> | <img src="https://github.com/user-attachments/assets/d6114edb-e239-4f6e-8fdd-85d7b54e4ece" width="100%"> |

</div>

---

## ▸ ⚡ Install

```
$ omarchy-theme-install https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme.git
```

### Then add Waybar *(optional)*

> [!NOTE]
> Your existing Waybar config is automatically backed up before anything is changed.

```bash
# Install dependencies
sudo pacman -S --needed python-requests python-psutil networkmanager \
  papirus-icon-theme pavucontrol bc zenity jq curl
sudo systemctl enable --now NetworkManager
pip install psutil

# Backup existing Waybar config
if [ -d ~/.config/waybar ]; then
    BACKUP_NAME="waybar-backup-$(date +%d-%m-%Y)-$RANDOM"
    mv ~/.config/waybar ~/.config/"$BACKUP_NAME"
    echo "Backed up to ~/.config/$BACKUP_NAME"
fi

# Apply Copper Night Waybar
mkdir -p ~/.config/waybar
SOURCE_DIR="$HOME/.config/omarchy/current/theme/waybar"

if [ -d "$SOURCE_DIR" ]; then
    cp -r "$SOURCE_DIR"/* ~/.config/waybar/

    if [ -d ~/.config/waybar/scripts ]; then
        chmod +x ~/.config/waybar/scripts/*
        # Force system Python to prevent environment conflicts
        find ~/.config/waybar/scripts -type f -name "*.py" \
          -exec sed -i '1s|^#!/usr/bin/env python3|#!/usr/bin/python3|' {} +
    fi
fi

# Apply Papirus Dark icons & restart Waybar
gsettings set org.gnome.desktop.interface icon-theme 'Papirus-Dark'
killall -q waybar; nohup waybar > /dev/null 2>&1 &
```

---

## ▸ 🪟 Waybar — Pick a Variant

> [!WARNING]
> All variants require the theme install above (and **Step 2** for the default Waybar).

```
  1) Default             → pre-installed with the theme
  2) Pill Style          → EXTRA/WAYBARS/waybar-1 · ./Setup-Waybar.sh
  3) Ember Arc           → EXTRA/WAYBARS/waybar-2 · ./waybar-setup.sh
  4) Pastel Capsule      → EXTRA/WAYBARS/waybar-3 · ./waybar-setup.sh
  5) Catppuccin Capsule  → EXTRA/WAYBARS/waybar-4 · ./waybar-setup.sh
```

### 1 · Default Waybar

<div align="center">
<img width="1920" height="55" alt="Default Waybar" src="https://github.com/user-attachments/assets/2aab9a8e-2bed-45e9-ab6b-a2c2e6c51d77" />
<p><em>Clean and minimal — ships out of the box with the full install.</em></p>
</div>

### 2 · Waybar-1 — Pill Style

<div align="center">
<img width="1920" height="78" alt="Waybar-1 Pill Style" src="https://github.com/user-attachments/assets/05fd9edb-4d6b-4f5b-8fd4-56a004b1c428">
<p><em>Neon pill borders · Rounded segments · Compact & clean</em></p>
</div>

```bash
cd ~/.config/omarchy/current/theme/EXTRA/WAYBARS/waybar-1 \
  && chmod +x Setup-Waybar.sh && ./Setup-Waybar.sh \
  && chmod +x ~/.config/waybar/scripts/*
```

### 3 · Waybar-2 — Ember Arc

<div align="center">
<img width="1917" height="76" alt="Waybar-2 Ember Arc" src="https://github.com/user-attachments/assets/72af47f3-be44-4c73-bca3-d028735b69c0" />
<p><em>Copper warmth · Floating arcs · Glows like a setting sun</em></p>
</div>

```bash
cd ~/.config/omarchy/current/theme/EXTRA/WAYBARS/waybar-2 \
  && chmod +x waybar-setup.sh && ./waybar-setup.sh
```

### 4 · Waybar-3 — Pastel Capsule

<div align="center">
<img width="1917" height="76" alt="Waybar-3 Pastel Capsule" src="https://github.com/user-attachments/assets/a7b5d807-249c-4641-bad3-f6b2a8c113ea" />
<p><em>Neon pastel · Rounded capsules · Floating in a dark sky</em></p>
</div>

```bash
cd ~/.config/omarchy/current/theme/EXTRA/WAYBARS/waybar-3 \
  && chmod +x waybar-setup.sh && ./waybar-setup.sh
```

### 5 · Waybar-4 — Catppuccin Mocha Capsule

<div align="center">
<img width="1920" height="57" alt="Waybar-4 Catppuccin Mocha Capsule" src="https://github.com/user-attachments/assets/71e5fc69-c0f0-43d9-ad9c-d9782941b0ed" />
<p><em>Catppuccin Mocha · Copper borders · Rounded capsules with workspace circles</em></p>
</div>

```bash
cd ~/.config/omarchy/current/theme/EXTRA/WAYBARS/waybar-4 \
  && chmod +x waybar-setup.sh && ./waybar-setup.sh
```

---

## ▸ 🌤️ Weather Widget

No more editing scripts. **One click** updates your city.

```
click →  type city  →  enter
  🌡️     "London"     ✓ done
  ☀️     "Tokyo"      ✓ saved
  🌧️     "Patna"      ✓ instant
```

> [!TIP]
> Your city is saved automatically. To refresh, click the icon again or run `killall waybar; waybar &`.

---

## ▸ 🔒 Lock Screen

<div align="center">

<img width="1311" height="737" alt="Hyprlock Preview" src="https://github.com/user-attachments/assets/86b69c94-6096-411f-a41e-4704c238f394" />

*Glassmorphism lock screen with live clock, random quotes, and media controls*

</div>

### Setup

> [!WARNING]
> Complete the theme install before running this.

```bash
# 1. Install Playerctl (required for media key support)
sudo pacman -S --needed playerctl

# 2. Fix Spotify media controls (Flatpak only)
if command -v flatpak &> /dev/null; then
    flatpak override --user \
      --talk-name=org.mpris.MediaPlayer2.spotify \
      com.spotify.Client
fi

# 3. Copy lock screen config files
mv ~/.config/hypr/hyprlock.conf ~/.config/hypr/hyprlock.conf-Backup && \
cp -r ~/.config/omarchy/current/theme/scripts \
      ~/.config/omarchy/current/theme/quotes.txt \
      ~/.config/omarchy/current/theme/hyprlock.conf \
      ~/.config/hypr/

# 4. Make scripts executable
chmod +x ~/.config/hypr/scripts/*
```

<details>
<summary><b>⚠️ Fix: Black Screen on Lock</b></summary>

If your screen goes black when locking, apply this quick fix.

**1. Open the file:**

```bash
nano ~/.local/share/omarchy/bin/omarchy-system-lock
```

**2. Find this line at the bottom:**

```bash
omarchy-brightness-display off
```

**3. Comment it out by adding `#` at the start:**

```bash
# omarchy-brightness-display off
```

**4. Save and exit:** `Ctrl+O` → `Enter` → `Ctrl+X`

</details>

### Customize

```bash
nano ~/.config/omarchy/current/theme/hyprlock.conf
```

```ini
# Wallpaper
background {
    monitor =
    path = /home/YOUR_USER/Pictures/your-wallpaper.jpg
    blur_passes = 3   # 0 = sharp · 3 = soft glass · 5+ = dreamy
    blur_size   = 7
}

# Profile Picture
image {
    monitor =
    path = /home/YOUR_USER/Pictures/your-avatar.png
    size = 150
}
```

| `blur_passes` | Effect |
|:---:|:---|
| `0` | Sharp — no blur |
| `2` | Subtle — light frost |
| `3` | Standard — soft glass |
| `5+` | Heavy — dreamy glow |

### Restore the original

```bash
rm ~/.config/hypr/hyprlock.conf \
  && mv ~/.config/hypr/hyprlock.conf-Backup ~/.config/hypr/hyprlock.conf
```

---

## ▸ ✨ Features

`◆ = enabled out of the box`

| | Feature | What you get |
|:---:|:---|:---|
| ◆ | **Wallpaper** | Traditional Japanese Pixel Art Pagoda — handpicked for the aesthetic |
| ◆ | **Widgets** | Floating diagnostic panels with custom animated resource bars |
| ◆ | **Color Palette** | Deep Indigos · Electric Magentas · Warm Copper-Orange accents |
| ◆ | **Weather Widget** | Live weather with click-to-change city — no script editing needed |
| ◆ | **Lock Screen** | Glassmorphism Hyprlock with blur, quotes, and media controls |
| ◆ | **Media Controls** | Playerctl integration with full Spotify Flatpak support |
| ◆ | **5 Waybar Variants** | Pick your vibe — Default, Pill, Ember Arc, Pastel, Catppuccin |

---

## ▸ 🗂️ Theme Files

One install themes your **entire desktop** — here's the layout:

```
~/.config/omarchy/current/theme/
├── hyprland.conf          Hyprland WM
├── hyprlock.conf          Lock screen
├── waybar/                Waybar · 5 variants
├── mako.ini               Notifications
├── swayosd.css            On-screen display
├── walker.css             App launcher
├── wofi.css               Wofi launcher
├── gtk.css                GTK apps
├── alacritty.toml         Terminal
├── kitty.conf             Terminal
├── ghostty.conf           Terminal
├── foot.ini               Terminal
├── warp.yaml              Terminal
├── gum.env.conf           Gum styling
├── neovim.lua             Editor
├── helix.toml             Editor
├── vscode_colors.json     VSCode
├── obsidian.css           Obsidian
├── vencord.theme.css      Discord
├── tokyo-night.theme.css  Discord · Tokyo Night
├── theme.override.css     Browser
├── chromium.theme         Chromium flags
├── btop.theme             Btop
├── cava_theme             Cava
├── keyboard.rgb           RGB keyboard color
├── icons.theme            Papirus-Dark icons
├── quotes.txt             Lock screen quotes
├── scripts/               Lock screen helpers
└── backgrounds/           5 wallpapers
```

---

## ▸ 🎨 Color Palette

<div align="center">

| Background | Deep Indigo | Electric Blue | Magenta | Copper-Orange | Foreground |
|:---:|:---:|:---:|:---:|:---:|:---:|
| ![](https://placehold.co/48x20/11111b/11111b) | ![](https://placehold.co/48x20/565f89/565f89) | ![](https://placehold.co/48x20/7aa2f7/7aa2f7) | ![](https://placehold.co/48x20/bb9af7/bb9af7) | ![](https://placehold.co/48x20/fab387/fab387) | ![](https://placehold.co/48x20/c0caf5/c0caf5) |
| `#11111b` | `#565f89` | `#7aa2f7` | `#bb9af7` | `#fab387` | `#c0caf5` |

</div>

> 💡 **Copper-Orange** `#fab387` is the signature accent — it glows through window borders, Waybar modules, and the lock screen.

---

## ▸ 🖼️ Wallpapers

> [!NOTE]
> All wallpapers ship with the theme, optimized for dark desktop aesthetics.

### 🌙 Featured — Cats at Moonrise

<div align="center">

<img src="backgrounds/cats-anime.jpg" width="100%" alt="Cats at Moonrise">

*Five cats perched before a copper sunset — the spirit of Copper Night in one frame.*

</div>

<div align="center">

| | |
|:---:|:---:|
| <img src="backgrounds/Character with Glowing Eyes and Katana.jpg" width="100%" alt="The Last Swordsman"> | <img src="backgrounds/Girl with Hannya Mask.jpeg" width="100%" alt="Girl and Hannya"> |
| ⚔️ **The Last Swordsman** · *Dark Fantasy* | 👺 **Girl & Hannya** · *Monochrome Yokai* |
| <img src="backgrounds/japanese-castle-pixel-digital-art.jpg" width="100%" alt="Mountain Castle"> | <img src="backgrounds/Itachi Uchiha.jpg" width="100%" alt="Itachi and The Crows"> |
| 🏯 **Mountain Castle** · *Pixel Art* | 🪶 **Itachi & The Crows** · *Akatsuki* |

</div>

| Wallpaper | File | Style | Resolution |
|:---|:---|:---|:---:|
| 🐱 Cats at Moonrise | `backgrounds/cats-anime.jpg` | Lofi · Ghibli | 3840 × 2160 |
| 🏯 Mountain Castle | `backgrounds/japanese-castle-pixel-digital-art.jpg` | Pixel Art | 3840 × 2160 |
| ⚔️ The Last Swordsman | `backgrounds/Character with Glowing Eyes and Katana.jpg` | Dark Fantasy | 3840 × 2160 |
| 👺 Girl & Hannya | `backgrounds/Girl with Hannya Mask.jpeg` | Monochrome · Yokai | 3000 × 1688 |
| 🪶 Itachi & The Crows | `backgrounds/Itachi Uchiha.jpg` | Naruto · Akatsuki | 3840 × 2160 |

---

## ▸ 🤝 Contribute

Contributions are warmly welcome!

```
git checkout -b feat/your-idea
git commit -m "feat: add your idea"
git push && open a Pull Request
```

---

<div align="center">

Made with 🧡 for **Omarchy**

*If this theme made your desktop beautiful, consider leaving a ⭐ — it means a lot!*

[![GitHub](https://img.shields.io/badge/GitHub-hembramnishant50--glitch-181717?style=for-the-badge&logo=github)](https://github.com/hembramnishant50-glitch)

</div>
