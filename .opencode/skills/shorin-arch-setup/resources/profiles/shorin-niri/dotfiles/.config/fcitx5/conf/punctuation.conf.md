---
source: dotfiles/.config/fcitx5/conf/punctuation.conf
target: .config/fcitx5/conf/punctuation.conf
type: text
language: conf
mode: "0600"
executable: false
protected: true
generated: false
update_policy: protect
owner_scope: user
backup: true
sha256: "912c05ed8ecb9deb97a4717f723bdf256bd4b8e16c744d51f0290d6973c38409"
size_bytes: 213
git_status: clean
---

# .config/fcitx5/conf/punctuation.conf

Source: `dotfiles/.config/fcitx5/conf/punctuation.conf`

Install target: `~/.config/fcitx5/conf/punctuation.conf`

~~~~conf
# 字母或者数字之后输入半角标点
HalfWidthPuncAfterLetterOrNumber=True
# 同时输入成对标点 (例如引号)
TypePairedPunctuationsTogether=False
# Enabled
Enabled=True

[Hotkey]
0=Control+period


~~~~
