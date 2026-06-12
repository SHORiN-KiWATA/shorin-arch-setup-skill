# Shorin Niri Verification

## Package Checks

```sh
command -v yay || command -v paru
pacman -Q shorin-niri-git xdg-desktop-portal-gnome cliphist-tui-git kitty firefox fcitx5 fcitx5-rime
```

## Dotfile Checks

```sh
test -f ~/.config/niri/config.kdl
test -f ~/.config/niri/binds.kdl
test -f ~/.config/niri/rule.kdl
test -f ~/.config/matugen/config.toml
test -f ~/.config/waybar/config.jsonc
test -f ~/.config/kitty/kitty.conf
test -f ~/.config/fuzzel/fuzzel.ini
test -x ~/.local/bin/matugen-update
```

## Runtime Command Checks

```sh
command -v niri
command -v waybar
command -v waypaper
command -v fuzzel
command -v mako
command -v fcitx5
command -v cliphist
```

## Optional Niri Validation

```sh
niri validate
```

## Matugen Checks

```sh
command -v matugen
test -f ~/.config/waybar/colors.css
test -f ~/.config/fuzzel/colors.ini
test -f ~/.config/kitty/themes/matugen.conf
test -f ~/.config/niri/colors.kdl
```
