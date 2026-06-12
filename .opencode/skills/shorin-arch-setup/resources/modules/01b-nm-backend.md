---
id: 01b-nm-backend
source: /home/shorin/Documents/github/shorin-arch-setup/scripts/01b-nm-backend.sh
source_relative: scripts/01b-nm-backend.sh
phase: optional-network
risk: high
requires_root: true
language: bash
mode: "0644"
sha256: "2ff32e7c7e21cc5ce485308a364c561494207b10911b9cc9cdf8e2567a9750d2"
generated_from: bash-source
---

# 01b-nm-backend

## Intent

Switch NetworkManager Wi-Fi backend to iwd when NetworkManager is present.

## Declarative Reading Notes

This module is a Markdown declaration of the original Bash behavior. Treat the embedded Bash as
source evidence, not as the preferred execution path. When applying this module, first audit the
current system state, then apply only the missing state described by package, file, service, and
verification sections.

## Extracted Mutating Commands

### pacman

- `exe pacman -S --noconfirm --needed iwd impala`

### systemctl

- `exe systemctl enable iwd`

### file_mutations

- `mkdir -p /etc/NetworkManager/conf.d`
- `rm -rfv /etc/NetworkManager/system-connections/*`


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
# 01b-nm-backend.sh - Network Backend Configuration
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/00-utils.sh"

check_root

section "Optional" "Network Backend (iwd)"

# Check if NetworkManager is installed before attempting configuration
if pacman -Qi networkmanager &> /dev/null; then
    log "NetworkManager detected. Proceeding with iwd backend configuration..."
    
    log "Configuring NetworkManager to use iwd backend..."
    exe pacman -S --noconfirm --needed iwd impala
    exe systemctl enable iwd
    # Ensure directory exists
    if [ ! -d /etc/NetworkManager/conf.d ]; then
        mkdir -p /etc/NetworkManager/conf.d
    fi
    if [ -f /etc/NetworkManager/conf.d/wifi_backend.conf ];then
        rm /etc/NetworkManager/conf.d/wifi_backend.conf
    fi
    if [ ! -f /etc/NetworkManager/conf.d/iwd.conf  ];then
        echo -e "[device]\nwifi.backend=iwd" >> /etc/NetworkManager/conf.d/iwd.conf
        rm -rfv /etc/NetworkManager/system-connections/*
    fi
    log "Notice: NetworkManager restart deferred. Changes will apply after reboot."
    success "Network backend configured (iwd)."
else
    log "NetworkManager not found. Skipping iwd configuration."
fi

~~~~
