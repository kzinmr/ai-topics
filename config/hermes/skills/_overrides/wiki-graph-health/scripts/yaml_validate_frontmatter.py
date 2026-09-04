#!/usr/bin/env python3
"""Validate YAML frontmatter of every L2 wiki page.

wiki_health.py silently returns {} on YAML failure, so this independent scan is the
authoritative frontmatter health check. Exit 1 if any page fails to parse.

Usage:
  /opt/data/.hermes/venv/bin/python scripts/yaml_validate_frontmatter.py [--detail]

Run from ~/ai-topics. Scope: entities/ concepts/ comparisons/ queries/ events/,
skipping _archive/ subtrees. Frontmatter = text between first two '---' lines.
"""
import os
import re
import sys

try:
    import yaml
except ImportError:
    print("NO PyYAML — run with /opt/data/.hermes/venv/bin/python (system python3 may lack it)")
    sys.exit(2)

WIKI = "/opt/data/ai-topics/wiki"
DETAIL = "--detail" in sys.argv


def scan():
    fails = []
    for subdir in ["entities", "concepts", "comparisons", "queries", "events"]:
        base = os.path.join(WIKI, subdir)
        if not os.path.isdir(base):
            continue
        for root, dirs, files in os.walk(base):
            if "_archive" in root.split(os.sep):
                continue
            for f in files:
                if not f.endswith(".md"):
                    continue
                path = os.path.join(root, f)
                rel = os.path.relpath(path, WIKI)
                with open(path) as fh:
                    content = fh.read()
                if not content.startswith("---"):
                    continue
                end = content.find("\n---", 3)
                if end == -1:
                    continue
                fm = content[3:end]
                try:
                    data = yaml.safe_load(fm)
                    if not isinstance(data, dict):
                        fails.append((rel, f"not a dict: {type(data).__name__}", ""))
                except Exception as e:
                    lm = None
                    for m in re.finditer(r"line (\d+)", str(e)):
                        lm = int(m.group(1))
                    line = ""
                    if lm:
                        lines = fm.split("\n")
                        if 0 < lm <= len(lines):
                            line = lines[lm - 1]
                    fails.append((rel, str(e).split("\n")[0][:90], line))
    return fails


def main():
    fails = scan()
    print(f"YAML parse failures: {len(fails)}")
    for rel, err, line in fails:
        print(f"  {rel}: {err}")
        if DETAIL and line:
            print(f"      line: {line[:150]}")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
