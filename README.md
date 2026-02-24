<div align="center">

<br>

```
░█▀▀█ ░█▀▀▀█ ░█▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀█   ░█▄─░█ ▀█▀ ░█▀▀█ ░█─░█ ▀▀█▀▀
░█─── ░█──░█ ░█▄▄█ ░█▄▄█ ░█▀▀▀ ░█▄▄▀   ░█░█░█ ░█─ ░█─▄▄ ░█▀▀█ ─░█──
░█▄▄█ ░█▄▄▄█ ░█─── ░█─── ░█▄▄▄ ░█─░█   ░█──▀█ ▄█▄ ░█▄▄█ ░█─░█ ─░█──
```

# 🌌 Omarchy: Copper Night

> *"Where the deep indigo of Tokyo meets the warm glow of an ember sunset."*

A high-performance **Hyprland** rice for **Omarchy** — featuring a carefully crafted **Tokyo Night** palette  
kissed by a striking **Copper-Orange** border that glows like a setting sun.

<br>

[![Version](https://img.shields.io/badge/version-1.2-C87941?style=for-the-badge&logo=git&logoColor=white)](https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme)
[![License](https://img.shields.io/badge/license-MIT-7AA2F7?style=for-the-badge&logo=opensourceinitiative&logoColor=white)](LICENSE)
[![Hyprland](https://img.shields.io/badge/Hyprland-Rice-565f89?style=for-the-badge&logo=archlinux&logoColor=white)](https://hyprland.org)
[![Stars](https://img.shields.io/github/stars/hembramnishant50-glitch/omarchy-coppernight-theme?style=for-the-badge&color=BB9AF7&logo=starship&logoColor=white)](https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme/stargazers)

<br>

</div>

---

## 📸 Screenshots

<div align="center">

| | |
|:---:|:---:|
| <img src="https://github.com/user-attachments/assets/39ec8953-3b6f-4420-a9fe-88eb83d76899" width="100%"> | <img src="https://github.com/user-attachments/assets/b84e6655-4653-408d-8281-03d9a34d7b4d" width="100%"> |
| <img src="https://github.com/user-attachments/assets/9560a87d-5b0a-4dfb-803c-29b647411de4" width="100%"> | <img src="https://github.com/user-attachments/assets/16bef38a-b05b-4b98-8da7-eb614974d2d3" width="100%"> |
| <img src="https://github.com/user-attachments/assets/5521874f-feab-4880-b59c-bb2350045173" width="100%"> | <img src="https://github.com/user-attachments/assets/d2dd0073-0f8d-4a87-91e2-7772e865e705" width="100%"> |
| <img src="https://github.com/user-attachments/assets/3a8c2c4a-7bdd-4c73-94c1-8d4ae6f0c6ef" width="100%"> | <img src="https://github.com/user-attachments/assets/c0208938-787d-4e68-8d97-022438678f02" width="100%"> |

</div>

<br>

---

## ✨ Theme Highlights

<div align="center">

| Feature | Description |
|:---:|:---|
| 🖼️ **Wallpaper** | Traditional Japanese Pixel Art Pagoda — handpicked for the aesthetic |
| 🪟 **Widgets** | Floating diagnostic panels with custom animated resource bars |
| 🎨 **Color Palette** | Deep Indigos · Electric Magentas · Warm Copper-Orange accents |
| 🌤️ **Weather Widget** | Live weather display with configurable location |
| 🔒 **Lock Screen** | Glassmorphism Hyprlock with blur, quotes, and media controls |
| 🎵 **Media Controls** | Playerctl integration with full Spotify Flatpak support |

</div>

<br>

---

## 🚀 Installation

> **Choose the method that suits you best.** Both paths lead to the same beautiful result.

<br>

### ⚡ Option A — Theme Only *(Minimal)*

Just want the colors and wallpaper? Run this single command:

```bash
omarchy-theme-install https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme.git
```

<br>

### 🌟 Option B — Full Install *(Recommended)*

This installs **all system dependencies**, **backs up** your existing Waybar config safely, and applies the complete **Copper Night** theme with a fully configured Waybar.

```bash
# 1. Install dependencies
sudo pacman -S --needed \
  python-requests \
  python-psutil \
  networkmanager \
  papirus-icon-theme \
  pavucontrol

# 2. Install the theme
omarchy-theme-install https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme.git

# 3. Backup existing Waybar config (safe — uses a random suffix)
[ -d ~/.config/waybar ] && mv ~/.config/waybar ~/.config/waybar-backup-$RANDOM

# 4. Apply the Copper Night Waybar config
mkdir -p ~/.config/waybar
cp -r ~/.config/omarchy/themes/coppernight/waybar/. ~/.config/waybar/
chmod +x ~/.config/waybar/scripts/*

# 5. Apply Papirus Dark icons
gsettings set org.gnome.desktop.interface icon-theme 'Papirus-Dark'

# 6. Restart Waybar
killall waybar; waybar &
```

> 💡 **Tip:** Your old Waybar config is backed up as `~/.config/waybar-backup-XXXXX`. Nothing is deleted.

<br>

---

## ⚙️ Configuration

### 🌤️ Weather Widget — Set Your City

The weather widget displays **New York** by default. Here's how to change it:

**Step 1** — Open the weather script:
```bash
nano ~/.config/waybar/scripts/weather.py
```

**Step 2** — Find the `CITY` variable and update it:
```python
# ── Configuration ─────────────────────────────
CITY = "Tokyo"   # ← Replace with your city name
```

**Step 3** — Save and exit:
```
Ctrl + O  →  Enter    (Save)
Ctrl + X              (Exit)
```

**Step 4** — Restart Waybar to apply:
```bash
killall waybar; waybar &
```

<br>

---

## 🔒 Hyprlock — Custom Lock Screen

<div align="center">

<img width="1311" height="737" alt="Hyprlock Preview" src="https://github.com/user-attachments/assets/86b69c94-6096-411f-a41e-4704c238f394" />

*Glassmorphism lock screen with live clock, random quotes, and media controls*

</div>

<br>

> ⚠️ **Run this after completing Option A or Option B above.**

<br>

### 📦 Setup Commands

```bash
# 1. Install Playerctl (required for media key support)
sudo pacman -S --needed playerctl

# 2. Fix Spotify media controls (only needed for Flatpak version)
if command -v flatpak &> /dev/null; then
    flatpak override --user \
      --talk-name=org.mpris.MediaPlayer2.spotify \
      com.spotify.Client
fi

# 3. Copy lock screen config files to Hyprland directory
cp -r \
  ~/.config/omarchy/current/theme/scripts \
  ~/.config/omarchy/current/theme/quotes.txt \
  ~/.config/omarchy/current/theme/hyprlock.conf \
  ~/.config/hypr/

# 4. Make scripts executable
chmod +x ~/.config/hypr/scripts/*
```

<br>

### 🖼️ Customizing the Lock Screen

You can swap the **background wallpaper** and **profile picture** directly in the config:

```bash
nano ~/.config/hypr/hyprlock.conf
```

Look for these two sections and update the `path =` lines:

```ini
# ── Background Wallpaper ──────────────────────────────────────
background {
    monitor =
    path = /home/YOUR_USER/Pictures/your-wallpaper.jpg   # ← .jpg or .png

    # Blur settings (0 = sharp, higher = more blur)
    blur_passes = 0    # try 3 for a soft glass effect
    blur_size   = 7    # strength of the blur kernel
}

# ── Profile Picture ───────────────────────────────────────────
image {
    monitor =
    path = /home/YOUR_USER/Pictures/your-avatar.png      # ← .jpg or .png
    size = 150
}
```

> **Blur Presets:**
> | `blur_passes` | Effect |
> |:---:|:---|
> | `0` | Sharp — no blur at all |
> | `2` | Subtle — light frost |
> | `3` | Standard — soft glass |
> | `5+` | Heavy — dreamy glow |

<br>

---

## 🎨 Color Palette

<div align="center">

| Name | Hex | Preview |
|:---|:---|:---:|
| Background | `#1a1b2e` | ![](https://placehold.co/60x20/1a1b2e/1a1b2e) |
| Deep Indigo | `#565f89` | ![](https://placehold.co/60x20/565f89/565f89) |
| Electric Blue | `#7aa2f7` | ![](https://placehold.co/60x20/7aa2f7/7aa2f7) |
| Magenta | `#bb9af7` | ![](https://placehold.co/60x20/bb9af7/bb9af7) |
| Copper-Orange | `#c87941` | ![](https://placehold.co/60x20/c87941/c87941) |
| Foreground | `#c0caf5` | ![](https://placehold.co/60x20/c0caf5/c0caf5) |

</div>

<br>

---

## 🤝 Contributing

Got ideas? Found a bug? Contributions are warmly welcome!

1. **Fork** this repository
2. **Create** a feature branch: `git checkout -b feat/your-idea`
3. **Commit** your changes: `git commit -m "feat: add your idea"`
4. **Push** and open a **Pull Request**

<br>

---

<div align="center">

Made with 🧡 and deep indigo ink

*If this theme made your desktop beautiful, consider leaving a ⭐ — it means a lot!*

[![GitHub](https://img.shields.io/badge/GitHub-hembramnishant50--glitch-181717?style=for-the-badge&logo=github)](https://github.com/hembramnishant50-glitch)

</div>
