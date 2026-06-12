#!/usr/bin/env python3
"""Compatibility wrapper for the skill-local resource generator."""

from __future__ import annotations

from pathlib import Path
import runpy


PROJECT_ROOT = Path(__file__).resolve().parents[1]
GENERATOR = PROJECT_ROOT / ".opencode" / "skills" / "shorin-arch-setup" / "tools" / "generate_resources.py"

runpy.run_path(str(GENERATOR), run_name="__main__")
