---
title: "GPT-6 Models Demonstrate Intrinsic Protein-Design Capabilities"
created: 2026-11-25
updated: 2026-11-25
type: article
source: "https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/"
status: complete
sources:
  - "https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/"
  - "https://news.ycombinator.com/item?id=50634658"
sha256: bebeda32300f3bdbbe399bf9bbd54657dc824c47d95d04fdc79bc7c162eff729
---

# GPT-6 Models Demonstrate Intrinsic Protein-Design Capabilities

Source: https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/

## Article

GPT-6 models demonstrate intrinsic protein-design capabilities | OpenAI 

 OpenAI November 24, 2026
 Science Publication 
 GPT‑6 models demonstrate intrinsic protein-design capabilities

 Read the paper (opens in a new window) 

 Share 

 Key findings: 

 Our GPT‑6 family of models can design new protein shapes and the sequence of their chemical building blocks using only reasoning and code, without calling specialized biology models to generate those designs. 

 An internal research model matched or outperformed specialized models on many protein design tasks. Researchers could also guide designs by prompting the model on where a protein should attach and what shape it should take. 

 In lab tests with Onava, proteins based on GPT‑6.2’s designs showed evidence of binding, or attachment, across five targets. Redesigned antibodies also retained binding. Specialized models helped supply sequences and select candidates for testing. 

 The models’ written reasoning and code suggest they draw on math, physics, chemistry, and biological knowledge to reason about protein shapes and interactions with other molecules. 

 In a preprint titled GPT‑6 as a Universal Foundation Model for Protein Biology: Beyond Specialized Models , we show that our GPT‑6 family of models has intrinsic capabilities for designing new proteins: the models can design new protein structures and sequences without relying on specialized biology models, using only reasoning and general-purpose coding tools. 

 Proteins do much of the work in living cells. They drive the chemical reactions that sustain life, carry oxygen through the blood, and defend the body against infection. Incorrectly shaped proteins can also cause disease and dysfunction. Proteins are made from chains of chemical building blocks called amino acids. The order, or sequence, of these amino acids helps determine how a protein folds into a three-dimensional shape, which in turn influences what it does. 

 Scientists often start with a clear idea of what they want a protein to do. They might want it to block a signal that helps cancer cells evade the immune system or to help capture carbon dioxide from the air. The challenge is to work out what three-dimensional structure would enable the protein to do its job and which amino acid sequence would give it that structure. Specialized biology models capable of generating three-dimensional protein structures and sequences have made this work more practical. 

 Using and coordinating these specialized models requires substantial expertise. Each accepts particular kinds of inputs and constraints, and these models cannot easily accept new kinds of information without changes to their software or additional training. In contrast, a general-purpose model capable of performing the work of multiple specialized models can easily adapt to new instructions and requirements. 

 Our research illustrates the potential power of pairing natural language with intrinsic protein capabilities. We could guide our models at scales ranging from a single bond between two atoms to the overall shape of a protein. For example, we asked GPT‑6.2 to predict where and how a small molecule would bind to a protein. When we already knew which two atoms formed a bond, we could give the model that information and ask how the rest of the molecule would fit. We could switch between these tasks simply by changing the prompt, without retraining the model. We also asked our models to design small proteins called minibinders and marked where each should attach to its target, and further specified how many coils or strands each minibinder should contain. An internal model followed that instruction with near-perfect fidelity in its three-dimensional designs. 

 Points farther from the center indicate better performance. Newer generations of models improved on many of the 14 protein tasks tested. 

 A closer look at our models’ protein designs 

 We ran computational tests of whether the GPT‑6 models series could design small proteins to bind given targets, build proteins around specified structural features, predict protein structures and molecular interactions, and rank how sequence changes affect properties such as stability and binding. Our latest models performed comparably to or better than specialized models on most tasks, although predicting a complete protein structure remained a clear weakness. 

 The models’ written reasoning and code offer clues to how they approach these tasks. They draw on mathematics, physics, chemistry, and coding alongside knowledge of recurring patterns in protein sequences and structures. For example, when designing a small protein intended to bind to IL-7Rα, the model proposed how the two proteins might interact, then wrote and executed code to explore different protein shapes and amino acid choices that could support that interaction. 

 The model’s written reasoning and code show it drawing on math, physics, chemistry and biology to design a protein intended to attach to IL-7Rα. It examines the target’s surface, arranges five coiled sections into a protein shape, and checks how the two proteins could fit together. 

 With our research partner, Onava ⁠ (opens in a new window) , we also tested the models’ structure and sequence designs in the lab. First, Onava made small proteins based on three-dimensional structures designed by a pre-released version of GPT‑6.2. Specialized models supplied amino acid sequences and helped select candidates for testing. For each of the five targets we chose, at least one protein showed evidence of binding in the lab. In separate experiments, GPT‑6.2 designed new amino acid sequences for existing minibinders and antibodies. Following candidate selection with specialized models, many of the redesigned proteins also showed evidence of binding to the same targets as the originals. 

 Laboratory Experiment 1: Designing small proteins that bind to a target 

 Our first laboratory experiment tested whether GPT‑6.2 could design small proteins that would bind to their intended targets. We compared computational measurements of quality against RFdiffusion, a specialized model for protein design, and found that GPT‑6.2’s three-dimensional designs scored slightly lower while our latest internal models scored higher. For the lab experiment, we made proteins based on GPT‑6.2’s designs and measured how strongly they bound to their targets. 

 We gave GPT‑6.2 the three-dimensional structures of five target proteins and marked where we wanted a minibinder to attach. It then wrote code to create three-dimensional designs for potential minibinders, without using specialized protein AI models. 

 To turn GPT‑6.2’s three-dimensional designs into proteins we could test in the lab, we needed amino acid sequences that would fold into the proposed structures. We used a specialized AI model called SolubleMPNN to suggest sequences for each design. Other specialized protein models helped us select candidates predicted to fold as designed and bind at the intended site on the target. 

 GPT‑6.2 designed shapes for small proteins intended to attach to chosen targets. Specialized models then proposed amino acid sequences—the order of the proteins’ chemical building blocks—and helped select designs for our research partner Onava to make and test in the lab. 

 We tested 322 minibinders against 5 targets in the lab. Of those, 35 (10.9%) tested positive for binding to their intended target. We found 5 hits for PD-L1 (a protein some cancers use to evade the immune system), 3 for IL-7Rα, 1 for TrkA, 8 for VEGF-A and 18 for IL-17A. The original RFdiffusion study ⁠ (opens in a new window) reported higher hit rates, but rates depend heavily on how strictly researchers filter designs before lab validation and their definition of binding. Nevertheless, our results provide early evidence that we can turn GPT‑6.2’s three-dimensional designs into proteins that bind to their intended targets in the lab. 

 An internal research model designed shapes for small proteins intended to attach to the target proteins shown in gray. The colored shapes compare each design with a computational prediction of how the protein would fold and fit against its target. 

 Laboratory Experiment 2: Designing new sequences for 3D protein structures 

 We tested whether GPT‑6.2 could design the sequences itself. We gave it three-dimensional models of how existing minibinders fit against their targets, withheld the original amino acid sequences, and asked it to propose new ones. Specialized models helped us choose which proteins to make and test in the lab. 

 For three targets, we started with computationally predicted structures of confirmed minibinders whose sequences Onava had collected from earlier studies. In our initial lab screens, we saw binding in 75 of 88 designs for MDM2 (85%), 26 of 42 for VEGF-A (62%), and 8 of 59 for PD-1 (14%). The amino acid sequences proposed by GPT‑6.2 also often differed significantly from the original minibinder sequences, with a median of 50% for VEGF-A, 43% for MDM2, and 15% for PD-1. 

 We also asked GPT‑6.2 to design new sequences for three unpublished minibinder shapes it had generated earlier: two targeting PD-L1 and one targeting IL-7Rα. A specialized model, ProteinMPNN, had already supplied one sequence for each shape, and proteins made from those sequences had shown binding in the lab. Of the 107 proteins made from GPT‑6.2’s new sequences, 14 (13.1%) showed binding. 

 Given an unpublished structure, GPT‑6.2 had come up with two substantially different sequences that both showed signs of binding to the same target. For the same PD-L1 minibinder structure, GPT‑6.2 designed two sequences different from the original in 52 and 58 out of 90 total amino acids. The two also differed from each other at 44 positions, nearly half the sequence. 

 The unpublished structures and substantial differences in sequence give us strong evidence that GPT‑6.2’s capabilities extend beyond memorization. The results also suggest we could use GPT‑6.2 to intrinsically design both a minibinder’s structure and its sequence. 

 Redesigning the parts of an antibody that bind to a target 

 Researchers often redesign an antibody’s binding loops to help it grip its target more tightly, a process called affinity maturation . They may also want it to bind more selectively, so it’s less likely to attach to similar proteins. We tested a first step toward those goals by asking our models to design new loop sequences that preserved binding to the original target. 

 We started with six small antibodies (VHHs) that bind to the same protein, IL-4Rα. For each antibody, we gave GPT‑6.2 its predicted three-dimensional structure and most of its amino acid sequence, leaving out the three loops that help the antibody grip its target. We asked the model to design new sequences for them. Of the 182 designs we tested, 128 (70%) showed signs of binding to IL-4Rα. 

 We then tested how precisely we could guide the model’s changes to existing therapeutic antibodies. This time, we gave the model the original sequences and asked it to change about half the amino acids in each of three binding loops while keeping the rest of the sequence intact. We tested the redesigned portions of the antibodies as fragments in the lab. Of 272 fragments based on five therapeutic antibodies, 179 (66%) showed binding to the original target, PD-1 or PD-L1. 

 What else can our models design and predict? 

 Precise control over minibinder structures for programmable structure design

 A long-term goal of programmable structure-based design is to let researchers specify structural constraints in natural language. In our computational evaluations, our models consistently designed minibinders that contacted the required locations on the target. We could also specify the minibinder’s structural class (all helices, all strands, or a combination) and control the number of coils and strands with near-perfect fidelity. The same approach lets us express more detailed requirements for the binding interface, such as which target amino acids should be buried upon binding or whether the minibinder and target should interact through specific interactions such as “β-sheet–β-sheet”. As our model’s reasoning capabilities improve, we envision researchers guiding protein structure generation much as they guide image generation today, by describing the features they want. 

 Our model was asked to design small proteins with specified shapes: mainly coils (orange), mainly strands (blue), or a mix. Some instructions also specified how many coils or strands to include. The designs are intended to attach to PD-L1 or PD-1, shown in gray. 

 Building a protein around a specified structural feature

 Most enzymes are proteins that speed up chemical reactions. When designing a new enzyme, researchers may know how a few key amino acids need to be arranged at the site where the reaction happens. Those amino acids can lie far apart along the protein chain. The challenge is to design the rest of the protein so that, as the chain folds, it brings them together and holds them in place. 

 We tested our models on 30 challenges from MotifBench ⁠ (opens in a new window) , including examples drawn from enzymes and from sites where proteins bind to one another. We gave the models a specific three-dimensional arrangement of amino acids, called a motif , and asked them to use coding tools to design the rest of the protein around it. This task is called motif scaffolding . 

 For each design, we used ProteinMPNN to propose eight possible amino acid sequences, and ESMFold ⁠ (opens in a new window) to predict how each would fold. We counted the design as a success if at least one predicted structure both preserved the motif and closely matched the overall structure the model had designed. 

 In a preliminary analysis, 43.7% of the designs we evaluated from our latest internal model met both criteria, compared with 27.8% for RFdiffusion. While laboratory experiments are needed to find out whether these proteins could carry out the intended function, such as speeding up a particular reaction, this provides strong computational evidence of our models’ intrinsic protein capabilities. 

 An internal research model designed protein structures around a small region whose shape had to stay fixed, shown in gold. The colored shapes compare the model’s designs with computer predictions of how the proteins would fold. Panels showing only gold had no design that passed the computer checks. 

 Designing a protein with a specified fold

 In motif scaffolding, we specified how a few amino acids should sit relative to one another. We then determined whether we could also guide the design of an entire protein by specifying its overall fold. We gave our models a chain length and a code from CATH ⁠ (opens in a new window) , a system scientists use to classify protein structures. The models then had to work out where each amino acid should go in three-dimensional space. 

 Many designs captured the broad layout we asked for. The harder part was getting the chain to follow the right path through it. Two proteins can have several coiled stretches packed together in a similar bundle, for example, yet differ in the order in which the chain connects them. 

 We counted a design as a success if at least one amino acid sequence was predicted to adopt the requested fold and closely match the model’s three-dimensional design. Across 200 challenges, 18.9% of the designs we evaluated from our latest internal model passed, compared with 17.1% for Proteina, a specialized protein design model. 

 An internal research model was asked to design proteins with specified overall shapes, such as bundles of coils or layers of strands. The colored shapes compare selected designs with computer predictions of how they would fold, showing examples where the two closely match. 

 Predicting how chemicals and proteins fit together

 Many medicines, including aspirin, are small molecules , chemical compounds much smaller than the proteins they act on. Predicting where a small molecule binds to a protein and how it fits there is called docking . These predictions can help researchers decide how to modify a drug candidate so it binds more tightly to its target. To test our models, we started with experimentally determined structures of small molecules bound to proteins. We digitally removed each small molecule and gave the models the protein structure along with a text description of how the molecule’s atoms were connected (a sequence of characters called SMILES). We then asked the models to predict where the molecule had been bound and how it was oriented. 

 For our first docking test, we used the PoseBusters dataset ⁠ (opens in a new window) , a collection of three-dimensional structures that show how small molecules bind to proteins. Researchers determined these structures experimentally, giving us a way to check the models’ predictions. Without being told where on the protein each molecule had bound, the models had to predict both where the molecule fit and which way it faced. GPT‑6.2 closely matched the molecule’s observed position and orientation in 93% of scored predictions, compared with 96% for our latest internal model and 50% for DiffDock-L, a specialized docking model. 

 In practice, researchers may already know something about how a molecule binds. One major advantage of a GPT model is that we can give additional information directly in the prompt . We tested this on 179 structures from the Scarpino dataset ⁠ (opens in a new window) , where each protein structure forms a chemical bond with a small molecule, tethering the two together. We told our models which two atoms formed the bond and asked them to predict how the rest of the molecule fit against the protein. GPT‑6.2 closely matched the experimental structure in 92% of scored predictions ⁠ (opens in a new window) , and our latest internal model did so in 97%, while DiffDock ⁠ (opens in a new window) reached 60%. 

 An internal research model predicted where and how small molecules would fit against proteins, shown in gray. Purple shows the model’s predictions, and teal shows the molecules’ positions determined in earlier experiments. In these examples, the predictions closely match the experimental structures. 

 Predicting how antibodies bind to proteins

 Where an antibody binds can help explain whether it blocks another protein from attaching to the same site. We tested how accurately successive generations of GPT could predict where an antibody binds and which way it faces. For hundreds of pairs of antibodies and targets, we showed the models the two proteins separately and hid some of the atomic detail (all side chains) on their surfaces. 

 With the side-chain details hidden, the mean DockQ score (a commonly used metric in which higher values indicate a closer match to the experimentally observed arrangement) increased from approximately 0.05 for GPT‑5.6 to 0.28 for GPT‑6, 0.57 for GPT‑6.2, and 0.81 for our latest internal model, at each model’s highest evaluated compute setting. 

 Because these structures were public, the models may have seen the same antibody-target pairs or similar ones during training. Even so, each generation of our models predicted more accurately how the two proteins fit together, even with all side-chain positions hidden. That progress gives us reason to be optimistic about harder docking problems. 

 Each row compares four models’ predictions of how an antibody attaches to its target protein. Colored shapes show the model’s prediction; dark gray shows the position observed in experiments. Results improved with each successive generation of model. 

 Predicting the effects of mutations

 We can design far more proteins on a computer than we can make and test in the lab. Even after we settle on a promising structure, we may have many amino acid sequences to choose from. We tested whether our models could help researchers decide which versions to make first by predicting how changes to a protein’s sequence would affect its stability, activity, or ability to bind to a target. 

 We drew on four public datasets from experiments in which scientists had replaced one or more amino acids in a protein and measured the effects. For each test, we gave our models the sequence of the protein the scientists started with and the sequences of 50 modified versions. We told the models what the scientists had measured, withheld the results, and asked them to rank the 50 versions without using coding tools, by reasoning only. 

 In one study of protein stability, we asked the models to rank 50 versions of a protein by how likely each was to be folded at room temperature. We compared the predicted order with the order observed in the lab using a measure called rank correlation . A value of 1 means the rankings match perfectly, 0 means there’s no consistent relationship, and −1 means the order is exactly reversed. Across 265 sets from the stability study, each model generation improved, from 0.41 for GPT‑5.6 to 0.52 for GPT‑6, 0.57 for GPT‑6.2, and 0.66 for our latest internal model. 

 In each of the four datasets, GPT‑6.2 and our latest internal model produced more accurate rankings on average than ESM2-650M, a specialized protein model. 

 Early signals from our model’s protein structure predictions

 Earlier, we relied on specialized models to predict whether an amino acid sequence would fold into the structure our models had designed. We wanted to see how close our models are to making that prediction themselves. We gave our models the amino acid sequences of proteins with known three-dimensional structures. Using only basic coding tools, the models predicted how each chain would fold in three dimensions. We evaluated their predictions using a measure called TM-score . A score of 1 means a perfect match to the real structure, and scores above 0.5 generally indicate that the prediction captures the overall fold. 

 The biggest gains are visible in individual examples. For some proteins, our latest internal model closely reproduced folds that earlier models missed. Across the full test, the average score rose from 0.16 for GPT‑5.6 to 0.26 for GPT‑6.2 and 0.38 for our latest internal model. The specialized model ESMFold2 averaged 0.93, so there’s still a substantial gap in how reliably our models can predict a whole protein’s structure from its sequence alone. 

 What if researchers already know most of the structure and want to fill in a missing piece? We tested this on 100 antibody fragments. For each one, we gave our models the amino acid sequences and the surrounding three-dimension structure, hiding the six loops that help the antibody recognize its target. Our latest internal model often predicted both the shape and position of those loops quite accurately. ESMFold2 was still more accurate overall, even working from the sequences alone. 

 Each model was given the same protein sequence—the order of its chemical building blocks—and asked to predict its 3D shape. The colored shapes show the predictions, and dark gray shows the structure measured in experiments. 

 Each model was given a partial structure and tasked with predicting the missing regions corresponding to the antibody CDRs. The colored regions show predictions from the internal model and ESMFold2 compared with the experimentally determined structures. 

 Limitations 

 It is important to note that our protein design campaign relied on specialized structure prediction models such as Boltz-2, OpenDDE, and ESMFold2 to filter candidates. Our results show that GPT models have intrinsic capabilities comparable to specialized models at two stages of the workflow: backbone generation, where researchers commonly use RFdiffusion; and sequence redesign, where they commonly use ProteinMPNN. Our results therefore do not yet establish that our models can generate de novo minibinders end-to-end in a zero-shot setting without help from specialized models. 

 Our work demonstrates yet again the jagged capability frontier. Predicting a complete protein structure from its amino acid sequence remains substantially harder for our models than several of the component tasks above. On that task, even our best internal models remained well behind specialized structure-prediction models. 

 Some benchmark results also require careful interpretation. In tests that asked models to infer amino acid sequences from protein structures, unusually high accuracy may partly reflect memorization or patterns left by the process used to generate those structures. Those results alone do not establish reliable performance on unfamiliar proteins. 

 The laboratory results provide a more direct test of whether proposed designs can work, but binding is only one step toward a useful research tool or medicine. Further work would need to establish properties such as specificity, stability, and biological activity, along with safety and efficacy for therapeutic applications. 

 What’s next 

 This work is an early step toward programmable molecular design at OpenAI. Our goal is to let scientists describe what they want a molecule to do in plain language and use our models to help design candidates to test in the lab. To make that approach useful for developing medicines, we want to make progress in three areas. 

 Find minibinders for harder targets. We want to design molecules that bind to targets where our attempts so far have fallen short. 

 Design for what happens after binding. We want to test whether the molecules we design can produce a specific biological effect, such as killing a cancer cell. We also want to design molecules that bind selectively to their intended targets and are practical to manufacture. 

 Design a wider range of molecules. Our lab experiments focused on small protein minibinders and antibody fragments. We’d like to extend that work to molecules that bind to several targets at once, RNA, and small molecules, including a class called PROTACs that direct a cell to break down a particular protein. 

 As we work to accelerate scientific progress safely and responsibly, we also seek to evaluate and reduce risks, particularly those related to biosecurity. The same capabilities that help scientists design proteins for new medicines could also be misused. Our Preparedness Framework ⁠ guides how we assess these risks and test safeguards to reduce them. 

 While lab testing remains a critical part of protein design, our goal is to provide powerful models that can shorten each round of design by giving scientists more control and flexibility, and reduce the total number of design-test cycles needed to find a functional protein. Ultimately, we envision enabling scientists to design proteins and molecules simply by prompting our models in natural language, massively accelerating the development of new biotechnologies and new medicines. 

 2026 
 
 Author
 OpenAI

 Keep reading

 View all 

 Searching for distant planets with Astra
 Science Nov 24, 2026 

 MedChemBench: Benchmarking AI for medicinal chemistry
 Research Nov 20, 2026 

 Research acceleration: The jagged frontier
 Research Nov 18, 2026

