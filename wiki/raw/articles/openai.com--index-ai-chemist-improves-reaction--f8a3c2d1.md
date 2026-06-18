---
title: "A near-autonomous AI chemist improves a challenging reaction in medicinal chemistry"
url: "https://openai.com/index/ai-chemist-improves-reaction"
fetched_at: 2026-06-18T07:02:00.000000+00:00
source: "OpenAI News"
tags: [blog, raw]
---

# A near-autonomous AI chemist improves a challenging reaction in medicinal chemistry

Source: https://openai.com/index/ai-chemist-improves-reaction

With Molecule.one's Maria, GPT-5.4 found a surprising additive boosting Chan-Lam Coupling yields for over 80% of tested substrates.

## Overview

OpenAI's work in science is motivated by a simple belief: advanced AI can become a powerful partner for scientists, helping them explore more ideas, connect distant concepts, design better experiments, and accelerate discoveries that benefit humanity. We have already shared early examples of models contributing to novel results in mathematics, including work on the unit distance problem, in theoretical physics, through a new result on gluon amplitudes, and in biology, where GPT-5 helped lower the cost of cell-free protein synthesis in an automated lab. We also introduced GPT-Rosalind, a purpose-built model to support life sciences research and drug discovery workflows.

This project extends that trajectory into medicinal chemistry, where progress cannot be measured by reasoning alone. A hypothesis has to work in the lab with real molecules, instruments, and experimental noise. Working with Molecule.one, we connected GPT-5.4 to Maria—an agentic chemistry AI integrated with a high-throughput laboratory for autonomous research—and gave it an open-ended goal: to improve one of several important reaction classes. The system generated research proposals, designed and ran experiments, analyzed experimental data, and proposed follow-up experiments. Humans remained in the loop by designing steering and grading prompts and selecting proposals to test. They also made limited corrections to experimental plans, assisted with basic laboratory operations, and independently validated the final result.

The most promising proposal, OAI-M1-03, focused on a difficult but useful version of Chan-Lam coupling, a reaction chemists use to form carbon-nitrogen bonds. Starting from the open-ended goal of improving Chan-Lam coupling for process chemistry, GPT-5.4 independently identified primary sulfonamides as a challenging, high-value substrate class and suggested that mild oxidants, including TEMPO, could improve the reaction.

Across two cycles of experimentation in Maria Lab that idea produced a significant improvement. Under the optimized conditions, measured yields improved for 88% of the boronic acids and 83% of the sulfonamides tested. The mean yield rose from 16.6% to 25.2%, and the share of reactions above 30% yield increased from 15.6% to 37.5%. Human chemists then repeated representative reactions at bench scale. Those experiments confirmed the microliter-scale results, showing higher yields for 11 of 14 substrate pairs, with a more than twofold increase in most cases.

## Why the chemistry problem matters

Organic chemistry underpins all small-molecule medicines, as well as products in agriculture, electronics, and materials science. A reaction is especially useful when it can make the same kind of chemical bond reliably across many different starting materials. When reactions produce low yields or too many unwanted byproducts, chemists may have to abandon otherwise promising molecules or spend significant time developing a different route. This makes synthesis a major bottleneck in drug discovery: scientists can generally only test the molecules they can make or otherwise obtain.

Chan-Lam coupling is useful in medicinal chemistry because it forms carbon-nitrogen bonds, which are common in medicines. However, the reaction does not work equally well for every class of molecule. In particular, coupling primary sulfonamides with boronic acids has historically produced low yields. Sulfonamides are an important family of molecules found in medicines used in oncology and infectious disease.

## Connecting GPT-5.4 to Maria AI and Lab

The combined system paired complementary capabilities. Prompts written by scientists working with Maria AI were used with GPT-5.4 within a harness to generate and rank thousands of possible research proposals. Human chemists reviewed the small subset of proposals that ranked highest according to the system and selected four for laboratory testing. Maria AI then translated selected high-level plans into detailed lab instructions, ran thousands of high-throughput experiments, analyzed the raw data, and returned structured results to GPT-5.4.

One of the four selected proposals, OAI-M1-03, suggested using mild oxidants such as TEMPO to improve the performance of the Chan-Lam reaction for sulfonamide synthesis. Chemists found the suggestion both surprising and interesting.

The full process took three months, from the first prompt on March 4th to sharing the OAI-M1-03 results with independent experts on June 4th.

We describe this workflow as near-autonomous, not fully autonomous, because human chemists still made important decisions throughout the process. The model proposed the key research ideas, while human chemists provided high-level steering and judgment, corrected experimental details, helped prepare lab consumables and reagents, and repeated key experiments by hand.

## What we found

OAI-M1-03 identified TEMPO as a useful additive for the primary sulfonamide Chan-Lam coupling studied here. Under the optimized conditions, the reaction improved in two ways: average yield went up, and more substrate combinations reached practically useful yields.

Across two cycles, Maria ran a total of 10,080 reactions – more than a chemist running three reactions every day would run in a decade. That scale mattered because chemistry results can be misleading when they are tested on only a few examples.

After analyzing the first round of data, the system proposed a more focused second round of experiments to test follow-up hypotheses. One useful follow-up finding was that TEMPO could be replaced by a much cheaper analog, 4-hydroxy-TEMPO, with little loss in performance.

The result also held up beyond Maria Lab's microliter-scale screening format. Human chemists reproduced representative reactions manually at bench scale and observed an increase in yield for 11 of 14 substrate pairs; for eight pairs the increase was greater than twofold.

Four external chemistry experts reviewed the preprint describing OAI-M1-03. Their assessments supported our view that the result was novel and worth sharing with the scientific community.

"The merger of high throughput experimentation and modern AI represents a new frontier of scientific discovery. This new reaction is a powerful demonstration, where exceptionally mild conditions and a practical oxidant enable a nicely general substrate scope for one of the more popular reactions in drug synthesis." —Tim Cernak, Associate Professor of Medicinal Chemistry, University of Michigan

Of the other three proposals generated by GPT-5.4 and tested by Maria during the three-month period, OAI-M1-02 and OAI-M1-04 were experimentally proven in the Maria Lab, while OAI-M1-01 was disproven.

## Limitations

This work shows that a model can make a useful contribution in organic chemistry. It did more than summarize the literature or suggest a one-off experiment: it proposed a specific surprising hypothesis and surfaced it for human review, designed experiments, interpreted experimental data, and designed follow-up experiments.

It does not show that AI can independently run a chemistry research program from end to end. Human judgment remained essential, and the workflow depended on specialized high-throughput infrastructure. It also does not establish that the method will generalize to other coupling reactions, other substrate classes, or manufacturing conditions.

## Preparedness

Chemistry capabilities require careful treatment because the same tools that can support medicine and materials science could also be misused. We deliberately scoped this work to a legitimate medicinal-chemistry problem: improving a known coupling reaction used to make drug-like molecules. The experiments did not involve toxins, chemical weapons, or requests to design harmful compounds.
