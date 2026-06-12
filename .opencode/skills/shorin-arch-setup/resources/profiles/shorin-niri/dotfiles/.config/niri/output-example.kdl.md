---
source: dotfiles/.config/niri/output-example.kdl
target: .config/niri/output-example.kdl
type: text
language: kdl
mode: "0644"
executable: false
protected: true
generated: false
update_policy: protect
owner_scope: user
backup: true
sha256: "b00ce3a95e87d7047b06cec0f3e05c0c2b1c0262c8f9f40a81fe7c4f12770b15"
size_bytes: 192
git_status: clean
---

# .config/niri/output-example.kdl

Source: `dotfiles/.config/niri/output-example.kdl`

Install target: `~/.config/niri/output-example.kdl`

~~~~kdl
output "eDP-1"{
//	off
    mode "2560x1440@165"
	scale 1.3
	position x=0 y=0

}
output "DP-2"{
	//主要显示器DP-2
	mode "2560x1440@180"
	scale 1
	position x=0 y=0
    focus-at-startup

}


~~~~
