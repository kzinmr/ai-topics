#!/usr/bin/env python3
"""Pre-run script for the unified wiki-health-fix cron job.

Runs wiki_health.py --json and outputs the structured data for the agent.
"""
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parent / "wiki_health.py"

result = subprocess.run(
    [sys.executable, str(SCRIPT), "--json"],
    capture_output=True,
    text=True,
    timeout=120,
    cwd=str(SCRIPT.parent.parent),
)

if result.returncode != 0:
    print(f'{{"ok": false, "error": "wiki_health.py failed", "stderr": {result.stderr!r}}}')
    sys.exit(0)

sys.stdout.write(result.stdout)
