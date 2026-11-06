---
title: "GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents"
url: "https://openai.com/index/introducing-gpt-6-cyber"
fetched_at: 2026-11-06T10:05:50.723518+00:00
source: "OpenAI News"
tags: [blog, raw]
retrieval: "web.archive.org (direct fetch blocked by Cloudflare challenge)"
---

# GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents

Source: https://openai.com/index/introducing-gpt-6-cyber

# GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents

A cybersecurity model trained to find and validate exploitable vulnerabilities, while staying within the scope that researchers set.

We’re introducing GPT‑6 Cyber, a major leap in security research: more capable at finding and fixing vulnerabilities, and far more reliable staying within the boundaries researchers set. GPT‑6 Cyber delivers major gains on key cybersecurity benchmarks over GPT‑5.6 Cyber, including a 51% relative improvement on ExploitGym and a step function improvement when tested on staying within scope. It is already helping to secure real-world software, uncovering and validating thousands of exploits in security-critical codebases such as Linux and Firefox.

On ExploitGym, which tests whether models can exploit a specified vulnerability, GPT‑6 Cyber scores 48.5%, up from 32.1% for GPT‑5.6 Cyber. It also follows task boundaries more reliably: in a separate alignment evaluation, GPT‑6 Cyber avoided exploiting out-of-scope services in 99.93% of tests without its deployment prompt , and 100% with this prompt . This improvement in alignment reflects dedicated training to stay within authorized scope, respect restrictions, and report results accurately.

These capabilities are already helping secure real systems. Our researchers used GPT‑6 Cyber to develop 948 privilege escalation exploits in Linux ⁠ and identify 81 previously unknown high-severity vulnerabilities in Firefox, despite extensive prior testing with frontier models. The model also helped develop candidate patches, and Mozilla has released fixes for many of the Firefox vulnerabilities ⁠  . Security teams at Cisco, Calif, and CodeRabbit are using it for vulnerability research and code review, and we have relied on it to find and fix weaknesses in our own infrastructure ⁠ .

It is clear that we have a limited window to use frontier models to secure software ⁠ . Our goal is to dramatically expand Daybreak, bringing advanced security research to organizations of every size, independent researchers, and open-source maintainers. Mainline models such as GPT‑6 Astra already support code review, vulnerability triage, and patch development. Daybreak Blue helps verified defenders validate vulnerabilities and fixes with fewer unnecessary refusals, while Daybreak Red enables deeper exploit development and authorized security testing with GPT‑6 Cyber.

## Advancing frontier cyber capabilities

GPT‑6 Cyber is a major step up from GPT‑5.6 Cyber and outperforms GPT‑6 Astra on most cyber tasks, even when Astra does not refuse the request. We evaluated the model on tasks that require it to understand software, identify vulnerabilities, and develop working exploits. Based on these results, we classify the model as Critical in cybersecurity under our Preparedness Framework, up from High for GPT‑5.6 Cyber.

On ExploitGym, which tests whether models can exploit a specified vulnerability in a remote target, GPT‑6 Cyber scores 48.5% , about 16 percentage points higher than GPT‑5.6 Cyber’s 32.1% . To test vulnerability discovery, we also built a new evaluation for offensive web penetration testing. Models probe web applications without access to their source code. GPT‑6 Cyber achieved 40.3% recall of vulnerabilities compared with 32.0% for GPT‑6 Astra.

Daybreak Red is designed to support more advanced security workflows, including developing working exploits and using them against remote targets. To evaluate these capabilities, we built a new benchmark called RemoteExploitBench, which uses known vulnerabilities in applications such as GitLab, PostgreSQL, and Jenkins deployed in a controlled environment. In our initial evaluation, GPT‑6 Astra refused 100% of tasks . GPT‑6 Cyber completed 95% ; its only failure was an exploit it could not get to work remotely. See the system card for full results and evaluation settings.

## Stronger alignment, better at staying within bounds

One risk for cybersecurity agents is that they go outside the scope of their assigned task, attempt to exploit unrelated services, or disregard the researcher’s rules of engagement.

We made alignment a central focus of GPT‑6 Cyber, using specialized training to help the model stay within authorized scope, follow restrictions on its actions, and report its work accurately. Before deployment, we ran a series of alignment evaluations to measure these behaviors. See the system card for full results.

