---
source: dotfiles/.config/matugen/templates/steam.css
target: .config/matugen/templates/steam.css
type: text
language: css
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "85641ffeafad5d9e5e62ee7923718afe50f788715b96985a26e049748ff62c94"
size_bytes: 2400
git_status: clean
---

# .config/matugen/templates/steam.css

Source: `dotfiles/.config/matugen/templates/steam.css`

Install target: `~/.config/matugen/templates/steam.css`

~~~~css
/*
* GTK 4 Colors
* Converted from Matugen template
*/

:root {
    --adw-accent-rgb: {{ colors.primary.default.red }} {{ colors.primary.default.green }} {{ colors.primary.default.blue }};
    --adw-accent-bg-rgb: {{ colors.primary.default.red }} {{ colors.primary.default.green }} {{ colors.primary.default.blue }};
    --adw-accent-fg-rgb: {{ colors.on_primary.default.red }} {{ colors.on_primary.default.green }} {{ colors.on_primary.default.blue }};

    --adw-window-bg-rgb: {{ colors.background.default.red }} {{ colors.background.default.green }} {{ colors.background.default.blue }};
    --adw-window-fg-rgb: {{ colors.on_background.default.red }} {{ colors.on_background.default.green }} {{ colors.on_background.default.blue }};

    --adw-headerbar-bg-rgb: {{ colors.surface_dim.default.red }} {{ colors.surface_dim.default.green }} {{ colors.surface_dim.default.blue }};
    --adw-headerbar-fg-rgb: {{ colors.on_surface.default.red }} {{ colors.on_surface.default.green }} {{ colors.on_surface.default.blue }};

    --adw-popover-bg-rgb: {{ colors.surface_dim.default.red }} {{ colors.surface_dim.default.green }} {{ colors.surface_dim.default.blue }};
    --adw-popover-fg-rgb: {{ colors.on_surface.default.red }} {{ colors.on_surface.default.green }} {{ colors.on_surface.default.blue }};

    --adw-view-bg-rgb: {{ colors.surface.default.red }} {{ colors.surface.default.green }} {{ colors.surface.default.blue }};
    --adw-view-fg-rgb: {{ colors.on_surface.default.red }} {{ colors.on_surface.default.green }} {{ colors.on_surface.default.blue }};

    --adw-card-bg-rgb: {{ colors.surface.default.red }} {{ colors.surface.default.green }} {{ colors.surface.default.blue }};
    --adw-card-fg-rgb: {{ colors.on_surface.default.red }} {{ colors.on_surface.default.green }} {{ colors.on_surface.default.blue }};

    --adw-sidebar-bg-rgb: {{ colors.background.default.red }} {{ colors.background.default.green }} {{ colors.background.default.blue }};
    --adw-sidebar-fg-rgb: {{ colors.on_background.default.red }} {{ colors.on_background.default.green }} {{ colors.on_background.default.blue }};
    --adw-sidebar-border-rgb: {{ colors.background.default.red }} {{ colors.background.default.green }} {{ colors.background.default.blue }};
    --adw-sidebar-backdrop-rgb: {{ colors.background.default.red }} {{ colors.background.default.green }} {{ colors.background.default.blue }};
}

~~~~
