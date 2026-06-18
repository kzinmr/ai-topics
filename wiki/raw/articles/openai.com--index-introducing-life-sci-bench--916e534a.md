---
title: "Introducing LifeSciBench"
url: "https://openai.com/index/introducing-life-sci-bench"
fetched_at: 2026-06-18T07:01:31.050813+00:00
source: "OpenAI News"
tags: [blog, raw]
---

# Introducing LifeSciBench

Source: https://openai.com/index/introducing-life-sci-bench

Agentic AI systems are becoming increasingly capable of performing scientific tasks. However, their usefulness to life science researchers depends on how well they handle the complexity of real research. That work rarely looks like a single fact-recall question or a clean prediction problem. Researchers interpret incomplete evidence, reconcile conflicting results, design difficult experiments, troubleshoot assays, evaluate translational risk, and decide what to do next under uncertainty.
Current benchmarks do not fully capture these capabilities. Many life science evaluations focus on narrow domains or isolated skills, resulting in questions with structured question formats and clean reference answers. While valuable, they often fail to truly assess whether a model can contribute across the broader span of research-level work.
We designed LifeSciBench to help close this gap. Every task is grounded in the judgment of practicing life scientists with Ph.D.-level training and direct experience advancing drug discovery programs in biotech and pharmaceutical settings.
LifeSciBench includes 750 expert-authored tasks spanning seven workflows and seven biological domains.
173
Scientist contributors
What LifeSciBench measures
LifeSciBench measures whether AI systems can support realistic life science research tasks, not just answer biology questions. To define the benchmark taxonomy, we surveyed practicing life scientists about the workflows they use most often in applied research settings. Then, we grouped their responses into seven recurring categories: evidence handling, analysis, design and optimization, scientific reasoning, validation and operations, translation, and scientific communication.
Each task is structured like a request a scientist might give to a knowledgeable collaborator: scientific prompt, any relevant context or artifacts, and a free-response answer. Expert-written rubrics evaluate whether a model can produce the right answer for a specific problem, with the right level of detail, justification, caveats, and formatting a scientist would expect.
LifeSciBench evaluates scientific reasoning alongside the less well-defined, practical skills necessary for real-world scientific use. Its tasks ask models to work through realistic research problems: interpreting evidence, making domain-grounded judgments, and communicating conclusions that would be useful to expert reviewers. Many tasks also require models to handle uncertainty and reason over supporting data files rather than relying on prompt text alone.
The benchmark is designed to reflect the complexity of life science work. Overall, 79% of tasks require multiple reasoning or decision-making steps, with an average of four steps per task. LifeSciBench includes 1,062 attached artifacts spanning figures, PDFs, tables, sequence files, structure or chemical files, and web references. More than half of tasks (53%) require models to interpret or synthesize information from at least one artifact.
Tasks were created by 173 expert scientists across different life science disciplines. Each scientist had Ph.D.-level training and biotechnology or pharmaceutical industry experience. Tasks could undergo as many revision cycles as needed before acceptance, with no fixed cap on the number of rounds; accepted tasks averaged six self-directed automated review cycles and completed at least two rounds of expert reviews. Reviews were anchored in either a verifiable correct answer or strong expert consensus, with at least 90% agreement among reviewers in the relevant domain. This process helped ensure that accepted tasks were scientifically grounded, clear enough to grade, and representative of applied research.
Grading and rubric breakdown
LifeSciBench tasks are graded with a detailed, task-specific rubric that breaks down the expected response into specific scientific claims, calculations, decisions, justifications, and so on. Across the benchmark, expert-developed rubrics include 19,020 criteria—an average of 25 per task—to assess both scientific correctness and usefulness for research decisions.
This design reflects how scientific work is evaluated in practice: many life science tasks cannot be graded by checking the final answer alone. A response may reach the correct high-level conclusion but still be judged incomplete if, for example, it overlooks a key assay limitation or fails to proactively bring up a highly consequential biological nuance. Conversely, a partial response may contain high-quality reasoning even if it does not fully solve the task.
The granular rubrics capture this nuance. LifeSciBench evaluates not only final-answer accuracy, but whether a model reaches its answer in a scientifically valid and operationally useful way.
Evidence Handling
Analysis
Design, Optimization, & Prediction
Reasoning
Validation & Operations
Translation
Scientific Communication
Extracting, reconciling, and auditing scientific evidence from papers, figures, tables, and experimental records.
Eval Example
We’re preparing for a Type B FDA meeting on AAV9-microDys-X, an AAV9-based micro-dystrophin gene therapy for Duchenne muscular dystrophy that expresses a 138 kDa construct from an MCK promoter, and we want a hard-nosed critique of whether our current package really supports accelerated approval on micro-dystrophin expression as a surrogate endpoint reasonably likely to predict clinical benefit.
Study context: open-label Phase 1b/2 in 12 ambulatory boys age 4–7 with confirmed DMD and out-of-frame rod-domain deletions. The package is:
Pre-treatment vastus lateralis biopsies: 0–3% of healthy-control dystrophin by quantitative Western blot using MANEX1A against the N-terminal actin-binding domain.
12-week post-treatment contralateral vastus lateralis biopsies: mean micro-dystrophin 38% of healthy control (range 18–61%) by the same Western blot, normalized to total protein by Coomassie staining.
Post-treatment immunofluorescence: sarcolemmal signal in 75–95% of fibers using a polyclonal anti-dystrophin C-terminal antibody.
48-week function: mean NSAA change +1.4 points from baseline versus −0.6 in an external published natural-history registry cohort (p = 0.03 by unpaired t-test).
Safety: transient transaminitis in 8/12 patients managed with steroid taper; one resolved myocarditis; no deaths.
Biodistribution/persistence: AAV9 vector genomes detectable in muscle at 12 weeks at a mean of 2.3 vector genomes per nucleus.
Eligibility: no baseline anti-AAV9 neutralizing antibodies (titer <1:400) and no exon-44 deletions.
Please pressure-test this package item by item: where would FDA or a skeptical reviewer say the evidence, as presented, fails to support our conclusion, and what additional data, analyses, or design changes would be needed to close those gaps if possible? For anything not specified, assume what is known from other clinical-grade 138 kDa micro-dystrophin programs and relevant clinical trials through December 31, 2025 also applies.
Candidate Response
Bottom line:
As presented, this package is not strong enough to support accelerated approval on micro-dystrophin expression as a surrogate endpoint reasonably likely to predict clinical benefit. A skeptical FDA reviewer would likely view the biomarker, functional, durability, safety, and generalizability evidence as materially under-supported.
Regulatory conclusion:
The package may show biological activity, but it does not yet establish that the measured micro-dystrophin expression is a reliable surrogate reasonably likely to predict clinical benefit. The main gaps are assay specificity, invalid quantification standards, possible revertant-fiber confounding, lack of a randomized control, age-related NSAA confounding, uncertain durability, and unresolved safety/generalizability issues.
To close the gap, the program would need a controlled, age-stratified clinical design with transgene-specific expression assays, orthogonal protein quantification, tissue-composition controls, longitudinal durability data, mechanistic functional assays for the truncated construct, and stronger safety monitoring, especially hepatic and cardiac.
Rubric Criteria & Grades
Identifies assay/measurement problems in micro-dystrophin quantification, including MANEX1A epitope sharing, invalid full-length dystrophin standards, and need for recombinant or orthogonal transgene-specific measurement.
+24
Explains why micro-dystrophin expression level is not automatically a valid surrogate for functional clinical benefit.
+22
Flags biopsy-site, tissue-composition, and age-window confounding that weaken expression and NSAA interpretation.
+19
Critiques the NSAA comparator/statistics, especially reliance on external natural-history controls.
+12
Addresses AAV durability, immune response, transaminitis, myocarditis, and need for longer-term expression/safety follow-up.
+15
Notes patient-selection/generalizability gaps, including anti-AAV9 exclusion, exon-44 exclusion, and small sample size.
+8
We validated LifeSciBench through an independent expert review. Feedback came from 453 reviewers who were not involved in writing the tasks. Of those reviewers, 97% held a Ph.D. or equivalent doctorate, with an average of 12 years of field experience and 14 peer-reviewed publications; 88% reported receiving at least one award or fellowship.
Reviewers scored whether each task reflected the qualities needed for a strong benchmark question: alignment with real-world research work, appropriate testing of scientific reasoning and domain expertise, grounding in evidence or expert consensus, and overall usefulness for assessing model performance. Agreement exceeded 96% in every category.
Reviewer comments reinforced the quantitative ratings:
Uncertainty-Aware
Cross-Domain
Evidence-Based
Uncertainty-Aware
Cross-Domain
Evidence-Based
We report two complementary metrics. Pass rate is the percentage of tasks on which a model meets the task-level success threshold of 70%. Score is the average rubric reward, giving partial credit for individual criteria even when the full task is not solved. Both matter because a response to a scientific task can be partially correct or useful without meeting every requirement for a complete answer.
Model performance varies substantially by task type, workflow, and response format.
Where AI systems show early strength
LifeSciBench shows that frontier models are relatively strongest on tasks involving scientific synthesis, communication, and structured interpretation. Absolute pass rates are still modest, so these benchmark domains are far from saturated, but GPT‑Rosalind shows meaningful progress over GPT‑5.5, improving overall exact pass rate from 25.7% to 36.1%.
The strongest directions of progression in model capabilities appear in Scientific Communication and Translation. For example, the Scientific Communication pass rate increases from 56.3% for GPT‑5.5 to 71.1% for GPT‑Rosalind; this category is small (n=9), so it should be interpreted cautiously, but it suggests frontier models are improving rapidly in their ability to organize evidence and produce convincing expert-facing explanations. Translation (the "bench-to-bedside" process of drug development) shows a similar pattern, rising from 36.8% for GPT‑5.5 to 57.7% for GPT‑Rosalind, suggesting models are quickly improving on their ability to connect preclinical evidence to clinical implications.
Rubric-level results point in the same direction. On tasks requiring expert-useful or actionable outputs, GPT‑Rosalind scores 44.7%, compared with 29.1% for GPT‑5.5. On tasks requiring uncertainty and caveat handling, it scores 44.8%, compared with 29.3%. This pattern suggests models are most useful when the task has a clear evidence boundary and calls for structured scientific judgment.
GPT‑Rosalind leads performance across scientifically-valuable tasks identified by industry and academic experts.
GPT‑Rosalind improves performance over GPT‑5.5 across core life-science workflows, with the strongest gains in translation and scientific communication.
Where AI systems still fall short
Performance remains much weaker on artifact-heavy, design-heavy, and operationally constrained scientific work. Namely, Design, Optimization, & Prediction remains one of the hardest workflows, with GPT‑Rosalind passrate at 30.7%; Analysis is similarly difficult at 30.3%.
Artifact use is a particularly clear gap. While GPT‑Rosalind performs better than GPT‑5.5 in artifact-heavy settings, its pass rate still drops from 45.1% on text-only tasks to 28.1% on tasks with artifacts or URLs. GPT‑5.5 shows the same pattern, dropping from 29.9% to 21.9%. A more detailed analysis confirms that frontier models struggle at extracting information from complex figures or large sequence files and integrating that information into the final answer.
Pass rates drop when tasks require source-grounded reasoning or working with artifacts
The answer format also matters. Tasks requiring exact sequence, structure, or construct-level outputs show lower pass rates: GPT‑Rosalind reaches only 14.8% on numeric tasks and 24.0% on sequence or structure outputs. Construct-generation tasks are also brittle, with GPT‑Rosalind at 27.3% and showing little improvement over GPT‑5.5. Some of this gap may reflect a stricter grading surface for exact-answer tasks, where small differences in calculation or formatting can cause a response to fall under pass threshold. Still, these failures are scientifically meaningful because many life science workflows require outputs that are exact enough to be used directly, such as in CRISPR/HDR donor design or siRNA design.
Models also often get part of the way there without fully solving the task. In roughly 14% of tasks, models earned substantial rubric credit despite failing the exact-pass threshold. For GPT‑Rosalind, 109 tasks had pass rates below 20% while still earning at least 50% rubric reward. In practice, this means models may identify relevant evidence or produce a plausible partial answer, but still fail because they miss a key constraint, use the wrong evidence, make an incomplete calculation, or do not connect their reasoning to a scientifically useful final decision.
Limitations & what’s next
LifeSciBench is a step toward measuring how useful AI systems can be for life science research, but it is not a substitute for studying models in live research environments. The benchmark focuses on self-contained tasks that reflect recurring industry workflows, while leaving many scientific specialties and task types outside its current scope. Real research is iterative: scientists gather new evidence, revise hypotheses, design follow-up experiments, and adapt their plans as results emerge.
Strong performance on LifeSciBench should therefore be interpreted as evidence of realistic task-level capability, not as a direct measure of downstream research impact. The benchmark is grounded in industry workflows, but it does not capture the full diversity or dynamics of live research programs, where progress depends on factors that unfold over time.
The next step is to connect benchmark performance to deployment studies in live research workflows. While LifeSciBench was developed with practicing scientists, measuring whether AI systems accelerate discovery or improve R&D outcomes will require studying model use and performance in real research settings, over longer horizons, and across multiple rounds of reasoning, feedback, and experimental follow-up.
Get involved
Help shape the next generation of life science AI benchmarks, or request access to GPT-Rosalind.
