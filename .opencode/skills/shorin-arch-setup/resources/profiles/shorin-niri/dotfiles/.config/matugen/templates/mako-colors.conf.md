---
source: dotfiles/.config/matugen/templates/mako-colors.conf
target: .config/matugen/templates/mako-colors.conf
type: text
language: conf
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "92fdae201121abcd384466a6596e9584bb26206ebf17c20333098e46024321df"
size_bytes: 144
git_status: clean
---

# .config/matugen/templates/mako-colors.conf

Source: `dotfiles/.config/matugen/templates/mako-colors.conf`

Install target: `~/.config/matugen/templates/mako-colors.conf`

~~~~conf
background-color={{colors.surface_bright.default.hex}}
border-color={{colors.outline.default.hex}}
text-color={{colors.on_surface.default.hex}}

~~~~
