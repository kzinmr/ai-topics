---
title: "Ten advances in mathematics and theoretical computer science"
url: "https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything"
fetched_at: 2026-08-02T10:14:19.942052+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Ten advances in mathematics and theoretical computer science

Source: https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything

1st August 2026 - Link Blog
Ten advances in mathematics and theoretical computer science
(
via
) A few days ago it was Anthropic
discovering cryptographic weaknesses with Claude
using Mythos Preview, spending $100,000 on tokens and with prompts that included "again we are not looking for low hanging fruit, we want proper research to find genuinly hard findings."
Now it's OpenAI's turn to flex. They set "an internal version of Astra, our next major model" on finding solutions to ten mathematical problems that "have seen no progress on the main result for at least a decade". They claim to have spent less than $2,000 at GPT-5.6 Sol token prices on each one.
(No news on how many problems they spent $2,000 on
without
reaching a solution though.)
The
openai/ten-proofs
repository has Lean 4 formalizations of their results, and there's also
a paper
describing the solutions and an additional
LLM-generated PDF
where the model "reconstructs how the proof came together" based on the unpublished reasoning traces.
That's a decent level of transparency, but I want to see the prompts they used!
A lot of mathematicians online are experiencing a collective burst of
Deep Blue
. Mathematician Kirwin Hampshire published an impassioned essay last week,
The Dark Night of Mathematics
, describing "a profound spiritual crisis" brought on by previous (and less significant) results.
OpenAI's results reminds me of what Terence Tao described as "big mathematics" in
IEEE Spectrum in June
:
Unlike some of his peers, Tao is neither dismissive of AI nor fearful. Instead, he sees it as the catalyst for a fundamental shift in the discipline—a transition toward what he calls “big mathematics.” He envisions a future of large-scale, decentralized collaborations between humans and machines, where complex mathematical tasks can be diced and sliced, with humans claiming the creative parts and AI doing the lion’s share of the technical grunt work.
