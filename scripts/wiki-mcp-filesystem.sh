#!/bin/bash
# Publish the ai-topics wiki as a READ-ONLY local MCP server using the
# official Filesystem MCP server (modelcontextprotocol/servers) inside Docker.
#
#   - Read-only is enforced at the filesystem level via a Docker `ro` bind mount,
#     so query agents can read/list/search the wiki but never modify it.
#   - See docs/wiki-mcp.md for the full design, tool reference, and how a
#     consuming agent should navigate the wiki (SCHEMA.md -> index.md -> pages).
#
# Usage:
#   scripts/wiki-mcp-filesystem.sh pull      # pull the mcp/filesystem image
#   scripts/wiki-mcp-filesystem.sh smoke     # MCP handshake + read/write checks
#   scripts/wiki-mcp-filesystem.sh config    # print the Claude Code mcpServers JSON
#   scripts/wiki-mcp-filesystem.sh           # pull + smoke + config (default)
set -euo pipefail

IMAGE="mcp/filesystem"
# Resolve the wiki path from this script's location so the config is portable.
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WIKI_DIR="$REPO_ROOT/wiki"
SERVER_NAME="ai-topics-wiki"

docker_run_args=(run -i --rm
  --mount "type=bind,src=$WIKI_DIR,dst=/wiki,ro"
  "$IMAGE" /wiki)

pull() {
  echo "==> docker pull $IMAGE"
  if ! docker pull "$IMAGE"; then
    cat <<EOF
Pull failed. Build it from source instead:
  git clone https://github.com/modelcontextprotocol/servers
  docker build -t $IMAGE servers/src/filesystem
EOF
    return 1
  fi
}

smoke() {
  echo "==> Smoke test against $WIKI_DIR (read-only)"
  printf '%s\n' \
    '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"smoke","version":"0"}}}' \
    '{"jsonrpc":"2.0","method":"notifications/initialized"}' \
    '{"jsonrpc":"2.0","id":2,"method":"tools/list"}' \
    '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"list_directory","arguments":{"path":"/wiki"}}}' \
    '{"jsonrpc":"2.0","id":4,"method":"tools/call","params":{"name":"read_file","arguments":{"path":"/wiki/index.md"}}}' \
    '{"jsonrpc":"2.0","id":5,"method":"tools/call","params":{"name":"write_file","arguments":{"path":"/wiki/__write_probe.md","content":"x"}}}' \
    | docker "${docker_run_args[@]}" 2>/dev/null \
    | python3 -c '
import sys, json
ok = {"init": False, "tools": False, "list": False, "read": False, "ro": False}
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    try: m = json.loads(line)
    except Exception: continue
    i = m.get("id")
    if i == 1:
        ok["init"] = True
        print("  init      :", m["result"]["serverInfo"])
    elif i == 2:
        ok["tools"] = True
        print("  tools     :", [t["name"] for t in m["result"]["tools"]])
    elif i == 3:
        ok["list"] = True
        dirs = [l for l in m["result"]["content"][0]["text"].splitlines() if "[DIR]" in l]
        print("  list /wiki:", " ".join(d.replace("[DIR] ", "") for d in dirs))
    elif i == 4:
        c = m["result"]["content"][0]["text"]
        ok["read"] = bool(c)
        print("  read      : index.md ->", c.splitlines()[0] if c else "(empty)")
    elif i == 5:
        r = m.get("result", {})
        ok["ro"] = bool(r.get("isError"))
        print("  read-only : write rejected ->", r.get("content",[{}])[0].get("text","")[:60])
import sys as _s
if all(ok.values()):
    print("  RESULT    : PASS")
else:
    print("  RESULT    : FAIL", ok); _s.exit(1)
'
}

config() {
  cat <<EOF

Register with Claude Code (user-level ~/.claude/settings.json or a project .mcp.json):

{
  "mcpServers": {
    "$SERVER_NAME": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "--mount", "type=bind,src=$WIKI_DIR,dst=/wiki,ro",
        "$IMAGE", "/wiki"
      ]
    }
  }
}

Or via the CLI:
  claude mcp add $SERVER_NAME -- docker run -i --rm --mount type=bind,src=$WIKI_DIR,dst=/wiki,ro $IMAGE /wiki
EOF
}

case "${1:-all}" in
  pull)   pull ;;
  smoke)  smoke ;;
  config) config ;;
  all)    pull && smoke && config ;;
  *)      echo "usage: $0 {pull|smoke|config|all}" >&2; exit 2 ;;
esac
