# Workflow: Install Shorin Niri

This is the first enabled desktop workflow for the Markdown skill.

## Scope

- Base assumptions come from `modules/00-btrfs-init.md`, `modules/01a-base.md`,
  `modules/02-musthave.md`, `modules/03a-user.md`, and
  `modules/03c-snapshot-before-desktop.md`.
- Desktop behavior comes from `modules/04-niri-setup.md` and
  `profiles/shorin-niri/profile.md`.
- Dotfiles come from `profiles/shorin-niri/dotfiles/`.
- Assets come from `profiles/shorin-niri/assets/assets-index.md`.

## Steps

1. Audit system type, target user, package manager, AUR helper, Btrfs/snapper, and display manager.
2. If system mutation is requested, confirm or create a `Before Desktop Environments` checkpoint.
3. Install or verify `xdg-desktop-portal-gnome` and `shorin-niri-git`.
4. Apply `shorinniri init` semantics from `profiles/shorin-niri/profile.md`.
5. Deploy non-protected Markdown dotfile capsules to `$HOME`, backing up collisions first.
6. Deploy binary assets from `profiles/shorin-niri/assets/`.
7. Apply user settings: XDG dirs, xdg terminal list, gsettings, Flatpak overrides, theme links,
   default wallpaper assets, and Rime LLM initialization when available.
8. Configure display manager only after confirming no existing DM conflict.
9. Run `profiles/shorin-niri/verification.md`.

## Confirmation Points

- Installing packages with `pacman`, `yay`, or `paru`.
- Writing to `/etc`, `/usr`, `/boot`, or systemd services.
- Enabling a display manager.
- Overwriting protected dotfiles.
