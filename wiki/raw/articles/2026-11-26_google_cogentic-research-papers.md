---
title: "Google Cogentic research papers: deterministic subexponential integer factorization, discrete logs"
source: https://github.com/google-research/google-research/tree/master/cogentic_research_papers
type: hn-discussion
fetched: 2026-11-26
sha256: f74ab730e36007daed18f3cbbd1886a5b075c69099ef7b90fd07313272685d2f
---

# Google releases Cogentic papers on integer factorization, discrete logs and more

Repo: https://github.com/google-research/google-research/tree/master/cogentic_research_papers
Method paper: "Cogentic: Multi-Agent Orchestration for Automated Proof Discovery" (2026),
https://arxiv.org/abs/2609.40324
HN: https://news.ycombinator.com/item?id=50642086 (494 pts / 357 comments)

Note: the primary artifact is a GitHub tree of preprints (the GitHub `/tree/` view renders thin), so
this raw file is built from the HN comment tree plus the Aaronson-thread notes, not from a fetched
article body.

What is described in the thread: Cogentic is a specialized harness for existing LLMs to collaborate on
mathematical conjectures, using a central orchestrator and a shared database of intermediate proofs.
Built on Gemini 4 Argon, it produced a batch of publishable results including a **deterministic
subexponential-time integer factorization algorithm** and discrete-log results. Related single-paper
entry that also hit the front page: "Unconditional Integer Factorization in Subexponential Time"
(HN 50651627).

## HN discussion highlights (item 50642086)

[david-gpu] Cogentic appears to be a specialized harness for existing LLMs to collaborate together to
solve mathematical conjectures, using a central orchestrator and a shared database of intermediate
proofs. And with just that, using Gemini 4 Argon, they have already obtained a number of interesting
results? Math is going through its own version of the industrial revolution.

[wood_spirit] I think we'll see a move from grep to code servers where the server is also the conduit
between the subagents for coding too.

[schleck8] Context: "Cogentic: Multi-Agent Orchestration for Automated Proof Discovery" (2026)
https://arxiv.org/abs/2609.40324

[vlovich123] GNFS would take 10^47 operations while this takes 10^2572 for a 4096 bit RSA key. The only
improvement here is that this is guaranteed to work for arbitrary numbers. My money would be no [for
breaking normal RSA key sizes]. Elliptic curve cryptography already uses a different mechanism that
isn't susceptible to factorization improvements.

[cogman10] "Post quantum" really just means "doesn't rely on integer factorization". It's possible there
are other quantum algorithms that could attack current best asymmetric cryptography (though it seems
unlikely).

[roomey] Are we going to see factorization on classical computers with this? Any opinions on the
possibility of a novel algorithm to allow large int factorization?

[fwlr] (mocking the abstract register) "The proof reduces monochromatic rectangle density via Gaussian
hyperplane rounding and box-constrained biasing to refuting the existence of biased Kullback-Leibler-
stable sign matrices ..." Ah yes, of course.

[edumucelli] Students doing their PhDs in Math and CS on more theory-related theses are having a tough
time. You never know if your thesis is going to be the next OpenAI/Anthropic and now Google trophy
paper.

[brandonpelfrey] A weird take to me. Can a PhD in math or theoretical CS not be about using models and
agents to more efficiently explore ideas? That seems like an extremely valuable path ... not at risk of
being scooped.

[_1] They could still go for more elegant and understandable proofs than the behemoths that these LLMs
are churning out.

## Related rumor thread (item 50643065, 492 pts, "Rumors swirling that labs might have cracked Factoring in P")

[jerf, supplying the sources] Scott Aaronson on his own blog (comment on p=10362): "I've now heard many,
many rumors that one or both labs are sitting on Factoring in P. I don't know how much to credit this.
While I'm virtually certain that the labs are, indeed, sitting on one or more bombshells for
cryptography, it's possible that the exact nature of those bombshells has gotten distorted via a game
of Telephone."

[Cakez0r] Anthropic factored RSA-896 a couple of months ago (https://saweis.net/posts/rsa-896.html). They
used existing methods and stressed that they didn't find a more efficient approach to factoring (maybe
true, maybe not). It does show that they are at least looking at the problem and willing to throw
substantial computing power at it.

[Geof25] Big problem with post quantum crypto is that we kind of don't know if it is actually working.
Is there some mistake which we don't see but make it easily breakable? PQ crypto is much more fragile
in this regard.

[cls59] We have post-quantum options available. Most sites that would need to deploy it are nowhere near
"ready to go" on a project of that scale.

[wry_xy] I've been doing [defense-in-depth, multiple independent schemes] for my personal tools for many
years. I've been surprised at the willingness of supposedly security-conscious people to put all their
eggs in one basket.
