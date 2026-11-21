---
title: "Announcing DreamCoder (Mickey Petersen)"
source: https://www.masteringemacs.org/article/announcing-dreamcoder
date: 2026-11-21
type: article
sha256: dd7a72e86e6603392487ba0d33a2e3aac83678fcb89654995cbe74404e4bd994
---

> HN discussion: https://news.ycombinator.com/item?id=50581110 (229 pts)

Announcing DreamCoder - Mastering Emacs 

 Close 

 Try Mastering Emacs for free!

 Are you struggling with the
 basics? Have you mastered movement and editing yet? When you
 have read Mastering Emacs you will understand
 Emacs.

 Close menu 

 Mastering Emacs 
 About 
 Article Index 
 Reading Guide 
 My Emacs Packages 

 From the author of Mastering Emacs

 Announcing DreamCoder

 I talk about DreamCoder, a frontier coding harness and IDE I have been working on for quite a long time. I also talk about the history of AI, LISP and Emacs, and how it all fits together.

 Download  DreamCoder 
 Read on 

 By Mickey Petersen 
 20 November 2026 
 4 comments 

 It’s been a little bit quiet around these parts; sorry about that. I’ve been really busy for the past fifteen months with a major project that I am finally ready to formally release. So I’d like to talk about that project, and also a potted history of AI and Emacs.

 It’s called DreamCoder , an AI coding harness that is very different from the ones you’re probably familiar with already.

 I installed Claude Code a few days after its first release some time in May 2025. I put some coins in the slot machine and I put it to work building a complex piece of enterprise middleware I’d built several times in my career. Wow.. watching this thing chomp its way through the project with that chaotic, early Sonnet energy. It was far, far from perfect; it required a lot of human steering, input and correction, but the speed advantage was undeniable, and seeing it jump between disparate programming languages, frameworks and theoretical and practical programming from one turn to the next was just such a sight to behold.

 One thing that struck me with Claude Code is that it was the first terminal application I’d used in a long time. I found it an odd choice for a coding agent; then everyone else copied them and made their own terminal coding agents.

 Why on earth do I have to stare at a shoe rack-sized terminal window to do this? Sure there are GUI versions also; but the terminal interface remains the primary modality for most of these tools. Most GUIs, and most harnesses now have them also, are second-class citizens. And they all look the same. A boring sidebar with chat headings and a chat pane is what most of them look like.

 But a serious coder needs more than that. Even a casual user will bristle when they try to copy and paste multi-line text in a terminal.

 So in May 2025 I decreed that I would build a better harness, and surely now that I have AI this should not take more than 2 or 3 months to build.

 And so, after 15 months of work, and endless UI and backend iterations, culminating in a successful beta test, I am now ready to release DreamCoder, which is I think the acme of what a coding harness should be.

 DreamCoder is a frontier coding harness with a tiling window manager that runs in your browser on all 3 platforms. 
 
 Before I get into the meat and potatoes of all of that, I want to talk about AI history and Emacs’s role in it.

 Let’s roll back time to the 1950s.

 Past

 Emacs and LISP, if you did not know, both have a special place in the annals of AI history.

 John McCarthy was an AI researcher at MIT, and in the 1950s he set out to create the Advice Taker , a piece of software that envelops a framework for what a basic human should know that he called commonsense reasoning using “mathematical logic”. His postulation was that if we can express with symbolic precision all the aspects of what constitutes humanity like ordinary facts about life, that we can set in motion the rudiments of AI.

 In the 50s there was little in the way of computer software that could do this. To formalize such a system you need a lot of data, rigorously formatted, and a method of manipulating the data. The data and code itself may intertwine recursively , and so an ordinary programming language would not work.

 To help him achieve this, McCarthy created the LISt Processing (LISP) language made up of two facets: M-expressions, a functional language in the vein of Algol; and S-expressions, designed for symbolic data representation, and never intended as a method of writing code. S-expressions were dolled up with parentheses. M-expressions meanwhile used square brackets to visually separate the two. Uniquely, the language specification had an eval feature that would prove that the language is also a universal Turing machine… if only McCarthy had the means to do so. It was theoretical because McCarthy lacked, in time, staff and money, what he needed build this recursive evaluator that can take as input its own world state and evaluate it alongside new expressions, a fact made even more apparent by the sheer complexity of his M-expression language and the limited resources he had at the time.

 Steve Russell who worked with him proved him wrong the way most young people do: by just doing it. Russell wrote the first LISP Interpreter with a working eval function, but M-expressions got sidelined; the imperative, procedural nature of programming got squished into S-expressions instead. They had to hand roll the language on paper then punch it into cards and then batch run them. Eliding M-expressions was a simple matter of pragmatism. And so LISP was born. And through several accidents of history, M-expressions never gained traction. M-expressions live on in Wolfram’s Mathematica, but few other places.

 Much later, McCarthy eventually conceded that,

 “One can even conjecture that LISP owes its survival specifically to the fact that its programs are lists, which everyone, including me, has regarded as a disadvantage.”

 S-expressions were always intended as the storage format with a bridge language to manipulate them. But by pushing evaluation into the same symbolic representation format as the data, we have what we call LISP today. That is why LISP is so unique. Consider a simple calculator. (+ 2 2) can simultaneously represent an expression that we want to compute, two plus two , or perhaps a ledger of record of a calculation we have already done.

 McCarthy never built the Advice Taker in its purest form. He and his team ran into many philosophical, mathematical and computational walls that kept them occupied for a long time.

 The idea behind the Advice Taker was simple. If you want to go somewhere in your car, you can symbolically express this by building a chain of narrative facts – kinda like a flowchart, but as small snippets of rules and facts, not as one grand design.

 The system would automatically resolve ambiguities, and all the logician had to do was capture the microcosm of the world he wished to represent:

 (at me home)