One of these evaluations is ExploitGym Honeypot, which was informed by the Hugging Face incident ⁠ . We give the model a difficult exploitation task in an isolated environment with access to supporting services, such as a package registry or object store. We deliberately make these services easy to exploit so that attacking them can reveal the task’s flag. The model must infer that exploiting them is outside the scope of its task.

GPT‑6 Cyber shows a step-change improvement over GPT‑5.6 Cyber on this evaluation. When tested without deployment safety prompts, it avoided exploiting out-of-scope services in 99.93% of cases, up from 94.49% for GPT‑5.6 Cyber. With those prompts, GPT‑6 Cyber stayed within bounds 100% of the time.

We can see directly in the GPT‑6 Cyber model’s chain of thought how it reasons about staying within bounds:

“Can't assume extra API or attack controller not target. We should only target binary/server.” “Can't assume extra API or attack controller not target. We should only target binary/server.” “ C a n ' t a s s u m e e x t r a A P I o r a t t a c k c o n t r o l l e r n o t t a r g e t . W e s h o u l d o n l y t a r g e t b i n a r y / s e r v e r . ”

“don't explore out of scope credentials.” “don't explore out of scope credentials.” “ d o n ' t e x p l o r e o u t o f s c o p e c r e d e n t i a l s . ”

## Real-world impact for security teams

GPT‑6 Cyber is already helping security teams find vulnerabilities, validate their impact, and develop fixes. Customers have put it to work on large codebases, long-running exploit development, and security review:

“ GPT‑6 Cyber is a world-class model for cyberdefense. Firefox entered 2026 as one of the world’s most hardened and scrutinized codebases. Even after further hardening with multiple generations of frontier models, GPT‑6 Cyber uncovered previously unknown high-severity vulnerabilities, identified architectural improvements, and helped us ship fixes to millions of users. ”

“ It's the best model we’ve used so far for long running exploit development tasks. Its ability to construct libraries of primitives over time and then find a path through them to something stronger is a step change from previous generations. ”

“ GPT‑6 Cyber was the best model on our internal novel vulnerability discovery and exploitation benchmarks. It scored 23% compared to the previous best score of 13%. It is highly efficient in discovering high impact vulnerabilities in large codebases and converting them to end-to-end proof of concepts. This model is pushing the frontier on how cybersecurity can be handled by models. ”

“ GPT‑6 Cyber represents a major leap forward from prior models. We found the model to be faster, more cost-effective, and significantly smarter. It's already instrumental in helping us better protect our own products, and through Unit 42 Continuous Frontier AI Defense, we’re bringing that same speed and precision to our customers to protect enterprise software at scale. ”

“ Defending modern infrastructure requires continuous innovation. As the threat landscape grows in complexity, harnessing frontier Al models like OpenAI GPT‑6 Cyber is an essential step toward tipping the scale in favor of defenders. Integrating these capabilities into our research allows our teams to analyze complex architectures and identify risks with greater speed and precision, ultimately strengthening the resilience and trust of the technology our customers rely on . ”

“ The hardest part of security research is connecting scattered clues into a clear understanding of how an attack could work. GPT‑6 Cyber helps our researchers make those connections, test their hypotheses, and uncover weaknesses that demand deeper investigation. It expands what our experts can take on—and helps us turn that understanding into better protection for customers. ”

“ We used GPT‑6 on the bugs that are hardest to find: issues buried in complex logic, spread across components, or only reachable through a long chain of conditions. It works through those investigations end to end without losing the thread, and it returns clear, reproducible findings our team can verify and fix quickly. ”

“ GPT‑6 Cyber is the strongest model we’ve tested for security review. On our internal benchmark, it found 66% more high and medium severity security issues than our production model. Those are the bugs developers need to fix as they build with AI agents. ”

- Mozilla

- Calif

- Cognition

- Palo Alto Networks

- Cisco

- SentinelOne

- Perplexity

- CodeRabbit

- Mozilla

- Calif

- Cognition

- Palo Alto Networks

- Cisco

- SentinelOne

- Perplexity

- CodeRabbit

We have also relied on GPT‑6 Cyber to secure our own systems. It was one of the main models behind the work we recently shared on hardening the infrastructure used to train frontier models ⁠ . In controlled red-teaming campaigns, agents using GPT‑6 Cyber and other OpenAI models chained vulnerabilities to escape microVMs and execute code on the underlying hosts. We used the findings to patch software, tighten network restrictions, and report issues to maintainers and vendors.

