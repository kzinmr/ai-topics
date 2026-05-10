---
title: "Ask & Adjust: The Future of Productivity Interfaces"
source: "Warp Blog"
url: "https://www.warp.dev/blog/ask-adjust-the-future-of-productivity-interfaces"
scraped: "2026-05-10T01:27:08.793010+00:00"
lastmod: "2026-04-24T14:39:18.000Z"
type: "sitemap"
---

# Ask & Adjust: The Future of Productivity Interfaces

**Source**: [https://www.warp.dev/blog/ask-adjust-the-future-of-productivity-interfaces](https://www.warp.dev/blog/ask-adjust-the-future-of-productivity-interfaces)

Product
Ask & Adjust: The Future of Productivity Interfaces
Zach Lloyd
April 12, 2023
This article describes my best guess of how productivity apps will work in a future where Generative AI is everywhere. I’m writing this from the perspective of someone who is currently building a
productivity app
, so it’s been on my mind a lot lately.
By productivity apps, I mean things like Figma, Google Docs, VSCode, Notion - basically any software where knowledge workers spend their days writing, designing, coding, analyzing, etc
1
I’m particularly interested in “horizontal” productivity apps - ones used to produce a wide variety of artifacts or accomplish lots of different tasks, rather than very narrow ones (e.g. an app that just creates marketing blogs). Finally, I’m discussing AI in professional tools, not consumer apps, where I think the path will be different.
In case you don’t have time to read the entire piece, the tl;dr is that I believe we are moving to an AI-first world in productivity, but, importantly, not an AI-only world.  I think the main paradigm in horizontal productivity apps is going to be
Ask & Adjust
: AIs will iteratively generate drafts or edits, and humans will hand-tweak them until they are right. I believe the closer the application is to one where “creative-license” is allowed (e.g. image creation or marketing copy), the less important these hand-editing interfaces will be; however for activities like coding where it’s very hard to express your intent exactly to an AI, the hand-editing interfaces, along with collaborative re-use, will remain crucial.
Before Generative AI: apps optimized for hand-editing
Before I get to Generative AI, it’s worth quickly describing how productivity apps have evolved over the years.  Traditionally, the paradigm for creation in productivity apps has been pretty simple: the author uses the tool to create, edit, and share their work. I mean “author” here in a broad sense – in Figma the author is a designer, in VSCode it’s a developer, in GDocs it’s a literal author, in Webflow it’s a website creator.
Because the author has always been a human, these productivity tools are heavily optimized for a human-driven creation experience (obviously). I think of  them being optimized for
hand-editing
- the apps that provide the best experiences are ones that have the most powerful, intuitive and efficient knobs and dials for humans to create artifacts or accomplish tasks.
In VSCode, this means a convenient UI for comprehending and editing code (e.g. multi-cursor, jump to definition, etc). In Notion it’s a great interface for dealing with structured and semi-structured data.  In Webflow it’s a fast way of editing websites, etc. A lot of work has gone into improving these hand-editing interfaces over the years and, from the perspective of app builders, it’s super-important to get them right.
Collaborative building blocks: shared templates, libraries and scripts
In addition to optimized hand-editing, much innovation in productivity apps lately has come from collaboration and re-use features. These features allow users to use the work of others (either their teammates or the community) as a starting point, and to easily share whatever you create for others to browse and re-use. Shared templates, libraries, and scripts – along with real-time “create together” flows
2
are all examples of collaborative building blocks improving productivity interfaces.
Templates,
for instance,are a way of bootstrapping the creative process by starting from a premade “thing” (e.g. a company’s template presentation, or something more task specific like a “todo list” template in a spreadsheet, or a marketing site template on Webflow). Templates come in many forms — GitHub Codespaces is basically a fancy template mechanism for development environments.
Libraries
, like Figma components for designers or open source repos for devs, allow reuse of “pieces” of prebuilt functionality, saving time and increasing consistency.  Libraries are everywhere these days and are probably the most important collaborative building block.
Scripts
and
macros
simulate human interaction with the interface to make accomplishing a task easier – you “record” or write what actions you want, possibly parameterized, and then have the ability to rerun them later.  The closer you get to developer tools, the more frequently you see scripting and macros (e.g. in spreadsheets and command-line tools).
The rise of cloud-based collaboration has made
sharing
all of these things – templates, libraries, scripts, and finished artifacts – drastically easier in the last 15 years.  Native sharing and storage has also created network effects around certain tools, which is why a few cloud native apps like Figma and Github have won in their spaces.
However, even with all of these shared building blocks the important thing to realize is that at some point human authors (either individually or jointly) are responsible for the bulk of the creation in today’s productivity apps.  Humans sitting behind keyboards hand-edit and stitch everything together. In a world with Generative AI, this is about to change.
Today’s creation loop looks something like:
From hand-editing and collaborative building blocks to “ask & adjust”
Productivity apps will be much different in a world with Generative AI.  My belief is that rather than hand-editing and collaborative re-use being the primary workflows for authors, the primary workflow is going to be
ask and adjust
.
In an
ask and adjust
world the human asks an AI within the app for help creating or editing something, and the AI provides a draft or revision.  This asking could be explicit (e.g. through a chat interface) or implicit (e.g. through an autocompletion interface) but the net result is the same: the AI suggests something that looks like fully formed content. I believe the “asking” will still happen within vertical productivity apps rather than being part of some “uber” AI creation interface because (as I’ll discuss below) I don’t see the hand-editing part of these interfaces going away anytime soon.
For example, in Webflow, rather than starting from scratch, users will ask for a “marketing website that features X images and shows the brand in a whimsical tone” and Webflow will generate a custom starting point – a bespoke template.  For product designs, users will ask Figma to adjust their component library to have “a more futuristic style” and the app will oblige.  And so on - anyone who has spent time in ChatGPT or Dall-E or similar will get the idea.  This technology is about to be in every productivity app.
However, it’s important to point out that the
ask
phase will usually not generate finished products. Instead, the AI will take a stab and give users a draft. The draft might be 80% of the way there. It might be 50%. In some cases this draft could actually be perfect; e.g when I use Github Copilot, the suggestion captures my intent perfectly something like 30% of the time. But I think perfection is the exception not the rule.  Users will usually have to tweak the draft by iteratively changing the AI prompt.
The reason these drafts will usually not be perfect is that for a lot of creative pursuits the human author doesn’t know what perfect actually looks like when they ask for help. There are two issues: one, humans are not able to perfectly express their intents; so even if the AI was a perfect translator of stated intent into form it would still be wrong a lot of the time.  Secondly, creation is an inherently iterative process where intent is often discovered as you draft and edit.
That said, even when the AI doesn’t perfectly nail it, there’s still a tremendous amount of value in how much time it saves and how far it can get you, which is why AI will be a core part of every productivity interface. For people who can’t illustrate or design websites or compose music it may even be that the draft makes the impossible possible - taking you from something you could never do to something that’s pretty good.
The interfaces for the
ask
phase are still being worked out, but the ones folks have started with are autosuggestions and chat. This will evolve towards deeper integrations and the apps that can most seamlessly integrate the AI into the creation experience will have an advantage. E.g. Imagine an AI “collaborator” in this GDoc I’m in right now suggesting improvements as I go, or an AI “co-designer” who cleans up your Figma designs as you make them.
The adjust phase - what will the interface look like?
However, for most productivity apps, my prediction is that the
ask
phase will not be the end of the story.  Instead the
ask
phase is going to need to be followed by an
adjust
phase where the human author hand-tweaks the output to match their intent.
For
ask & adjust
, the creation loop will look something like:
Before diving into the details of the
adjust
phase, some readers may question whether a hand-adjustment phase is going to be necessary at all.  For example, using a tool like Midjourney, you can generate and iterate on images in Discord using just text based prompts and simple buttons to get variations.  There is no complex interface to learn and no hand-tweaking UI.  Why can’t all productivity interfaces work this way?
Let’s briefly imagine that they can. In such a world, you wouldn’t actually need tools like Figma or Webflow or VSCode with all of their fancy controls and dials – this would be a world where successive prompting of the AI would be enough to get you to the perfect result.
A user would ask for a design or website or app and a draft would appear fully formed.  To the extent that thing wasn’t “right” the user would ask the AI for revisions until it was good enough, thereby removing the requirement to ever learn any of the harder parts of these tools’ interfaces (or learn how to “truly” design or code for that matter).
And beyond obviating these interfaces you can imagine a world without the need for the intermediate data models that these tools operate on.  If AI perfectly generates computer programs, is there an advantage to it generating something human readable?  Why generate javascript when web assembly is faster?  Why generate design files when you can generate the interface they describe directly?
Despite the rapid improvements in AI, I don’t think we are actually close to this world, at least not for professional apps. I say this not because I understand generative AI technology very deeply or because I don’t believe in the high rate of progress of AI (I do). Instead I say it because I believe there are inherent limitations in
humans
: often the gap in going from a person’s
expressed intent
to the final product using just natural language is too big.
Put another way, for the applications I’m talking about (VSCode, Figma, Webflow, Notion, Warp and the like) we are often unable to express our intentions to AI precisely enough for an AI to get it completely right, even through repeated prompting.
Of course it’s not just a single user’s prompt that is informing the result but the entire trained data set - but still I believe for a lot of applications that at some point users will need to refine their intents at a more fine-grained level, by actually writing code or altering vectors or writing characters using a purpose built tool
3
. After some amount of AI-assisted iteration, manual tweaking will actually be a more efficient way of getting the result they want. They will also (at least for now) want to understand the result and verify the AIs suggestions are correct.
Creative-license vs. precise requirements: how important is the adjust phase?
To be clear, I don’t think this is true for every kind of app.  I think it’s very much an application- or domain-specific challenge.  In general, the closer the domain is to one where there are a broad range of acceptable creative outcomes – where there is “creative license” – the less manual adjustment will be needed.  That means for image creation, music creation, marketing pabulum AI is going to be able to get you pretty much all the way there.
These outputs don’t need to be perfect – they can be good enough.
On the flip side, for domains where there is one correct outcome that has to be precisely implemented – and I would put coding and most developer activities in this camp – you are going to need adjustment UIs. For coding in particular, I think AI will have a huge impact, but it will be in streamlining the process, not writing the entire app for you without you seeing or editing any code.
The reason I think this is that the hard part of coding has always been humans getting clear on how they want a thing to work and then presenting this to a machine for execution.  This is why we write code in programming language rather than natural language; programming language is an extension of formal logic and lets humans express with exactitude what they want done.
For most coding applications this really matters – e.g. login flows need to be implemented in an exact way; so does most business logic in my experience.  It’s not an area where creative license really applies, and so an 80% right solution will not work.  You generally don’t have to fix bugs in images or marketing copy – you do in code, and that’s usually because humans can’t express (or often even fully understand) how their system needs to work. The “working” program is the only complete specification of the system typically – tests can verify parts of it, but not define the whole thing.   I don’t see how AI helps with this fundamental problem.
For instance I’ve frequently been trying to imagine AI writing the app I’m currently building – Warp.  It’s very easy to imagine an AI writing small parts of it: e.g. write me a function for storing this terminal output block on the server.  But for the more novel parts – - e.g. write me a block based terminal emulator with a modern text editor as its input – I can’t imagine an AI producing working code for them because I don’t even fully understand how they should work.
This leads me to believe that hand-adjustment in our productivity apps is not going away anytime soon. I think the much more likely flow in the next five years is that the AI helps generate and edit drafts, but then there is a “fallback UI” that the human uses to finish the process.  This fallback UI is what we think of today as the primary UI in most of our productivity apps, but as the AI gets better and better, we will need to use that UI less and less.
Likewise, I don’t see collaborative re-use going away – it’s just too valuable to be able to reuse standard components, even if you have AI helping you along the way. The value is not just in time savings but also in consistency and maintainability and knowledge-sharing.
My guess is that the best AIs will understand which shared templates, scripts, and components exist and suggest using them – eventually the AIs will be able to create and share and surface these components themselves
4
What does all this mean for creators of productivity apps?
First off, authors of apps should figure out where they sit on the spectrum of needing an adjustment UI - the more creative license there is, the less adjustment needed (and vice versa).
If your app does need an adjustment UI, you should think of AI today not as a replacement for the core interface, but as a way of more quickly, efficiently and intuitively generating drafts and edits within that interface.
For these apps, it means that the primary interfaces of today will likely become fallback interfaces tomorrow.
It means that if you are starting a new company building a “horizontal” productivity app, it’s risky to ignore the primary interface and try to skip directly to an AI-only interface.
It means that we should expect primary interfaces to become simpler and more hidden, and that AI will increasingly be a universal interface present in all productivity apps.
It means that collaborative re-use will remain an important part of the creation process, but one that is aided by AI.
In summary, the apps best positioned to succeed in this world are ones that add AI seamlessly to the creation and editing process, but still have UIs for hand-tweaking and collaboration that humans can efficiently use to get to the end results they want.
That’s my take at least. I’d love to know what you all think.
\---
Footnotes
1 These changes are already happening at a high rate (e.g. the launches of “insert product name AI” that are happening every day). I’m more documenting this as a way of talking about the changes and trying to give them names rather than pointing out something totally novel.
2 These apps also greatly improve consumption and knowledge sharing by centralizing access to a team’s stuff – there are a lot of benefits to cloud native collaboration.
3 Can you imagine for instance an AI generating text without it going into a text editor? Maybe for very niche use cases, but in general the AI will participate in drafting but not obviate the need for the editing tool itself.
4 As an aside, one of the issues with Github Copilot right now is that by always generating raw code it creates more code than is necessary; it bloats the codebase and creates duplicate code fragments. I suspect this will change and going forward Copilot will be able to suggest decompositions and create reusable libraries for you.
Related articles
Apr 28, 2026  ·  7 min
Warp is now open-source
Warp is now open-source, and the community can participate in building it using an agent-first workflow managed by Oz, our cloud agent orchestration platform.
Apr 14, 2026  ·  2 min
Introducing Universal Agent Support: level up any coding agent with Warp
Warp now supports the most popular CLI coding agents — including Claude Code, Codex, Gemini CLI, and OpenCode — with vertical tabs, notifications, native code review, rich input, and remote control, making it the best terminal for multi-threaded agentic development.
Mar 24, 2026  ·  7 min
Build vs buy: how to deploy coding agents at scale
Should you build an in-house agent orchestration system or buy one off the shelf? Here's how to think about the decision and where the real complexity lies.
