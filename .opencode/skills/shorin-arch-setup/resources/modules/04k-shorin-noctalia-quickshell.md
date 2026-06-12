---
id: 04k-shorin-noctalia-quickshell
source: /home/shorin/Documents/github/shorin-arch-setup/scripts/04k-shorin-noctalia-quickshell.sh
source_relative: scripts/04k-shorin-noctalia-quickshell.sh
phase: desktop
risk: high
requires_root: true
language: bash
mode: "0644"
sha256: "52e79451c99cb08e9af53a5f9caa4d8bc7cb31df61732f88c0fe6a97ed928de1"
generated_from: bash-source
---

# 04k-shorin-noctalia-quickshell

## Intent

Install Shorin Noctalia Niri profile from local dotfiles.

## Declarative Reading Notes

This module is a Markdown declaration of the original Bash behavior. Treat the embedded Bash as
source evidence, not as the preferred execution path. When applying this module, first audit the
current system state, then apply only the missing state described by package, file, service, and
verification sections.

## Extracted Mutating Commands

### pacman

- `exe pacman -S --noconfirm --needed $FM_PKGS1`

### aur_helper

- `exe as_user "$AUR_HELPER" -S --noconfirm --needed $CORE_PKGS`
- `exe as_user "$AUR_HELPER" -S --noconfirm --needed $FM_PKGS2`
- `exe as_user "$AUR_HELPER" -S --noconfirm --needed $TERM_PKGS`
- `exe as_user "$AUR_HELPER" -S --noconfirm --needed bazaar`
- `exe as_user "$AUR_HELPER" -S --noconfirm --needed $THEME_PKGS`

### flatpak

- `if command -v flatpak &>/dev/null; then`
- `as_user flatpak override --user --filesystem=xdg-data/themes`
- `as_user flatpak override --user --filesystem="$HOME_DIR/.themes"`
- `as_user flatpak override --user --filesystem=xdg-config/gtk-4.0`
- `as_user flatpak override --user --filesystem=xdg-config/gtk-3.0`
- `as_user flatpak override --user --env=GTK_THEME=adw-gtk3-dark`
- `as_user flatpak override --user --filesystem=xdg-config/fontconfig`

### file_mutations

- `rm -f "$VERIFY_LIST" # 确保每次运行生成全新的订单`
- `rm -f "$SUDO_TEMP_FILE"`
- `as_user mkdir -p "$WALLPAPER_DIR"`
- `as_user mkdir -p "$HOME_DIR/Templates"`
- `as_user sed -i "s/shorin/$TARGET_USER/g" "$HOME_DIR/.config/gtk-3.0/bookmarks"`
- `exe mkdir -p "$POL_DIR"`
- `rm -f /etc/systemd/system/getty@tty1.service.d/autologin.conf 2>/dev/null`


## Extracted Package/App State Variables

### CORE_PKGS

- `noctalia-shell`
- `niri`
- `xwayland-satellite`
- `kitty`
- `xdg-desktop-portal-gnome`
- `niri-sidebar-git`
- `satty`
- `mpv`
- `polkit-gnome`

### FM_PKGS1

- `ffmpegthumbnailer`
- `gvfs-smb`
- `nautilus-open-any-terminal`
- `file-roller`
- `gnome-keyring`
- `gst-plugins-base`
- `gst-plugins-good`
- `gst-libav`
- `nautilus`
- `icoextract`
- `python-pillow`

### FM_PKGS2

- `xdg-desktop-portal-gtk`
- `thunar`
- `tumbler`
- `ffmpegthumbnailer`
- `poppler-glib`
- `gvfs-smb`
- `file-roller`
- `thunar-archive-plugin`
- `gnome-keyring`
- `thunar-volman`
- `gvfs-mtp`
- `gvfs-gphoto2`
- `webp-pixbuf-loader`
- `libgsf`

### TERM_PKGS

- `linuxqq-clipsync-git`
- `xdg-terminal-exec`
- `bat`
- `fuzzel`
- `wf-recorder`
- `wl-screenrec-git`
- `ttf-jetbrains-maple-mono-nf-xx-xx`
- `eza`
- `zoxide`
- `starship`
- `jq`
- `fish`
- `libnotify`
- `timg`
- `imv`
- `cava`
- `imagemagick`
- `wl-clipboard`
- `cliphist`
- `shorin-contrib-git`
- `slurp`
- `opencode`
- `rime-wanxiang-gram-zh-hans`

### THEME_PKGS

- `matugen`
- `adw-gtk-theme`
- `python-pywalfox`
- `firefox`
- `nwg-look`
- `breeze-cursors`


