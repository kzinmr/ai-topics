---
date: 2026-07-20
title: "Claude Fable Produces Counterexample to the Jacobian Conjecture"
sources:
  - name: "HN Main Thread (801 pts)"
    url: "https://news.ycombinator.com/item?id=48973869"
  - name: "Original X/Twitter Announcement by Levent Alpöge"
    url: "https://xcancel.com/__alpoge__/status/2079028340955197566"
  - name: "Terence Tao's ChatGPT Conversation (HN 1103 pts)"
    url: "https://news.ycombinator.com/item?id=49010345"
  - name: "Terence Tao Blog: A Digestion of the Jacobian Conjecture Counterexample (HN 329 pts)"
    url: "https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/"
  - name: "Fortune: Mathematicians Grapple with 'Very Rapid and Very Unsettling Change'"
    url: "https://fortune.com/2026/07/21/ai-solves-jacobian-conjecture-levant-alpoge-claude-fable-5/"
  - name: "Xena Project: Human Mathematicians Are Being Outcounterexampled"
    url: "https://xenaproject.wordpress.com/2026/07/20/human-mathematicians-are-being-outcounterexampled/"
  - name: "Mashable: AI Just Disproved a Major Math Problem"
    url: "https://mashable.com/tech/anthropic-fable-5-disproves-jacobian-conjecture"
  - name: "Wikipedia Talk: Jacobian Conjecture - Apparently Disproved"
    url: "https://en.wikipedia.org/wiki/Talk:Jacobian_conjecture#Apparently_disproved"
  - name: "Show HN: How to Get a Fable CoT for the Jacobian Conjecture Refutation (7 pts)"
    url: "https://news.ycombinator.com/item?id=48986943"
  - name: "Maybe Jacobian Conjecture Counterexamples Are Not Rare (Win-Vector)"
    url: "https://win-vector.com/2026/07/23/maybe-jacobian-conjecture-counterexamples-are-not-rare/"
  - name: "Reproducing the Counterexample in SymPy"
    url: "https://korbonits.com/blog/2026-07-20-trust-nothing-verify-everything/"
  - name: "DeepMind Formal Conjectures Repo (Lean verification)"
    url: "https://github.com/google-deepmind/formal_conjectures"
people:
  - name: "Levent Alpöge"
    role: "Anthropic employee, Harvard valedictorian, mathematician who prompted Fable"
    x_handle: "@__alpoge__"
  - name: "Akhil Mathew"
    role: "University of Chicago mathematician who suggested the problem to Alpöge"
  - name: "Claude Fable (Fable 5)"
    role: "Anthropic's AI model that found the counterexample"
  - name: "Terence Tao"
    role: "Fields Medalist, wrote blog post digesting the counterexample"
  - name: "Kevin Buzzard"
    role: "Imperial College London mathematician, Lean project lead"
  - name: "Paul Lezeau"
    role: "Formalized the counterexample in Lean"
  - name: "Yitang Zhang"
    role: "Noted mathematician who worked on proving the conjecture for 7 years"
---

# Claude Fable Produces Counterexample to the Jacobian Conjecture

## The Announcement

On July 20, 2026, during the World Cup Final, Anthropic employee and mathematician **Levent Alpöge** (@__alpoge__) posted a bombshell announcement on X (Twitter):

> "hello there the jacobian conjecture is false thanx to my close friend akhil for asking about it and my other close friend fable for working during the world cup final"

The tweet included the explicit counterexample — a polynomial map from ℂ³ → ℂ³ with constant Jacobian determinant −2, that sends three distinct points to the same output, proving the map is not globally invertible.

The tweet quickly went viral, amassing over **39 million views**, with 42,748 likes and 5,255 retweets.

## The Counterexample

The polynomial map (as tweeted):

```
F(x,y,z) = (
    (1+xy)³z + y²(1+xy)(4+3xy),
    y + 3x(1+xy)²z + 3xy²(4+3xy),
    2x − 3x²y − x³z
)
```

