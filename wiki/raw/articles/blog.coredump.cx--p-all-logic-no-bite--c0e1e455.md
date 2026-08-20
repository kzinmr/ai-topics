---
title: "All logic, no bite"
url: "https://blog.coredump.cx/p/all-logic-no-bite"
fetched_at: 2026-08-20T10:00:47.662315+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# All logic, no bite

Source: https://blog.coredump.cx/p/all-logic-no-bite

Today, I’d like to talk about logic — and before I do, I should probably explain why. But before we get to that, a definition may be in order: in a nutshell, logic is a system for drawing conclusions from premises (“facts”).
Formal logic usually isn’t taught in high school; as far as I know, a rigorous treatment of it isn’t even required for most computer science degrees. The concept is familiar to most mathematicians and to a handful of software engineers who dabble in esoteric programming languages. As for everyone else, we might know about “digital logic”, a simple algebra of binary numbers that involves operators such as AND, NOT, and OR. What’s less clear is how we get from zeroes and ones to some semblance of human reasoning.
For mathematicians, the most common role of formal logic is to provide a more precise vocabulary for proofs. To illustrate some of the ambiguities of everyday speech, consider the following statement in the form of
“if A then B”:
\(\require{color}
\text{“If }\underbrace{\text{you did your chores}\vphantom{|}}_{A}\text{, }\underbrace{\text{you can play Minecraft}\vphantom{|}}_{B}\text{.”}\)
It’s something a parent could say to a child. In that use, the phrasing clearly implies its own inverse,
“if not A then not B”:
\(\text{✅ “If you }\textbf{didn't}\text{ do chores, you }\textbf{can't}\text{ play Minecraft."}\)
The statement also seems to imply the converse (
“if B then A”
), although that form needs a small edit for clarity:
\(\text{✅ “If you can play Minecraft, } \underline{it \ means} \text{ you did chores."}\)
As for the contraposition
(“if not B then not A”
), its status is up for debate. It follows from the strict reading of the original sentence. That said, in real life, it would be tacitly understood that gaming privileges can be lost for serious violations of unrelated household rules:
\(\text{❓ "If you }\textbf{can't}\text{ play, }\underline{it \ means}\text{ you }{\textbf{didn't}}\text{ do chores."}\)
Do all other
“if A then B”
statements play by the same rules? Nope:
\(\text{“If }\underbrace{\text{my cat is hungry}\vphantom{|}}_{A}\text{, }\underbrace{\text{it meows}\vphantom{|}}_{B}\text{.”}\)
This time around, the phrasing doesn’t imply the inverse (
“if not A then not B”
). The speaker isn’t suggesting that Mr. Mittens meows only when it wants to eat. Therefore, we can’t infer the following:
\(\textrm{❌ }{\text{“If }{\text{my cat }\textbf{isn't }\text{hungry, it}\textbf{ doesn't}\text{ meow."}}}\)
On the flip side, if the original assertion is true — if the cat always begs for food — the contraposition (
“if not B then not A”
) follows in a straightforward way:
\(\text{✅ “If my cat }\textbf{doesn't }\text{meow, it }\textbf{isn't }\text{hungry."} \)
Our problems with cat logic don’t end here. Let’s consider the following:
\(\text{“If }\underbrace{\text{grass is green}\vphantom{|}}_{A}\text{ then }\underbrace{\text{kittens are cute}\vphantom{|}}_{B}\text{.”}\)
Both A and B are true, but most people would peg the statement as false — or at least
wrong
. The truths coincide, but we reject the argument because the antecedent (
A
) and the consequent (
B
) are not connected in any obvious way.
But what if I told you that every Sunday morning, Bob wakes up with a headache?
\(\text{“If }\underbrace{\text{it's Sunday morning}\vphantom{|}}_{A}\text{ then }\underbrace{\text{Bob has a headache}\vphantom{|}}_{B}\text{.”}\)
As before, I don’t know what’s the connection. Maybe there isn’t one; maybe the timing of Bob’s migraines is just a cosmic coincidence. Yet, in this context, a coincidence is good enough to accept the claim.
Another subjective issue crops up with the following statement:
\(\text{“If }\underbrace{\text{pigs can fly}\vphantom{|}}_{A}\text{ then }\underbrace{\text{pumpkins are square}\vphantom{|}}_{B}\text{.”}\)
It feels wrong, but there’s nothing we can disprove: the consequent is false, but so is the antecedent it’s gated on. We just don’t like that the sentence limits our imagination: perhaps if pigs could fly, all pumpkins would be donut-shaped? But if the task at hand is to work from true premises toward logical conclusions, and
A
is not a true premise, why the heck are we trying to form opinions about
B
? It’s a universe that doesn’t exist; we’re not given the axioms that govern it.
Let’s twist that knife a bit more: what do we make of the following pair of sentences?
\(\begin{array}{c}
\text{“If pigs can fly then pumpkins are square."} \\
\text{“If pigs can fly then pumpkins are }\textbf{not}\text{ square."} \\
\end{array}\)
An intuitive interpretation is that they can’t be both true at the same time. A more analytical view is that only the consequents can’t. In other words, maybe this is just telling us that pigs can’t fly?
It’s not just the
if-then
connective that’s cursed; the A and B atoms can cause problems too. In our examples, they appear to be declarations of facts — but can we proclaim anything we want? If I say
“this statement is false
”, is that a truth or a falsehood? Neither? Both?…
These semantic gotchas are great if you’re devising brain-teasers for nerds; they’re not helpful if you’re writing down a mathematical argument. This is why mathematicians rely on formal logic to define some predictable ground rules. The classic approach is pretty close to common sense, but it resolves the ambiguities by making several ad hoc calls. In particular:
A statement in the form
“if A then B” (“A
⇒ B”
):
…does not imply its inverse
(
“not A
⇒
not B”
). A cat that always meows when hungry isn’t required to stay quiet once fed.
…doesn’t imply the converse
(
“B
⇒
A”
). By extension, if you hear Mr. Mittens meowing, it’s not a given that he wants a meal.
…implies its contraposition
(“not B ⇒
not A”
). No meows is proof positive that the cat isn’t looking for food.
Lack of relevance is not fatal.
A true proposition implies any other true proposition. In
“if A then B”
, it’s enough that
A
is true in tandem with
B, so
there’s nothing false about
“if grass is green then kittens are cute”.
Counter-to-fact conditionals are true.
A false antecedent can imply whatever it wants: “
if pigs can fly then pumpkins are square”
. The sentence is true, with no actual consequences for pumpkin shape.
You gotta take sides.
The system only deals with statements that can bear a single, binary truth value. If it can’t, it’s not a valid statement.
Logic arguments expressed with words are easy to grasp, so to keep the riff-raff out, mathematicians often resort to symbolic notation. For example, the idea that sets
A
and
B
are equal to each other if and only if they contain the same elements can be more enigmatically spelled out as:
\(\forall A, B \bigl[A = B \iff \forall x ( x \in A \iff x \in B) \bigr]\)
My initial plan for this article was to dive into this symbology next. But before we do, it may be useful to show how formal logic acts not only as a convenient language for proofs, but also as the
source
of math.
Arithmetic is the oldest branch of mathematics; it’s also notable for having resisted attempts at formalization for a pretty long time. As it turns out, it’s tricky to explain numbers and basic arithmetic operations as anything other than “the things you know”. I don’t know why an apple plus an apple gives me two apples; I guess it’s just how apples are. It seems to work with fingers too.
Regular readers may recall two earlier articles about some of the successful efforts to construct the arithmetic of natural numbers and reals from scratch. In the end, we took the existence of an empty set as a given and then defined numbers and operations through the repeated application of several fairly intuitive rules:
The beauty of this method is that it gave us more than what we already knew. For example, it seamlessly generalized to operations on infinite numbers, with mildly surprising results.
Unfortunately, in math textbooks, intuitive explanations aren’t the rule. Many of the discipline’s foundational axioms stem from investigations of the natural world, but we prefer to teach the craft as if it owed nothing to reality. In the modern academic practice, the question of where a particular idea came from, or whether an axiom is
ontologically correct
, is considered vacuous and out of scope. For the most part, you’re just handed a rulebook to play someone else’s game.
In the remainder of the section, I’ll try to kill two birds with one stone. First, we’ll look at yet another method of constructing the reals to develop intuition that will pay off once we get to digital logic (i.e., Boolean algebra). Second, on the topic of my mini-rant about mathematical education, we’ll note that the use of logic doesn’t necessarily make one’s arguments logical.
The usual axiomatic approach to defining reals is to give students a collection of roughly fourteen ad-hoc rules for manipulating the elements of an otherwise opaque set we call “ℝ”. The axiomatic method doesn’t care what the set contains or what it
means
; the method doesn’t even posit the existence of any canonical version of ℝ. We simply assert the existence of some structures — i.e., collections of objects and object relations — that, by the will of the gods of mathematical abstraction, obey the rules we want these structures to obey.
The rules are usually divided into three parts: field axioms, order axioms, and the axiom of completeness. Field axioms are easy; they pretend to be abstract, but tacitly capture natural laws. They assert the existence of a mystery operation called “addition” (symbol: “+”). The operation takes two operands in the reals and produces a result that’s also in ℝ. Further, the operation is associative and commutative; that is, for any
a, b,
and
c
in ℝ, it obeys the following equivalencies:
\(\begin{array}{c}
a + (b + c) = (a + b) + c \\
a + b = b + a
\end{array}\)
The same ruleset is given for multiplication (“·”):
\(\begin{array}{c}
a \cdot (b \cdot c) = (a \cdot b) \cdot c \\
a \cdot b = b \cdot a
\end{array}\)
So far, we’ve said nothing about what these two operators actually do. Turns out that we don’t have to say much; first, to distinguish between them, the axioms assert the existence of additive and multiplicative identities. By that, we mean a pair of elements in ℝ, conventionally labeled “0” and “1”, such that for any
a
∈ ℝ, the following equalities always hold true:
\(\begin{array}{c}
a + 0 = a \\
a \cdot 1 = a
\end{array}\)
Again, the approach doesn’t concern itself with the “why” or the “how”; all we’re saying is that in a system that obeys the axioms, there must be a pair of elements for which the equalities hold. And if these elements exist, we might as well label them in a familiar way.
Next, we posit that for any
a
taken from ℝ, there exists an additive inverse (“
-a
”); and that for any
a
≠ 0, we can also find a multiplicative inverse (“
1/a
”). Because we don’t have subtraction or division defined just yet, we treat these inverses as atomic symbols that obey the following rules:
\(\begin{array}{c}
a + (-a) = 0 \\
a \cdot (1/a) = 1
\end{array}\)
The final field axiom is the distributive property that ties the two operators together:
a ·
(
b
+
c
)
= a · b + a · c.
The neat surprise is that these rules are already good enough to perform calculations in ℝ. By combining the axioms, we can easily prove that there can be only one additive identity (“0”), one multiplicative identity (“1”), and that “0” and “1” can’t be the same. Next, because addition always produces a result in ℝ, we conclude that there is a real associated with the value of 1 + 1. If we label this real “2”, we can for example show the following:
\(a \cdot 2 = a \cdot \underbrace{(1 + 1)}_{\substack{\text{by our} \\ \text{definition} \\ \text{of "2"}}} = \underbrace{a \cdot 1 + a \cdot 1\vphantom{)}}_{\substack{\text{expanded in line} \\ \text{with the distributive} \\ \text{property}}} = \underbrace{a + a\vphantom{)}}_{\substack{\text{eliminating} \\ \text{multiplicative} \\ \text{identities}}}\)
Alas, field axioms do not provide complete “driving directions” to the reals. There are many different algebraic fields; for instance, the exact same axioms are also satisfied by
complex numbers
. Heck, we can even make the rules work for certain types of finite sets, giving us modulo arithmetic systems that have applications in cryptography, but that would be frowned upon on a tax return. The smallest possible finite field needs just two elements: “0” and “1”, with the result of 1 + 1 simply wrapping around.
To get closer to where we want to be, we continue with order axioms. We begin by proposing that for any
a
and
b
chosen from ℝ, exactly one of three possibilities must hold:
a
<
b
,
a
=
b
, or
b
<
a
. Further, to tie the behavior of the less-than operator to existing algebraic rules, we give the following axioms for any
a, b, c
∈ ℝ
:
If
a < b
and
b < c,
then
a < c,
If
a < b
then
a + c < b + c,
If
a < b
and 0 <
c
, then
a · c
<
b · c
.
The structures that obey this criteria are infinite fields in which all elements are ordered in the usual arithmetic sense.
If you made this far, you might be wondering why I grumbled about how we teach math. Sure, we had a lot of axioms dumped at our doorstep with little justification, but they’re all saying reasonable things?…
The answer is that we’re not done yet: the rules we have in place are also valid for rational numbers (ℚ). To get to a ruleset that unambiguously describes reals, we need to toss in the axiom of completeness.
To explain the usual phrasing of the axiom, we must first talk about subsets and their bounds. If we have the set of real numbers, it stands to reason that we can take a subset of it. For example, we can construct subset A that consists of every real less than or equal to 2. Or, we may conjure subset B that contains all numbers divisible by 42.
A subset of an ordered set set may be
bounded above
; this means that in the parent set, we can find an element that’s greater than or equal to every element included in the subset. Any number that meets this criteria qualifies as an upper bound; for A, it can be any value ≥ 2. In contrast, for subset B, there’s no bound in ℝ; for any real we choose, we can produce a counterexample that’s the next multiple of 42.
A subset that’s bounded above may also have a
least
upper bound. That’s to say, among the values that qualify as upper bounds, there might be some definite “minimal” choice. For subset A, this is 2. Any value less than that can’t work because some elements of A would end up above the selected threshold.
With these preliminaries out of the way, the completeness axiom says that any non-empty subset of ℝ that is bounded above in the reals must also have a least upper bound in the reals.
That’s it. And —
what just happened
? We went through all this effort that say something that feels borderline meaningless?… At the same time, the rule is essential. For one, ℚ doesn’t obey it, for reasons that are left as an exercise for the willing reader (hint:
q
² < 2
). Just as important, we need the axiom to prove the Archimedean property. This property says that if we take any two positive reals such that
a < b
,  there’s some
n
∈
ℕ
that makes
n · a > b
.
The inequality-flipping mechanic of the Archimedean property couldn’t possibly work if we could pick an infinite number for
b
, or an infinitesimal (very roughly: “1/∞”) for
a
. This means that the property implies the absence of infinities or infinitesimals in reals. This is critical to a good chunk of higher math; for example, it allows us to justify limits in calculus.
Had we attempted the set-theoretic approach outlined in the earlier posts, the Archimedean property would arise as a natural consequence of the construction of reals via Dedekind cuts. But to prove it in the axiomatic method, we need the mildly perplexing completeness axiom. This invites but never answers questions such as
“where did that idea come from?”
and “
could we get better-behaved algebra if we phrased this axiom in a different way?
”
.
In any case, let’s prove the Archimedean property, the axiomatic way. We choose an arbitrary positive pair
a < b
and then construct a set
C
that consists of all the natural-number multiples of
a
:
\(C = \{ 0a, \; 1a, \; 2a, \; 3a, \; 4a, \; 5a, \; \ldots \}\)
When structured this way, C is obviously a subset of ℝ.
Next, assume that the Archimedean property does
not
hold: that there can be some
a < b
pair such that every multiple of
a
— i.e., every element of
C
— is still less than
b.
If so, we’re effectively asserting that
b
is an upper bound of
C
. It’s not necessarily the set’s
least
upper bound, but from the completeness axiom, the existence of the former automatically implies the existence of the latter. If it exists, we can designate this unspecified least upper bound as
s.
In our argument,
a
is positive, so if we calculate
s - a
, we know that the result will be less than
s.
As a reminder,
s
is the smallest real that’s still greater or equal than all the elements of
C
; if we pick any number less than that, there must be at least one member of C
that exceeds it.
In other words, there must be some element of
C
that’s greater than
s - a
:
\(\underbrace{n \cdot a}_{\substack{n\text{-th} \\\text{multiple} \\ \text{in set C}}} > s - a\)
We can rewrite this inequality by grouping all the
a
-containing terms on the left. We obtain:
But hold on — the new expression on the left is just
a
multiplied by a natural number,
n
+ 1. This should make it a member of
C
. At the same time,
s
is the least upper bound of
C
, so it can’t possibly be less than any existing element of that set. Oops?
We assumed that the Archimedean property doesn’t hold and we ended up with a contradiction. In standard two-valued logic, if a property can’t be false, it must be true — so that’s our proof.
For the few readers who are still here, I hope that this lengthy exposition underscored two interesting points. First, it would appear that given a sufficiently capable system of logic, we can build an algebra without needing apples, fingers, or any other
a priori
notion of numbers or arithmetic operators; if aliens from outer space understand logic, we can show them how to calculate 2 + 2 = 4. And second: we like to teach math in confusing ways.
Up until this point, we talked about logic as a way to formalize mathematical thinking, but most readers of this blog are probably more familiar with the logic of digital circuits. In computing, the term “logic” may seem suspect: the field leans on profoundly-sounding keywords such as “true” and “false”, but by the end of the day, integrated chips are just manipulating voltages.
Because of the tenuous connection to epistemology, it may be less confusing to describe the system as a somewhat unusual algebra over a two-symbol alphabet (“0” and “1”). Instead of addition and multiplication, this algebra is commonly equipped with unary negation (NOT, sometimes shortened to ¬ or
!
), along with two-parameter conjunction (AND, ∧,
&&
) and disjunction (OR, ∨,
||
).
In this system, each operand can take just one of two values, so we can spell out the behavior of the operators in a pretty explicit, visual way:
\(\begin{array}{| c | c |}
\hline
\mathbfit{a} & \textbf{NOT }\mathbfit{a} \\
\hline
0 & 1 \\
1 & 0 \\
\hline
\end{array}\)
\(\begin{array}{| c | c | c | c |}
\hline
\mathbfit{a} & \mathbfit{b} & \mathbfit{a}\textbf{ OR }\mathbfit{b} & \mathbfit{a}\textbf{ AND }\mathbfit{b} \\
\hline
0 & 0 & 0 & 0 \\
0 & 1 & 1 & 0 \\
1 & 0 & 1 & 0 \\
1 & 1 & 1 & 1 \\
\hline
\end{array}\)
In a nutshell, negation flips the input value. OR yields “1” if one of the input values is non-zero, and produces “0” otherwise. Finally, AND is true only when both parameters are “1”.
The use of different operators means that the resulting algebra is not a field under the axioms discussed earlier in the article, although a bit surprisingly, it comes close. Grab a piece of paper and see for yourself: AND meets all the axioms for multiplication when all you can do is 0 · 0, 0 · 1, 1 · 0, and 1 · 1. On the other hand, OR can’t imitate addition because it lacks an additive inverse. The term of the trade for this not-quite-a-field is a
semiring
.
From the three canonical operators we started with, we can derive more. For example, we can construct exclusive-or (XOR, ⊕), which returns “1” if and
only
if one of the parameters is “1”. This can be done the following way:
\(a \text{ XOR } b := (a \text{ OR } b) \text{ AND NOT } (a \text{ AND } b)\)
In electronics, these transformations are implemented using circuits known as
logic gates
. This is the second time I mention “logic” in this section, so I should note that in some contexts, the behavior of these gates
can
be understood as inference over facts. For instance, a bank might hold a belief that a person who has a stable job and no history of late payments is creditworthy. They can enshrine this axiom in the architecture of the circuit, encode facts about your financials as input voltage levels, and render decisions according to the following Boolean scheme:
\(is\_creditworthy = is\_employed \text{ AND NOT } has\_delinquencies\)
Computer-style Boolean algebra has a finite domain, so it’s not powerful enough to embed the algebra of natural numbers. Nevertheless, it can deal with practical calculations. For example, if we represent a pair of numbers in base-2, addition looks the following way:
\(\begin{alignat}{2}
0_2 &+ 0_2 &= 00_2 \\
0_2 &+ 1_2 &= 01_2 \\
1_2 &+ 0_2 &= 01_2 \\
1_2 &+ 1_2 &= 10_2 
\end{alignat}\)
The behavior is analogous to base-10, except overflow and carry to the next column happens sooner — after we cross “1”, not “9”. If we split out the output digits, the following logic circuit will produce the same result:
\(\begin{align}
left\_digit &= a \text{ AND } b \\
right\_digit &= a \text{ XOR } b 
\end{align}\)
All this once again hints at curious parallels between logic systems and algebras; it’s why we can reason with numbers and prove mathematical theorems with voltages.
Before we wrap up, it’s worth noting that in abstract mathematics, Boolean algebras are often looked at through different lens. To illustrate, let’s start with a trio of hopefully familiar set-theoretic operators that are applied to subsets of some set
B.
We need union:
\(\{ \; a, b, c \; \} \cup \{ \; b, c, d \; \} = \{ \; a, b, c, d \; \}\)
…intersection:
\(\{ \; a, b, c \; \} \cap \{ \; b, c, d \; \} = \{ \; b, c \; \}\)
…and complementation in relation to
B
, which gives all elements of
B
that don’t appear in the complemented set. In other words, for
B
=
{ a, b, c, d }
and
X
=
{ b }
, the result is:
\(X\,' = \{ \;  a, c, d \; \}
\)
This sounds completely unrelated to binary logic as we know it, but consider the special case of a single-element set
B = { a }.
This set has two trivial subsets: an empty set
{ }
and a set containing
a.
Let’s label these subsets “0” and “1”:
\(\begin{align}
0 &:= \{ \; \} \\
1 &:= \{ \; a \; \}
\end{align}\)
In this scenario, if we calculate 0 ∪ 0, we get an empty set, or zero. All the remaining unions — 0 ∪ 1, 1 ∪ 0, and 1 ∪ 1 — will produce
{ a }
, aka 1. This is functionally equivalent to OR.
In the same vein, intersections 0 ∩ 0, 0 ∩ 1, and 1 ∩ 0 produce empty sets because they share no elements in common; meanwhile, the intersection of 1 and 1 is
{ a }
, so this operator is the same as AND. Finally, the complementation operator turns
{ a }
into
{ }
and
{ }
into
{ a }
— the same as NOT.
This has two noteworthy consequences. First, it ties logic to set theory — in the end, algebra, logic, and set theory are just parts of the same, incestuous family. It’s one more reason why we shouldn’t be particularly surprised that statistics mixed with matrix multiplication and executed on a video card can reason too.
Second, the trick lets us generalize Boolean algebra to multi-element sets, and thus, to more than two values; it’s something that mathematicians like to do, whatever that would mean in logic terms. Heck, we can even build countably infinite Boolean algebras if we’re in the mood.
Propositional logic is what you get if you ask the mathematicians to leave the room; it’s a more philosophical model of reasoning that arises when there’s no one to say
“what you have here is a semiring”
or
“I bet I could turn that into a set”
. It is functionally similar to Boolean algebra, but it’s expressed in a more humanlike way.
As suggested in the introduction, propositional logic deals only with declarative statements that can be assigned a single, binary truth value. These statements are known as
propositions
. Beyond this requirement, the system doesn’t interrogate the
meaning
of atomic statements; it allows the existence of opaque propositions such as
“I’m riding a bicycle
” without knowing anything about bicycles or the rest of the material universe. A sentence is true simply if we say so at the start. Because the inherent meaning of atoms doesn’t matter, propositions are often substituted with nondescript variables, such as
p
or
q
.
A sentence in propositional logic can be atomic, as shown above, or it can be constructed by nesting other propositions that are bridged by logical connectives. The most important connective is
material implication
, written as
p
⇒
q
,
p → q
, or
p
⊃
q.
The connective can be interpreted as
“p implies q”
or “
if p then q”
.
As discussed earlier, in standard formal logic, an expression in the form of
“if p then q”
, when taken as a whole, is false only if
p
is true while
q
is not. It’s not invalidated by the inverse or the converse:
q
can be true when
p
isn’t. Taking this into account, we can spell out the following truth table for this connective:
\(\begin{array}{| c | c | c |}
\hline
\mathbfit{p} & \mathbfit{q} &  \mathbfit{p \Rightarrow q} \\
\hline
false & false & \color{steelblue}{true} \\
\hline
false & true & \color{steelblue}{true} \\
\hline
true & false & \color{red}{false} \\
\hline
true & true & \color{steelblue}{true} \\
\hline
\end{array}\)
In a mind-bending tie-in to computer logic, the truth table for material implication is the same as what we’d write for
out
= (NOT
a
) OR
b
. In other words, the concept of implication feels semantically special
to humans, but it’s just an algebraic operation we can assemble from seemingly unrelated parts.
The table shown above tells us what value we assign to
“if p then q”
as a proposition when
p
and
q
are known. This is distinct from what the same statement, if taken as a true premise, tells us about the possible values of the underlying variables:
\(\require{color}
\begin{array}{| c | c |}
\hline
\mathbfit{p} & \mathbfit{p \Rightarrow q} \textbf{ says} \\
\hline
false & \color{gray}{\text{(nothing)}} \\
\hline
true & q \text { is true!} \\
\hline
\end{array}
\quad
\begin{array}{| c | c |}
\hline
\mathbfit{q} & \mathbfit{p \Rightarrow q} \textbf{ says} \\
\hline
false & p \text{ is false!} \\
\hline
true & \color{gray}{\text{(nothing)}} \\
\hline
\end{array}\)
Another important connective is
material biconditional
, aka equivalence. It can be written as
p
⇔
q, p ↔ q,
or
p ≡ q
. It means “
p if and only if q”
and in contrast to the earlier example, it does imply the inverse and the converse; as a proposition, it’s deemed false if it can be shown that the truth values of
p
and
q
differ:
\(\begin{array}{| c | c | c |}
\hline
\mathbfit{p} & \mathbfit{q} &  \mathbfit{p \Leftrightarrow q} \\
\hline
false & false & \color{steelblue}{true} \\
\hline
false & true & \color{red}{false} \\
\hline
true & false & \color{red}{false} \\
\hline
true & true & \color{steelblue}{true} \\
\hline
\end{array}\)
In Boolean logic terms, this is the same as the negation of the exclusive-or gate:
out =
NOT (
a
XOR
b
).
Compared to the material conditional, this statement — if taken as a true premise — has more to say about
p
and
q
:
\(\begin{array}{| c | c |}
\hline
\mathbfit{p} & \mathbfit{p \Leftrightarrow q} \textbf{ says} \\
\hline
false & q \text{ is false!} \\
\hline
true & q \text { is true!} \\
\hline
\end{array}
\quad
\begin{array}{| c | c |}
\hline
\mathbfit{q} & \mathbfit{p \Leftrightarrow q} \textbf{ says} \\
\hline
false & p \text{ is false!} \\
\hline
true & p \text { is true!} \\
\hline
\end{array}\)
The remaining common logical connectives mimic the standard choice of Boolean operators; they include negation (¬, ~), conjunction (aka AND, ∧), and disjunction (aka OR, ∨). Further, constants representing “true” and “false” may be cheekily written as ⊤ and ⊥.
In some texts, you may also encounter meta-logic annotations. “
M
⊨
A
” is an assertion that whatever’s on the left
semantically
entails
what’s on the right — i.e., that there is no possibility for
A
to be false in any reality that obeys the conditions spelled out by
M
. Because the circumstances given by
M
are sufficient for
A
to hold, we can say that
M
is
a
model of A
or that it
satisfies
A
.
A single proposition can have multiple models, and we can slice and dice them however we want. For example, this is fine:
\(\begin{align}
\text{“It's a sunny day."} &\vDash \text{“Bob likes ice cream."} \\
\text{“Aliens conquered Earth."} &\vDash \text{“Bob likes ice cream."}
\end{align}
\)
The two models may be describing incompatible versions of reality; even though Bob’s love of ice cream is evidently true in both, we might still want to analyze them separately. We’ll come back to this in a while.
More prosaically, we can use the symbol to explain the intended operation of formal logic by providing minimal models for certain outcomes; for example, we can say that when
p
and
q
are true, so is the conjunction
p
∧
q:
\(p, q \vDash (p \land q)\)
There’s also a closely related meta-symbol,
syntactic entailment
(“
M
⊢
A”).
This asserts (without showing) that under our chosen system of reasoning,
A
can be procedurally deduced from a specific set of premises,
M
. The difference between semantic consequence and syntactic provability matters in some contexts, but for the logic systems discussed in this article, they’re functionally the same.
Arguments in propositional logic are typically divided into premises and conclusions. To illustrate, let’s assume we’re given the following axiom consisting of two atomic sentences and an
if-then
connective:
\(\text{If }\underbrace{\text{the weather's nice}\vphantom{|}}_{p} \text{ then } \underbrace{\text{Bob is wearing shorts}\vphantom{|}}_{q}.\)
Further, let’s say that we’re given an atomic statement “
the weather’s nice” —
or, in more abstract terms, we’re told that
p
is true. These are our premises. Given that pair of starting points, we can conclude that Bob is wearing shorts — i.e., that
q
is true. Some authors may write the premises on top and conclusions on the bottom of a “fraction”, giving you notation like this:
\(\dfrac{p \Rightarrow q, \; \, p}{q}
\)
Again, propositional logic largely obeys common sense, but it resolves a couple of semantic gotchas in a specific way. Most of the wonkiness surrounds material implication, but we also require every sentence
p
to have a binary logic value:
p
∨ ¬
p
. Further, the system is 100% contradiction-intolerant: at all times, we need ¬(
p
∧ ¬
p)
.
Although it might seem uninteresting, that last detail is quite important. If we ignore the requirement and take
p
∧ ¬
p
as a true premise, we can prove literally anything, an effect known as the
principle of explosion
. The fact that a single contradiction can break an entire system of logic is part of the reason why
no one likes Kurt Gödel very much
.
To explain how the “explosion” happens, note that the conjunction (AND) operator in the premise is true only if both operands are true. This means that from the starting premise, we can infer both
p
and ¬
p
as separate truths. Next, we introduce a sentence
p
∨
q,
where
q
is the spurious statement we want to prove (e.g., “2 + 2 = 5”). We can do this because this entire sentence is true regardless of the truth of
q
; the disjunction operator (OR) is satisfied if
p
is true, and we know that’s the case.
So far, so good. But we also know that ¬
p
is true, which makes its negation (¬¬
p)
false; double negation obviously cancels out, so
p
is evidently false. We’ve previously used valid, formal reasoning to establish that
p
∨
q
is true. That fact is settled, but we’re now adding the knowledge that
p
is false. The only way for the already-proved disjunction to hold is if
q = “2 + 2 = 5”
is true.
Although propositional logic is quite useful, it doesn’t allow generalizations over objects. For example, it doesn’t let us formulate a rule that
“<x> is a child of <y>
” is equivalent to
“<y> is a parent of <x>
”, and then apply the rule to the premise
“Anne is a child of Sue”
to infer that
“Sue is a parent of Anne”.
Family relations aside, this makes it impossible to express many desirable mathematical axioms. For instance, we can’t symbolically assert that for any
a
in ℝ, there exists an additive inverse “-
a
” such that
a + (-a)
= 0.
To address this problem, first-order logic extends propositional logic with
predicates —
a function-style notation that allows us to specify properties that attach to objects, e.g.:
None of the individual words in this statement have any independent logic meaning; they’re just labels, no different from “xyzzy”, “glarp”, or “quux”
.
That said, the combination of a predicate symbol (“Child”) with a pair of objects (“Anne”, “Sue”) produces a well-formed proposition with a logic value. We can interpret this proposition as saying that Anne is Sue’s child.
We may use this predicate-object notation to say something like:
\(Child(Anne, Sue) \land Child(Sue, Bob) \Rightarrow Grandchild(Anne, Bob)\)
Or, in plain English: if Anne is Sue’s child and Sue is Bob’s child, then Anne is a grandchild of Bob. Note that we use ⇒ and not ⇔ because in real life, this implication is one-directional. Anne could be Bob’s grandchild even if Sue isn’t the common link.
To take this approach to the next level, we introduce variables and quantifiers. The universal quantifier (∀) selects one or more free variables and then applies the subsequent statement to every object in a context-dependent “universe of discourse”. For example, if we’re talking about humans, we can generalize the earlier grandchild rule as:
\(\forall a, b, c \bigl[ Child(a, b) \land Child(b, c) \Rightarrow Grandchild(a, c) \bigr]\)
This is saying that for any
a
,
b
, and
c
, if
a
is
b
’s child and
b
is
c
’s child, then
a
is a grandchild of
c.
In addition to the universal quantifier, first-order logic also allows existential quantification (∃), which means
“there exists”
— i.e., there’s at least one object for which the following formula is true. To illustrate, let’s assert that there exists a human who is Sue’s child:
\(\exists a \bigl[ Child(a, Sue) ]\)
We can also say that this child, whoever they might be, has a ponytail:
\(\exists a \bigl[ Child(a, Sue) \land HasPonytail(a) ]\)
First-order logic doesn’t know anything about sets, but it’s often used in the context of set theory. When you see
x
∈
A
in a logic expression, it can be understood as a shorthand for a predicate that defines (or inquiries about) an opaque relation between two objects. We can also write it as ∈
(x, A)
,
IsAnElementOf(x, A),
or
IsGlarp(x, A)
; as far the logic system is concerned, the talk of “sets” just human gobbledygook.
In addition to predicates, first-order logic also allows functions. The notation is similar to predicates, so the distinction is contextual. You can think of functions as external maps that translate one or more input objects into another object. An example would be
sum(x, y), x + y,
or the set-theoretic union operator,
A
∪
B
; all of these mean
“replace this with the object that is the result of the relevant operation under the chosen algebra”
. Note that a function can’t appear as a standalone proposition because it emits a bare object (e.g., “Sue” or “42”); such an object has no logic meaning.
First-order logic also has an equality operator, which amounts to a proposition that the compared objects are indistinguishable. The symbol has a couple of common-sense semantics attached to it; for one, any object is always equal to itself (
k = k
). There’s also the substitution property: if two objects are equal, they can be swapped at will. That is, if
k = l
, then any formula written with
k
is equivalent to the same formula written with
l.
The “=” operator can be seen in action in the Zermelo-Fraenkel set theory (ZFC) equality axiom. This is the axiom we opened with earlier in the article:
\(\forall A, B \bigl[ A = B \iff \forall x ( x \in A \iff x \in B )\bigr]\)
The notation says that for any set
A
and
B
,
A
is equal to
B
only if every object
x
taken from the universe of discourse is either simultaneously present in or absent from both sets. Or, in a more existential sense: under ZFC, sets are distinguished by their elements and nothing else.
It bears repeating that descriptions similar to the one above take liberties to express the meaning behind the syntax. As far as first-order logic is concerned, there’s no such thing as sets and there’s no concept of an object being contained in another. Fundamentally,
A
and
B
are just “things”, while
x
∈
A
is a shorthand for an inherently meaningless predicate ∈
(x, A).
If we want set-like behaviors, we need to write axioms that explain what the predicate does (the ZFC example above is a start). If we choose different axioms, we may instead get a universe of familial relations or something else entirely.
To be extra obtuse, Wikipedia and some other sources give the earlier set equality axiom as a one-way implication:
\(\forall A \forall B \bigl[ \forall x(x \in A \iff x \in B) \implies A = B \bigr]\)
This notation is saying that if sets have the same elements, they’re the same. But because ⇒ doesn’t imply the inverse, the phrasing leaves open the possibility that some sets could be equal even if the antecedent is false (i.e., they have different elements). What gives?
Well, it comes down to the aforementioned semantics of the equality operator; the substitution property says that if
k = l
, any relation involving symbol
k
is equivalent to the same relation written with symbol
l.
This makes sense: if one object can’t be a stand-in for the other, it doesn’t sound like they’re truly equal.
If we take
A = B
to be true, this substitution must be possible for the “is an element of” relation (∈) too. For any
x
, there should be no functional difference between
x
∈
A
and
x
∈
B.
That’s to say,
x
can be element of
A
if and only if it also appears in B. Based on this analysis, we can write:
\(A = B \implies \forall x (x \in A \iff x \in B)\)
In effect, one half of the needed equivalence is provided by the ZFC axiom, and the other half (in the opposite direction) arises from the built-in rules of first-order logic.
This is also a good demonstration that when mathematicians can choose between two equivalent ways of expressing an idea, they will often choose the option that feels clever but is harder to read.
Before we wrap up, let’s ponder if first-order logic can be considered “good enough” — that is, if its language is expressive enough to describe the mathematical structures we care about.
The answer is “sort of”. To explain, we can circle back to the set-theoretic construction of natural numbers (ordinals), as outlined in an
earlier article
. We start with an empty set and label it “0”. Next, we iteratively construct the ordinal 1 as { 0 }, 2 as { 0, 1 }, 3 as { 0, 1, 2 }, and so forth. The successor operation to create
n
+ 1 from
n
is:
Although this set-nesting scheme is a bit contrived, it has a nice properties. First, it doesn’t require any objects other than what the set theory already gives us for free. Second, the essential ordering relation
“a
≤
b”
becomes equivalent to “
a
∈
b
”, making it very easy to express.
In Zermelo-Fraenkel set theory, this underlying structure appears to be enshrined in the axiom of infinity. The axiom, written in the language of first-order logic, asserts the existence of an infinite set such that an empty set is a member of it, and that for any
x
, if
x
is in the set, then so is the object produced by the successor function S(…):
\(\exists A \bigl[ \{ \, \} \in A ∧ \forall x (x \in A \implies S(x) \in A ) \bigr]

\)
More precisely, the rule says that there exists an opaque object we arbitrarily call “{ }” that has an opaque relation “∈” to another mystery object, A. That’s our concept of a zero. If zero has this relation to A, then so does S(0) — an object resembling 1. If 1 satisfies the criteria, then so must S(1), aka 2. Rinse, repeat. At first blush, this looks a lot like the set of natural numbers, ℕ.
But… is it? Other ambiguities aside, the axiom only specifies which objects
must
be included, not which ones
cannot
. For example, it doesn’t prohibit a distinct element labeled 🐷. The element can’t be one of the S-successors of the empty set — all of these are accounted for in the “main” sequence of what we want to be naturals — but it could be a part of a separate, unmoored succession chain that stretches to infinity. The underlying pig-containing mathematical structure, if crafted with care, could give us consistent arithmetic not just 2 + 2, but also for 2 + 🐷.
In first-order logic, we can’t really really excise these demons. In a throwback to the discussion of semantic entailment, our number-system axioms are satisfied by multiple models; some of these models give us the minimal,
“sunny day”
version of the set we intended to build. Others represent the
“aliens invaded Earth”
scenario, full of unwanted numbers and other horrors from the deep. These extra elements usually don’t harm us, but impossibility of zeroing in on the
“sunny day”
scenario makes the foundations of math a bit more murky than we assume.
The problem can be solved by devising a logic system with higher expressive power. Alas, this comes at a price: there are proof techniques that work only if the system isn’t too clever in what it asserts. For now, first-order logic appears to be the sweet spot.
Here are some related posts you might enjoy:
I write original, in-depth articles about electronic circuit design, mathematics, geek culture, and more. If you like what you see, please subscribe.
