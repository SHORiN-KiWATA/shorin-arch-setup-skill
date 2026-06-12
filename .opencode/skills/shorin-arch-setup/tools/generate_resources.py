#!/usr/bin/env python3
"""Generate Markdown resources for the shorin-arch-setup opencode skill."""

from __future__ import annotations

import hashlib
import argparse
import json
import os
import re
import shutil
import stat
import subprocess
from dataclasses import dataclass
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path(__file__).resolve().parents[4]
RESOURCES = SKILL_ROOT / "resources"

CONFIG_FILE = SKILL_ROOT / "config" / "sources.json"

SETUP_REPO = (PROJECT_ROOT / "../shorin-arch-setup").resolve()
NIRI_REPO = (PROJECT_ROOT / "../shorin-niri").resolve()

FENCE = "~~~~"


MODULE_META = {
    "install": ("bootstrap", "critical", "Main installer orchestrator: desktop selection, optional modules, mirrors, module execution, cleanup, reboot."),
    "strap": ("bootstrap", "high", "Bootstrap from GitHub tarball and run installer."),
    "strap-proxy": ("bootstrap", "high", "Bootstrap a PR build by cloning and merging a pull request before running installer."),
    "undochange": ("rollback", "critical", "Rollback to the 'Before Shorin Setup' Btrfs snapshot."),
    "de-undochange": ("rollback", "critical", "Rollback to the 'Before Desktop Environments' Btrfs snapshot."),
    "00-utils": ("shared", "medium", "Shared logging, user detection, command execution, display-manager, dotfile, and Flatpak helper functions."),
    "00-btrfs-init": ("base", "critical", "Initialize snapper safety net, Btrfs snapshots, GRUB decoupling, and rollback commands."),
    "01a-base": ("base", "high", "Configure editor, multilib, fonts, archlinuxcn, console font, and AUR helpers."),
    "01b-nm-backend": ("optional-network", "high", "Switch NetworkManager Wi-Fi backend to iwd when NetworkManager is present."),
    "02-musthave": ("base", "high", "Install essential firmware, audio, locale, input method, Bluetooth, power, fastfetch, and Flatpak support."),
    "02a-dualboot-fix": ("optional-boot", "high", "Enable os-prober integration for Windows dual boot when Windows is detected."),
    "03a-user": ("user", "high", "Create or configure target user, sudoers, XDG directories, and user PATH."),
    "03b-gpu-driver": ("optional-hardware", "high", "Install chwd and run automatic hardware driver detection."),
    "03c-snapshot-before-desktop": ("checkpoint", "medium", "Create the pre-desktop snapper checkpoint and remove stale compositor autostarts."),
    "04-niri-setup": ("desktop", "high", "Install Shorin Niri meta package, run shorinniri init, copy wallpapers, and configure display manager."),
    "04b-kdeplasma-setup": ("desktop", "high", "Install KDE Plasma, optional KDE app list, KDE dotfiles, and Plasma login manager."),
    "04c-dms-quickshell": ("desktop", "critical", "Run external DankMaterialShell installer and add Niri/Fcitx/file-manager integration."),
    "04d-gnome": ("desktop", "high", "Install and configure GNOME, extensions, gsettings, dotfiles, Firefox policy, and GDM."),
    "04e-illogical-impulse-end4-quickshell": ("desktop", "critical", "Run external Illogical Impulse End4 installer and configure display manager."),
    "04f-ambxst-quickshell": ("desktop-legacy", "high", "Legacy/experimental Noctalia Niri autologin module not wired in the main installer."),
    "04g-caelestia-quickshell": ("desktop", "critical", "Clone Caelestia dots, run its installer, add file-manager deps, and configure display manager."),
    "04h-shorindms-quickshell": ("desktop", "high", "Install Shorin DMS Niri meta package and run shorindms init."),
    "04i-shorin-hyprniri-quickshell": ("desktop", "high", "Install Hyprland/Niri DMS hybrid environment, clone dotfiles, apply policies, and configure display manager."),
    "04j-minimal-niri": ("desktop", "high", "Install minimal Niri from local dotfiles and package groups."),
    "04k-shorin-noctalia-quickshell": ("desktop", "high", "Install Shorin Noctalia Niri profile from local dotfiles."),
    "04l-minimal-labwc": ("desktop", "high", "Install minimal Labwc profile from local dotfiles."),
    "04m-inir-quickshell": ("desktop", "critical", "Clone and run external iNiR installer, then patch Niri/Fcitx/file-manager integration."),
    "05-verify-desktop": ("verify", "medium", "Verify package shipment list and key desktop config paths."),
    "07-grub-theme": ("optional-boot", "high", "Configure GRUB kernel parameters, themes, power entries, and regenerate GRUB config."),
    "99-apps": ("optional-apps", "high", "Install common applications from repo/AUR/Flatpak lists and apply app-specific tweaks."),
}

