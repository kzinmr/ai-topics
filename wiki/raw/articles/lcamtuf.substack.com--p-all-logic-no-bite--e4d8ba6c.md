---
title: "All logic, no bite"
url: "https://lcamtuf.substack.com/p/all-logic-no-bite"
fetched_at: 2026-06-27T07:01:07.331794+00:00
source: "lcamtuf.substack.com"
tags: [blog, raw]
---

# All logic, no bite

Source: https://lcamtuf.substack.com/p/all-logic-no-bite

Today, I’d like to talk about logic — and before I do, I should probably explain why. But before we get to that, a definition may be in order: in a nutshell, logic is a system for drawing conclusions from premises (“facts”).
Formal logic usually isn’t taught in high school; as far as I know, it’s not even a requirement for most computer science degrees. The concept is familiar to most mathematicians and to a handful of software engineers who dabble in esoteric programming languages. As for everyone else, we might know about “digital logic”, a simple algebra of binary numbers that involves operators such as AND, NOT, and OR. What’s less clear is how we get from zeroes and ones to some semblance of human reasoning.
For mathematicians, the most common role of formal logic is to provide a more precise vocabulary for proofs. To illustrate some of the ambiguities of everyday speech, consider the following statement in the form of
“if A then B”:
\(\text{“If }\underbrace{\text{you finish house chores}\vphantom{\biggl(}}_{A}\text{, }\underbrace{\text{you can play Minecraft}\vphantom{\biggl(}}_{B}\text{.”}\)
It’s something a parent could say to a child. In that use, the phrasing clearly implies its own inverse,
“if not A then not B”:
\(\text{✅ "If you }\textbf{don't}\text{ finish chores, you }\textbf{can't}\text{ play Minecraft."}\)
On the flip side, it probably doesn’t imply its converse (
“if B then A”
) or the contraposition
(“if not B then not A”
). I say “probably” because there’s a temporal relationship baked into the order of the propositions; if we reverse it, we end up with mild gibberish:
\(\text{❓ "If you }\textbf{can't}\text{ play Minecraft, you }\textbf{don't}\text{ finish chores."}\)
Do all other
“if A then B”
statements play by the same rules? Nope:
\(\text{“If }\underbrace{\text{my cat is hungry}\vphantom{\biggl(}}_{A}\text{, }\underbrace{\text{it meows}\vphantom{\biggl(}}_{B}\text{.”}\)
This time around, the phrasing doesn’t imply the inverse (
“if not A then not B”
). The speaker isn’t suggesting that Mr. Mittens meows only when it wants to eat. Therefore, we can’t infer the following:
\(\textrm{❌ }{\text{“If }{\text{my cat }\textbf{isn't }\text{hungry, it}\textbf{ doesn't}\text{ meow."}}}\)
On the flip side, if the original assertion is true — if the cat always begs for food — the contraposition (
“if not B then not A”
) follows in a straightforward way:
\(\text{✅ "If my cat }\textbf{doesn't }\text{meow, it }\textbf{isn't }\text{hungry."} \)
Our problems with cat logic don’t end here. Next, let’s consider the following:
\(\text{“If }\underbrace{\text{grass is green}\vphantom{\biggl(}}_{A}\text{ then }\underbrace{\text{kittens are cute}\vphantom{\biggl(}}_{B}\text{.”}\)
Both A and B are true, but most people would peg the statement as false — or at least
wrong
. The truths coincide, but we reject the argument because the concepts are not connected in any obvious way.
But what if I told you that every Sunday morning, Bob wakes up with a headache?
\(\text{“If }\underbrace{\text{it's Sunday morning}\vphantom{\biggl(}}_{A}\text{ then }\underbrace{\text{Bob has a headache}\vphantom{\biggl(}}_{B}\text{.”}\)
As before, I don’t know what’s the connection. Maybe there isn’t one; maybe the timing of Bob’s migraines is just a cosmic coincidence. In this context, a coincidence is good enough to accept the claim.
It’s not just the
if-then
connective that’s cursed; the A and B atoms are also suspect. In our examples, they appear to be declarations of facts — but can we proclaim anything we want? If I say
“this statement is false
”, is that a truth or a falsehood? Neither? Both?…
These semantic gotchas are great if you’re devising brain-teasers for nerds; they’re not helpful if you’re writing down a mathematical argument. This is why mathematicians rely on formal logic to define some predictable ground rules. The classic approach is pretty close to common sense, but it resolves the ambiguities by making several ad hoc calls. In particular:
A statement in the form
“if A then B”
does not
imply its inverse (
“if not A then not B”
). The assertion that Mr. Mittens meows when hungry doesn’t rule out meowing for other causes.
By extension, the syntax
does
not
imply the converse (
“if B then A”
). If you hear meowing, it’s not a given that the cat wants to be fed.
On the flip side, the construction
does
imply its contraposition
(“if not B then not A”
). No meows is proof positive that the cat had its meal.
To prove
“if A then B”
, it’s sufficient to show that B is true whenever A is true. There’s nothing wrong with
“if grass is green then kittens are cute”.
The system only deals with statements that can bear a binary truth value. We don’t allow “neither” or “both”.
Logic statements expressed with words are easy to grasp, so to keep the riff-raff out, mathematicians often resort to symbolic notation. For example, the idea that sets A and B are equal to each other if and only if they contain the same elements can be more enigmatically spelled out as:
\(\forall \mathrm{A} \forall \mathrm{B} \bigl[ \forall x ( x \in \mathrm{A} \iff x \in \mathrm{B}) \implies \mathrm{A} = \mathrm{B}\bigr]\)
My initial plan for this article was to dive into this symbology next. But on second thought, before we do, it may be useful to show how formal logic acts not only as a convenient language for proofs, but as the
source
of math.
Arithmetic is the oldest branch of mathematics; it’s also notable for having resisted attempts at formalization for a pretty long time. As it turns out, it’s tricky to explain numbers and arithmetic operations as anything other than “the things you know”.
Regular readers may recall two earlier articles about some of the successful efforts to construct the arithmetic of natural numbers and reals from scratch. In the end, we took the existence of an empty set as a given and then defined numbers and operations through the repeated application of several fairly intuitive rules:
The beauty of this method is that it gave us more than what we already knew. For example, it seamlessly generalized to operations on infinite numbers, with mildly surprising results.
Unfortunately, in math textbooks, explanations from first principles aren’t the rule. Many of the discipline’s foundational axioms stem from investigations of the natural world, but we prefer to teach the craft as if it owed nothing to reality. In the modern academic practice, the question of where the idea came from, or whether it’s ontologically correct, is considered vacuous and out of scope. For the most part, you’re just handed a rulebook to play someone else’s game.
In the remainder of the section, I’ll try to kill two birds with one stone. First, we’ll look at yet another method of constructing the reals to develop intuition that will pay off once we get to digital logic, aka Boolean algebra. Second, on the topic of my mini-rant about mathematical education, we’ll note that the use of logic doesn’t necessarily make one’s arguments easy to justify.
The usual axiomatic approach to defining reals is to give students a collection of roughly fourteen ad-hoc rules for manipulating the elements of an otherwise opaque set we call “ℝ”. The axiomatic method doesn’t care what the set contains or what it
means
; the method doesn’t even posit the existence of any canonical version of ℝ. The point is just that we can imagine the existence of some sets that, by an unseen mechanism, obey the specified rules.
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
To distinguish between the two operators, the axioms also assert the existence of additive and multiplicative identities. By that, we mean a pair of elements in ℝ, conventionally labeled “0” and “1”, such that for any
a
∈ ℝ, the following equalities always hold true:
\(\begin{array}{c}
a + 0 = a \\
a \cdot 1 = a
\end{array}\)
Again, the model doesn’t concern itself with the “why” or the “how”; all we’re saying is that in a system that obeys the axioms, there must be a pair of elements for which the equalities hold. And if these elements exist, we might as well label them in a familiar way.
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
Perhaps surprisingly, these rules are already good enough to perform calculations in ℝ. By combining the axioms, we can easily prove that there can be only one additive identity (“0”), one multiplicative identity (“1”), and that “0” and “1” can’t be the same. Next, because addition always produces a result in ℝ, we conclude that there is a real associated with the value of 1 + 1. If we label this real “2”, we can for example show the following:
\(a \cdot 2 = a \cdot \underbrace{(1 + 1)}_{\substack{\text{by our} \\ \text{definition} \\ \text{of "2"}}} = \underbrace{a \cdot 1 + a \cdot 1\vphantom{)}}_{\substack{\text{expanded in line} \\ \text{with the distributive} \\ \text{property}}} = \underbrace{a + a\vphantom{)}}_{\substack{\text{eliminating} \\ \text{multiplicative} \\ \text{identities}}}\)
Alas, field axioms do not provide complete “driving directions” to the reals. There are many different fields; for example, the exact same axioms are also satisfied by
complex numbers
. Heck, we can even make the rules work for certain types of finite sets, giving us modulo arithmetic systems that have applications in cryptography, but that would be frowned upon on a tax return. The smallest possible finite field needs just two elements: “0” and “1”, with the result of 1 + 1 simply wrapping around.
In any case, to get closer to the destination, we continue with order axioms. We begin by proposing that for any
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
. Further, to tie the behavior of the less-than operator to existing algebraic rules, we give the following rules for any
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
If you made this far, you might be wondering why I grumbled about how we teach math. Sure, we get a lot of axioms dumped at our doorstep at once with little justification, but they’re all saying reasonable things.
The answer is that we’re not done yet: the rules we have in place are also valid for rational numbers (ℚ). To get to a ruleset that unambiguously describes reals, we need to toss in the axiom of completeness.
To explain the usual phrasing of the axiom, we must first talk about subsets and their bounds. If we have the set of real numbers, it stands to reason that we can take a subset of it. For example, we can construct subset A that consists of every real less than or equal to 2. Or, we may conjure subset B that contains all numbers divisible by 42.
A subset of an ordered set may be
bounded above
; this means that in the parent set, we can find an element that’s greater than or equal to every element included in the subset. Any number that meets this criteria qualifies as the upper bound; for A, it can be any value ≥ 2. In contrast, for subset B, there’s no bound in ℝ.
It stands to reason that a subset that’s bounded above may also have a
least
upper bound. That’s to say, among the values that qualify as the upper bound, there might be some definite “minimal” choice. For subset A, this is 2. Any value less than that can’t work because some elements of A would end up above the selected bound.
With these preliminaries out of the way, the completeness axiom says that any non-empty subset of ℝ that is bounded above in the reals must also have a least upper bound in the reals.
That’s it. And —
what just happened
? We went through all this effort that say something that feels borderline meaningless?… At the same time, the rule is essential. For one, ℚ doesn’t obey it, for reasons that are left as an exercise for the willing reader. Just as important, we need the axiom to prove the Archimedean property. This property says that if we take any two positive reals such that
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
, or an infinitesimal for
a
. This means that the property implies the absence of infinities or infinitesimals in reals. This is critical to a good chunk of higher math; for example, it allows us to justify limits in calculus.
Had we attempted the set-theoretic approach outlined in the earlier posts, the Archimedean property would arise as a natural consequence of the construction of reals via Dedekind cuts. But to prove it in the axiomatic model, we need the mildly perplexing completeness axiom. This invites but never answers questions such as
“where did that idea come from?”
and “
could we get better-behaved algebra if we phrased it in a different way?
”
.
In any case, let’s prove the Archimedean property, the axiomatic way. We choose an arbitrary positive pair
a < b
and then construct a set C that consists of all the natural-number multiples of
a
:
\(\text{C} = \{ 0a, \; 1a, \; 2a, \; 3a, \; 4a, \; 5a, \; \ldots \}\)
When structured this way, C is obviously a subset of ℝ.
Next, we assume that the Archimedean property does
not
hold: that there can be some
a < b
pair such that every multiple of
a
— i.e., every element of C — is still less than
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
is the smallest real that’s still greater or equal than all the elements of C; if we pick any number less than that, there must be at least one member of C
that exceeds it.
In other words, there must be some element of C that’s greater than
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
+ 1. This should make it a member of C. At the same time,
s
is the least upper bound of C, so it can’t possibly be less than any existing element of that set. Oops?
We assumed that the Archimedean property doesn’t hold and we ended up with a contradiction. In standard two-valued logic, if a property can’t be false, it must be true — so that’s our proof.
For the few readers who are still here, I hope that this lengthy exposition underscored two interesting points. First, it would appear that given a sufficiently capable system of logic, we can build an algebra without needing any
a priori
notion of numbers or arithmetic operators. And second: we like to teach math in confusing ways.
Up until this point, we talked about logic as a way to formalize mathematical reasoning, but most readers of this blog are probably more familiar with the logic of digital circuits. In computing, the term “logic” may seem suspect: it’s true that the field leans on importantly-sounding keywords such as “true” and “false”, but by the end of the day, we’re just manipulating voltages.
Because of the tenuous connection to epistemology, it may be less confusing to describe the system as a somewhat unusual algebra over a two-symbol domain (“0” and “1”). Instead of addition and multiplication, this algebra is commonly equipped with unary negation (NOT, sometimes shortened to ¬ or
!
), along with two-parameter conjunction (AND, ∧,
&&
) and disjunction (OR, ∨,
||
).
In this model, each operand can take just one of two values, so we can spell out their behavior in a pretty transparent way:
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
The use of a different set of operators means that the result algebra is not a field, although it actually comes close; the only issue is that the latter two operators can’t possibly have inverses — see if you can figure out why. The term of the trade for this not-quite-a-field is a
semiring
.
From the three canonical operators we started with, we can derive more. For example, we can construct exclusive-or (XOR, ⊕), which returns “1” if and
only
if one of the parameters is “1”. This can be done the following way:
\(a \text{ XOR } b := (a \text{ OR } b) \text{ AND NOT } (a \text{ AND } b)\)
In electronics, these transformations are implemented using circuits known as
logic gates
. This is the second time I mention “logic” in this section, so I should note that in some contexts, the behavior of the gates can be understood as inference over facts. For example, if we hold that a a person who has a stable job and no history of late payments is creditworthy, we can encode these facts as input voltages and design the circuit to render decisions according to the following scheme:
\(is\_creditworthy = is\_employed \text{ AND NOT } has\_delinquencies\)
Computer-style Boolean algebra has a finite domain, it’s not powerful enough to embed the algebra of natural numbers. Nevertheless, it can deal with practical calculations. For example, if we represent a pair of numbers in base-2, addition looks the following way:
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
All this once again hints at a curious equivalence between logic systems and algebras; it’s why we can reason with numbers and prove mathematical theorems with voltages.
Before we wrap up, it’s worth noting that in abstract mathematics, Boolean algebras are often looked through different lens. Imagine a trio of familiar set-theoretic operators that are performed on subsets of some set
B.
We need union:
\(\{ \; a, b, c \; \} \cup \{ \; d, e, f \; \} = \{ \; a, b, c, d, e, f \; \}\)
…intersection:
\(\{ \; a, b, c \; \} \cap \{ \; b, c, d \; \} = \{ \; b, c \; \}\)
…and complementation in relation to
B
, which gives all elements of
B
that don’t appear in the complemented set. In other words, for
B
=
{ a, b, c }
and
X
=
{ b }
, the result is:
\(X\,' = \{ \;  a, c \; \}
\)
This sounds completely unrelated to Boolean algebras as we know them, but consider the special case of a single-element set
B = { a }.
This set has two trivial subsets: an empty set
{ }
, which we can call “0”, and a set containing
a,
which we can label “1”.
In this scenario, if we calculate 0 ∪ 0, we get an empty set, or zero. All the remaining unions — 0 ∪ 1, 1 ∪ 0, and 1 ∪ 1 — all produce
{ a }
, aka 1. Semantically, this is equivalent to OR.
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
This has two interesting consequences. First, it ties logic to set theory — in the end, algebra, logic, and set theory are just parts of the same, incestuous family. Second, the trick lets us generalize Boolean algebra to higher numbers of symbols, some of which may have a complex internal structure; heck, we can even build infinite Boolean algebras if we’re in a mood.
Propositional logic is what you get if you ask the mathematicians to leave the room; it’s a more philosophical model of reasoning that arises when there’s no one to say
“what you have here is a semiring”
or
“I bet I could turn that into a set”
.
Propositional logic deals only with declarative statements that can be assigned a single, binary truth value. These are, fittingly, known as
propositions
. Beyond this requirement, the system doesn’t interrogate the
meaning
of atomic statements; it allows the existence of opaque propositions such as
“I’m riding a bicycle
”. Because of this, propositions are often substituted with nondescript variables, such as
p
or
q
.
A sentence in propositional logic can be atomic, but it can also be constructed by nesting other propositions that are bridged by logical connectives. Probably the most important connective is
material implication
, written as
p
⇒
q
and meaning
“p implies q”
or “
if p then q”
.
As discussed earlier, in standard formal logic, a statement in the form of
“if p then q”
can be deemed false only if we show that
p
is true while
q
is not. It doesn’t imply the inverse (
“if not p then not q”
). Because of this, another important connective is
material biconditional
, aka equivalence. It can be written as
p
⇔
q
or
p ≡ q
; it means “
p if and only if q”.
This one does imply the inverse; it’s deemed false if it can be shown that the truth values of
p
and
q
differ.
The remaining common logical connectives largely overlap with Boolean operators; they include negation (¬, ~), conjunction (aka AND, ∧), and disjunction (aka OR, ∨). In some texts, you may also encounter meta-logic annotations, such as “⊨” to signify that in author’s analysis, whatever is on the left entails what’s to the right.
Statements in propositional logic are typically divided into premises and conclusions. To illustrate, let’s assume we’re given the following axiom consisting of two atomic sentences and an
if-then
connective:
\(\text{If }\underbrace{\text{it’s Sunday morning}}_{p} \text{ then } \underbrace{\text{I’m riding a bicycle}}_{q}.\)
Further, let’s say that we’re giving an atomic premise “
it’s Sunday morning” —
or, in more abstract terms, we’re told that
p
is true. These are our premises. Given that pair of starting points, can conclude that you’re riding a bicycle — i.e., that
q
is true.
Again, propositional logic largely obeys common sense, but it resolves a couple of semantic gotchas in a specific way; for example,
p
⇒
q
doesn’t automatically suggest that ¬
p
⇒
¬
q
. The system also requires every sentence to have a binary logic value (
p
∨ ¬
p
) and is 100% contradiction-intolerant: it must be that ¬(
p
∧ ¬
p)
.
Although this detail might seem uninteresting, the last rule is quite important. If we take
p
∧ ¬
p
as a premise — that is, if we assume that there’s a statement
p
that’s true and false at the same time — we can prove literally anything, an effect known as the
principle of explosion
. This is also why
no one likes Kurt Gödel very much
.
To explain how this happens, note that the conjunction (AND) operator in the premise is true only if both operands are true. This means that from the starting premise, we can infer both
p
and ¬
p
as separate, true facts. Next, we introduce a sentence
p
∨
q,
where
q
is the spurious statement we want to prove (e.g., “2 + 2 = 5”). This entire sentence is valid regardless of the truth of
q
because the disjunction operator (OR) is satisfied if
p
is true.
So far, so good. But we also know that ¬
p
is true, which makes its negation (¬¬
p)
false; double negation obviously cancels out, so
p
is evidently false. We’ve previously established that
p
∨
q
is true and we now know that
p
is false. The only way for the disjunction operator to give us the result it must give is if
q = “2 + 2 = 5”
is true.
Although propositional logic is quite useful, it doesn’t allow us to generalize. For example, it doesn’t allow us to formulate a rule that says “
if <x> is the child of <y>, then <y> is a parent of <x>”
and then apply it to the premise that Anne is a child of Mary to infer that Mary is a parent of Anne. Family relations aside, this makes it impossible to formalize many desirable mathematical axioms, such as that for every
n
∈
ℕ,
n
+ 1 should also be in
ℕ.
To address this problem, first-order logic extends propositional logic with
predicates —
a function-style notation that allows us to specify the properties of objects, e.g.:
None of the individual words in this statement have any independent logic meaning; that said, the application of a predicate symbol (“Child”) to a pair of objects (“Anne”, “Mary”) produces a well-formed proposition with a logic value that we can interpret as saying that Anne is Mary’s child.
We can use this syntax to make more complex assertions, such as:
\(Child(Anne, Mary) \land Child(Mary, Bob) \Rightarrow Grandchild(Anne, Bob)\)
Or, in plain English: if Anne is Mary’s child and Mary is Bob’s child, then Anne is a grandchild of Bob.
To take this model to the next level, we introduce variables and quantifiers. The universal quantifier (∀) says that the statement that comes next is true for all possible values of the attached variable. For example, we can generalize the earlier grandchild rule as:
\(\forall a, b, c \bigl[ Child(a, b) \land Child(b, c) \Rightarrow Grandchild(a, c) \bigr]\)
This is saying that for every
a
,
b
, and
c
, if
a
is b’s child and b is c’s child, then
a
is the grandchild of
c.
This syntax assumes some sensible “universe of discourse” from which the objects are picked; if this isn’t clear from the context, we could, for example, say “
a, b, c
∈
P”,
where
P
is the set of all people.
In addition to the universal quantifier, first-order logic also allows existential quantification (∃), which means
“there exists”
— i.e., there’s at least one object for which the following sentence is true. To illustrate, let’s assert that there exists a human who is Anne’s parent:
\(\exists a  \bigl[ Child(Anne, a) ]\)
There’s a bit more to first-order logic; for example, it also also allows functions, which use a notation similar to predicates. You can think of a function as an external lookup table that maps one object to another. This is useful because we can write
sum(x, y)
instead of trying to define addition from first principles. In the same vein, first-order logic has an equality operator that compares any two objects and emits a proposition that’s either true or false. This is what can be seen in the Zermelo-Fraenkel set theory (ZFC) equality axiom presented early in this article:
\(\forall \mathrm{A} \forall \mathrm{B} \bigl[ \forall x ( x \in \mathrm{A} \iff x \in \mathrm{B}) \implies \mathrm{A} = \mathrm{B}\bigr]\)
It just says that for every set
A
and
B
, if every
x
is either simultaneously present or absent in both sets, it’s true that set
A
is equal to set
B
.
