---
source: dotfiles/.config/matugen/templates/fastfetch-config.jsonc
target: .config/matugen/templates/fastfetch-config.jsonc
type: text
language: jsonc
mode: "0644"
executable: false
protected: false
generated: false
update_policy: replace
owner_scope: user
backup: true
sha256: "17a33a8026e420e31e00236c132f4aeb7b1fce10b57a50eed668abf95a41ea84"
size_bytes: 4175
git_status: clean
---

# .config/matugen/templates/fastfetch-config.jsonc

Source: `dotfiles/.config/matugen/templates/fastfetch-config.jsonc`

Install target: `~/.config/matugen/templates/fastfetch-config.jsonc`

~~~~jsonc
{
  "$schema": "https://github.com/fastfetch-cli/fastfetch/raw/master/doc/json_schema.json",
  "logo": {
    //"type": "kitty",
    //"source": "/home/shorin/Pictures/picture.png",
    "width": 25,
    // "height":20,
    "color":{
      "1":"{{colors.primary.default.hex}}",
      "2":"{{colors.primary.default.hex}}"
    },
    "padding": {
      "top": 1, // Top padding
      "left": 2, // Left padding
      "right": 2 // Right padding
    },
  },
  "display": {
    "separator": " ", // Separator between keys and values
    "color": {
      //"keys": "{{colors.secondary.default.hex}}", // Key color module名字的颜色
      "title": "{{colors.on_surface_variant.default.hex}}", // Title color 主机名的颜色
      "output": "{{colors.on_surface_variant.default.hex}}"
    },
  },
  "modules": [
    "break",
    {
      "type": "os", //这是哪个module
      "key": "OS", //module名字的显示
      // "keyColor": "#00ff00",      //module名字颜色
      // "format": "{name} {version}",    //具体内容
      "keyColor": "{{colors.primary.default.hex}}",
   
    },
    {
      "type": "kernel",
      "key": " ├   KER ",
      "keyColor": "{{colors.primary.default.hex}}",

    },
    {
      "type": "packages",
      "key": " ├   PAK ",
      "format": "{all}",
      "keyColor": "{{colors.primary.default.hex}}",
    },
    {
      "type": "command",
      "key": " ├   AGE ",
      "text": "birth_install=$(stat -c %W / 2>/dev/null || stat -f %B /); current=$(date +%s); days_difference=$(( (current - birth_install) / 86400 )); echo $days_difference days",
      "keyColor": "{{colors.primary.default.hex}}",
    },
    {
      "type": "title",
      "key": " └   USR ",
      "keyColor": "{{colors.primary.default.hex}}",
    },
    "break",
    "break",
    {
      "type": "wm",
      "key": "WM",
      "keyColor": "{{colors.tertiary.default.hex}}",
   },
    {
      "type": "de",
      "key": " ├ 󱈹  DES ",
      "keyColor": "{{colors.tertiary.default.hex}}",
     //"outputColor": "{{colors.tertiary_fixed_dim.default.hex}}"
    },
    {
      "type": "shell",
      "key": " ├   SHE ",
      "keyColor": "{{colors.tertiary.default.hex}}",
      //"outputColor": "{{colors.tertiary_fixed_dim.default.hex}}"
    },
    {
      "type": "terminal",
      "key": " ├   TER ",
      "keyColor": "{{colors.tertiary.default.hex}}",
      //"outputColor": "{{colors.tertiary_fixed_dim.default.hex}}"
    },
    {
      "type": "terminalfont",
      "key": " └   TFO ",
      "keyColor": "{{colors.tertiary.default.hex}}",
      //"outputColor": "{{colors.tertiary_fixed_dim.default.hex}}"
    },
    "break",
    "break",
    {
      "type": "host",
      "key": "PC ",
      "keyColor": "{{colors.secondary_fixed.default.hex}}",
      //"outputColor": "{{colors.secondary_fixed_dim.default.hex}}"
    },
    {
      "type": "cpu",
      "key": " ├   CPU ",
      "keyColor": "{{colors.secondary_fixed.default.hex}}",
      //"outputColor": "{{colors.secondary_fixed_dim.default.hex}}"
    },
    {
      "type": "memory",
      "key": " ├   MEM ",
      "keyColor": "{{colors.secondary_fixed.default.hex}}",
      //"outputColor": "{{colors.secondary_fixed_dim.default.hex}}"
    },
    {
      "type": "swap",
      "key": " ├   SWP ",
      "keyColor": "{{colors.secondary_fixed.default.hex}}",
      //"outputColor": "{{colors.secondary_fixed_dim.default.hex}}"
    },
    {
      "type": "gpu",
      "key": " ├ 󰢮  GPU ",
      "format": "{1} {2}",
      "keyColor": "{{colors.secondary_fixed.default.hex}}",
      //"outputColor": "{{colors.secondary_fixed_dim.default.hex}}"
    },
    {
      "type": "display",
      "key": " ├   MON ",
      "format": "{name} {width}x{height}@{refresh-rate} ",
      "keyColor": "{{colors.secondary_fixed.default.hex}}",
      //"outputColor": "{{colors.secondary_fixed_dim.default.hex}}"
    },
    {
      "type": "disk",
      "key": " └ 󰋊  DIS ",
      "keyColor": "{{colors.secondary_fixed.default.hex}}",
      //"outputColor": "{{colors.secondary_fixed_dim.default.hex}}"
    },
    "break",
    "break",
    "colors"
  ]
}

~~~~