PROTECTED_PATHS: set[str] = set()
GENERATED_PATHS: set[str] = set()

BINARY_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ttf", ".ttc", ".otf", ".pf2", ".woff", ".woff2",
}

LANG_BY_SUFFIX = {
    ".sh": "bash",
    ".bash": "bash",
    ".fish": "fish",
    ".py": "python",
    ".kdl": "kdl",
    ".toml": "toml",
    ".json": "json",
    ".jsonc": "jsonc",
    ".yaml": "yaml",
    ".yml": "yaml",
    ".conf": "conf",
    ".ini": "ini",
    ".css": "css",
    ".xml": "xml",
    ".lua": "lua",
    ".md": "markdown",
    ".txt": "text",
    ".desktop": "ini",
    ".service": "ini",
    ".theme": "ini",
    ".svg": "svg",
}

TEXT_SUFFIXES = set(LANG_BY_SUFFIX) - {".svg"}


@dataclass
class Capsule:
    source: Path
    source_relative: str
    target_relative: str
    capsule_path: Path
    mode: str
    sha256: str
    size: int
    language: str
    protected: bool
    generated: bool
    executable: bool
    update_policy: str
    status: str


def clean_generated() -> None:
    for path in [
        RESOURCES / "modules",
        RESOURCES / "profiles" / "shorin-niri" / "dotfiles",
        RESOURCES / "profiles" / "shorin-niri" / "assets",
        RESOURCES / "source-capsules",
        RESOURCES / "assets",
    ]:
        if path.exists():
            shutil.rmtree(path)
        path.mkdir(parents=True, exist_ok=True)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def is_binary(path: Path) -> bool:
    if path.suffix.lower() in BINARY_SUFFIXES:
        return True
    data = path.read_bytes()[:8192]
    if b"\0" in data:
        return True
    if path.suffix.lower() in TEXT_SUFFIXES:
        return False
    try:
        data.decode("utf-8")
    except UnicodeDecodeError:
        return True
    return False


def language_for(path: Path) -> str:
    return LANG_BY_SUFFIX.get(path.suffix.lower(), "text")


def mode_string(path: Path) -> str:
    return f"{stat.S_IMODE(path.stat().st_mode):04o}"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def yaml_bool(value: bool) -> str:
    return "true" if value else "false"


def resolve_config_path(value: str) -> Path:
    expanded = os.path.expandvars(os.path.expanduser(value))
    path = Path(expanded)
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return path.resolve()


