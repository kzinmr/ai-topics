#!/usr/bin/env python3
"""Relay the latest ai-topics-slack-hot-posts output to Discord verbatim.

Reads the most recent output file from the Slack hot-posts cron job,
extracts the actual delivered content after "## Response",
and prints it to stdout for no_agent delivery to Discord.
Silent (no output) if no Slack output file exists."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path


def main() -> None:
    hermes_home = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
    slack_job_output = hermes_home / "cron" / "output" / "5e91a0b47c32"

    if not slack_job_output.is_dir():
        sys.exit(0)

    files = sorted(slack_job_output.glob("*.md"), reverse=True)
    if not files:
        sys.exit(0)

    content = files[0].read_text(encoding="utf-8", errors="replace")

    # Extract everything after "## Response" to end of file
    response_match = re.search(
        r"^## Response\s*\n(.*)",
        content,
        re.MULTILINE | re.DOTALL,
    )
    if response_match:
        delivered = response_match.group(1).strip()
    else:
        delivered = content.strip()

    if delivered:
        print(delivered)
    # Else: silent — nothing to relay


if __name__ == "__main__":
    main()
