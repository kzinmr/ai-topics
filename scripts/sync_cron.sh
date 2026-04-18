#!/usr/bin/env bash
# Sync Hermes cron jobs between ~/.hermes/cron/jobs.json and repo.
# Usage: sync_cron.sh pull   — copy Hermes → repo (before git commit)
#        sync_cron.sh push   — copy repo   → Hermes (after git checkout/pull)

set -euo pipefail

HERMES_JOBS="$HOME/.hermes/cron/jobs.json"
REPO_JOBS="$(cd "$(dirname "$0")/.." && pwd)/config/hermes/cron/jobs.json"

case "${1:-}" in
  pull)
    cp "$HERMES_JOBS" "$REPO_JOBS"
    echo "Pulled: ~/.hermes/cron/jobs.json → config/hermes/cron/jobs.json"
    ;;
  push)
    cp "$REPO_JOBS" "$HERMES_JOBS"
    echo "Pushed: config/hermes/cron/jobs.json → ~/.hermes/cron/jobs.json"
    ;;
  *)
    echo "Usage: $0 {pull|push}" >&2
    exit 1
    ;;
esac