def load_source_config() -> tuple[Path, Path]:
    setup = os.environ.get("SHORIN_ARCH_SETUP_SOURCE")
    niri = os.environ.get("SHORIN_NIRI_SOURCE")
    if CONFIG_FILE.exists():
        data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        setup = setup or data.get("shorin_arch_setup")
        niri = niri or data.get("shorin_niri")
    return (
        resolve_config_path(setup or "../shorin-arch-setup"),
        resolve_config_path(niri or "../shorin-niri"),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate shorin-arch-setup skill resources.")
    parser.add_argument("--setup-repo", type=Path, help="Path to the shorin-arch-setup source repository.")
    parser.add_argument("--niri-repo", type=Path, help="Path to the shorin-niri source repository.")
    return parser.parse_args()


def git_status_map(repo: Path) -> dict[str, str]:
    try:
        out = subprocess.check_output(["git", "status", "--porcelain"], cwd=repo, text=True)
    except Exception:
        return {}
    result: dict[str, str] = {}
    for line in out.splitlines():
        if len(line) < 4:
            continue
        result[line[3:]] = line[:2].strip() or "clean"
    return result


def git_value(repo: Path, *args: str) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()
    except Exception:
        return "unknown"


def normalize_home_path(value: str) -> str:
    value = value.strip().strip('"').strip("'")
    prefixes = ("~/", "$HOME/", "${HOME}/")
    for prefix in prefixes:
        if value.startswith(prefix):
            return value[len(prefix):]
    return value.lstrip("/") if value.startswith("/home/") else value


def parse_matugen_outputs(config_path: Path) -> set[str]:
    if not config_path.exists():
        return set()
    outputs: set[str] = set()
    for raw in config_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        match = re.search(r"^output_path\s*=\s*['\"]([^'\"]+)['\"]", line)
        if match:
            outputs.add(normalize_home_path(match.group(1)))
    return outputs


def extract_commands(text: str) -> dict[str, list[str]]:
    commands: dict[str, list[str]] = {
        "pacman": [],
        "aur_helper": [],
        "flatpak": [],
        "systemctl": [],
        "snapper": [],
        "grub": [],
        "external": [],
        "file_mutations": [],
    }
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if re.search(r"\bpacman\s+-S", line):
            commands["pacman"].append(line)
        if re.search(r"\b(yay|paru)\s+-S", line) or (
            re.search(r"\$\{?AUR_HELPER\}?|\"\$AUR_HELPER\"", line) and re.search(r"\s-S(i|y|yu)?\b|\s-S\s", line)
        ):
            commands["aur_helper"].append(line)
        if re.search(r"\bflatpak\b", line):
            commands["flatpak"].append(line)
        if re.search(r"\bsystemctl\b", line):
            commands["systemctl"].append(line)
        if re.search(r"\bsnapper\b", line):
            commands["snapper"].append(line)
        if re.search(r"\b(grub-mkconfig|grub-editenv|/etc/default/grub)\b", line):
            commands["grub"].append(line)
        if re.search(r"\b(curl|git clone|wget)\b", line):
            commands["external"].append(line)
        if re.search(r"\b(sed -i|tee|cp |mv |rm -|mkdir|ln -s|echo .*>|cat <<)\b", line):
            commands["file_mutations"].append(line)
    return {key: values[:25] for key, values in commands.items() if values}


def extract_state_variables(text: str) -> dict[str, list[str]]:
    names = ("PKG", "PKGS", "APP", "APPS", "DEPS", "SOFTWARE", "CORE", "PRE")
    found: dict[str, list[str]] = {}
    array_pattern = re.compile(r"^\s*([A-Z0-9_]*(?:PKG|PKGS|APP|APPS|DEPS|SOFTWARE|CORE|PRE)[A-Z0-9_]*)=\((.*?)\)", re.S | re.M)
    for match in array_pattern.finditer(text):
        name = match.group(1)
        body = re.sub(r"#.*", "", match.group(2))
        values = re.findall(r"['\"]([^'\"]+)['\"]|([^\s()]+)", body)
        cleaned = [a or b for a, b in values]
        found[name] = [item for item in cleaned if item and not item.startswith("#")]
    scalar_pattern = re.compile(r"^\s*([A-Z0-9_]*(?:PKG|PKGS|APP|APPS|DEPS|SOFTWARE|CORE|PRE)[A-Z0-9_]*)=\"([^\"]+)\"", re.M)
    for match in scalar_pattern.finditer(text):
        name, value = match.groups()
        if name in found:
            continue
        found[name] = [item for item in value.split() if item]
    for key in list(found):
        if not any(token in key for token in names):
            del found[key]
    return found


def bullet_list(items: list[str]) -> str:
    if not items:
        return "- None detected.\n"
    return "".join(f"- `{item}`\n" for item in items)


def generate_module(path: Path, source_root: Path, module_id: str | None = None) -> None:
    rel = path.relative_to(source_root).as_posix()
    module_id = module_id or path.stem
    phase, risk, purpose = MODULE_META.get(module_id, ("undocumented", "medium", "Generated module spec from source."))
    text = read_text(path)
    commands = extract_commands(text)
    state_vars = extract_state_variables(text)
    requires_root = "check_root" in text or "EUID" in text
    out = RESOURCES / "modules" / f"{module_id}.md"
    command_sections = []
    for name, values in commands.items():
        command_sections.append(f"### {name}\n\n{bullet_list(values)}")
    command_text = "\n".join(command_sections) if command_sections else "No system-changing commands were extracted."
    variable_sections = []
    for name, values in state_vars.items():
        variable_sections.append(f"### {name}\n\n{bullet_list(values[:80])}")
    variable_text = "\n".join(variable_sections) if variable_sections else "No package or app state variables were extracted."
    content = f"""---
id: {module_id}
source: {path}
source_relative: {rel}
phase: {phase}
risk: {risk}
requires_root: {yaml_bool(requires_root)}
language: bash
mode: "{mode_string(path)}"
sha256: "{sha256_file(path)}"
generated_from: bash-source
---

# {module_id}

## Intent

{purpose}

## Declarative Reading Notes

This module is a Markdown declaration of the original Bash behavior. Treat the embedded Bash as
source evidence, not as the preferred execution path. When applying this module, first audit the
current system state, then apply only the missing state described by package, file, service, and
verification sections.

## Extracted Mutating Commands

{command_text}

## Extracted Package/App State Variables

{variable_text}

## Verification Guidance

- Verify packages mentioned by package-manager commands are installed.
- Verify files mentioned by file mutation commands exist and contain the desired state.
- Verify services mentioned by `systemctl` commands are enabled or active as declared.
- For high or critical risk modules, create or confirm a relevant Btrfs/snapper checkpoint first.

## Rollback Guidance

- Prefer Btrfs/snapper rollback markers when the module changes system state.
- For desktop-stage changes, prefer the `Before Desktop Environments` checkpoint.
- For base-stage changes, prefer the `Before Shorin Setup` checkpoint.
- Do not run destructive rollback commands without explicit user confirmation.

## Legacy Bash Source

{FENCE}bash
{text}
{FENCE}
"""
    write_text(out, content)


def generate_modules() -> None:
    rows: list[str] = []
    top_level = [
        (SETUP_REPO / "install.sh", "install"),
        (SETUP_REPO / "strap.sh", "strap"),
        (SETUP_REPO / "strap-proxy.sh", "strap-proxy"),
        (SETUP_REPO / "undochange.sh", "undochange"),
    ]
    for path, module_id in top_level:
        if path.exists():
            generate_module(path, SETUP_REPO, module_id)
            phase, risk, purpose = MODULE_META.get(module_id, ("undocumented", "medium", "Generated module spec from source."))
            rows.append(f"| `{module_id}` | `{phase}` | `{risk}` | `{path.relative_to(SETUP_REPO).as_posix()}` | {purpose} |")
    for path in sorted((SETUP_REPO / "scripts").glob("*.sh")):
        module_id = path.stem
        generate_module(path, SETUP_REPO)
        phase, risk, purpose = MODULE_META.get(module_id, ("undocumented", "medium", "Generated module spec from source."))
        rows.append(f"| `{module_id}` | `{phase}` | `{risk}` | `{path.relative_to(SETUP_REPO).as_posix()}` | {purpose} |")
    write_text(RESOURCES / "modules" / "modules-index.md", f"""# Modules Index

Generated from `{SETUP_REPO}`.

| Module | Phase | Risk | Source | Intent |
| --- | --- | --- | --- | --- |
""" + "\n".join(rows) + "\n")


def capsule_target_for_niri(path: Path) -> str:
    rel = path.relative_to(NIRI_REPO).as_posix()
    if rel.startswith("dotfiles/"):
        return rel[len("dotfiles/"):]
    return rel


def is_protected(target: str) -> bool:
    return any(target == rule or target.startswith(rule.rstrip("/") + "/") for rule in PROTECTED_PATHS)


def is_generated(target: str) -> bool:
    return target in GENERATED_PATHS


def capsule_path_for(target: str) -> Path:
    return RESOURCES / "profiles" / "shorin-niri" / "dotfiles" / f"{target}.md"


def write_dotfile_capsule(path: Path, status_map: dict[str, str]) -> Capsule:
    rel = path.relative_to(NIRI_REPO).as_posix()
    target = capsule_target_for_niri(path)
    protected = is_protected(target)
    generated = is_generated(target)
    executable = os.access(path, os.X_OK)
    mode = mode_string(path)
    digest = sha256_file(path)
    language = language_for(path)
    status = status_map.get(rel, "clean")
    update_policy = "generate" if generated else "protect" if protected else "replace"
    capsule = capsule_path_for(target)
    text = read_text(path)
    content = f"""---
source: {rel}
target: {target}
type: text
language: {language}
mode: "{mode}"
executable: {yaml_bool(executable)}
protected: {yaml_bool(protected)}
generated: {yaml_bool(generated)}
update_policy: {update_policy}
owner_scope: user
backup: true
sha256: "{digest}"
size_bytes: {path.stat().st_size}
git_status: {status}
---

# {target}

Source: `{rel}`

Install target: `~/{target}`

{FENCE}{language}
{text}
{FENCE}
"""
    write_text(capsule, content)
    return Capsule(path, rel, target, capsule, mode, digest, path.stat().st_size, language, protected, generated, executable, update_policy, status)


def copy_asset(path: Path, source_root: Path, dest_root: Path) -> tuple[str, str, str, int]:
    rel = path.relative_to(source_root).as_posix()
    dest = dest_root / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, dest)
    return rel, dest.relative_to(RESOURCES).as_posix(), sha256_file(path), path.stat().st_size


