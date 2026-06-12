---
source: dotfiles/.config/xdg-desktop-portal/niri-portals.conf
target: .config/xdg-desktop-portal/niri-portals.conf
type: text
language: conf
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "b986ffe409451184b704cf3157445fef56e2890105f80ecb0ff2643c79adc055"
size_bytes: 302
git_status: clean
---

# .config/xdg-desktop-portal/niri-portals.conf

Source: `dotfiles/.config/xdg-desktop-portal/niri-portals.conf`

Install target: `~/.config/xdg-desktop-portal/niri-portals.conf`

~~~~conf
[preferred]
default=gnome;gtk;
org.freedesktop.impl.portal.Access=gtk;
org.freedesktop.impl.portal.Notification=gtk;
org.freedesktop.impl.portal.FileChooser=gtk;
org.freedesktop.impl.portal.Secret=gnome-keyring;
org.freedesktop.impl.portal.ScreenCast=gnome
org.freedesktop.impl.portal.Screenshot=gnome

~~~~
