---
source: grub-themes/Crossgrub/theme.txt
type: source-resource
language: text
mode: "0755"
sha256: "8409aed45d3621862ef33594ae9547457672744101de7cae4540d1cb9f756027"
size_bytes: 1327
---

# grub-themes/Crossgrub/theme.txt

~~~~text
# Global

title-text: ""
desktop-image: "background.png"

# Terminal for Console and Options
terminal-border: "20"
terminal-left: "20%"
terminal-top: "20%+23"
terminal-width: "60%"
terminal-height: "60%"
terminal-box: "term_*.png"
terminal-font: "Monocraft Regular 22"

# SHADOW
+ boot_menu {
	left = 2%-1
	top = 60%-1
	width = 600
	height = 500

	item_font = "PixelHallfeticaJP10P Regular 30"
	item_color = white
	selected_item_color = white
	item_height = 30
	item_icon_space = -20
	item_spacing = 45
	scrollbar = false
}

+ boot_menu {
	left = 2%
	top = 60%
	width = 600
	height = 500

	item_font = "PixelHallfeticaJP10P Regular 30"
	item_color = black
	selected_item_color = black
	item_height = 30
	item_padding = 0
	item_icon_space = -20
	item_spacing = 45
	item_pixmap_style = "item_*.png"
	selected_item_pixmap_style = "selected_item_*.png"
	scrollbar = false
}

# TEXT 
+ label {
	id = "__timeout__"
	
	left = 50%
	top = 100%-50
	height = 24
	width = 50%-6	
	
	text = "Executing selected entry in %d seconds"
	align = "right"
	font = "PixelHallfeticaJP10P Regular 30"
	color = "white"
}

# SHADOW 
+ label {
	id = "__timeout__"

	left = 50%+3
	top = 100%-47
	height = 24
	width = 50%-6

	text = "Executing selected entry in %d seconds"
	align = "right"
	font = "PixelHallfeticaJP10P Regular 30"
	color = "#3f3f3f"
}



~~~~
