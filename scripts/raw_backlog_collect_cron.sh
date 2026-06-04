#!/bin/bash
# Wrapper for raw_backlog_collect.py - used by raw-backlog-ingest cron job.
# Passes --sort ai-hint to prioritize AI-relevant articles.
profile_root="${HERMES_PROFILE_ROOT:-${HERMES_SUBPROCESS_HOME:-$HOME}}"
cd "$profile_root/ai-topics"
exec python3 scripts/raw_backlog_collect.py --count 5 --sort ai-hint --min-size 500
