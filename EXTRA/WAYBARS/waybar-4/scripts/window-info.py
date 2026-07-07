#!/usr/bin/python3
import subprocess
import json
import hashlib
import re
import time
import html

# --- CONFIGURATION ---
MAX_TITLE_LEN = 20

# --- MUSIC FILTER ---
MUSIC_PLAYERS = ["spotify", "ncspot", "cider", "rhythmbox", "vlc", "mpv", "music"]
MUSIC_WEB_KEYWORDS = ["spotify", "soundcloud", "music", "deezer", "bandcamp"]
PATTERNS = [" ── ", " ─╼ ", " ╼╾ ", " ╾▩ ", " ▩▩ ", " ▩╼ ", " ╼─ "]
PATTERN_LEN = len(PATTERNS)

# --- EXACT USER APP RULES ---
APP_RULES = {
    # --- 0. Google / Proton / Web apps---
    "google-chrome":                  ("", "#4285f4", "Chrome"),
    "google-gmail":                   ("󰊭", "#ea4335", "Gmail"),
    "google-drive":                   ("󰝰", "#34a853", "Drive"),
    "google-calendar":                ("󰸗", "#4285f4", "Calendar"),
    "contacts.google.com": ("", "#4285f4", "Google Contacts"),
    "calendar.google.com":     ("󰸗", "#4285f4", "Calendar"),
    "google-keep":                    ("󰟶", "#fbbc04", "Keep"),
    "google-maps":                    ("󰉙", "#34a853", "Maps"),
    "maps.google.com": ("", "#ea4335", "Google Maps"),
    "google-docs":                    ("󰈙", "#4285f4", "Docs"),
    "google-sheets":                  ("󰈛", "#34a853", "Sheets"),
    "google-slides":                  ("󰈧", "#fbbc04", "Slides"),
    "google-meet":                    ("󰻵", "#00897b", "Meet"),
    "google-photos":                  ("󰄄", "#ff4500", "Photos"),
    "google-youtube":                 ("󰗃", "#ff0000", "YouTube"),
    "messages.google.com": ("󰍡", "#1a73e8", "Google Messages"),
    "mail.google.com":     ("󰊭", "#ea4335", "Gmail"),
    "drive.google.com":    ("󰝰", "#34a853", "Drive"),
    "keep.google.com":     ("󰟶", "#fbbc04", "Keep"),
    "docs.google.com":     ("󰈙", "#4285f4", "Docs"),
    "sheets.google.com":   ("󰈛", "#34a853", "Sheets"),
    "slides.google.com":   ("󰈧", "#fbbc04", "Slides"),
    "meet.google.com":     ("󰻵", "#00897b", "Meet"),
    "photos.google.com":   ("󰄄", "#ff4500", "Photos"),
    "youtube.com":         ("󰗃", "#ff0000", "YouTube"),
    "www.google.com":      ("", "#4285f4", "Google"),
    "notebooklm.google.com": ("󰠮", "#4285f4", "NotebookLM"),

    "chrome-mail.proton.me__-default":       ("󰇮", "#6d4aff", "Proton Mail"),
    "chrome-calendar.proton.me__-default":   ("󰸗", "#6d4aff", "Proton Calendar"),
    "chrome-drive.proton.me__-default":      ("󰝰", "#6d4aff", "Proton Drive"),
    "chrome-pass.proton.me__-default":       ("󰷖", "#6d4aff", "Proton Pass"),
    "chrome-vpn.proton.me__-default":        ("󰖂", "#6d4aff", "Proton VPN"),
    "chrome-lumo.proton.me__-default":       ("󱔐", "#6d4aff", "Proton Lumo"),

    "app.zoom.us": ("", "#2d8cff", "Zoom"),


    # --- 1. STUDENT & RESEARCH (Flathub Versions) ---
    "ClamUI":                         ("󰂵", "#7c4dff", "ClamUI"),
    "md.obsidian.Obsidian":           ("󱓧", "#7c4dff", "Obsidian"),
    "Obsidian":           ("󱓧", "#7c4dff", "Obsidian"),
    "net.ankiweb.Anki":               ("󰮔", "#ffffff", "Anki"),
    "org.zotero.Zotero":              ("󱓷", "#cc2914", "Zotero"),
    "org.libreoffice.LibreOffice":    ("󰏆", "#185abd", "LibreOffice"),
    "org.onlyoffice.desktopeditors":  ("󰏆", "#ff6f21", "ONLYOFFICE"),
    "com.github.xournalpp.xournalpp": ("󱞈", "#2980b9", "Xournal++"),
    "com.github.johnfactotum.Foliate":("󰂵", "#629c44", "Foliate"),
    "org.kde.kalgebra":               ("󰪚", "#3daee9", "KAlgebra"),
    "io.github.fabrialberio.pinapp":  ("󰐚", "#4caf50", "Pins"),
    "org.bunkus.mkvtoolnix-gui":      ("󰔑", "#81a2be", "MKVToolNix"),
    "garden.jamie.Morphosis":         ("󰈹", "#3584e4", "Morphosis"),
    "Io.github.vmkspv.lenspect": ("󰍉", "#14b8a6", "Lenspect"),
    "Io.gitlab.theevilskeleton.upscaler": ("󰊓", "#d946ef", "Upscaler"),
    "Net.nokyan.resources": ("󰓅", "#3b82f6", "Resources"),

    # --- 2. WEB BROWSERS (Flathub Versions) ---
    "io.github.zen_browser.zen":      ("󰈹", "#4f4f4f", "Zen Browser"),
    "org.mozilla.firefox":            ("", "#ff7139", "Firefox"),
    "org.qutebrowser.qutebrowser":    ("󰈹", "#8dc21f", "qutebrowser"),
    "io.gitlab.librewolf-community":  ("󰈹", "#3269d6", "LibreWolf"),
    "com.vivaldi.Vivaldi":            ("", "#ef3939", "Vivaldi"),
    "net.mullvad.MullvadBrowser":     ("󰇚", "#3c9519", "Mullvad Browser"),

    # --- 3. DEVELOPMENT & SYSTEM (Flathub Versions) ---
    "com.visualstudio.code":          ("󰨞", "#007acc", "VS Code"),
    "com.vscodium.codium":            ("󰨞", "#23a7d2", "VSCodium"),
    "com.github.tchx84.Flatseal":     ("󱓷", "#3eb34f", "Flatseal"),
    "io.missioncenter.MissionCenter": ("󱓟", "#3584e4", "Mission Center"),
    "io.github.flattool.Warehouse":   ("", "#ff9500", "Warehouse"),

    # --- 4. MEDIA & DESIGN (Flathub Versions) ---
    "org.videolan.VLC":               ("󰕼", "#ff9900", "VLC"),
    "io.github.celluloid_player.Celluloid": ("󰕼", "#5e5ce6", "MPV/Celluloid"),
    "io.bassi.Amberol":               ("󰎆", "#f8d210", "Amberol"),
    "org.gimp.GIMP":                  ("", "#5c5543", "GIMP"),
    "org.inkscape.Inkscape":          ("", "#ffffff", "Inkscape"),
    "org.kde.kdenlive":               ("", "#3daee9", "Kdenlive"),
    "org.upscayl.Upscayl":            ("󰭹", "#ff4500", "Upscayl"),

    # --- 5. UTILITIES (Flathub Versions) ---
    "org.localsend.localsend_app":    ("󰄶", "#3db2ff", "LocalSend"),
    "com.github.flameshot.Flameshot": ("󰄀", "#ff4081", "Flameshot"),
    "com.github.unhndrd.pdfarranger": ("󰈦", "#f1c40f", "PDF Arranger"),
    "com.bitwarden.desktop":          ("󰞀", "#175DDC", "Bitwarden"),
    "io.github.hlubek.Eyedropper":    ("󰈊", "#3584e4", "Eyedropper"),
    "io.github.kolunmi.Bazaar":       ("", "#e74c3c", "Bazaar"),
    "io.github.michelegiacalone.bazaar": ("", "#e74c3c", "Bazaar"),
    "org.audacityteam.Audacity":      ("󰓃", "#0000eb", "Audacity"),
    "audacity":                       ("󰓃", "#0000eb", "Audacity"),
    "com.rafaelmardojai.Blanket":     ("󰖗", "#3daee9", "Blanket"),
    "blanket":                        ("󰖗", "#3daee9", "Blanket"),
    "org.gnome.gitlab.YaLTeR.VideoTrimmer": ("󰐊", "#c061cb", "Video Trimmer"),
    "org.libretro.RetroArch":         ("󰊴", "#3daee9", "RetroArch"),
    "Tui.float": ("", "#a6e3a1", "Floating TUI"),
    
    # --- 6. SOCIAL (Flathub Versions) ---
    "com.discordapp.Discord":         ("", "#5865f2", "Discord"),
    "org.telegram.desktop":           ("", "#24a1de", "Telegram"),
    "com.ayugram.desktop":            ("", "#3399ff", "AyuGram"),
    "App.drey.dialect": ("󰗊", "#3584e4", "Dialect"),
    "Fingergo": ("󰟆", "#8b5cf6", "Fingergo"),
    "pinapp":                         ("󰐚", "#4caf50", "Pins"),
    "Pins":                           ("󰐚", "#4caf50", "Pins"),
    "Dev.geopjr.collision": ("󰆕", "#c061cb", "Collision"),

    # --- Omarchy Versions ---
    # --- Gaming ----
    "minecraft-launcher":             ("󰍳", "#3e8527", "Minecraft"),
    "minecraft launcher":             ("󰍳", "#3e8527", "Minecraft"),
    "org.prismlauncher.PrismLauncher":("󰍳", "#52b12e", "Prism"),
    "org.multimc.MultiMC":            ("󰍳", "#f9b000", "MultiMC"),
    "com.gdlauncher.gdlauncher":      ("󰍳", "#14b1e7", "GDLauncher"),
    "retroarch":                      ("󰊴", "#3daee9", "RetroArch"),
    "RetroArch":                      ("󰊴", "#3daee9", "RetroArch"),
    "app.fizzy.do": ("󰃌", "#f43f5e", "Fizzy"),

    # --- AI & EDUCATION ---
    "careerwill":                     ("🎓", "#ff9900", "Careerwill"),
    "chatgpt":                        ("󰚩", "#74aa9c", "ChatGPT"),
    "gemini":                         ("󰊭", "#8ab4f8", "Gemini AI"),
    "claude":                         ("", "#d97757", "Claude AI"),
    "bing":                           ("", "#2583c6", "Bing Chat"),
    "perplexity":                     ("󰚩", "#2ebfab", "Perplexity"),

    # --- BROWSERS ---
    "com.brave.Browser":              ("󰖟", "#ff542b", "Brave"),
    "brave-browser":                  ("󰖟", "#ff542b", "Brave"),
    "Brave-origin-beta":              ("󰖟", "#ff542b", "Brave Origin"),
    "omarchy-chromium":               ("", "#00bcd4", "Omarchy Chromium"),
    "librewolf":                      ("󰈹", "#3269d6", "LibreWolf"),
    "tor-browser":                    ("", "#7d4698", "Tor Browser"),
    "ungoogled-chromium":             ("", "#ffffff", "Ungoogled Chromium"),
    "microsoft-edge":                 ("", "#0078d7", "Microsoft Edge"),
    "firefox":                        ("", "#ff7139", "Firefox"),
    "chromium":                       ("", "#4285f4", "Chromium"),
    "cromium":                        ("", "#4285f4", "Chromium"),
    "opera":                          ("", "#ff1b2d", "Opera"),
    "vivaldi":                        ("", "#ef3939", "Vivaldi"),
    "epiphany":                       ("󰈹", "#3584e4", "GNOME Web"),
    "helium":                         ("󰈹", "#ffeb3b", "Helium"),
    "mullvadbrowser":                 ("󰖟", "#ffdc00", "Mullvad"),
    "mullvadbrowser.real":            ("󰖟", "#ffdc00", "Mullvad"),
    "mullvad-browser-bin":            ("󰖟", "#ffdc00", "Mullvad"),
    "mullvad browser":                ("󰖟", "#ffdc00", "Mullvad"),
    "mullvad-browser":                ("󰖟", "#ffdc00", "Mullvad"),

    # --- SOCIAL MEDIA & COMMUNICATION ---
    "ayugram-desktop":                ("", "#3399ff", "AyuGram"),
    "telegram-desktop":               ("", "#24A1DE", "Telegram"),
    "telegram":                       ("", "#24a1de", "Telegram"),
    "discord":                        ("", "#5865f2", "Discord"),
    "whatsapp":                       ("", "#25d366", "WhatsApp"),
    "reddit":                         ("", "#ff4500", "Reddit"),
    "twitter":                        ("", "#1da1f2", "Twitter"),
    "x.com":                          ("", "#000000", "X"), 
    "facebook":                       ("", "#1877f2", "Facebook"),
    "instagram":                      ("", "#c13584", "Instagram"),
    "linkedin":                       ("", "#0077b5", "LinkedIn"),
    "pinterest":                      ("", "#bd081c", "Pinterest"),
    "tumblr":                         ("", "#35465c", "Tumblr"),
    "tiktok":                         ("", "#ff0050", "TikTok"),
    "org.signal.Signal":              ("󰭹", "#3a76f0", "Signal"),
    "signal-desktop":                 ("󰭹", "#3a76f0", "Signal"),

    # --- PRODUCTIVITY & OFFICE ---
    "onlyoffice":                     ("󰏆", "#ff6f21", "ONLYOFFICE"),
    "libreoffice-startcenter":        ("󰏆", "#185abd", "LibreOffice"),
    "libreoffice-writer":             ("󰏆", "#005396", "Writer"),
    "libreoffice-calc":               ("󰏆", "#2d7335", "Calc"),
    "libreoffice-impress":            ("󰏆", "#b83c22", "Impress"),
    "libreoffice-draw":               ("󰏆", "#833e14", "Draw"),
    "libreoffice-math":               ("󰏆", "#4285f4", "Math"),
    "libreoffice-base":               ("󰏆", "#622a7a", "Base"),
    "DesktopEditors":                 ("󰏆", "#ff6f21", "ONLYOFFICE"),
    "joplin":                         ("󰮔", "#002e7a", "Joplin"),
    "anki":                           ("󰮔", "#ffffff", "Anki"),
    "zotero":                         ("󱓷", "#cc2914", "Zotero"),
    "xournalpp":                      ("󱞈", "#2980b9", "Xournal++"),
    "pdfarranger":                    ("󰈦", "#f1c40f", "PDF Arranger"),
    "notion":                         ("", "#000000", "Notion"),
    "trello":                         ("", "#0079bf", "Trello"),
    "gmail":                          ("", "#ea4335", "Gmail"),
    "outlook":                        ("", "#0078d4", "Outlook"),
    "hey":                            ("󰮏", "#ffcc00", "HEY Mail"),
    "basecamp":                       ("", "#ffcc00", "basecamp"),
    "chrome-app.zoom.us__wc_home-default": ("󰕧", "#2d8cff", "Zoom"),

    # --- GRAPHICS & MEDIA ---
    "flameshot":                      ("󰄀", "#ff4081", "Flameshot"),
    "gimp":                           ("", "#5c5543", "GIMP"),
    "inkscape":                       ("", "#ffffff", "Inkscape"),
    "figma":                          ("", "#f24e1e", "Figma"),
    "canva":                          ("", "#00c4cc", "Canva"),
    "vlc":                            ("󰕼", "#ff9900", "VLC"),
    "obs":                            ("", "#262626", "OBS Studio"),
    "spotify":                        ("", "#1db954", "Spotify"),
    "youtube":                        ("", "#ff0000", "YouTube"),

    # --- SYSTEM & UTILITIES ---
    "warehouse":                      ("", "#ff9500", "Warehouse"),
    "bitwarden":                      ("󰞀", "#175DDC", "Bitwarden"),
    "Bitwarden":                      ("󰞀", "#175DDC", "Bitwarden"),
    "pavucontrol":                    ("󰓃", "#67808d", "Volume Control"),
    "bleachbit":                      ("󰃢", "#e6e6e6", "BleachBit"),
    "timeshift":                      ("󰁯", "#ed333b", "Timeshift"),
    "nautilus":                       ("", "#f2c94c", "Files"),
    "dolphin":                        ("", "#3daee9", "Dolphin"),
    "thunar":                         ("", "#a9b665", "Thunar"),
    "calculator":                     ("", "#4193f4", "Calculator"),
    "keypunch":                       ("", "#ff4081", "Keypunch"),
    "bazaar":                         ("", "#e74c3c", "Bazaar"),
    "Com-abdownloadmanager-desktop-appkt": ("󰇚", "#00aaff", "AB Download Manager"),
    "aether":                         ("󰑭", "#a29bfe", "Aether"),
    "typora":                         ("󰂺", "#b4637a", "Typora"),
    "1password":                      ("", "#0572ec", "1Password"),
    "Io.gitlab.adhami3310.converter": ("󱊲", "#3584e4", "Converter"),
    "fr.handbrake.ghb":               ("󱁆", "#b71c1c", "Handbrake"),
    "curlew":                         ("󰕧", "#2e7d32", "Curlew"),
    "soundconverter":                 ("󰓃", "#f57c00", "SoundConverter"),
    "mystiq":                         ("󰕧", "#00d2ff", "MystiQ"),
    "Gitlab.yalter.videotrimmer":     ("󰐊", "#c061cb", "Video Trimmer"),
    "com.ozmartians.VidCutter":       ("󰐊", "#2d8cff", "VidCutter"),
    "losslesscut":                    ("󰐊", "#000000", "LosslessCut"),
    "io.gitlab.clark_johnston.Footage": ("󰿚", "#3584e4", "Footage"),
    "Stremio.stremio":                ("󰐊", "#7b3fe4", "Stremio"),
    "com.stremio.Stremio":            ("󰐊", "#7b3fe4", "Stremio"),
    "stremio":                        ("󰐊", "#7b3fe4", "Stremio"),
    "com.stremio.Service":            ("󱑫", "#7b3fe4", "Stremio Service"),
    "Io.github.sigmasd.stimulator":   ("󰅶", "#f57c00", "Stimulator"),
    "stimulator":                     ("󰅶", "#f57c00", "Stimulator"),
    "de.haeckerfelix.Shortwave":      ("󰕱", "#613583", "Shortwave"),
    "Shortwave":                      ("󰕱", "#613583", "Shortwave"),
    "shortwave":                      ("󰕱", "#613583", "Shortwave"),
    "fr.romainvigier.MetadataCleaner":("󰃢", "#5e5c64", "Metadata Cleaner"),
    "metadatacleaner":                ("󰃢", "#5e5c64", "Metadata Cleaner"),
    "Metadata Cleaner":               ("󰃢", "#5e5c64", "Metadata Cleaner"),
    "Morphosis":                      ("󰈹", "#3584e4", "Morphosis"),
    "morphosis":                      ("󰈹", "#3584e4", "Morphosis"),
    "garden.jamie.morphosis":         ("󰈹", "#3584e4", "Morphosis"),
    "mkvtoolnix-gui":                 ("󰔑", "#81a2be", "MKVToolNix"),
    "mkvtoolnix":                     ("󰔑", "#81a2be", "MKVToolNix"),
    "MKVToolNix GUI":                 ("󰔑", "#81a2be", "MKVToolNix"),
    "Org.cryptomator.launcher.cryptomator$mainapp": ("󰌋", "#2ebd59", "Cryptomator"),
    "Nwg-look": ("󰏘", "#0db9d7", "nwg-look"),
    "Imv": ("", "#06b6d4", "Imv"),
    "Localsend": ("", "#3db2ff", "LocalSend"),
    "Mpv": ("󰐊", "#bd93f9", "mpv"),
    "Github.pintaproject.pinta": ("", "#0ea5e9", "Pinta"),

    # --- DOWNLOAD MANAGERS ---
    "com.abdownloadmanager.abdownloadmanager": ("󰇚", "#00aaff", "AB Download Manager"),
    "abdownloadmanager":              ("󰇚", "#00aaff", "AB Download Manager"),
    "qbittorrent":                    ("󱑢", "#3b4ba4", "qBittorrent"),
    "transmission":                   ("󰇚", "#e63946", "Transmission"),
    "deluge":                         ("󱑢", "#49a010", "Deluge"),
    "aria2":                          ("󰈚", "#f1c40f", "Aria2"),
    "motrix":                         ("󰇚", "#ff4a00", "Motrix"),
    "xdm":                            ("󱑢", "#2c3e50", "XDM"),
    "uget":                           ("󰈚", "#fa8e3c", "uGet"),
    "jdownloader":                    ("󱑣", "#ff9000", "JDownloader"),
    "persepolis":                     ("󰈚", "#34495e", "Persepolis"),
    "fdm":                            ("󰇚", "#00aaff", "FDM"),
    "kget":                           ("󱑢", "#3daee9", "KGet"),

    # --- GNOME SUITE ---
    "org.gnome.clocks":               ("󱎫", "#3584e4", "Clocks"),
    "gnome-clocks":                   ("󱎫", "#3584e4", "Clocks"),
    "org.gnome.Nautilus":             ("", "#f2c94c", "Files"),
    "nautilus":                       ("", "#f2c94c", "Files"),
    "org.gnome.Calculator":           ("", "#4193f4", "Calculator"),
    "gnome-calculator":               ("", "#4193f4", "Calculator"),
    "org.gnome.DiskUtility":          ("󰋊", "#3584e4", "Disks"),
    "gnome-disk-utility":             ("󰋊", "#3584e4", "Disks"),
    "org.gnome.TextEditor":           ("", "#61afef", "Text Editor"),
    "gnome-text-editor":              ("", "#61afef", "Text Editor"),
    "org.gnome.gedit":                ("", "#61afef", "Gedit"),
    "gedit":                          ("", "#61afef", "Gedit"),
    "org.gnome.Evince":               ("󰈙", "#2e7d32", "Document Viewer"),
    "evince":                         ("󰈙", "#2e7d32", "Document Viewer"),
    "org.gnome.Boxes":                ("󰒓", "#3584e4", "Boxes"),
    "gnome-boxes":                    ("󰒓", "#3584e4", "Boxes"),
    "org.gnome.SystemMonitor":        ("󱓟", "#3584e4", "System Monitor"),
    "gnome-system-monitor":           ("󱓟", "#3584e4", "System Monitor"),
    "org.gnome.Settings":             ("⚙️", "#9a9996", "Settings"),
    "gnome-control-center":           ("⚙️", "#9a9996", "Settings"),
    "org.gnome.Software":             ("🛍️", "#3584e4", "Software"),
    "gnome-software":                 ("🛍️", "#3584e4", "Software"),
    "org.gnome.Terminal":             ("", "#61afef", "Terminal"),
    "gnome-terminal":                 ("", "#61afef", "Terminal"),
    "org.gnome.Console":              ("", "#61afef", "Console"),
    "kgx":                            ("", "#61afef", "Console"),
    "gnome-console":                  ("", "#61afef", "Console"),
    "org.gnome.Epiphany":             ("󰈹", "#3584e4", "Web"),
    "epiphany":                       ("󰈹", "#3584e4", "Web"),
    "org.gnome.Maps":                 ("󰍍", "#3584e4", "Maps"),
    "gnome-maps":                     ("󰍍", "#3584e4", "Maps"),
    "org.gnome.Weather":              ("󰖕", "#3584e4", "Weather"),
    "gnome-weather":                  ("󰖕", "#3584e4", "Weather"),
    "org.gnome.Calendar":             ("󰃭", "#3584e4", "Calendar"),
    "gnome-calendar":                 ("󰃭", "#3584e4", "Calendar"),
    "org.gnome.Contacts":             ("󰊻", "#3584e4", "Contacts"),
    "gnome-contacts":                 ("󰊻", "#3584e4", "Contacts"),
    "org.gnome.Characters":           ("󰜫", "#3584e4", "Characters"),
    "gnome-characters":               ("󰜫", "#3584e4", "Characters"),
    "org.gnome.FontViewer":           ("󰅠", "#3584e4", "Fonts"),
    "gnome-font-viewer":              ("󰅠", "#3584e4", "Fonts"),
    "org.gnome.Logs":                 ("󰌮", "#3584e4", "Logs"),
    "gnome-logs":                     ("󰌮", "#3584e4", "Logs"),
    "org.gnome.Photos":               ("󰉏", "#3584e4", "Photos"),
    "gnome-photos":                   ("󰉏", "#3584e4", "Photos"),
    "org.gnome.Music":                ("󰓃", "#3584e4", "Music"),
    "gnome-music":                    ("󰓃", "#3584e4", "Music"),
    "org.gnome.Totem":                ("", "#3584e4", "Videos"),
    "totem":                          ("", "#3584e4", "Videos"),
    "org.gnome.baobab":               ("󰮗", "#3584e4", "Disk Usage"),
    "baobab":                         ("󰮗", "#3584e4", "Disk Usage"),
    "org.gnome.eog":                  ("󰉏", "#3584e4", "Image Viewer"),
    "eog":                            ("󰉏", "#3584e4", "Image Viewer"),
    "org.gnome.Loupe":                ("󰉏", "#3584e4", "Loupe"),
    "org.gnome.Snapshot":             ("󰄀", "#3584e4", "Camera"),
    "org.gnome.SoundRecorder":        ("󰓃", "#3584e4", "Sound Recorder"),
    "org.gnome.seahorse":             ("󰛋", "#3584e4", "Passwords"),
    "seahorse":                       ("󰛋", "#3584e4", "Passwords"),
    "org.gnome.FileRoller":           ("󰗙", "#3584e4", "Archive Manager"),
    "file-roller":                    ("󰗙", "#3584e4", "Archive Manager"),
    "org.gnome.Extensions":           ("󰛓", "#3584e4", "Extensions"),
    "org.gnome.Tweaks":               ("󰛓", "#3584e4", "Tweaks"),
    "gnome-tweaks":                   ("󰛓", "#3584e4", "Tweaks"),
    "org.gnome.ConnectionManager":    ("󰒓", "#3584e4", "Connections"),
    "gnome-connections":              ("󰒓", "#3584e4", "Connections"),
    "org.gnome.Fractal":              ("󰙯", "#3584e4", "Fractal"),
    "org.gnome.Evolution":            ("󰇮", "#3584e4", "Evolution"),
    "evolution":                      ("󰇮", "#3584e4", "Evolution"),
    "org.gnome.Geary":                ("󰇮", "#3584e4", "Geary"),
    "geary":                          ("󰇮", "#3584e4", "Geary"),
    "org.gnome.gitlab.sushi":         ("󰉏", "#3584e4", "Sushi"),
    "org.gnome.Builder":              ("󰨞", "#3584e4", "Builder"),
    "org.gnome.design.IconLibrary":   ("󰱱", "#3584e4", "Icon Library"),
    "org.gnome.design.Contrast":      ("󰈐", "#3584e4", "Contrast"),
    "org.gnome.design.Palette":       ("󰈐", "#3584e4", "Palette"),
    "org.gnome.World.Secrets":        ("󰛋", "#3584e4", "Secrets"),
    "org.gnome.gitlab.YaLTeR.VideoTrimmer": ("󰐊", "#c061cb", "Video Trimmer"),
    "org.gnome.clocks":               ("󱎫", "#3584e4", "Clocks"),
    "gnome-clocks":                   ("󱎫", "#3584e4", "Clocks"),
    "org.gnome.Zenity":               ("󰘔", "#3584e4", "Zenity"),

    # --- DEVELOPMENT & TERMINALS ---
    "nvim":                           ("", "#57a143", "Neovim"),
    "vim":                            ("", "#019833", "Vim"),
    "code":                           ("󰨞", "#007acc", "VS Code"),
    "ghostty":                        ("", "#cba6f7", "Ghostty"),
    "kitty":                          ("", "#cba6f7", "Kitty"),
    "alacritty":                      ("", "#f9e2af", "Alacritty"),
    "terminator":                     ("", "#e53935", "Terminator"),
    "foot":                           ("󰽒", "#88c0d0", "Foot"),
    "org.omarchy.terminal":           ("", "#f9e2af", "Terminal"),
    "docker":                         ("", "#2496ed", "Docker"),
    "localhost":                      ("", "#00ff00", "Localhost"),
    "Recent Documents": ("󰈚", "#eab308", "Documents"),

    
    # --- EXTRA ---
    "com-tonikelope-megabasterd-mainpanel": ("󰗽", "#d92323", "MegaBuster"),
    
    # --- WEB SERVICES & SHOPPING ---
    "gitlab":                         ("", "#fc6d26", "GitLab"),
    "github-desktop":                 ("󰊤", "#ffffff", "GitHub"),
    "GitHub Desktop":                 ("󰊤", "#ffffff", "GitHub"),
    "io.github.shiftey.Desktop":      ("󰊤", "#ffffff", "GitHub"),
    "github":                         ("󰊤", "#ffffff", "GitHub"),
    "stackoverflow":                  ("", "#f48024", "StackOverflow"),
    "amazon":                         ("", "#ff9900", "Amazon"),
    "cafebazaar":                     ("󰄶", "#42b029", "Bazaar"),
    "ir.cafebazaar":                  ("󰄶", "#42b029", "Bazaar"),
}

