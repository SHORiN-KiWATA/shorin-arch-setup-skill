---
source: dotfiles/.config/matugen/templates/ghostty-colors.conf
target: .config/matugen/templates/ghostty-colors.conf
type: text
language: conf
mode: "0755"
executable: true
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "06b519a1448720a726ca2a92f1098190966fc1bb07cac150a7986c94f322cdcd"
size_bytes: 324
git_status: clean
---

# .config/matugen/templates/ghostty-colors.conf

Source: `dotfiles/.config/matugen/templates/ghostty-colors.conf`

Install target: `~/.config/matugen/templates/ghostty-colors.conf`

~~~~conf
background = {{colors.background.default.hex}}
foreground = {{colors.on_surface.default.hex}}
cursor-color = {{colors.on_surface.default.hex}}
cursor-text = {{colors.on_surface_variant.default.hex}}
selection-background = {{colors.secondary_fixed_dim.default.hex}}
selection-foreground = {{colors.on_secondary.default.hex}}

~~~~
