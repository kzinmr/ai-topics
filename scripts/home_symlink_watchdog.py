#!/usr/bin/env python3
"""Watchdog: verify profile-local links point at canonical profile paths."""
import os
import sys
from pathlib import Path

PROFILE_ROOT = Path(os.environ.get("HERMES_PROFILE_ROOT") or os.environ.get("HERMES_SUBPROCESS_HOME") or Path.home()).expanduser()
EXPECTED_LINKS = {
    PROFILE_ROOT / "wiki": PROFILE_ROOT / "ai-topics" / "wiki",
}
OPTIONAL_LINKS = {
    PROFILE_ROOT / "bin" / "xurl": PROFILE_ROOT / ".hermes" / "bin" / "xurl",
}

issues = []


def check_link(path: Path, target: Path, required: bool) -> None:
    if not path.exists() and not path.is_symlink():
        if required:
            issues.append(f"MISSING: {path}")
        return
    if not path.is_symlink():
        kind = "directory" if path.is_dir() else "file"
        issues.append(f"NOT_A_SYMLINK: {path} is a real {kind}")
        return
    if path.resolve() != target.resolve():
        issues.append(f"WRONG_TARGET: {path} -> {path.resolve()} (expected {target.resolve()})")


for link, target in EXPECTED_LINKS.items():
    check_link(link, target, required=True)

for link, target in OPTIONAL_LINKS.items():
    check_link(link, target, required=False)

if issues:
    for issue in issues:
        print(f"ERROR: {issue}")
    sys.exit(1)

sys.exit(0)
