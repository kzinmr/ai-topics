---
title: "Notion CLI (ntn) — Official Developer Docs Overview"
source: https://developers.notion.com/cli/get-started/overview
date: 2026-05-13
scraped: 2026-05-14
type: raw_article
tags: [notion, cli, developer-tools, api, workers]
---

# Notion CLI (ntn)

`ntn` is the official Notion CLI. Use it to authenticate with Notion, deploy and manage Notion Workers, and make API requests — all from your terminal.

Installed via: `curl -fsSL https://ntn.dev | bash`

## Core Commands

### Authentication
```bash
ntn login
```
Opens a browser for OAuth authorization. Credentials stored in system keychain.

### Notion Workers
Create, deploy, and operate Workers — small TypeScript programs that extend Notion with syncs, tools, and webhooks:
```bash
ntn workers new           # Scaffold a project
ntn workers deploy        # Build and upload
ntn workers list          # List deployed workers
```

### API Requests
Inline JSON construction with shell completion:
```bash
ntn api v1/users                              # GET users
ntn api v1/pages parent[page_id]=abc123       # POST with inline body fields
ntn api v1/pages/abc123 -X PATCH archived:=true   # PATCH with typed assignment
```

### File Uploads
```bash
ntn files create < photo.png
ntn files create --external-url https://example.com/photo.png
ntn files list
```

## Key Features
- Free on all plans (Workers require Business/Enterprise)
- Designed for developers and AI coding assistants
- Darwin (arm64, x86_64) and Linux (x86_64, arm64) support via musl binaries
- Shell completions available
- Full docs at https://developers.notion.com/guides/get-started/overview
