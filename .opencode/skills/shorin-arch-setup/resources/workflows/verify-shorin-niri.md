# Workflow: Verify Shorin Niri

This workflow is safe by default because it is read-only unless a missing state is explicitly
requested to be fixed.

## Checks

- AUR helper exists: `yay` or `paru`.
- Key packages from `profiles/shorin-niri/packages.md` are installed.
- Niri config files exist under `~/.config/niri`.
- Waybar, Fuzzel, Kitty, Mako, Matugen, and Fcitx5 configs exist.
- Executable scripts from capsules with `executable: true` or executable modes such as `0755` have executable mode.
- Assets exist where the profile expects them.
- Matugen-generated outputs exist or can be regenerated.
- Optional: `niri validate` succeeds when available.

## Output

Report missing packages, missing files, wrong modes, protected path conflicts, and generated files
that should be regenerated.
