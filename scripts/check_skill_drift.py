#!/usr/bin/env python3
"""
Compare Hermes formula skills with _overrides/ to detect drift.
Outputs JSON report of skills that have diverged from formula.

Formula skills are searched recursively under ~/.hermes/skills (they may be
flat, e.g. ~/.hermes/skills/dogfood, or category-nested, e.g.
~/.hermes/skills/research/active-crawl-wiki). Archive/backup directories
(.archive, .curator_backups, .hub, .quarantine) are excluded.
"""
import os
import sys
import json
from pathlib import Path
from datetime import datetime

HERMES_SKILLS = Path.home() / ".hermes" / "skills"
OVERRIDES_DIR = Path.home() / "ai-topics" / "config" / "hermes" / "skills" / "_overrides"

# Directories under HERMES_SKILLS that are NOT live formula skills
# (archives, curator backups, hub cache, quarantine).
EXCLUDED_DIRS = {".archive", ".curator_backups", ".hub", ".quarantine"}

def get_skill_version(skill_dir):
    """Extract version or last modified from SKILL.md frontmatter."""
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return None
    try:
        content = skill_md.read_text()
        # Try to find version in frontmatter
        if content.startswith("---"):
            frontmatter = content.split("---")[1]
            for line in frontmatter.split("\n"):
                if line.strip().startswith("version:"):
                    return line.split(":", 1)[1].strip()
        # Fallback to file mtime
        return datetime.fromtimestamp(skill_md.stat().st_mtime).isoformat()
    except Exception as e:
        return f"error: {e}"

def get_skill_files(skill_dir):
    """Get set of all files in a skill directory."""
    files = set()
    for f in skill_dir.rglob("*"):
        if f.is_file() and not f.name.startswith("."):
            files.add(f.relative_to(skill_dir))
    return files

def find_formula_skill(skill_name):
    """Find the live formula skill dir for skill_name.

    Formula skills may live directly under HERMES_SKILLS (flat, e.g.
    ``~/.hermes/skills/dogfood``) or under a category subdirectory (e.g.
    ``~/.hermes/skills/research/active-crawl-wiki``). Search recursively and
    return the shallowest match; None if not found. Excludes archive/backup
    directories.
    """
    matches = []
    for f in HERMES_SKILLS.rglob("SKILL.md"):
        parts = f.relative_to(HERMES_SKILLS).parts
        if parts[0] in EXCLUDED_DIRS:
            continue
        if f.parent.name == skill_name:
            matches.append(f.parent)
    if not matches:
        return None
    # Shallowest match is the canonical formula location
    return min(matches, key=lambda p: len(p.relative_to(HERMES_SKILLS).parts))

def compare_skills():
    """Compare formula skills with overrides."""
    report = {
        "timestamp": datetime.now().isoformat(),
        "checks": [],
        "drifted": [],
        "missing_formula": [],
        "missing_override": []
    }

    if not OVERRIDES_DIR.exists():
        print(json.dumps({"error": "OVERRIDES_DIR not found"}))
        return

    # Get all override skills
    override_skills = set()
    for d in OVERRIDES_DIR.iterdir():
        if d.is_dir() and (d / "SKILL.md").exists():
            override_skills.add(d.name)

    # Check each override against formula
    for skill_name in sorted(override_skills):
        override_dir = OVERRIDES_DIR / skill_name
        formula_dir = find_formula_skill(skill_name)
        expected_flat = HERMES_SKILLS / skill_name

        check = {
            "skill": skill_name,
            "override_path": str(override_dir),
            "formula_path": str(formula_dir) if formula_dir else str(expected_flat),
            "formula_exists": formula_dir is not None,
            "status": "unknown"
        }

        if formula_dir is None:
            check["status"] = "formula_missing"
            report["missing_formula"].append(skill_name)
        else:
            # Compare files
            override_files = get_skill_files(override_dir)
            formula_files = get_skill_files(formula_dir)

            only_override = override_files - formula_files
            only_formula = formula_files - override_files
            common = override_files & formula_files

            # Check if common files differ
            modified = []
            for f in common:
                try:
                    if (override_dir / f).read_bytes() != (formula_dir / f).read_bytes():
                        modified.append(str(f))
                except PermissionError:
                    print(f"WARNING: unreadable formula file: {formula_dir / f}", file=sys.stderr)
                except Exception:
                    pass

            check["only_override"] = sorted([str(f) for f in only_override])
            check["only_formula"] = sorted([str(f) for f in only_formula])
            check["modified"] = modified

            if only_formula:
                check["status"] = "formula_has_new_files"
                report["drifted"].append(skill_name)
            elif modified:
                check["status"] = "formula_updated"
                report["drifted"].append(skill_name)
            else:
                check["status"] = "in_sync"

        report["checks"].append(check)

    # Output
    print(json.dumps(report, indent=2, ensure_ascii=False))

    # Summary to stderr
    print(f"\n=== SUMMARY ===", file=sys.stderr)
    print(f"Total overrides: {len(override_skills)}", file=sys.stderr)
    print(f"Drifted (need review): {len(report['drifted'])}", file=sys.stderr)
    print(f"Formula missing: {len(report['missing_formula'])}", file=sys.stderr)
    if report['drifted']:
        print(f"\nDrifted skills:", file=sys.stderr)
        for s in report['drifted']:
            print(f"  - {s}", file=sys.stderr)

if __name__ == "__main__":
    compare_skills()
