---
source_url: https://heymaxwell.ai/
ingested: 2026-10-22
sha256: 95bf3f7f007778cc
---

Maxwell: The first Code Execution Model, by doubleAI

Maxwell

Manifesto

Research 
↗

Get early access

Join

§

Section: 

All Thinking Things

All Thinking Things

Proofs, Mathematics, and Code

Maxwell: An Agent for the Machine

Notes

LTX-2.5 at 4K, in half the time

An already efficient pipeline

What Maxwell changed

The same video

Afterword

Maxwell

: 

The first Code Execution Model

by 
doubleAI

Maxwell understands and improves code while it runs, reasoning about hardware and data, not just code. Every improvement is formally proven equivalent to the original code. 
Read the manifesto 
→

Get early access

38
×

faster data processing pipelines

4.25
×

faster AI inference kernels

What is a code execution model?

Play
1:41

A short animated film, with narration and captions, introducing Maxwell: most code never sees the hardware it runs on or the data it processes. Maxwell watches a program while it runs, rewrites the binary underneath to fit that exact machine and data, and formally proves every improvement equivalent to the original. It runs on CPUs and GPUs, speeding up data pipelines and AI inference kernels.

Featured customer

LTX-2.5 generates 4K video in half the time

LTX built LTX-2.5 for efficiency from day one, compiled end to end, 
sequence-parallel
 across GPUs, decoding on a 
hand-written
 attention kernel. A pipeline built and optimized by top human experts. Maxwell made their 4K generation nearly twice as fast.

 (opens ltx.io)

Load video · 1.3 MB

Each run is labelled in the video. The original pipeline takes 4 minutes 9 seconds; with Maxwell, the same clip takes 2 minutes 14 seconds. The race plays sped up, then both finished clips play at their own speed.

1.87
×

faster 4K video generation

134
s

per 4K clip on two B200s, down from 250s

Read the story 
→

Maxwell’s Demonstration

See Maxwell in action optimizing both GPU-based and CPU-based code. Once Maxwell has enough runtime data, it swaps in formally proven optimizations tailored to that exact machine while the program keeps running.

GPU-based speech-to-text using Whisper

Load video · 13.1 MB

Two terminals run the same Python script on the same RTX 4090: 180 transcriptions with Whisper-small from a cold start. Without Maxwell, on the left, it takes 106.23 seconds. With Maxwell, on the right, it completes in 49.82 seconds. Both produce identical transcripts. The recording plays at 4× speed.

CPU-based graph algorithms

Load video · 0.3 MB

Two terminals run the same Python script on the same machine: NetworkX betweenness centrality, 15 runs. Without Maxwell, on the left, it takes 61.44 seconds. With Maxwell, on the right, it completes in 17.50 seconds. Both print identical results. The recording plays at 4× speed.

Research behind Maxwell

Maxwell approaches Speed of Light on Blackwell

After one day of search, Maxwell beats NVIDIA’s PyTorch baselines on 90% of 
SOL-ExecBench
’s Blackwell kernels.

→

 (opens on doubleai.com)

doubleAI’s Maxwell: Surpassing 
Expert-Written
 Kernels At Scale

Independently generated and verified a hyper-optimized drop-in version of NVIDIA cuGraph, 3.6× faster on average.

→

 (opens on doubleai.com)

Blazing Fast pandas Without Changing a Line

Maxwell completely rewrote pandas’ kernels from scratch, specialized for modern hardware.

→

 (opens on doubleai.com)

Backed by

Contents

All Thinking Things

Proofs, Mathematics, and Code

Maxwell: An Agent for the Machine

Notes

All Thinking Things

"What we want is a machine that can learn from experience. The possibility of letting the machine alter its own instructions provides the mechanism for this."

— Alan Turing, London Mathematical Society, February 1947

In 1952 Alan Turing played a game of chess against his colleague Alick Glennie. He did so by taking on the role of a computer: he had written a chess program on a few sheets of paper, and at every turn he followed the instructions of his program to the letter, until they produced a move. Every move took him about half an hour. He lost.

Throughout that game, Alan did exactly what a computer does. He carried out the program faithfully, without improving a line of it, however obvious the improvements must sometimes have looked.

Promptly thereafter, the machines arrived. And programming settled into a division of labour that has held ever since: Human beings decide, and write down, 
precisely
 what a program should do. A computer then carries it out, instruction by instruction and billions of times a second, exactly as written. Any and all thinking happens before the program is executed, but absolutely none during or after.

