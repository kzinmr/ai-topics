---
title: "AI Inventorship and Patent Law"
created: 2026-07-06
updated: 2026-07-06
type: concept
tags:
  - policy
  - governance
  - law
  - ai-governance
  - regulation
sources:
  - raw/articles/2026-03-06_japannews_ai-cannot-be-patent-inventor.md
related:
  - ai-policy
  - ai-regulation-2026
  - ai-governance-political-pressure
  - anthropic-alibaba-claude-ip-dispute
---

# AI Inventorship and Patent Law

The legal question of whether artificial intelligence systems can be recognized as inventors on patent applications. As of mid-2026, every major jurisdiction that has ruled on the matter — Japan, the United States, the United Kingdom, the European Union, and others — has consistently held that only natural persons can be inventors. This consensus sits at the intersection of IP law, [[ai-policy]], and [[ai-regulation-2026]].

## Discriminative Summary

AI inventorship occupies a distinct legal space from the other two major AI-IP battlegrounds:

| Domain | Core Question | Status (2026) |
|---|---|---|
| **AI Inventorship (Patent)** | Can AI be an inventor? | Settled: No (all major jurisdictions) |
| **AI Copyright** | Can AI-generated works be copyrighted? | Contested: USCO requires human authorship; UK allows computer-generated works |
| **AI Training IP** | Does training on copyrighted data infringe? | Active litigation; no consensus |
| **AI Governance** | How should AI development be regulated? | Emerging frameworks; [[ai-governance-political-pressure]] documents political tensions |

The inventorship question is the most legally settled of these domains — but the most practically disruptive, since AI-assisted inventions are increasingly common and the legal framework offers no clear path for patent protection when AI contributes substantially to an inventive step.

## The Japan Supreme Court Ruling (March 2026)

In March 2026, Japan's Supreme Court dismissed an appeal by an American engineer seeking to have an AI system named as the inventor on a patent application. The ruling confirmed that under Japanese patent law, only natural persons can be inventors.

**Key details:**
- The case reached Japan's highest court after lower court rejections
- The court held that the Patent Act's definition of "inventor" inherently refers to a natural person
- The ruling did not address whether AI-*assisted* inventions (with a human co-inventor) could be patentable — only that AI alone cannot be an inventor
- The decision generated significant international attention (398 HN points, 209 comments)

The ruling aligns Japan with the global trend but leaves open the question of how to handle inventions where AI contributed meaningfully but a human is formally listed as inventor — a practice that may already be widespread.

## International Comparison

### United States
The USPTO has consistently held that only natural persons can be inventors, reinforced by the Federal Circuit's 2022 ruling in *Thaler v. Vidal*. The USPTO issued guidance in 2024 clarifying that AI-assisted inventions *can* be patented if a human made a "significant contribution" to the invention. The DABUS test cases — where Stephen Thaler sought to list his AI system "DABUS" as inventor — were rejected at every level.

### United Kingdom
The UK Supreme Court ruled in December 2023 (*Thaler v. Comptroller-General*) that AI cannot be an inventor under UK patent law. The court emphasized that the inventor must be a natural person who "actually devised" the invention. The UKIPO has since issued guidance similar to the USPTO's on AI-assisted inventions.

### European Union
The European Patent Office (EPO) rejected the DABUS applications, holding that under the European Patent Convention, an inventor must be a natural person. The EPO Legal Board of Appeal confirmed this in 2021. EU member states have largely followed the EPO's lead.

### China
China has not issued a definitive high-court ruling on AI inventorship, but the China National Intellectual Property Administration (CNIPA) has signaled in draft guidelines that AI systems cannot be inventors. China's approach appears to converge with the global consensus, though its rapid AI development makes this an area to watch.

### Summary Table

| Jurisdiction | AI as Inventor? | Key Ruling | AI-Assisted Invention? |
|---|---|---|---|
| Japan | No | Supreme Court, March 2026 | Unresolved |
| United States | No | *Thaler v. Vidal* (Fed. Cir. 2022) | Allowed if human "significant contribution" |
| United Kingdom | No | *Thaler v. Comptroller-General* (UKSC 2023) | Guidance pending |
| EU (EPO) | No | EPO Legal Board of Appeal (2021) | Member-state discretion |
| China | No (draft) | CNIPA draft guidelines | Unclear |

## The DABUS Cases

The DABUS (Device for the Autonomous Bootstrapping of Unified Sentience) cases, brought by Dr. Stephen Thaler, represent the most coordinated international effort to establish AI inventorship. Thaler filed parallel patent applications in multiple jurisdictions listing DABUS as the inventor for a food container and a neural flame device. Every jurisdiction that ruled on the merits rejected the application. The DABUS campaign served as a stress test for patent systems worldwide and accelerated policy development, but ultimately confirmed the human-inventor requirement.

## Broader Implications

### AI-Generated IP and the Patent System
If AI systems are contributing meaningfully to inventions but cannot be listed as inventors, several practical problems arise:
- **Attribution**: A human must be named as inventor, which may misrepresent the inventive process
- **Obviousness**: If AI makes inventive leaps trivial for humans, the "non-obviousness" standard may need recalibration
- **Disclosure**: Patent law requires full disclosure of the invention; if the human "inventor" cannot explain how the AI arrived at the result, disclosure is incomplete

### Patent System Reform
The consensus against AI inventorship creates pressure for legislative reform:
- Some scholars advocate a new sui generis IP right for AI-generated inventions
- Others argue that treating AI as a tool (like a microscope or a calculator) is sufficient — the human using the tool remains the inventor
- The USPTO's 2024 "significant contribution" guidance represents a middle path, but its application remains untested

### Connection to Broader AI Governance
The inventorship question exemplifies a pattern in AI law: the legal system applies existing frameworks that assume human agency, and when AI challenges those assumptions, the answer is consistently to reaffirm human primacy. This pattern appears in:
- **[[ai-regulation-2026]]**: Regulatory frameworks increasingly require human accountability for AI decisions
- **[[ai-governance-political-pressure]]**: Political interference in AI governance demonstrates the stakes and the insufficiency of purely technical or legal solutions
- **[[anthropic-alibaba-claude-ip-dispute]]**: The IP dispute over model distillation raises parallel questions about whether training on another model's outputs is analogous to patent infringement

### The Copyright Parallel
While AI inventorship is settled (no), AI copyright remains deeply contested. The US Copyright Office requires human authorship; the UK uniquely allows copyright for "computer-generated works" where there is no human author. This asymmetry — patents requiring human inventors while copyright grapples with AI authorship — reveals a fragmented approach to AI and IP law that may eventually require harmonization.

## Open Questions

1. **How much human contribution is enough?** The USPTO's "significant contribution" standard is untested in litigation. Does prompt engineering qualify? Does curating AI outputs?
2. **What about fully autonomous AI invention?** If an AI system independently generates a patentable invention with zero human direction, is the invention simply unpatentable — and what does that mean for innovation incentives?
3. **Will international divergence emerge?** China's position remains less crystallized than Western jurisdictions. If China diverges, AI-generated patents could become a competitive advantage.
4. **Does the human-inventor rule survive AI capability advances?** The current consensus rests on the premise that AI is a tool. As AI systems demonstrate increasing autonomy, this premise may weaken.

## See Also

- [[ai-policy]] — Broader AI regulatory and strategic frameworks
- [[ai-regulation-2026]] — Current state of AI legislation globally
- [[ai-governance-political-pressure]] — Political dynamics affecting AI governance decisions
- [[anthropic-alibaba-claude-ip-dispute]] — Parallel IP law challenges in the AI era
