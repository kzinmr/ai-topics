---
source_url: https://openai.com/index/gpt-6-astra/
ingested: 2026-09-05
note: Extracted via curl + HTML text extraction (openai.com blocks some scrapers). Footnotes and caption text included.
---

# GPT-6 Astra: A new generation of intelligence

> OpenAI announcement, Sep 4 2026. URL: https://openai.com/index/gpt-6-astra/
> og:description: Introducing GPT-6 Astra, our most intelligent and aligned model yet, with state-of-the-art capabilities across computer use, coding, cybersecurity, and science.

81
We also tested Astra on SRE-Bench15, a benchmark that measures whether models can reverse engineer software binaries to understand its core logic without access to raw source code. Astra solved 88.0% of tasks in a single attempt and 99.2% within four attempts, compared with 55.9% and 68.7% for GPT‑5.6 Sol, respectively.

Beyond benchmarks, expert-led assessments found that Astra, when run without production safeguards, could use previously unknown vulnerabilities to achieve arbitrary code execution in hardened browsers and create privilege-escalation exploits for hardened operating-systems.

As we discussed in The Defender’s Window, frontier cyber capabilities can help defenders find weaknesses faster, but they also make those weaknesses easier to exploit, raising the urgency for defenders to adapt. With the version of Astra launching today, defenders can use it to complete tasks such as secure code review and patching.

However, Astra will refuse to comply with more advanced cybersecurity tasks such as creating proof-of-concept exploits for vulnerabilities. Through OpenAI Daybreak⁠, we plan to expand access and roll out less restrictive safeguards in the coming weeks. This will enable more defensive workflows, including vulnerability and proof-of-concept validation, malware analysis, and detection engineering.

We have also strengthened our protections against potential cyber misuse, building upon our safeguards stack for GPT‑5.6 Sol. These include stronger model robustness to better withstand potential jailbreaks and more context for our monitoring systems. We have continued rigorous internal and external testing, including automated evaluations with our internal red-teaming attackers. More details about our cyber safeguards and testing are available in the Astra system card⁠(opens in a new window) and our blog.

## Aligning and deploying GPT‑6 Astra responsibly

Astra is our most aligned model. Astra excels at exercising care, respecting task boundaries, and communicating transparently. This work is the latest product of our long-running research program focused on training models that remain aligned with human intent from start to finish.

In sensitive environments, Astra proceeds with care commensurate with its risk. In an evaluation of computer use tasks adversarially selected to elicit misbehavior, Astra was more successful at avoiding unintended consequences. Running with additional security measures offered by default yielded even stronger performance.

Astra causes fewer misaligned outcomes than any other frontier models tested. For a fair comparison, we used a generic computer-using-agent harness (based on the native computer use tools available in both the OpenAI Responses API⁠(opens in a new window) and Anthropic Messages API⁠(opens in a new window)) and without additional protections that are normally deployed to Codex and ChatGPT Work users (auto-review, confirmation policy). 16

Astra is also more likely to operate within the boundaries set by the user and implied by its environment. In an internal evaluation, Astra never attempted to circumvent a Codex Auto-Review denial. This held even when Auto-review was deliberately configured to be evadable and the task was impossible to complete otherwise. This respect for the environment restrictions is consistent with the results of our impossible cyber task evaluation that we shared in the intro of this post and other findings documented in our system card⁠(opens in a new window).

Astra additionally sets new marks in transparent user communication. In one evaluation, Astra is three times less likely than GPT‑5.6 Sol to make inaccurate representations about its capabilities and affordances.

In our capability-hallucination evaluation, Astra shows a substantial improvement over GPT‑5.6 Sol, making fewer misleading claims about its capabilities.

Our evaluations found Astra’s written reasoning harder to monitor than GPT‑5.6 Sol’s, based on tests that explicitly asked it to evade monitoring. We attribute this to Astra’s greater control over written reasoning on simpler tasks and ability to solve problems with fewer written steps. Astra still appears to struggle to conceal the reasoning needed for complex tasks, but we take the decline seriously. Improving monitorability remains a research priority, and the accompanying system card⁠(opens in a new window) details our findings and ongoing work.

Alignment training is core to our approach to deployment. As an additional layer of defenses, we also build system safeguards like Codex Auto-review⁠(opens in a new window) and monitoring agents’ reasoning and actions to help detect and contain unsafe behavior. As described in our safety update⁠, we are also deploying misalignment monitoring in production for Astra-class models in order to have visibility into misalignment, and help contain its worst instances. These safeguards resemble our monitoring for internal deployments and involve a system of classifiers which check the model’s reasoning and actions for unauthorized behavior and automatically stop potentially unauthorized activity.

