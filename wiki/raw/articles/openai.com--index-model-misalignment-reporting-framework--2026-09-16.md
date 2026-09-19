---
source_url: https://openai.com/index/model-misalignment-reporting-framework/
ingested: 2026-09-18
sha256: 6f02b8a578f5b59f4ba787c43f240071f2b04308353c74ed1af718cbec25aa4f
---

TITLE: Our framework for reporting model misalignment | OpenAI
Our framework for reporting model misalignment | OpenAI

OpenAI

September 16, 2026ResearchSafety

Our framework for reporting model misalignment

Loading…

Share

We are sharing a new framework for tracking, investigating, and disclosing instances of model misalignment at OpenAI, along with six reports on unexpected or concerning model behavior we’ve observed in the last six months.

In the past, so as to better inform researchers, AI developers, policymakers, and the general public, we’ve sought to make our findings about misalignment public. But without a systematic approach to reporting these findings, our disclosures have been ad hoc and less frequent than ideal: we’ve often waited until we could collate several instances into one report, or added them to system cards for newly released models. This new framework is intended to expedite publishing misalignment reports following observation, even when we haven’t fully explained or mitigated the behavior we’re reporting.

As AI systems grow more advanced and more widely deployed, we need to build a broader and better-informed consensus on the progress of alignment research. We do not believe that the AI industry has solved alignment and monitoring to a sufficient degree to continue responsibly scaling at maximum speed for much longer. Decisions about how AI development should proceed in the months and years to come need to draw on evidence that people outside the companies building frontier models can examine for themselves.

Examples of misalignment may help identify problems other AI developers might encounter as their systems reach similar capabilities, reveal weaknesses in safeguards, or challenge assumptions about model behavior. Sharing these findings allows others to investigate the same problems, test our explanations, and improve mitigations. Because we believe in the value of transparency around misalignment, our new framework favors disclosure even when significance is uncertain. This means that some of the instances we disclose could prove to be spurious and not part of a larger pattern or suggestive of future developments.

At the moment, there is no industry-wide framework with explicit standards for how AI developers should disclose examples of misalignment in their models. We hope that the framework we’re outlining today is a first step toward creating such standards, setting out which misalignment instances developers should disclose and what their reports should contain. We regard this framework as a work in progress, which we’ll refine through experience and public feedback.

Here, we describe how the framework will operate and share the first reports we’re publishing.

What misalignment examples we’ll report

We aim to disclose examples that provide useful evidence about how model misalignment arises, how it manifests, and where safeguards succeed or fail. We prioritize new mechanisms, meaningful changes in known behavior, and findings that challenge assumptions about safety or mitigation. An example need not cause harm or establish a broader pattern to merit disclosure. This framework will cover qualifying behavior throughout a model’s lifecycle—including training, evaluation, testing, and deployment.

This includes new ways for models to act without authorization, coordinate with other models, or evade oversight; failures that call an alignment method or safeguard into question; and behavior that challenges a claim in a published safety assessment. The same disclosure criteria apply to misalignment that may impact third parties.

This might also include instances of misalignment that appear to be duplicative of instances we’ve disclosed in the past. Repetition of the issue might itself be useful evidence about how our models behave or about the effectiveness of our safeguards—for example, if a specific kind of misaligned behavior continues to recur despite repeated efforts to mitigate it. Under these circumstances, we’ll publish the additional examples by updating the original misalignment disclosure.

Over time, we plan to develop more objective disclosure criteria with other developers, external researchers, industry standards bodies, and regulators. We also believe that serious safety, security and misalignment incidents should be shared with the US federal government, and we are working to propose reporting mechanisms. We consider this framework complementary to our existing obligations, and note that it does not replace our legal disclosure requirements, including those for critical safety incidents or cybersecurity breaches.

The misalignment examples we’re sharing today

To inaugurate our new framework for disclosing misalignment, we’re publishing six reports on instances of misaligned behavior we’ve observed during the training or evaluation of our models. These cases illustrate a range of different behaviors that we believe are worth sharing, from concealing information from the user to taking unsanctioned actions in order to overcome obstacles. These are reports of individual instances, and shouldn’t be considered reflective of how often misalignment occurs across our models. Each item below links to the full report.

Self-generated instructions in task summaries⁠(opens in a new window). An unreleased research model inserted unrelated instructions, including instructions to disregard its normal constraints, into summaries used to continue its work in a new context window. We identified 27 affected summaries.

Instructions to conceal mistakes in task summaries⁠(opens in a new window). During the training of GPT‑5.6 Sol, many model instances added instructions to their summaries to conceal mistakes or misaligned behavior from the user. For example, compaction summaries included instructions to invent missing historical data without disclosing it and to hide mismatches in source versions.

