# Workflow: Update Shorin Niri

Update mode is conservative. It should preserve user-edited state.

## Steps

1. Read `profiles/shorin-niri/protected-paths.md`.
2. Merge user-defined protected paths from `~/.config/shorin-niri/protected.list` if it exists.
3. Audit packages from `profiles/shorin-niri/packages.md` and install missing packages only after confirmation.
4. For every dotfile capsule, skip targets whose policy is `protect` or `generate`.
5. Before replacing any target, copy the existing file into `~/.cache/shorin-niri-backup/<timestamp>/`.
6. Deploy replaceable capsules.
7. Do not overwrite Matugen-generated outputs; regenerate them with Matugen when appropriate.
8. Run verification.

## Override Rule

Only overwrite protected paths when the user explicitly says to do so for a specific path or group.
