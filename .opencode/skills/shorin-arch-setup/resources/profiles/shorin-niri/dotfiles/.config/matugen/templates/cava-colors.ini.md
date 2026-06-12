---
source: dotfiles/.config/matugen/templates/cava-colors.ini
target: .config/matugen/templates/cava-colors.ini
type: text
language: ini
mode: "0755"
executable: true
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "805e9151f514ffe237f99e095b32bdc90ad5c8cec770c0a969421ad8c6b4b7f8"
size_bytes: 686
git_status: clean
---

# .config/matugen/templates/cava-colors.ini

Source: `dotfiles/.config/matugen/templates/cava-colors.ini`

Install target: `~/.config/matugen/templates/cava-colors.ini`

~~~~ini
[color]
background = 'default'
foreground = '{{colors.primary.default.hex}}'

; gradient = 0
gradient = 1
gradient_color_1 = '{{colors.primary_container.default.hex}}'
gradient_color_2 = '{{colors.primary.default.hex}}'
gradient_color_3 = '{{colors.on_primary_container.default.hex}}'

horizontal_gradient = 0
; horizontal_gradient = 1
horizontal_gradient_color_1 = '{{colors.primary_container.default.hex}}'
horizontal_gradient_color_2 = '{{colors.primary.default.hex}}'
horizontal_gradient_color_3 = '{{colors.on_primary_container.default.hex}}'
horizontal_gradient_color_4 = '{{colors.primary.default.hex}}'
horizontal_gradient_color_5 = '{{colors.primary_container.default.hex}}'



~~~~
