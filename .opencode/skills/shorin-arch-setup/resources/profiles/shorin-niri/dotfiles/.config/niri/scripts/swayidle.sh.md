---
source: dotfiles/.config/niri/scripts/swayidle.sh
target: .config/niri/scripts/swayidle.sh
type: text
language: bash
mode: "0755"
executable: true
protected: true
generated: false
update_policy: protect
owner_scope: user
backup: true
sha256: "dfa959adb84546bc539fe3e265fe701c39545d721bdb2d43172b40c7f6f53012"
size_bytes: 286
git_status: clean
---

# .config/niri/scripts/swayidle.sh

Source: `dotfiles/.config/niri/scripts/swayidle.sh`

Install target: `~/.config/niri/scripts/swayidle.sh`

~~~~bash
#!/usr/bin/env bash

# 5分钟锁屏，10分钟熄屏，20分钟休眠
exec swayidle -w \
timeout 600  'hyprlock -c ~/.config/niri/hyprlock.conf &' \
timeout 900  'niri msg action power-off-monitors' \
resume       'niri msg action power-on-monitors' \
timeout 1800 'systemctl suspend'

~~~~
