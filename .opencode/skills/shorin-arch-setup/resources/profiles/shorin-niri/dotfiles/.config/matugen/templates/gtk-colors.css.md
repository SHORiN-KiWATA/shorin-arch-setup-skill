---
source: dotfiles/.config/matugen/templates/gtk-colors.css
target: .config/matugen/templates/gtk-colors.css
type: text
language: css
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "87a5f54407d1897f1894c7bfeb9b4b39c738091a0e471d8d52aef5f555bab0dd"
size_bytes: 1305
git_status: clean
---

# .config/matugen/templates/gtk-colors.css

Source: `dotfiles/.config/matugen/templates/gtk-colors.css`

Install target: `~/.config/matugen/templates/gtk-colors.css`

~~~~css
@define-color accent_color {{colors.primary_fixed_dim.default.hex}};
@define-color accent_fg_color {{colors.on_primary.default.hex}};
@define-color accent_bg_color {{colors.primary_fixed_dim.default.hex}};
@define-color window_bg_color {{colors.surface_container.default.hex}};
@define-color window_fg_color {{colors.on_surface.default.hex}};
@define-color headerbar_bg_color {{colors.surface_container.default.hex}};
@define-color headerbar_fg_color {{colors.on_surface.default.hex}};
@define-color popover_bg_color {{colors.surface_container.default.hex}};
@define-color popover_fg_color {{colors.on_surface.default.hex}};
@define-color view_bg_color {{colors.surface_container_low.default.hex}};
@define-color view_fg_color {{colors.on_surface.default.hex}};
@define-color card_bg_color {{colors.surface_container_low.default.hex}};
@define-color card_fg_color {{colors.on_surface.default.hex}};
@define-color sidebar_bg_color @window_bg_color;
@define-color sidebar_fg_color @window_fg_color;
@define-color sidebar_border_color @window_bg_color;
@define-color sidebar_backdrop_color @window_bg_color;
@define-color dialog_bg_color {{colors.surface_container.default.hex}};
@define-color dialog_fg_color {{colors.on_surface.default.hex}};
@define-color borders {{colors.outline_variant.default.hex}};


~~~~
