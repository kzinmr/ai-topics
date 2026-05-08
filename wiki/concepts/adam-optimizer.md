---
title: "Adam Optimizer"
type: concept
aliases:
  - Adam
  - AdamW
  - Adaptive Moment Estimation
created: 2026-05-08
updated: 2026-05-08
tags:
  - optimization
  - training
  - fine-tuning
related:
  - concepts/grpo
  - concepts/fine-tuning/_index
  - concepts/pytorch-fsdp
  - concepts/qlora
  - raw/articles/2024-02-08_linkedin-processsense-adam-adamw.md
sources:
  - "https://www.linkedin.com/pulse/understanding-adam-adamw-dsaisolutions-ileof/"
  - "https://arxiv.org/abs/1412.6980"
  - "https://openreview.net/forum?id=Bkg6RiCqY7"
---

# Adam Optimizer

**Adam（Adaptive Moment Estimation）** は、深層学習において最も広く使われている適応的学習率最適化アルゴリズム。2014年に Diederik P. Kingma と Jimmy Lei Ba によって提案され（ICLR 2015）[^1]、SGD with Momentum と RMSProp の長所を組み合わせた手法である。

## 位置付け

| 最適化手法 | 学習率 | モーメンタム | 適応的学習率 |
|-----------|--------|------------|------------|
| SGD | 固定 | なし | なし |
| SGD + Momentum | 固定 | 1次モーメント | なし |
| RMSProp | 固定 | なし | 2次モーメント（勾配の二乗平均） |
| **Adam** | 適応的 | **1次 + 2次モーメント** | **両方** |
| **AdamW** | 適応的 | 1次 + 2次モーメント | 両方 + **Weight Decay 分離** |

## 仕組み

Adam は勾配の**1次モーメント（平均）** と **2次モーメント（非中心分散）** の指数移動平均を追跡し、各パラメータに個別の適応的学習率を割り当てる。

### コア更新式

```
mt = β1·m_{t-1} + (1-β1)·gt       # 1次モーメント（勾配の指数移動平均）
vt = β2·v_{t-1} + (1-β2)·gt²      # 2次モーメント（勾配の二乗の指数移動平均）
m̂t = mt / (1-β1ᵗ)                 # バイアス補正
v̂t = vt / (1-β2ᵗ)                 # バイアス補正
θt = θ_{t-1} - η·m̂t / (√v̂t + ε)   # パラメータ更新
```

### Bias Correction（バイアス補正）

m0 と v0 はゼロベクトルで初期化されるため、特に初期ステップでモーメント推定値がゼロ方向に偏る。β1=0.9, β2=0.999 の場合、初期ステップでの m1 = 0.1·gt と著しく小さくなる。バイアス補正（1-βᵗ での除算）はこの初期バイアスを打ち消す。

### ハイパーパラメータ

- **β1 = 0.9**: 1次モーメントの減衰率。勾配の「勢い」の保持期間を制御
- **β2 = 0.999**: 2次モーメントの減衰率。適応的学習率の調整速度を制御。β1 より 1 に近い値が推奨される（1-β2 = 0.001 << 1-β1 = 0.1）
- **ε = 1e-8**: ゼロ除算防止の微小項
- **η（学習率）**: 一般的な初期値は 1e-3〜1e-4

## AdamW: Decoupled Weight Decay

Adam の主要な問題点は **正則化（L2 / Weight Decay）が適応的学習率と暗黙的に結合している** こと。具体的には、Adam の実装では Weight Decay 項が勾配計算に組み込まれ（gt = ∇f + λθ）、その後のモーメント推定と √vt による正規化の影響を受ける。結果として、勾配分散の大きいパラメータは小さい正則化しか受けない。

**AdamW**（Loshchilov & Hutter, 2019）[^2] は **Weight Decay を最適化ステップから分離（decouple）** することでこの問題を解決する：

```
# Adam (weight decay が勾配に混入)
gt = ∇f(θ) + λθ                     # ← 問題: λ が √vt でスケールされる
→ mt, vt に正則化項が混入
→ 更新時: θ = θ - η·m̂t/(√v̂t + ε)   # λ の効果がパラメータごとに不均一

# AdamW (weight decay を分離)
gt = ∇f(θ)                           # 純粋な勾配
→ mt, vt は勾配のみを追跡
→ 更新時: θ = θ - η·m̂t/(√v̂t + ε) - ηλθ  # λ が全パラメータに均一に適用
```

### なぜ AdamW が重要なのか

1. **学習率と Weight Decay の独立調整**: 学習率を変更しても最適な Weight Decay を再計算する必要がない
2. **安定した最適化**: 特に大規模モデルで汎化性能が改善
3. **実用上の標準**: PyTorch の `torch.optim.AdamW`、HuggingFace Transformers のデフォルト、LLM事前学習の標準

## LLM 学習における Adam/AdamW

大規模言語モデルの学習では AdamW が事実上の標準：

- **GPT シリーズ**: Adam（β1=0.9, β2=0.95, ε=1e-8）を使用
- **LLaMA シリーズ**: AdamW（β1=0.9, β2=0.95）を使用
- **DeepSeek**: AdamW を使用（→ [[concepts/grpo|GRPO]] は別のRL最適化手法）

LLM のファインチューニングでは、AdamW に加えて **8-bit Adam**（bitsandbytes）や **LoRA+AdamW** がメモリ効率の良い選択肢として使われる（→ [[concepts/qlora|Q-LoRA]]）。

## 強みと弱み

| 強み | 弱み |
|------|------|
| スパース勾配に強い（NLP, CV 両方で良好） | 初期学習率に敏感 |
| ハイパーパラメータ調整が比較的少ない | 小さなデータセットで過学習しやすい |
| 鞍点や平坦な領域で効率的 | 理論的な収束保証がSGDより弱い |
| 広範な実績とエコシステム | Weight Decay の暗黙的スケーリング（Adamの場合） |

## 参考文献

[^1]: Kingma, D. P., & Ba, J. (2014). **Adam: A Method for Stochastic Optimization**. arXiv:1412.6980. ICLR 2015.
[^2]: Loshchilov, I., & Hutter, F. (2019). **Decoupled Weight Decay Regularization**. ICLR 2019. https://openreview.net/forum?id=Bkg6RiCqY7
