# X-accounts-scan addenda (verified 2026-11-01 run)

Condensed from the 2026-10-31/11-01 x-accounts-scan cron run. Complements
`references/x-accounts-scan-cron.md` (which remains the primary procedure doc).

## Fiction / creative works on tech-blog domains

A personal-blog post linked from a scan tweet is NOT always an essay — it can be a long
speculative SHORT STORY (this run: Kyle Corbitt's "The Machine Starts", ~56k chars on
corbt.com, framed with a Nick Bostrom epigraph, free epub). Still worth a raw article.

- Scrape with the generic curl + `<main>`/`<article>` tag-strip recipe.
- **Slice beyond the head**: print the head (~4k), a MIDDLE slice (e.g. `t[25000:29000]`),
  and the END (`t[-3000:]`). Long-form fiction puts the payoff/thesis in the coda; the
  first 4k chars are scene-setting only.
- Capture: pub date, epub availability, epigraph, main plot beats, thesis line(s), and the
  **quoted-tweet context**. A fiction amplify often quotes an empirical study on the same
  theme (here: Alex Tamkin's Anthropic randomized trial with 50 data analysts vs Corbitt's
  story about AI beating experts on all 78 regulated decisions). Name that
  fiction-vs-empiricism pairing explicitly in both the raw file and the entity section —
  it is the durable insight, not the plot summary.

## Model-release tweets: check for an existing base-release page first

Before creating an event page for a model-release tweet,
`grep -rn "<model-slug>" wiki/index.md wiki/events wiki/entities` — the base release usually
already has an event/concept page (this run: NVIDIA NVFP4 quant of DeepSeek-V4.1-Flash-1017
linked back to `events/2026-10-17-deepseek-v4.1-flash-1017-release`, and concepts
`deepseek-v4`, `deepseek-v4-serving`, `nvidia-blackwell-architecture` all existed).

- A new **vendor quant** of an existing model = its own small event page, cross-linking the
  base release + serving/architecture concepts, with an index entry and Events count bump.
- Record the HF Hub-listed parameter count / modality tag verbatim (e.g. "Image-Text-to-Text,
  665B") and the "day-N after base checkpoint" framing.
- If the model card wasn't scraped, set `confidence: medium` and add a Caveats section saying
  benchmark deltas vs BF16/MXFP4 are pending — don't present the Hub tag as verified card data.
- NVFP4 (Blackwell/SM100-native, vendor-shipped) vs MXFP4 (DeepSeek's own QAT) is a durable
  distinction worth stating on such pages.

## Decision-model application posts (van Strien pattern)

Daniel van Strien (@vanstriendaniel) posts often bundle (a) an open model/data release with a
GitHub recipe repo and (b) a HF Space demo applying a small decision model. Both scrape well:

- GitHub recipe READMEs: the standard `<article>` regex recipe yields the full how-to
  (commands, hardware flags, throughput/cost numbers). Capture the exact cost/speed claims
  (e.g. "1,020,000 FineWeb pages in ~19 min / ~$5 on HF Jobs") — those are the quotable facts.
- When a Space demo uses another tracked org's model (e.g. Liquid AI d1-2B in the Prelinger
  moments Space), write a "in the wild" paragraph on the MODEL's entity page too, not just the
  author's — cross-linking both directions is what makes the graph useful.
- His HF Jobs demos (Unlimited-OCR-2 etc.) are thin reply-followups: a dated bullet in his
  entity "Recent X Activity" is enough; no raw file needed when the payload is just a script link.

## Reply-thread workflow descriptions are worth full capture

Ankur Goyal's 6-step Pattern→synthetic-eval→coding-agent-fix loop arrived as a truncated
`replied_to` reply. The xurl direct-ID fetch recovered the full numbered list (truncation point
was mid-sentence at "Ask coding agent"). Rule: when a reply from a founder/CEO enumerates a
workflow, always fetch the full text — the step list IS the content even though engagement is
low (5 likes). Position it against existing concept pages (here
`concepts/evaluation/evals-vs-monitoring-debate`, `concepts/active-observability`).

## Tag pre-checks that passed cleanly (2026-11-01)

Whole-file `grep -oE "(^|, )$t(,|$)" wiki/SCHEMA.md` confirmed valid: `nvidia`,
`announcement`, `open-source`, `deepseek`, `quantization`, `inference`, `liquid-ai`, `ocr`,
`datasets`, `evaluation`, `agent-evaluation`, `multimodal`, `retrieval`, `huggingface`, `llm`,
`small-language-model`, `decision-model`. NOT valid: bare `model` (use `llm` /
`small-language-model` / other specific tag — though some old pages still carry `model` in
frontmatter, a NEW page adding it may be blocked; prefer specific tags).
