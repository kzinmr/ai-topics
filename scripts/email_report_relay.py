#!/usr/bin/env python3
"""
Hermes Email Report Relay — reads latest Slack hot-posts output and forwards via Cloudflare Email.

Architecture:
  Slack cron (5e91a0b47c32) → output files → this script reads latest → Cloudflare Email API

Mirrors the Discord relay pattern (discord_slack_relay.py) but with email as transport.
Designed to run as a no_agent=True cron job — zero tokens, zero LLM cost.

Env vars needed (in addition to cloudflare_email.py requirements):
  SLACK_OUTPUT_DIR     — Path to Slack cron output dir (default: ~/.hermes/cron/output/5e91a0b47c32)
  CF_EMAIL_TO          — Report recipient(s)
  CF_EMAIL_SUBJECT_PREFIX — Subject prefix (default: "[Hermes Report]")
"""

import os
import sys
import re
import glob
from datetime import datetime

# Add ai-topics/scripts to path for cloudflare_email module
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
AI_TOPICS_SCRIPTS = os.path.expanduser("~/ai-topics/scripts")
if AI_TOPICS_SCRIPTS not in sys.path:
    sys.path.insert(0, AI_TOPICS_SCRIPTS)

from cloudflare_email import send_email_via_cloudflare

# ── Configuration ─────────────────────────────────────────────────────────
SLACK_OUTPUT_DIR = os.environ.get(
    "SLACK_OUTPUT_DIR",
    os.path.expanduser("~/.hermes/cron/output/5e91a0b47c32")
)

# ── Content extraction ────────────────────────────────────────────────────


def find_latest_slack_output() -> str | None:
    """Find the most recent Slack hot-posts output file."""
    pattern = os.path.join(SLACK_OUTPUT_DIR, "*.md")
    files = glob.glob(pattern)
    if not files:
        return None
    return max(files, key=os.path.getmtime)


def extract_response_from_md(filepath: str) -> str | None:
    """
    Extract the agent response from a Slack cron output markdown file.

    The file format is:
      # Cron Job: ...
      ## Prompt
      ...
      ## Response
      <actual report content>
    """
    with open(filepath) as f:
        content = f.read()

    # Find "## Response" section
    match = re.search(r"^## Response\s*\n(.*)", content, re.DOTALL | re.MULTILINE)
    if not match:
        return None

    response = match.group(1).strip()
    return response


def md_to_html(md_text: str) -> str:
    """
    Convert markdown to basic HTML for email.
    Handles the most common patterns: headers, bold, italic, links, tables, code blocks.
    """
    # Escape HTML entities first
    text = md_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    lines = text.split("\n")
    html_lines = []
    in_code_block = False
    in_table = False

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Code blocks
        if stripped.startswith("```"):
            if in_code_block:
                html_lines.append("</code></pre>")
                in_code_block = False
            else:
                html_lines.append('<pre style="background:#1e1e1e;color:#d4d4d4;padding:12px;border-radius:6px;overflow-x:auto;"><code>')
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            html_lines.append(line)
            i += 1
            continue

        # Horizontal rules
        if stripped == "---":
            html_lines.append("<hr>")
            i += 1
            continue

        # Headers
        if stripped.startswith("#### "):
            html_lines.append(f"<h4>{stripped[5:]}</h4>")
            i += 1
            continue
        if stripped.startswith("### "):
            html_lines.append(f"<h3>{stripped[4:]}</h3>")
            i += 1
            continue
        if stripped.startswith("## "):
            html_lines.append(f"<h2>{stripped[3:]}</h2>")
            i += 1
            continue
        if stripped.startswith("# "):
            html_lines.append(f"<h1>{stripped[2:]}</h1>")
            i += 1
            continue

        # Tables
        if "|" in stripped and stripped.startswith("|"):
            if not in_table:
                html_lines.append('<table style="border-collapse:collapse;width:100%;">')
                in_table = True

            # Skip separator rows like |---|---|
            if re.match(r"^\|[\s\-:]+\|", stripped):
                i += 1
                continue

            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            tag = "th" if in_table and i < len(lines) and not re.match(r"^\|[\s\-:]+\|", lines[i-1].strip()) else "td"
            row_html = "<tr>" + "".join(
                f'<{tag} style="border:1px solid #ddd;padding:8px;text-align:left;">{_format_inline(c)}</{tag}>'
                for c in cells
            ) + "</tr>"
            html_lines.append(row_html)
            i += 1
            continue
        elif in_table:
            html_lines.append("</table>")
            in_table = False

        # Blockquotes
        if stripped.startswith("> "):
            html_lines.append(f'<blockquote style="border-left:4px solid #ccc;margin:8px 0;padding-left:12px;color:#666;">{_format_inline(stripped[2:])}</blockquote>')
            i += 1
            continue

        # Blank lines
        if not stripped:
            html_lines.append("<br>")
            i += 1
            continue

        # Normal paragraph
        html_lines.append(f"<p>{_format_inline(stripped)}</p>")
        i += 1

    if in_table:
        html_lines.append("</table>")
    if in_code_block:
        html_lines.append("</code></pre>")

    return "\n".join(html_lines)


