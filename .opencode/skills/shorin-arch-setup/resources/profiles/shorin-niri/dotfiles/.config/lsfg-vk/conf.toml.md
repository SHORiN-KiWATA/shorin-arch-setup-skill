---
source: dotfiles/.config/lsfg-vk/conf.toml
target: .config/lsfg-vk/conf.toml
type: text
language: toml
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "ccae32888583722d5912061172c6bfa0b8bf58097586bb45967cad3ec987405b"
size_bytes: 169
git_status: clean
---

# .config/lsfg-vk/conf.toml

Source: `dotfiles/.config/lsfg-vk/conf.toml`

Install target: `~/.config/lsfg-vk/conf.toml`

~~~~toml
version = 1

[global]
no_fp16 = false

[[game]]
exe = "miyu"
multiplier = 2
flow_scale = 1.0
performance_mode = true
hdr_mode = false
experimental_present_mode = "fifo"

~~~~
