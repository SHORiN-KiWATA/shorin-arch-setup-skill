# Modules Index

Generated from `/home/shorin/Documents/github/shorin-arch-setup`.

| Module | Phase | Risk | Source | Intent |
| --- | --- | --- | --- | --- |
| `install` | `bootstrap` | `critical` | `install.sh` | Main installer orchestrator: desktop selection, optional modules, mirrors, module execution, cleanup, reboot. |
| `strap` | `bootstrap` | `high` | `strap.sh` | Bootstrap from GitHub tarball and run installer. |
| `strap-proxy` | `bootstrap` | `high` | `strap-proxy.sh` | Bootstrap a PR build by cloning and merging a pull request before running installer. |
| `undochange` | `rollback` | `critical` | `undochange.sh` | Rollback to the 'Before Shorin Setup' Btrfs snapshot. |
| `00-btrfs-init` | `base` | `critical` | `scripts/00-btrfs-init.sh` | Initialize snapper safety net, Btrfs snapshots, GRUB decoupling, and rollback commands. |
| `00-utils` | `shared` | `medium` | `scripts/00-utils.sh` | Shared logging, user detection, command execution, display-manager, dotfile, and Flatpak helper functions. |
| `01a-base` | `base` | `high` | `scripts/01a-base.sh` | Configure editor, multilib, fonts, archlinuxcn, console font, and AUR helpers. |
| `01b-nm-backend` | `optional-network` | `high` | `scripts/01b-nm-backend.sh` | Switch NetworkManager Wi-Fi backend to iwd when NetworkManager is present. |
| `02-musthave` | `base` | `high` | `scripts/02-musthave.sh` | Install essential firmware, audio, locale, input method, Bluetooth, power, fastfetch, and Flatpak support. |
| `02a-dualboot-fix` | `optional-boot` | `high` | `scripts/02a-dualboot-fix.sh` | Enable os-prober integration for Windows dual boot when Windows is detected. |
| `03a-user` | `user` | `high` | `scripts/03a-user.sh` | Create or configure target user, sudoers, XDG directories, and user PATH. |
| `03b-gpu-driver` | `optional-hardware` | `high` | `scripts/03b-gpu-driver.sh` | Install chwd and run automatic hardware driver detection. |
| `03c-snapshot-before-desktop` | `checkpoint` | `medium` | `scripts/03c-snapshot-before-desktop.sh` | Create the pre-desktop snapper checkpoint and remove stale compositor autostarts. |
| `04-niri-setup` | `desktop` | `high` | `scripts/04-niri-setup.sh` | Install Shorin Niri meta package, run shorinniri init, copy wallpapers, and configure display manager. |
| `04b-kdeplasma-setup` | `desktop` | `high` | `scripts/04b-kdeplasma-setup.sh` | Install KDE Plasma, optional KDE app list, KDE dotfiles, and Plasma login manager. |
| `04c-dms-quickshell` | `desktop` | `critical` | `scripts/04c-dms-quickshell.sh` | Run external DankMaterialShell installer and add Niri/Fcitx/file-manager integration. |
| `04d-gnome` | `desktop` | `high` | `scripts/04d-gnome.sh` | Install and configure GNOME, extensions, gsettings, dotfiles, Firefox policy, and GDM. |
| `04e-illogical-impulse-end4-quickshell` | `desktop` | `critical` | `scripts/04e-illogical-impulse-end4-quickshell.sh` | Run external Illogical Impulse End4 installer and configure display manager. |
| `04f-ambxst-quickshell` | `desktop-legacy` | `high` | `scripts/04f-ambxst-quickshell.sh` | Legacy/experimental Noctalia Niri autologin module not wired in the main installer. |
| `04g-caelestia-quickshell` | `desktop` | `critical` | `scripts/04g-caelestia-quickshell.sh` | Clone Caelestia dots, run its installer, add file-manager deps, and configure display manager. |
| `04h-shorindms-quickshell` | `desktop` | `high` | `scripts/04h-shorindms-quickshell.sh` | Install Shorin DMS Niri meta package and run shorindms init. |
| `04i-shorin-hyprniri-quickshell` | `desktop` | `high` | `scripts/04i-shorin-hyprniri-quickshell.sh` | Install Hyprland/Niri DMS hybrid environment, clone dotfiles, apply policies, and configure display manager. |
| `04j-minimal-niri` | `desktop` | `high` | `scripts/04j-minimal-niri.sh` | Install minimal Niri from local dotfiles and package groups. |
| `04k-shorin-noctalia-quickshell` | `desktop` | `high` | `scripts/04k-shorin-noctalia-quickshell.sh` | Install Shorin Noctalia Niri profile from local dotfiles. |
| `04l-minimal-labwc` | `desktop` | `high` | `scripts/04l-minimal-labwc.sh` | Install minimal Labwc profile from local dotfiles. |
| `04m-inir-quickshell` | `desktop` | `critical` | `scripts/04m-inir-quickshell.sh` | Clone and run external iNiR installer, then patch Niri/Fcitx/file-manager integration. |
| `05-verify-desktop` | `verify` | `medium` | `scripts/05-verify-desktop.sh` | Verify package shipment list and key desktop config paths. |
| `07-grub-theme` | `optional-boot` | `high` | `scripts/07-grub-theme.sh` | Configure GRUB kernel parameters, themes, power entries, and regenerate GRUB config. |
| `99-apps` | `optional-apps` | `high` | `scripts/99-apps.sh` | Install common applications from repo/AUR/Flatpak lists and apply app-specific tweaks. |
| `de-undochange` | `rollback` | `critical` | `scripts/de-undochange.sh` | Rollback to the 'Before Desktop Environments' Btrfs snapshot. |
