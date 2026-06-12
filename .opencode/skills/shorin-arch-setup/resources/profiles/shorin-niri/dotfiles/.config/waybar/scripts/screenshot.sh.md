---
source: dotfiles/.config/waybar/scripts/screenshot.sh
target: .config/waybar/scripts/screenshot.sh
type: text
language: bash
mode: "0755"
executable: true
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "bb12bca755e907fcf2a731f2e73330522d43e7f3fdc5f4b053805319cf2994b8"
size_bytes: 239
git_status: clean
---

# .config/waybar/scripts/screenshot.sh

Source: `dotfiles/.config/waybar/scripts/screenshot.sh`

Install target: `~/.config/waybar/scripts/screenshot.sh`

~~~~bash
#!/usr/bin/env bash

COORDS=$(slurp)
if [ -z "$COORDS" ]; then
    exit 0
fi
pw-play /usr/share/sounds/freedesktop/stereo/camera-shutter.oga > /dev/null 2>&1 & 
grim -g "$COORDS" - | wl-copy && notify-send "Screenshot" "copy to clipboard"

~~~~