## Verification Guidance

- Verify packages mentioned by package-manager commands are installed.
- Verify files mentioned by file mutation commands exist and contain the desired state.
- Verify services mentioned by `systemctl` commands are enabled or active as declared.
- For high or critical risk modules, create or confirm a relevant Btrfs/snapper checkpoint first.

## Rollback Guidance

- Prefer Btrfs/snapper rollback markers when the module changes system state.
- For desktop-stage changes, prefer the `Before Desktop Environments` checkpoint.
- For base-stage changes, prefer the `Before Shorin Setup` checkpoint.
- Do not run destructive rollback commands without explicit user confirmation.

## Legacy Bash Source

~~~~bash
#!/usr/bin/env bash

# --- Import Utilities ---
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

if [[ -f "$SCRIPT_DIR/00-utils.sh" ]]; then
    source "$SCRIPT_DIR/00-utils.sh"
else
    echo "Error: 00-utils.sh not found in $SCRIPT_DIR."
    exit 1
fi

check_root
VERIFY_LIST="/tmp/shorin_install_verify.list"
rm -f "$VERIFY_LIST" # 确保每次运行生成全新的订单

# --- Identify User & DM Check ---
log "Identifying target user..."
detect_target_user

if [[ -z "$TARGET_USER" || ! -d "$HOME_DIR" ]]; then
    error "Target user invalid or home directory does not exist."
    exit 1
fi

info_kv "Target User" "$TARGET_USER"

check_dm_conflict

# --- Temporary Sudo Privileges ---
log "Granting temporary sudo privileges..."
SUDO_TEMP_FILE="/etc/sudoers.d/99_shorin_installer_temp"
echo "$TARGET_USER ALL=(ALL) NOPASSWD: ALL" > "$SUDO_TEMP_FILE"
chmod 440 "$SUDO_TEMP_FILE"

cleanup_sudo() {
    if [[ -f "$SUDO_TEMP_FILE" ]]; then
        rm -f "$SUDO_TEMP_FILE"
        log "Security: Temporary sudo privileges revoked."
    fi
}
trap cleanup_sudo EXIT INT TERM

# --- Installation: Core Components ---
AUR_HELPER="paru"
section "Shorin Noctalia" "Core Components"
log "Installing core shell components..."

CORE_PKGS="noctalia-shell niri xwayland-satellite kitty xdg-desktop-portal-gnome niri-sidebar-git satty mpv polkit-gnome "

echo "$CORE_PKGS" >> "$VERIFY_LIST"
exe as_user "$AUR_HELPER" -S --noconfirm --needed $CORE_PKGS

# --- Dotfiles & Wallpapers ---
section "Shorin Noctalia" "Dotfiles & Wallpapers"
log "Deploying user dotfiles..."
DOTFILES_SRC="$PARENT_DIR/noctalia-dotfiles"
chown -R "$TARGET_USER:" "$DOTFILES_SRC"
force_copy "$DOTFILES_SRC/." "$HOME_DIR"

log "Deploying wallpapers..."
WALLPAPER_SOURCE_DIR="$PARENT_DIR/resources/Wallpapers"
WALLPAPER_DIR="$HOME_DIR/Pictures/Wallpapers"
chown -R "$TARGET_USER:" "$WALLPAPER_SOURCE_DIR"
as_user mkdir -p "$WALLPAPER_DIR"
force_copy "$WALLPAPER_SOURCE_DIR/." "$WALLPAPER_DIR/"


# --- File Manager & Terminal Setup ---
section "Shorin Noctalia" "File Manager & Terminal"
log "Installing Nautilus, Thunar and dependencies..."
FM_PKGS1="ffmpegthumbnailer gvfs-smb nautilus-open-any-terminal file-roller gnome-keyring gst-plugins-base gst-plugins-good gst-libav nautilus icoextract python-pillow"
FM_PKGS2="xdg-desktop-portal-gtk thunar tumbler ffmpegthumbnailer poppler-glib gvfs-smb file-roller thunar-archive-plugin gnome-keyring thunar-volman gvfs-mtp gvfs-gphoto2 webp-pixbuf-loader libgsf"

echo "$FM_PKGS1" >> "$VERIFY_LIST"
echo "$FM_PKGS2" >> "$VERIFY_LIST"

