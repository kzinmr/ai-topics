#!/usr/bin/env python3
"""Debug SCHEMA.md tag parsing."""
import re

with open('/opt/data/ai-topics/wiki/SCHEMA.md') as f:
    content = f.read()

idx = content.find('## Tag Taxonomy')
section = content[idx:idx+5000]

# Check for backtick patterns - use chr(96) to avoid shell issues
bt = chr(96)
backtick_tags = re.findall(bt + r'([a-z][a-z0-9-]+)' + bt, section)
print(f"Backtick-wrapped tags: {len(backtick_tags)}")
if backtick_tags:
    print(f"  {backtick_tags}")

# Check category lines
print("\nCategory lines:")
for line in section.split('\n')[:30]:
    if line.strip().startswith('- **'):
        parts = line.split(':', 1)
        if len(parts) == 2:
            body = parts[1]
            print(f"  {line[:80]}...")
            # Show first 10 comma-separated items
            items = [t.strip() for t in body.split(',')[:10]]
            print(f"    First items: {items}")
