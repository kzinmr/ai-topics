---
name: documentation-page-ingestion
description: "Policy for ingesting official documentation pages (product docs, developer guides, API references) into the wiki. Prioritizes creating a comprehensive overview guide of the subject over mechanically mirroring the source structure."
trigger: "When the user provides a URL to an official documentation page (product docs, developer guide, API reference, platform overview) and asks to create a wiki page from it, OR when enriching an existing wiki page from a documentation source."
---

# Documentation Page Ingestion Policy

## 基本方針

ドキュメントページを wiki に取り込む際、最優先すべきは **「そのドキュメントが解説している対象（サービス、フレームワーク、プラットフォームなど）の全体像を網羅的に把握できるガイド」を作ること** である。

ソース文書の構成はあくまで素材であり、wiki ページの目的は「これを読めばこの対象について一通りの理解が得られる」状態にすること。ソースの構造を機械的になぞることが目的ではない。

## 判断フロー

1. **対象の全体像を定義する**: このドキュメントは何についてのものか？ 読者がこの対象を理解するために必要な知識領域は何か？
2. **ソースを素材として活用する**: ソースのセクション構成は有用な手がかりだが、対象の全体像を網羅するために、ソースにないセクションを補ったり、逆に重要でないセクションを縮小したりする判断を行う
3. **他ソースとの統合**: 対象の全体像を描くために、同じ対象に関する他のドキュメントページや既存の wiki ページがあれば統合・参照する

## 具体例: 今回の失敗と修正

```
ソース: Build with Claude（Anthropic の開発者向けガイド）
対象: 「Claude を使ってアプリケーションを構築する方法」の全体像

失敗（修正前）:
  - モデルタイムラインがページの60%を占めていた
  - 「Claude の全モデル歴史」が主題になってしまい、対象の全体像を見失った

修正後:
  - 4本柱（Quick Start → Capabilities → Architecture → Optimization）で対象を網羅
  - モデル情報は Appendix に圧縮
```

## チェックリスト

ページ作成後、以下を確認する：

1. **ページを読めば、対象の全体像が掴めるか？** 概要を知りたい人がこの1ページで満足できるか
2. **特定の部分領域（モデル履歴、価格表など）にページの過半が割かれていないか？** 特に、特定の構造化データ（テーブル、タイムライン）が肥大化していないか
3. **ソースにないセクションが必要なら補ったか？** 対象の全体像を描くためにソースだけでは不十分な場合、補完しているか
4. **チュートリアル的手順（インストールコマンド、curl例など）が必要以上に展開されていないか？** wiki は構造化知識の場であり、ハウツーの場ではない

## Quick Start セクションの扱い

ソースに Quick Start / Getting Started がある場合、手順説明（インストールコマンド、APIキー取得手順など）はチュートリアル的な内容であり、wiki の知識ベースには馴染まない。リンク付きの1〜2文に圧縮する。

## コンテンツ取得のピットフォール

### web_extract のタイムアウト問題

`web_extract` は 14K+ chars のドキュメントページでタイムアウトする（特に Read the Docs の RST ソースや大規模な技術文書）。

**回避策**: `curl` + `read_file` を使用する。

```bash
# 1. curl でソースをローカルにダウンロード（RSTソースを推奨: _sources/*.rst.txt）
curl -sL 'https://verl.readthedocs.io/en/latest/_sources/hybrid_flow.rst.txt' -o /tmp/doc.rst

# 2. read_file で全文を読み取り
```

RST ソースの方が HTML より軽量でタイムアウトしにくい。Read the Docs の場合、`View page source` リンクから RST ソースの URL が得られる（`_sources/<name>.rst.txt`）。

### browser_navigate も使えない場合がある

`browser_navigate` は Chrome がインストールされていない環境（`agent-browser install` 未実施）では失敗する。この場合も `curl` + `read_file` にフォールバックする。

### 大規模HTMLからのテキスト抽出（両方フォールバック時）

`web_extract` がタイムアウトし、`browser_navigate` も使えない場合、`curl` でダウンロードしたHTMLファイル（500KB+）をそのまま `read_file` するのは非効率。ナビゲーション・フッターのノイズが多く、本文を見つけるのに大量のオフセットスキャンが必要になる。

**回避策**: PythonスクリプトでHTMLタグを除去してから `read_file` する（詳細なステップバイステップガイドは `references/large-html-extraction.md` を参照）。

```bash
# 1. curl でHTMLをダウンロード
curl -sL '<URL>' -o /tmp/doc.html

# 2. Pythonでタグ除去 → プレーンテキスト化
python3 -c "
import re
with open('/tmp/doc.html', 'r') as f:
    html = f.read()
html = re.sub(r'<(script|style)[^>]*>.*?</\\1>', '', html, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', ' ', html)
text = re.sub(r'\\n{3,}', '\\n\\n', text)
with open('/tmp/doc.txt', 'w') as f:
    f.write(text)
print(f'Done: {len(text)} chars')
"

# 3. read_file で本文を読み取る（offset/limit でチャンク読み）
```

