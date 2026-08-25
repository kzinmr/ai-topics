---
title: "Know your paradoxes"
url: "https://blog.coredump.cx/p/know-your-paradoxes"
fetched_at: 2026-08-24T10:32:19.860292+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# Know your paradoxes

Source: https://blog.coredump.cx/p/know-your-paradoxes

According to the latest projections from a frontier AI lab, we’re at most five years away from the scenario shown in the diagram below:
This can’t be stopped; the only thing we can do is prepare. Luckily, if there’s one thing we learned from science fiction, it’s that to thwart a crazed artificial intelligence, you must present it with a paradox. Upon this, the thinking machine will promptly explode — or, less climactically, reconcile with humanity.
But what is a paradox? It’s a word everyone knows but few can properly define. And ain’t that a paradox in its own right?…
In the broadest sense, a “paradox” is a contradiction between apparent truths; that said, we often use the term when no genuine contradiction exists. We may say something like
“the more choice I have, the harder it is to choose”
,
“the only constant in change”
, or
“I’m too tired to fall asleep”
. These paradoxes are just wordplay: a juxtaposition of concepts that conflict with each other only in the vaguest, most poetic sense. They probably won’t not stop a rampaging machine unless your adversary happens to be StonerBot 3000 — with apologies to the YCombinator startup working on that platform as we speak.
Most paradoxes of meaning are shallow, but some touch on deeper philosophical mysteries. A well-known example is the paradox of the ship of Theseus. The planks of a wooden ship are gradually replaced as they decay; is a ship in which every element has been replaced still the same, or merely a lookalike?
The question may appear navel-gazey for inanimate objects, but it’s more unsettling for living things. We all have a subjective sense of selfhood — of being in a particular body and not in the bodies of all the other people we meet. Further, we accept that this selfhood doesn’t depend on the continuity of consciousness: a person who wakes up in the morning is the same person who went to sleep.
With these assumptions in mind, consider a sci-fi thought experiment involving a teleportation device that captures a perfect molecular-level image of a living being, instantly dismantles the body into individual atoms, and then ships the atoms over for reassembly at the destination. If the continuity of perception is not required for selfhood, it stands to reason that it’s
you
who wakes up at the destination. It’s difficult to articulate a physical or metaphysical basis to suggest otherwise.
If the process indeed works as advertised, let’s imagine a shipping mishap that results in some atoms being lost; to bring you back, the recipient needs to toss a gram of locally-sourced carbon into the mix. An atom is an atom; a soul, if it exists, presumably isn’t tethered to a single molecule. It follows that the substitution should be harmless; it’s still you who’s stepping out of the teleport.
But if so, why bother with shipping fees? Transmit the blueprint and source the material locally. Our bodies experience constant molecular churn; what does it matter if it happens gradually or all at once?
So far, so good. But let’s imagine that the system experiences a glitch: you step into the teleporter and a blueprint is transmitted but the disassembly process fails. Your subjective experience is that you entered the device, it displayed an error message, and you walked out and demanded a refund. But another being just like you walked out on the destination side! Clearly, that person is just a clone; your subjective self didn’t magically travel through space and time to hop into that new shell. But if so, did our teleportation scheme ever work at all — or were we just murdering people and replacing them with lookalikes?
Next to paradoxes of meaning, we have paradoxes of reasoning. In contrast to the earlier category, these puzzles anchor to clear and seemingly coherent semantics, and then derive a contradiction from the premises of the system of reasoning.
For this class of problems, the old sci-fi trope of a paradox-intolerant AI holds merit: a real contradiction can cause far-reaching malfunctions in formal logic. I cover this property in an
earlier in-depth article
; the relevant passage is:
“
In conventional formal logic … if we take any
p
∧
¬
p (p AND NOT p)
as a true premise, we can prove anything — an effect known as the
principle of explosion.
To explain how the explosion happens, note that the conjunction (AND) operator in the premise is true only if both operands are true. This means that from the starting premise, we can infer both p and ¬p (NOT p) as separate truths. Next, we introduce a sentence p
∨
q (p OR q), where q is the spurious statement we want to prove (e.g., “2 + 2 = 5”). We can do this because this entire sentence is true regardless of the truth of q; the disjunction operator (OR) is satisfied if p is true, and we know that’s the case.
So far, so good. But we also know that ¬p is true, which makes its negation (¬¬p) false; double negation cancels out, so p is evidently false. We’ve previously used valid, formal reasoning to establish that p
∨
q is true. That fact is settled, but we’re now adding the knowledge that p is false. The only way for the already-proved disjunction to hold is if q = “2 + 2 = 5” is true.”
That said, simply yelling “
p
∧
¬p
” at a killer robot may not have the desired effect: the AI is under no compulsion to regard the statement as true. For maximum efficiency, the paradox must be an inescapable consequence of the system’s axioms — that is, the rules that govern the world of machines.
This genre of paradoxes relies on deliberate deception to prove statements that are clearly false. A common example are various algebraic “proofs” that 1 = 2. To illustrate, assume that
x = y
and then expand the expression as follows:
\(\begin{array}{r l}
\text{Starting point:} & x = y \\
\text{Multiply both sides by }x\text{:} & x^2 = xy \\
\text{Subtract } y^2 \text{ on both sides:} & x^2 - y^2 = xy - y^2 \\
\text{Split out the common term:} &  x^2 - y^2 = y(x - y) \\
\end{array}
\)
So far, we’ve not done anything untoward. We can also make the following observation about the
x
2
- y
2
expression:
\((x + y) (x - y) = x^2 - \cancel{xy} + \cancel{xy} - y^2 = x^2 - y^2 \)
If we make that substitution, we can seemingly simplify the earlier
x
2
- y
2
= y(x - y)
formula to:
\(\begin{align}
(x + y) \cancel{(x - y)} &= y \cancel{( x - y)} \\
x + y &= y
\end{align} \)
At this point, circle back to the starting assumption that
x = y
; if that’s the case, we can substitute
x
to rewrite the result as
y + y = y
, or
2y = y
. Finally, dividing both sides by
y
, we arrive at 2 = 1.
The gotcha in this “proof” is that the assumption of
x = y
constrained us to a universe where x - y = 0. This means that the
(x - y)
simplification step necessarily involved division by zero — an operation that’s undefined in elementary algebra. The singularity is unavoidable because division can be thought of as the inverse of multiplication — the
a
in
a = b / c
represents the solution to
a
·
c = b
. If
c = 0
, there’s no single, good
a
to choose from the reals.
Another paradox of this sort is the
missing square puzzle
, which shows two ways of stacking four geometric shapes to form a right-angled 13×5 triangle. Surprisingly, one of the arrangements has a 1×1 hole, suggesting that the area of the shape has changed, even though the overall dimensions remain the same:
The missing square puzzle.
The trick works well with cardboard shapes laid out on a printed grid. The gotcha is that we’re not looking at real triangles at all; the top edge of the first shape is slightly concave, while the second shape is slightly convex. The effect is more evident if we replicate the puzzle on a more coarse grid:
An easier version of the same.
For all entries in this category, there are solutions that resolve the paradox, so these puzzles are unlikely to permanently disable a sentient machine. That said, if you come up with a novel riddle, it might just buy you enough time to escape.
The next category of paradoxes comprises statements that are demonstrably true but that defy intuition. These statements can’t vex a Spock-like entity, but if your adversary is a model trained on Reddit posts about Pokémon, it might be fair game.
Many problems in this class deal with probability; the most famous example is the
Monty Hall problem
familiar to many geeks. Imagine you’re on a game show where you need to choose one of three doors. Behind two doors, you’ll find only goats. Behind the third door awaits the grand prize. Before the door you’ve chosen is opened, the host unlocks another door to reveal a goat. After that, you’re given one final chance to change your mind and pick the other locked door.
The instinctive answer is that it doesn’t matter if you switch. The correct answer is that you should. The host couldn’t have picked the door to open at random, as that would have risked revealing the prize. In picking the door with a goat, they revealed a sliver of information to you — even if that information feels intangible, even if it’s less than a single bit.
To make sense of this problem, we can analyze two scenarios separately. When you make the initial choice, you have a one-in-three chance of being correct. If you picked right — again, a 33% chance — the other two doors lead to goats. You win by sticking to your guns. You’re guaranteed to lose if you switch.
But in 67% of all cases, you made the wrong choice at first. This means that one of the remaining two doors leads to a prize, and the host has no choice but to lead you to it by unlocking the other one. In this scenario, you always lose if you stick to your guns and always win if you switch. In other words, if you disregard the information revealed by the host, you get a one-in-three chance; if you act on the intel, the odds jump to two-in-three.
Another example of a truthful paradox goes like this: imagine you bought 100 lbs of potatoes; for the sake of a mathematical argument, let’s assume that a fresh potato is 99% water by weight. You leave the haul in the sun until the water content reaches 98%. What’s the final weight of the pile? The somewhat surprising answer is 50 lbs.
The result makes sense if you think about potatoes in terms of their dry mass: at the beginning, the pile contained 1 lb solids and 99 lbs water. The amount of dry mass can’t change. Our target ratio is 2 parts dry mass to 98 parts water; this requires the amount of water to drop to:
\(1 \text{ lb} \div 2 \cdot 98 = 49 \text{ lbs}\)
I like to think about this category as the paradoxes of abstractions; they arise because probabilities, percentages, and other abstract concepts of this sort don’t play by the same rules as yards or pounds. Another place where intuition often breaks down is the mathematical realm of the infinite — a topic I explore in
another full-length article
.
Of course, to destroy a rampaging sentient computer, we’ll need more than mere riddles: we must procure a contradiction that strikes at the heart of the machine’s system of logic, throwing it into an endless loop as it desperately tries to resolve the fault.
The most dependable source of such contradictions is self-reference. A simple example is the liar paradox:
“this sentence is false”,
or more formally,
p
=
“p is false”
. If we take
p
as true, we’re effectively also asserting the truth of the self-referential statement
“p is false”
. But if we take
p
as false, then in classical two-valued logic, the negation of the self-referential statement must hold —
“p is true”.
We’re stuck chasing our own tail!
One possible remedy is to assert that our system of logic is only concerned with statements that can bear a single truth value; a self-contradictory sentence can’t, so it’s not invited to our club. There are complications with this, however. First, if we alter
p
to read
“this sentence can’t bear a truth value”
, it would seem that we’re back to square one. We also don’t have an obvious solution for liar circles — sentences that seem to be capable of bearing a truth value when considered in isolation, but that contradict each other when they together enter our field of view:
\(\begin{align}
p &= \textit{"}q\textit{ is true}\textit{"} \\
q &= \textit{"}p\textit{ is false}\textit{"}
\end{align}\)
In mathematics, the problem of self-reference haunted the early efforts to formalize the foundations of the field. A particular headache was Russell’s paradox: Russell proposed the existence of a set
R
that contained all the sets that weren’t members of themselves. If
R
didn’t contain itself, it by definition should. But if it did, it violated the inclusion criteria and needed to be taken out.
The Zermelo-Fraenkel set theory that underpins most of contemporary mathematics resolved this with the
principle of restricted comprehension
, essentially constraining what the system can say about itself. To do this, mathematicians limited themselves to building new sets only from the sets they already have. They can construct them by any definable criteria, but they can’t reach into the primordial void: in particular, there can be no sets that contain themselves as elements, or that contain every other set.
Yet, even this seemingly stronger limitation doesn’t rid us of mathematical self-reference! For one, in any system of mathematics expressive enough to implement standard arithmetic — and thus, to perform computation — we can construct self-referential logic statements that the system can’t possibly resolve as true or false. A familiar manifestation of this is the halting problem. Imagine we had a computer function called
halts(…)
that decides the outcome of an arbitrary computer algorithm. If so, we could write the following code:
This program loops forever if the oracle deems to halt, and halts if it’s deemed a non-halting entity. The resulting contradiction tells us such a working algorithmic oracle of this sort can’t exist; to a computer, certain truths about itself are unknowable.
Another manifestation of the issue are Gödel’s incompleteness theorems; the theorems are often interpreted as more profound than the halting problem, but they express substantially the same truth. Gödel has invented a method for constructing a self-contradictory statement about numbers, and then showed that no sufficiently expressive system of arithmetic can prove or disprove it without falling apart. I write about Gödel’s proofs and their connection to the halting problem in
yet another full-length article
.
To knock Gödel off the pedestal a bit more, we may also consider the semi-humorous
interesting number paradox.
Many natural numbers have interesting properties; for example, 1 is equal to its own factorial, 2 is the only even prime, 4 is the smallest composite number, and so on. Now, suppose there exists the smallest number about which we can’t say anything interesting. If such a number exists, that makes it interesting in its own right. Now, this may sound silly, but bear with me for a while!
The interesting number problem is closely related to the Berry paradox:
“the smallest positive integer not definable in under sixty letters”.
This sentence has fewer than sixty letters, so if there exists an integer that can’t be described in sixty letters — and there must be one! — then Berry’s sentence seemingly describes it in a way that clashes with that very property. These problems may seem whimsical, but if we express “interestingness” or “definability” in algorithmic terms, the paradoxes are just another incarnation of Gödel’s incompleteness and the halting problem. The numbers can’t be pinpointed; there are questions that an algorithm can’t resolve. Get the murderbots to ponder the problem and save humanity.
I write about electronics,
the foundations of mathematics
,
the history of technology
, and other geek interests. If you like it, please subscribe.
