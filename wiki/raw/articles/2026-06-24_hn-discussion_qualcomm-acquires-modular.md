---
title: "Qualcomm to Acquire Modular — HN Discussion"
source: "hn-algolia"
source_url: "https://news.ycombinator.com/item?id=48659798"
external_url: "https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/"
hn_points: 238
hn_comments: 125
date: 2026-06-24
date_ingested: 2026-06-27
type: raw_article
tags: [acquisition, qualcomm, modular, mojo, max, ai-infrastructure]
---

# Qualcomm to Acquire Modular

## Source
- URL: https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/
- HN Points: 238
- HN Comments: 125

## Context
Qualcomm announced the acquisition of Modular, the AI infrastructure startup co-founded by Chris Lattner (LLVM, Swift) and Tim Davis, known for the Mojo programming language and MAX AI platform. The deal signals consolidation in the AI infrastructure space as major chipmakers seek to integrate software stacks.

## HN Discussion Highlights
### roflcopter69
Tbh, Modular getting acquired happened sooner than I would have expected, if ever. Don&#x27;t know how to feel about this one.<p>Also so many mixed feelings about Mojo, the programming language powering Modular. Of course Chris Lattner is free to pursue whatever he wants, his many contributions to tech will always be highly regarded, but to me it feels as if he &quot;wasted&quot; lots of his precious mental capacity on making Mojo a python-like language instead of trying to come up with something better from first principles. I know, the promise of Mojo eventually being a Python superset has been taken back, which I think is the right move, and I understand why Mojo&#x27;s initial motivation for being close to Python was to attract ML folks, but I&#x27;m getting counterfactual regret just 

### melodyogonna
Qualcomm has acquired excellent engineering talent here, the infrastructure I&#x27;ve seen Modular build in the 3 years I&#x27;ve followed the company is insane.

### melodyogonna
Related, Reuters reported the deal a few days ago, valued at $4b: <a href="https:&#x2F;&#x2F;www.reuters.com&#x2F;legal&#x2F;transactional&#x2F;qualcomm-nearing-deal-ai-chip-startup-modular-bloomberg-news-reports-2026-06-22&#x2F;" rel="nofollow">https:&#x2F;&#x2F;www.reuters.com&#x2F;legal&#x2F;transactional&#x2F;qualcomm-nearing...</a>

### bobajeff
It&#x27;s kind of funny that Modular is getting acquired by a hardware company considering what it&#x27;s founder has said repeatedly in interviews and articles about how those companies fail to make AI stacks.<p>* <a href="https:&#x2F;&#x2F;www.modular.com&#x2F;blog&#x2F;democratizing-ai-compute-part-9-why-do-hw-companies-struggle-to-build-ai-software" rel="nofollow">https:&#x2F;&#x2F;www.modular.com&#x2F;blog&#x2F;democratizing-ai-compute-part-9...</a>

### bit_economist
It&#x27;s interesting that acquire.fyi data shows tech M&amp;A deal volume is down 11% year to date, but total deal value is up 40%. So, fewer deals are closing in tech, but the deals that are closing are much larger. I wish we had the deal value for this one.

### samuell
As a meta comment, I&#x27;m surprised such a news is not reaching the frontpage already.

### revengerwizard
Oh, that is unexpected... I tried applying for a position at Modular a few days ago.

### ssivark
Qualcomm seems to be assembling a whole portfolio of technologies&#x2F;products aimed at<p>1. Moving beyond ARM to RISC-V<p>2. Being competitive for AI&#x2F;could needs instai of just chips for phones and other edge devices.<p>Interesting to see bold and high-conviction moves in this direction. Tenstorrent, Modular, Ventana, Alphawave, etc.

### WhereIsTheTruth
Of all possible acquirers, Qualcomm is the worst outcome for Mojo, rip

### semiinfinitely
latty gotta get his baggy

### YuechenLi
I honestly think Mojo would be better served if it is just a high-level language for GPU programming that compiles down to PTX with clear Python&#x2F;Rust interop boundaries instead of trying for the &quot;one language, multiple computational model&quot; thing that they seem to be going for. The programming model between CPU and GPU programming is very different: code that runs best on CPU with heavy branching behaviors should not be written the same way as massively parallel matrix multiplication oriented GPU code, which I think they will be forced to do in the MLIR level anyway.<p>So, you end up with a language that looks like Python, but doesn&#x27;t behave like Python, and companies that adopt Mojo early with the promise of Python compatibility may find themselves running into edge cas

### dwa3592
Has anyone used mojo&#x2F;modular extensively in their work? I installed it as soon as it was available but never went past the toy examples.

### maxloh
I don&#x27;t get it.<p>Qualcomm has almost no products in the high-end inference&#x2F;training market. The industry standard is the NVIDIA Hopper H100&#x2F;H200.<p>What could they possibly get from acquiring Modular?

### fishgoesblub
Welp, I think I can give up on my hope for Mojo.

### markkitti
Yesterday, LineShine a supercomputer in China emerges as #1 in the Top500 using ARM v9 based chips and no GPUs. Today, Qualcomm a premier designer of ARMv9 licensed chips in the United States acquires Modular, who has been creating a compiler stack that provides an alternative to NVIDIA&#x27;s CUDA stack.<p>Are you ready for Qualcomm ARMv9 powered inference running Mojo&#x2F;MAX written kernels doing low-cost inference at scale for AI?