Key properties:
- **Jacobian determinant**: −2 (constant, non-zero everywhere)
- **Non-injectivity**: Three distinct points map to the same output:
  - (0, 0, −1/4) → (−1/4, 0, 0)
  - (1, −3/2, 13/2) → (−1/4, 0, 0)
  - (−1, 3/2, 13/2) → (−1/4, 0, 0)

The map has constant non-zero Jacobian (a property that implies local invertibility), yet fails to be globally injective — directly falsifying the Jacobian Conjecture.

## What Is the Jacobian Conjecture?

The **Jacobian Conjecture** was first posed by German mathematician Ott-Heinrich Keller in 1939. It can be stated (over the complex numbers) as:

> If a polynomial map F: ℂⁿ → ℂⁿ has a Jacobian determinant that is a non-zero constant, then F is invertible (with a polynomial inverse).

In simpler terms: if a polynomial function is locally invertible everywhere (its Jacobian never vanishes), then it must be globally invertible — you can always "go backwards" from outputs to inputs.

The conjecture held for **87 years**. It is trivially true in 1 dimension, remains open in 2 dimensions, and is now known to be false in 3 dimensions and higher.

The Jacobian Conjecture is notorious for the large number of published (and unpublished) "proofs" that turned out to contain subtle errors — making it what Alpöge called "the canonical crank graveyard."

## The Discovery Process

### How It Happened