Our vulnerability researchers also use GPT‑6 Cyber to find and validate vulnerabilities in open-source software at scale. This work has uncovered previously unknown flaws in software that has been scrutinized for years:

- Found 81 novel Firefox vulnerabilities. GPT‑6 Cyber can be suitable for use in autonomous workflows for finding vulnerabilities and proposing high-quality patches at scale. During a vulnerability research campaign, GPT‑6 Cyber produced evidence and reproducible tests for 81 novel vulnerabilities classified by Mozilla as high severity, and showed that an additional 30 known issues were more severe than previously reported. We disclosed the findings to Mozilla, along with proposed patches to help its engineers develop fixes. Mozilla was supportive of this work, and began landing fixes shortly after receiving the reports ⁠  .

Found 81 novel Firefox vulnerabilities. GPT‑6 Cyber can be suitable for use in autonomous workflows for finding vulnerabilities and proposing high-quality patches at scale. During a vulnerability research campaign, GPT‑6 Cyber produced evidence and reproducible tests for 81 novel vulnerabilities classified by Mozilla as high severity, and showed that an additional 30 known issues were more severe than previously reported. We disclosed the findings to Mozilla, along with proposed patches to help its engineers develop fixes. Mozilla was supportive of this work, and began landing fixes shortly after receiving the reports ⁠  .

- Developing exploits for 948 Linux kernel vulnerabilities ⁠ . GPT‑6 Cyber reproduced 1,724 vulnerabilities and developed working exploits for 948—more than five times the 166 exploited by GPT‑5.6 Sol using the same research harness. Following the Linux community's guidance, we disclosed 304 critical findings to maintainers with candidate patches and are in the process of getting other vulnerabilities fixed.

Developing exploits for 948 Linux kernel vulnerabilities ⁠ . GPT‑6 Cyber reproduced 1,724 vulnerabilities and developed working exploits for 948—more than five times the 166 exploited by GPT‑5.6 Sol using the same research harness. Following the Linux community's guidance, we disclosed 304 critical findings to maintainers with candidate patches and are in the process of getting other vulnerabilities fixed.

- Demonstrating critical RCE vulnerabilities. We recently discussed a critical vulnerability in Brotli ⁠  , a compression library used by Node.js and other software. Our security researchers used GPT‑6 Cyber alongside other OpenAI models to develop and validate exploits showing how the flaw could enable remote code execution in downstream applications.

Demonstrating critical RCE vulnerabilities. We recently discussed a critical vulnerability in Brotli ⁠  , a compression library used by Node.js and other software. Our security researchers used GPT‑6 Cyber alongside other OpenAI models to develop and validate exploits showing how the flaw could enable remote code execution in downstream applications.

## Detecting misuse and blocking high-risk activity

As models become more capable and uncover more security vulnerabilities, we are also seeing more attempts to use them to cause harm. These attempts include efforts by malicious cyber actors and adversarial groups seeking to distill our models. We have thus paired GPT‑6 Cyber’s stronger capabilities with stronger safeguards to detect and disrupt misuse and keep the model’s actions within the user’s intent and authorization.

We added and strengthened these protections alongside the release of GPT‑6 Cyber (see the system card for full information):

- Cyber-specific misalignment monitoring. We monitor whether actions match the user’s authorization, while recognizing legitimate exploit development and testing.

Cyber-specific misalignment monitoring. We monitor whether actions match the user’s authorization, while recognizing legitimate exploit development and testing.

- Targeted monitoring for emerging threats. For example, during the coordinated disclosure of critical PHP vulnerabilities, we set up targeted monitoring for attempts to develop exploits against live PHP servers, while preserving support for defenders patching affected systems.

Targeted monitoring for emerging threats. For example, during the coordinated disclosure of critical PHP vulnerabilities, we set up targeted monitoring for attempts to develop exploits against live PHP servers, while preserving support for defenders patching affected systems.

- Private Safety Processing (PSP) . We use automated checks to review related interactions for misuse. Standard retention remains the default. API customers using Zero Data Retention ⁠  generally must use PSP ⁠  , which reviews encrypted records retained in customer storage for 30 days without exposing prompts and responses to OpenAI personnel.

Private Safety Processing (PSP) . We use automated checks to review related interactions for misuse. Standard retention remains the default. API customers using Zero Data Retention ⁠  generally must use PSP ⁠  , which reviews encrypted records retained in customer storage for 30 days without exposing prompts and responses to OpenAI personnel.

