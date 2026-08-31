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

**The last Omarchy rice you'll ever need.**

> *"Where the deep indigo of Tokyo meets the warm glow of an ember sunset."*

![Version](https://img.shields.io/badge/version-1.2-C87941?style=for-the-badge&logo=git&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-7AA2F7?style=for-the-badge&logo=opensourceinitiative&logoColor=white)
![Hyprland](https://img.shields.io/badge/Hyprland-Rice-565f89?style=for-the-badge&logo=archlinux&logoColor=white)
![Omarchy](https://img.shields.io/badge/Made%20for-Omarchy-1E1E2E?style=for-the-badge&logo=archlinux&logoColor=white)
![Stars](https://img.shields.io/github/stars/hembramnishant50-glitch/omarchy-coppernight-theme?style=for-the-badge&color=BB9AF7&logo=stars&logoColor=white)

[![Copper Night Preview](preview.png)](preview.png)

</div>

---

## 📸 Gallery

<div align="center">

| Desktop | Terminal | Lock Screen |
|:-------:|:--------:|:-----------:|
| ![Desktop](https://private-user-images.githubusercontent.com/235138312/569810468-74b6b030-6181-4f01-a142-0a56e4046b14.png) | ![Terminal](https://private-user-images.githubusercontent.com/235138312/569817836-94cdb423-e93f-4498-9f0c-a60f7ba3ed0f.png) | ![Lock](https://private-user-images.githubusercontent.com/235138312/551009845-86b69c94-6096-411f-a41e-4704c238f394.png) |

</div>

---

## ⚡ Install

```bash
omarchy-theme-install https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme.git
```

### Then add Waybar *(optional)*

> ⚠️ Your existing Waybar config is automatically backed up before anything is changed.

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
        find ~/.config/waybar/scripts -type f -name "*.py" \
          -exec sed -i '1s|^#!/usr/bin/env python3|#!/usr/bin/python3|' {} +
    fi
fi

# Apply Papirus Dark icons & restart Waybar
gsettings set org.gnome.desktop.interface icon-theme 'Papirus-Dark'
killall -q waybar; nohup waybar > /dev/null 2>&1 &
```

---

## 🪟 Waybar — Pick a Variant

> ⚠️ All variants require the theme install above (and **Step 2** for the default Waybar).

| Variant | Style | Command |
|:-------:|:------|:--------|
| **1** | Default | Pre-installed with the theme |
| **2** | Pill Style | `cd EXTRA/WAYBARS/waybar-1 && ./Setup-Waybar.sh` |
| **3** | Ember Arc | `cd EXTRA/WAYBARS/waybar-2 && ./waybar-setup.sh` |
| **4** | Pastel Capsule | `cd EXTRA/WAYBARS/waybar-3 && ./waybar-setup.sh` |
| **5** | Catppuccin Capsule | `cd EXTRA/WAYBARS/waybar-4 && ./waybar-setup.sh` |

### 1 · Default Waybar
*Clean and minimal — ships out of the box with the full install.*

### 2 · Waybar-1 — Pill Style
*Neon pill borders · Rounded segments · Compact & clean*

### 3 · Waybar-2 — Ember Arc
*Copper warmth · Floating arcs · Glows like a setting sun*

### 4 · Waybar-3 — Pastel Capsule
*Neon pastel · Rounded capsules · Floating in a dark sky*

### 5 · Waybar-4 — Catppuccin Mocha Capsule
*Catppuccin Mocha · Copper borders · Rounded capsules with workspace circles*

---

## 🌤️ Weather Widget

No more editing scripts. **One click** updates your city.

```
click →  type city  →  enter
  🌡️     "London"     ✓ done
  ☀️     "Tokyo"      ✓ saved
  🌧️     "Patna"      ✓ instant
```

> 💡 Your city is saved automatically. To refresh, click the icon again or run `killall waybar; waybar &`.

---

## 🔒 Lock Screen

<div align="center">

![Hyprlock Preview](https://private-user-images.githubusercontent.com/235138312/551009845-86b69c94-6096-411f-a41e-4704c238f394.png)

</div>

*Glassmorphism lock screen with live clock, random quotes, and media controls*

### Setup

> ⚠️ Complete the theme install before running this.

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

**⚠️ Fix: Black Screen on Lock**

If your screen goes black when locking, apply this quick fix.

1. Open the file:
```bash
nano ~/.local/share/omarchy/bin/omarchy-system-lock
```

2. Find this line at the bottom:
```bash
omarchy-brightness-display off
```

3. Comment it out by adding `#` at the start:
```bash
# omarchy-brightness-display off
```

4. Save and exit: `Ctrl+O` → `Enter` → `Ctrl+X`

### Customize

```bash
nano ~/.config/omarchy/current/theme/hyprlock.conf
```

```conf
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
|:-------------:|:-------|
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

## ✨ Features

| Feature | Description |
|:--------|:------------|
| ◆ **Wallpaper** | Traditional Japanese Pixel Art Pagoda — handpicked for the aesthetic |
| ◆ **Widgets** | Floating diagnostic panels with custom animated resource bars |
| ◆ **Color Palette** | Deep Indigos · Electric Magentas · Warm Copper-Orange accents |
| ◆ **Weather Widget** | Live weather with click-to-change city — no script editing needed |
| ◆ **Lock Screen** | Glassmorphism Hyprlock with blur, quotes, and media controls |
| ◆ **Media Controls** | Playerctl integration with full Spotify Flatpak support |
| ◆ **5 Waybar Variants** | Pick your vibe — Default, Pill, Ember Arc, Pastel, Catppuccin |
| ◆ **Stylus Theme** | 136+ website themes for Chrome/Firefox via Stylus extension |

---

## 🗂️ Theme Files

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
├── Stylus.json            Chrome extension themes
├── quotes.txt             Lock screen quotes
├── scripts/               Lock screen helpers
└── backgrounds/           5 wallpapers
```

---

## 🎨 Color Palette

<div align="center">

| Color | Name | Hex | Usage |
|:-----:|:-----|:----|:------|
| 🔵 | **Blue** | `#89b4fa` | Primary accent |
| 🟣 | **Mauve** | `#cba6f7` | Secondary accent |
| 🟠 | **Copper** | `#fab387` | Warm highlights |
| 🟢 | **Green** | `#a6e3a1` | Success states |
| 🔴 | **Red** | `#f38ba8` | Error states |
| 🩷 | **Pink** | `#f5c2e7` | Special elements |
| 🩵 | **Sky** | `#89dceb` | Info states |
| 🩶 | **Surface** | `#313244` | UI elements |
| ⬛ | **Base** | `#11111b` | Background |

</div>

```
Background: #11111b  ← Deep indigo darkness
Mantle:     #181825  ← Slightly lighter
Surface:    #313244  ← UI elements
Text:       #fab387  ← Copper-orange glow
Accent:     #89b4fa  ← Electric blue
Green:      #a6e3a1  ← Success/syntax
Pink:       #f5c2e7  ← Special highlights
Mauve:      #cba6f7  ← Secondary accent
```

---

## 🛠️ Built With

- **[Hyprland](https://hyprland.org/)** — Dynamic tiling Wayland compositor
- **[Omarchy](https://omarchy.org/)** — Arch Linux desktop environment
- **[Waybar](https://github.com/Alexays/Waybar)** — Highly customizable Wayland bar
- **[Catppuccin](https://catppuccin.com/)** — Softer pastel theme inspiration
- **[Tokyo Night](https://github.com/enkia/tokyo-night-vscode-theme)** — Color palette inspiration

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 💝 Credits

- **Catppuccin** — For the beautiful pastel color palette inspiration
- **Tokyo Night** — For the deep indigo base colors
- **Omarchy** — For making Arch Linux accessible to everyone

---

<div align="center">

**Made with 💖 by [Nishant](https://github.com/hembramnishant50-glitch)**

*"Where the deep indigo of Tokyo meets the warm glow of an ember sunset."*

![Visitors](https://api.visitorbadge.io/api/visitors?path=hembramnishant50-glitch%2Fomarchy-coppernight-theme&countColor=%23C87941&style=for-the-badge)

</div>
