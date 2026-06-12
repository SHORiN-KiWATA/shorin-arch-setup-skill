---
name: shorin-arch-setup
description: Use when working on Shorin Arch Setup, shorin-niri, Arch initialization, Btrfs/snapper, GRUB, desktop profiles, package manifests, or Markdownized dotfiles. Triggers on shorin-arch-setup, shorin-niri, shorinniri, Niri, Arch setup, Btrfs, snapper, GRUB, dotfiles.
---

# Shorin Arch Setup

This skill describes a Markdown-first, LLM-operated version of Shorin Arch Setup.

The intended final behavior is equivalent to the existing Bash installer in
`/home/shorin/Documents/github/shorin-arch-setup`, but this skill uses Markdown resources as the
declarative source of truth. The first fully modeled desktop profile is `shorin-niri`.

## Hard Rules

- Do not modify `/home/shorin/Documents/github/shorin-arch-setup` unless the user explicitly asks.
- Do not modify `/home/shorin/Documents/github/shorin-niri` unless the user explicitly asks.
- Treat the Markdown resources in this skill as the editable declarative layer.
- For high-risk actions, audit first and ask before executing: bootloader edits, Btrfs rollback,
  sudoers changes, driver installation, NetworkManager backend changes, user deletion, package
  removals, and service changes that can affect login/networking.
- Prefer idempotent repair: check current state, apply only missing or divergent pieces, verify.
- Preserve user state by backing up target files before replacement.
- Respect protected paths during updates unless the user explicitly requests an override.

## Resource Index

- `resources/index.md`: top-level resource map and workflow model.
- `resources/modules/`: Markdownized installer modules from the Bash implementation.
- `resources/profiles/shorin-niri/profile.md`: Shorin Niri profile intent and behavior.
- `resources/profiles/shorin-niri/packages.md`: package groups and install sources.
- `resources/profiles/shorin-niri/protected-paths.md`: update protection rules.
- `resources/profiles/shorin-niri/verification.md`: post-install and repair checks.
- `resources/profiles/shorin-niri/dotfiles/`: text dotfiles stored as Markdown capsules.
- `resources/profiles/shorin-niri/assets/`: binary/media/icon/theme assets.
- `config/sources.json`: source repository defaults used by the generator.
- `tools/generate_resources.py`: resource regeneration helper kept inside the skill tree.

## Operating Model

When the user asks to install, update, repair, or audit Shorin Arch Setup:

1. Identify the requested scope: base system, optional module, desktop profile, application list,
   dotfiles, or verification only.
2. Read the relevant module/profile Markdown resources before proposing commands.
3. Build an audit checklist from `packages`, `files`, `services`, `conditions`, and `verification`.
4. Run read-only checks first.
5. For safe missing items, apply idempotent fixes.
6. For high-risk items, summarize what will change and ask for confirmation.
7. Verify after every phase.

## First Profile: shorin-niri

The `shorin-niri` profile is based on `/home/shorin/Documents/github/shorin-niri` and the legacy
installer module `/home/shorin/Documents/github/shorin-arch-setup/scripts/04-niri-setup.sh`.

The canonical runtime behavior is:

- install `shorin-niri-git` and required desktop packages
- run `shorinniri init` semantics
- deploy dotfiles from Markdown capsules
- deploy wallpapers/assets from the assets manifest
- configure locales, user environment, Flatpak permissions, Firefox policies, Matugen, Fcitx5,
  Kitty, Waybar, Niri, and related user tools
- verify packages, dotfiles, generated files, and session commands

## Dotfile Capsule Format

Each text dotfile is represented as a Markdown file with frontmatter and a fenced payload:

```md
---
source: dotfiles/.config/niri/config.kdl
target: .config/niri/config.kdl
type: text
language: kdl
mode: "0755"
sha256: "..."
protected: false
generated: false
update_policy: replace
---

~~~~kdl
...
~~~~
```

Binary files are not embedded in Markdown. They are copied into `assets/` and listed in the asset
manifest.

## Risk Levels

- `low`: documentation or user-only file checks.
- `medium`: user dotfiles, package checks, non-critical services.
- `high`: system packages, login managers, sudoers, user account changes, GRUB regeneration.
- `critical`: Btrfs rollback, bootloader structure changes, external upstream installer scripts,
  automated driver changes.

## Verification Priority

Always verify in this order:

1. package manager and AUR helper availability
2. target user and home directory
3. Btrfs/snapper checkpoints if system mutations are planned
4. packages and services
5. dotfiles and assets
6. generated Matugen/Fcitx/Niri files
7. login/session startup viability
