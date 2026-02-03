<div align="center">

# 🌌 Omarchy: Copper Night

> *"Where the deep indigo of Tokyo meets the warm glow of an ember sunset."*

A high-performance **Hyprland** rice for Omarchy featuring a custom **Tokyo Night** palette accented by a striking **Copper-Orange** border.

![Version](https://img.shields.io/badge/version-1.0-orange?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![Hyprland](https://img.shields.io/badge/Hyprland-Rice-indigo?style=for-the-badge&logo=archlinux)

</div>

---

## 📸 Preview

| **Feature** | **Description** |
|:---|:---|
| 🖼️ **Wallpaper** | Traditional Japanese Pixel Art Pagoda. |
| 🪟 **UI** | Floating diagnostic widgets with custom resource bars. |
| 🎨 **Colors** | Deep Indigos, Magentas, and Copper-Orange accents. |

---

## 🚀 Easy Installation (One-Line)

This command installs all system dependencies (Python libraries, NetworkManager, and Papirus Icons), performs a safe backup of your existing Waybar config, and applies the Copper Night theme.

```bash
sudo pacman -S --needed python-requests python-psutil networkmanager papirus-icon-theme && \
omarchy-theme-install https://github.com/hembramnishant50-glitch/omarchy-coppernight.git && \
{ [ -d ~/.config/waybar ] && mv ~/.config/waybar ~/.config/waybar-backup-$RANDOM; }; \
mkdir -p ~/.config/waybar && \
cp -r ~/.config/omarchy/themes/coppernight/waybar/. ~/.config/waybar/ && \
chmod +x ~/.config/waybar/scripts/* && \
gsettings set org.gnome.desktop.interface icon-theme 'Papirus-Dark' && \
killall waybar; waybar &
