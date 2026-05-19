# Triage Archive

トリアージで skip/reference 判定された記事の退避先。削除はせず、ここに移動して後日の再評価や参照に備える。

## ディレクトリ構造

```
archived/triage/
├── blog/          # blog-triage の skip/reference 判定記事
├── newsletter/    # newsletter-triage の skip/reference 判定記事
└── dreaming/      # dreaming-group の skip/reference 判定記事
```

## ファイル命名規則

`{YYYY-MM-DD}_{triage_run_id}.json`

## 各エントリのJSON構造

```json
{
  "archived_at": "ISO8601",
  "triage_run_id": "...",
  "source": "blog|newsletter|dreaming",
  "decisions": [
    {
      "item_id": "...",
      "title": "...",
      "url": "...",
      "raw_path": "...",
      "recommended_action": "skip|reference",
      "reason_ja": "...",
      "body_excerpt": "本文冒頭200字..."
    }
  ]
}
```

## ポリシー

- **削除しない**: 誤判定の可能性があるため、アーカイブは削除ではなく退避。後日再評価できる
- **重複排除あり**: 同一 URL の記事が複数回アーカイブされることはない（archive_index.json で管理）
- **再評価**: 半年に1回程度、アーカイブ記事を見直し、新たな文脈で価値が出たものを再トリアージ
