---
source: dotfiles/.config/matugen/templates/niri-colors.kdl
target: .config/matugen/templates/niri-colors.kdl
type: text
language: kdl
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "00a92e850d97dfb8e7e3941db4e6ba7500a93e85342d1ba78d2432fae27848af"
size_bytes: 360
git_status: clean
---

# .config/matugen/templates/niri-colors.kdl

Source: `dotfiles/.config/matugen/templates/niri-colors.kdl`

Install target: `~/.config/matugen/templates/niri-colors.kdl`

~~~~kdl
layout{
    focus-ring{
        active-gradient from="{{colors.primary.default.hex}}cc" to="{{colors.tertiary.default.hex}}cc" angle=135
        urgent-color "{{colors.error.default.hex}}"

        }
}
recent-windows {    
    highlight {
        active-color "{{colors.surface_bright.default.hex}}"
        urgent-color "{{colors.error.default.hex}}"
    }
}

~~~~
