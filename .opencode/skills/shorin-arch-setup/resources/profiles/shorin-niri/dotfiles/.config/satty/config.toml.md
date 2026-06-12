---
source: dotfiles/.config/satty/config.toml
target: .config/satty/config.toml
type: text
language: toml
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "a1237285f53a546a5a2efda6a15c01f2e6f8277cfa5cc8fe82e93105fb80c035"
size_bytes: 306
git_status: clean
---

# .config/satty/config.toml

Source: `dotfiles/.config/satty/config.toml`

Install target: `~/.config/satty/config.toml`

~~~~toml
[general]
copy-command = "wl-copy"
focus-toggles-toolbars= true
initial-tool = "brush"
zoom-factor=1.1
actions-on-right-click = ["save-to-clipboard"]
[font]
family = "Noto Sans"
style = "Regular"
fallback = [
    "Noto Sans CJK SC",
    "Noto Sans CJK JP",
    "Noto Sans CJK TC",
    "Noto Sans CJK KR"
]

~~~~