In the last few years AI has joined the fray. AI models now draft code with programmers, and since the 
November singularity
, increasingly for them. But the code they write still goes to the same computers, which carry it out mechanically, deterministically, and unthinkingly, in much the same way Turing did with his chess program.

Why has AI thus far been relegated only to help 
write
 code, but never to help 
execute
 it?

Had Turing been free to act on what he saw at the board, he could have 
improved
 his program with every move, and it would have played a little better each time. Analogously, every piece of 
computer code
, coupled with full 
“contextual knowledge”
 of the environment and conditions under which it is executed, and the flow of data through it, could be accelerated, made to use fewer resources, or otherwise improved.

At doubleAI we have built a new category of models to do exactly this.

We call them 
code execution models
, or 
CEMs
. They place artificial intelligence somewhere it has never been before: 
between code and silicon.
 CEMs work under wholly different constraints from models that write code. A CEM lives 
inside the running program
, watching the data flow through it and reshaping the algorithms and instructions as it goes. The output is a binary, run directly on the hardware. No humans in the loop. Therefore, 
the model must never err
. To date, no AI has made that promise. Read on to see how we do so.

Proofs, Mathematics, and Code

Very recently formal verification
¹
 has revolutionised mathematics. Anthropic 
published
 a complete, 13-million-line formal proof of 
Fermat's Last Theorem
.
²
 Four days after Anthropic's proof appeared, OpenAI published a finite-time blow-up result for the 
Navier–Stokes equations
, one of the 
Millennium Prize problems
, again backed by a complete formal proof. Since then, AI-written formal proofs of important results have been appearing 
at

a

dizzying

rate
. Mathematics itself is seemingly being 
remade
.

This raises the question: can the same be done for software? For a CEM, this question is crucial. After all, a CEM evolves running programs, often many times a day, without any human reviewer in the loop. Even if there were time for it, rote testing would not be sufficient. What does it take to do this safely?

The answer is the same tool that is now remaking mathematics: 
formal verification
. The first step is to 
formalise
 the code, giving it a precise mathematical meaning that a machine can reason about. From then on, any question about how the code behaves can be settled by proof.

Our first CEM, which we are releasing for early access, is called 
Maxwell’s Daemon

³
, or more casually, 
Maxwell
. Its goal is 

superoptimisation

: finding the fastest possible way to carry out a piece of code on the machine in front of it. Maxwell takes existing code and, while the program is running, modifies the algorithms and the machine instructions, emitting 
new binary code
, much as a just-in-time compiler does, though with far more freedom in what the new algorithm may look like.
⁴
 Any replacement it makes must be precisely semantically equivalent to the code that preceded it.

Crucially, nothing changes in the source code
. Rather, what changes is what runs underneath: much faster 
binaries
, proven to be exactly equivalent to those that they replace. While a program runs, Maxwell identifies its bottlenecks, along with the ways in which they are expressed. For each bottleneck it finds, Maxwell creates a new version, assembled for the exact machine on which it is running. The source code stays exactly as its authors wrote it, whether they are human or a coding agent such as Claude Code. Maxwell is therefore 
complementary
 to coding agents: they write the program, and Maxwell makes sure the machine 
runs it optimally
.

For Maxwell, formal verification takes the form of 
formal proofs of semantic equivalence
.

Two programs are semantically equivalent when, given the same input, they always produce the same result and have the same effect on the world around them. They may look nothing alike. One might be a few lines of Python and the other some Rust or C code. What matters is that nobody using them, no matter how hard they try, is able to tell them apart (except, of course, that one is much more efficient). A formal proof of equivalence establishes this for every possible input and every possible scenario at once, in a language precise enough for a machine to check every step.
⁵

Original

def

original
(n):
 s = 0

for
 i 
in
 range(n):

for
 j 
in
 range(i):
 s += 1

return
 s

Replacement

fn

replacement
(n: i64) -> i64 {
 n * (n - 1) / 2
}

Proof of equivalence

requires
 n : int
 0 ≤ n ≤ 3037000500

theorem

original
(n) = 
replacement
(n)

by induction on
 n

case
 0:

original
(0) = 0 = 
replacement
(0)

case
 n + 1:

original
(n + 1) = 
original
(n) + n
 = n(n − 1)/2 + n
 = (n + 1)n/2
 = 
replacement
(n + 1) 
∎

