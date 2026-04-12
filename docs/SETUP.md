# Hermes AI Topic Manager — Setup Guide

## ✅ What's Already Done

| Component | Status | Details |
|-----------|--------|---------|
| Hermes Agent v0.8.0 | ✅ Installed | `~/.hermes/hermes-agent/` |
| LLM-Wiki skill | ✅ Configured | `wiki.path: ~/wiki` |
| Wiki structure | ✅ Created | `~/wiki/` with SCHEMA, index, log |
| Wiki web browser | ✅ Running | Port 8000 (systemd: `wiki-server`) |
| Email watcher | ✅ Running | systemd: `email-watcher` |
| Email processor | ✅ Installed | `~/scripts/process_email.py` |
| ai-topics repo | ✅ Cloned | `~/ai-topics/` (hermes/ folder ready) |
| SOUL.md | ✅ Configured | AI Topics knowledge agent personality |
| Node.js + Playwright | ✅ Installed | Browser tools available |

## ⚠️ Remaining Manual Steps (require your credentials)

### Step 1: Enable Email Receiving

Run from your **local machine** (not this VM):
```bash
ssh exe.dev share receive-email hermes-topic-manager on
```

Then subscribe newsletters to addresses like:
- `newsletters@hermes-topic-manager.exe.xyz`
- `ai-news@hermes-topic-manager.exe.xyz`
- Any `*@hermes-topic-manager.exe.xyz` works (wildcard)

### Step 2: Configure LLM Provider

Edit `~/.hermes/.env` and set ONE of:
```bash
# Option A: OpenRouter (recommended - access to 200+ models)
OPENROUTER_API_KEY=sk-or-...

# Option B: Anthropic direct
ANTHROPIC_API_KEY=sk-ant-...

# Option C: Google AI Studio (free tier available)
GOOGLE_API_KEY=...
```

Then set the default model in `~/.hermes/config.yaml`:
```yaml
model:
  default: "anthropic/claude-sonnet-4-20250514"  # or your preferred model
```

### Step 3: Set Up Discord Bot

1. Go to https://discord.com/developers/applications
2. **New Application** → name it "Hermes"
3. **Bot** tab → Reset Token → copy the token
4. Enable **Privileged Gateway Intents**:
   - ✅ Message Content Intent
   - ✅ Server Members Intent
5. **OAuth2** → URL Generator:
   - Scopes: `bot`, `applications.commands`
   - Permissions: Send Messages, Read Message History, Attach Files, Embed Links, Add Reactions
   - Permission integer: `274878286912`
6. Copy the generated URL and open it to invite the bot to your server
7. Get your Discord User ID (Developer Mode → right-click your name → Copy User ID)

Edit `~/.hermes/.env`:
```bash
DISCORD_BOT_TOKEN=your-bot-token-here
DISCORD_ALLOWED_USERS=your-discord-user-id
DISCORD_HOME_CHANNEL=channel-id-for-notifications  # optional
```

### Step 4: Start Hermes Gateway

After configuring .env:
```bash
# Install as systemd service
sudo cp ~/scripts/hermes-gateway.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now hermes-gateway

# Check status
sudo systemctl status hermes-gateway
journalctl -u hermes-gateway -f
```

### Step 5 (Optional): Web Search API

For better scraping when Hermes processes wiki pages:
```bash
# In ~/.hermes/.env
EXA_API_KEY=...          # https://exa.ai
# or
FIRECRAWL_API_KEY=...    # https://firecrawl.dev
```

## Architecture Overview

