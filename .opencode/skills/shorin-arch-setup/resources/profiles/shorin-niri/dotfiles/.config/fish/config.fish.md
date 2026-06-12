---
source: dotfiles/.config/fish/config.fish
target: .config/fish/config.fish
type: text
language: fish
mode: "0755"
executable: true
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "b4a7c98e238ef687cc08057ae27804dae4f5c3c4abb4bb2884e9a75d3cc52bba"
size_bytes: 1119
git_status: clean
---

# .config/fish/config.fish

Source: `dotfiles/.config/fish/config.fish`

Install target: `~/.config/fish/config.fish`

~~~~fish
if status is-interactive
    # Commands to run in interactive sessions can go here
end
set fish_greeting ""
set -p PATH ~/.local/bin
starship init fish | source
zoxide init fish --cmd cd | source

function y
	set tmp (mktemp -t "yazi-cwd.XXXXXX")
	yazi $argv --cwd-file="$tmp"
	if read -z cwd < "$tmp"; and [ -n "$cwd" ]; and [ "$cwd" != "$PWD" ]
		builtin cd -- "$cwd"
	end
	rm -f -- "$tmp"
end

function cat 
	command bat $argv
end

function ls
	command eza --icons $argv
end
function lt
	command eza --icons --tree $argv
end

# grub
abbr grub 'LANGUAGE=en_US.UTF-8 LANG=en_US.UTF-8 sudo grub-mkconfig -o /boot/grub/grub.cfg'
# 小黄鸭补帧 需要steam安装正版小黄鸭
abbr lsfg 'LSFG_PROCESS="miyu"'
# fa运行fastfetch
abbr fa fastfetch
abbr reboot 'systemctl reboot'
function sl 
	command sl | lolcat	
end
function 滚
	sysup 
end
function raw
	command ~/.config/scripts/random-anime-wallpaper.sh $argv
end

function 安装
	command yay -S $argv
end

function 卸载
	command yay -Rns $argv
end 

# Added by LM Studio CLI (lms)
set -gx PATH $PATH /home/shorin/.lmstudio/bin
# End of LM Studio CLI section


~~~~
