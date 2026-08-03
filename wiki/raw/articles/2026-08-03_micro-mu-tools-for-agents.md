# Mu - Tools for Agents

- **Source**: https://github.com/micro/mu
- **Published**: August 3, 2026 (Show HN)
- **Author**: Asim (micro/mu)
- **HN Discussion**: https://news.ycombinator.com/item?id=49148899 (Show HN, 50 pts)
- **License**: AGPL-3.0

## Overview

Mu is an MCP server and web app that provides agents and humans access to the real world through MCP. It offers tools for news, web search, mail, markets, weather, video, places, images, files, calendar, contacts, and more. Available live at micro.mu or self-hosted.

## Tool Categories

| Area | Tools |
|---|---|
| Agent | agent, chat — ask the whole thing a question |
| Apps | apps_build, apps_run, apps_edit — build/run small web tools |
| Calendar | events_create, events_free, events_list |
| Contacts | contacts_find, contacts_add, contacts_list |
| Files | files_put, files_get, files_list, files_share |
| Faith | islam_today, islam_prayer, islam_qibla, quran, hadith |
| Index | index_search — everything this instance holds |
| Images | images_generate, images_search |
| Mail | mail_inbox, mail_send, mail_address — real SMTP with DKIM |
| Markets | markets_list — crypto, futures, commodities, currencies |
| News | news_list, news_read, news_search — RSS aggregation |
| Places | places_search, places_nearby, places_eta |
| Storage | db_create, db_get, db_list, db_update, db_delete |
| Writing | blog_*, social_*, stream_* |
| Wallet | wallet_balance |
| Weather | weather_forecast |
| Web | web_search, web_fetch |
| Video | video_list, video_search |

## Architecture

Single Go binary that runs both the server (mu --serve) and CLI. Every tool is a mu subcommand. The CLI is registry-driven — tools added to the server automatically become CLI commands. LLM backend supports Claude, Atlas Cloud (DeepSeek), or local Ollama/OpenAI-compatible endpoints. Includes Discord and Telegram bot integration.

## HN Discussion Highlights

- Contributors: "one human and four agents"
- Skepticism about MCP server usefulness in general
- Interest in the "Faith" tool category
- Discussion of value proposition and AI-written marketing copy
