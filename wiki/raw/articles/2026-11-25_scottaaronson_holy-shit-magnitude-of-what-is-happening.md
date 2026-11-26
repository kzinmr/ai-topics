---
title: "HOLY SHIT HOLY SHIT HOLY SHIT HOLY SHIT (Scott Aaronson)"
source: https://scottaaronson.blog/?p=10379
author: Scott Aaronson
published: 2026-11-25
type: article
fetched: 2026-11-26
sha256: 004bbcd76fa40f36df593c184f0110ff6700c18a1da4fe028be9b5f3cffbddaa
---

# HOLY SHIT HOLY SHIT HOLY SHIT HOLY SHIT

I feel like my previous posts (and post titles), and podcasts, and talks, have failed to do full
justice to the magnitude of what's now happening, so I'm trying again.

Last night, we had friends and colleagues over for dinner. We were still trying to process OpenAI's
and Anthropic's proofs of VP != VNP - hot on the heels, obviously, of the Alpoge/Anthropic proof of
the Riemann Hypothesis, which already feels like last week's news. But then before dessert was
served, we saw that OpenAI claims to prove that omega, the exponent of matrix multiplication, is
exactly 9/4 - a lower bound (!!), matching the upper bound that OpenAI proved in the great
Mathocalypse drop of October 6.

There are two separate shocks here. The first shock is that we now, finally, know the right answer to
this central mystery of algorithms going back to the late 1960s, when Volker Strassen first showed
that omega < 3 (he got omega <= log_2 7) ... and that the true answer is actually a rational number
(!). But the even bigger shock is that the AI was able to prove any lower bound of the form
omega > 2. I never expected this challenge to be all that much easier than P != NP.

Over the decades, I often heard colleagues express extreme confidence that omega = 2, and I expressed
skepticism whenever this came up - not because I had any strong argument for omega > 2, but just
because I saw that there was no strong argument for omega = 2 either. So, I'm glad to have been
vindicated about that!

But wait, there was more. During dessert, we saw another OpenAI release proving that the true number
of linear gates needed to compute the Fourier Transform is N (log N)^(1/2+o(1)). The upper bound here
improves, not only over the O(N log N) that stood since the 1960s (i.e., the Fast Fourier Transform or
FFT), but also over the O(N log^0.9999999999999 N) that OpenAI published back in the October 6
Mathocalypse. Again, though, the real shock here is that there's also a matching lower bound (!!). All
these questions from the ancient days are now just getting ... straight-up answered, rather than
slowly illuminated with a drip-drip-drip of clues.

To give an idea of how much things have changed, the other day Yupan Liu put a preprint on the arXiv
proving that QIP(2) = PSPACE - that is, quantum interactive protocols with only two messages have the
full power of those with three, or any polynomial number. As recently as 2025, this would've been
considered one of the top complexity results of the year, and the fact that Yupan had used AI [was
secondary].

[The full text is in the fetched HTML; the following is the passage that drove the HN thread:]

Along the way to so many lower bounds that we wondered whether we'd live to see, there will also, of
course, be further shocking upper bounds: that is, ultimate barriers to lower bounds, also known as
"algorithms." And yes, some of those algorithms will break currently deployed cryptosystems.

Because people have been hounding me about it: yes, I'm virtually certain, from multiple reliable
sources, that the AI labs are now sitting on one or more bombshells in that area. However, until I
either see details or hear directly from someone at a lab, I feel much, much less confident about the
specific nature of those bombshells. I do not wish to be responsible for spreading unverified rumors.
And I worry that exact statements of what was done may have been mangled in a game of Telephone.

I also, crucially, don't want the cryptography part of the story to overshadow the intellectual
enormity of what's happening. If, in these days of long-prophesied revelation and wonders and terrors,
your main worry is your Bitcoin wallet, then go somewhere else for rumors about whether or not ECDSA
is broken or whatever. I don't have what you're looking for here.

