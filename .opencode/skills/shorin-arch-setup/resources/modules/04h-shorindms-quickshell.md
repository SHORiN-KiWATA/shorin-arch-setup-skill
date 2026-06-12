---
id: 04h-shorindms-quickshell
source: /home/shorin/Documents/github/shorin-arch-setup/scripts/04h-shorindms-quickshell.sh
source_relative: scripts/04h-shorindms-quickshell.sh
phase: desktop
risk: high
requires_root: true
language: bash
mode: "0644"
sha256: "d163b2744583298490279061b619b5a2a94ae4ed31481e7e343c934a08f8abcd"
generated_from: bash-source
---

# 04h-shorindms-quickshell

## Intent

Install Shorin DMS Niri meta package and run shorindms init.

## Declarative Reading Notes

This module is a Markdown declaration of the original Bash behavior. Treat the embedded Bash as
source evidence, not as the preferred execution path. When applying this module, first audit the
current system state, then apply only the missing state described by package, file, service, and
verification sections.

## Extracted Mutating Commands

### aur_helper

- `if ! as_user "$AUR_HELPER" -S --noconfirm --needed $PRE_PKGS; then`
- `if as_user "$AUR_HELPER" -Si "$CORE_PKG" &>/dev/null; then`
- `as_user "$AUR_HELPER" -Si "$CORE_PKG" | grep "^Depends On" | cut -d':' -f2- | tr -s ' ' '\n' | sed -e 's/[<>=].*//g' -e '/^$/d' -e '/None/d' >> "$VERIFY_LIST"`
- `if ! as_user "$AUR_HELPER" -S --noconfirm --needed "$CORE_PKG"; then`

### file_mutations

- `rm -f "$VERIFY_LIST"`
- `rm -f "$SUDO_TEMP_FILE"`
- `as_user mkdir -p "$WALLPAPER_DIR"`


## Extracted Package/App State Variables

### PRE_PKGS

- `quickshell-git`
- `vulkan-headers`
- `xdg-desktop-portal-gnome`

### CORE_PKG

- `shorin-dms-niri-git`


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
# 04-dms-setup.sh - DMS Desktop (Pre-install separated + Pre-Verify)
# ==============================================================================

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
rm -f "$VERIFY_LIST"

# --- Identify User & DM Check ---
log "Identifying target user..."
detect_target_user


if [[ -z "$TARGET_USER" || ! -d "$HOME_DIR" ]]; then
    error "Target user invalid or home directory does not exist."
    exit 1
fi

info_kv "Target User" "$TARGET_USER"
check_dm_conflict
log "DM Check result $SKIP_DM"
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

critical_failure_handler() {
    local failed_reason="$1"
    trap - ERR
    echo -e "\n\033[0;31m[CRITICAL FAILURE] $failed_reason\033[0m\n"
    # 这里省略了你原有的报错大框框，保持原有逻辑即可
    exit 1
}
trap 'critical_failure_handler "Script Error at Line $LINENO"' ERR

AUR_HELPER="paru"

# ==============================================================================
# STEP 1: Pre-requisites Installation
# ==============================================================================
section "Shorin DMS" "Installing Pre-requisites"

PRE_PKGS="quickshell-git vulkan-headers xdg-desktop-portal-gnome"

log "Generating verify list for pre-requisites..."
echo "$PRE_PKGS" | tr ' ' '\n' >> "$VERIFY_LIST"

log "Installing pre-requisites explicitly..."
if ! as_user "$AUR_HELPER" -S --noconfirm --needed $PRE_PKGS; then
    critical_failure_handler "Failed to install pre-requisites: $PRE_PKGS"
fi

# ==============================================================================
# STEP 2: Core Meta Environment
# ==============================================================================
section "Shorin DMS" "Installing Core Environment"
CORE_PKG="shorin-dms-niri-git"

log "Fetching dependency list from AUR for verification..."
echo "$CORE_PKG" >> "$VERIFY_LIST"
# 使用 -Si 查询远程信息，提前写入清单 (剥离版本号 <>=)
if as_user "$AUR_HELPER" -Si "$CORE_PKG" &>/dev/null; then
    as_user "$AUR_HELPER" -Si "$CORE_PKG" | grep "^Depends On" | cut -d':' -f2- | tr -s ' ' '\n' | sed -e 's/[<>=].*//g' -e '/^$/d' -e '/None/d' >> "$VERIFY_LIST"
    log "Dependencies added to $VERIFY_LIST."
else
    warn "Could not fetch remote dependency info for $CORE_PKG. Skipping verify list append."
fi

log "Installing $CORE_PKG environment via AUR..."
if ! as_user "$AUR_HELPER" -S --noconfirm --needed "$CORE_PKG"; then
    critical_failure_handler "Failed to install $CORE_PKG"
fi

# ==============================================================================
# STEP 3: Initialize Dotfiles & Environment
# ==============================================================================
log "Initializing User Dotfiles and Environment..."
exe as_user shorindms init

# ==============================================================================
# STEP 4: Static Resources
# ==============================================================================
section "Shorin DMS" "Wallpapers & Tutorials"

log "Deploying wallpapers..."
WALLPAPER_SOURCE_DIR="$PARENT_DIR/resources/Wallpapers"
WALLPAPER_DIR="$HOME_DIR/Pictures/Wallpapers"
if [ -d "$WALLPAPER_SOURCE_DIR" ]; then
    as_user mkdir -p "$WALLPAPER_DIR"
    force_copy "$WALLPAPER_SOURCE_DIR/." "$WALLPAPER_DIR/"
    chown -R "$TARGET_USER:" "$WALLPAPER_DIR"
fi

# ==============================================================================
# Finalization & Auto-Login
# ==============================================================================
section "Final" "Auto-Login & Cleanup"


log "Cleaning up legacy TTY autologin configs..."

if [[ "$SKIP_DM" == false ]]; then
    setup_ly
fi

success "Shorin DMS Niri Installation Complete!"
~~~~
