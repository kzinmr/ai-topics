# Single-Script Same-Entity Enrichment (Dreaming Wiki Ingest Pattern)

**適用**: 2記事以上が同一エンティティページをenrichment対象とする場合 — 複数のサブエージェントが同じファイルに同時書き込みすると競合するため、単一Pythonスクリプトで全ての追加を直列実行する。

## いつ使うか
- ✅ Triageの全takeが同一 `candidate_wiki_path` を指している
- ✅ エンティティページは既に存在し40行超（`write_file`不可、`patch`必須）
- ❌ 異なるエンティティへのenrichmentは並列サブエージェントに委任する

## Workflow

### Phase 1: Verification
1. エンティティページを `read_file` で全文読む — 行数と既存セクション構成を把握
2. 各raw articleを `read_file` で全文読む — 本文から追加すべき具体的内容を特定
3. 既存ページと記事の内容を比較 — **本当にギャップがあるか確認**（「記事タイトルに合致する概念セクションがあるけどデータが古い」等）

### Phase 2: Script Construction（ `write_file` → `/tmp/` ）
**構造**: 1つのPythonスクリプトに全str.replace()呼び出しを直列記述

```python
#!/usr/bin/env python3
def main():
    path = "/opt/data/ai-topics/wiki/entities/target-entity.md"
    content = open(path).read()
    
    # === PATCH 1: Frontmatter更新（sources追加 + updated日付）===
    content = content.replace(
        "  - raw/articles/existing-article.md",
        "  - raw/articles/existing-article.md\n  - raw/articles/2026-06-25_new-article-1.md\n  - raw/articles/2026-06-25_new-article-2.md"
    )
    content = content.replace("updated: 2026-06-17", "updated: 2026-06-25")
    
    # === PATCH 2: 既存セクションの更新（Hybrid Harness等）===
    content = content.replace("old section text", "new section text with updates")
    
    # === PATCH 3: 新規セクションの追加（文字列前後でユニークなコンテキストを指定）===
    content = content.replace(
        "既存セクション末尾のテキスト\n\n## 次のセクション見出し",
        "既存セクション末尾のテキスト\n\n## 新規セクション (June 2026)\n\n新しい内容...\n\n## 次のセクション見出し"
    )
    
    # === PATCH 4: Related Entitiesセクションに新しいwikilink追加 ===
    content = content.replace(
        "- [[entities/existing-entity]]\n",
        "- [[entities/existing-entity]]\n- [[concepts/new-concept]] — 関連する概念の説明\n"
    )
    
    content = content.replace(
        "\n## Sources",
        "**Sources:** [[raw/articles/2026-06-25_new-article-1]]\n\n## Sources"
    )
    
    with open(path, 'w') as f:
        f.write(content)
    print(f"OK: enriched ({len(content.splitlines())} lines)")

if __name__ == "__main__":
    main()
```

**キールール**:
- 各 `old_string` に**2-3行のユニークなコンテキスト**を含める — 短すぎると複数マッチして `replace()` が全出現箇所を置換してしまう
- セクション追加は「前のセクション末尾＋空行＋次のセクション見出し」をひとかたまりのold_stringにする
- `updated` 日付と `sources` は最終更新として最初に変更する
- 実行前に `write_file` でスクリプトを保存 → 文法チェック（lint）を通過させる

### Phase 3: Execution（ `terminal python3 /tmp/script.py` ）
- スクリプトが成功したら、`read_file` で対象ページを確認
- 特に注意：old_string が意図通りにマッチしなかった場所がないか

### Phase 4: Fallback Patch（ `|-` read_file prefix trap 対策 ）
`read_file` の出力（`648|- ...`）を str.replace() の old_string に使うと、パイプ記号 `|` が埋め込まれる。`str.replace()` はマッチ失敗を**エラーにせず**、対象文字列が見つからないだけ → 置換が行われず、気づかないまま次に進む。

**シグナル**: スクリプトが"OK"を返したが、対象ページを `read_file` で確認すると特定のパッチが未適用

**対策**:
1. 未適用の場所を特定
2. `sed -n 'N,Mp' wiki/entities/file.md | cat -A` で実際のファイル内容を確認
3. `|` なしの正しい文字列で `patch` tool で個別修正
4. 例: `|- 18/100`（間違い）→ `- 18/100`（正しい）

**ルート原因**: `read_file` の行番号プレフィックス（`NNN|`）をコピペするとファイル内容ではない装飾が混入する。ファイルの生の内容を確認するには `sed -n 'Np'` を使う。

### Phase 5: Index.md 確認
エンティティが index.md にまだ存在しない場合がある（初期作成時に追加漏れ）。patch で追加:

```
- [[entities/target-entity]] — Entity名; 追加した内容の簡潔な説明 (June 25)
```

日本語の日付ラベルは英語で書くこと（pre-commit hookがCJK文字をブロックする）。

### Phase 6: Log.md 追記 + Archive + Commit
- `write_file` で `log.md` を上書きしない — Python prepend script を `/tmp/` に書き、`terminal python3` で実行
- `python3 scripts/archive_triage.py dreaming --keep-reference` — dedupで0件でも正常
- `git add wiki/ && git commit -m 'wiki: enrich ...' && git push`

## 検証例（2026-06-25）

| 項目 | 値 |
|------|-----|
| 対象ページ | `entities/fireworks-ai.md` (289→348行, +59行) |
| 追加記事数 | 2 (training infrastructure + worker+advisor) |
| 追加セクション | 「Frontier Training Infrastructure (June 2026)」新設 + Hybrid Harness GLM 5.2更新 |
| 遭遇したトラップ | `read_file` 出力の `|-` を old_string に混入 → str.replace()がサイレント失敗 |
| 復旧方法 | patch tool で個別修正 |
| Index.md | エンティティ未登録だった → patch で追加 |
| Pre-commit | タグ3ファイル、全通過 |
| 合計時間 | ~3分（含む復旧） |