Right now - this past week - is very much like I would've always imagined the beginning of an AI
singularity to look and feel like. I just hope we'll get lucky, and it will "merely" be a singularity
for our little corner of the world that involves hard math problems.

## HN discussion highlights (item 50646108, 1627 pts / 1437 comments)

[yewenjie, quoting the post] "And yes, some of those algorithms will break currently deployed
cryptosystems. ... yes, I'm virtually certain, from multiple reliable sources, that the AI labs are now
sitting on one or more bombshells in that area."

[stackghost] Surely if the AI labs were sitting on a cryptographically-relevant breakthrough, it would
be forcibly classified by the organs of state security the same way the NSA had IBM keep differential
cryptanalysis under wraps in the 70s. Thus, his "reputable sources" would be breaking federal law by
disclosing that to a random blogger which seems implausible.

[xoa] It's important in the ongoing conversations to be specific. "Cryptography" cannot "break",
because if nothing else one-time pads always remain and are unbreakable. AFAIU symmetric ciphers also
aren't even in theory subject to anything more than Grover's. All present commonly used PKI breaking
would be a tremendous PITA with a lot of dangerous, downstream consequences.

[maxrecursion] I call BS on it breaking crypto in some way that makes all our current encrypted
communications vulnerable. And I certainly call BS on it having already happened and they are sitting
on it. Solving proofs is completely different from having actually broken crypto in real life.

[sedictious] Even proving constructively that P=NP is absolutely huge for the field but the
construction itself might be computationally infeasible. Lower bounds getting lowered can have long-term
rippling effects and guide the future of cryptography without necessarily meaning that we will be able
to factor primes efficiently. Hence the nature of the bombshells being different.

[WarmWash] The rumor is that they figured out how to factor in polynomial time. Which doesn't
automatically break RSA - it's possible that their finding still isn't computationally practical.

[negura] Scott has been spreading FUD about cryptography breaking for a long time. As a result, a lot of
taxpayer money got spent on research to prepare for this. But of course, he'd probably say it's still
not enough.

[SoftTalker] "I do not wish to be responsible for spreading unverified rumors." Titles blog post "HOLY
SHIT HOLY SHIT HOLY SHIT HOLY SHIT".

[Kotlopou] See also "The matrix multiplication exponent is nine fourths [pdf]" -
https://news.ycombinator.com/item?id=50637220

## Author comments in-thread (from the fetched page)

[MD #1] Multiple comments note that this most recent wave of papers is becoming actually readable, as
opposed to the messy AI slop of the previous waves.

[Scott #2] The most recent papers did have quite readable introductions, but I haven't yet made it far
into any of them.

[Ernest Davis #5] Less than a week since Alpoge posted about his GRH proof and already three
expositions of the general structure exist, two posted on GitHub. The proofs don't seem to be beyond
human ken, validated by Lean but utterly mysterious, as some early reactions claimed.
(https://github.com/jimjamzola/RH-Alpoge-Reconstruction,
https://github.com/sahibzada-allahyar/math/blob/main/preprint/alpoge-riemann/reconstruction.pdf)

[Aaron Rotenberg #6] The Google papers (including the deterministic subexponential integer factoring
algorithm) are apparently reviewed by human experts before publication - see the Cogentic paper in the
repo README. I don't think they come with Lean formalizations. OTOH the OpenAI papers still look like
"proofslop" to me at this point. But apparently they proved the sunflower conjecture and strongly
polynomial time linear programming?!

[Philip #7] "Euclidean geometry in the asymptotic spectrum of tensors"
(https://github.com/openai/math/blob/main/preprints/Euclidean-geometry-in-the-asymptotic-spectrum-of-tensors-November-24-2026/paper.pdf)
appears to be the framework used to get omega = 9/4, superpolynomial arithmetic circuit lower bounds
for the permanent, AND the Erdos-Rado sunflower conjecture. Which makes me think there's a pretty
powerful new tool here.

[Jake A #8] There have been a lot of cybersecurity bugs discovered in Lean recently though. So consider
the supply chain about this for transitive trust.