def _format_inline(text: str) -> str:
    """Format inline markdown: bold, italic, inline code, links, emoji."""
    # Bold: **text**
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Italic: *text*
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    # Inline code: `text`
    text = re.sub(r"`([^`]+)`", r'<code style="background:#f4f4f4;padding:1px 4px;border-radius:3px;">\1</code>', text)
    # Links: [text](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text


def build_email_html(response_md: str, source_file: str) -> str:
    """Build a complete HTML email from the markdown response."""
    body_html = md_to_html(response_md)

    # Get source timestamp from filename
    filename = os.path.basename(source_file)
    timestamp = filename.replace(".md", "").replace("_", " ")

    return f"""\
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body style="font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;max-width:720px;margin:0 auto;padding:20px;color:#333;line-height:1.6;">
<div style="background:#f0f0f0;padding:12px 16px;border-radius:8px;margin-bottom:20px;font-size:13px;color:#666;">
  📊 <strong>AI Topics Report</strong> — {timestamp} UTC<br>
  <span style="font-size:12px;">Generated by Hermes Agent · via Cloudflare Email Sending</span>
</div>
{body_html}
<hr style="margin-top:24px;border:none;border-top:1px solid #eee;">
<div style="font-size:11px;color:#999;margin-top:12px;">
  This is an automated report from <a href="https://github.com/kzinmr/ai-topics">github.com/kzinmr/ai-topics</a>.
  Sent via Cloudflare Email Service.
</div>
</body>
</html>"""


# ── Main ──────────────────────────────────────────────────────────────────


def main():
    # Find latest Slack output
    latest_file = find_latest_slack_output()
    if not latest_file:
        print("No Slack output files found — nothing to relay.", file=sys.stderr)
        sys.exit(0)  # Silent exit — cron delivery suppressed

    # Check file is fresh (within last 6 hours)
    mtime = os.path.getmtime(latest_file)
    age_seconds = datetime.now().timestamp() - mtime
    if age_seconds > 6 * 3600:
        print(f"Latest output is {age_seconds/3600:.1f}h old — skipping (stale).", file=sys.stderr)
        sys.exit(0)

    # Extract response
    response = extract_response_from_md(latest_file)
    if not response:
        print("Could not extract response from Slack output.", file=sys.stderr)
        sys.exit(1)

    # Get date for subject
    date_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M")

    # Build email
    html = build_email_html(response, latest_file)

    # Send
    success = send_email_via_cloudflare(
        subject=f"AI Topics Hot Posts — {date_str} UTC",
        html=html,
    )

    if success:
        print(f"Email relay sent successfully ({os.path.basename(latest_file)})")
    else:
        print("Email relay failed — check logs.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