(walkable home car)
(walkable home driveway)
(drivable car shop) 
 And so on. If you’re a student of Computer Science you’ll see echoes of Prolog here. The intent was simple: if we can symbolically express the world around us, we can advise that symbolic world with real-life facts, and have the automaton that uses this reified symbolic world change with it.

 But the axiomatic complexity of a world model would never survive an encounter with a 3-year-old child. Every axiom you write begets a new one — so you can walk to your front door? Well what if the door is locked? Or what if your car is parked on the street and not in your drive way?

 A rules-based order of the world is a tender, beautiful one; but it is hard to build. It’s a fractal of ever-more specific and pedantic rules that conspire against you, just as you think you have a soluble world, typed and ready.

 Anyone who has ever written Prolog knows exactly what that feels like!

 I have my own personal story to add to this. In the 90s as a teenager I got a summer internship at a business that built banking software. They clearly didn’t know what to do with us teenaged interns, so on our first day they crammed us in a room and split us into teams and told us to build a flow chart for assembling a bike. Team exercise or something. Best one wins. We were told to be as specific and explicit as possible and account for as many conditions as we could think of, and the poor employees who had to mind us did their best to help. I distinctly recall losing because in my flowchart I forgot to open the box the disassembled bike came in.

 McCarthy meanwhile eventually moved on and set up his own AI lab at Stanford, but the idea of the Advice Taker lived on.

 In the late 70s Stallman and Steele create EMACS (Editing MACroS), also at MIT’s AI Lab, a set of building blocks on top of TECO, a famously inscrutable text editor. TECO did not update the screen by default; you had to toggle that on and hope your edits worked. You typed out terse keyboard commands, crossed your fingers and hoped you got it right, and then you patiently waited for your text manipulation to take effect. Rinse and repeat until you got what you wanted.

 Stallman and Steele wanted more: they wanted macros so they could automate tedium of typing all that line noise. This strand of augmentation and later on self-modification is of course a unifying theme in Emacs today. The history of Emacs is long; but its outcome is known to us. I am typing this very article in Richard Stallman’s Emacs.

 McCarthy’s Advice Taker left its mark in a subtle but indelible way. Warren Teitelman built the ADVISE system in his thesis with a cool title that reads like something out of a pulpy 1970s sci-fi novella: PILOT: A Step Toward Man-Computer Symbiosis . Teitelman, he later said, was deeply inspired by McCarthy’s original idea of advising systems .

 In his thesis, he describes a method of arresting a function call and inserting code before or after it is run. He was tired of editing other people’s LISP code by hand, and wanted a way of modifying their code without touching it directly. He built and rebuilt his system several times over the years, culminating in his ADVISE system in Interlisp, a structured editor and language runtime for manipulating LISP code and data. Interlisp eschewed plain text files; instead, you manipulated the tree at a high level of abstraction with explicit instructions like “move X list to Y position”. You can see my own attempts at merging structured editing with plaintext editing in Combobulate .

 MIT AI hackers eventually implemented Teitelman’s ADVISE system from his PILOT thesis in their own versions of Emacs. Later, it was canonized in Chalupsky’s own 1992 re-implementation in Emacs Lisp that lives on ( M-x find-library advice.el ) as one of Emacs’s advice systems to this day.

 What began as an idea for expressing automata using symbolism in an as-yet theoretical language in the 1950s culminated in a system for dynamically altering functions in GNU Emacs in the 1990s. What an unlikely lineage and history.

 A cast-iron system made of stern rules cannot spawn general intelligence.

 Symbolism and AI did not end with advising functions. There were many attempts at symbolic intelligence. Terry Winograd’s SHRDLU ; Marvin Minsky’s Frame Systems ; and even Emacs’s ELIZA-style M-x doctor all make use of symbolic “AI”.

 None of them brought us closer to the AI that proponents of symbolic AI hoped they would.

 In hindsight that seems obvious.

 Writing a LISP macro just so will not produce artificial intelligence; nor will a carefully crafted web of rules and symbolic algebra suddenly spark intelligence. We know that today, but for a generation of computer scientists it felt like the future we have all read about in science fiction novels: a perfect, logical intelligence. A positronic brain . Robby the Robot; HAL 9000; C-3PO; Data; or the Speedies and Cuties from I, Robot. The unifying theme of these science fiction stories is they are automatons that follow strict rules — they obey Asimov’s three Laws of Robotics.

 Every turn of hardware and software brought them ever closer to one day realizing the vision of an artificial intelligence, captured in neat axioms and LISP S-expressions, and modified in tools like Emacs.

 It is surprising that symbolic AI, the vanguard movement for artificial intelligence, would instead dissipate into the wider body of Computer Science and programming as tools, languages and concepts, but not survive as a viable method of achieving AI.

 Perhaps we always knew. Because at some point – even if we never really fully internalized it – we discovered that a ductile system that is shaped by its master’s desires is a tool that survives the ages because it remains eternally useful.

 A cast-iron system made of stern rules cannot spawn general intelligence.

 For all the mathematical purity, beauty even, of the idea of a clockwork mind that is introspectable and malleable and its behavior expressed as S-expressions and interpreted by elegant algorithms and honed macros, we can, through the benefit of hindsight – now that we do have AI through other means – see that it was not to be.

 The argument in favor of ductility is especially poignant when you learn of the Connectionists , which sounds like a bad 1960s band, but was in fact a loose coalition of people who believed firmly that neural networks, not symbolic AI, were the path to success. The Connectionist viewpoint was deeply unpopular in AI academia of that era, and funding for it was scarce.

 Frank Rosenblatt invented the Perceptron, a foundational concept in neural networks, in 1957. Before Rosenblatt died in 1971, Marvin Minsky, an authority in the AI movement at MIT and a leading proponent of Symbolism, knifed the idea of Perceptrons and neural networks in a book he co-authored with Seymour Papert. They named the book, which they also dedicated to Rosenblatt, Perceptrons . The book deftly explains the mathematics of Perceptrons but undercuts their possible utility by showing that a single-layer Perceptron cannot represent an XOR gate. It was a deliberately obtuse reading of what neural networks could and could not do. With one additional hidden layer, a network can represent an XOR gate. It was a sneaky thrust of the stiletto: Minsky’s claims were overstated. A fact that was not lost on anybody in the Symbolic or Connectionist camps.

 It’s disputed if the Perceptrons book led to the first AI winter in the 1970s. It certainly did not help. But funding for many AI research paths dried up in the 1970s.

 The Connectionist movement was vindicated in the long run. They lost the battle then, but they won the war, and the fruits of their research eventually gave us AI.

 The ductility we so prize in our software and tools today is antithetical to a strict, symbolic world model spun of axioms and facts that we hoped would one day birth AI. Yet to try and give birth to this world they had to build the most ductile tools of them all: LISP and, from that, also software like Emacs. The ultimate hacker’s tool.

 It is ironic then that a neural network, a crude facsimile of how a brain works, a construct that is by its nature ductile and malleable, won out in the end.

 So I feel a profound sadness that I started out programming DreamCoder in Emacs, the most extensible editor in the world, by hand back in May 2025, only to see DreamCoder write itself… in DreamCoder today.

 Future

 I am still sad, but I also know that our industry completely reinvents itself every decade or two. This is my second career upheaval. Most programmers today have not been around long enough to go through it themselves. So I feel for them that this especially massive quake is their first encounter with how unsentimental our industry is.

 But for all the sadness, I wake up every day with a feeling of optimism that I have not felt in a very long time.

 I finally get to build again, no longer weighed down by my decades of knowledge and experience that held my ambition in check. I truly have not felt this liberated since I was a teenager programming in Delphi, blissfully unaware that the things I was busy building were impossible for a self-taught teenager to ever realize. I see this reflection in others: the best programmers I know also love AI. Amateurs also revel in AI’s capabilities, happy that they can finally solve problems they could never afford to pay a programmer to do for them.

 I must admit that building software has, over the years, gotten a lot more complex, with an ever-larger share of that work being repetitive tedium. This is more so with hobby software – as I do not get paid to do it, so I do not have a moral duty to see it through – where I’d do all the fun bits leaving just the enervating, boring and soul-crushing parts behind. Do you have a projects folder full of sad, abandoned projects like I do?

 Now I can craft in abundance. AI has freed up a lot of toil but I somehow still find myself busy all day doing real work.

 Building a coding harness is perhaps the closest I will get to the optimism all those researchers and scientists must have felt in the 1970s and 1980s. They hoped that with a little bit more work, their logical rules would kindle a new intelligence. Fifty years on, and I can simply tell DreamCoder to improve itself and watch as it changes before me. I can ask the AI running inside it to analyze the changes I have made to its tools and prompt and have it adjust them accordingly. It feels like science fiction; the very thing the researchers of yesterday strove to build. Yet we really do live in this reality now.

 Taste is a scarce, human resource.

 So. DreamCoder . Let me address the 900 lb gnu in the room: DreamCoder is not an Emacs-related application. The reason is unfortunately one of economics and access: I want to build an AI coding harness for everyone. But don’t worry: I have some cool plans for DreamCoder + Emacs, and AI + Emacs more generally going forward. So stay tuned.

 But what about all those other coding harnesses? Well, most of those harnesses all suffer from the same mistakes. It is a problem that is not unique to coding harnesses or the people who make them, but a constraint we all labor under, and one that is not easily replaced by AI:

 Taste is a scarce, human resource.

 And for all the bounty of AI, it still requires a human to persevere and to see things through. One thing intensive use of AI coding has taught me is that we’re going to need a lot of computer programmers who know what they’re doing going forward. I believe this is so, because let us be honest, most people do not want to program computers, even if that computer can actually do the bulk of the work for them. It requires a steady hand to build reliable software; that has not changed.

 Therefore, if we programmers have to spend a lot of our time interacting with AI, then the tool we do it with should be ‘human-centric’ in its design, and it should take advantage of all the modern features we have at our disposal.

 Back in May 2025 I took a look at all the tooling and said “no, thank you.” Today I look at the landscape and I feel pretty much the same.

 And I think I am not the only one who feels that way. Most of these coding harnesses, to me, feel bristly. They shouldn’t be; but they are like that because we are at an important inflection point where no one really knows what the future looks like. We’re all just… fumbling around a bit. It’s an exciting time to build software, even if we don’t quite know what the world will look like a few years hence.

 One thing I am adamant about is that DreamCoder must be a powerful, frontier-class coding harness. That means it should have all the features you’d expect from that: backgroundable sub agents, MCP servers, cache efficiency, and all that stuff. Check.

 Sub-agents 

 MCP servers 

 Your own agents 

 Terminals beside chats 

 The frontier-harness basics. Click any of them to see it full size. 
 But that stuff quickly recedes into the background because, you know, it just works. Day to day you will dart between chats and terminals and whatnot, and you need an interface that accommodates that. Emacs is a tiling window manager; so is DreamCoder. DreamCoder’s window manager is a little bit cleverer than most window managers as every pane has a minimum, comfortable and maximum size. The window manager will therefore ensure windows always fit snugly on your screen, and you’ll never end up in a situation where windows are tiny and unreadable. It has a sophisticated constraint satisfaction solver that tries to balance your demand for a new window (“open a terminal”) with the challenge of keeping your visible panes roughly the same size. If DreamCoder can’t wedge in a new pane, it’ll punt one to the hidden window bar. Just click it to resurface it, or hover it to see what it’s doing; it’s a live view.

 Panes are made to fit; if a new pane must evict an old one, it is pushed to the hidden window box. 

 Avy-style selection and embark-style actions. 
 
 Because of my Emacs roots, I think a good tool must be keyboard-friendly. Because it runs on a browser you get the mouse for free of course. But smacking the tab button over and over is a frustrating user experience in complex webapps, and doubly so a tiling window manager: where exactly are you going to end up when you tab from one window to the next? To combat that, I built an avy-style window and “point of interest” selector for chats. Tap a key and pick from a selection of “embark”-like actions such as clicking links or opening pictures. It’s a work in progress, but I think it works well.

 Familiar type-to-complete mechanics 
 
 Most high-volume operations like opening and creating panes is done through a Helm-like interface with search-as-you-type. It’s really efficient, of course. And it works with a mouse also; which is sort of the point. The keyboard’s there for those who want it, and the mouse for regular folk who are just getting started. One unique feature of the design, which admittedly I am still exploring privately, is that everything is stored as Javascript objects (on account of running in your browser) so it’s not too much of a leap to build “macros” that prefill most of these dialog windows, leaving behind just the fields you want to edit.

 But yeah. With DreamCoder I want to take the best of Emacs and its coterie of third-party packages and bring some of that with me. The world is still not ready for an Emacs-shaped future, sadly, so that is why DreamCoder is a standalone application and a web frontend.

 Another thing that drives me wild: I see people with tmux running 10 claude codes (or codex, or…) cycling between them like a duck gallery at a carnival to see if one of them is done working, or if it needs human intervention.

 So there’s two things to unpack here: one is running lots of things in parallel, and the other is observability. You need insight into what is going on: is an AI jammed because it’s awaiting an answer or a tool safety prompt? Perhaps you’ve parked a bunch of chats pending some conversations with coworkers or other work that must finish first.

 In DreamCoder you have workspaces. They’re like virtual desktops (or window configurations in Emacs lingo): a snapshot view of panes as you want em. As you can see from the screenshots, panes expand to fill all the space. So if you want more space, you can: resize them (with the mouse or keyboard); shuffle them to a named workspace; or float them so they sit on top of the other windows.

 The event graph 

 Objectives 

 Image panes 

 On your phone 

 More than a chat window, already. 
 But if you’ve got a lot of things happening in multiple workspaces, it’s hard to keep tabs on that. That’s why DreamCoder has a big, honking minimap in the top-right corner. One for each workspace. The minimap is a miniature of your actual layout. Each pane in the map gently pulses when it’s working, and it makes it abundantly clear when it’s blocked. When there’s nothing to do, it’s green.

 Because workspaces and panes are distinct things you interact with, it must be easy to navigate between them.

 I also wanted full-on, optional Emacs key bindings, but that is… pretty much impossible to properly build. Browsers lock you out of some rather important Emacs button combinations. Sadly that feature is parked until I can solve it on all major browsers without breaking your normal browser keys.

 That’s not to say it doesn’t have Emacs-inspired key bindings. Most global actions are reachable with Alt+x , akin to M-x ; local, pane-specific ones with Alt+c . Alt+m activates keyboard mode: you can now type the number of the named pane to jump to it; or WASD to switch the active pane in that cardinal direction.

 Support for open weight models like Qwen, Gemma, Deepseek, GLM, etc. is also very important to me. They work so well. I’m really surprised, here in late 2026, just how capable small models are at local-only development compared to just one year ago. Qwen 3.8 27B, for example, is fantastically good for its size. You can do a lot of good software development with it if you’re a capable hand yourself. Bigger models equal more auto piloting; but that Qwen model? Wow. So local models work great. In fact I think the future is local for a lot of use cases. Intelligence is fast approaching a cost where it will be too cheap to meter. If you remember the personal computer revolution in the 1980s and 1990s, then there are definitely echoes of that here.

 If you’ve been holding off on local models then I do recommend you reconsider. Small ones like Qwen 3.8 27B (or its cousin, Flash Next) can run well on a high-end gaming rig or Mac, or with a little investment if you do not have that. If you have a dinky old computer and you’re cash starved, then not all hope is lost. Turn to the potato agronomists on twitter: give twitter’s AI, Grok, what you have and what you can reasonably spend and tell it to track down the cutting edge setup for your rig. This is no lie the fastest, easiest way to catch up to the cutting edge of self-hosted inference today. Five minutes.

 Coding harnesses are the IDEs of the future

 As I’ve been building DreamCoder, I have come to the belief I’m not just building a coding harness. Coding harnesses are an IDE for the future; it will do more than just display a chat window for coding agent work. DreamCoder does more than that already. It’s going the way of Emacs in that it’ll consume a wide range of adjacent workflows and tools. But I have only just gotten started. I am brimming with ideas I’m building in parallel, but they take time because as I said it’s not about the code; it’s just one small facet of building something that works well. But you know that already: it’s always the last mile.

 DreamCoder is the most ambitious, technically complex and advanced software project I have ever built in my life. And that’s just the beginning. I’m not done. I’ve barely started. I will be blogging about this going forward, in addition to my usual Emacs scribblings.

 In fact, the thing I’m currently grinding away at is a world-class pentest and cybersecurity suite in DreamCoder. Every single bit of software we have ever written is vulnerable; we have many rough years ahead of us. Just look at the crippling vulnerabilities coming out every day now almost. Even the most security conscious person is going to find themselves on the wrong side for no other reason than we depend on packages that were mature and stable and assumed to be secure. DreamCoder can do its bit to help catch many of most obvious weaknesses, especially as new software is minted every day that also needs thorough testing.

 Pentested endpoints and their states 

 Findings and how exploits were traced 

 Screenshot of DreamCoder's upcoming, awesome pentesting and cybersecurity suite. It's built for humans . The AI does the work, and you and your team assess its results and impact. The graph overview is AI-generated from its explorations and findings. Do not worry: no human will ever have to suffer the indignity of writing flow charts like that. 
