---
source: grub-themes/bsol/theme.txt
type: source-resource
language: text
mode: "0644"
sha256: "e1f2055822f8e9ccfd756a56ba395db138ac6b48a16d8cae322eba40dc7bc88b"
size_bytes: 813
---

# grub-themes/bsol/theme.txt

~~~~text
# Global options
title-text: ""
desktop-image: "background.png"
desktop-color: "#000000"
terminal-font: "Victor Mono Italic 20"
terminal-box: "terminal_box_*.png"
terminal-left: "0"
terminal-top: "0"
terminal-width: "100%"
terminal-height: "100%"
terminal-border: "0"

# Boot menu
+ boot_menu {
  left = 17%
  top = 53%
  width = 47%
  height = 65%
  item_font =  "Victor Mono Bold Italic 24"
  item_color = "#cccccc"
  selected_item_color = "#ffffff"
  icon_width = 50
  icon_height = 50
  item_icon_space = 20
  item_height = 40
  item_padding = 2
  item_spacing = 10
  selected_item_pixmap_style = "select_*.png"
}


# Countdown
+ label {
  left = 25%
  top = 30%
  align = "left"
  id = "__timeout__"
  text = "Selected OS will start in %d seconds"
  color = "#cccccc"
  font = "Victor Mono Bold Italic 28"
}

~~~~
