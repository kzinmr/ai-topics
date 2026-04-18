#!/usr/bin/env bash
# Install versioned git hooks from .githooks/ into .git/hooks/ as symlinks.
# Run once per clone.
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
SRC_DIR="$REPO_ROOT/.githooks"
DST_DIR="$REPO_ROOT/.git/hooks"

if [ ! -d "$SRC_DIR" ]; then
  echo "error: $SRC_DIR not found" >&2
  exit 1
fi

mkdir -p "$DST_DIR"
count=0
for hook in "$SRC_DIR"/*; do
  [ -e "$hook" ] || continue
  name="$(basename "$hook")"
  ln -sfn "../../.githooks/$name" "$DST_DIR/$name"
  chmod +x "$hook"
  echo "  $name"
  count=$((count + 1))
done
echo "Installed $count hook(s) from .githooks/ → .git/hooks/"
