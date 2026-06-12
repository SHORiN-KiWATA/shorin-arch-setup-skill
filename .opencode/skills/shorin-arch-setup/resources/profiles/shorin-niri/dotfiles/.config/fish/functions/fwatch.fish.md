---
source: dotfiles/.config/fish/functions/fwatch.fish
target: .config/fish/functions/fwatch.fish
type: text
language: fish
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "b22524d7a90f74b1b1bc41b033e44667f980337fbf97b15604cc0fa5eb81bffd"
size_bytes: 87
git_status: clean
---

# .config/fish/functions/fwatch.fish

Source: `dotfiles/.config/fish/functions/fwatch.fish`

Install target: `~/.config/fish/functions/fwatch.fish`

~~~~fish
function fwatch
    while true
    	clear
        f $argv
        sleep 5
    end
end


~~~~
