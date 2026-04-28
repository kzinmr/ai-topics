---
title: "AI is not another abstraction because god plays dice"
url: "https://rakhim.exotext.com/ai_is_not_another_abstraction_because_god_plays_dice"
fetched_at: 2026-04-28T07:02:00.243213+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# AI is not another abstraction because god plays dice

Source: https://rakhim.exotext.com/ai_is_not_another_abstraction_because_god_plays_dice

Some folks have gone all-in on AI-assisted coding. I've seen some tweets (not sure if sarcastic or real, to be honest) expressing disgust about the prospects of ever writing code by hand anymore.
The common argument I hear is that this is just another step in the long history of programming breakthroughs. We moved from machine code to assembly, from assembly to C, and from C to high-level languages like Python. Each step was a new layer of abstraction, hiding the messy details of the underlying hardware and software. Some even compare AI to a compiler. The AI prompt, in this view, is simply the next abstraction layer on top of "raw" code.
But this analogy is flawed. AI is not another abstraction layer, and the comparison to a compiler is misleading. Abstractions in programming are
deterministic
. A compiler can be very complex, but it is fundamentally a deterministic machine. Given the same input, it will always produce the same output. It is a tool that we can understand, predict, and, most importantly, trust.
AI, in its current form, is not deterministic. It is a probabilistic system. It is not a compiler, it's a contractor.
When you send an email to a contractor, you are describing what you want with a relatively high-level specification. The contractor then uses their own knowledge and experience to produce the result. What you get back depends on how well you described your needs, and how well the contractor understood them.
This is a perfectly valid way to work. But we should not lie to ourselves and call it an abstraction in the same way that a programming language is an abstraction. It is a delegation of a task to a non-deterministic agent.
There's a reason we distinguish between programmers and managers
; if "AI is just another abstraction", then a manager is just another programmer operating on a level above code. I mean, sure, we can say that, but words become kind of meaningless at this point.
This distinction matters. When we use an abstraction, we are still in control. We can always step into lower layers and do things "by hand" while maintaining the deterministic high-to-low generation loop; e.g. when writing C, we can do inline assembly, or when writing Python we can utilize C-bindings, or we can extend and modify the compiler stack like LLVM. The entire flow from high-level DSL to CPU register manipulations is determenistic and can in principle be done on paper. While LLM computations can also technically be done on paper (just a few matrix multiplications, right?), you will have to generate random numbers in order to perform the computation (like, play dice).
P.S. Some people call my recent blog posts "anti-AI" or whatever. Feels like any critique of AI will attract at least a few maximalists, which happens in all high-hype technology fields. I appreciate the progress in AI/LLMs, and use various AI tools daily. I also believe in having a healthy conversation about it rather than YOLO-ing into the future.
