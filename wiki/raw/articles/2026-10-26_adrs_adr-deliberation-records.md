---
title: "adr-deliberation-records"
source: https://adrs.systems
publisher: adrs
captured: 2026-10-26
type: article
status: full
sha256: a0b24924e3ba0ab1c9ffa103b3af972b9a72de702871449ad9c5b471bd79022f
---

# adr-deliberation-records

Source: https://adrs.systems
Publisher: adrs
Captured: 2026-10-26

ADRs4AI — Your thinking stops disappearing. Your decisions start compounding. ADRs4AI get started 
 the idea 
 blog 
 github ADRs4AI Your thinking stops disappearing. Your decisions start compounding. The template 
A repository starter: ADR & seed templates, the directives, the inbox protocol, task-runner recipes. Adopt whole or by feature — it works from your first seed. The VS Code extension 
Tree views of your open questions, diagnostics that catch malformed records as you type, deep links, and an MCP server so your agents can query the record. Also on Open VSX . The iOS client 
Your project's open questions, in your pocket: sign in, import a repo, review, and one-tap Accept that lands real answers as commits. On the App Store . The most valuable byproduct of the collaboration between a human and an AI
is the thinking — and in ordinary practice, all of it evaporates. You can already
make good decisions with your AI. Every session produces reasoning you will
need again, and lose by default. This keeps the why, so it compounds. A record, verbatim This is the method&rsquo;s product — one question from a live, public project&rsquo;s own
record, exactly as it sits in the repository: ### QST-HISTORICAL-TRUTH: How should corrections preserve what was previously believed?
 - Status: answered
 - Why asking: Conversation attribution needs “what was true or documented as
 of date X,” while later research may correct earlier records.
 - Need: Approve or revise the proposed temporal policy.

 **Options** :

 - **A — Mutable present truth**: Correct records in place; rely on Git
 history for prior states.
 - **B — Append-only assertions**: Never change claims; append corrections
 and supersession edges.
 - **C — Bitemporal hybrid**: Correct descriptive records when needed, while
 claims/events carry valid-time, observed-time, and explicit supersession;
 Git remains a third audit layer.

 **Recommendation** : (by GPT 5.6 Sol at Perplexity Computer)

 **C — Bitemporal hybrid.** 

 **Rationale** : Git history records when repository bytes changed, not when a
 release became valid or when a provider made a statement. Explicit
 valid-time and observed-time support historical queries, while supersession
 edges preserve corrections without forcing every typo into an eternal
 domain event.

 **Confidence** : High that Git history alone is insufficient; medium-high
 that two temporal axes cover the first release.

 **Falsifier** : If real attribution cases require additional independent
 times, such as product-availability time distinct from announced and
 effective time, the temporal model must expand rather than overload either
 axis.

 **ANS:** (by Jérémie &#34;Sonnet 4.5&#34; Lumbroso (via ADRs4AI mobile))
 C — Bitemporal hybrid.
 From frontier-model-observatory ,
verbatim. The AI staked the question; the recommendation — options,
rationale, confidence, and what would prove it wrong — is GPT 5.6 Sol&rsquo;s;
the one-line ruling came from the founder&rsquo;s phone. That&rsquo;s the whole
mechanic : The AI carries the reasoning, the human spends one judgment —
accept, override, or any answer in any shape —
and the record keeps the why, for every mind that comes later. Ten minutes, from zero Real commands, the flow the founder actually runs — one seed, one question,
one ruling: # 1 · Your copy of the template 
 gh repo create my-project --private --clone \
 --template ADRs4AI/human-ai-collaboration-template-A
 cd my-project

 # 2 · Open CLAUDE.md, fill in the top block (messy is fine), 
 # then stake the record before any work starts: 
 git add -A && git commit -m &#34;chore: the record begins before the building does&#34; 

 # 3 · Recruit — open your agent and offer the mission: 
 claude # or your agent of choice 
 # &#34;Hello — I have a mission for you. Read about it and tell me 
 # if you accept, or any pushback.&#34; 
 Then dump your thinking into a first seed — dictation is fine; your AI
chunks it into ADRs that keep your actual words, the options, the reasoning,
the open questions. Answer the first question it stakes. Every open question
is one grep away, always: grep -rn '^### QST' docs/adr/
 One seed, one question, one answered ruling — that&rsquo;s the loop, and it
already compounds. Running a crew — several seats, wake-on-brief, you stop being the message
bus — is the optional next chapter: steps 7–9 of Get started . How it works, in twenty seconds Dump your thinking into a seed — messy is fine, dictation is fine; capture
first. Your AI chunks it into ADRs that keep what usually evaporates: your
actual words, the options considered, the reasoning, the open questions. Every
question is findable by one grep — ### QST: — or surfaced by the editor
extension, the MCP server, the phone in your pocket; and each arrives with the
AI&rsquo;s options, its recommendation, its rationale, its stated confidence,
and what would prove it wrong — so answering streamlines to accept or
override : Cognitive load down, bandwidth freed for the deliberations that
matter. It&rsquo;s where conversations become decisions that keep their reasons —
 deliberative programming , in one habit. You don&rsquo;t need to be an experienced engineer to start. The method was built
through daily practice by one human and a growing crew of AI collaborators,
and its whole point is that the record does the remembering — as much
for the veteran with too many projects, as for the beginner building their
very first one. The extension&rsquo;s Open Questions view, on this project&rsquo;s own record: A question, its options, an attributed recommendation — and the answer box. Question 16 of 75, that day. What it is not Not transcript archival. Not vector-database &ldquo;memory.&rdquo; Not an orchestration
platform. Not a claim that an AI possesses persistent identity — the record
holds, minds change, and the work resumes either way. The ecosystem, mapped Everything in the ADRs4AI world and what each piece is for, on one page —
methodology & template, editors & clients, crew automation, projects
practicing it, learning & teaching — every entry marked by kind and
language: awesome-adrs4ai ,
the curated map. Papers Cybernetic and Epistemic: A Missing Vocabulary for Trustworthy Agentic
Delegation — accepted at the AAAI 2026 Fall Symposium on Trustworthy
Agentic Systems ( TAS 2026 ) ·
 arXiv:2610.00961 Deliberative Programming: A Versioned Deliberation Protocol for Human–AI
Collectives — DOI 10.5281/zenodo.23300579 The methodology template itself is citable: concept DOI
 10.5281/zenodo.23303469 —
always resolves to the latest archived release. The idea underneath The most valuable thing that happens between a human and an AI is not the
code, the draft, or the answer. It&rsquo;s the thinking — and in ordinary
practice, all of it evaporates. […] It does not make an AI persistent, and
it does not make anyone remember. It makes the work resumable — and the
thinking compound. — from What is ADRs4AI? , the founding essay. A stranger can
read it cold; its authorship and review record are public, because that is
the method. From the blog 2026-08-25 Acknowledgments, before the launch 2026-08-25 Cybernetic and epistemic: Two ways to relate to AI An epistemic-continuity protocol for humans and AI. Built in the open by Jérémie Lumbroso and a crew of named, attributed AI collaborators — which is the whole point.
· Why this exists · Privacy · Support
