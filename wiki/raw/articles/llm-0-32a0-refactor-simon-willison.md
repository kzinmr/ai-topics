# LLM 0.32a0: メッセージシーケンスとストリーミングパートへの大規模リファクタ

## 概要
Simon Willison は2026年4月29日、LLM Python ライブラリ/CLI ツールのアルファリリース **0.32a0** を公開した。これは後方互換性を維持しつつ、LLM が現代のフロンティアモデルの多様な入出力タイプに対応するための大規模リファクタリングである。

## リファクタリングの背景
LLM は2023年4月の開始以来、「テキストプロンプト → テキストレスポンス」のシンプルな抽象化で動作していた。しかし、以下の変化に対応する必要が生じた:

- **マルチモーダル入力**: 画像、音声、ビデオのサポート
- **構造化出力**: スキーマベースの JSON 出力
- **ツール呼び出し**: エージェントが外部ツールを実行する機能
- **推論サポート**: モデルの内部思考プロセス
- **ストリーミング**: 部分的な結果のリアルタイム配信

元の抽象化では、これらの新しい機能を適切に表現できなくなっていた。

## 主要な変更点
### 1. メッセージシーケンスとしてのプロンプト
LLM 0.32a0 では、プロンプトをメッセージのシーケンスとして表現できるようになった:

```python
import llm
from llm import user, assistant

model = llm.get_model("gpt-5.5")

response = model.prompt(messages=[
    user("Capital of France?"),
    assistant("Paris"),
    user("Germany?"),
])
print(response.text())
```

これにより、OpenAI の Chat Completions API などのベンダー API との互換性が向上し、過去の会話の再現やエミュレーションが容易になった。

### 2. ストリーミングパート
応答を異なる型のパートのストリームとして構成できるようになった。これにより、テキスト、画像、ツール呼び出しなどが混在するストリーミング出力を適切に扱える。

### 3. 後方互換性
従来の `prompt=` オプションも引き続き機能し、内部的に単一アイテムのメッセージ配列にアップグレードされる。

## 関連概念
- [[ai-agents]] — エージェントフレームワーク
- [[tool-use]] — ツール呼び出し機能
- [[multimodal-models]] — 複数モーダル入出力

## ソース
- Simon Willison's Weblog: https://simonwillison.net/2026/Apr/29/llm/
- LLM Documentation: https://llm.datasette.io/en/latest/changelog.html
