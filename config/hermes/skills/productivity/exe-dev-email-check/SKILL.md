---
name: exe-dev-email-check
description: Check and process emails on exe.dev VM using Maildir filesystem. Use this when user asks to check emails or when newsletters arrive.
category: productivity
version: 2.0.0
author: hermes
license: MIT
metadata:
  hermes:
    tags: [Email, Maildir, exe.dev, Newsletter, Automation]
---

# exe.dev Email Check Workflow

This VM uses exe.dev's Maildir-based email system. There is NO IMAP/SMTP server. Do NOT use himalaya, mutt, or any mail client.

## Key Facts
- Email address: `anything@hermes-topic-manager.exe.xyz` (wildcard)
- New emails arrive in `~/Maildir/new/`
- Emails moved to `~/Maildir/cur/` after initial read
- Fully processed emails moved to `~/Maildir/processed/`
- `email-watcher` service auto-processes newsletters on arrival
- Processed email IDs tracked in `~/.hermes/processed_emails.json`
- Pre-built scripts: `~/.hermes/scripts/check_mail.sh`, `~/.hermes/scripts/process_email.py`

## Email Flow
```
Gmail → Maildir/new/ → email-watcher runs → scrape links → save to wiki/raw/articles/ → move to Maildir/processed/
```

## Steps to Check for New Emails

### 1. Quick status check
```bash
~/.hermes/scripts/check_mail.sh list
```
Shows: New count, Unprocessed (cur/) count, Processed count

### 2. Check for unprocessed emails (all directories)
```bash
ls -lt ~/Maildir/new/ ~/Maildir/cur/ ~/Maildir/processed/ 2>&1
```
- If `new/` has files: fresh emails, not yet seen
- If `cur/` has files but `new/` is empty: emails were seen but may not be processed
- If `processed/` has files: emails were handled by email-watcher (may need verification)

### 3. Read email content (manual)
```bash
~/.hermes/scripts/check_mail.sh read <filename>
```
Works for files in all directories

### 4. Process unprocessed emails
```bash
~/.hermes/scripts/check_mail.sh process
```
This runs `process_email.py` which checks `new/`, `cur/`, AND `processed/` directories.

### 5. Verify processing results
```bash
ls -lt ~/wiki/raw/articles/ 2>&1 | head -10
cat ~/.hermes/processed_emails.json | python3 -m json.tool | head -20
```

## Important: Email-Watcher Behavior

**The `email-watcher` service** auto-runs `process_email.py` on new mail arrival:
- Scrapes article links from newsletters
- Saves content to `~/wiki/raw/articles/`
- Moves emails to `~/Maildir/processed/`
- Updates `~/.hermes/processed_emails.json`

**However, scraping can fail silently** (403 errors, network disconnects). When this happens:
- Emails are moved to `processed/` but IDs are NOT saved to DB
- Content is NOT saved to `wiki/raw/articles/`
- User must manually re-run the script

## Handling Backlogged Emails

When many emails have accumulated (e.g., 20+):

### 1. Identify unprocessed emails
```python
import json, email, os
from pathlib import Path

processed_dir = Path.home() / "Maildir" / "processed"
db_path = Path.home() / ".hermes" / "processed_emails.json"

# Load DB
with open(db_path) as f:
    data = json.load(f)
processed_ids = set(data.get("message_ids", []))

# Find emails in processed/ but NOT in DB
for f in sorted(processed_dir.glob("*.eml")):
    if f.stem not in processed_ids:
        print(f"Unprocessed: {f.name}")
```

### 2. Bulk scrape with web_extract
```python
# Extract URLs from unprocessed emails, then:
web_extract(urls=[url1, url2, url3, url4, url5])  # max 5 per call
```

### 3. Create wiki pages from raw articles
Read saved articles from `~/wiki/raw/articles/` and create structured wiki pages in `~/wiki/entities/` or `~/wiki/concepts/`.

## Substack Content Handling

**Email-watcher already saves Substack articles** to `~/wiki/raw/articles/` as markdown transcripts:
- Files named `substack.com--app-link-post--*.md` or `substack.com--redirect-*.md`
- Contain full article content with timestamps
- Can be read directly with `read_file` — no need to re-scrape
- Use these as source material for wiki page creation

## Troubleshooting

### Scraping failed silently
Check logs: `tail -50 ~/logs/email_processor.log`
Look for 403 errors, connection timeouts, or network resets.

### "No new emails" but files exist in directories
Run script directly:
```bash
cd ~/.hermes/scripts && source venv/bin/activate && python3 process_email.py
```

### Dependencies missing
```bash
cd ~/.hermes/scripts && python3 -m venv venv && source venv/bin/activate && pip install httpx beautifulsoup4 readability-lxml
```

### Processed database corruption
```bash
rm ~/.hermes/processed_emails.json
```
This will cause all emails to be reprocessed.

### Network errors during scraping
- Use `web_extract` tool for individual URLs
- Batch process with multiple `web_extract` calls
- Substack articles already saved in `raw/articles/` — read those directly

## Gmail Forwarding Setup
If user forwards from Gmail, they must first confirm forwarding via the link in the Gmail Forwarding Confirmation email. Until confirmed, emails won't arrive.

## Wiki Maintenance After Processing

### Rebuilding index.md
After creating wiki pages, rebuild `wiki/index.md` with this Python pattern:
```python
from pathlib import Path
import re

wiki_dir = Path.home() / "wiki"
entities = sorted((wiki_dir / "entities").glob("*.md"))
concepts = sorted((wiki_dir / "concepts").glob("*.md"))
comparisons = sorted((wiki_dir / "comparisons").glob("*.md"))
raw_articles = sorted((wiki_dir / "raw" / "articles").glob("*.md"), 
                      key=lambda f: f.stat().st_mtime, reverse=True)

def get_metadata(filepath):
    with open(filepath) as f:
        content = f.read(500)
    title_match = re.search(r'title:\s*"([^"]+)"', content)
    return title_match.group(1) if title_match else filepath.stem

# Build index content programmatically, then write to wiki/index.md
```

### Updating log.md
Append dated entries to `wiki/log.md` with format:
```markdown
## YYYY-MM-DD
- **Summary:** what was processed
- **Pages created:** count and names
- **Updated:** files modified
- **Sources:** raw articles used
```

### Git Commit & Push
Always commit and push after wiki changes:
```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: <summary>" && git push
```

## Pitfalls
- Do NOT use himalaya, mutt, or IMAP/SMTP clients
- File paths in Python need `os.path.expanduser()` for `~`
- Large emails (newsletters) may be 100KB+
- email-watcher runs automatically, so `new/` may be empty even if mail was received
- **Scraping failures are silent** — always verify content was saved to `wiki/raw/articles/`
- **Check `processed/` directory** — emails may be there but never scraped
- **Substack articles are pre-saved** — don't re-scrape, just read from `raw/articles/`
- **Always rebuild index.md** after creating pages — it doesn't auto-update
- **Git push is required** — wiki changes aren't visible until pushed to github.com/kzinmr/ai-topics
