#!/bin/bash
# Watch Maildir/new/ for incoming emails and process them
set -euo pipefail

MAILDIR_NEW="$HOME/Maildir/new"
PYTHON="$HOME/.hermes/hermes-agent/venv/bin/python"
SCRIPT="$HOME/scripts/process_email.py"

mkdir -p "$MAILDIR_NEW"

echo "[$(date)] Email watcher started. Watching $MAILDIR_NEW"

# Process any existing emails first
$PYTHON $SCRIPT

# Watch for new files
inotifywait -m -e create -e moved_to "$MAILDIR_NEW" --format '%f' | while read -r filename; do
    echo "[$(date)] New email detected: $filename"
    # Small delay to ensure file is fully written
    sleep 2
    $PYTHON $SCRIPT
done