def iter_source_files(root: Path) -> list[Path]:
    return [p for p in sorted(root.rglob("*")) if p.is_file() and ".git" not in p.parts]


def generate_niri_profile() -> None:
    global PROTECTED_PATHS, GENERATED_PATHS
    profile_root = RESOURCES / "profiles" / "shorin-niri"
    profile_root.mkdir(parents=True, exist_ok=True)
    shorinniri_text = read_text(NIRI_REPO / "shorinniri")
    PROTECTED_PATHS = set(parse_bash_array(shorinniri_text, "UPDATE_IGNORE"))
    GENERATED_PATHS = parse_matugen_outputs(NIRI_REPO / "dotfiles" / ".config" / "matugen" / "config.toml")
    status_map = git_status_map(NIRI_REPO)
    capsules: list[Capsule] = []
    assets: list[tuple[str, str, str, int]] = []
    asset_root = profile_root / "assets"
    for path in iter_source_files(NIRI_REPO):
        rel = path.relative_to(NIRI_REPO).as_posix()
        if rel.startswith(".git/"):
            continue
        if is_binary(path) or path.suffix.lower() == ".svg":
            assets.append(copy_asset(path, NIRI_REPO, asset_root))
        else:
            capsules.append(write_dotfile_capsule(path, status_map))
    write_niri_manifests(capsules, assets)


