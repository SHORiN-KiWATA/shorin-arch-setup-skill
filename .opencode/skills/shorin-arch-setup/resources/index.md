# Resource Index

This directory stores the Markdown declaration layer for `shorin-arch-setup`.

## Layout

| Path | Meaning |
| --- | --- |
| `modules/` | Markdown specs generated from the original Bash modules; start at `modules/modules-index.md`. |
| `profiles/shorin-niri/` | First desktop profile implemented as Markdown resources. |
| `profiles/shorin-niri/dotfiles/` | Text dotfiles converted to Markdown capsules. |
| `profiles/shorin-niri/assets/` | Binary/media/icon assets copied from source repositories. |
| `source-capsules/` | Non-profile text resources from the original setup repo. |
| `assets/` | Shared binary resources from the original setup repo. |
| `source-provenance.md` | Source repository branch, commit, and dirty working-tree status captured during generation. |

## Declaration Contract

Every module should describe:

- intent
- phase
- risk
- preconditions
- package state
- file state
- service state
- commands that mutate system state
- verification
- rollback or recovery path

Every dotfile capsule should describe:

- source path
- target path under `$HOME`
- mode and executable bit
- protection policy
- generated-file status
- checksum
- exact content
