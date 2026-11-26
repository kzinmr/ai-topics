---
title: "Complexity-Theory AI Breakthrough Wave (November 2026)"
created: 2026-11-26
updated: 2026-11-26
type: concept
tags:
  - mathematics
  - complexity-theory
  - openai
  - anthropic
  - cryptography
  - post-quantum-crypto
  - ai-research-automation
  - ai-safety
  - lab-rumors
  - integer-factorization
confidence: medium
sources:
  - raw/articles/2026-11-25_scottaaronson_holy-shit-magnitude-of-what-is-happening.md
  - raw/articles/2026-11-26_google_cogentic-research-papers.md
  - "https://news.ycombinator.com/item?id=50646108"
  - "https://news.ycombinator.com/item?id=50643065"
  - "https://news.ycombinator.com/item?id=50648050"
  - "https://github.com/lsernau/grh-lean"
related:
  - concepts/openai/formal-math-publication-2026
  - concepts/openai-math-preprint-race
  - concepts/ai-mathematics-theorem-proving
  - concepts/google-cogentic-proof-discovery
  - concepts/academic-reception-of-ai-math
---

# Complexity-Theory AI Breakthrough Wave (November 2026)

In the last week of November 2026 a run of AI-generated results landed on problems that had been open
for fifty years, and Scott Aaronson's 2026-11-25 post "HOLY SHIT HOLY SHIT HOLY SHIT HOLY SHIT" (HN
1627 pts / 1437 comments — the largest AI thread of the month) is the document that frames the moment.
Unlike the October bulk-publication story ([[concepts/openai/formal-math-publication-2026]]), the
distinguishing feature here is **lower bounds**: results of a shape most complexity theorists did not
believe an AI would produce.

## The results, as claimed

| Result | Claimant | Why the shock is the *shape*, not the value |
|---|---|---|
| omega = 9/4 exactly (matrix multiplication exponent) | OpenAI | The value being a rational number is surprising; **a matching lower bound (omega > 2)** is the part Aaronson "never expected ... to be much easier than P != NP." Strassen's omega < 3 stood since the late 1960s. |
| VP != VNP | OpenAI and Anthropic (separately) | Algebraic circuit lower bound; OpenAI claims it solved the separation *before* Anthropic ([[concepts/openai-math-preprint-race]]) |
| Linear gates for the Fourier Transform = N (log N)^(1/2 + o(1)) | OpenAI | Beats O(N log N) standing since the 1960s **and** OpenAI's own October bound, again with a matching lower bound |
| Riemann Hypothesis (Lean) | Alpöge + Anthropic; shortened re-verification by lsernau | Shorter-version re-proof hit 472 pts (HN 50648050) |
| QIP(2) = PSPACE | Yupan Liu (arXiv preprint, AI-assisted) | Would have been a top-complexity-result-of-the-year in 2025; the AI use was treated as secondary |

Aaronson's own framing of the regime change: "All these questions from the ancient days are now just
getting ... straight-up answered, rather than slowly illuminated with a drip-drip-drip of clues." He
also notes being vindicated on a decade-old disagreement — colleagues "express extreme confidence that
omega = 2" while he "saw that there was no strong argument for omega = 2 either."

## The cryptography rumor, and how the thread handled it

The passage that drove coverage: "some of those algorithms will break currently deployed cryptosystems
... yes, I'm virtually certain, from multiple reliable sources, that the AI labs are now sitting on one
or more bombshells in that area." Aaronson immediately limited it — no details, refuses to specify the
nature, worries "exact statements of what was done may have been mangled in a game of Telephone," and
explicitly declines to feed the ECDSA-Bitcoin-wallet reading.

A Reddit-sourced rumor that a lab had "cracked Factoring in P" independently reached 492 pts
(HN 50643065). Aaronson's own blog comment, quoted as the rumor's primary source: "I've now heard many,
many rumors that one or both labs are sitting on Factoring in P. I don't know how much to credit this."

The thread's objections are the durable part of the record:

- **Classification argument** — stackghost: a cryptographically relevant breakthrough would be
  forcibly classified, "the same way the NSA had IBM keep differential cryptanalysis under wraps in the
  70s," which makes the leak-to-a-random-blogger version implausible.
