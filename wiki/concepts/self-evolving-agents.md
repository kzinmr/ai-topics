---
title: "Self-Evolving Agents"
tags: [self-improving, agent-harness, agent-architecture, harness-engineering]
created: 2026-04-13
updated: 2026-04-24
type: concept
---

# Self-Evolving Agents

エージェントが自身の振る舞いや能力を時間とともに改善していくパターン。固定されたロジックではなく、フィードバックと学習による継続的な進化を可能にする。

## Core Concept

エージェントは単なるタスク実行者ではなく、自身のパフォーマンスを監視・分析・改善する**自律的な学習システム**として設計される。

```
Execute → Observe → Analyze → Adapt → Execute...
```

## Levels of Self-Evolution

### Level 1: Parameter Tuning

- プロンプトの温度や最大トークン数の自動調整
- リトライ回数の最適化
- ツール選択の重み付け更新

### Level 2: Strategy Adaptation

- 成功したパターンを記憶して再利用
- 失敗したアプローチを避ける
- タスクタイプに応じた戦略選択

### Level 3: Capability Expansion

- 新しいツールの発見と統合
- ワークフローの自動生成
- ドメイン知識の蓄積

### Level 4: Architectural Evolution

- マルチエージェント構成の動的変更
- オーケストレーションパターンの最適化
- システム設計の自己改善

### Level 5: Self-Modification（自己書き換え）

- **エージェントが自身のツール定義ファイルを読み取り、新しいツールクラスを追記する**
- ファクトリーパターンにより、ツール定義がクラスとして分離されていることが前提
- ランタイムが `st_mtime` でファイル変更を検知 → `importlib.reload()` でホットリロード
- エージェントは**書いた直後のターンで**新しいツールを呼び出せる
- 双方向：ツールの**作成**だけでなく**削除**も可能

**実装パターン**: [[concepts/agents-that-build-themselves]] を参照。Hugo Bowne-Anderson + Ivan Leo のワークショップで実証された「software building software」パラダイム。

```python
# Hot reload mechanism
def _check_reload(self):
    current_mtime = os.path.getmtime("agent_tools.py")
    if current_mtime > self._tools_mtime:
        importlib.reload(agent_tools)
        self._load_tools()
```

## Key Mechanisms

### Feedback Loops

- ユーザーからの明示的フィードバック
- 実行結果の暗黙的評価（成功/失敗）
- パフォーマンスメトリクスの監視

### Memory Systems

- 成功事例の保存と検索
- 失敗パターンの学習
- コンテキストの圧縮と保持

### Experimentation

- A/Bテストによる戦略比較
- 小さな変更からの学習
- 安全な探索空間の定義

## Risks and Mitigations

| Risk | Mitigation |
|------|-----------|
| 過学習 | 定期的なベースラインテスト |
| 劣化 | バージョン管理とロールバック |
| 予測不可能性 | 変更の監査証跡 |
| セキュリティ | 権限の制限と検証 |

## Related

- [[concepts/agents-that-build-themselves]] — Agents That Build Themselves (concrete implementation of Level 5)
- [[concepts/memory-systems-design-patterns]] — Memory Systems Design Patterns
- [[concepts/agent-team-swarm]] — Agent Team / Swarm
- [[concepts/harness-engineering]] — Harness Engineering
- [[concepts/evaluation-flywheel]] — Evaluation Flywheel
- [[entities/ivan-leo]] — Ivan Leo (co-creator of self-extending agent workshop)
