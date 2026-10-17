---
title: "Yours truly - lcamtuf’s thing"
url: "https://blog.coredump.cx/p/yours-truly"
fetched_at: 2026-10-16T10:00:36.745278+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# Yours truly - lcamtuf’s thing

Source: https://blog.coredump.cx/p/yours-truly

Today, we’ll talk about the nature of truth. And I know what’s your first reaction:
“how do I unsubscribe?”
. Look, I’ve got no idea. I’ve been trying to figure that out myself.
I get it. I cover a variety of topics, but
this
is probably not what you signed up for. At the same time, this blog has only one rule: I shy away from current events. I’m getting older, so I’m deliberately giving up reach in favor of content that stands the test of time. News-related punditry is ephemeral; no one holds you accountable for bad takes, and if you’re right, your insights are soon trivialized. They’re what everyone has “always known” to be correct.
I can’t tune out the headlines, but I’ve been trying to channel this energy toward the exploration of more enduring and less obvious truths. For example, earlier this year, I published a pair of articles on the foundations of computer logic and the nature of paradoxes. These topics are interesting on their own and are usually treated superficially. Just as important, they’re quite relevant to whether large language models can reason — and if so, why:
Both posts proved to be phenomenally unpopular — not even a snarky comment on Hacker News! — so I doubled down with two additional features meant to counterbalance the techno-rationalist worldview favored both by the business tycoons who champion artificial intelligence, and by their opponents in the AI safety community:
My goal wasn’t to say “you’re wrong”; it was to show that philosophy is interesting and that the conclusions reached by some well-known tech thinkers are not as complete or inescapable as they seem.
Long-time readers might remember that these aren’t this blog’s first forays into philosophy. For example, in 2025, I covered the
origins and consequences of mathematical abstractions
; a bit later, I explored the connection between
Gödel and the theory of computability
. Don’t get me wrong: the field has a propensity for navel-gazing and petty semantic squabbles. That said, philosophy has given us the foundations of mathematics and most of modern science — and while it occasionally peddles mysticism and promises false certainty, it’s still the purest way to examine meaning, existence, reason, and truth.
Truth appears to be the fundamental goal for philosophical inquiry. It’s not hard to see why: falsehoods are dime a dozen but lack epistemological value. In contrast, the uppercase Truth — taken as a whole — is the singularly correct account of reality.
Of course, that’s just a slogan; similarly to mathematicians, modern philosophers tend to be more analytical. A mathematician is not content with the definition of a number as
“something we can count to”
; they want to pinpoint the essential characteristics of numbers and then apply this knowledge to new realms. In the same vein, most philosophers wish to define uppercase Truth as something more than just a synonym for reality.
Whatever the nature of this singular Truth might be, we seem to experience it through individual value judgments; we hold that some
things
are true and others are false. These plentiful lowercase truths are not standalone beings; instead, they appear to be bivalent (two-valued) attributes that attach to statements made in a language of our choice. An apple, in the sense of a physical object, can’t be “true” or “false”; a statement about apples might.
Of course, not every utterance can be a truth-bearer (a
proposition
). For one, the candidate phrase must be unambiguously interpretable. It must also make a factual declaration of some sort;
“I am holding an apple”
is fine — it gives us a binary claim we can examine — but
“please hand me an apple”
won’t do.
In an
earlier article on paradoxes
, I also remarked that self-referential statements, such as
“this sentence is false”
, might need to be taken out of the equation. In the same write-up, I’ve given an even wackier example of Curry’s paradox. It’s a sentence that doesn’t seem to contradict itself, but forces us to accept an arbitrarily-chosen consequent (the
B
in “
if A then B”
) as true:
“Imagine the following seemingly innocent sentence:
\(p = \text{“if }p\text{ is true, then pigs can fly”}\)
Considered as a whole, an “if A then B” statement can’t possibly be true if the antecedent (A) is true while the consequent (B) is not. For example, if I say “if it’s Wednesday, then I’m at my mom’s”, and it’s Wednesday and you catch me partying, my earlier claim couldn’t have been correct.
Circling back to Curry’s sentence, this tells us that p, taken as a whole, can’t possibly be considered true unless pigs are actually able to fly: if p equals true, this automatically renders the antecedent true and requires the consequent to hold. Without forming an opinion about the logic value of p, we can formalize this conclusion in the form of a new statement, q:
\(q = \text{“if }p\text{ is true, then pigs can fly”}\)
But hold on: q is a necessary truth, but it also says precisely the same thing as p. Therefore, p is also necessarily true; pigs must be able to fly.”
Paradoxes of self-reference can be kept at bay by placing constraints on the object language — that is, the language we use to build propositions. This language can be more restricted than the meta-language we use to discuss their meaning.
At this point, we have a fairly agreeable definition of truth as a semantic attribute; to build on this, in
another article
, I outlined the usual formal rules of manipulating propositions to derive new facts. For example, it makes sense to codify that
when we write
“p = a AND b”
, this means that
p
is true if and only if both
a
and
b
are true. The resulting truth-algebra can be tinkered with to taste, but right now, we have a far more pressing issue to solve.
So far, we’ve defined truth as a semantic attribute of propositions and then endowed it all with an algebra. This makes mathematicians happy but lacks any notion of
truthmaking
: there’s no process, other than whimsy, by which we decide that “
2 + 2 = 4”
ought to be true and
“pigs can fly”
ought to be not.
An instinctive approach is to adopt the
correspondence theory
: that is, the belief that semantic truth must correspond to
facts
. This, however, creates as many problems as it solves. We now need to decide the meaning of facts: are they just ideas we can express with words — a collection of sentences and attached judgments? If yes, what distinguishes facts from any other set of semantic truths taken as axioms? Do we need this at all if facts and truths look pretty much the same?…
Conversely, if facts are separate from semantic truths… what are they, exactly? A more nebulous, non-linguistic property of reality? Can you
see
a fact? When you’re looking at a cat on a sofa, how do you know it’s a cat and a sofa, and not some singular, Cronenberg-type cat-sofa entity? Do we need a theory of
cathood
first?
The questions may seem capricious, but under the correspondence theory, it’s hard to say anything useful about facts without first building a seemingly unattainable meta-model of mind and reality. Without it, facts just
are
.
Because of this issue, some thinkers reject the correspondence theory and hold that uppercase Truth is more or less inscrutable: it’s the end of the line for philosophical inquiry. In the most radical (
deflationist
) view, any mention of truth is just syntactic sugar;
“<x> is true”
is the same as saying
“suppose that <x>”
or simply
“<x>”
. In this view, the only requirement for philosophical investigations is that they start from internally consistent axioms; that’s to say, in conventional logic, we can’t simultaneously assert that
“pigs can fly”
and
“pigs cannot fly”
. Beyond this, we can construct any universe we like; truth is just an outcome of a thought process that follows that universe’s rules.
This is essentially the approach of mathematical logic; we choose axioms based on intuition and never look back. The method works surprisingly well. For example, it’s given us a good theory of infinite quantities, with applications to calculus.
The discussion in the preceding section might have biased you toward the view that all this talk of a singular, uppercase Truth is just a waste of time. If so, there’s a simple thought experiment that might change your mind.
Say that I own a 12-pound cat named Cindy Clawford; you wish to inquire about her weight. I can answer in a number of ways. In particular, I can say that Cindy weighs
“less than, equal to, or more than 1,000 pounds”
. This is a truth, but it’s a logical tautology that holds for any physical object. It’s given you no information whatsoever.
In light of this, it would seem foolish to reduce philosophy solely to the pursuit of semantic, lowercase truths; we’re clearly seeking something more. Now, suppose that our uppercase Truth exists and has the shape of a set T containing all possible true statements about the world. To illustrate, in the Cindy-verse, a slice of the set may look the following way:
\(\begin{align}
\ldots \\
t_{1010} &= \text{“Cindy doesn't weigh 10 pounds.”} \\
t_{1011} &= \text{“Cindy doesn't weigh 11 pounds.”} \\
t_{1012} &= \text{“Cindy weighs 12 pounds.”} \\
t_{1013} &= \text{“Cindy doesn't weigh 13 pounds.”} \\
t_{1014} &= \text{“Cindy doesn't weigh 14 pounds.”} \\
t_{1015} &= \text{“Cindy doesn't weigh 15 pounds.”} \\
\ldots \\
t_{2000} &= \text{“Cindy doesn't weigh 1,000 pounds.”} \\
\ldots

\end{align}\)
We don’t concern ourselves with where the contents of T come from. Maybe it’s the scientific theory of everything, maybe we found it in a holy book. The only point is that T — a collection of all truths — is a complete model of reality, at least to the extent that it can be expressed with words.
Channeling Karl Popper, this allows us to rank semantic truths — which can be viewed basically as competing descriptions (theories) of reality — simply by measuring how well they cover T. That is to say, we can assess the theories’ uppercase
Truthlikeness
. Consider the following:
\(\begin{align}
c_{1} &= \text{“Cindy weighs less than, equal to, or more than 1,000 pounds.”} \\
c_{2} &= \text{“Cindy weighs less than 1,000 pounds.”} \\
c_{3} &= \text{“Cindy weighs less than 14 pounds.”} \\
c_{4} &= \text{“Cindy weighs 12 pounds.”}

\end{align}\)
In this example, the tautological theory
c
1
is true, but doesn’t entail (or confirm) any statements listed in our earlier subset of T-truths. So, we have a practical indication of the theory’s worthlessness.
Statement
c
2
—
“Cindy weighs less than 1,000 pounds”
— gets us farther: it lets us infer the truth of
t
2000
, so it’s a measurably better theory of T. This continues with statement
c
3
—
“Cindy weighs less than 14 pounds”
— which additionally establishes the truth of
t
1014
and
t
1015
. Finally, statement
c
4
is a complete theory of what’s shown in the earlier snippet of T.
Again, this approach allows us to rate empirical statements based on how well they approximate the whole Truth of T. This sounds like a better way to frame the goal of rational inquiry: we’re not merely collecting truth-Pokémon, we’re trying to get closer to enlightenment. Of course, this approach still leaves many questions unanswered; for example, we don’t have a metric of usefulness or similarity of the statements that are entitled by different theories, so it’s not necessarily the case that a theory with higher T-truth content is worth our time.
Another way to illustrate the shortcomings of the method is to consider the problem of invalid theories. The earlier statement that Cindy weighs less than 1,000 pounds is a valid theory of T, but it is ranks low in the T-truth hierarchy: it describes reality rather imprecisely. In contrast, the claim that Cindy weighs eleven pounds is invalid with respect to T — it contradicts reality — but it’s
almost
correct. In particular, in the earlier snippet, it selects for many of the same T-truths as our most accurate valid theory,
c
4
. So, can we build a partial Truthlikeness ordering of invalid theories, too?
Alas, a simple ranking appears to be unattainable. To explain, let’s assume we have two invalid theories of T — A and B — and that both entail some factually-accurate statements that belong to T; that’s their T-true content. At the same time, because the theories are invalid, they must also entail some statements that contradict T; this is the T-false content of A and B.
Next, assume that the T-truth content of A is greater than B; in essence, let’s declare that this is the theory that ought to sit higher than B in the hierarchy of Truthlikeness. If so, there must be at least one T-true proposition,
a
t
, which is entailed by A but not B. Further, because A is an invalid theory, it must also entail at least one counter-to-T statement,
a
f
.
With this in mind, let’s consider a new statement in the form
p
=
a
t
∧
a
f
. Here, “∧” is the logical conjunction operator (AND), so
p
is true if and only if both
a
t
and
a
f
are true. This is necessarily the case under A, so
p
is a logical consequence by this theory. This new statement is also T-false because it hinges on the truth of a counter-to-T proposition
a
f
; in other words, it belongs on the theory’s T-false bin.
In contrast, theory B doesn’t entail
p
because the truth of
p
hinges on
a
t
, and by the criteria spelled out at the onset, this proposition is not a consequence of B. Therefore,
p
is a T-falsehood that’s produced only by A — a surplus invalid result. It would seem that it’s not possible for theory A to have larger coverage of uppercase Truth without also incurring more T-falsehoods; it can’t get better without simultaneously getting worse.
But then, again — is
p
an interesting consequence of the theory, or is it just fluff that’s safe to ignore? Or for that matter, what’s the significance of
a
t
and
a
f
? These questions are worth asking, but are a wholly separate can of worms.
I write original, in-depth articles about electronics, geek culture, mathematics, algorithms, history, and more. If you like what you see, please subscribe.