**注意**: `terminal` 内のインラインPythonはシェルのクォート問題（ネストした引用符、heredoc展開）で失敗しやすい。長いPythonコードは先に `write_file` で `/tmp/extract_script.py` に保存してから `terminal` で `python3 /tmp/extract_script.py` を実行する方が安全。

### Google Slides のテキストエクスポート

Google Slides（`docs.google.com/presentation/d/<ID>/edit`）は `web_extract` の編集URL取得がほぼ常に失敗する（network_error）。また `web_extract` で `/export/txt` URL を指定しても LLM 要約がタイムアウトして途中で切れる（実績: 16K chars のスライドテキストが 5K で打ち切り）。

**回避策**: `/export/txt` エンドポイントを `curl` で直接取得する。

```bash
# プレゼンテーションIDからエクスポートURLを構築
curl -sL 'https://docs.google.com/presentation/d/<PRESENTATION_ID>/export/txt' -o /tmp/slides.txt

# 行数・バイト数でサイズ確認
wc -l /tmp/slides.txt && wc -c /tmp/slides.txt
```

このエンドポイントは全スライドのテキストをプレーンな行区切りテキストとして返す。図や画像は含まれないが、コードブロックや箇条書きは保持される。スライド境界は空行で表現される。

**スライドデッキの扱い**:
- スライドデッキにはほぼ常にテンプレートスライド（自己紹介、コース案内、アジェンダなど）が含まれる。ユーザーが「p1-6はテンプレ、本文はp7から」などと明示した場合は、テンプレートをスキップし本編のみを素材とする。
- `read_file` を `offset`/`limit` で分割読み（200行ずつが目安）して全体を把握する。
- raw article のファイル名は [[raw-article-filename-policy]] の「Slides/presentations」ルールに従い、取り込み日 + `date_ingested` frontmatter を使う。
- スライドから作成する wiki 概念ページは、スライドの順序を素材としつつも、トピックの全体像を網羅する構成に再編成する（この skill の基本方針に従う）。

**スライドから wiki ページへの変換例**:
- 「Lexical Search & BM25」スライド → `lexical-search.md` + `bm25.md` に分割（TokenizationとScoringは別概念のため）
- 「Vector Search & Embedding Retrieval」スライド → `embeddings.md` + `vector-search.md` に分割（埋め込み学習とANN検索は別概念のため）

ページの分割判断基準：スライドが扱う概念が独立した知識領域を形成するか、既存 wiki に別ページが存在するか。

## Feature-Level Documentation Pages

ドキュメントページがプラットフォーム全体ではなく**特定の機能やコマンド**を対象とする場合（例: Claude Codeの `/goal`、`/loop`、Codexの `/goal`）、プラットフォーム向けの全体像ガイドとは異なる構成が適する。`references/feature-doc-template.md` のテンプレートを参照。

## Docs → Cross-Cutting Concept Enrichment

ドキュメントページが説明する機能が、wiki内の**既存の概念フレームワーク**（例: Lance MartinのContext Engineering、Jeff HuberのInner/Outer Loop）に明確に対応する場合、スタンドアロンページの作成よりも**既存概念ページの拡充**を優先する。

### 判断基準

以下の条件が揃った場合、このパターンを使う：
1. ドキュメントの機能が既存のwiki概念フレームワークに**1対1でマッピング**できる（例: continue/resume/fork → Write/Select/Isolate）
2. 既存の概念ページが十分に成熟しており、新しいセクションの追加が自然
3. ドキュメント単体よりも、**マッピングの分析自体**に知識価値がある

### ワークフロー

1. **Raw記事保存**: ドキュメント全文を `wiki/raw/articles/` に保存（`date_ingested` frontmatterを使用）
2. **マッピング分析**: SDK API / 機能を既存フレームワークの各要素に対応付ける
3. **概念ページ拡充**: 既存の概念ページに新セクションとして追加。対応表 + 設計判断の分析 + 含意を含める
4. **エンティティページ更新**: 対象プロダクトのエンティティページにも新セクションを追加し、双方向リンク
5. **ソース登録**: 概念ページとエンティティページの両方の `sources:` にraw記事リンクを追加

### 実例: Claude Code Agent SDK Sessions

```
ソース: https://code.claude.com/docs/en/agent-sdk/sessions
機能: continue / resume / fork の3操作によるセッション管理

マッピング:
  continue → Write + Select（透過的永続化と復元）
  resume   → Select（精密なコンテキスト検索）
  fork     → Isolate（会話履歴の分岐）

拡充先:
  concepts/harness-engineering/context-engineering.md  → 新セクション「Claude Code Agent SDK: Context Engineering の SDK 実装」
  entities/claude-code.md                               → 新セクション「Session Management (Agent SDK)」
```

## Batch Blog Ingestion Pattern (sitemap → raw → concepts)

When ingesting an entire blog (e.g. developers.openai.com/blog, anthropic.com/engineering):