A very simple proof that a Python function and its replacement, written in Rust, are semantically equivalent. Proofs of this kind can be conditional. Here, the condition is the one stated in the proof, and whenever it does not hold, a very fast guard hands control back to the original code. Note that the two programs need not share a language. This example is deliberately simple. The code Maxwell typically works on is full of mutable state, exceptions and other side effects, and its proofs are correspondingly far harder.

There is a deep and well-known connection between programs and proofs, known as the 
Curry–Howard correspondence
. Essentially, a proof is a program, and checking a proof amounts to checking that the program is correctly put together. More concretely, most programming languages are underpinned by 
types
, which describe what “kind of thing” a value is (for example, a number or a piece of text). The correspondence observes that a type can just as well describe a 
mathematical statement
, and that a program producing a value of that type is then a proof of the statement. Much in the same way, through this correspondence, a lemma becomes a small function, and a theorem built from lemmas becomes a larger program that calls them. Checking the proof is then nothing more than type-checking the program. This is 
type theory
 (in a nutshell), the mechanism on top of which most modern proof checkers are built.

At doubleAI we have made a number of breakthroughs in formally verified code.

One such breakthrough is our complete formalisation of the Python programming language, among the most dynamic languages there are.

Why is Python so difficult to formalise? In Python a value can change type from one line to the next. In fact, Python is so dynamic that even basic principles, such as what a number is, and what it means to add two of them up, can be wholly 
redefined
 while the program is running. This dynamic nature is part of what makes Python such an appealing programming ecosystem.

Our formalisation accounts for all of this behaviour.
 It covers not just small, self-contained functions that formal methods have traditionally been limited to. Rather, it covers ordinary, general-purpose Python as it exists in the real world, including code that performs communication, uses files, and so forth. With Python formalised, the claim that a piece of Python and a rewritten version of it agree can itself be written down formally, and proved.

Part of what makes Maxwell so potent is that it is 
trained at doubleAI
 to work within this formal system, writing each piece of new code alongside its formal proof of semantic equivalence.

Writing such proofs may sound like an enormous undertaking. For a person, it would be. 
Maxwell is not a person
. Its proofs are largely built from reusable 
proof gadgets
, each proved only once. Proofs also compose, so a proof for an entire unit can be assembled from many small ones. What is left is meticulous, tedious work; exactly the kind at which AI far surpasses human beings.

Maxwell handles 
both CPU and GPU code.
 Python code gets swapped for low-level, bare-metal optimised code (including, for instance, direct SIMD implementations, wherever relevant). PyTorch code similarly gets replaced with highly optimised kernels for the particular GPU present on the machine. The optimisations are far-reaching and encompass many more moving parts across the Python ecosystem.

One of the key enablers for optimisation is the contextual information about 
how programs are run
. This lets Maxwell specialise code to what it has actually observed, while of course guarding against the scenario in which any of the assumed preconditions has changed. Because every acceleration comes with a machine-checked proof, Maxwell can afford to be 

brave

, taking on transformations that no compiler or human engineer would risk, while being absolutely sure of their correctness, always.

Building a CEM like Maxwell comes with a great deal of engineering. Maxwell has to slip seamlessly into the runtime, detect bottlenecks, and accelerate code throughout, all without ever slowing down the “hot path”. Each of these is a story of its own, but perhaps one best left for another day.

Maxwell: An Agent for the Machine

Until now, AI in software has worked for programmers, writing code at their request and then stepping away. Maxwell lives with the code. It works for as long as the program runs, on behalf of the machine it runs on. It sees the hardware the program has landed on and the exact shapes and types of the data flowing through it, and it keeps fitting the code to both as they change.

Once Maxwell has proved a faster version of some code, that version becomes the starting point for its next attempt, and the program 
keeps getting faster
 for as long as it runs, while its source stays exactly as its authors left it. We think of this as 
self-improving code.
 Maxwell can bring this to every machine it runs on, at internet scale.

We think this matters well beyond any single program. Computing power has become one of the 
scarcest

resources
 in the world, and much of it goes to running code far more slowly than it could run. Every program Maxwell speeds up gives some of that back. Maxwell will be available soon, in early access. We are very excited to see what a world full of Maxwells looks like.

In 1952, Turing had to follow his program exactly as written. Our machines no longer have to.

¹

Formal verification is the practice of writing a proof in a language precise enough for a computer to check every step.

²

The proof was written by Anthropic's AI agents over the span of eleven days. Formalising the theorem had previously been the goal of a five-year, publicly funded programme that a group of top human mathematicians began in 2024.

