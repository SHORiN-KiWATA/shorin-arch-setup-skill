---
source: dotfiles/.config/kitty/kitty.conf
target: .config/kitty/kitty.conf
type: text
language: conf
mode: "0755"
executable: true
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "c354e3bdaf27926ee6aa096011573ef8fda5ca5567ea6ef4503ba4ab22921c0f"
size_bytes: 351
git_status: clean
---

# .config/kitty/kitty.conf

Source: `dotfiles/.config/kitty/kitty.conf`

Install target: `~/.config/kitty/kitty.conf`

~~~~conf
include themes/matugen.conf
window_padding_width 5
hide_window_decorations yes
background_opacity 0.8
font_family JetBrains Maple Mono 
font_size 13.5
remember_window_size no
confirm_os_window_close 0
shell fish
cursor_trail 1 
cursor_shape block
shell_integration no-cursor

# BEGIN_KITTY_THEME
# Matugen
include current-theme.conf
# END_KITTY_THEME

~~~~
