# HERMES_HOME Symlink Structure (Cron-Mode Pitfall)

## The Symlink Chain

```
/opt/data/.hermes/                    ← HERMES_HOME (canonical)
/opt/data/.hermes/home/.hermes/       ← symlink to ".." (resolves to /opt/data/.hermes)
```

Both paths resolve to the **same directory**. This means:
- `ls /opt/data/.hermes/cron/data/...` and `ls /opt/data/.hermes/home/.hermes/cron/data/...` show the same files
- `os.environ.get('HERMES_HOME')` returns `/opt/data/.hermes` — this is correct
- `os.path.expanduser("~/.hermes")` in cron terminal context may return `/opt/data/.hermes/home/.hermes` — this ALSO works because the symlink resolves

## Debugging Triage Path Issues

When verifying triage JSON exists:

```bash
# Both of these should show the same file:
ls -la /opt/data/.hermes/cron/data/dreaming/triage_latest.json
ls -la /opt/data/.hermes/home/.hermes/cron/data/dreaming/triage_latest.json

# Check symlink:
readlink -f /opt/data/.hermes/home/.hermes
# Should output: /opt/data/.hermes
```

## In Python Scripts

For cron-mode scripts written to `/tmp/` and executed via `terminal`:

```python
# CORRECT: use env var
hermes_home = os.environ.get('HERMES_HOME', '/opt/data/.hermes')

# ALSO WORKS (but less clear): expanduser resolves through symlink
hermes_home = os.path.expanduser('~/.hermes')

# Both produce valid paths because the symlink chain is intact
```

The pitfall described in the main skill (`expanduser` resolving to nested path) is **mitigated by the symlink** — the nested path still points to the correct directory. The real risk is if the symlink is broken or removed.
