# An Opinionated Guide to ML Research
**Author**: John Schulman
**Date**: 2020-01-24 (originally written December 2017)
**URL**: http://joschu.net/blog/opinionated-guide-ml-research.html

---

I originally wrote this guide in back in December 2017 for the OpenAI Fellows program

In this essay, I provide some advice to up-and-coming researchers in machine learning (ML), based on my experience doing research and advising others. The advice covers how to choose problems and organize your time. I also recommend the following prior essays on similar topics:

- You and Your Research by Richard Hamming
- Principles of Effective Research by Michael Nielsen

My essay will cover similar ground, but it's more tuned to the peculiar features of ML.

The keys to success are working on the right problems, making continual progress on them, and achieving continual personal growth. This essay is comprised of three sections, each covering one of these topics.

## Choosing Problems

### Honing Your Taste

Your ability to choose the right problems to work on is even more important than your raw technical skill. This taste in problems is something you'll develop over time by watching which ideas prosper and which ones are forgotten. You'll see which ones serve as building blocks for new ideas and results, and which ones are ignored because they are too complicated or too fragile, or because the incremental improvement is too small.

Ways to speed up developing good taste:

1. Read a lot of papers, and assess them critically. Discuss with others who have deeper knowledge.
2. Work in a research group with other people working on similar topics.
3. Seek advice from experienced researchers on what to work on. Ideas are cheap; your skill comes in choosing and executing.
4. Spend time reflecting on what research is useful and fruitful.

The biggest bursts of impactful work tend to be tightly clustered in a small number of research groups and institutions—not because these people are dramatically smarter, but because they have a higher density of expertise and perspective.

### Idea-Driven vs Goal-Driven Research

Two approaches to deciding what to work on:

**Idea-driven**: Follow the literature. See how to do X better. Embark on a project to test your idea.

**Goal-driven**: Develop a vision of new AI capabilities you'd like to achieve, and solve problems that bring you closer to that goal. Test existing methods, then develop your own improvements.

Goal-driven research has several advantages:
- Differentiated perspective from the rest of the community
- Leads to questions no one else is asking
- More motivating—you can imagine achieving your goal
- Enables team collaboration on different aspects of the problem

### Case Study: Graduate School Work

First half of PhD: enable robots to manipulate deformable objects. Developed approach based on learning from human demonstrations. Unexpected subproblems arose—trajectory optimization work became most influential.

Second half: reinforcement learning for robotic locomotion. Goal: get a 3D robot to learn to run from scratch. Focused on policy gradient methods → developed TRPO and GAE → achieved 3D humanoid locomotion.

When DeepMind presented DQN on Atari, many jumped on the Q-learning bandwagon. Schulman had already explored Q-learning and concluded it wasn't good for locomotion, so he continued with policy gradient methods → TRPO, GAE, and later PPO. Choosing a different problem led to exploring different ideas.

### Restrict Yourself to General Solutions

Pitfall of goal-driven research: taking your goal too literally. Constrain your search to solutions that seem general and applicable to other problems. When working on locomotion, Schulman avoided domain-specific solutions—the goal was to achieve locomotion "in a way that was general and could be applied to other problems."

### Aim High, and Climb Incrementally

Ask yourself: how large is the potential upside? Will this be a 10% improvement or a 10X improvement?

Incremental work is most useful in the context of a larger goal. The AlexNet paper (Krizhevsky, Sutskever, Hinton, 2012) contained no radically new components—just a large number of small improvements stacked to achieve unprecedented results.

If working on incremental ideas, their usefulness depends on complexity. A method that slightly improves the baseline better be very simple—otherwise no one will use it.

## Making Continual Progress

### Keep a Notebook, and Review It

Strongly recommended: keep a notebook recording daily ideas and experiments.

Daily entries: what you're doing, ideas, experimental results (paste in plots and tables).

Every 1-2 weeks: review all daily entries, condense into sections:
- Experimental findings
- Insights (from you, colleagues, reading)
- Code progress
- Next steps / future work

Value of the notebook:
1. Write down ideas as soon as you have them—revisit later
2. Keep experimental results in a unified place
3. Monitor your use of time—identify if you've been jumping between ideas too much

### When to Switch Problems

Switching problems too frequently (giving up on promising ideas) is a more common failure mode than not switching enough.

Rule of thumb: when looking back at months of work, you should find lots of small dead ends, but the majority of time directed toward projects that yielded a deliverable (paper, blog post). If substantial fraction was spent on half-finished projects abandoned for newer ideas—make a stronger effort towards consistency and follow-through.

Strategy: devote fixed time budget to trying new ideas (e.g., one day per week on something different)—epsilon-greedy exploration.

## Personal Development

Allocate some fraction of time towards improving general knowledge of ML as opposed to working on current projects. Without this, knowledge will plateau.

Main ways to build knowledge:
- Read textbooks, theses, and papers
- Reimplement algorithms from these sources

Early career: split time about evenly between textbooks and papers.

Textbooks: much denser way to absorb knowledge than papers. Each conference paper typically contains one main new idea with a too-concise background section. Good textbooks collect decades of ideas in proper order with consistent notation.

Recommended: Numerical Optimization (Nocedal & Wright), Elements of Information Theory (Cover & Thomas).

PhD theses: benefit most from (1) introductory/background material and (3) conclusion/outlook—unifying views written by experts.

Reimplementing papers: much deeper understanding than passive reading. Quick feedback by reproducing known results. Once you can easily reproduce SOTA, you'll be ready to go beyond it.

Keep track of incoming papers with a critical eye—notice trends, build up taste by observing the dependency graph of ideas.

Go forth and do great research!