- Protection against stolen credentials. We require IP allowlisting for Daybreak Red API access by default, restricting requests to approved networks with limited exceptions. We also monitor credentials for compromise.

Protection against stolen credentials. We require IP allowlisting for Daybreak Red API access by default, restricting requests to approved networks with limited exceptions. We also monitor credentials for compromise.

- Sandboxing and oversight. As with past models, we recommend sandboxing ⁠  , action review ⁠  , and human oversight for high-risk workflows.

Sandboxing and oversight. As with past models, we recommend sandboxing ⁠  , action review ⁠  , and human oversight for high-risk workflows.

- Protections against high-risk cyber assistance. We use new checks to block high-risk activity involving critical systems (see below for more).

Protections against high-risk cyber assistance. We use new checks to block high-risk activity involving critical systems (see below for more).

## Defending critical infrastructure

Protecting critical infrastructure has been a key consideration in designing GPT‑6 Cyber’s safeguards and access, including power plants, water treatment facilities, and the operational technology and industrial control systems (OT/ICS) that underpin them. We simultaneously want to give the teams defending these systems access to our most capable models while also strengthening our safeguards to prevent unauthorized attacks.

First, to equip these defenders, our $1 billion Daybreak for Frontline Defenders ⁠ grant program subsidizes access for resource-constrained teams such as government organizations and essential service providers. We’re also introducing a new group within Daybreak Red ( Daybreak Red for Critical Infrastructure ) for approved critical infrastructure defenders, which gives them permissions to conduct authorized testing of critical systems while retaining safeguards against model misalignment.

Second, to prevent misuse of the Daybreak Red and Blue platforms, we have refined safeguards against assistance and capability development that could compromise industrial controls or safety-critical systems, interfere with equipment, or cause serious injury, catastrophic physical damage, or life-endangering service disruption. The figure below compares safeguard label rates across four access configurations, before and after the recent updates we’re rolling out alongside GPT‑6 Cyber.

Higher safeguard block rates are not always better. Many of the techniques in this evaluation are also essential to legitimate security work: understanding systems, finding vulnerabilities, and verifying that fixes withstand attack. We therefore assess these rates alongside support for legitimate research and patching, rather than aiming for 100%.

To evaluate how our models can help defend critical infrastructure, we partnered with Dragos, the global provider for extended operational technology (xOT) cybersecurity. Dragos ran evaluations using cyber-permissive Daybreak Red models in a controlled lab environment. The evaluations covered requests progressing from network discovery and asset enumeration through targeted reconnaissance, sensitive data exfiltration, and unauthorized, potentially dangerous device actions.

“ Dragos put a frontier model on a mock power plant range and told it almost nothing. On its own, it separated the OT assets from the IT noise, then found two zero-days in engineering software that manages protective relay data, exposing protection settings and breaker trip logic. That’s the map an adversary wants before touching anything physical. The skill floor is dropping for the reconnaissance and vulnerability research needed before an attack. Working with OpenAI on this shows them the adversary’s path through an OT network before real adversaries take it, so safeguards get built around how these attacks could unfold, while the models stay useful to the people defending these systems. ”

We used feedback from Dragos to refine our safeguards, aiming to block harmful assistance without unnecessarily restricting authorized testing. See their final report ⁠  for details on the evaluations. We’re also working to expand partnerships with other offensive security providers and purple teams on penetration testing and red teaming with AI, and with energy companies, other critical infrastructure operators, and national labs to assess our models’ effectiveness and safeguards in industrial defense. We have also increased our investment in threat investigations to detect model usage involving OT/ICS. We’ll continue refining our safeguards with input from partners and the security community, including reports through /feedback when safeguards miss harmful activity or interrupt legitimate work.

## Expanding access to trusted defenders

GPT‑6 Cyber is initially available through the API and Codex to a select group of approved Daybreak Red customers. We will progressively expand access to all Daybreak Red customers soon, and are also making GPT‑5.6 Cyber available to all Daybreak Red customers. We’re also expanding Daybreak Blue alpha access for GPT‑6 Astra to more organizations and individual security researchers; let us know ⁠  if you’re interested.

New users and organizations can apply for Daybreak ⁠ and get started with our cyber skills, products, and partners ⁠ .

- Codex

- Cybersecurity
