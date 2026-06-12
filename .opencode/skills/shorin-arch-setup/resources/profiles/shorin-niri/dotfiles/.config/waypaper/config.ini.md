---
source: dotfiles/.config/waypaper/config.ini
target: .config/waypaper/config.ini
type: text
language: ini
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "7ac369ccc4830541ef685a42abd54f0167b1ee59cf9b2d5b4476ad2fede76026"
size_bytes: 660
git_status: clean
---

# .config/waypaper/config.ini

Source: `dotfiles/.config/waypaper/config.ini`

Install target: `~/.config/waypaper/config.ini`

~~~~ini
[Settings]
language = en
folder = ~/Pictures/Wallpapers
monitors = All
wallpaper = ~/Pictures/Wallpapers/wall_1769769387.png
show_path_in_tooltip = True
backend = awww
fill = fill
sort = daterev
color = #ffffff
subfolders = False
all_subfolders = False
show_hidden = False
show_gifs_only = False
zen_mode = True
post_command = $HOME/.config/scripts/matugen-update.sh && sleep 0.8 && $HOME/.config/scripts/niri_set_overview_blur_dark_bg.sh
number_of_columns = 3
swww_transition_type = any
swww_transition_step = 63
swww_transition_angle = 0
swww_transition_duration = 3
swww_transition_fps = 60
mpvpaper_sound = False
mpvpaper_options = 
use_xdg_state = False


~~~~
