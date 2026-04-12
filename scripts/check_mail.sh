#!/bin/bash
# Quick mail checker — list or read emails from Maildir
# Usage:
#   check_mail.sh              # List new emails (summary)
#   check_mail.sh read <file>  # Read a specific email
#   check_mail.sh process      # Run full processing pipeline

MAILDIR_NEW="$HOME/Maildir/new"
MAILDIR_CUR="$HOME/Maildir/cur"
PYTHON="$HOME/.hermes/hermes-agent/venv/bin/python"

case "${1:-list}" in
  list)
    new_count=$(ls "$MAILDIR_NEW" 2>/dev/null | wc -l)
    cur_count=$(ls "$MAILDIR_CUR" 2>/dev/null | wc -l)
    proc_count=$(ls "$HOME/Maildir/processed" 2>/dev/null | wc -l)
    echo "New: $new_count | Unprocessed: $cur_count | Processed (wiki済): $proc_count"
    if [ "$new_count" -gt 0 ]; then
      echo "--- New ---"
      for f in "$MAILDIR_NEW"/*; do
        [ -f "$f" ] || continue
        from=$($PYTHON -c "import email,email.policy,sys; m=email.message_from_bytes(open('$f','rb').read(),policy=email.policy.default); print(m['From'],'|',m['Subject'])" 2>/dev/null)
        echo "  $(basename $f): $from"
      done
    fi
    ;;
  read)
    if [ -z "$2" ]; then
      echo "Usage: check_mail.sh read <filename>"
      exit 1
    fi
    filepath="$MAILDIR_NEW/$2"
    [ -f "$filepath" ] || filepath="$MAILDIR_CUR/$2"
    [ -f "$filepath" ] || { echo "Not found: $2"; exit 1; }
    $PYTHON -c "
import email, email.policy, sys
msg = email.message_from_bytes(open('$filepath','rb').read(), policy=email.policy.default)
print('From:', msg['From'])
print('Subject:', msg['Subject'])
print('Date:', msg['Date'])
print('---')
body = msg.get_body(preferencelist=('plain','html'))
if body:
    print(body.get_content()[:3000])
"
    ;;
  process)
    $PYTHON $HOME/scripts/process_email.py
    ;;
  *)
    echo "Usage: check_mail.sh [list|read <file>|process]"
    ;;
esac