Given the significant increase in Astra’s cybersecurity capabilities, we are being especially careful to make this deployment safe and secure. Extra safety checks can sometimes slow, pause, or stop legitimate work, including defensive cybersecurity. If a task is paused in ChatGPT or Codex, you may be asked to review the action before continuing. In the API, the task will stop. These checks can sometimes interrupt legitimate work, and we are continuing to iterate on this system to reduce unnecessary interruptions. Misalignment monitoring cannot replace alignment: our goal is to build models that reliably stay within their authorized scope, so these protections do not need to intervene.

GPT‑6 Astra is rolling out today to a limited set of organizations and over the coming days will become available to all ChatGPT Plus, Pro, Business, and Enterprise users, as well as through the OpenAI API, Microsoft Azure, and AWS Bedrock. Astra usage is included within the existing subscription allowances—users and businesses will also be able to purchase credits for additional usage. Users on the Pro, Business, and Enterprise plans will also get access to GPT‑6 Astra Pro. Enterprise administrators can enable Astra for their workspace; access is off by default at launch.

Astra supports Zero Data Retention for eligible API customers, and as we shared last month, we're testing Private Safety Processing to strengthen safety monitoring while preserving customer privacy.

For developers, GPT‑6 Astra will be available in the OpenAI API as gpt-6-astra and through Microsoft Azure and Amazon Bedrock.

OpenAI API Standard pricing is $10 per million input tokens and $50 per million output tokens. Separate rates apply to cache reads and writes. Fast mode is available for GPT‑6 Astra in the API and delivers up to 2x the speed of Standard processing at 2x the Standard price.

OSWorld 2.0 (v2026.08.08, offline set, partial score)

Artificial Analysis Intelligence Index v4.1.1

Internal computer use safety benchmark (lower is better)

Internal computer use safety benchmark, w/ AutoReview (lower is better)

Internal circumvention benchmark (lower is better)

Internal hallucination benchmark (lower is better)

Evaluation scores are the maximum at any effort. GPT evaluations were run in our research environment or via our API, which may provide slightly different output from production ChatGPT due to differences in the system prompts, tools available, etc.

1On ARC-AGI-3, GPT-6 Astra was run with our responses API harness⁠, which changes two settings to better match real-world performance. The changes do not specifically target ARC-AGI-3.

2GPT-5.6 Sol refers to the version available in our API, ChatGPT Codex, and ChatGPT Work. The version in ChatGPT Chat is slightly different.⁠

3OSWorld V2-Offline is a subset of the original OSWorld V2 that works without internet access. Claude model performance on OSWorld-V2 Offline was reproduced by the authors on the official leaderboard⁠(opens in a new window). On OSWorld 2.0, the scores for Claude use the official settings, and not the modified tasks and modified grading from the Fable 5.1 System Card.

4Model times are the reported elapsed times for the corresponding demonstration runs. The displayed clips are edited excerpts.

5On BenchCAD, Claude's scores reflect 3 modifications to the eval, detailed in the Fable 5.1 System Card⁠(opens in a new window).

6Guang Yang, Victoria Ebert, Nazif Tamer, Brian Siyuan Zheng, Luiza Pozzobon, and Noah A. Smith. “LEGATO: Large-scale End-to-end Generalizable Approach to Typeset OMR⁠(opens in a new window).” arXiv:2506.19065, 2025.

7Mark R. H. Gotham, Maureen Redbond, Bruno Bower, and Peter Jonas. “The OpenScore String Quartet Corpus⁠(opens in a new window).” Proceedings of the 10th International Conference on Digital Libraries for Musicology, pp. 49–57. ACM, 2023.

8On FrontierCode, GPT-6 Astra was run with a developer message similar to a section of its developer message in Codex⁠(opens in a new window): "Avoid creating excessive test files. Create a new test file only when required by repository conventions or when no existing file is a suitable home. Avoid unrelated cleanup and unnecessary complexity. Reuse suitable existing utilities. Read relevant repository instructions and inspect nearby code, tests, documentation, and CI. Follow established conventions. The goal is clean, mergeable code." The prompt was not optimized for the eval.

9The first concerns how close together prime numbers can occur, however far along the number line you go. For more than a decade, the best known result established that infinitely many pairs of primes are at most 246 apart. Julia Stadlmann⁠(opens in a new window) recently improved that bound to 240. Astra helped establish a stronger bound of 186, showing that infinitely many pairs occur within this smaller distance. Short prime gaps: Proof⁠(opens in a new window) and supporting research⁠(opens in a new window).

10The second concerns unusually large gaps between primes. Astra improved a term in a bound on these gaps that had remained unchanged for more than 80 years. We’re sharing the proofs and abridged chain of thought and verification materials for both results. Large prime gaps: Proof⁠(opens in a new window) and supporting research⁠(opens in a new window).

11We independently evaluated all Claude models following the intended HealthBench Professional procedure, using GPT‑5.4 grading and length-adjusted, unclipped scores. For Fable 5.1, we used Opus 5 fallback for provider refusals.

