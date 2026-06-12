---
id: 03b-gpu-driver
source: /home/shorin/Documents/github/shorin-arch-setup/scripts/03b-gpu-driver.sh
source_relative: scripts/03b-gpu-driver.sh
phase: optional-hardware
risk: high
requires_root: true
language: bash
mode: "0644"
sha256: "569b96f3ba51597ac09186991859e29ad6a9c9c966a6ba53e092e6bd1f9e5f85"
generated_from: bash-source
---

# 03b-gpu-driver

## Intent

Install chwd and run automatic hardware driver detection.

## Declarative Reading Notes

This module is a Markdown declaration of the original Bash behavior. Treat the embedded Bash as
source evidence, not as the preferred execution path. When applying this module, first audit the
current system state, then apply only the missing state described by package, file, service, and
verification sections.

## Extracted Mutating Commands

### aur_helper

- `exe runuser -u "$TARGET_USER" -- yay -S --noconfirm --needed --answerdiff=None --answerclean=None chwd-arch-git`

### file_mutations

- `rm -f "$SUDO_TEMP_FILE"`


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
# 03b-gpu-driver.sh GPU Driver Installer (Powered by chwd)
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "$SCRIPT_DIR/00-utils.sh" ]; then
    source "$SCRIPT_DIR/00-utils.sh"
else
    echo "Error: 00-utils.sh not found."
    exit 1
fi

check_root

section "Phase 2b" "GPU Driver Setup"

DETECTED_USER=$(awk -F: '$3 == 1000 {print $1}' /etc/passwd)
TARGET_USER="${DETECTED_USER:-$(read -p "Target user: " u && echo $u)}"

#--------------sudo temp file--------------------#
SUDO_TEMP_FILE="/etc/sudoers.d/99_shorin_installer_temp"
echo "$TARGET_USER ALL=(ALL) NOPASSWD: ALL" >"$SUDO_TEMP_FILE"
chmod 440 "$SUDO_TEMP_FILE"
log "Temp sudo file created..."

cleanup_sudo() {
    if [ -f "$SUDO_TEMP_FILE" ]; then
        rm -f "$SUDO_TEMP_FILE"
        log "Security: Temporary sudo privileges revoked."
    fi
}
trap cleanup_sudo EXIT INT TERM

# ==============================================================================
# 1. 安装你的专属硬件检测工具
# ==============================================================================
log "Installing chwd-arch-git from AUR..."
exe runuser -u "$TARGET_USER" -- yay -S --noconfirm --needed --answerdiff=None --answerclean=None chwd-arch-git

# ==============================================================================
# 2. 自动检测并安装驱动
# ==============================================================================
log "Running Automated Hardware Detection and Driver Installation..."
# -a 自动配置所有匹配的 PCI 设备
chwd -a

# 检查上一条命令是否成功
if [ $? -eq 0 ]; then
    success "Hardware drivers installed via chwd."
else
    warn "chwd encountered an error. Please check pacman logs."
fi

log "Module 03b completed."
~~~~