³

After the tiny creature James Clerk Maxwell imagined in 1867, which lowered the entropy of a gas simply by sorting its molecules. Our Maxwell brings the same kind of order to code, fitting it to your hardware, your data and the way you use it.

⁴

Compilers and just-in-time compilers, such as torch.compile and PyPy, are limited to transformations written in advance by their engineers, and superoptimisers such as STOKE to short, loop-free fragments of machine code, optimised once, statically. Maxwell rewrites entire functions, algorithms included, inside real-world programs as they run. It fits each version to the exact hardware and to the data actually flowing through the program, keeps re-optimising as either changes, and proves every piece of code equivalent, rather than testing it.

⁵

Rice's theorem
 tells us that no algorithm can decide semantic equivalence for every pair of programs. That is a limit on a 
universal
 procedure, however, and says nothing about the particular pair in front of you. In practice, for nearly any two equivalent programs that we care about, such a claim can be written down formally, as a proof.

Contents

LTX-2.5 at 4K, in half the time

An already efficient pipeline

What Maxwell changed

The same video

Afterword

Read the full article on doubleai.com

Full article
 on doubleai.com

↗

LTX-2.5 at 4K, in half the time

LTX-2.5 is 
LTX
's state-of-the-art 
open
 world model, which generates, simulates, and shapes video, audio, and the physical world. 
Maxwell
 made LTX-2.5 generate 4K video nearly 
twice as fast
, with the same output.

4K video generation using LTX-2.5, shown at 10x speed. Left: original pipeline (250s). Right: Maxwell's optimised pipeline (134s). Both pipelines generating the same clip.

An already efficient pipeline

LTX-2.5 was built for efficiency from the start: it is light enough to run on edge devices, and the inference pipeline behind it is state-of-the-art. The pipeline is compiled end to end, runs across multiple GPUs with sequence parallelism, and decodes video with a hand-written attention kernel. It was built and optimized by top human experts.

We set Maxwell to push this already efficient pipeline further.

Where the time goes, component by component, in one five-second 4K clip on two B200s.

What Maxwell changed

Maxwell came back with more than a dozen significant changes, ranging from algorithmic all the way down to edits inside individual GPU kernels. 
Read the full research post
 for the details.

Attention across two GPUs.

Thinner tiling seams.

Changes inside the decoder.

Pause animations

The same video

None of Maxwell's speedups come at the cost of quality. The videos produced by Maxwell’s optimised pipeline are visually indistinguishable to that of the original code.

A clip that starts from a photo of a colour chart, at native 4K resolution: cropped, not scaled.

Fine texture: a hand brushing across grass. The inset in each corner magnifies the boxed area.

Afterword

Thanks to the LTX and doubleAI teams for making this collaboration possible. There is plenty more code to optimize, and we’re excited to see what Maxwell finds next.

The faster LTX-2.5 pipeline is 
open source
. Try it on your own videos, or 
bring your own workload to Maxwell
 and see how much faster it can run, even if you’ve already optimized it.

Privacy Policy

About this notice

This preliminary notice describes how the Maxwell website, presented by doubleAI, handles personal information. It covers this website and its early-access and contact forms, not the processing of customer code or data by a future Maxwell product. The full legal entity name, registered address and dedicated privacy contact will be added after verification. Until then, privacy enquiries can be submitted through our Contact page.

Information collected

The early-access form asks for your name, email address and optional organization. The contact form asks for your name, email address, optional organization and message. These details are used to handle your request. Accepted requests are stored as lead records in PostHog, including your contact details, organization when provided, request type and receipt time. Contact messages are also retained with the request. Please do not submit confidential code or sensitive personal information through these forms.

Technical information such as IP address, browser information and request logs may be processed to deliver and secure the website. If you allow analytics, PostHog receives a randomly generated browser identifier, page visits, visit and interaction timing, selected button and link interactions, browser, operating system, device information, approximate location derived from your IP address, and website performance measurements. Analytics also include the referring website's origin and approved campaign tags, when available. A browser identifier can distinguish repeat visits from the same browser and can be linked to your contact profile when you submit a form with analytics enabled.

Purposes

We use form submissions to respond to enquiries and administer early-access requests. We use technical information to deliver and secure the website. Optional analytics help us understand how visitors find and use Maxwell, which pages and campaigns lead to early-access requests, where the forms encounter errors, and whether the website performs well. Optional analytics and advertising remain off until you allow them. Requesting early access is not, by itself, consent to unrelated promotional email.