def scroll_text(text, width=25):
    """Creates a scrolling marquee effect for music tracks"""
    if len(text) <= width:
        return html.escape(text)
    
    text_with_pad = text + "   ♫   "
    offset = int(time.time() * 2) % len(text_with_pad)
    scrolled = (text_with_pad * 2)[offset:offset+width]
    return html.escape(scrolled)

def get_media_info():
    """Handles Music Visualizer & Scrolling Animation"""
    try:
        cmd = ["playerctl", "metadata", "--format", "{{status}}|||{{playerName}}|||{{title}}|||{{artist}}"]
        output = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, timeout=1).decode().strip()
        
        if output:
            parts = output.split("|||")
            if len(parts) == 4:
                status, player_name, title, artist = parts
                player_name = player_name.lower()
                
                if status == "Playing":
                    is_music_app = any(app in player_name for app in MUSIC_PLAYERS)
                    is_music_web = any(web in title.lower() for web in MUSIC_WEB_KEYWORDS)

                    if is_music_app or is_music_web:
                        bars = PATTERNS[int(time.time() * 2) % PATTERN_LEN]
                        
                        full_track_name = f"{title} - {artist}" if artist else title
                        scrolling_title = scroll_text(full_track_name, width=25)
                        
                        # Retained the Spotify bright green (#1db954) for the animation bars
                        display = f"<span color='#1db954'>{bars}</span> <span color='#cdd6f4'>{scrolling_title}</span> <span color='#1db954'>{bars}</span>"
                        tooltip = f"Now Playing: {html.escape(title)} by {html.escape(artist)} ({player_name.capitalize()})"
                        return display, tooltip
                elif status == "Paused":
                    return "<span color='#f57f17'>󰏤 Paused</span>", "Click to Resume"
    except:
        pass
    return None, None

