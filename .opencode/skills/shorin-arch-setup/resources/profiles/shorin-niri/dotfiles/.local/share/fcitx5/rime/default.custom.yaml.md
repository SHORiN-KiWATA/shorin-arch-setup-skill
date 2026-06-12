---
source: dotfiles/.local/share/fcitx5/rime/default.custom.yaml
target: .local/share/fcitx5/rime/default.custom.yaml
type: text
language: yaml
mode: "0644"
executable: false
protected: true
generated: false
update_policy: protect
owner_scope: user
backup: true
sha256: "a2c3233b90f178c11cc9f7608cf3d698d288c180689ca43366bd7bacd63c6f16"
size_bytes: 223
git_status: clean
---

# .local/share/fcitx5/rime/default.custom.yaml

Source: `dotfiles/.local/share/fcitx5/rime/default.custom.yaml`

Install target: `~/.local/share/fcitx5/rime/default.custom.yaml`

~~~~yaml
patch:
  ascii_composer:
    good_old_caps_lock: true
  schema_list:
    - schema: rime_ice
    - schema: luna_pinyin_simp
    - schema: double_pinyin_flypy
    - schema: wubi86
    - schema: bopomofo
  "menu/page_size": 6

~~~~
