# Zyphra Releases ZAYA1-8B: MoE Reasoning Model Trained on AMD

> Source: Zyphra PR Newswire + Zyphra Blog — May 6, 2026
> URL: https://www.prnewswire.com/news-releases/zyphra-releases-zaya1-8b-302764700.html

Zyphra has released ZAYA1-8B, a mixture-of-experts (MoE) language model with 8.4 billion total parameters and only 760 million active parameters per inference pass. Trained entirely on AMD Instinct MI300X hardware with AMD Pensando Pollara networking on IBM Cloud infrastructure.

## Performance

With under 1 billion active parameters, ZAYA1-8B matches or exceeds substantially larger open-weight models:
- Matches or exceeds Mistral-Small-4-119B and Nemotron-3-Nano-30B-A3B
- Remains competitive with first-generation frontier reasoning models (DeepSeek-R1-0528, Gemini-2.5-Pro, Claude 4.5 Sonnet)
- On HMMT'25: 89.6 vs GPT-5-High's 88.3 (with Markovian-RSA test-time compute)
- Strong on AIME, LiveCodeBench, GPQA-Diamond, IFEval, IFBench

## Technical Innovations

- **MoE++ architecture**: Zyphra's proprietary mixture-of-experts design
- **AMD-native training**: First MoE model pretrained, midtrained, and supervised fine-tuned entirely on AMD hardware (1,024 MI300X nodes)
- **Reasoning from scratch**: Reasoning data included from pretraining onward using answer-preserving trimming
- **Markovian-RSA**: Novel test-time compute methodology for additional performance gains

## Availability

- Apache 2.0 license
- Model weights on Hugging Face (zyphra/ZAYA1-8B)
- Free serverless endpoint on Zyphra Cloud
- arXiv technical report: 2605.05365

Zyphra subsequently released ZAYA1-VL-8B on May 14, a vision-language model building on ZAYA1-8B with 700M active parameters, outperforming Deepseek-VL2, Qwen3-VL, and MolmoE.
