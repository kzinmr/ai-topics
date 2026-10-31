#!/usr/bin/env bash
# Batch wikilink target verifier — post-write gate for dreaming / wiki-ingest.
# Usage: cd ~/ai-topics/wiki && bash <this-script> concepts/foo entities/bar ...
# Page paths are relative to wiki/ (no leading 'wiki/', no '.md').
#
# Why bash [ -f ] and not `find -e`: `find wiki -e "wiki/$t.md"` does NOT test
# existence (-e is parsed as a predicate) — every link reports MISSING.
# Why grep -o "\[\[[^]|]*": strips both the [[ and any |alias in one pass.
#
# See README-wikilink-check.md in this scripts/ dir for ghost->real retarget table.
set -uo pipefail

if [ "$#" -eq 0 ]; then
  echo "usage: cd <wiki-dir> && bash $0 <page/path> [<page/path> ...]   (relative to wiki/, no .md)" >&2
  exit 2
fi

missing=0
for page in "$@"; do
  f="$page.md"
  if [ ! -f "$f" ]; then
    echo "SKIP (page not found): $page"
    continue
  fi
  # Extract [[target]] and [[target|alias]] targets, dedup.
  while IFS= read -r t; do
    [ -z "$t" ] && continue
    case "$t" in
      http://*|https://*|\#*) continue ;;   # skip non-wikilink captures
    esac
    if [ -f "$t.md" ] || [ -f "$t/_index.md" ]; then
      echo "OK      [$page] $t"
    else
      echo "MISSING [$page] $t   -> sweep: find concepts entities -iname '*$(basename "$t")*'"
      missing=$((missing+1))
    fi
  done < <(grep -o "\[\[[^]|]*" "$f" | sed 's/.*\[\[//' | sort -u)
done

echo "-----"
if [ "$missing" -eq 0 ]; then
  echo "ALL WIKILINKS OK"
else
  echo "$missing MISSING wikilink target(s). Do NOT create stubs to satisfy them — retarget to a real page (see README-wikilink-check.md)."
fi
exit $([ "$missing" -eq 0 ] && echo 0 || echo 1)
