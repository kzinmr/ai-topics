---
title: "unpublished blog posts"
url: "https://jyn.dev/unpublished-blog-posts/"
fetched_at: 2026-11-23T10:10:16.223928+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# unpublished blog posts

Source: https://jyn.dev/unpublished-blog-posts/

i am officially declaring bankruptcy on blog post ideas.
i have too many ideas and not enough time or focus to write them all.
some of them i've been planning for literal years and if they haven't happened by now they're probably not going to happen.
here is a very short summary of all of them.
note: some of these bullets are
not
cleaned up and will probably piss people off. oh well.
misc technical
Why can't the Rust compiler just figure out the lifetimes for me?
Requires global analysis. Global analysis is bad actually.
c.f. global inference in Haskell
Rust
could
elide lifetimes in more cases than today (in particular in ADTs). But either the syntax would be confusing, or you would have no way to name the lifetime.
Similar to how turbofish isn't allowed for elided lifetimes in functions, but worse because it applies to types and not just values. Limiting for cross-crate annotations.
RDP bound to a Tailscale interface + Yubikey
typed clojure
including redefining types at runtime in the repl
opt out types instead of opt in
similar premise to Julia's type system
actually i wonder if i could make a Clojure that compiled to Julia ...
Writing CI scripts in Clojure
YAML is a bad language. Write in a better language that compiles to YAML.
At this point, you may as well go all the way around the
Configuration Complexity Clock
.
It turns out Clojure is nice for data structures actually.
Why not EDN? Better ask, why EDN? Having functions is nice. You don't need templates if you have a proper language.
What about purity? Just sandbox the whole thing, yank out the I/O from the standard library. The halting problem is not actually important in practice.
Haha psych this was actually a post about build systems. Don't need a Makefile if you have a proper standard library.
Prior art: Shake. But Shake is too powerful; declarative builds are nice actually.
Prior art: Starlark. Clojure doesn't actually have much advantage over Starlark, I just like it better. Also you can easily represent enums without newtypes by using
:keywords
.
c.f.
build system tradeoffs
and
action graph serializations
features-oriented vs maintenance-oriented
inherently in conflict
maintainer always ends up as a gatekeeper, saying "this is hard for reasons you aren't aware of". a lot of work for them and a lot of disappointment for the person who wants a new feature
think this is responsible for a lot of burnout within complex years-long projects, especially open-source projects
i want to find some way for the person who wants a feature to be the one responsible for finding a mechanism whereby it can work
c.f. Rust RFCs are solution-oriented when they should be problem-oriented
one possible solution is to decentralize development so more things can be built as forks / plugins / libraries, without needing to support every single use case in Postgres/Rust
i want a better paradigm for OS infrastructure
like Nix, but you can
curl | sh
and still get atomic rollbacks
without writing a packaging script
c.f. Fedora Atomic. kinda. not really.
need tracked writes.
orthogonal persistence
solves a lot of these problems
how to use a debugger effectively
you're not tricking me into writing this post through bullets dear god the last time i tried i spent three hours and threw the whole mess away
AI is better at these days at mechanically using a debugger than i am, but sometimes you can still give it useful ideas it turns into commands
how i built
x clippy
unreasonably difficult, partly because sysroots and partly because staging confusion in bootstrap itself
clippy also doesn't expect its runtime and compile-time sysroot to be different, which didn't help
how Linux input works
kernel level (
keyd
)
kernel framebuffer (only in proper TTYs, not PTYs)
Xcompose (X.org)
IMEs (ibus)
turns out the IMEs reimplement a lot of the Xcompose stack because it's not flexible enough. oops!
turns out that RAlt (kernel level) is
not
the same as what GNOME and friends call "Right Alt" (X.org level)
when to split git repos
splitting at the VCS level is different from splitting at an interface boundary
use compilation units for the latter
you can still have microservices! microservices are different from repo boundaries! you just have to be disciplined about import trees. tooling can help.
splitting into multiple repos is
usually
a mistake
most splits are along team boundaries, for Conway's Law reasons. this is a bit silly. use CODEOWNERS instead.
worst of all worlds is when no team feels responsible for a repo
docs should almost always be in the same repo unless your CI times are absolutely brutal. in that case they should be a subtree.
things that are released together should be versioned together
releasing 5-10 different repos to make a single change absolutely sucks and makes mistakes more likely
in general i think you have to be
very
large before separate repos make sense
main motivator is CI time + build system that can't handle incremental retesting
separate issue trackers can also be a motivation when using GitHub. have you considered using a better issue tracker, though?
the build system i want instead of Cargo
psych Amos already built it it's called Vixen
also very similar to my existing
four posts about build systems
Buck/Bazel are
not
this because they're too hard to use and have high switching costs
what's wrong with cargo anyway?
prior art
it's impossible to detangle the different parts
you can't say "replace Cargo's built-in executor with Ninja or my distributed/hermetic executor"
no way to sandbox just build scripts, you have to sandbox the whole build graph. Cargo also wants to own its cache dirs which makes sandboxing harder.
you can't opt out of feature unification
the declarative language is not flexible enough
Cargo is intentionally not general purpose, which is fine, but makes it frustrating when everyone insists your project should build with Cargo
you simply cannot write integration tests for build scripts
closely related, you can't have "staged builds"; builds are at the package level and even then many commands only support packages in the workspace
many things that could be declarative require compiling a build.rs instead
it's not sound or minimal
rebuilds all the time for silly reasons
needed to add a new
[lints]
table to just to avoid rebuilding the world when you add
-A unused
--deny=warnings
needed its own special configuration option built on top of Rustc JSON output
doing things this way legitimately makes the UX nicer than a naïve approach that rebuilds everything in the workspace! but there's no middle ground between "rebuild the world" and "dedicated Cargo feature"
no way to make the cache key content-hashes rather than timestamps
no way to express negative dependencies (admittedly this is true of ~all build systems i know about)
no way to cache tests (for incremental re-testing)
build scripts are very very poorly supported
if you get it wrong, tough luck
not possible or practical to express all the dependencies a build script has
no interface for expressing which system packages you depend on. in practice people often end up vendoring C source code and building it from scratch inside the build script.
workspaces, .cargo/config, and user-wide config don't interact well
you can't query it very well
cargo metadata is simultaneously too much info (slow, heavy) and too little (works at the wrong level of abstraction for many use cases)
you can't ask "what would be rebuilt next time" except by actually building
you can't ask "what files were used on the last run" except by parsing .d files yourself
you can't ask "what source code corresponds to this built
.rmeta
file" — in particular cargo semver-checks wanted this so it didn't have to rebuild the world to get cross-crate links from rustdoc-json
poor discovery for the underlying commands it wraps; inconsistent where it adds wrapping flags or requires
--
style forwarding
the difference between compiling for the host and cross-compiling is stupidly complicated for no good reason other than back-compat
just adding
--target $(rustc --print=host-tuple)
changes behavior!
complications around proc-macros and build scripts, caused docs.rs no end of trouble
design:
start by importing Cargo metadata from Cargo.toml, so that 80% of builds can still be declarative.
have a FUSE filesystem that tracks reads and writes
for platforms that don't support FUSE, fall back to .d files
record accesses in a way similar to tup. notice and rebuild when the accessed files change.
if processes are interrupted, delete all the artifacts they created in the latest (partial) run (this also fixes "ctrl-c breaks incremental linking sometimes").
extend the tup model to system dependencies by strace-ing all spawned processes. rebuild if a system dependency changes.
don't need reproducibility for our purposes, just rebuilding on file changes is enough
tracking environment variables
is hard
, but we can still get quite a long ways by tracking FS access
we could allow trading back-compat for additional correct guarantees: opt-in mode where only the env variables you explicitly declare are available in a build script
disallow setting
-l
and
-L
; instead require that build scripts print the path to all shared objects they want to link. rebuild if any of those change.
expose all this info with a nextest-like query language
for example RA could ask "all used files" cheaply (because it's cached from the previous build)
this would be the main interface for build scripts; they could say "give me the registered C compiler for this target" using the same query language as external processes
build in a dumb executor (something like what cargo has today). have a plugin (or builtin) that uses the query language to export to .ninja.
do the cmake thing where ninja automatically recreates its files if it needs to.
what does this actually get you?
partial/staged builds (e.g. running integration tests on a build script)
artifact dependencies are not flexible enough for this
running arbitrary commands over the build graph
e.g.
-Z rustdoc-scrape-examples
for arbitrary crates, without needing native cargo support
proper dependency tracking for build scripts
"the burden of proof for screwing with a principled caching system is really high IMO. you need to actually prove to yourself somehow that the behaviour isn't going to change because otherwise you're exposing people to horrible caching bugs"
weird example: glibc upgrades between builds
the Nix-hater's handbook
i am opposed philosophically
i should not need to package a program to use it!
i should not need to debug glibc errors to use programs!
or at very least, the glibc errors should be because i'm writing a compiler and i have a bug
on Nix, i literally cannot tell if the errors are my fault or Nix's fault
yes i know about buildFHSEnv. no that doesn't solve it—if i use that, i'm basically opting out of Nix and may as well use a more normal distro/package manager.
i should not need to use the Nix language to use nixpkgs!
there's literal person-decades of knowledge about how Unix works locked inside those packages, but i can't use them except by writing .nix derivations. i want to call nixpkgs as libraries!
i should be able to compose build systems!
no, i don't mean "Nix should be able to call my build system", i mean "my build system should be able to call Nix"
why do i have to think about a "Nix runtime environment"? why are all of Nix's build paths tied to the nix store?
yes i know why this is true in a technical sense, but why should i
as a user
have to think about it?
you are solving a problem that most people do not need to solve!
Nix solves "i have three versions of libLLVM.so on my system and i need to keep them all straight"
but most people use it as a package manager
if you just need a project manager, you can use mise-en-place or the dozen other things like it
if you need a system-wide package manager, what was wrong with the existing ones?
if you want a user-wide configuration manager, you can use dotbot or the dozen other things like it
if you want a system-wide configuration manager, admittedly the options for that are pretty slim, but you could build one that's a
lot
simpler than Nix
i am opposed technically
your docs are not good
no, REPLs don't make up for bad docs
your errors are not good
your language is hard to understand and use
your evaluator is dog slow
why is half the nixpkgs standard library written in shell script ....
your culture of shell
and
rewriting the world leads to silly bugs like "someone forgot to shell-quote the linker arguments" that are hell to debug on the downstream side
in general it feels weird that your isolation is designed to be correct-by-construction and yet everything else is a pile of hacks? i mean i've written hacks myself, but the contrast feels weird
your naming is needlessly confusing
did we really need a "the trinity is separate and unified at the same time" meme for the word "Nix"
did you really need to name this the same as "*nix" (which is now completely out of style because it's too confusing)
the
nix
crate i guess came after you guys, but still
i thought NixOS would let me declaratively configure my disk setup and various other early-boot options but it very much does not let me do that
i am opposed culturally
have you guys seen your community?
i can see your internal divisions from your CLI help, docs, and feature flags
everyone i know who's worked on Nix core says it's made them miserable
for a system that's designed to be correct-by-construction it sure seems to break a lot
very "academic project that unexpectedly got users" vibe
misc culture
"just talk to people"
"talking to people wins again"
most personal/professional conflicts i have are resolved by talking to the other person
this sounds obvious but is surprisingly hard when the two of you are mad at each other
"joke about the outcomes you want to see"
i’ve seen multiple people get jobs by joking on social media “so anyone want to hire me?”
"focus on the outcomes you want to see more of"
you need a positive vision of the future or you accidentally steer towards the thing you’re afraid of
this is why the EAs and rationalists are doomed, no matter how smart and influential they are
cannot emphasize enough how important it is to have positive visions of the future
You can't do things ironically.
Jokes are not actually jokes. At some level you mean the things you are saying.
Acting eventually becomes real. Poe's Law; "Fake it until you make it"; Johnny Depp is still all his characters decades later
“I don't think I believe in 'deep down'. I kind of think all you are is just the things that you do.”
hiring followup
why do tech bros think they know everything?
"tech bro" is not actually a coherent concept
“tech bro” is a slur against autistic trans women—deleted bluesky post
I am tired of the word 'techbro', Ash
"bro" is inherently gendered in this context (c.f. "bro culture") but people use "tech bro" to mean "anyone in tech with opinions i don't like"
maybe not originally. but they certainly do now.
pfrazee is doing the coolest shit now, but a decade ago he was indistinguishable from everyone else really into blockchain
tech workers get
fast
feedback on complex systems. most other fields need decades.
doesn't mean they're right as often as they think they are. does mean they often have a different perspective that isn't purely a result of ignorance.
ignorance can often be involved; cc
xkcd 793
but even then tech makes you unusually accustomed to researching things you don't know in fields you've never touched before, and the experience with complex systems makes you more humble about unknown unknowns
work in tech? poking your head into other fields? naïvely confident that you don't need to put in the research? skill issue!
admittedly "not all tech bros" is a really fucking funny line of defense
why are SWEs the ones who built Direct File? why not accountants and lawyers using WordPress?
not talking about the guy who “knows better than Signal president”. not interesting to me. there's jackasses in every field, but there's no term for "physics bro".
AI is introducing culture splits that didn't exist a year ago
Scissor statements
one side is focused on "does the thing do what i want"
the other is focused on "is it high-quality, does it build a community, does it bring people meaning and joy"
it used to be that these were symbiotic. now someone can sit in their room alone and build quite a complicated project without talking to anyone.
"artisan" work is slowly becoming a hobby/bespoke rather than economically compensated, like leatherworking
this is not necessarily a good thing; but see "Weizenbaum" below
we're early in this transition, for many projects it's still economically rational to hand-write code, especially for long-lived complicated projects with high stakes for failure
where is this going to go?
After Work, We'll Have Each Other, Clara Collier
The modern labor market has dissolved the bonds of tradition, family, and clan. In the modern world, relationships matter less. And because they matter less, we can do much more inside them. They are freer. They have room to breathe.
if people don't get status hierarchies from work, they'll get them from somewhere else. people want to belong, it's very fundamental.
not purely about in-groups and out-groups; there will always be parties with a limited guest list, and people enjoy parties in their own right
Revisiting Weizenbaum on education and society
Weizenbaum, German-American inventor of Eliza, writes about how computers are a fundamentally conservative force
“But we live in a concrete society, [and] with concrete social and historical circumstances and political realities in this society, it is perfectly obvious that when something like a computer is invented, then it is going to be adopted will be for military purposes.”
"The questioning should start the other way -- it should perhaps start with the question of what education is supposed to accomplish in the first place."
Computers allow existing institutions to metastasize rather than decentralize
"Why can't Johnny read?" must still be asked. [...] questions of that kind are uncomfortable. When we ask this question, we may discover that Johnny is hungry when he comes to school, or that Johnny comes from a milieu in which reading is irrelevant to concrete problems or survival on the street [...]
at a certain point, the problems of education are problems of society, not problems of teaching
and we would combat them better by reducing economic stress and social inequality than by designing better curricula
What's wrong with universities?, Henry Snow
"Employers claim they value the critical thinking skills students learn in the process of getting a well-rounded education. The actual job market experience suggests otherwise."
"A narrow and transactional focus on job training thus means underinvesting in the future. [...] A better higher ed system needs not only more money, but more freedom from market logic."
Employers are eating their own seedcorn by not hiring juniors
Using a technology forces you into its worldview. Using AI forces you into the worldview that productivity matters above all else.
Technology and computing has always been the practice of automating people out of a job.
As far back as Luddites during the industrial revolution
What's changed? Now the jobs being lost are "high-status".
We programmers don't like the taste of our own medicine.
With sufficient automation, the only alternatives to widespread poverty are T. J. Kaczynski's, or
sharing the material surplus in our society
Call to action: What technology are you, personally, building? Given the social/historical/political realities of your society, what purposes will it be adopted for? Could you build a technology that encourages decentralization instead?
positive visions of the future
Revisiting Asimov on education
(see "Weizenbaum on education", above, for more context)
The New Teachers, Asimov
"In other words, the student will ask questions, answer questions, make statements, offer opinions, and from all of this, the machine will be able to gauge the student well enough to adjust the speed and intensity of its course of instruction and, what's more, shift it in the direction of the student interest displayed."
To a great extent, AI makes this a reality today:
Koji—A world-class tutor in every home, Brilliant
What's the problem with Asimov's vision? Too isolating.
The Fun They Had, Asimov
No shared group projects, social interaction, mentoring.
teaching ≠ mentoring; you don't want an AI giving life advice
If you look at a modern classroom, everyone is staring down at their laptop screens
Not everyone has a computer!
certainly
not everyone has home access, but even some schools don't have computer labs, at least not enough for everyone
which means that computers can assist, but they cannot be the primary mechanism of learning
but maybe we can get the benefits of computing without the drawbacks of personal computers?
can we make computers
economical
? can they be
shared
?
Dynamicland
Dynamicland is made by Bret Victor:
Stop Drawing Dead Fish
Vision of computing as
out in the real world
, not buried in a screen. Projectors, not VR goggles.
"Computation means people coming together in the same space"
Montessori education
Hands-on, collaborative learning encouraging independence, problem solving, and focusing on personal interests
Mixed-age cohorts (usually 3-6 year spread), uninterrupted work time, prepared environments, learning-by-doing
Historically, single-age cohorts are
an aberration
(attributable to standardized compulsory education)
Backed by studies and evidence
Discourages grades and tests
Flipped classrooms
Encourages working together
Avoids further disadvantaging children with an unsupportive home environment
Avoids incentive to cheat on homework. Especially important now that internet+AI makes cheating so easy.
AI can act as a reviewer, and as a way to discover new topics, but not a teacher or assessor. Teachers and mentors are around in person to notice when the AI is acting up or on the wrong track.
Group projects
Selected from a "menu" of standard topics, with the exact project at the students' discretion
Menu makes sure that projects can correspond to learning outcomes (reading, writing, math, etc.)
Avoids dumping unpaid curriculum work onto teachers
Allows students to choose their own interests
Small problem: how do standardized assessments work?
Seeing Like A State
Governments will not accept teachers' words that learning is happening
Furthermore we don't
want
them to; non-standard grading allows widespread discrimination
Maastricht "progress testing"
Cumulative throughout school year, rather than per-chapter
Avoids incentive to cram, naturally encourages spaced repetition
Aalborg group assessments
Individual assessment
about a group project
.
Presentation to the class is ungraded (excluding public speaking courses)
1-1 interview with the teacher is graded on a rubric
Naturally allows AI without incentive for cheating: you can use it to build a cooler project, but not to avoid understanding how the project works
Naturally reduces incentive to "coast" and allow teammates to do all the work (you won't understand the project as well)
Does Ubiquitous Computing Need Interface Agents?, Mark Weiser
Weiser was Head of CS Lab at Xerox PARC
“People are most effective and authentic when they are fully engaged, mind and body, in the world”
copilot vs. enhancing your own ability to act
How does this apply to our vision?
"Minimap" showing what projects each group is working on
"Archivist" that suggests connections between each project
"Mind map" helps students organize their own notes and projects, while still connecting back to the topic
Call to action: Ask your kid, or a friend's kid, or a friend still in school, what they're learning.
You do know
someone
in school, right?
Do you think that school is a good use of their time?
If you think their time would be better spent in industry, sports, performing-arts/vocational schools, etc., examine exactly why you think that is.
Perhaps those activities are better at teaching than our public schools currently are?
Callback to Henry Snow on colleges as degree mills
Misc. notes that don't fit into the rest of the article
Schools are absurdly shackled to the interests of local homeowners, parents, and local/state/national politics
Changing education is hard because it's unpopular with the parents (c.f. Common Core Math)
Unsure how to address Weizenbaum's "we ought not to use entire generations of schoolchildren as experimental subjects". But clearly
something
isn't working, and at least Montessori/Aalborg/Maastricht have decades of results backing them up.
computer of the future
generality through systems thinking
languages have to constantly recreate features from scratch, which gets more expensive as the baseline for features grows
new operating systems Simply do not get adopted
implementing in userspace, but at the OS level, allows solving the problem once for all time, without locking you in
for that OS. but most OSes support enough tracing/sandboxing features that you can port, and those that don't can usually be emulated with a performance slowdown.
implementing at the OS level requires thinking about all possible interactions between the program and the OS
this is not actually as hard as it sounds (still hard but not intractable), just requires you not to "flinch"
a compiler/program pair is much simpler than the compiler in full generality
futamura transformation again
and you can think about this in terms of runtime tracking: valgrind is a kind of compiler
all systems come with a capability/expressiveness tradeoff
capabilities, service management, and generalized erlang
systemd socket-activated services
maybe the other end isn't connected until you actually send a request. the client doesn't have to care.
telefork
you don't have "a bunch of computers", you have "The Computer" with a bunch of nodes
c.f. Plan9 "CPU servers"
everything is serializable, because erlang function calls can be remote
editable programs
emacs
describe-key
(go to command that implements keybind, generalized version of
tmux list-keys
)
now that for every single program on your computer
CTF
DWARF-fs
"inside google this is easier"
corresponding unstripped binary for everything in prod
debuginfo servers are
kinda
this but not as reliable
"ideally gets you all the way back to your VCS"
not just source code,
original source code
, you are looking at the protobuf message instead of the generated C code
compilation is an implementation detail
Smalltalk VMs and Pharos
“no code/data distinction”
the postmodern build system
makes builds ~instant
need to write "decentralized build caching" before the rest of this section makes sense
trustfall and composable compilers
"don't solve a problem, obliterate the problem class"
map-reduce on arbitrary programs
work at the right meta language (composable compilers)
debuginfo that works between two
arbitrary
languages ("tree of IRs")
closely related to "editable programs"
want languages to interop as a "tapestry", not a stack
imagine a compiler that understands both haskell and rust and compiles haskell to MIR
find the shortest mapping between any two languages
we want many more IRs than currently exist (there is a midpoint between Rust and C that's not LLVM IR)
can automatically generate mappings
learn how to generate a language using targeted fuzzing + ML
learn how the language maps to the underlying IR with more fuzzing on the behavior
do that for two languages that compile to the same IR
congrats, you know how to get between one language and the other
do this for sub programs, gradually reassemble, stop anywhere you can insert an FFI boundary
Clippy: “this part of the query system looks like a Prolog, do you want me to rewrite it for you”
"compilers are partial evaluators"
deterministic concurrent programs
decentralized build caching
oh god everything here is a giant mess i'm only making it public because it's buried in a dozen other posts
uhhhh imagine bittorrent but you're distributing the source code, the binary,
and
a proof that the two correspond to each other
"what's the proof" something something when you run gcc, do it on a risc0 VM and create a fancy ZKP at the same time. look i don't understand the math ok
combine this with
orthogonal persistence
so incremental rebuilds are fast
other
“Slack your rope, Hangman”
Moving to the Netherlands with the power of friendship
The USA needs electoral reform
congrats, you elected one Democratic president. what next?
Congress is bad at passing laws, so most power ends up with the President, who acts through executive orders
the President's party changes every 4–8 years
when a new President enters, he often cancels the old president's EOs
as a result, other countries simply cannot trust the USA to be a stable partner
we saw this most recently with tariffs, the 2018 Iran nuclear deal withdraw, etc.
this is not specific to Trump! the USA has withdrawn from international organizations
more than any other country
since WWII.
most recently other countries are building their own coalitions that don't depend on the unstable mess that is the USA
this also applies domestically. no company is going to make a bet that depends on "the federal government completes a 10-year infrastructure project" because the government will simply not finish what they start
why don't we have good rail lines? rail requires a long-term commitment
epicycles
Congress doesn't do anything useful → people don't trust it → politicians campaign on weakening government institutions → Congress doesn't do anything useful
it took COVID and the Great Recession to get it to act, but usually it just … doesn't do much
First-pass-the-post laws → two party system → no incentive to compromise → hard to pass laws → FPTP remains in place
incumbent effects amplify this
other systems
do
have an incentive to compromise, especially parliamentary systems that require multi-party coalitions. you might not like their policies, but at least they're relatively stable.
why does multi-party help? a new government is often composed of at least one party from the previous government; no incentive to rip up laws they had already supported
all these epicycles interact
do you feel like the country you live in is getting better over time? i sure didn't.
i actually don't see any way out of this trap. let's consider some possibilities.
major crises (COVID-19, Great Recesssion, 1960s Vietnam War and Civil Rights Movements, WWII, Great Depression)
can lead to large changes in policy, including stable changes that last for decades
do
not
lead to changes in incentives between crises
dissolution of balances of power
Trump administration is already willfully disobeying judicial orders (El Salvador deportations, ignoring court orders in lawsuits)
some precedent here: Andrew Jackson “John Marshall has made his decision, now let him enforce it”
no lasting change! only accumulated power to the President
political violence (
It Could Happen Here, Robert Evans et. al
)
domestic insurrection (coup): literally already happened on January 6th, effectively no change in governance or incentives
local resistance to federal actors (grassroots + state-wide): literally already happened in Minnesota and Oregon, resulted in sweeping Blue midterms but no change in electoral incentives
domestic insurrection (grassroots): will likely just make things worse instead of better
independent states (without seccession)
imagine California, for example, becomes fiscally self-sufficient and starts ignoring federal laws and EOs
oops! no more Medicaid! there goes your government coalition. also it would be pretty damn bad for people's health.
people will still owe federal income tax; California can't meaningfully allow people to be US citizens without paying income tax
independent states (with seccession)
lol where's your military
requires sympathizers in the National Guard willing to disobey their chain of command
to break this, we have to break
both epicycles at once
if we only break "Congress doesn't do anything" (e.g. during crises), we revert to baseline incentives as soon as the crisis ends
if we only break FPTP, power remains with the President and we still get whiplash from EOs
i see exactly one possible way out, which is to switch to proportional representation, sparked by a crisis that forces Congress to act
seems unlikely!
most likely to happen if a major political party is already splintering and individual representatives want to stay in power despite the breakup
would likely require coordination across both parties. perhaps if both parties splinter at the same time?
but at least it's a goal to work towards
some prior art in
Fair Representation Act
, but very unlikely to pass
wrapping up
hopefully i will turn some of these into actual posts at some point!
if not feel free to DM me (email below) and i'm happy to blather on at length.
