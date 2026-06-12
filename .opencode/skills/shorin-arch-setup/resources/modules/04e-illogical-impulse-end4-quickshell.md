---
id: 04e-illogical-impulse-end4-quickshell
source: /home/shorin/Documents/github/shorin-arch-setup/scripts/04e-illogical-impulse-end4-quickshell.sh
source_relative: scripts/04e-illogical-impulse-end4-quickshell.sh
phase: desktop
risk: critical
requires_root: false
language: bash
mode: "0644"
sha256: "d9e1c25270dd90551a1486a4cc0744c93b8a9d53d3f0b5c9d48b2ddc284cc35d"
generated_from: bash-source
---

# 04e-illogical-impulse-end4-quickshell

## Intent

Run external Illogical Impulse End4 installer and configure display manager.

## Declarative Reading Notes

This module is a Markdown declaration of the original Bash behavior. Treat the embedded Bash as
source evidence, not as the preferred execution path. When applying this module, first audit the
current system state, then apply only the missing state described by package, file, service, and
verification sections.

## Extracted Mutating Commands

### external

- `if curl -fsSL "$II_URL" -o "$INSTALLER_SCRIPT"; then`

### file_mutations

- `rm -f "$SUDO_TEMP_FILE"`
- `rm -f "$INSTALLER_SCRIPT"`


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
# 04e-illogical-impulse-end4-quickshell.sh

# 1. 引用工具库
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PARENT_DIR="$(dirname "$SCRIPT_DIR")"
if [ -f "$SCRIPT_DIR/00-utils.sh" ]; then
    source "$SCRIPT_DIR/00-utils.sh"
else
    echo "Error: 00-utils.sh not found."
    exit 1
fi
log "installing Illogical Impulse End4 (Quickshell)..."

# ==============================================================================
#  Identify User & DM Check
# ==============================================================================
log "Identifying user..."
detect_target_user
info_kv "Target" "$TARGET_USER"

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

# DM Check
check_dm_conflict

log "Target user for End4 installation: $TARGET_USER"
# ==============================================================================
#  install
# ==============================================================================
section "Desktop" "illogical-impulse"
# 下载并执行安装脚本
INSTALLER_SCRIPT="/tmp/end4_install.sh"
II_URL="https://ii.clsty.link/get"

log "Downloading Illogical Impulse installer wrapper..."
if curl -fsSL "$II_URL" -o "$INSTALLER_SCRIPT"; then
    
    chmod +x "$INSTALLER_SCRIPT"
    chown "$TARGET_USER" "$INSTALLER_SCRIPT"
    
    log "Executing End4 installer as user ($TARGET_USER)..."
    log "NOTE: If the installer asks for input, this script might hang."
    
    if runuser -u "$TARGET_USER" -- bash -c "cd ~ && $INSTALLER_SCRIPT"; then
        success "Illogical Impulse End4 installed successfully."
    else
        # 安装失败不应该导致整个系统安装退出，所以只警告
        warn "End4 installer returned an error code. You may need to install it manually."
    fi
    rm -f "$INSTALLER_SCRIPT"
else
    warn "Failed to download installer script from $II_URL."
fi
# === 隐藏多余的 Desktop 图标 ===
section "Config" "Hiding useless .desktop files"
log "Hiding useless .desktop files"
run_hide_desktop_file

# ==============================================================================
#  autologin
# ==============================================================================
section "Config" "Display Manager"

if [ "$SKIP_DM" = true ]; then
    log "Display Manager setup skipped (Conflict found or user opted out)."
    warn "You will need to start your session manually from the TTY."
else
    
    setup_ly
fi

log "Module 04e (End4) completed."

~~~~