Service providers and recipients

The website is hosted using Amazon Web Services Amplify Hosting. Form submissions are sent to the form endpoint configured for this website. If no endpoint is configured, the website cannot accept form submissions and shows an error instead of confirming receipt. The form service runs on AWS Lambda. Submissions are recorded in AWS CloudWatch logs, shared with our team through Slack, and synced to PostHog for managing requests and follow-up. An early-access request can also trigger a confirmation through Resend.

PostHog provides our lead directory and optional website analytics. The form service creates a contact profile for an accepted request even when optional browser analytics are disabled. If analytics are enabled when you submit a form, a browser identifier can link your consented visit history and subsequent activity to that contact profile. Without that identifier, we do not guess which visits belong to you. The project discards IP addresses after approximate location enrichment; server-side lead records disable location enrichment. PostHog's privacy notice is available at https://posthog.com/privacy.

Google Tag Manager loads only when you allow both analytics and advertising. Its published container includes Google Analytics and LinkedIn Insight to measure website use and campaign results. These services may receive page addresses, referrers, device and network information, and use cookies or other identifiers. The container also includes an X advertising tag that is currently inactive because its consent check needs updating. Google's privacy notice is at https://policies.google.com/privacy, LinkedIn's at https://www.linkedin.com/legal/privacy-policy, and X's at https://x.com/en/privacy. The container is managed separately from this website, so its published tags may change. Information may also be disclosed where legally required.

Cookies and similar storage

Necessary storage supports website functionality, security and remembering cookie choices. The local-storage entry maxwell-cookie-consent records your analytics and advertising choices, their date and the consent version. A choice is valid for 180 days. After expiry or a change to the consent version, a new choice is requested. It is browser-specific. The consent record itself is not sent with your early-access submission; browser and session identifiers are included only when analytics are enabled.

Visitors in all regions can reject optional tracking, allow analytics only, or allow analytics and advertising. PostHog's optional local storage remembers a random browser identifier and analytics session information. This integration uses local storage rather than PostHog analytics cookies. Its use is limited by the consent lifecycle: expired, withdrawn or superseded consent removes the recognized optional local storage. A new analytics choice may therefore start a new browser identifier.

Current tracking safeguards

PostHog loads only after analytics consent. Analytics-only consent does not enable Google Tag Manager: the entire optional container remains blocked unless you allow both analytics and advertising. The site also blocks optional tracking when it detects a browser Do Not Track or Global Privacy Control signal.

PostHog session replay, heatmaps, console recording, automatic error capture and network recording are disabled. Automatic click capture is limited to links and buttons, with element text and attributes masked. Form field contents, email addresses, names and messages are excluded from browser analytics events and the explicit Google Tag Manager events sent by this website. The separate form service stores accepted requests and contact details in the PostHog lead directory. Purpose-built events record form progress, success or failure and non-identifying context, such as the page and button location. For PostHog, page addresses are reduced to known views; arbitrary query strings and fragments are excluded, approved campaign fields are restricted, and referrers are reduced to their origin. These PostHog filters do not sanitize data collected directly by Google Analytics or LinkedIn; those services may receive the full page address and referrer after you allow both optional categories.

You can reject all optional tracking and still use the website and its forms. Cookie settings in the footer lets you change or withdraw your choice at any time. Withdrawal stops analytics, removes recognized optional storage and reloads the page to stop previously loaded optional scripts. Changes are also applied to other open tabs when the browser makes the storage change available to them. A missing-page view uses an existing analytics choice and links back to the home page to manage preferences.

Third-party storage

Google Analytics and LinkedIn may set optional measurement or advertising cookies after both categories are allowed. Their cookie names and lifetimes depend on the vendors' published configuration; a complete cookie-by-cookie inventory and retention schedule remain pending. The configured X tag is currently inactive. Withdrawal removes recognized optional cookies and PostHog local-storage entries accessible to this website, but cannot erase cookies on another domain or information already received by a provider. Your browser settings can also remove cookies and site data.

Retention and international processing

Form submissions and related records should be kept only as long as needed to handle the request, administer early access, maintain necessary business records or meet applicable legal obligations. The 180-day browser consent lifecycle is not a promise to delete analytics events already received by PostHog. AWS submission logs are configured for 365 days of retention. Specific PostHog contact and analytics retention, other form-service retention and international-transfer arrangements remain pending confirmation. Providers may process information outside your country; this notice does not assert that any particular transfer safeguard has already been verified.