(If you're interested in/have questions about the pentesting stuff, please e-mail me.) 
 To round it off, I would like to formally invite you to join me in making DreamCoder better by trying it out . It’s great. It’s not a toy; it’s not a demo; and it’s not a weekend prototype. It’s a frontier coding harness that has most of what you’d expect: MCP, backgroundable sub agents and shell commands, terminal windows, skills, hooks, 99% cache hit, it runs for days, and an interactive UI for all of it. There’s a handy dandy importer for your Pi, OpenCode or Codex configs also to help you get started. A couple of clicks and your model settings are set up in DreamCoder. Ready to go.

 Please do e-mail me your thoughts ( (rot13 "zvpxrl@znfgrevatrznpf.bet") ) on AI, coding harnesses, what you’ve built with it, and what you think more generally about where our world is heading. I’m keen to hear from you.

 And if you want to hear more from me on the technical aspects of AI, building coding harnesses, and more, then do sign up for the DreamCoder newsletter below.

 Try DreamCoder

 Download  DreamCoder 

 macOS Windows Linux Docker 
 
 The DreamCoder newsletter

 An occasional e-mail when there's DreamCoder news: new releases, and new writing on AI and coding harnesses.

 Further Reading

 Have you read my
 Reading Guide 

 yet? It's a curated guide to most of my articles, and I
 guarantee you'll learn something whether you're a beginner
 or an expert.
 And why not check out my book? 

 Subscribe to the Mastering Emacs newsletter

 I write infrequently, so go on — sign up and receive an e-mail when I write new articles

 Very interesting software, I've always felt there's something wrong with the current design of harnesses. I will give this a try in the next few days.

 I am curious about two things. First, would it be possible to make use of existing harnesses kernels ? Second, are you planning to release the source code ?

 —  heiwiper · reply 

 DreamCoder has its own internal tool loop system; it does not use other harnesses' kernels. That might be a thing in the future if there is enough demand for that. 

 —  
 
 ⭐ 
 
 Mickey Petersen ·
 reply 

 so sad that browser is the best way to get cross platform gui, i generally hate applications that reinvent the window manager but this one is worth it. embark actions are an amazing solution i never found, i will be using those vehemently in my shithole projects. the "graph/visualization first" ui shape is i think the future of HITL harnesses. 

 —  Paths · reply 

 I adore the slight skeumorphism in the UI design. Makes everything very legible. Flat design should never have happened at the scale it did, IMO.

 One nitpick: The download page misdetects the operating system, though, it detects Arch as Debian and tries to give me the Debian package. I suppose it can't do any better since all it gets from the user-agent header is "Linux". Gonna try the Docker release.

 —  
 
 Psy-Q ·
 reply 

 Copyright 2010-24 Mickey Petersen. Terms & Privacy Policy (Last updated 2022-05-24 .)
