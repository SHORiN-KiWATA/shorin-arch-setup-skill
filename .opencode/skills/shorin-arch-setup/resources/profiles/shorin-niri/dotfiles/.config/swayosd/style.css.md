---
source: dotfiles/.config/swayosd/style.css
target: .config/swayosd/style.css
type: text
language: css
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "bc8dd91919f277ba60bef0166f3cae93544dd11c7dc10afb842f7b9d1bfb411f"
size_bytes: 731
git_status: clean
---

# .config/swayosd/style.css

Source: `dotfiles/.config/swayosd/style.css`

Install target: `~/.config/swayosd/style.css`

~~~~css
@import url("colors.css");

/* 1. 主窗口 */
window#osd {
    background: none;
    padding: 1em;
    margin-bottom: 12em 6em 6em 6em; 
}

/* 2. 核心容器 */
#container {
    background-color: alpha(@secondary_container, 0.8);
    border: 0.1em solid alpha(@outline, 0.8); 
    border-radius: 0.5em;
    padding: 0.8em 1.2em; 
}

/* 3. 文字与图标 */
image, label {
    color: @on_surface;
}

label {
    font-size: 1.2em; 
    margin-left: 0.8em;
}

/* 4. 进度条 */
progressbar trough {
    background-color: alpha(@on_surface, 0.25);
    border-radius: 0.5em;
    min-height: 0.3em;
    min-width: 12em; 
}

progressbar progress {
    background-color: @on_surface;
    border-radius: 0.5em;
    min-height: 0.2em;
}

~~~~
