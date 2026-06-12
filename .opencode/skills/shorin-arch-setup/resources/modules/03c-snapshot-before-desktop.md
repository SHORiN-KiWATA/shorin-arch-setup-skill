---
id: 03c-snapshot-before-desktop
source: /home/shorin/Documents/github/shorin-arch-setup/scripts/03c-snapshot-before-desktop.sh
source_relative: scripts/03c-snapshot-before-desktop.sh
phase: checkpoint
risk: medium
requires_root: true
language: bash
mode: "0644"
sha256: "097a353182835b79abc5f207219a65381d0bc6e87a448fb10584f042ea179f43"
generated_from: bash-source
---

# 03c-snapshot-before-desktop

## Intent

Create the pre-desktop snapper checkpoint and remove stale compositor autostarts.

## Declarative Reading Notes

This module is a Markdown declaration of the original Bash behavior. Treat the embedded Bash as
source evidence, not as the preferred execution path. When applying this module, first audit the
current system state, then apply only the missing state described by package, file, service, and
verification sections.

## Extracted Mutating Commands

### snapper

- `if ! command -v snapper &>/dev/null; then`
- `if snapper -c root get-config &>/dev/null; then`
- `if snapper -c root list --columns description | grep -Fqx "$MARKER"; then`
- `snapper -c root create --description "$MARKER"`
- `if snapper -c home get-config &>/dev/null; then`
- `if snapper -c home list --columns description | grep -Fqx "$MARKER"; then`
- `snapper -c home create --description "$MARKER"`

### file_mutations

- `rm -f "$HYPRLAND_AUTOSTART"`
- `rm -f "$NIRI_AUTOSTART"`


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
# 03c-snapshot-before-desktop.sh
# Creates a system snapshot before installing major Desktop Environments.
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 1. 引用工具库
if [ -f "$SCRIPT_DIR/00-utils.sh" ]; then
    source "$SCRIPT_DIR/00-utils.sh"
else
    echo "Error: 00-utils.sh not found."
    exit 1
fi

# 2. 权限检查
check_root

section "Phase 3c" "System Snapshot"

# ==============================================================================

create_checkpoint() {
    local MARKER="Before Desktop Environments"
    
    # 0. 检查 snapper 是否安装
    if ! command -v snapper &>/dev/null; then
        warn "Snapper tool not found. Skipping snapshot creation."
        return
    fi

    # 1. Root 分区快照
    # 检查 root 配置是否存在
    if snapper -c root get-config &>/dev/null; then
        # 检查是否已存在同名快照 (避免重复创建)
        if snapper -c root list --columns description | grep -Fqx "$MARKER"; then
            log "Snapshot '$MARKER' already exists on [root]."
        else
            log "Creating safety checkpoint on [root]..."
            # 使用 --type single 表示这是一个独立的存档点
            snapper -c root create --description "$MARKER"
            success "Root snapshot created."
        fi
    else
        warn "Snapper 'root' config not configured. Skipping root snapshot."
    fi

    # 2. Home 分区快照 (如果存在 home 配置)
    if snapper -c home get-config &>/dev/null; then
        if snapper -c home list --columns description | grep -Fqx "$MARKER"; then
            log "Snapshot '$MARKER' already exists on [home]."
        else
            log "Creating safety checkpoint on [home]..."
            snapper -c home create --description "$MARKER"
            success "Home snapshot created."
        fi
    fi
}

# ==============================================================================
# 执行
# ==============================================================================
# --- Identify User & DM Check ---
log "Identifying target user..."
detect_target_user

if [[ -z "$TARGET_USER" || ! -d "$HOME_DIR" ]]; then
    error "Target user invalid or home directory does not exist."
    exit 1
fi

log "Preparing to create restore point..."
create_checkpoint

HYRPLAND_AUTOSTART="$HOME_DIR/.config/systemd/user/hyprland-autostart.service"
NIRI_AUTOSTART="$HOME_DIR/.config/systemd/user/niri-autostart.service"
if [ -f "$HYPRLAND_AUTOSTART" ]; then
    log "Removing existing Hyprland autostart service..."
    rm -f "$HYPRLAND_AUTOSTART"
fi
if [ -f "$NIRI_AUTOSTART" ]; then
    log "Removing existing Niri autostart service..."
    rm -f "$NIRI_AUTOSTART"
fi
log "Module 03c completed."
~~~~
