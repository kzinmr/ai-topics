---
title: "Coplot: Supporting the research process through visualization"
source: "Cohere Blog"
url: "https://cohere.com/blog/coplot"
scraped: "2026-06-04T06:00:24.164936+00:00"
lastmod: "2026-06-03"
type: "sitemap"
---

# Coplot: Supporting the research process through visualization

**Source**: [https://cohere.com/blog/coplot](https://cohere.com/blog/coplot)

Research reaches its full impact when researchers can see what they're doing clearly, both for themselves as they work and for the people they share it with. Visualizations are key to that. They help researchers understand their own work along the way, what an experiment is actually showing, what to try next, what's holding up and what isn't. The visualizations that accompany a paper or blog post, ranging from diagrams to bar plots to tables to line plots, are the visible output of a much longer process of looking at data and figuring out what it means.
At Cohere Labs part of my role is to create these visualizations, both simple and complex, to support the team as we pursue our research questions. As I built more and more plots, it became clear that existing workflows made it difficult to iterate quickly while preserving reproducibility and fidelity to the underlying data. This is a real bottleneck to the research process. Matplotlib, used by many researchers, was hard to iterate with. Small changes often required full script reruns. Figma, a design tool, produced beautiful plots but couldn't reliably take in data, which meant manually tracing plots from Matplotlib which risked accuracy. Both paths slowed the work down and made it harder to fully utilize data visualization as part of the research process.
So I started experimenting. Initially my goal was to create a simple styling tool that produced code with styling rules that would work well in Matplotlib. But as I got deeper and deeper working alongside my teammates we realized we could build something even more helpful. We call it
co/plot
:
a tool we could prototype with quickly, with prebaked yet customizable styling, that stays accurate to the underlying data.
While building Tiny Aya, co/plot was thoroughly tested. During the model build I expanded its capabilities to account for the 70+ languages we were evaluating, and while creating the technical report I honed its styling to make our findings as clear and polished as possible. I was also handing off the tool to researchers along the way, refining the user experience to make it work better for them.
During this process, co/plot's impact on our workflow became clear. Better styled, more legible plots helped us make better decisions along the way. The plots weren't just helpful in the Technical Report. They were crucial for the process as well.
As steadfast believers in open science, we decided to release co/plot to the public. Releasing tools, in addition to papers and models, raises the baseline for how research gets done across the field. Independent researchers from our open science community are already using co/plot to work through their findings more clearly, which means they can iterate faster, get better feedback, and share their work with more confidence. To me, that's the point. When the floor of visualization tooling rises, more researchers can do clearer work and reach clearer conclusions, and good ideas can surface from places we wouldn't have thought to look.
The data visualization landscape is shifting quickly, and the tools researchers reach for shape how they engage with their data. The iterative work of making a plot, trying a representation and seeing what it shows you, is part of how researchers come to understand their findings. co/plot was built with that belief in mind: that the process of making the plot matters as much as the plot itself, and that tools for research should support that process rather than abstract it away. We're looking forward to continuing to develop co/plot, releasing more of the tools that have shaped our own research process, and hearing from the community about what would make these tools work better for them.
Blog
Written By
Thomas Euyang
Research Visual Storyteller
Tags
Open Science
Research
Share
AI isn’t a shortcut.
It’s how business gets ahead.
Contact sales