def parse_bash_array(text: str, name: str) -> list[str]:
    match = re.search(rf"{re.escape(name)}=\((.*?)\)", text, re.S)
    if not match:
        return []
    body = re.sub(r"#.*", "", match.group(1))
    return re.findall(r"['\"]([^'\"]+)['\"]", body)


def write_niri_manifests(capsules: list[Capsule], assets: list[tuple[str, str, str, int]]) -> None:
    profile_root = RESOURCES / "profiles" / "shorin-niri"
    shorinniri_text = read_text(NIRI_REPO / "shorinniri")
    packages = parse_bash_array(shorinniri_text, "TARGET_SOFTWARE")
    ignores = parse_bash_array(shorinniri_text, "UPDATE_IGNORE")
    package_lines = "\n".join(f"- `{pkg}`" for pkg in packages)
    ignore_lines = "\n".join(f"- `{item}`" for item in ignores)
    generated_lines = "\n".join(f"- `{item}`" for item in sorted(GENERATED_PATHS))
    write_text(profile_root / "profile.md", f"""# Shorin Niri Profile

Source profile: `{NIRI_REPO}`

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

- Text capsules: {len(capsules)}
- Assets: {len(assets)}
- Dirty source files captured: {sum(1 for c in capsules if c.status != 'clean')}
""")
    write_text(profile_root / "packages.md", f"""# Shorin Niri Packages

Generated from `shorinniri` `TARGET_SOFTWARE`.

## Target Software

{package_lines}

## Package Manager Rule

Use `yay` if available; otherwise use `paru`. If neither exists, install or configure an AUR
helper before applying this profile.

## Verification

Check all installed packages with `pacman -Q` where possible. AUR helper package names are still
visible to pacman after installation.
""")
    write_text(profile_root / "protected-paths.md", f"""# Protected Paths

Generated from `shorinniri` `UPDATE_IGNORE`.

During update mode, skip any target that equals one of these paths or is below one of these paths.

{ignore_lines}

## User Extension

Also merge entries from `~/.config/shorin-niri/protected.list`.

## Generated Paths

Treat these as generated/runtime-owned and do not overwrite them during normal update:

{generated_lines}
""")
    write_text(profile_root / "verification.md", """# Shorin Niri Verification

## Package Checks

```sh
command -v yay || command -v paru
pacman -Q shorin-niri-git xdg-desktop-portal-gnome cliphist-tui-git kitty firefox fcitx5 fcitx5-rime
```

## Dotfile Checks

```sh
test -f ~/.config/niri/config.kdl
test -f ~/.config/niri/binds.kdl
test -f ~/.config/niri/rule.kdl
test -f ~/.config/matugen/config.toml
test -f ~/.config/waybar/config.jsonc
test -f ~/.config/kitty/kitty.conf
test -f ~/.config/fuzzel/fuzzel.ini
test -x ~/.local/bin/matugen-update
```

## Runtime Command Checks

```sh
command -v niri
command -v waybar
command -v waypaper
command -v fuzzel
command -v mako
command -v fcitx5
command -v cliphist
```

## Optional Niri Validation

```sh
niri validate
```

## Matugen Checks

```sh
command -v matugen
test -f ~/.config/waybar/colors.css
test -f ~/.config/fuzzel/colors.ini
test -f ~/.config/kitty/themes/matugen.conf
test -f ~/.config/niri/colors.kdl
```
""")
    capsule_rows = "\n".join(
        f"| `{c.target_relative}` | `{c.language}` | `{c.mode}` | `{c.update_policy}` | `{c.status}` |"
        for c in capsules
    )
    write_text(profile_root / "dotfiles" / "dotfiles-index.md", f"""# Dotfiles Index

Generated from `{NIRI_REPO}` current working tree.

| Target | Language | Mode | Policy | Git Status |
| --- | --- | --- | --- | --- |
{capsule_rows}
""")
    asset_rows = "\n".join(f"| `{rel}` | `{dest}` | `{size}` | `{digest}` |" for rel, dest, digest, size in assets)
    write_text(profile_root / "assets" / "assets-index.md", f"""# Assets Index

Binary/media/icon assets copied from `{NIRI_REPO}`.

| Source | Asset Path | Size | SHA256 |
| --- | --- | ---: | --- |
{asset_rows}
""")