def get_active_window():
    try:
        output = subprocess.check_output(["hyprctl", "activewindow", "-j"], stderr=subprocess.DEVNULL).decode("utf-8")
        data = json.loads(output)
        
        raw_title = data.get("title", "")
        raw_class = data.get("class", "").lower()
        title_lower = raw_title.lower()

        def format_output(icon, color, app_name, win_title):
            clean_title = win_title
            if app_name == "YouTube":
                clean_title = win_title.replace(" - YouTube", "").replace("YouTube", "").strip()
                clean_title = re.sub(r'\(\d+\)', '', clean_title).strip()
                if not clean_title: clean_title = win_title
                if len(clean_title) > MAX_TITLE_LEN:
                    clean_title = clean_title[:MAX_TITLE_LEN] + "..."
                display = f"<span color='{color}'>{icon}</span>  {app_name} <span color='#788587'>|</span> <span color='#dcd6d6'>{html.escape(clean_title)}</span>"
            else:
                display = f"<span color='{color}'>{icon}</span>  {app_name}"

            if clean_title and clean_title != app_name:
                tooltip = f"{app_name} — {html.escape(win_title)}"
            else:
                tooltip = app_name
            return display, tooltip

        # 1. Title match first (catches web apps in browsers: YouTube, Gmail, GitHub, etc.)
        for key, (icon, color, name) in APP_RULES.items():
            key_lower = key.lower()
            if re.search(r'\b' + re.escape(key_lower) + r'\b', title_lower):
                return format_output(icon, color, name, raw_title)

        # 2. Class match second (native apps: Discord, Code, terminal, etc.)
        for key, (icon, color, name) in APP_RULES.items():
            key_lower = key.lower()
            if key_lower in raw_class:
                return format_output(icon, color, name, raw_title)
        
        # 3. Desktop Check
        if not raw_class:
            return "<span color='#dcd6d6'>󱂬</span> Desktop", "Workspace"

        # 4. Fallback for unrecognized apps 
        clean_name = raw_class.replace("org.gnome.", "").replace("org.kde.", "").replace("com.", "").replace(".desktop", "")
        if "mitchellh." in clean_name: clean_name = clean_name.replace("mitchellh.", "")
        
        clean_name = clean_name.capitalize()
        
        # Fallback to a neutral text color (#dcd6d6) if not found in your list
        hex_color = "#dcd6d6"
        
        if "gnome" in raw_class: icon = ""
        elif "kde" in raw_class: icon = ""
        else: icon = ""

        return format_output(icon, hex_color, clean_name, raw_title)

    except:
        return "<span color='#dcd6d6'>󱂬</span> Desktop", "Workspace"

if __name__ == "__main__":
    media_text, media_tooltip = get_media_info()
    if media_text:
        display_text = media_text
        tooltip_text = media_tooltip
    else:
        display_text, tooltip_text = get_active_window()
    print(json.dumps({"text": display_text, "tooltip": tooltip_text}))
