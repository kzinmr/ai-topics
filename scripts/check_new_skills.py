#!/usr/bin/env python3
"""Detect new/removed local skills in ~/.hermes/skills/ vs managed baseline.

Baseline: config/hermes/skills/ in the ai-topics repo.
Target:   ~/.hermes/skills/ (local skills only, excluding builtin).

Outputs a summary to stdout for Hermes cron --script injection.
"""
import json
import sys
from pathlib import Path

HERMES_SKILLS = Path.home() / ".hermes" / "skills"
BUILTIN_SKILLS = Path.home() / ".hermes" / "hermes-agent" / "skills"
MANAGED_SKILLS = Path(__file__).resolve().parent.parent / "config" / "hermes" / "skills"
STATE_FILE = Path(__file__).resolve().parent / "cache" / "skills_baseline.json"


def find_local_skills(skills_dir: Path) -> dict[str, str]:
    """Find all skill dirs containing SKILL.md. Returns {name: category}."""
    skills = {}
    if not skills_dir.exists():
        return skills
    for skill_md in skills_dir.rglob("SKILL.md"):
        skill_dir = skill_md.parent
        # category/skill-name/SKILL.md -> category = parent of skill_dir
        rel = skill_dir.relative_to(skills_dir)
        parts = rel.parts
        if len(parts) == 2:
            category, name = parts
        elif len(parts) == 1:
            category, name = "uncategorized", parts[0]
        else:
            continue
        skills[name] = category
    return skills


def load_state() -> dict[str, str]:
    """Load previous scan state."""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(skills: dict[str, str]):
    """Save current scan state."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(skills, indent=2))


def main():
    hermes_skills = find_local_skills(HERMES_SKILLS)
    builtin_skills = find_local_skills(BUILTIN_SKILLS)
    managed_skills = find_local_skills(MANAGED_SKILLS)
    previous = load_state()

    # Unmanaged = in .hermes/skills, not builtin, not managed
    unmanaged = {
        k: v for k, v in hermes_skills.items()
        if k not in managed_skills and k not in builtin_skills
    }

    # Diff against previous scan (filter both sides to unmanaged-only)
    prev_unmanaged = {
        k: v for k, v in previous.items()
        if k not in managed_skills and k not in builtin_skills
    }
    new_skills = {k: v for k, v in unmanaged.items() if k not in prev_unmanaged}
    removed_skills = {k: v for k, v in prev_unmanaged.items() if k not in unmanaged}

    # Save only unmanaged state (builtin changes are noise)
    save_state(unmanaged)

    # Output report
    lines = []

    if new_skills:
        lines.append(f"## New unmanaged skills ({len(new_skills)})")
        for name, cat in sorted(new_skills.items()):
            lines.append(f"- **{name}** (category: {cat})")
        lines.append("")

    if removed_skills:
        lines.append(f"## Removed skills ({len(removed_skills)})")
        for name, cat in sorted(removed_skills.items()):
            lines.append(f"- **{name}** (was: {cat})")
        lines.append("")

    lines.append(f"## Summary")
    lines.append(f"- Managed (git): {len(managed_skills)}")
    lines.append(f"- Unmanaged (local): {len(unmanaged)}")
    lines.append(f"- Builtin: {len(builtin_skills)}")

    if unmanaged and not new_skills:
        lines.append("")
        lines.append("### Unmanaged local skills (for review)")
        for name, cat in sorted(unmanaged.items()):
            lines.append(f"- {name} ({cat})")

    print("\n".join(lines))

    # Exit 0 even if nothing new (cron always runs)
    return 0


if __name__ == "__main__":
    sys.exit(main())
