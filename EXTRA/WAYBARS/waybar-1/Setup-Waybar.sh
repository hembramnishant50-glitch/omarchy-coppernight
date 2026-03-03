#!/bin/bash

# Define paths
SOURCE_DIR="$HOME/.config/omarchy/current/theme/EXTRA/WAYBARS/waybar-1"
TARGET_DIR="$HOME/.config/waybar"
TIMESTAMP=$(date +"%Y-%m-%d-%H-%M-%S")
BACKUP_DIR="$HOME/.config/waybar-backup-$TIMESTAMP"

# 1. Check if source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory $SOURCE_DIR does not exist."
    exit 1
fi

# 2. Backup existing waybar folder
if [ -d "$TARGET_DIR" ]; then
    echo "Backing up current waybar config to $BACKUP_DIR..."
    mv "$TARGET_DIR" "$BACKUP_DIR"
fi

# 3. Apply new theme
echo "Applying new waybar-1 theme..."
mkdir -p "$TARGET_DIR"
cp -r "$SOURCE_DIR/." "$TARGET_DIR/"

# 4. FIX PERMISSIONS
if [ -d "$TARGET_DIR/scripts" ]; then
    echo "Setting executable permissions on scripts..."
    chmod +x "$TARGET_DIR/scripts/"*
    
    # 5. HOTFIX: Fix 'nmcli' ALL-SETTINGS error
    echo "Patching nmcli syntax in scripts..."
    sed -i 's/ALL-SETTINGS/GENERAL/g' "$TARGET_DIR/scripts/wifi_info.sh" 2>/dev/null
fi

# 6. Restart Waybar
echo "Restarting Waybar..."
killall waybar && waybar & disown

echo "Done! Theme applied, permissions fixed, and nmcli patched."