exe pacman -S --noconfirm --needed $FM_PKGS1
exe as_user "$AUR_HELPER" -S --noconfirm --needed $FM_PKGS2
# 创建模板文件
as_user mkdir -p "$HOME_DIR/Templates"
as_user touch "$HOME_DIR/Templates/new" "$HOME_DIR/Templates/new.sh"
as_user bash -c "echo '#!/usr/bin/env bash' >> '$HOME_DIR/Templates/new.sh'"
chown -R "$TARGET_USER:" "$HOME_DIR/Templates"
# Nautilus 配置
log "Applying Nautilus bugfixes and bookmarks..."
configure_nautilus_user
# bookmarks修复
as_user sed -i "s/shorin/$TARGET_USER/g" "$HOME_DIR/.config/gtk-3.0/bookmarks"


# --- Terminal Utilities ---
section "Shorin Noctalia" "Terminal Utilities"
log "Installing terminal utilities..."
TERM_PKGS="linuxqq-clipsync-git xdg-terminal-exec bat fuzzel wf-recorder wl-screenrec-git ttf-jetbrains-maple-mono-nf-xx-xx eza zoxide starship jq fish libnotify timg imv cava imagemagick wl-clipboard cliphist shorin-contrib-git slurp opencode rime-wanxiang-gram-zh-hans"

echo "$TERM_PKGS" >> "$VERIFY_LIST"
exe as_user "$AUR_HELPER" -S --noconfirm --needed $TERM_PKGS
# shorin-contrib
log "Linking shorin-contrib..."
as_user shorin link
# 默认终端处理
log "Configuring default terminal and templates..."
if ! grep -q "kitty" "$HOME_DIR/.config/xdg-terminals.list"; then
    echo 'kitty.desktop' >> "$HOME_DIR/.config/xdg-terminals.list"
fi
sudo -u "$TARGET_USER" dbus-run-session gsettings set com.github.stunkymonkey.nautilus-open-any-terminal terminal kitty
# xterm链接
if command -v kitty &>/dev/null; then
    exe ln -sf /usr/bin/kitty /usr/local/bin/xterm
fi

# --- Flatpak & Theme Integration ---
section "Shorin Noctalia" "Flatpak & Theme Integration"

if command -v flatpak &>/dev/null; then
    log "Configuring Flatpak overrides and themes..."
    echo "bazaar" >> "$VERIFY_LIST"
    exe as_user "$AUR_HELPER" -S --noconfirm --needed bazaar
    as_user flatpak override --user --filesystem=xdg-data/themes
    as_user flatpak override --user --filesystem="$HOME_DIR/.themes"
    as_user flatpak override --user --filesystem=xdg-config/gtk-4.0
    as_user flatpak override --user --filesystem=xdg-config/gtk-3.0
    as_user flatpak override --user --env=GTK_THEME=adw-gtk3-dark
    as_user flatpak override --user --filesystem=xdg-config/fontconfig
    as_user ln -sf /usr/share/themes "$HOME_DIR/.local/share/themes"
fi

# === Theme Components & Browser ===
log "Installing theme components and browser..."
THEME_PKGS="matugen adw-gtk-theme python-pywalfox firefox nwg-look breeze-cursors"
echo "$THEME_PKGS" >> "$VERIFY_LIST"
exe as_user "$AUR_HELPER" -S --noconfirm --needed $THEME_PKGS

# 配置 Firefox Pywalfox 与 uBlock Origin 插件安装政策
log "Configuring Firefox extensions policy..."
POL_DIR="/etc/firefox/policies"
exe mkdir -p "$POL_DIR"
cat << 'EOF' > "$POL_DIR/policies.json"
{
  "policies": {
    "Extensions": {
      "Install": [
        "https://addons.mozilla.org/firefox/downloads/latest/pywalfox/latest.xpi",
        "https://addons.mozilla.org/firefox/downloads/latest/ublock-origin/latest.xpi"
      ]
    }
  }
}
EOF
exe chmod 755 "$POL_DIR"
exe chmod 644 "$POL_DIR/policies.json"


# --- Desktop Cleanup & Tutorials ---
section "Config" "Desktop Cleanup"
log "Hiding unnecessary .desktop icons..."
run_hide_desktop_file
log "Copying tutorial files..."
force_copy "$PARENT_DIR/resources/必看-Shorin-Noctalia-Niri使用方法.txt" "$HOME_DIR"

# --- Finalization & Auto-Login ---
section "Final" "Auto-Login & Cleanup"


# --- display manager setup ---
log "Cleaning up legacy TTY autologin configs..."
rm -f /etc/systemd/system/getty@tty1.service.d/autologin.conf 2>/dev/null

if [ "$SKIP_DM" = true ]; then
    log "Display Manager setup skipped (Conflict found or user opted out)."
    warn "You will need to start your session manually from the TTY."
else
    
    setup_ly
fi


~~~~
