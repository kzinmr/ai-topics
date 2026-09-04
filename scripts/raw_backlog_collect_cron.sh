#!/bin/sh
# Wrapper for raw_backlog_collect.py - used by raw-backlog-ingest.
# Defaults match the old cron behavior, but manual runs can override via env.
set -eu

profile_root="${HERMES_PROFILE_ROOT:-${HERMES_SUBPROCESS_HOME:-$HOME}}"
cd "$profile_root/ai-topics"

count="${RAW_BACKLOG_COUNT:-5}"
sort_mode="${RAW_BACKLOG_SORT:-ai-hint}"
min_size="${RAW_BACKLOG_MIN_SIZE:-500}"

if [ "${RAW_BACKLOG_DRY_RUN:-0}" = "1" ] && [ "${RAW_BACKLOG_ESTIMATE:-0}" = "1" ]; then
  exec python3 scripts/raw_backlog_collect.py --count "$count" --sort "$sort_mode" --min-size "$min_size" --dry-run --estimate
elif [ "${RAW_BACKLOG_DRY_RUN:-0}" = "1" ]; then
  exec python3 scripts/raw_backlog_collect.py --count "$count" --sort "$sort_mode" --min-size "$min_size" --dry-run
elif [ "${RAW_BACKLOG_ESTIMATE:-0}" = "1" ]; then
  exec python3 scripts/raw_backlog_collect.py --count "$count" --sort "$sort_mode" --min-size "$min_size" --estimate
else
  exec python3 scripts/raw_backlog_collect.py --count "$count" --sort "$sort_mode" --min-size "$min_size"
fi
