# Audio Tokenizer Comparison — SoundStream / EnCodec / DAC / SpeechTokenizer / Mimi

5つの音声トークナイザ（SoundStream、EnCodec、DAC、SpeechTokenizer、Mimi）は、同じ「音声を離散トークン列にする」手法でも、何のためのトークン化かがかなり違う。本稿ではその比較と実務的な選び方を解説する。

## Summary

- SoundStream / EnCodec / DAC：高忠実度ニューラル音声コーデック（圧縮と再構成品質が主眼）
- SpeechTokenizer / Mimi：speech language model 向け（意味情報と音響情報を階層的に整理）

5手法とも大枠では RVQ 系の離散化を使うが、後者2つは semantic teacher / distillation を入れて意味と音響の分離を明示的に狙うのが本質的な差。

## Comparison Table

| 手法 | 位置づけ | semantic/acoustic分離 | token rate | bitrate | sample rate | streaming |
|------|---------|----------------------|------------|---------|-------------|-----------|
| SoundStream | 原型 | ❌ | ~50 Hz | 3–18 kbps | 24 kHz | ✅ |
| EnCodec | 標準形 | ❌ | ~50 Hz | 1.5–24 kbps | 24/48 kHz | ✅ |
| DAC | 高忠実度・汎用 | ❌ | ~50 Hz | 8 kbps | 44.1 kHz | ❌ |
| SpeechTokenizer | LLM向け統合 | ✅ (Layer1=semantic) | ~50 Hz | ~4 kbps | 16 kHz | ❌ |
| Mimi | 低レート会話向け | ✅ (WavLM distillation) | **12.5 Hz** | **1.1 kbps** | 24 kHz | ✅ fully |

## Detailed Breakdown

### SoundStream
fully convolutional encoder/decoder + RVQ を end-to-end で学習、再構成損失と adversarial loss を併用。quantizer 層への structured dropout により 3–18 kbps の可変ビットレート。24 kHz、低遅延ストリーミング、スマホ CPU 上の real-time 動作。中心思想は「良い codec を作り、その code を token として使う」。

### EnCodec
SoundStream をベースに、single multiscale spectrogram adversary + loss balancer、軽量 Transformer による entropy coding（最大40%追加圧縮）。24 kHz mono causal / 48 kHz stereo non-causal の2種類。codec 系 tokenizer の中でもかなり実用性が高く、研究・実装の両面で使いやすい定番。

### DAC (Descript Audio Codec)
論文名：High-Fidelity Audio Compression with Improved RVQGAN。44.1 kHz 音声を 8 kbps、約90倍圧縮、speech / environment / music を単一の universal model で扱う。improved vector quantization + improved adversarial / reconstruction losses。EnCodec の drop-in replacement としても位置づけられる。高忠実度・汎用音源・生成向け front-end として最も強い。

### SpeechTokenizer
「既存の semantic token も acoustic token も speech language modeling には最適でない」という立場から出発。encoder-decoder + RVQ だが、第1 quantizer = semantic token、残り = timbre などの補完情報。HuBERT 系の semantic teacher で第1層を導く。sample_rate=16 kHz、strides=[8,5,4,2]、n_q=8、codebook_size=1024 → 約50 frames/sec、約4 kbps。「第1層だけ使えば意味寄り、全層使えば再構成寄り」という操作性が強み。

### Mimi
SpeechTokenizer の「semantic と acoustic を統合」を引き継ぎつつ、token rate をリアルタイム会話 LLM で回せる水準まで押し下げた設計。24 kHz → 12.5 Hz → 1.1 kbps、80 ms frame latency、fully streaming。encoder/decoder 両方に Transformer 追加、第1 codebook を WavLM 表現に合わせる distillation、adversarial loss + feature matching。肝は「semantic 情報を保ちながら autoregressive step 数を大きく減らす」こと。

## 比較軸（4つ）

1. **codec 品質重視 vs LLM 用 token 重視**
2. **semantic/acoustic の分離を明示するか**
3. **token rate をどこまで下げるか**
4. **対応ドメイン**（DAC は speech/music/environment、SpeechTokenizer/Mimi は speech 寄り）

## 実務的な選び方

- 音楽や環境音も含めて高忠実度に token 化 → DAC、次に EnCodec
- 可変ビットレート streaming codec の基本形を理解 → SoundStream
- speech LLM / zero-shot TTS / semantic-first 制御 → SpeechTokenizer
- リアルタイム対話 / streaming spoken LLM / 低遅延最重要 → Mimi

## 注意

5手法の音質を単純な1列ランキングにはしにくい。SoundStream(24 kHz)、EnCodec(24/48 kHz)、DAC(44.1 kHz)、SpeechTokenizer(16 kHz)、Mimi(24 kHz speech) と sample rate が異なり、EnCodec には non-causal モデルがあり、Mimi は fully streaming。比較は「誰が一番音が良いか」ではなく「何を token に残したいのか（音質か、意味か、遅延か）」で見るのが正しい。
