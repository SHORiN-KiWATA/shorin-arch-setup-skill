---
id: 04-niri-setup
source: /home/shorin/Documents/github/shorin-arch-setup/scripts/04-niri-setup.sh
source_relative: scripts/04-niri-setup.sh
phase: desktop
risk: high
requires_root: true
language: bash
mode: "0644"
sha256: "f4c51d90f71634b487ca0b1a7bbcf8ffc9f5ed1f8ce064134bc58ce0bae2a380"
generated_from: bash-source
---

# 04-niri-setup

## Intent

Install Shorin Niri meta package, run shorinniri init, copy wallpapers, and configure display manager.

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
- `cleanup_sudo() { rm -f "$SUDO_TEMP_FILE"; }`
- `as_user mkdir -p "$WALLPAPER_DIR"`
- `rm -f "$SUDO_TEMP_FILE"`


## Extracted Package/App State Variables

### CORE_PKG

- `shorin-niri-git`

### PRE_PKGS

- `xdg-desktop-portal-gnome`


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
# 04-niri-setup.sh - Niri Desktop (Refactored & Pre-Verify)
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

source "$SCRIPT_DIR/00-utils.sh"
VERIFY_LIST="/tmp/shorin_install_verify.list"
rm -f "$VERIFY_LIST"

check_root
detect_target_user
check_dm_conflict

SUDO_TEMP_FILE="/etc/sudoers.d/99_shorin_installer_temp"
echo "$TARGET_USER ALL=(ALL) NOPASSWD: ALL" >"$SUDO_TEMP_FILE"
chmod 440 "$SUDO_TEMP_FILE"

cleanup_sudo() { rm -f "$SUDO_TEMP_FILE"; }
trap cleanup_sudo EXIT INT TERM

critical_failure_handler() {
    local failed_reason="$1"
    trap - ERR
    echo -e "\n\033[0;31m[CRITICAL FAILURE] $failed_reason\033[0m\n"
    exit 1
}
trap 'critical_failure_handler "Script Error at Line $LINENO"' ERR

# ==============================================================================
# STEP 1: Install Meta Package & Initialize Environment
# ==============================================================================
section "Step 1/3" "Install Environment & Dotfiles"

AUR_HELPER="paru"
CORE_PKG="shorin-niri-git"
PRE_PKGS="xdg-desktop-portal-gnome"

log "Generating verify list for pre-requisites..."
echo "$PRE_PKGS" | tr ' ' '\n' >> "$VERIFY_LIST"

log "Installing pre-requisites explicitly..."
if ! as_user "$AUR_HELPER" -S --noconfirm --needed $PRE_PKGS; then
    critical_failure_handler "Failed to install pre-requisites: $PRE_PKGS"
fi



# --- 在安装发生【之前】动态提取依赖写入 VERIFY_LIST ---
log "Fetching dependency list from AUR for verification..."
echo "$CORE_PKG" >> "$VERIFY_LIST"

if as_user "$AUR_HELPER" -Si "$CORE_PKG" &>/dev/null; then
    as_user "$AUR_HELPER" -Si "$CORE_PKG" | grep "^Depends On" | cut -d':' -f2- | tr -s ' ' '\n' | sed -e 's/[<>=].*//g' -e '/^$/d' -e '/None/d' >> "$VERIFY_LIST"
    log "Dependencies added to $VERIFY_LIST."
else
    warn "Could not fetch remote dependency info for $CORE_PKG. Skipping verify list append."
fi
# --------------------------------------------------------

# 1. 委托 AUR 助手安装大包
log "Installing $CORE_PKG and all its dependencies via AUR..."
if ! as_user "$AUR_HELPER" -S --noconfirm --needed "$CORE_PKG"; then
    critical_failure_handler "Failed to install '$CORE_PKG' from AUR."
fi

# 2. 调用 CLI 脚本完成初始化
log "Running shorinniri initialization..."
exe as_user shorinniri init

# ==============================================================================
# STEP 2: Deploy Static Resources
# ==============================================================================
section "Step 2/3" "Static Resources"

log "Deploying wallpapers..."
WALLPAPER_SOURCE_DIR="$PARENT_DIR/resources/Wallpapers"
WALLPAPER_DIR="$HOME_DIR/Pictures/Wallpapers"
if [ -d "$WALLPAPER_SOURCE_DIR" ]; then
    as_user mkdir -p "$WALLPAPER_DIR"
    force_copy "$WALLPAPER_SOURCE_DIR/." "$WALLPAPER_DIR/"
    chown -R "$TARGET_USER:" "$WALLPAPER_DIR"
fi

# ==============================================================================
# STEP 3: Display Manager & Cleanup
# ==============================================================================
section "Step 3/3" "Cleanup & Boot Configuration"



log "Cleaning up legacy TTY autologin configs..."

if [ "$SKIP_DM" = true ]; then
    warn "You will need to start your session manually from the TTY."
else
    setup_ly
fi
rm -f "$SUDO_TEMP_FILE"
trap - ERR
success "Module 04 completed successfully. Shorin Niri is ready!"
~~~~