Your choices and rights

Depending on applicable law, you may have rights to access, correct, delete or receive your personal information, object to or restrict certain processing, withdraw consent, and complain to the relevant supervisory authority. Contact the team through the Contact page to make a privacy request; identify the request as a privacy enquiry and provide enough information to locate the relevant submission. Verification of identity may be necessary. Withdrawal does not affect the lawfulness of processing before withdrawal.

Updates

This is a preliminary website notice dated 19 October 2026, not a statement of verified compliance in every jurisdiction. Controller details, production form-service details, retention periods, transfer arrangements and any external tag-container inventory require confirmation. Updates will be published here with a revised date. A material change to optional tracking purposes will require a renewed consent choice.

Contact the team

Manage cookie choices

Terms of Use

Scope

These preliminary Terms of Use concern the Maxwell informational website, presented by doubleAI, its research content and its early-access and contact forms. They are not a software licence, service-level agreement, data-processing agreement or contract for use of a Maxwell product. The full legal entity name, registered address and jurisdiction details are pending verification and will be added in an updated version.

Using the website

Use the website lawfully. Do not attempt unauthorized access, interfere with availability or security, introduce harmful material, or submit fraudulent or abusive requests. When contacting the team, provide information you are entitled to share and do not include confidential source code or sensitive personal information.

Early access

An early-access request expresses interest only. It does not guarantee acceptance, a release date, product availability, specific performance, pricing or access rights. Any later access to software or services may require a separate agreement.

Research and performance information

Research summaries, demonstrations and performance figures describe particular experiments or configurations. They are not guarantees of results for every workload, machine or deployment. Website information may change and may contain errors or omissions. Evaluate the original research and your own requirements before relying on it.

Intellectual property

Website materials may be protected by copyright, trademarks and other intellectual-property rights. Rights remain with their respective owners. Reading the website does not grant a licence to Maxwell software or transfer ownership of any intellectual property. Separately published code, papers or datasets remain subject to their stated licences and terms.

External links

Links to third-party websites are provided for reference. Those websites have their own terms and privacy practices; their inclusion does not make their content part of these terms.

Privacy and cookie choices

Our Privacy Policy describes the handling of website data and the current preliminary status of the relevant disclosures. Optional cookie consent is separate from these terms and from an early-access request. You can change cookie choices through Cookie settings in the footer.

Availability and responsibility

The informational website is provided on an as-available basis without a promise of uninterrupted operation or error-free content. Nothing in these terms excludes liability that cannot lawfully be excluded, limits mandatory consumer rights, or overrides protections provided by applicable law.

Applicable law and updates

No specific governing law, exclusive court or arbitration process is designated in this preliminary version. Mandatory applicable law remains unaffected. Updated terms will be published here with a revised date; any separate product agreement will state its own applicable provisions.

Contact

For questions about the website or these terms, use the Contact page. This preliminary version is dated 17 October 2026 and requires legal review and verified company details before being treated as a finalized legal document.

Contact the team

Manage cookie choices

Get early access

Maxwell is in controlled availability. Leave your details to request early access.

Name

Email

Organization (optional)

We use these details to handle your early-access request. Read our 
Privacy Policy
 and 
Terms of Use
.

Request early access

Request received

You’re in line for early access.

We’ll be in touch at 

.

Contact

Questions about Maxwell, research, press or partnerships? Send the doubleAI team a message.

Name

Email

Organization (optional)

Message

We use your details to respond to this enquiry. Read our 
Privacy Policy
 and 
Terms of Use
.

Send message

Message sent

Thank you.

We’ll get back to you at 

 soon.

Privacy Policy

Terms of Use

Contact

Cookie settings

© 2026 
doubleAI
. All rights reserved.

×

We value your privacy

We use optional storage to understand visits and improve Maxwell. You can allow analytics, accept all optional services, or keep them off.

Accept all

Reject optional

Customize

×

Cookie preferences

Essential cookies keep this site working. Analytics and advertising cookies are optional.

Essential 
always on

Security, site functionality and remembering your choice.

Analytics 

Understand visits and interactions to improve the website.

Advertising 

Measure campaigns and advertising audience interactions.

Reject optional keeps optional services off. Allow analytics enables PostHog. Accept all also permits advertising tags, when configured.

Reject optional

Allow analytics

Accept all

Privacy Policy

Terms of Use