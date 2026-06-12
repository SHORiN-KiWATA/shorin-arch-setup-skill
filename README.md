# shorin-arch-setup-skill

Markdown-first opencode skill version of Shorin Arch Setup.

This project is intentionally separate from `/home/shorin/Documents/github/shorin-arch-setup`.
It treats the original Bash installer and the `shorin-niri` dotfiles as source material, then
documents them as declarative Markdown resources for an LLM-driven workflow.

Current scope:

- Skill name: `shorin-arch-setup`
- First implemented desktop profile: `shorin-niri`
- Existing Bash modules are preserved as Markdown module specs
- `shorin-niri` text dotfiles are stored as Markdown capsules
- Binary resources are stored under assets and referenced from Markdown manifests

The skill does not make the system declarative by itself. It gives opencode enough structured
knowledge to audit, install, update, verify, and repair the target state with explicit safety
checks.

Generate resources:

```sh
python tools/generate_resources.py
```

The real generator lives inside the skill at
`.opencode/skills/shorin-arch-setup/tools/generate_resources.py`.

Source repositories are configured in `.opencode/skills/shorin-arch-setup/config/sources.json`.
You can override them without editing the generator:

```sh
python tools/generate_resources.py --setup-repo ../shorin-arch-setup --niri-repo ../shorin-niri
```

or:

```sh
SHORIN_ARCH_SETUP_SOURCE=../shorin-arch-setup SHORIN_NIRI_SOURCE=../shorin-niri python tools/generate_resources.py
```

The generator intentionally derives profile state from source files where possible:

- `shorinniri` `TARGET_SOFTWARE` becomes `packages.md`
- `shorinniri` `UPDATE_IGNORE` becomes protected path policy
- `.config/matugen/config.toml` `output_path` entries become generated-file policy
- scripts and resources are discovered from the configured source repositories

Only module risk/intent metadata remains manually curated because that is semantic information, not
reliably inferable from shell syntax.

Load the skill by opening opencode from this repository, or by adding this path to opencode's
`skills.paths` later.
