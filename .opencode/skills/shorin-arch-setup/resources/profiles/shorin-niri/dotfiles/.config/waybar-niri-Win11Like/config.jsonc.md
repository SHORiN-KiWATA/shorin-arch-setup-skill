---
source: dotfiles/.config/waybar-niri-Win11Like/config.jsonc
target: .config/waybar-niri-Win11Like/config.jsonc
type: text
language: jsonc
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "efa468042335391f03eafa939a6f1a40e959b6d06aa74460874e1e937a9a2aa6"
size_bytes: 962
git_status: clean
---

# .config/waybar-niri-Win11Like/config.jsonc

Source: `dotfiles/.config/waybar-niri-Win11Like/config.jsonc`

Install target: `~/.config/waybar-niri-Win11Like/config.jsonc`

~~~~jsonc
{
    "include": [
        "~/.config/waybar-niri-Win11Like/modules.jsonc",
        "~/.config/waybar/modules.jsonc"
    ],
    "layer":"top",
    "position": "bottom",
    // "height": 40,
    "fixed-center": true,
    "reload_style_on_change": true,
    "modules-left": [
        "niri/workspaces",
        "custom/cava",
        "mpris",
        "custom/screenshot",
        "custom/wfrec",
	//"custom/wallpapers",
	"custom/clipboard",
	"custom/actions",
        "custom/colorpicker",
        "niri/window",
    ],
    "modules-center": [
        "custom/applauncher"
        //"custom/separator#2",
        //"cffi/niri-taskbar", //需要安装waybar-niri-taskbar-git
    ],
    "modules-right": [
        "custom/updates",
        "tray",
        "group/ddcutil",
        "group/audio",
        "bluetooth",
        "network",
        "idle_inhibitor",
        "battery",
        "power-profiles-daemon",
        "clock",
        "group/powermenu"
    ],
}

~~~~