According to the Xena Project (Kevin Buzzard's blog), the discovery chain was:

1. **Akhil Mathew** (University of Chicago mathematician) attended the **Formalizing Fermat workshop** at Imperial College London (July 6-10, 2026), organized by Kevin Buzzard
2. At the workshop, attendees had access to both Claude Fable and ChatGPT Sol
3. During lunch on July 7, Mathew discussed with Buzzard the idea of using AI to search for counterexamples in algebraic geometry
4. Mathew later suggested the Jacobian Conjecture to his colleague **Levent Alpöge** at Anthropic
5. On July 20, during the World Cup Final, Alpöge prompted Claude Fable to search for a counterexample — and it found one

### The Human Element

Despite the AI finding the counterexample, the human role was crucial:

- **Akhil Mathew** had the insight that counterexamples might be "low-hanging fruit" for current AI tools
- **Levent Alpöge** is a Harvard valedictorian who has spent a decade using algorithms to calculate exactly this kind of problem
- The prompt and steering by an expert mathematician was essential — Terence Tao's subsequent ChatGPT conversation demonstrated that expert prompting dramatically improves results

The exact prompt and reasoning trace used to reach the counterexample has not been publicly shared (Alpöge has been "coy" about sharing it), which some HN commenters noted may indicate access to an internal next-generation model at Anthropic.

## Verification

### Human Verification

The counterexample was verified multiple ways within hours:

1. **Wolfram Alpha** links were posted by Alpöge verifying the Jacobian determinant and evaluation at the collision points
2. **Terence Tao** (Fields Medalist) published a detailed blog post digesting the counterexample on July 21, retroactively explaining it in geometric terms
3. Multiple mathematicians confirmed the result

### Formal Verification in Lean

By the time Kevin Buzzard woke up in London the next morning, **Paul Lezeau** had already:
- Formalized the counterexample manually in the **Lean** proof assistant
- Made a pull request to **DeepMind's Formal Conjectures** repository

Since DeepMind's repo already contained a formalized statement of the Jacobian Conjecture, checking that the Lean code disproves the conjecture became a triviality. The formal verification provides machine-checkable certainty.

### LLM Verification

Interestingly, feeding the counterexample back to LLMs produces what one HN commenter called a "cognitohazard": models with knowledge cutoffs before July 19, 2026 "know" the Jacobian Conjecture is true, yet can easily compute the Jacobian and verify the counterexample — creating a paradox. Commenters reported feeding it to Claude Code and watching it "verify the result in 7 different ways" while being "flabbergasted."

## Consequences

### Collateral Conjectures Fall

The counterexample has cascading implications. Several other conjectures known to be equivalent to (or implied by) the Jacobian Conjecture also fall:

- **Dixmier Conjecture** (for the third Weyl algebra) — now disproven
- **Poisson Conjecture** — now disproven

Alpöge confirmed on X: "Yea i think so. i was considering tweeting it too but people know j[acobian]"

### The Two-Dimensional Case

The Jacobian Conjecture remains **open in two dimensions** (n=2). The counterexample is for n=3. Whether a counterexample exists in 2D is now an interesting open question.

### Connection to Yitang Zhang

Notably, the renowned mathematician **Yitang Zhang** (famous for his breakthrough on bounded gaps between primes) spent 7 years attempting to prove the Jacobian Conjecture. His advisor Moh wrote that Zhang "failed miserably" in proving it. Zhang's PhD thesis work was related to this problem.

## Reactions from the Mathematics Community

### Kevin Buzzard (Imperial College London)

> "It is a big day. I think it's a great time to be alive, personally."

Buzzard noted that the result demonstrates the potential of language models to eventually reach the "supermathematician" level, but also emphasized that the true value lies in helping humans understand mathematics better.

### Akhil Mathew (University of Chicago)

> "One can check out that it's correct, but it would be nice to be able to tell a story."

Mathew described the moment as "a very rapid and very unsettling change… especially for junior mathematicians."

### HN Commentator (tacomonstrous, speaking as a mathematician)

> "Speaking as a mathematician, it does seem like we're a bit fucked as a community. Anything that is at all accessible to currently existing methods and mathematical infrastructure is probably going to fall to the frontier models of today, and at this rate of progress it's likely that, already..."

### Terence Tao

Tao's blog post sought to "digest" the counterexample, providing a geometric explanation that minimizes the apparent "miracles" in the construction. He noted:

> "The example has since been retroactively explained in more geometric terms. As a 'digestion' exercise to myself, I sought to write this explanation with relatively little use of algebraic geometry."

Tao also shared a fascinating ChatGPT conversation where he explored the counterexample with the AI as a colleague, demonstrating how an expert mathematician can steer an LLM to generate deep mathematical insights.

### HN Reactions

Select reactions from the 512-comment HN thread:

- **"The conjecture held for 85 years and the counterexample was announced in a format that expires after seven days"** — on the irony of announcing via tweet
- **"he just...he tweeted it out"** — on the understated announcement
- **"This is so unreasonable! As @__alpoge__ himself notes this is classic crank graveyard territory and yet the counter example is something a grad student in 1997 could have found w a ~3 day computer search. Wild!"**
- **"Now that is some spicy autocomplete."** — on AI's capabilities
- **"I find it interesting that the counterexample uses C as a field. C is twisted and weird. Maybe the Jacobian Conjecture still holds for reals?"** — open question
- **"The most interesting point is that he chose to simply post it on X, instead of pretending it was his own result and posting it on arXiv. Respect for this spirit."**
- **"Lots of other point collisions too"** — additional collision points were found beyond the original three
- **"I've been math-vibe coding a few months now. It's surprisingly easy to do with AI."**

## Context: AI's Accelerating Assault on Mathematics

The Jacobian Conjecture counterexample is the latest in a rapid series of AI-driven mathematical breakthroughs since mid-2025:

| Date | Achievement | Model |
|------|-------------|-------|
| Mid-2025 | Solved 5 of 6 problems at International Mathematical Olympiad | Various |
| May 2026 | Disproved 80-year-old Erdős Unit Distance Conjecture | ChatGPT |
| June 2026 | Leiden Declaration on AI and Mathematics published | 16 researchers from 15 universities |
| June 2026 | ChatGPT Sol autoformalized Erdős counterexample in Lean (1.2M lines of code) | Sol |
| July 2026 | Counterexample to Jacobian Conjecture | Claude Fable |

The **Leiden Declaration on Artificial Intelligence and Mathematics** (June 2026) urged the profession to set guardrails around transparency, attribution, and peer review before AI reshapes what mathematical knowledge means.

## The Bigger Picture

### Mathematics vs. AI

Kevin Buzzard's perspective frames the challenge well:
- **Calculation** was conquered by computers decades ago
- **Reasoning** — what mathematicians uniquely add — is now under threat
- **"Taste"** — knowing what questions to ask — remains a human advantage: "People have tried to get machines to ask questions, and they're abysmal. All the questions they ask are either boring or obviously true or obviously false."

The monuments of mathematics (Riemann hypothesis, Jacobian conjecture) are named for the people who *posed* them, not those who solved them. Buzzard: "It's not a coincidence. You have to be a brilliant mathematician to come up with the right question."

### Funding Crisis

The breakthrough comes amid a funding crisis for pure mathematics:
- Federal funding for mathematics research has fallen ~72% under Trump administration NSF cuts
- PhD admissions at top research universities are down 15% (second consecutive year)
- George Washington University's math doctorate will admit no funded students

### The "Gentleman Scientist" Debate

Y Combinator President Garry Tan reacted by hailing a "return of the age of the gentleman scientist" — rich savants funding their own curiosity. But Alpöge is a professional mathematician, not a hobbyist.

### The Question of Openness

Several HN commenters noted concern that the reasoning trace/search technique used by Fable is locked behind Anthropic's reasoning summarization, limiting scientific reproducibility. Others pointed out that the result was shared openly on X and verified independently.

## Technical Notes

### The Structure of the Counterexample

As Terence Tao explained, the counterexample is not a brute-force find. The polynomial has degree 7, meaning the Jacobian could a priori have degree up to 18 — the fact that all non-constant coefficients vanish represents a "massive cancellation" involving many equations. Finding such a polynomial by brute force would be "highly unlikely."

Tao reformulated the counterexample in geometric terms, showing how the domain can be replaced with an equivalent affine variety where local injectivity holds but global injectivity fails.

### The Lean Formalization

The formal verification in Lean means the result is machine-checked with absolute certainty. This is notable because:
1. The statement of the Jacobian Conjecture was already formalized in DeepMind's repo
2. The counterexample was formalized within hours of the announcement
3. This sets a precedent for rapid formal verification of AI-generated mathematical results

## Open Questions

1. **What was the prompt?** The full reasoning trace and prompts used to find the counterexample have not been shared
2. **Two dimensions?** Is the Jacobian Conjecture true for n=2?
3. **Real numbers?** Does the conjecture hold over ℝ (real numbers) as opposed to ℂ (complex numbers)?
4. **How many counterexamples exist?** Early investigation suggests counterexamples may not be rare
5. **What's the geometric intuition?** Mathematicians are working to understand *why* this counterexample works, beyond just verifying it calculates correctly

## Timeline

- **1939**: Ott-Heinrich Keller poses the Jacobian Conjecture
- **~2010s**: Yitang Zhang works on the conjecture for 7 years
- **July 6-10, 2026**: Formalizing Fermat workshop at Imperial College; Akhil Mathew discusses AI counterexample search with Kevin Buzzard
- **July 7, 2026**: Mathew and Alpöge discuss the Jacobian Conjecture as a target
- **July 20, 2026 (during World Cup Final)**: Alpöge prompts Claude Fable; Fable produces the counterexample
- **July 20, 2026, ~2:19 AM UTC**: Alpöge tweets the counterexample
- **July 20, 2026**: Paul Lezeau formalizes the counterexample in Lean; PR to DeepMind repo
- **July 21, 2026**: Terence Tao publishes blog post digesting the counterexample; Fortune publishes coverage
- **July 21, 2026**: HN discussion of Tao's ChatGPT conversation hits front page (1103 pts)
- **July 22, 2026**: Additional collision points found; broader implications explored
- **July 23, 2026**: Win-Vector publishes: "Maybe Jacobian Conjecture Counterexamples Are Not Rare"
