---
title: "Checkpoint forensics: GPU-architecture fingerprinting in model weights"
created: 2026-11-13
updated: 2026-11-13
type: concept
tags: [weight-provenance, us-china-ai-race, export-controls, ai-supply-chain-security, model-attestation, chip-design, ai-infra-security, geopolitics, reverse-engineering]
sources:
  - raw/articles/2026-11-13_unemploymentlabs_checkpoint-forensics-blackwell-fingerprint.md
  - "https://news.ycombinator.com/item?id=50474883"
confidence: medium
---

# Checkpoint forensics: GPU-architecture fingerprinting in model weights

"Checkpoint forensics" (Unemployment Labs, Nov 12, 2026) is a method that reads the
**GPU architecture a model was trained on directly out of the released weights**, by
matching seed-initialization and tensor-layout artifacts left by the accelerator's
processor-core count. HN 307pts/114c. The technique matters more than any single finding:
it turns "which chips did this lab have?" from an unverifiable claim into a measurable
property of a public artifact.

## How it works

NVIDIA's Blackwell classes have distinct streaming-multiprocessor counts — 148 SMs for
B200/B300, 152 SMs for GB200/GB300 — and those counts leak into the numerical structure of
checkpoint initialization. Matching a candidate model against roughly 6 trillion
seed-and-layout combinations yields a statistical match strength the authors report as
**49 to 1,385 sigma** per model, against a ~8-sigma expected chance maximum for the same
search space. The weakest individual test reported is 20 sigma. Hopper is a known blind
spot: H800, H100 SXM and H200 share one fingerprint, so Hopper-era identifications in the
paper rest on lab disclosures rather than the method.

Validation: on the 24 models whose hardware developers publicly disclosed, the method
agrees every time — including NVIDIA's own Nemotron-3 Ultra, whose technical report names
GB200 for one training phase and which reads as 152 SMs, the same as Kimi K3.

## Findings

Six models from four Chinese labs read as Blackwell-trained: DeepSeek-V4-Flash and
MiniMax-M3 (B200/B300); DeepSeek-V4-Pro, Kimi K3, Kimi K3.1-Pro and Ling-3.1-flash
(GB200/GB300). Every one of these requires a US export license for China and none has been
reported granted.

The transition dates are sharp: DeepSeek reads Hopper through DeepSeek-V3 (Dec 2024) and
Blackwell from V4 (Apr 2026); Moonshot Hopper through Kimi K2.5 (Jan 2026) and Blackwell
from K3 (Jul 2026); MiniMax flips at M3 (Jun 2026); Ant Group's Ling flips between 3.0
(Aug 2026) and 3.1 (Oct 2026). Kimi K2.7-Code sits in between — Hopper-era weights with a
B200/B300-matching component, posted six weeks before K3. Kimi K3.1-Pro starts from K3's
seed and may just be a further-post-trained K3 checkpoint.

Not all Chinese labs switched: the newest readable models from Alibaba (Qwen), Zhipu (GLM),
Tencent, Xiaomi and StepFun all read as Hopper-trained, and Meituan's LongCat-2.0 (claimed
"AI ASIC superpods") shows no NVIDIA fingerprint at all.

Scale estimates from model size plus training data: Kimi K3 and DeepSeek-V4-Pro each needed
thousands of Blackwell GPUs for two to three months (best estimates ~4,500 and ~3,000,
i.e. ~11,500 and ~7,500 H100-equivalents); ~12,000 Blackwell GPUs across the five runs. At
the ~$70k/GPU price implied by WSJ's reporting on ByteDance's 36,000-chip Malaysia
deployment (~$2.5B), the largest cluster is $200–300M and the five together exceed half a
billion dollars.

## Limits the authors state, and limits the thread adds

The paper is explicit that this is **technical evidence of access to advanced compute, not
evidence of a violation** — it does not establish where the chips sat, how access was
obtained, or whether export controls were broken. Training in a third-country data centre
operated for a Chinese customer is legal; chips inside China are legal to possess. AMD
hardware is the only other restricted route identified and is excluded for
DeepSeek-V4-Flash, considered very unlikely for the rest.

The thread adds three objections worth keeping:

- **Method robustness.** liuliu (a credible name on this) is unsure how robust the
  fingerprint is independent of a PyTorch implementation quirk, noting parallel Philox-based
  PRNG design is a well-studied area and finding this class of leakage surprising.
- **Policy futility vs price effect.** The dominant exchange is the export-controls debate:
  "never effective, huge grey-market reseller chain" (saidnooneever) against "controls raise
  cost and force the other side to spend or forgo" (wmchen) and "against a near-peer there is
  no price too high" (overfeed). LarsDu88's "banning raises the price, that alone justifies
  it" gets pushed back on by AnthonyMouse: if the fix is putting someone else's name on a
  form, the price rises by an amount that rounds to zero while your own firms eat the
  compliance cost.
- **Toleration hypothesis.** Several commenters float that Washington may have tolerated the
  flows knowingly (cadamsdotcom's thought experiment; schainks and taylorfinley on the
  Huang/Trump episode and the reported $25M ballroom gift). This is speculation layered on
  the technical result and should be treated as such.

## Why it matters

Export-control policy has historically been evaluated on shipment data, which is exactly the
layer grey-market intermediation defeats. A weight-level fingerprint bypasses that layer: it
answers what hardware *produced the artifact* regardless of who signed the paperwork. That
makes it a candidate tool for frontier-model monitoring and for AI supply-chain assurance
alongside model cards and provenance attestation — with the caveat that it is currently a
single non-peer-reviewed source with a strong policy agenda, no vendor response, and an
unresolved question about whether the signal is a genuine hardware property or an
implementation artifact.

## Related

- [[concepts/us-china-ai-competition]]
- [[concepts/china-mofcom-announcement-48-export-controls]]
- [[concepts/cuda-moat]]
- [[concepts/weight-provenance]]

## Sources

- https://unemploymentlabs.com/checkpoint-forensics (fetched, saved to raw)
- HN discussion: https://news.ycombinator.com/item?id=50474883
