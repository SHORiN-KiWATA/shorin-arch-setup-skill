---
source: dotfiles/.config/matugen/templates/hyprland-colors.conf
target: .config/matugen/templates/hyprland-colors.conf
type: text
language: conf
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "1f9d1def37ffc104e1fa005eccd5a600f109acb5e4e8d04af477e49c3dec6235"
size_bytes: 96
git_status: clean
---

# .config/matugen/templates/hyprland-colors.conf

Source: `dotfiles/.config/matugen/templates/hyprland-colors.conf`

Install target: `~/.config/matugen/templates/hyprland-colors.conf`

~~~~conf
<* for name, value in colors *>
${{name}} = rgba({{value.default.hex_stripped}}ff)
<* endfor *>

~~~~
