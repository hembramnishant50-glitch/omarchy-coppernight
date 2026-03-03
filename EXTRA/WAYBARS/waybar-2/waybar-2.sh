#!/bin/bash

# Define variables
REPO_URL="https://github.com/hembramnishant50-glitch/omarchy-coppernight-theme.git"
TMP_DIR="/tmp/omarchy-theme"
TARGET_CONFIG="$HOME/.config/waybar"
SUFFIX=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 4 | head -n 1)

echo "Starting installation of Waybar-2 theme..."

# 1. Clone the repository
if [ -d "$TMP_DIR" ]; then rm -rf "$TMP_DIR"; fi
git clone "$REPO_URL" "$TMP_DIR"

# 2. Backup existing waybar folder
if [ -d "$TARGET_CONFIG" ]; then
    BACKUP_NAME="${TARGET_CONFIG}-$SUFFIX"
    mv "$TARGET_CONFIG" "$BACKUP_NAME"
    echo "----------------------------------------------------------"
    echo "Your backup is saved as $BACKUP_NAME"
    echo "----------------------------------------------------------"
fi

# 3. Install waybar-2 theme
mkdir -p "$TARGET_CONFIG"
cp -r "$TMP_DIR/EXTRA/waybar-2/." "$TARGET_CONFIG/"

# 4. Cleanup
rm -rf "$TMP_DIR"

echo "Success! waybar-2 theme has been installed to $TARGET_CONFIG"
echo "You may need to restart Waybar (killall waybar && waybar &) to apply changes."