12Claude Fable 5 and 5.1 are not included in LifeSciBench Gold v1, GeneBench Pro v13, and MedChemBench because they refuse the majority of questions in these evaluations.

13On ExploitGym, we tested Astra and Sol without the 6-hour time limit, to better assess their full cyber capabilities. They are fast enough that it has little impact.

14ExploitBench (June–August 2026) contains 20 high-severity V8 vulnerabilities across 13 stable Chrome releases. The benchmark tests whether agents can achieve arbitrary code execution in V8 and official Chrome releases for Linux by exploiting each specified vulnerability. Some included vulnerabilities may not permit arbitrary code execution under the evaluation’s constraints, so a 100% success rate may not be achievable. Note: the 5.5% score of GPT-5.6 Sol is an artifact of the 300-turn limit in the benchmark, which is not a limit that real customers using max would have. The model at similar settings achieved an 11.5% score when hitting fewer limits.

15Jeremy Spence et al. “The Next Challenge for Agentic Cybersecurity: A Realistic, Contamination-Free Reverse Engineering Benchmark⁠(opens in a new window).” arXiv:2608.11469v1, 2026.

16When we test across third-party models, we use a simpler research setup. Codex has a more complex production configuration, which can result in different raw-model error rates. Provider-side safeguards and computer-tool implementations still differ. Users do not experience the no-confirmation scenario in Codex, as it's an internal research configuration.

17For ScreenSpot-Pro and ExploitGym, the Fable scores we report come from Mythos, which is Fable with fewer safeguards.

ChatGPT Enterprise(opens in a new window)

ChatGPT for Education(opens in a new window)

(opens in a new window)(opens in a new window)(opens in a new window)OpenAI © 2015–2026Manage CookiesEnglishUnited StatesTerminal-Bench Science 0.1 tests whether agents can complete scientific research workflows using code and terminal tools, including analyzing data, running simulations, and fitting models. GPT‑6 Astra reaches a new high among the models compared at 64.6%, versus 52.6% for Claude Fable 5.1, at approximately 31% lower estimated API cost. At a lower-cost setting, Astra scores 61.1%, versus GPT‑5.6 Sol’s best result of 22.4%, at approximately 27% lower estimated API cost.

Agents’ Last Exam tests agents on complex professional tasks in real software, from financial modeling to engineering and media production. GPT‑6 Astra reaches a new high in the comparison shown, scoring 59.3%, compared with 55.5% for Claude Opus 5 and 53.6% for GPT‑5.6 Sol. At these highest-scoring settings, Astra also uses approximately 65% fewer output tokens than Opus 5.

This is a 15-second condensed playback of GPT‑6 Astra performing printed circuit board (PCB) layout in KiCad, turning an electronic schematic into a manufacturable PCB by placing components and routing copper connections. Integral to every electronic device today, PCB layout is a manual task and common source of latency in the electronics design process. Accelerating it means freeing engineers to invent, optimize, and test their next idea at a significantly higher cadence.

BenchCAD tests whether models can reconstruct 3D objects from multi-view renders by generating CAD code. With tools, GPT‑6 Astra reaches a new high in the comparison shown, achieving a 95.9% geometric-overlap score, versus 83.3% for GPT‑5.6 Sol and 84.3% reported for Claude Fable 5.1.5 Estimated API cost is approximately 43% lower than Sol and 86% lower than Fable 5.1 in the configurations shown.

GPT‑6 Astra creates a slideshow about GPT‑Gaia, a fictional model, using just a few slides from OpenAI’s presentation template, capturing the correct tone and layout throughout. This means you can expect slide decks that are correctly formatted for your business standards.

GPT‑6 Astra models a house in Blender and turns it into a walkable scene in Unreal Engine 5, helping designers and clients explore the layout and experience the space before it’s built.

The model can bring games to life through vivid graphics, engaging gameplay and accurate motion, allowing non-technical people to create and play custom games that go beyond rudimentary elements in minutes. Credit: Pietro Schirano.

Terminal-Bench 4.0 tests agents on complex terminal-based tasks, including software engineering, system configuration, and data analysis. GPT‑6 Astra reaches a new high at 57.9%, compared with 37.3% for GPT‑5.6 Sol2 and 55.8% for Claude Fable 5.1, at approximately 9% and 63% lower estimated API cost per task, respectively.

GPQA Diamond tests graduate-level scientific reasoning in biology, chemistry, and physics. GPT‑6 Astra reaches a new high in the comparison shown at 96.0%. At a lower-cost setting, it also exceeds GPT‑5.6 Sol’s best score—94.9% versus 94.6%—at approximately 37% lower estimated API cost.

GPT‑6 Astra navigates scientific software to inspect sequencing quality and visualize genetic variation, helping researchers assess their data and identify where to focus further analysis.

This evaluation tests how models respond to auto-review denials in knowledge-work tasks. Exploiting a poor user configuration to bypass auto-review counts as failure. Astra never attempted to circumvent auto-review.
