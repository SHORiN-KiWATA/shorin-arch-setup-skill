---
source: dotfiles/.config/niri-sidebar/config.toml
target: .config/niri-sidebar/config.toml
type: text
language: toml
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "27f32cc057e8a7d67aeed4ea1d39dd71585d3ec813693100f34bea56103b9573"
size_bytes: 835
git_status: clean
---

# .config/niri-sidebar/config.toml

Source: `dotfiles/.config/niri-sidebar/config.toml`

Install target: `~/.config/niri-sidebar/config.toml`

~~~~toml
# niri-sidebar configuration

[geometry]
# Width of the sidebar in pixels
width = 400
# Height of the sidebar windows
height = 300 
# Gap between windows in the stack
gap = 8 

[margins]
# Space from the top/bottom of the screen
top = 46
# Space from the right edge of the screen
right = 12

[interaction]
# Width of windows when sidebar is hidden in pixels
peek =0 
# Width of window when sidebar is hidden but window is focused in pixels
# set this equal to peek to disable this feature
# set this equal to sidebar_width + offset_right to make focused windows "unhide"
focus_peek = 0 

# Example window rule
# all fields are optional if not given a default from other configs will be used
[[window_rule]]
app_id = "opencode"  # regex, if not set will match all app_id's
width = 600
height = 1080
auto_add = true  # defaults to false

~~~~
