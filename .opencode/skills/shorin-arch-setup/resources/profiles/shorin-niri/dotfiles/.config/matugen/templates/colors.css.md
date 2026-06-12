---
source: dotfiles/.config/matugen/templates/colors.css
target: .config/matugen/templates/colors.css
type: text
language: css
mode: "0755"
executable: true
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "3b171e167301b7b7d743cbe04fc00dfce847488741ca89b6ad221e33121d0afe"
size_bytes: 139
git_status: clean
---

# .config/matugen/templates/colors.css

Source: `dotfiles/.config/matugen/templates/colors.css`

Install target: `~/.config/matugen/templates/colors.css`

~~~~css
/*
* Css Colors
* Generated with Matugen
*/
<* for name, value in colors *>
    @define-color {{name}} {{value.default.hex}};
<* endfor *>

~~~~
