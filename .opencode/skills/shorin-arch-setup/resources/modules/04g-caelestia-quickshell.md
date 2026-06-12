---
id: 04g-caelestia-quickshell
source: /home/shorin/Documents/github/shorin-arch-setup/scripts/04g-caelestia-quickshell.sh
source_relative: scripts/04g-caelestia-quickshell.sh
phase: desktop
risk: critical
requires_root: false
language: bash
mode: "0644"
sha256: "f1d039f47742ee111ec522599d0bd511097cfb36cbdcfc2917d6c1873620cd72"
generated_from: bash-source
---

# 04g-caelestia-quickshell

## Intent

Clone Caelestia dots, run its installer, add file-manager deps, and configure display manager.

## Declarative Reading Notes

This module is a Markdown declaration of the original Bash behavior. Treat the embedded Bash as
source evidence, not as the preferred execution path. When applying this module, first audit the
current system state, then apply only the missing state described by package, file, service, and
verification sections.

## Extracted Mutating Commands

### aur_helper

- `exe yay -Syu --needed --noconfirm fish`
- `exe yay -S --needed --noconfirm thunar tumbler ffmpegthumbnailer poppler-glib gvfs-smb file-roller thunar-archive-plugin gnome-keyring polkit-gnome rime-wanxiang-gram-zh-hans`

### external

- `if exe as_user git clone "$CAELESTIA_REPO" "$CAELESTIA_DIR"; then`

### file_mutations

- `rm -f "$SUDO_TEMP_FILE"`
- `rm -rf "$CAELESTIA_DIR"`


## Extracted Package/App State Variables

No package or app state variables were extracted.

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
#!/bin/bash

# ==============================================================================
#  1. Load Utilities
# ==============================================================================
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

if [ -f "$SCRIPT_DIR/00-utils.sh" ]; then
    source "$SCRIPT_DIR/00-utils.sh"
else
    echo "Error: 00-utils.sh not found."
    exit 1
fi

section "Start" "Installing Caelestia (Quickshell)..."

# ==============================================================================
#  2. Identify User & Display Manager Check
# ==============================================================================
log "Identifying target user..."

# Detect user ID 1000 or prompt manually
detect_target_user

info_kv "Target User" "$TARGET_USER"
info_kv "Home Dir"    "$HOME_DIR"

check_dm_conflict

# ==============================================================================
#  3. Temporary Sudo Access
# ==============================================================================
# Grant passwordless sudo temporarily for the installer to run smoothly
SUDO_TEMP_FILE="/etc/sudoers.d/99_shorin_installer_temp"
echo "$TARGET_USER ALL=(ALL) NOPASSWD: ALL" >"$SUDO_TEMP_FILE"
chmod 440 "$SUDO_TEMP_FILE"
log "Privilege escalation: Temporary passwordless sudo enabled."

cleanup_sudo() {
    if [ -f "$SUDO_TEMP_FILE" ]; then
        rm -f "$SUDO_TEMP_FILE"
        log "Security: Temporary sudo privileges revoked."
    fi
}
trap cleanup_sudo EXIT INT TERM

# ==============================================================================
#  4. Installation (Caelestia)
# ==============================================================================
section "Repo" "Cloning Caelestia Repository"

CAELESTIA_REPO="https://github.com/caelestia-dots/caelestia.git"
CAELESTIA_DIR="$HOME_DIR/.local/share/caelestia"

# Clone to .local (Caelestia uses symlinks, not direct copies)
log "Cloning repository to $CAELESTIA_DIR ..."
if [ -d $CAELESTIA_DIR ]; then
    warn "Repository clone failed or already exists. Deleting..."
    rm -rf "$CAELESTIA_DIR"
fi

if exe as_user git clone "$CAELESTIA_REPO" "$CAELESTIA_DIR"; then
    chown -R $TARGET_USER $CAELESTIA_DIR
    log "repo cloned."
fi

log "Ensuring fish shell is installed..."
exe yay -Syu --needed --noconfirm fish

section "Install" "Running Caelestia Installer"

# Switch to user, go home, and run the installer
if as_user sh -c "cd && fish $CAELESTIA_DIR/install.fish --noconfirm"; then
    chown -R $TARGET_USER $HOME_DIR/.config
    success "Caelestia installation script completed."
fi

# ==============================================================================
#  file manager
# ==============================================================================
section "config" "file manager"

if ! command -v thunar; then
    
    exe yay -S --needed --noconfirm thunar tumbler ffmpegthumbnailer poppler-glib gvfs-smb file-roller thunar-archive-plugin gnome-keyring polkit-gnome rime-wanxiang-gram-zh-hans
    
fi

# === 隐藏多余的 Desktop 图标 ===
section "Config" "Hiding useless .desktop files"
log "Hiding useless .desktop files"
run_hide_desktop_file

# ==============================================================================
#  6. dispaly manager
# ==============================================================================
section "Config" "Display Manager"

if [ "$SKIP_DM" = true ]; then
    log "Display Manager setup skipped (Conflict found or user opted out)."
    warn "You will need to start your session manually from the TTY."
else
    
    setup_ly
fi

section "End" "Module 04e (Caelestia) Completed"

~~~~
