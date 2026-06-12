---
source: dotfiles/.config/waybar-niri-Win11Like/scripts/toggle-bluetooth.sh
target: .config/waybar-niri-Win11Like/scripts/toggle-bluetooth.sh
type: text
language: bash
mode: "0755"
executable: true
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "2ab8eeb4976b674c7d3e2857a1d5449c2b49262cc95ffce933f6303fb8747476"
size_bytes: 636
git_status: clean
---

# .config/waybar-niri-Win11Like/scripts/toggle-bluetooth.sh

Source: `dotfiles/.config/waybar-niri-Win11Like/scripts/toggle-bluetooth.sh`

Install target: `~/.config/waybar-niri-Win11Like/scripts/toggle-bluetooth.sh`

~~~~bash
#!/usr/bin/env bash
# 检查蓝牙的 rfkill 状态
# 'rfkill list bluetooth' 会输出蓝牙设备的信息
# 'grep -q "Soft blocked: yes"' 在输出中安静地 (-q) 查找 "Soft blocked: yes" 字符串

if rfkill list bluetooth | grep -q "Soft blocked: yes"; then
    # 如果找到了 "Soft blocked: yes" (说明蓝牙被软屏蔽了)
    # 则执行 unblock 命令来解锁
    rfkill unblock bluetooth
    # (可选) 发送一个通知，提供操作反馈
else
    # 如果没有找到 "Soft blocked: yes" (说明蓝牙是开启的)
    # 则执行 block 命令来屏蔽
    rfkill block bluetooth
    # (可选) 发送通知
fi

~~~~