def generate_setup_resources() -> None:
    source_root = RESOURCES / "source-capsules" / "shorin-arch-setup"
    asset_root = RESOURCES / "assets" / "shorin-arch-setup"
    capsules: list[str] = []
    assets: list[tuple[str, str, str, int]] = []
    candidates = [
        SETUP_REPO / "common-applist.txt",
        SETUP_REPO / "kde-applist.txt",
        SETUP_REPO / "kde-common-applist.txt",
        SETUP_REPO / "exclude-dotfiles.txt",
        SETUP_REPO / "README.md",
    ]
    candidates.extend(iter_source_files(SETUP_REPO / "resources"))
    candidates.extend(iter_source_files(SETUP_REPO / "grub-themes"))
    for path in sorted(set(candidates)):
        if not path.exists() or not path.is_file():
            continue
        rel = path.relative_to(SETUP_REPO).as_posix()
        if is_binary(path):
            assets.append(copy_asset(path, SETUP_REPO, asset_root))
            continue
        target = source_root / f"{rel}.md"
        text = read_text(path)
        language = language_for(path)
        content = f"""---
source: {rel}
type: source-resource
language: {language}
mode: "{mode_string(path)}"
sha256: "{sha256_file(path)}"
size_bytes: {path.stat().st_size}
---

# {rel}

{FENCE}{language}
{text}
{FENCE}
"""
        write_text(target, content)
        capsules.append(rel)
    capsule_rows = "\n".join(f"- `{item}`" for item in capsules)
    asset_rows = "\n".join(f"| `{rel}` | `{dest}` | `{size}` | `{digest}` |" for rel, dest, digest, size in assets)
    write_text(source_root / "source-index.md", f"""# Shorin Arch Setup Source Capsules

Text data resources converted to Markdown capsules.

{capsule_rows}
""")
    write_text(asset_root / "assets-index.md", f"""# Shorin Arch Setup Assets

Binary resources copied from the original setup repository.

| Source | Asset Path | Size | SHA256 |
| --- | --- | ---: | --- |
{asset_rows}
""")


