---
source: dotfiles/.config/matugen/templates/swaync-colors.css
target: .config/matugen/templates/swaync-colors.css
type: text
language: css
mode: "0755"
executable: true
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "d0b280772a1becca149dad464dd01b76fa00ad485a52d610355150dbbd68d28f"
size_bytes: 92
git_status: clean
---

# .config/matugen/templates/swaync-colors.css

Source: `dotfiles/.config/matugen/templates/swaync-colors.css`

Install target: `~/.config/matugen/templates/swaync-colors.css`

~~~~css
:root {
  <* for name, value in colors *>
--{{name}}: {{value.default.hex}};
<* endfor *>
}

~~~~
