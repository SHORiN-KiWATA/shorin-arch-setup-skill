# Known Issues From Source Review

These issues were observed while converting the Bash implementation into Markdown specs.

## 04l-minimal-labwc

`scripts/04l-minimal-labwc.sh` references `FM_PKGS1`, but that variable is not defined in the file
before use. Treat the module as `needs-review` before enabling it in the Markdown workflow.

## 04m-inir-quickshell

`scripts/04m-inir-quickshell.sh` writes an xdg-desktop-portal startup line to
`$DMS_NIRI_CONFIG_FILE`, but the module appears to define/use `INIR_ENV_CONFIG` elsewhere. Treat
this as `needs-review` before enabling it.

## External Installers

The DMS, End4, Caelestia, iNiR, and Minegrub modules call external scripts or clone external
repositories. In Markdown skill mode, these are critical-risk steps and require explicit user
confirmation plus post-run verification.

## shorin-niri README Link

The source `shorin-niri/README.md` currently contains a malformed nested Markdown link in the docs
section. The Markdown capsule preserves the source content exactly instead of silently fixing it.

## shorin-niri Protected Theme Path

`shorinniri` `UPDATE_IGNORE` contains `.local/themes`, while the repository stores theme files
under `.local/share/themes`. The skill preserves the upstream protected path and records the actual
theme files as capsules/assets. Review this before changing update-protection behavior.
