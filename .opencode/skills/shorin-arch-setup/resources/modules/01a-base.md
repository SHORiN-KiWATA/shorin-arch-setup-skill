---
id: 01a-base
source: /home/shorin/Documents/github/shorin-arch-setup/scripts/01a-base.sh
source_relative: scripts/01a-base.sh
phase: base
risk: high
requires_root: true
language: bash
mode: "0644"
sha256: "846ef90c8f09f292ac9d1446e342fdf47b81597b3e17372d2f878e23d5f686b6"
generated_from: bash-source
---

# 01a-base

## Intent

Configure editor, multilib, fonts, archlinuxcn, console font, and AUR helpers.

## Declarative Reading Notes

This module is a Markdown declaration of the original Bash behavior. Treat the embedded Bash as
source evidence, not as the preferred execution path. When applying this module, first audit the
current system state, then apply only the missing state described by package, file, service, and
verification sections.

## Extracted Mutating Commands

### pacman

- `exe pacman -Syu --noconfirm gvim`
- `exe pacman -Syu`
- `exe pacman -S --noconfirm --needed ttf-liberation noto-fonts noto-fonts-cjk noto-fonts-emoji ttf-jetbrains-mono-nerd otf-font-awesome`
- `exe pacman -S --noconfirm --needed terminus-font`
- `exe pacman -Syu --noconfirm archlinuxcn-keyring`
- `exe pacman -S --noconfirm --needed base-devel yay paru`

### systemctl

- `exe systemctl restart systemd-vconsole-setup`

### file_mutations

- `exe sed -i "s/^EDITOR=.*/EDITOR=${TARGET_EDITOR}/" /etc/environment`
- `exe sed -i "/\[multilib\]/,/Include/"'s/^#//' /etc/pacman.conf`
- `exe sed -i 's/^FONT=.*/FONT=ter-v28n/' /etc/vconsole.conf`
- `cat <<EOT >> /etc/pacman.conf`
- `cat <<EOT >> /etc/pacman.conf`


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
# 01-base.sh - Base System Configuration
# ==============================================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/00-utils.sh"

check_root

log "Starting Phase 1: Base System Configuration..."

# ------------------------------------------------------------------------------
# 1. Set Global Default Editor
# ------------------------------------------------------------------------------
section "Step 1/6" "Global Default Editor"

TARGET_EDITOR="vim"

if command -v nvim &> /dev/null; then
    TARGET_EDITOR="nvim"
    log "Neovim detected."
    elif command -v nano &> /dev/null; then
    TARGET_EDITOR="nano"
    log "Nano detected."
else
    log "Neovim or Nano not found. Installing Vim..."
    if ! command -v vim &> /dev/null; then
        exe pacman -Syu --noconfirm gvim
    fi
fi

log "Setting EDITOR=$TARGET_EDITOR in /etc/environment..."

if grep -q "^EDITOR=" /etc/environment; then
    exe sed -i "s/^EDITOR=.*/EDITOR=${TARGET_EDITOR}/" /etc/environment
else
    # exe handles simple commands, for redirection we wrap in bash -c or just run it
    # For simplicity in logging, we just run it and log success
    echo "EDITOR=${TARGET_EDITOR}" >> /etc/environment
fi
success "Global EDITOR set to: ${TARGET_EDITOR}"

# ------------------------------------------------------------------------------
# 2. Enable 32-bit (multilib) Repository
# ------------------------------------------------------------------------------
section "Step 2/6" "Multilib Repository"

if grep -q "^\[multilib\]" /etc/pacman.conf; then
    success "[multilib] is already enabled."
else
    log "Uncommenting [multilib]..."
    # Uncomment [multilib] and the following Include line
    exe sed -i "/\[multilib\]/,/Include/"'s/^#//' /etc/pacman.conf
    
    log "Refreshing database..."
    exe pacman -Syu
    success "[multilib] enabled."
fi

# ------------------------------------------------------------------------------
# 3. Install Base Fonts
# ------------------------------------------------------------------------------
section "Step 3/6" "Base Fonts"

log "Installing adobe-source-han-serif-cn-fonts adobe-source-han-sans-cn-fonts , ttf-liberation, emoji..."
exe pacman -S --noconfirm --needed ttf-liberation noto-fonts noto-fonts-cjk noto-fonts-emoji ttf-jetbrains-mono-nerd otf-font-awesome
log "Base fonts installed."

log "Installing terminus-font..."
# 安装 terminus-font 包
exe pacman -S --noconfirm --needed terminus-font

log "Setting font for current session..."
exe setfont ter-v28n

log "Configuring permanent vconsole font..."
if [ -f /etc/vconsole.conf ] && grep -q "^FONT=" /etc/vconsole.conf; then
    exe sed -i 's/^FONT=.*/FONT=ter-v28n/' /etc/vconsole.conf
else
    echo "FONT=ter-v28n" >> /etc/vconsole.conf
fi

log "Restarting systemd-vconsole-setup..."
exe systemctl restart systemd-vconsole-setup

success "TTY font configured (ter-v28n)."
# ------------------------------------------------------------------------------
# 4. Configure archlinuxcn Repository
# ------------------------------------------------------------------------------
section "Step 4/6" "ArchLinuxCN Repository"

if grep -q "\[archlinuxcn\]" /etc/pacman.conf; then
    success "archlinuxcn repository already exists."
else
    log "Adding archlinuxcn mirrors to pacman.conf..."
    
    # Timezone check: KISS approach, works reliably inside arch-chroot and host system
    LOCAL_TZ=""
    if [ -L /etc/localtime ]; then
        LOCAL_TZ=$(readlink -f /etc/localtime)
    fi
    
    echo "" >> /etc/pacman.conf
    echo "[archlinuxcn]" >> /etc/pacman.conf
    
    if [[ "$LOCAL_TZ" == *"Asia/Shanghai"* ]]; then
        log "Timezone is Asia/Shanghai. Applying mainland mirrors..."
        cat <<EOT >> /etc/pacman.conf
Server = https://mirrors.ustc.edu.cn/archlinuxcn/\$arch
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/\$arch
Server = https://mirrors.hit.edu.cn/archlinuxcn/\$arch
Server = https://repo.huaweicloud.com/archlinuxcn/\$arch
EOT
    else
        log "Non-Shanghai timezone detected. Prepending global repo.archlinuxcn.org mirror..."
        cat <<EOT >> /etc/pacman.conf
Server = https://repo.archlinuxcn.org/\$arch
Server = https://mirrors.ustc.edu.cn/archlinuxcn/\$arch
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/\$arch
Server = https://mirrors.hit.edu.cn/archlinuxcn/\$arch
Server = https://repo.huaweicloud.com/archlinuxcn/\$arch
EOT
    fi
    success "Mirrors added based on timezone."
fi

log "Installing archlinuxcn-keyring..."
# Keyring installation often needs -Sy specifically, but -Syu is safe too
exe pacman -Syu --noconfirm archlinuxcn-keyring
success "ArchLinuxCN configured."
# ------------------------------------------------------------------------------
# 5. Install AUR Helpers
# ------------------------------------------------------------------------------
section "Step 5/6" "AUR Helpers"

log "Installing yay and paru..."
exe pacman -S --noconfirm --needed base-devel yay paru
success "Helpers installed."


# ------------------------------------------------------------------------------

log "Module 01 completed."
~~~~
