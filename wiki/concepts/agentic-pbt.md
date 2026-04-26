---
title: Agentic Property-Based Testing (Anthropic + Hypothesis)
type: concept
aliases: [agentic-pbt, anthropic-property-based-testing]
created: 2026-04-14
updated: 2026-04-14
status: active
sources:
  - https://red.anthropic.com/2026/property-based-testing/
  - https://mmaaz-git.github.io/agentic-pbt-site/
  - https://github.com/HypothesisWorks/hypothesis
  - http://drmaciver.com/2026/04/how-ive-been-using-claude-code/
  - https://antithesis.com/blog/2026/hegel/
tags:
  - concept
  - ai-coding
  - property-based-testing
  - ai-evals
  - software-correctness
---

# Agentic Property-Based Testing

Anthropic + Hypothesis共同研究（NeurIPS 2025 DL4C Workshop）。Claude Codeエージェントが型注釈、docstring、関数名、コメントからコードの不変条件（properties）を自律的に推論し、HypothesisフレームワークでPBTを生成・実行する。

## Agent Architecture

```
Analyze Target → Propose Properties → Generate Tests → Self-Reflect → Report
     ↓                ↓                   ↓              ↓          ↓
  Read code,     Infer invariants    Write Hypothesis  If fail:   Formatted
  docs, usage    from type ann,      tests with        real bug   bug report
  context        docstrings, names   auto-generated    or bad     only when
                                   inputs              test?      confident
```

**Key Design Features:**
- **TODOリスト**による長期推論管理
- **Self-reflection loop**でfalse positiveを大幅削減
- **Opus 4.1**と**Sonnet 4.5**でSonnet 4より性能大幅向上
- 明示的なドキュメント/使用パターンへのgroundingが重要

## Evaluation Results

### Phase 1 (Opus 4.1)
- **100+ PyPIパッケージ**（NumPy, SciPy, Pandas等）をテスト
- 984件のバグレポート生成
- 50件の手動レビュー結果：
  - 56%がvalid bugs
  - 32%がvalid & reportable
- **Rubricランキング**適用時（上位レポート）：
  - 86% validity rate
  - 81% reportable rate

### Phase 2 (Sonnet 4.5)
- 10件のcriticalパッケージで複数回実行
- **自動化評価エージェント + 3名の専門レビュアー**でhigh-severityバグを検証
- Strict Validation Protocol：メンテナ疲労回避のため、3専門家+著者確認済みのバグのみ filing
- 全データ（valid/invalid/unvalidated）を公開

## Notable Bugs Discovered

| Package | Function | Issue | Impact |
|---------|----------|-------|--------|
| `numpy` | `random.wald` | 負の数を返す | Catastrophic cancellation。修正で相対誤差を~10桁改善 |
| `aws-lambda-powertools` | `slice_dictionary()` | 最初のチャンクを重複 | イテレータが再構築中にインクリメントされない |
| `cloudformation-cli-java-plugin` | `item_hash()` | 全リストで同一ハッシュ | 破壊的`.sort()`がNoneを返すため |
| `tokenizers` | `calculate_label_colors()` | 無効なHSL CSS出力 | 閉じ括弧の欠落 |
| `python-dateutil` | `easter()` | 非日曜日の日付（ユリウス暦） | メンテナー確認済みの微妙なセマンティクス |

## Limitations

> "Deriving properties from code with subtle or complex semantics remains difficult. If the code makes an implicit assumption, only the library maintainers can decide what the correct property to test is."

**Implicit assumptions** — コードが暗黙の前提を持っている場合、正しいテストプロパティを決定できるのはライブラリメンテナーのみ。

## Future Directions

- **Proactive Security**: LLM-powered exploit生成に対抗し、デプロイ前に脆弱性を特定
- **Automated Patching**: "If it is possible to (nearly) completely specify the correctness properties of a block of code, then correcting the bug becomes significantly easier." — メンテナレビュー用のLLM生成パッチ
- **Ecosystem Expansion**: より多くのPyPIプロジェクトへのスケーリング、自動検証パイプラインの改善

## Connection to DRMacIver / Antithesis

この研究は**David R. MacIver**（Hypothesis作者、Antithesis Senior Engineer）の哲学と完全に一致：

> "Property-based testing is going to be a huge part of how we make AI-agent-based software development not go terribly."

Anthropic研究の共同著者**Liam DeVoe**もHypothesisコアメンテナーの一人。MacIverと同様にAntithesisに参加しており、Agentic PBTとHegel（言語横断PBTプロトコル）の開発を推進している。

MacIverのClaude Code実践レポート（2026-04）：
> "In order to ensure there's enough testing, we set minimum coverage to 100%. I basically think there's no good reason to have untested code in a project with AI working on it."

## Related Concepts

-  — テストパラダイムの基礎
- [[concepts/harness-engineering]] — Claude CodeコマンドとしてのAgentic PBT
- [[concepts/ai-evals]] — 984バグレポート生成、86%妥当性率
-  — AIエージェントによる自律的コード品質保証
-  — 不変条件によるバグ発見
- [[drmaciver]] — Hypothesis作者、Antithesis Senior Engineer
- [[concepts/mismanaged-geniuses-hypothesis]] — Python PBTライブラリ
-  — 言語横断PBTプロトコル

## Sources

- [Property-Based Testing with Claude](https://red.anthropic.com/2026/property-based-testing/) — Anthropic Research
- [Agentic PBT Bug Database](https://mmaaz-git.github.io/agentic-pbt-site/) — 全バグレポート公開
- [NeurIPS 2025 DL4C Workshop](https://openreview.net/forum?id=...) — 論文
- [How I've been using Claude Code](http://drmaciver.com/2026/04/how-ive-been-using-claude-code/) — MacIver's practical report
- [Hegel: Universal PBT Protocol](https://antithesis.com/blog/2026/hegel/) — Antithesis
