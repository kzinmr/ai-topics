# xurl Config Migration — Token Merge

Merge OAuth2 tokens from an old xurl config file into the current active one.

## When This Happens
- Hermes stores config at `~/.hermes/home/.xurl` while old config at `/opt/data/.xurl`
- `xurl auth status` shows "oauth2: (none)" even though tokens exist

## Diagnostic
```bash
find ~ -name ".xurl" 2>/dev/null
xurl auth status
```

## Fix: Merge Tokens
```python
import yaml
with open(old_config) as f: old = yaml.safe_load(f)
with open(current_config) as f: current = yaml.safe_load(f)
# Merge oauth2_tokens, client_id, client_secret from old into current
with open(current_config, 'w') as f:
    yaml.dump(current, f, default_flow_style=False)
```

## Verify
```bash
xurl auth status
xurl --auth oauth2 --app lucy --username kzinmr /2/users/me
```

## Important
- Never print token values to LLM context
- Run `xurl auth status` after merging to confirm
