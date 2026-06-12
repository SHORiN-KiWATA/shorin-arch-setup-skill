---
source: dotfiles/.config/niri/colors.kdl
target: .config/niri/colors.kdl
type: text
language: kdl
mode: "0644"
executable: false
protected: true
generated: true
update_policy: generate
owner_scope: user
backup: true
sha256: "22779e1530deffa5a13a7d91c4d5bc9de8ed5465724632fd13b29f885b511311"
size_bytes: 241
git_status: clean
---

# .config/niri/colors.kdl

Source: `dotfiles/.config/niri/colors.kdl`

Install target: `~/.config/niri/colors.kdl`

~~~~kdl
layout{
    focus-ring{
        active-gradient from="#88d6bbcc" to="#a8cbe2cc" angle=135
        urgent-color "#ffb4ab"

        }
}
recent-windows {    
    highlight {
        active-color "#343b38"
        urgent-color "#ffb4ab"
    }
}

~~~~