1. **Extract article list from sitemap** — `curl /sitemap-0.xml | grep '<loc>' | grep '/blog/'`. RSS feeds often mix blog posts with docs/cookbook/guides — sitemap filtering by path prefix is more accurate.
2. **Save all raw articles** — Use `delegate_task` with 2 parallel subagents (split URLs evenly). Each subagent fetches via curl, extracts article body, saves with YAML frontmatter to `wiki/raw/articles/`.
3. **Cross-reference with existing wiki** — Search wiki for URL paths (not generic words). Searching for bare slugs like `intro` or `responses-api` matches unrelated content. Use the full URL or `developers.openai.com/blog/<slug>` pattern.
4. **Prioritize by cross-vendor comparison** — When a competitor's blog is already ingested (e.g. Anthropic engineering), map each new article to its equivalent. This prevents priority drift and reveals coverage gaps. Create a comparison table: topic area → vendor A article → vendor B article → wiki page status.
5. **Create wiki pages in parallel** — `delegate_task` with batch of 3 subagents. Each reads raw articles + existing cross-reference pages, creates concept pages, updates index entries.
6. **Fix index.md section structure** — After adding entries, verify section counts: `awk '/^## Concepts/{s="c"} /^## Events/{s="e"} /^- \[\[/{counts[s]++} END{for(k in counts) print k": "counts[k]}' index.md`. Pre-existing misplacement bugs are common (concept entries under wrong section headers).
7. **Tag taxonomy check before commit** — Pre-commit hook blocks on tags not in SCHEMA.md. Add missing tags to SCHEMA.md taxonomy lines BEFORE committing. Common additions needed: product names, engineering concepts, company names.

### 注意点

- ドキュメントを機械的にミラーリングしない。マッピングと分析が本体であり、APIリファレンスの再掲は最小限に留める
- マッピング表は必ず含める（読者が一目で関係を把握できる）
- 「設計上の含意」セクションで、なぜこのマッピングが重要なのかを論じる

## シリーズ物のドキュメントを扱う場合

同じ著者・同じシリーズから複数回ドキュメントを取り込む場合（例: Doug Turnbull "Cheat at Search" シリーズ）、以下の作業を推奨：

1. **既存の関連ページを確認**: シリーズの過去の講義が既にwikiに取り込まれていないか検索する
2. **シリーズ間の接続を明記**: 新しい概念ページに、同じシリーズの関連ページへの相互リンクを追加する
3. **概念的進化を追跡**: 前回までの話題と今回の新話題がどう接続するかを「過去の講義との接続点」として記録する
4. **エンティティページも更新**: 著者のエンティティページに今回の講義を追加し、シリーズ全体のタイムラインを維持する

例: 5回の「Cheat at Search」講義を取り込んだ後、`agentic-search.md` に全5回の比較表（収量/呼び出し比）を追加し、各概念ページ間で双方向リンクを張った。

## Lecture Series / Transcript Cross-References

レクチャーシリーズ（例: Cheat at Search）の transcript を新規作成する場合、**既存の鄰接 transcript の "Related transcripts" セクションも更新する**。新規 transcript に既存へのリンクを張るだけでなく、双方向リンクにする。

**手順:**
1. 新規 transcript を作成（フロントマター + 本文 + Companion Resources）
2. `wiki/raw/transcripts/` で既存の同シリーズ transcript を確認（`search_files` で author/date パターン一致）
3. 隣接 transcript（前回・次回）の "Related transcripts" セクションに新規ファイルへの wikilink を追加
4. 同様に `wiki/raw/articles/` の対応スライド記事もあればリンク確認
5. 全ファイルを同じコミットに含める

**ピットフォール:** transcript のみ新規作成してスライド記事の存在確認を忘れると、片方向リンクになる。必ず `search_files` でシリーズ全体を把握してから作業を始める。

## コミット・プッシュ時の Git 競合

### log.md の rebase 競合

複数のエージェントやcronジョブが同時にwikiを更新する環境では、`git push` が reject され `git pull --rebase` で `log.md` に競合が発生することが頻繁にある。

**対応手順**:
```bash
cd ~/ai-topics
git stash                     # 未ステージ変更を退避
git pull --rebase             # rebase試行 → log.mdでCONFLICT
# 競合マーカーを手動解決（HEAD側のエントリ + 自分のエントリを両方残す）
grep -n '<<<<<<<|=======|>>>>>>>' wiki/log.md  # 競合箇所確認
# patch ツールで解決
git add wiki/log.md
GIT_EDITOR=true git rebase --continue
git stash pop                 # 退避した変更を復元
git push
```

**注意**: `GIT_EDITOR=true` でエディタをスキップしないと `error: Terminal is dumb, but EDITOR unset` で失敗する。ログエントリは両方残す（削除しない）。

## タグバリデーション

wiki の pre-commit フックは、ページに使われているすべてのタグが `SCHEMA.md` のタクソノミーに存在するかチェックする。SCHEMA.md にないタグを使うとコミットがブロックされる。

**対応**: コミット前に `SCHEMA.md` に必要なタグを追加する。タグ追加時も SCHEMA.md をコミットに含めること。

例: veRL の HybridFlow ページでは `ray` タグを Infrastructure カテゴリに追加した。
