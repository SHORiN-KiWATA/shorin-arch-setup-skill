---
source: dotfiles/.config/fcitx5/config
target: .config/fcitx5/config
type: text
language: text
mode: "0600"
executable: false
protected: true
generated: false
update_policy: protect
owner_scope: user
backup: true
sha256: "d3c79d9d941c84ab95f415a2ffe32c8ccb2dccd29510a1ec0d1c035d77e5f0b4"
size_bytes: 1771
git_status: clean
---

# .config/fcitx5/config

Source: `dotfiles/.config/fcitx5/config`

Install target: `~/.config/fcitx5/config`

~~~~text
[Hotkey]
# 按住切换键的修饰键时进行轮换切换
EnumerateWithTriggerKeys=True
# 向前切换输入法
EnumerateForwardKeys=
# 向后切换输入法
EnumerateBackwardKeys=
# 轮换输入法时跳过第一个输入法
EnumerateSkipFirst=False
# 触发修饰键快捷键的时限 (毫秒)
ModifierOnlyKeyTimeout=250

[Hotkey/TriggerKeys]
0=Super+space
1=Zenkaku_Hankaku
2=Hangul

[Hotkey/ActivateKeys]
0=Hangul_Hanja

[Hotkey/DeactivateKeys]
0=Hangul_Romaja

[Hotkey/AltTriggerKeys]
0=Shift_L

[Hotkey/EnumerateGroupForwardKeys]
0=Super+space

[Hotkey/EnumerateGroupBackwardKeys]
0=Shift+Super+space

[Hotkey/PrevPage]
0=Up

[Hotkey/NextPage]
0=Down

[Hotkey/PrevCandidate]
0=Shift+Tab

[Hotkey/NextCandidate]
0=Tab

[Hotkey/TogglePreedit]
0=Control+Alt+P

[Behavior]
# 默认状态为激活
ActiveByDefault=False
# 重新聚焦时重置状态
resetStateWhenFocusIn=No
# 共享输入状态
ShareInputState=No
# 在程序中显示预编辑文本
PreeditEnabledByDefault=True
# 切换输入法时显示输入法信息
ShowInputMethodInformation=True
# 在焦点更改时显示输入法信息
showInputMethodInformationWhenFocusIn=False
# 显示紧凑的输入法信息
CompactInputMethodInformation=True
# 显示第一个输入法的信息
ShowFirstInputMethodInformation=True
# 默认页大小
DefaultPageSize=5
# 覆盖 XKB 选项
OverrideXkbOption=False
# 自定义 XKB 选项
CustomXkbOption=
# Force Enabled Addons
EnabledAddons=
# Force Disabled Addons
DisabledAddons=
# Preload input method to be used by default
PreloadInputMethod=True
# 允许在密码框中使用输入法
AllowInputMethodForPassword=False
# 输入密码时显示预编辑文本
ShowPreeditForPassword=False
# 保存用户数据的时间间隔（以分钟为单位）
AutoSavePeriod=30


~~~~
