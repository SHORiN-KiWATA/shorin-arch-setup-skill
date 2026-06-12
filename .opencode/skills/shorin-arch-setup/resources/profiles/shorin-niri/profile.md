# Shorin Niri Profile

Source profile: `/home/shorin/Documents/github/shorin-niri`

This profile models the `shorinniri` desktop preset as Markdown declarations.

## Runtime Commands

- `shorinniri init`: install/sync packages, deploy dotfiles, configure user/system environment.
- `shorinniri update`: install package changes and update non-protected dotfiles.
- `shorinniri remove`: remove managed dotfiles and suggest package cleanup.
- `shorinniri protect PATH`: add a user protected path.
- `shorinniri unprotect PATH`: remove a user protected path.
- `shorinniri protected-list`: list protected paths.

## Managed State

- Text dotfiles are stored as Markdown capsules under `dotfiles/`.
- Binary/media assets are stored under `assets/` and listed in `assets/assets-index.md`.
- Updates must respect `protected-paths.md`.
- Matugen outputs are generated runtime files, not authoritative source files.

## Backup Policy

Before replacing an existing target file, copy it to `~/.cache/shorin-niri-backup/<timestamp>/`.

## Source Snapshot

- Text capsules: 141
- Assets: 100
- Dirty source files captured: 3
