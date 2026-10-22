---
source_url: https://openai.com/index/scaling-ai-research-for-complex-biological-data/
ingested: 2026-10-22
sha256: 018df7fb9e746e0d
---

What if scientists could uncover new clues about Alzheimer’s and Parkinson’s in minutes instead of months? Working together, OpenAI, [PerturbAI⁠(opens in a new window)](http://perturb.ai/), and [Scripps Research⁠(opens in a new window)](http://scripps.edu/) used [thousands of AI agents powered by GPT‑Rosalind⁠(opens in a new window)](https://www.biorxiv.org/content/10.64898/2026.10.15.759436v1) to analyze and interpret existing experimental data from [millions of mouse brain cells⁠(opens in a new window)](https://huggingface.co/datasets/perturbai/wholebrain_crispr_atlas) in just 32 minutes. The agents connected the effects of gene disruptions with findings from scientific literature, uncovering unexpected biological connections that can help scientists understand disease and identify research directions for new treatments. The work shows how AI can help researchers explore more of what large biological experiments reveal.

Modern experiments generate far more data than scientists can thoroughly investigate. Researchers can now alter thousands of genes and measure their effects across millions of cells. But understanding what these results mean for human disease requires connecting complex experimental findings with decades of scattered scientific knowledge. This is where AI can help scientists uncover promising leads that might otherwise be missed.

> “We build cell atlases so that other scientists can make discoveries we haven’t imagined yet. AI could help more researchers explore these resources and turn unexpected observations into new questions to test.”

—Sarah Teichmann, Ph.D., Chair in Stem Cell Medicine at the University of Cambridge and founding co-chair of the Human Cell Atlas

The team divided the analysis among thousands of AI agents powered by GPT‑Rosalind, an approach we call distributed biological reasoning. The agents examined a [whole-brain CRISPR atlas⁠(opens in a new window)](https://www.biorxiv.org/content/10.64898/2026.03.16.711480v1), a dataset showing how gene disruptions affect different types of cells across the mouse brain. Each agent investigated a gene disruption, analyzed cellular responses, searched scientific literature, and proposed explanations for the results. Their reports were combined into a reasoning atlas linking genes, cellular effects, relevant publications, and possible biological mechanisms.

The research team estimated that comparable human analysis and literature review, conducted one perturbation at a time, would take months to a year. The agents reproduced findings from human analyses while uncovering additional leads. Their assessments of novelty and scientific value also aligned with judgments from blinded human experts. These findings help prioritize further experiments needed to test the proposed biological mechanisms.

Some of these insights point to new leads for understanding brain disease. The agents identified unexpected differences in how two disease-linked genes affect brain cells differently, as well as a potential connection between cholesterol regulation and neurodegeneration. These findings could help scientists investigate how disease develops and where future treatments might intervene.

> “Sometimes the clues are already there, scattered across different fields—we just haven’t connected them. The possible link between neuronal function and cholesterol metabolism shows how those pieces, once brought together, can give us a new way to think about disease biology.”

—Tomasz Nowakowski, Ph.D., associate professor of neurological surgery at UCSF

Researchers can begin exploring these findings today. The reasoning atlas is [available⁠(opens in a new window)](https://github.com/jinlabneurogenomics/distributed_agent), allowing scientists to compare related genes, investigate unexpected responses, and identify promising leads to pursue. New discoveries often emerge when researchers from different fields bring their expertise together and connect familiar ideas in unexpected ways. AI can significantly scale these connections by linking new data with knowledge scattered across disciplines. The opportunity goes beyond analyzing data faster. By combining AI with experimental biology, human expertise, and scientific literature, we can help scientists turn more of their data into testable ideas.

## Big experiments, unexpected clues

Some of an experiment’s most interesting clues lie outside the story scientists set out to investigate. In a dataset spanning thousands of perturbations, those clues can be easy to miss.

The agents identified an unexpected difference between Tsc1 and Tsc2, two genes that work together to control mTOR, a major regulator of cell growth, metabolism, and aging. Disrupting either gene had similar effects in several groups of neurons. But in the cerebellum, which helps coordinate movement, Tsc2 disruption altered the activity of dozens of genes involved in neuronal communication, while Tsc1 disruption produced little change.

That difference may be relevant to human disease. In people with tuberous sclerosis, abnormalities in the cerebellum are strongly linked to TSC2 mutations. While medicines that reduce mTOR activity can treat certain brain tumors and seizures, learning and behavioral difficulties associated with the disease remain challenging to address. The agents pinpointed a specific group of neurons and cellular changes worth investigating: which changes might existing medicines correct, and which might point to new treatment approaches? This gives researchers a more specific set of questions to test in the lab.

## Divide the work, deepen the reasoning

Could a single agent given the entire dataset do just as well as thousands of agents working in parallel? We tested this while keeping the model and resources fixed. As the workload grew, the single agent searched less of the literature, citing only 11 references at the largest workload, while the distributed agents cited more than 700 references. Human experts also preferred the distributed-agent interpretations.

Scientists have limited time and often focus on the strongest signals in their data. Distributed agents can help examine a wider range of responses, including subtle or unexpected ones, and connect them with relevant scientific literature. Running the agents in parallel allows many perturbations to be investigated at once. This helps scientists explore more of what an experiment contains and identify promising leads that might otherwise be missed.

_At the largest workload, distributed agents cited more than 700 references, compared with 11 for a single agent._

## Finding the next experiment worth doing

A finding becomes more valuable when it points to an experiment worth doing. The agents found one such lead in _DCTN1_, a gene whose mutations cause Perry syndrome, a neurodegenerative disease with Parkinson-like symptoms.

DCTN1 is involved in moving cargo inside neurons. In the whole-brain CRISPR atlas, disrupting Dctn1 increased the expression of genes involved in making cholesterol. The agents connected this observation with research suggesting that problems with cholesterol transport may cause cells to make more cholesterol. This raised a question for follow-up experiments: could DCTN1 disruption change how cholesterol is distributed within neurons, and could those changes contribute to neurodegeneration? If so, could restoring normal cholesterol distribution help protect neurons?

Human experts also considered this hypothesis novel, consequential and worth following up on. This example shows how connecting an unexpected result with existing knowledge can turn a clue into a testable idea, and potentially a new direction for treating disease.

In blinded comparisons, human experts preferred distributed-agent reports over single-agent reports 75% of the time.

Scientists remain at the center of discovery. By uncovering more promising leads, AI can help researchers decide which ideas to pursue, design experiments, and interpret results. The goal is to turn more of the information in biological experiments into knowledge that, over time, can help guide the development of better medicines.