```
┌────────────────────────────────────────────────────────────┐
│                    hermes-topic-manager VM                     │
│                                                              │
│  ┌─────────────────┐   ┌────────────────┐   ┌──────────────┐ │
│  │  Newsletters  │   │  Email Watcher │   │ ~/wiki/raw/  │ │
│  │  (email in)   │──▶│  + Scraper     │──▶│  articles/   │ │
│  │  ~/Maildir/   │   │  (systemd)    │   │              │ │
│  └─────────────────┘   └────────────────┘   └─────┬────────┘ │
│                                                    │          │
│  ┌─────────────────┐   ┌────────────────┐   ┌─────┴────────┐ │
│  │  Discord Bot  │   │ Hermes Agent  │   │  ~/wiki/     │ │
│  │  (you chat)   │◀─▶│ (LLM-Wiki)   │◀─▶│  entities/   │ │
│  │              │   │ (systemd)    │   │  concepts/   │ │
│  └─────────────────┘   └────────────────┘   └─────┬────────┘ │
│                                                    │          │
│  ┌─────────────────┐   ┌────────────────┐   ┌─────┴────────┐ │
│  │  Wiki Server  │   │  Obsidian /   │   │ ai-topics    │ │
│  │  :8000       │   │  Browser     │   │ GitHub repo  │ │
│  │  (systemd)   │   │  (remote)    │   │ hermes/      │ │
│  └─────────────────┘   └────────────────┘   └──────────────┘ │
└────────────────────────────────────────────────────────────┘
```

## Key Paths

| Path | Purpose |
|------|---------|
| `~/.hermes/.env` | API keys, Discord token |
| `~/.hermes/config.yaml` | Hermes configuration |
| `~/.hermes/SOUL.md` | Agent personality |
| `~/wiki/` | LLM Wiki knowledge base |
| `~/wiki/SCHEMA.md` | Wiki conventions |
| `~/wiki/raw/articles/` | Auto-ingested newsletter articles |
| `~/ai-topics/hermes/` | Newsletter digests (pushed to GitHub) |
| `~/Maildir/new/` | Incoming emails |
| `~/scripts/` | Automation scripts |
| `~/logs/` | Logs |

## Service Management

```bash
# Wiki browser
sudo systemctl status wiki-server
sudo systemctl restart wiki-server
journalctl -u wiki-server -f

# Email watcher  
sudo systemctl status email-watcher
sudo systemctl restart email-watcher
journalctl -u email-watcher -f

# Hermes gateway (after configuring .env)
sudo systemctl status hermes-gateway
sudo systemctl restart hermes-gateway
journalctl -u hermes-gateway -f
```

## URLs

- **Wiki Browser:** https://hermes-topic-manager.exe.xyz:8000/
- **Wiki SCHEMA:** https://hermes-topic-manager.exe.xyz:8000/SCHEMA.md
- **Raw Articles:** https://hermes-topic-manager.exe.xyz:8000/raw/articles/

## Using Hermes via Discord

Once the gateway is running, you can:
- `@Hermes process the latest raw articles into wiki pages`
- `@Hermes what are the top AI trends this week?`
- `@Hermes lint the wiki`
- `@Hermes create an entity page for OpenAI`
- `@Hermes compare RAG vs LLM Wiki approaches`

## Obsidian Setup

To browse the wiki in Obsidian:
1. Install [Obsidian Git](https://github.com/denolehov/obsidian-git) plugin
2. Clone/sync `~/wiki/` to your local machine
3. Open it as an Obsidian vault
4. Wikilinks, frontmatter, and graph view work out of the box

Alternatively, use the web browser at port 8000.

## X/Twitter Account Entity Pipeline

### Architecture
1. **Input**: `~/x-accounts.yaml` — YAML list of X accounts with optional blog/RSS/topics
2. **Skeleton Generation**: `~/scripts/build_x_wiki.py` — scrapes blogs, discovers RSS, generates entity skeleton pages
3. **Enrichment**: Hermes Agent via Discord — researches each person and fills in Core Ideas, Related, etc.

### Usage Flow
```bash
# 1. Edit x-accounts.yaml to add new accounts
# 2. Generate skeletons
~/.hermes/hermes-agent/venv/bin/python ~/scripts/build_x_wiki.py

# 3. Commit skeletons
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: add X account skeletons" && git push

# 4. Ask Hermes to enrich (via Discord)
#    The script prints a ready-to-use Discord prompt after running
~/.hermes/hermes-agent/venv/bin/python ~/scripts/build_x_wiki.py --enrich

# 5. For single account
~/.hermes/hermes-agent/venv/bin/python ~/scripts/build_x_wiki.py --handle @username
```

### X API Not Required
No X/Twitter API credentials needed. Blog/RSS info is scraped directly.
X profile research is delegated to Hermes Agent's web search during enrichment.