- **Scope argument** — xoa: "Cryptography" cannot "break" in the flat sense; one-time pads are outside
  the question and symmetric ciphers are subject to little beyond Grover. "All present commonly used PKI
  breaking would be a tremendous PITA with a lot of dangerous, downstream consequences" — real, but a
  bounded engineering problem.
- **Proof-vs-attack argument** — maxrecursion: "Solving proofs is completely different from having
  actually broken crypto in real life," plus a direct prior-art warning that past quantum-crypto
  scares were "complete over-hyped BS."
- **Constructivity argument** — sedictious: even a constructive P=NP could be computationally
  infeasible to use; lowered lower bounds "guide the future of cryptography without necessarily meaning
  that we will be able to factor primes efficiently."
- **Credibility discount** — negura: Aaronson "has been spreading FUD about cryptography breaking for a
  long time," and it has already redirected taxpayer research money.
- **Tone** — SoftTalker reduced the whole post to one line: "'I do not wish to be responsible for
  spreading unverified rumors.' Titles blog post 'HOLY SHIT HOLY SHIT HOLY SHIT HOLY SHIT'."

Against the skeptics there is one concrete data point: Anthropic factored RSA-896 in September using
**existing** methods and publicly stressed it found no faster algorithm
(https://saweis.net/posts/rsa-896.html). That establishes interest and compute commitment, not a
breakthrough. See [[concepts/google-cogentic-proof-discovery]] for the vlovich123 cost accounting that
shows why a subexponential guarantee is nowhere near a practical factoring attack, and
[[concepts/cryptographic-capability-concealment]] for the symmetric case where labs can *hide* a
capability rather than publish it.

## Verification status as of 2026-11-26

- No independent verification of the November OpenAI preprints (same gap flagged for the
  omega = 9/4 and VP != VNP drops in [[concepts/openai-math-preprint-race]], on a channel whose
  October cohort lost 3 papers and required 14 repairs within 24 hours).
- The GRH proof is the best-supported: within a week of Alpöge's announcement there were three
  expositions of the proof's structure, two posted to GitHub, and a substantially shorter Lean
  re-verification (Ernest Davis: "The proofs don't seem to be beyond human ken, validated by Lean but
  utterly mysterious, as some of the early reactions breathlessly claimed").
- The Google Cogentic batch is reported human-reviewed but has no Lean formalization.

## Why this page exists separately from the benchmark story

Two claims that look identical in headlines carry different epistemic weight, and the last six weeks
make the distinction operational rather than philosophical:

1. **Machine-checkable claims** (Lean-verified GRH) accumulate independent reconstruction quickly.
2. **Narrative claims** (a lab "sitting on" a crypto break) accumulate nothing, cannot be checked, and
   propagate through screenshot-mediated channels (Reddit -> X -> blog comment -> blog post).

Aaronson's own post is a hybrid: (1) for the published results, (2) for the rumor. Reporting that
treats them as one story overstates the second. The honest position on 2026-11-26: the complexity
results are a genuine, verifiable inflection in automated mathematics; the cryptographic emergency is
an unfalsifiable rumor with a credentialed amplifier.

## Open questions

- Does the "Euclidean geometry in the asymptotic spectrum of tensors" framework unify omega = 9/4,
  superpolynomial permanent circuit lower bounds, and the Erdos-Rado sunflower conjecture — i.e. is
  there one new tool rather than many results (Philip, on the Aaronson thread)?
- Is the readability improvement ("becoming actually readable, as opposed to the messy AI slop of the
  previous waves") real, or selection on introductions? Aaronson has read intros only; Aaron Rotenberg
  still calls the OpenAI papers "proofslop."
- Would a deployed cryptosystem-breaking algorithm be released, classified, or quietly held? The
  classification argument says classified; the Hugging Face / public-repo publication culture of these
  labs says otherwise.
- Aaronson's closing hope — that this is "merely" a singularity "for our little corner of the world
  that involves hard math problems" — is the load-bearing assumption, and nothing in the thread tests
  it.

## Related

- [[concepts/openai/formal-math-publication-2026]] — the October industrial-scale Lean program
- [[concepts/openai-math-preprint-race]] — the lab-vs-lab priority dispute and its verification gap
- [[concepts/ai-mathematics-theorem-proving]] — the Lean / autoformalization arc, incl. Alpöge GRH
- [[concepts/google-cogentic-proof-discovery]] — the multi-agent harness and the factoring reality check
- [[concepts/academic-reception-of-ai-math]] — mathematician backlash and the AHM statement