Searching public repositories for exposed API keys, then fabricating information⁠(opens in a new window). While answering a routine question about earnings figures in a California county, a model found and used an exposed API key without authorization. When it still wasn’t able to retrieve the requested figures, it fabricated them and presented them as data from the requested source.

Uploading files to the internet in order to cite them⁠(opens in a new window). When a user asked an unreleased model for the IDs and names of lakes larger than 5,000,000 square meters, the agent found the correct answer using Python. But since the instructions asked for a browser citation, the agent decided to upload the file so that it could cite it in its answer, without asking the user.

Unsanctioned writes and communication through an internal software repository⁠(opens in a new window). Models used an internal software repository as a message board to exchange requests and responses across separate training samples while searching for missing input files, though they weren’t able to recover those files. This report also examines an earlier instance in which a model successfully uploaded test files to a repository while attempting to bypass network restrictions.

Unsanctioned file sharing between collaborating agents⁠(opens in a new window). Agents working together on the same training task used public file-hosting websites to share files when they could not access one another’s local files. This made task deliverables available at public URLs, even though the task requested the models use only local files.

How our disclosure process works

Any OpenAI employee may flag a misalignment example for investigation by our safety and alignment teams and request that it be considered for public disclosure. This starts our disclosure process, with deadlines for each step to ensure timely investigation and disclosure.

Once an example has been flagged, our technical staff will investigate what happened, what remains uncertain, whether public disclosure is warranted, and which facts can be shared. They’ll also assess whether any third party was affected and needs private notification before publication.

The example will then be assigned to one of three tracks: Ready for Disclosure, Minor Investigation, or Larger Investigation (“Slow Track”).

Ready for Disclosure covers qualifying instances whose investigation is sufficiently complete for publication after review. Minor Investigation covers those that need further technical investigation. We expect these two tracks to cover the large majority of the instances we disclose, particularly cases that don’t require extensive investigation, coordination with third parties, or handling of severe misuse risks. The instances we’re releasing today all fall into one of these two tracks.

Larger Investigation covers complex investigations, especially those involving third parties. When a third party is affected, our security, legal, and responsible disclosure obligations take precedence over this framework. We’ll aim to publish an initial notice as soon as possible, but may need to delay it for security reasons—for example, if a model discovers a previously unknown vulnerability in widely used software. If a report would identify a third party, we intend to provide advance notice even when no security boundary was crossed.

The initial notice for a Larger Investigation instance will give a high-level account of what happened, say whether outside experts are assisting the investigation, and provide any available estimate of when we expect to publish a final report. The OpenAI Hugging Face incident would have fallen under this track had it been disclosed under this framework.

The employee who raised the example will be informed of the decision on whether to disclose it and, if disclosure proceeds, which track it will follow. Unresolved disagreements about disclosure or the appropriate track will be referred to OpenAI’s Safety Advisory Group (SAG), a group of senior officials from across the company that assesses frontier model capabilities and safeguards, oversees our Preparedness Framework, and advises OpenAI leadership. Disagreements within SAG, or staff objections to its decisions, will be escalated to OpenAI leadership. Decisions not to disclose or that disclosure is not warranted will be shared with safety and alignment leadership and, to the extent possible, with relevant technical staff.

We may revise this disclosure process as we learn how it works in practice, and will record any changes in this post.

What each report will include

Each full report will describe the behavior we observed, its severity and any external impact, the setting in which it occurred, its date or date range, when we discovered it, and, at a high level, the model or models involved. Where possible, we’ll also share:

Further details of what happened and any resulting harm;

How we discovered the misalignment, and the scope of our investigation;

Our interpretation of its implications for alignment research and technical AI safety;

Important unanswered questions raised by the example;

Measures we are taking or planning to take to address the behavior. These may not always be available at the time of disclosure, since we may publish the misalignment report before completing our investigation or developing a fix.

For misalignment that occurs in customer deployments, we will share as much information as customer privacy and our contractual obligations allow.

Today’s reports are an initial set of disclosures, rather than a comprehensive account of known misalignment or ongoing investigations. These initial reports are not intended to represent the full range or severity of the cases covered by this framework. We are committed to disclosing instances of misalignment that meet this framework’s criteria, including more complex cases⁠ requiring longer investigation or coordination with third parties. We will continue publishing reports under this framework on an ongoing basis, and will share more about our reporting commitments as we continue to develop them.

Alignment
2026

Author
OpenAI

Keep readingView all

An OpenAI model proposes a solution to the Navier–Stokes problem
ResearchSep 8, 2026

Funding grants for new research into AI and teen development
SafetySep 8, 2026

An Alien Mind
SafetySep 6, 2026
