#!/usr/bin/env python3
"""Detect new/removed local skills in ~/.hermes/skills/ vs managed baseline.

Baseline: config/hermes/skills/ in the ai-topics repo (git-tracked).
Target:   ~/.hermes/skills/ (local runtime skills only, excluding builtin).

Outputs a summary to stdout for Hermes cron --script injection.

HISTORY / PITFALLS (do not regress these):
- 2026-08-23 repo restructured skills into _custom/ _overrides/ _adhoc/, which broke
  the original category/<name>/SKILL.md assumption -> "Managed (git): 0" forever.
- This script is *copied* to ~/.hermes/scripts/ for cron, so MANAGED_SKILLS must be an
  absolute path. Deriving it from __file__ silently yields a non-existent dir and makes
  every repo-managed skill show up as "unmanaged".
- Skills are loaded from several sources; the only trustworthy "is this a real skill?"
  oracle is `hermes skills list`. Repo-copy-only skills are not loaded at runtime and
  must not be counted as new work.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

AI_TOPICS = Path("/opt/data/ai-topics")
HERMES_SKILLS = Path.home() / ".hermes" / "skills"
BUILTIN_SKILLS = Path.home() / ".hermes" / "hermes-agent" / "skills"
HERMES_BIN = Path("/opt/data/.local/bin/hermes")
STATE_FILE = Path(__file__).resolve().parent / "cache" / "skills_baseline.json"

# Managed = git-tracked under config/hermes/skills (any depth: _custom/, _overrides/,
# _adhoc/, or the legacy managed/ dir), or under the legacy runtime managed/ dir.
MANAGED_SEARCH_ROOTS = [AI_TOPICS / "config" / "hermes" / "skills", HERMES_SKILLS / "managed"]


def skill_names(roots) -> set[str]:
    """Return skill directory names containing a SKILL.md under any root (any depth)."""
    names: set[str] = set()
    for root in roots:
        root = Path(root)
        if not root.exists():
            continue
        for skill_md in root.rglob("SKILL.md"):
            if ".archive" in skill_md.parts:
                continue
            names.add(skill_md.parent.name)
    return names


def runtime_skills() -> dict[str, str]:
    """Authoritative loaded-skill map {name: source} from `hermes skills list`.

    Returns {} if the CLI is unavailable, so callers can fall back to a filesystem scan.
    """
    if not HERMES_BIN.exists():
        return {}
    try:
        # COLUMNS keeps rich from truncating skill names to "…", which would silently
        # drop them from the inventory.
        env = {**os.environ, "COLUMNS": "200", "NO_COLOR": "1"}
        out = subprocess.run(
            [str(HERMES_BIN), "skills", "list"],
            capture_output=True, text=True, timeout=180, env=env,
        ).stdout
    except Exception:
        return {}
    skills: dict[str, str] = {}
    for line in out.splitlines():
        if "│" not in line and "|" not in line:
            continue
        # Splitting a bordered row yields leading/trailing emptics: ['', name, cat,
        # source, trust, status, ''] -> strip first so indexes are stable.
        cells = [c.strip() for c in re.split(r"[│|]", line)][1:]
        if len(cells) < 3 or cells[0] in ("", "Name"):
            continue
        name = cells[0]
        if not name or name.endswith("…"):  # truncated cell -> unreliable name
            continue
        skills[name] = cells[2]
    return skills


def filesystem_skills(skills_dir: Path) -> dict[str, str]:
    """Fallback scan: {name: category} for a skills tree, skipping .archive/."""
    skills: dict[str, str] = {}
    if not skills_dir.exists():
        return skills
    for skill_md in skills_dir.rglob("SKILL.md"):
        if ".archive" in skill_md.parts:
            continue
        skill_dir = skill_md.parent
        # A skill directory whose name differs from its frontmatter name is a stray
        # artifact, not a loadable skill — ignore it for inventory purposes.
        declared = ""
        for line in skill_md.read_text(errors="ignore").splitlines()[:20]:
            if line.startswith("name:"):
                declared = line.split(":", 1)[1].strip().strip("\"'")
                break
        if declared and declared != skill_dir.name:
            continue
        parts = skill_dir.relative_to(skills_dir).parts
        if len(parts) == 2:
            skills[parts[1]] = parts[0]
        elif len(parts) == 1:
            skills[parts[0]] = "uncategorized"
    return skills


def load_state() -> dict[str, str]:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            return {}
    return {}


def save_state(skills: dict[str, str]):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(skills, indent=2, sort_keys=True))


def main():
    managed = skill_names(MANAGED_SEARCH_ROOTS)

    runtime = runtime_skills()
    builtin_fs = filesystem_skills(BUILTIN_SKILLS)
    if runtime:
        local = {n: s for n, s in runtime.items() if s != "builtin"}
        builtin = {n: s for n, s in runtime.items() if s == "builtin"}
        builtin.update({n: "builtin" for n in builtin_fs if n not in builtin})
    else:
        local = filesystem_skills(HERMES_SKILLS)
        builtin = builtin_fs

    # Unmanaged = loaded at runtime, not builtin, not git-tracked in the repo.
    unmanaged = {k: v for k, v in local.items() if k not in managed and k not in builtin}

    previous = load_state()
    new_skills = {k: v for k, v in unmanaged.items() if k not in previous}
    removed_skills = {k: v for k, v in previous.items() if k not in unmanaged}

    save_state(unmanaged)

    lines = []
    if new_skills:
        lines.append(f"## New unmanaged skills ({len(new_skills)})")
        for name, cat in sorted(new_skills.items()):
            lines.append(f"- **{name}** (category: {cat})")
        lines.append("")
    if removed_skills:
        lines.append(f"## Removed skills ({len(removed_skills)})")
        for name, cat in sorted(removed_skills.items()):
            lines.append(f"- {name} (was: {cat})")
        lines.append("")

    lines.append("## Summary")
    lines.append(f"- Managed (git): {len(managed)}")
    lines.append(f"- Unmanaged (local): {len(unmanaged)}")
    lines.append(f"- Builtin: {len(builtin)}")
    if not runtime:
        lines.append("- NOTE: `hermes skills list` unavailable; used filesystem scan.")

    if unmanaged and not new_skills:
        lines.append("")
        lines.append("### Unmanaged local skills (for review)")
        for name, cat in sorted(unmanaged.items()):
            lines.append(f"- {name} ({cat})")

    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
