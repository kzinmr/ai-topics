# JP→EN Translation: Chinese Proper Noun Handling

## Problem
When scanning wiki files for Japanese content using CJK character regex (`[\u4E00-\u9FFF]`), many files report high "CJK character counts" that are actually Chinese proper nouns, not Japanese text.

## Examples Found in Production
- Person names: 姚顺雨 (Yao Shunyu)
- Organization names: 智谱AI (Zhipu AI), 月之暗面 (Moonshot AI)
- Product names: Various Chinese tech products

## Solution
1. **Use hiragana/katakana-only regex** to identify translatable JP content:
   ```python
   import re
   jp_kana = re.compile(r'[\u3040-\u309F\u30A0-\u30FF]')
   ```
2. **Verify CJK characters** are Chinese names/orgs before attempting translation
3. **Preserve Chinese proper nouns** as-is, optionally adding English translation in parentheses

## Verification Script
```python
import re
from pathlib import Path

wiki_root = Path('/opt/data/ai-topics/wiki')
jp_kana = re.compile(r'[\u3040-\u309F\u30A0-\u30FF]')
cjk = re.compile(r'[\u4E00-\u9FFF]')

for f in wiki_root.rglob('*.md'):
    if 'raw/' in str(f):
        continue
    content = f.read_text()
    kana_count = len(jp_kana.findall(content))
    cjk_count = len(cjk.findall(content))
    
    if kana_count > 0 or cjk_count > 50:
        print(f"{f.relative_to(wiki_root)}: {kana_count} kana, {cjk_count} CJK")
```

## Key Insight
A file with 149 CJK characters and 0 kana characters likely contains only Chinese proper nouns — no translation needed.