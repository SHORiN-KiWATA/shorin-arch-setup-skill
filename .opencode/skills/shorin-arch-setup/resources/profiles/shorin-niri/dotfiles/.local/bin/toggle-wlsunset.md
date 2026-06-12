---
source: dotfiles/.local/bin/toggle-wlsunset
target: .local/bin/toggle-wlsunset
type: text
language: text
mode: "0755"
executable: true
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "8ac803bcb2bebc43cc2916e3220177043dda634cf1efb0911a2b4e668393fd8b"
size_bytes: 1021
git_status: clean
---

# .local/bin/toggle-wlsunset

Source: `dotfiles/.local/bin/toggle-wlsunset`

Install target: `~/.local/bin/toggle-wlsunset`

~~~~text
#!/bin/bash

# ===============================================================
# 配置区
# ===============================================================
TEMP_LOW="5000"      # 夜间/护眼色温
TEMP_HIGH="6500"     # 日间/标准色温
TRANSITION="1800"    # 过渡时间 (30分钟)

# 经纬度
LAT="36.5"
LONG="128.0"

# ===============================================================
# 逻辑区
# ===============================================================
if pgrep -x "wlsunset" > /dev/null; then
    # 如果正在运行，则关闭
    pkill wlsunset
    notify-send -t 2000 -a "System" "护眼模式" "已关闭"
else
    # 如果未运行，则开启
    # 这里使用的是经纬度模式，如果你想用固定时间模式，
    # 请把下面这行改为: wlsunset -S 07:00 -s 19:00 -t $TEMP_LOW -T $TEMP_HIGH -d $TRANSITION &
    wlsunset -l $LAT -L $LONG -t $TEMP_LOW -T $TEMP_HIGH -d $TRANSITION &
    notify-send -t 2000 -a "System" "护眼模式" "已开启，目标色温 ${TEMP_LOW}K"
fi

~~~~
