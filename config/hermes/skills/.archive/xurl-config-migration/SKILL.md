---
name: xurl-config-migration
description: Merge OAuth2 tokens from an old xurl config file into the current active xurl config when config files are stored in different locations (common in Hermes agent environments).
version: 1.0.0
author: Hermes Agent
license: MIT
---

# xurl Config Migration — Token Merge

When xurl OAuth2 tokens exist in one `.xurl` config file but the active config is at a different path, commands fail with auth errors even though the tokens are technically saved.

## When This Happens

- Hermes environment stores config at `~/.hermes/home/.xurl` while an old config exists at `/opt/data/.xurl`
- After migrating environments, config files get split across locations
- `xurl auth status` shows `oauth2: (none)` for the default app even though tokens exist in a config file

## Diagnostic

```bash
# Check active config location
find ~ -name ".xurl" 2>/dev/null

# Check what xurl sees
xurl auth status
```

If you find multiple `.xurl` files, the one xurl actually uses is the one in your current home directory (usually `~/.hermes/home/.xurl` in Hermes environments).

## Fix: Merge Tokens

Read the old config (with tokens) and the current config, then merge the OAuth2 tokens into the current config.

```python
import yaml

old_config = "/opt/data/.xurl"       # config WITH tokens
current_config = "/opt/data/.hermes/home/.xurl"  # current active config

with open(old_config) as f:
    old = yaml.safe_load(f)

with open(current_config) as f:
    current = yaml.safe_load(f)

# Merge OAuth2 tokens from old into current
if 'apps' in old:
    for app_name, app_data in old['apps'].items():
        if app_name not in current.get('apps', {}):
            current['apps'][app_name] = {}
        if 'oauth2_tokens' in app_data:
            current['apps'][app_name]['oauth2_tokens'] = app_data['oauth2_tokens']
        if 'client_id' in app_data:
            current['apps'][app_name]['client_id'] = app_data['client_id']
        if 'client_secret' in app_data:
            current['apps'][app_name]['client_secret'] = app_data['client_secret']

with open(current_config, 'w') as f:
    yaml.dump(current, f, default_flow_style=False)
```

## Verify

```bash
xurl auth status
xurl --auth oauth2 --app lucy --username kzinmr /2/users/me
```

Expected: returns user JSON, not auth error.

## Important

- **Never** print token values to LLM context. Only read YAML structure keys.
- The `oauth2_tokens` field contains access/refresh tokens — treat as secrets.
- After merging, run `xurl auth status` to confirm tokens are loaded.
