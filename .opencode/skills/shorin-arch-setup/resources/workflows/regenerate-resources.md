# Workflow: Regenerate Skill Resources

The generated resource layer can be refreshed from the source repositories.

```sh
python tools/generate_resources.py
```

Source repositories:

- configured in `.opencode/skills/shorin-arch-setup/config/sources.json`
- override with `--setup-repo` and `--niri-repo`
- override with `SHORIN_ARCH_SETUP_SOURCE` and `SHORIN_NIRI_SOURCE`

Regeneration captures the current working tree content, including uncommitted changes.

After regeneration, review:

- `resources/modules/`
- `resources/profiles/shorin-niri/dotfiles/dotfiles-index.md`
- `resources/profiles/shorin-niri/assets/assets-index.md`
- `resources/source-capsules/shorin-arch-setup/source-index.md`
- `resources/assets/shorin-arch-setup/assets-index.md`
