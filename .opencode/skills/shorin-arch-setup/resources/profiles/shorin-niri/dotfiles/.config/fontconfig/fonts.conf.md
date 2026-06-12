---
source: dotfiles/.config/fontconfig/fonts.conf
target: .config/fontconfig/fonts.conf
type: text
language: conf
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "e3c520d7c5463ebc29854305c469ab12bb6dfbdce843ed5e9786b9f662cc64bd"
size_bytes: 1271
git_status: clean
---

# .config/fontconfig/fonts.conf

Source: `dotfiles/.config/fontconfig/fonts.conf`

Install target: `~/.config/fontconfig/fonts.conf`

~~~~conf
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd">
<fontconfig>

    <match target="font">
        <edit name="antialias" mode="assign"><bool>true</bool></edit>
        <edit name="hinting" mode="assign"><bool>true</bool></edit>
        <edit name="hintstyle" mode="assign"><const>hintslight</const></edit>
        <edit name="rgba" mode="assign"><const>rgb</const></edit>
        <edit name="lcdfilter" mode="assign"><const>lcddefault</const></edit>
    </match>

    <alias>
        <family>sans-serif</family>
        <prefer>
            <family>Noto Sans</family>
            <family>Noto Sans CJK SC</family>
            <family>Adwaita Sans</family>
            <family>Liberation Sans</family>
        </prefer>
    </alias>

    <alias>
        <family>serif</family>
        <prefer>
            <family>Noto Sans</family>
            <family>Noto Sans CJK SC</family>
            <family>Adwaita Sans</family>
            <family>Liberation Sans</family>
        </prefer>
    </alias>

    <alias>
        <family>monospace</family>
        <prefer>
            <family>JetBrains Mono</family>
            <family>JetBrains Maple Mono</family>
            <family>Adwaita Mono</family>
        </prefer>
    </alias>

</fontconfig>

~~~~
