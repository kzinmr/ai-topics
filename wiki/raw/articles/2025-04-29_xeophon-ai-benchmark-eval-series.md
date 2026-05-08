---
date: 2025-04-29
source: x.com (xeophon thread)
source_url: https://x.com/xeophon/status/1917175899948020203
author: Florian Brand (@xeophon)
type: x_thread
series: AI Benchmarks & Evals Series
parts: 18
scrape_status: complete_all_18
tags:
  - benchmarks
  - evals
  - llm-evaluation
  - ai-metrics
---

# AI Benchmarks & Evals Series — @xeophon (All 18 Parts)

Florian Brand (@xeophon)による、主要なAIベンチマーク・評価指標を解説する18部構成のXスレッドシリーズ。各Partで一つのベンチマークを取り上げ、その設計思想、データ収集方法、強みと弱点を解説している。

## Part 1: GPQA (Graduate-Level Google-Proof Q&A)
**Date:** 2025-04-29
**Summary:** 最も人気のあるベンチマークの一つ。生物学・物理学・化学のみを対象としている点に注意が必要。データ作成は洗練されており、HLEと同様の手法が使われている。金銭的インセンティブは現在の方が高い。また、メインセットよりもdiamond setの方が重要（メインセットには専門家間で意見が分かれる問題が含まれる）。

## Part 2: LiveCodeBench
**Date:** 2025-04-30
**Summary:** 数ヶ月ごとに問題を入れ替えて鮮度を保つ興味深いeval。ただし、最近のLLMは簡単なコーディングタスクが得意すぎて、easy/medium LeetCode問題には退屈してしまう。コード生成の汚染のない評価として設計されている。

## Part 3: Aider Polyglot
**Date:** 2025-05-01
**Summary:** 6つのプログラミング言語（Pythonだけでなく）をカバーするコーディングベンチマーク。多言語対応は思ったより珍しい特徴。

## Part 4: MMLU Pro
**Date:** 2025-05-02
**Summary:** MMLUを意味のある形で改善。LLM支援のフィルタリングを多用。MMLU Proの問題の43%はMMLUには含まれていない新規問題。

## Part 5: MMMU (Massive Multi-discipline Multimodal Understanding)
**Date:** 2025-05-05
**Summary:** シリーズ初の画像eval。データソーシングは多数の大学生による手作業。非常に幅広いトピックをカバーするが、難易度は比較的低め。

## Part 6: MRCR (Multi-Round Coreference Resolution)
**Date:** 2025-05-06
**Summary:** 長文コンテキストeval。単純なNIAH（Needle in a Haystack）を改善し、複数のneedleを配置し、hay（干し草=無関係なテキスト）をneedleにやや類似させる工夫がある。アイデアはGoogle発だが、OpenAIがオープンソース版を公開しており、これが標準になる可能性が高い。

## Part 7: SimpleQA
**Date:** 2025-05-07
**Summary:** ケイパビリティチェックというよりサニティチェック・ツール呼び出しeval。ニッチな知識に焦点を当てている。RLトレーニングの普及に伴いモデルが知識を失う可能性があるため、この種のevalの重要性が増している。

## Part 8: Vibe-Eval (Reka)
**Date:** 2025-05-08
**Summary:** 誰でも（そして誰もが）独自に持つべきeval。自分の興味のあるトピックに関するプロンプトセットで、幅広いタスクをカバーする。Rekaチーム自身がデータ収集を行ったパーソナライズド評価。

## Part 9: BFCL V3 (Berkeley Function Calling Leaderboard)
**Date:** 2025-05-09
**Summary:** 関数呼び出しeval。V3はマルチターン・マルチステップの関数呼び出しに焦点。今年非常に重要になる分野。人間による検証が行われており、非常によくできたeval。今年多く見られることを期待。

## Part 10: IFEval (Instruction Following Eval)
**Date:** 2025-05-13
**Summary:** クールで超シンプルなeval。LLMの一つの側面だけをテストし、評価が容易。指示追従能力の基本的なチェック。

## Part 11: ChartQA
**Date:** 2025-05-14
**Summary:** データソーシング（チャートプロバイダーのスクレイピング）は健全だが、テストデータが非常にノイジー。間違った例や曖昧な例が簡単に見つかり、小数点以下の桁数などの不整合もある。引退すべき時期。

## Part 12: Tau-Bench
**Date:** 2025-05-15
**Summary:** 別のLLMを使ってユーザーをシミュレートし、関数呼び出しをテストするクールで小さなベンチマーク。この種のevalは今年非常に重要になる。

## Part 13: Humanity's Last Exam (HLE)
**Date:** 2025-05-19
**Summary:** おそらく最も難しいMMLU形式の知識＋推論ベンチマーク。厳格なフィルタリングパイプラインと参加者への良いインセンティブ設計が特徴。

## Part 14: CountBenchQA
**Date:** 2025-05-20
**Summary:** 超シンプルなベンチマークだが、モデルがこのようなタスクで良好なパフォーマンスを発揮することは極めて重要。一つのことを一つのレベルでテストするベンチマークを評価。データも素晴らしい（*chefs kiss*）。

## Part 15: ARC-AGI (1) by François Chollet / ARC Prize
**Date:** 2025-05-21
**Summary:** 今でもお気に入りの一つのベンチマーク。抽象推論とfluid intelligenceをテストするARC-AGI。CholletとARC Prize財団による。

## Part 16: ARC-AGI 2 by ARC Prize
**Date:** 2025-05-22
**Tweet:** https://x.com/xeophon/status/1925513059281305612
**Summary:** ARC-AGIの第2版。多数の人間をタスクテストに参加させることで初版を意味のある形で改善。タスクは初版とかなり似ているにもかかわらず、非人間（AI）のパフォーマンスが急落するのが驚き。
- Website: https://arcprize.org
- Paper: https://arxiv.org/abs/2505.11831

## Part 17: SWE-Bench Verified by Ofir Press / OpenAI
**Date:** 2025-05-23
**Tweet:** https://x.com/xeophon/status/1925870415173300350
**Summary:** 健全なベンチマーク。モデルは既存のGitHub issueを解決するタスクを与えられる。1 issueあたり3名のアノテーターによる検証は手厚い。モデルが現在80-85%で頭打ちになっているのは驚き。また、最初の（？）エージェント的ベンチマークでもある。
- OG Paper: https://arxiv.org/abs/2310.06770
- SWE-bench Verified: https://openai.com/index/introducing-swe-bench-verified/
- Leaderboard: https://swebench.com

## Part 18: Factorio Learning Environment (FLE)
**Date:** 2025-05-27
**Tweet:** https://x.com/xeophon/status/1927325298011287757
**Summary:** 非常に楽しいeval。重要なのは、モデルがコードを書いてREPLを通じて対話する方式で、ビジョンは不要な点。Factorioを知らない人は調べない方がいい（何時間も溶けるので）。
- Project page: https://jackhopkins.github.io/factorio-learning-environment/
- Paper: https://arxiv.org/abs/2503.09617