def write_source_provenance() -> None:
    def repo_block(name: str, repo: Path) -> str:
        status = git_status_map(repo)
        dirty = "\n".join(f"- `{state}` `{path}`" for path, state in sorted(status.items())) or "- clean"
        return f"""## {name}

- Path: `{repo}`
- Branch: `{git_value(repo, 'branch', '--show-current')}`
- Commit: `{git_value(repo, 'rev-parse', 'HEAD')}`

### Working Tree

{dirty}
"""
    write_text(RESOURCES / "source-provenance.md", """# Source Provenance

Generated resources capture the current working-tree content from these source repositories.

""" + repo_block("shorin-arch-setup", SETUP_REPO) + "\n" + repo_block("shorin-niri", NIRI_REPO))


def main() -> None:
    global SETUP_REPO, NIRI_REPO
    args = parse_args()
    config_setup, config_niri = load_source_config()
    SETUP_REPO = args.setup_repo.resolve() if args.setup_repo else config_setup
    NIRI_REPO = args.niri_repo.resolve() if args.niri_repo else config_niri
    if not (SETUP_REPO / "scripts").is_dir():
        raise SystemExit(f"Invalid shorin-arch-setup source: {SETUP_REPO}")
    if not (NIRI_REPO / "shorinniri").is_file():
        raise SystemExit(f"Invalid shorin-niri source: {NIRI_REPO}")
    clean_generated()
    generate_modules()
    generate_niri_profile()
    generate_setup_resources()
    write_source_provenance()
    print(f"Generated resources under {RESOURCES}")


if __name__ == "__main__":
    main()