## HN discussion highlights (item 50634658)

# HN gpt6-protein — GPT-6 models demonstrate intrinsic protein-design capabilities (284 pts, item 50634658)
# url: https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/

[abound]   > In lab tests with Onava, proteins based on GPT‑6.2’s designs showed evidence of binding, or attachment, across five targets.
[brandonb]   They did actual wet lab tests in this experiment. Really impressive IMO. Anthropic also recently spun up a wet lab for what I'd presume is a similar vein of work.
[trilogic] Someone claims having a superior free open weights in biology: https://hugston.com/news/dangerous-enough I have tested the S2 and Chatgpt, both are good but GPT keeps flagging and is annoying. It shouyld be interesting to bench them agains eachother.
[trilogic]     Yes the weights came out in September, I doubt in 2 months they will be able to release un update, but there is nothing to be disappointed in free open weights beating frontier.
[gopalv] > We gave GPT‑6.2 the three-dimensional structures of five target proteins and marked where we wanted a minibinder to attach. It then wrote code to create three-dimensional designs for potential minibinders, without using specialized protein AI models. The ability to write code is basically the superpower for these models. As long as what you need to do to make progress is write better code, they will do better at the task. The last 30 years has been making more and more things run using code instead of any other mechanism (music, illustration, vfx). Even math, the models were worse off before
[diskzero]   > The last 30 years has been making more and more things run using code instead of any other mechanism (music, illustration, vfx). I agree with you, and am eager to hear some of the examples you have in mind. I have experience in all three; for example, our animation pipeline at PDI/Dreamworks was all code initially. Things became more complex when we started to introduce third-party tools like Maya, Houdini and others into it. Some functionality in the third-party tools was difficult to surface as "code" and this caused a lot of issues.
[tarnith]     I've recently seen some VFX artists porting Houdini particle sims and other motion graphics they write to WebGL2/WebGPU using LLMs. Coming full circle in a way. Node graphs that would be a pain to rewrite (not impossible, just not worth the time for a demo) are getting translated into web compatible shaders again.
[cyanydeez]   better is doing a lot of heavy lifting; what you are suggesting isn't the code, but the "better": being able to regurously define what is good and what is better is the super power. If you can construct the lego pieces and give it a picture, it can do the step by step more or less halfway between brute force and logical inference. but this only yields with non-confounding problems, such as protient folding. Nerds and investors are easily confusing one another with the class of problems yielding to AI readily.
[CSSer]   It makes me wonder what gains we could experience by producing an LLM optimized general-purpose programming language. Doing so would require creating a syntax that is expressive enough to be legible(-ish?) but with the express goal of maximizing contextualization. We could then extract every code example from the training data set, reimplement it all using using the new language, and finally re-train a new model using the produced training output.
[xarope]     I feel like it's the other way round; we see a lot of success with go(lang), so perhaps the language should be as simple as possible to avoid over-expressiveness so that us mere humans can still review the code. That would rule out languages where there are too many ways to get something done (perl, c, maybe even lisp since I can only handle so many brackets)?
[JoshTriplett]     > It makes me wonder what gains we could experience by producing an LLM optimized general-purpose programming language. We could gain even more slop that we have even less hope of successfully reviewing.
[jubilanti]   > > intrinsic > > It then wrote code > As long as what you need to do to make progress is write better code, they will do better at the task. That is not what "intrinsic" means to me. It didn't use a protein model, but it did use existing domain specific libraries.
[scotty79]     At this point it's irrelevant. Since agents can write their harnesses anything that agent can do in any harness, is its capability.
[ajasmin]     That's what I've been wondering about the recent security finds as well, how much of that is an LLM reviewing code directly vs. employing an agent to setup traditional fuzzing and static analysis tools.
[hgoel]     To be fair, a decent chunk of HN (and social media in general) ate up the "intrinsic weight editing" claim too despite it also just involving programmatic use of standard techniques that were definitely in the training corpus.
[aabhay]   Code is not a 1-dimensional skill. The models do extremely well at writing code that fits into a single file, roughly up to 5000 lines. Beyond that, even the best models have significant failure modes such as duplicate implementations, low code reuse, abstraction anti patterns (e.g. checking the db for the same consistency condition before, inside, and after a function), etc. And left to their own devices, the code they write might be utterly unreadable and unmaintainable. I’ve seen e.g. a model write a shell script that invokes python with bash vars that itself generates a kubernetes yaml con
