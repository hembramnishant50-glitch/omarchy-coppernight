#!/bin/bash

# Define paths
SOURCE_DIR="$HOME/.config/omarchy/current/theme/EXTRA/WAYBARS/waybar-4"
TARGET_DIR="$HOME/.config/waybar"
BACKUP_DIR="$HOME/.config/waybar-backup-$(date +%Y-%m-%d-%H%M%S)"
SCRIPT_DIR="$TARGET_DIR/scripts"

# 1. Create backup of the existing config if it exists
if [ -d "$TARGET_DIR" ]; then
    echo "Creating backup at $BACKUP_DIR..."
    cp -r "$TARGET_DIR" "$BACKUP_DIR"
fi

# 2. Ensure target directory exists
mkdir -p "$TARGET_DIR"

# 3. Copy the new files
echo "Installing new Waybar config..."
cp -r "$SOURCE_DIR/." "$TARGET_DIR/"

# 4. Ensure script permissions and trigger background scripts
if [ -d "$SCRIPT_DIR" ]; then
    echo "Setting execution permissions for helper scripts..."
    chmod +x "$SCRIPT_DIR"/*.sh "$SCRIPT_DIR"/*.py 2>/dev/null

    # Optional: Pre-fetch or trigger scripts like weather so Waybar loads it instantly
    if [ -f "$SCRIPT_DIR/weather.sh" ]; then
        echo "Initializing weather service cache..."
        "$SCRIPT_DIR/weather.sh" > /dev/null 2>&1 &
    fi
fi

# 5. Ensure power-menu.sh exists for battery on-click
POWER_MENU_SCRIPT="$HOME/.config/omarchy/scripts/power-menu.sh"
if [[ ! -f "$POWER_MENU_SCRIPT" ]]; then
    echo "Creating power-menu.sh..."
    mkdir -p "$(dirname "$POWER_MENU_SCRIPT")"
    cat > "$POWER_MENU_SCRIPT" << 'POWEREOF'
#!/bin/bash
choice=$(omarchy-menu-select "Power Menu" "Lock" "Suspend" "Hibernate" "Reboot" "Shutdown" "Logout" -- --title "Power Menu")
case "$choice" in
  Lock) omarchy system lock ;;
  Suspend) systemctl suspend ;;
  Hibernate) systemctl hibernate ;;
  Reboot) systemctl reboot ;;
  Shutdown) systemctl poweroff ;;
  Logout) hyprctl dispatch exit ;;
esac
POWEREOF
    chmod +x "$POWER_MENU_SCRIPT"
fi

# 6. Fix any hardcoded old usernames in config.jsonc
CONFIG_FILE="$TARGET_DIR/config.jsonc"
if [[ -f "$CONFIG_FILE" ]]; then
    sed -i "s|/home/nishant/|~/|g; s|/home/hisoka/|~/|g" "$CONFIG_FILE"
fi

echo "Restarting Waybar..."
killall waybar 2>/dev/null
sleep 0.5
(waybar > /dev/null 2>&1 &)

echo "Done! Your old config is safe in $BACKUP_DIR."