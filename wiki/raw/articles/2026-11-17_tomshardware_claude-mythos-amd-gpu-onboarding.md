---
title: "Claude Mythos slashed AMD GPU onboarding to ~3 days (Tom's Hardware)"
type: article
source: https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-says-claude-mythos-slashed-software-work-to-onboard-amd-gpus-from-up-to-12-months-to-around-three-days-writing-almost-100-percent-of-kernels-autonomously-chips-away-at-nvidias-cuda-moat
published: 2026-11-16
fetched: 2026-11-17T12:05:41Z
sha256: 3b9ad049f3b8fc6ab35433cbd4808a44ec3ce4b96b3896fccffeec384f1c803c
---

If AI can write the low-level code that ties models to Nvidia, CUDA matters less. 

 a]:text-inherit [&>a]:underline">
When you purchase through links on our site, we may earn an affiliate commission. Here’s how it works .

 (Image credit: AMD) 

Share 

 {alert('Link copied')}).catch(err => {console.error('Failed to copy: ', err)})" data-platform="copy_link" data-action="" class="font-ui-heading py-2 text-sm text-neutral-700 hover:bg-neutral-100 transition-colors no-underline block cursor-pointer border-0 bg-transparent w-full text-left normal-case" aria-label="Copy link" role="menuitem" data-analytics-id="article-social" analytics-label="utility-bar-social-share-copy-link" analytics-name="utility-bar-secondary" data-mrf-recirculation="article-social">

Copy link

Facebook

X

Whatsapp

Reddit

Pinterest

Flipboard

Email

 Share this article 

 Join the conversation 

Follow us

 Add us as a preferred source on Google 

Newsletter

 Subscribe to our newsletter 

 Anthropic told IPO investors that its Claude Mythos Preview model did the software work required to get its AI running on AMD’s GPUs in about three days, with “basically no human intervention,” a job it says used to take six to 12 months. The three days cover prompt processing for one Anthropic model on AMD MI355X GPUs “at a useful level of performance,” with Mythos porting or writing “almost 100% of the kernels.” That kind of low-level code, which ties an AI model to one company’s chips, has long been part of Nvidia’s CUDA moat, and an AI that can write it in days would suggest that moat is eroding. Tom Brown, Anthropic’s co-founder and chief compute officer, made the time comparison, noting to investors that the original meant using a team of “dozens of engineers.” The company already runs its models on multiple kinds of chips — on GPUs from Nvidia and AMD, Google ’s TPUs, and AWS Trainium — and its fleet is managed as “one fungible pool of compute.” Brown called the early multi-chip decision “an unconventional bet.” It may have been a wise one, given that Google’s TPUs can now natively run AI models built in PyTorch , and Meta uses them in production. Anthropic's claim that the job used to take six to 12 months comes from past work, from its “historical experience bringing up new accelerators using traditional engineering approaches,” where tailoring the code to each hardware platform was a challenge. Removing that onboarding barrier could reduce things to a purchase decision, and Anthropic started working with AMD GPUs for the first time this year, with an agreement for up to 2 gigawatts now in place. Latest Videos From Tom's Hardware Watch full video here: CUDA, Nvidia’s programming platform, is very mature at nearly two decades old. AMD has an equivalent, ROCm, with HIP as its programming layer. Code written for CUDA has to be transformed to work there, and AMD even built a tool called HIPify for the process. There is still a conversion cost to switching, and AMD’s vice president of AI software, Anush Elangovan, told EE Times in April that “Claude is better than HIPify because it has web search built in.” AMD has been making the argument that AI can write this type of code since August of last year, presenting a research agent that fell short of human experts at the time. In September of that year, AMD CEO Lisa Su said on the Possible podcast that much of AI software is written in CUDA, which needs to be “translated to AMD,” and “a ton of that can now be done in software.” 

 You may like

 Anthropic’s IPO filing shows most of its compute goes to R&D, not serving customers 

 Solo dev enables using CUDA on AMD hardware in Windows, getting multiple CUDA libraries running on a gaming Radeon RX 9060 XT GPU in Windows 

 ‘This is how AI should be used’ — OpenAI head of hardware breaks down the AI-assisted design of its Jalapeño ASIC 

 Moving forward to July earlier this year, AMD’s senior vice president of AI, Vamsi Boppana, said its engineers were using AI models to generate GPU kernels, and Su said that when she asked whether her team was helping the Anthropic engineer working on the MI355X, she was told they didn’t need any help. Boppana said that in some cases, the resulting kernels were even “better than the most manually tuned versions.” Under its July agreement with Anthropic, AMD is also using Claude to optimize workloads for its Instinct GPUs and to speed up ROCm development. At AMD’s Advancing AI event in July , OpenAI’s Philippe Tillet said that once OpenAI got its Helios racks, a single engineer confirmed everything worked within a few days, and that “agents are taking over our jobs, in a sense, as kernel engineers.” Before the event, AMD’s Andrew Dieckman, corporate vice president and general manager of the company’s data center GPU business, told reporters that he has had practically zero conversations with AMD’s customers about CUDA. 

Swipe to scroll horizontally

 Date 
 Who 
 What they said or showed 
 Where 

 Aug. 1, 2025 
 AMD researchers 
 Published GEAK, an AI agent that writes GPU kernels; against 30 expert-written kernels it got 19 right, at 0.92 times the experts’ speed on average 
 AMD’s ROCm blog 

 Sept. 24, 2025 
 Lisa Su, AMD chair and CEO 
 Asked about AI coding tools, said much of the code written for CUDA can now be translated to AMD in software: “We’re using software to significantly optimize our customers’ code so that they can run on AMD” 
 Possible podcast 

 April 1, 2026 
 Anush Elangovan, AMD vice president of AI software 
 Compared Claude with HIPify, AMD’s tool for converting CUDA code: “Claude is better than HIPify because it has web search built in” 
 EE Times interview 

 April 15, 2026 
 Jensen Huang, Nvidia CEO 
 “We use a ton of AI to create the kernels that we have”; “nobody knows our architecture better than we do” 
 Dwarkesh Patel interview 

 July 23, 2026 
 Andrew Dieckman, AMD corporate vice president and general manager, data center GPU business 
 “I have almost zero c

## HN discussion highlights (item 50526264, 48pts)

### claude-mythos-amd  (48pts, story=Claude Mythos slashed software work to onboard AMD GPUs to around three days)
[Creamsicle47] Ironic this is the same company trying to prevent people from modding Skate 3 inside of Minecraft
---
[nsoonhui] I doubt whether this will eventually be the undoing of Nvidia -- no, Jensen's affair doesn't even count. If Claude, which is trained on Nvidia chip, becomes so powerful that it allows developers to get onboard with ecosystems other than CUDA easily, what moat does Nvidia still have? Remember, CUDA is widely viewed as the greatest -- some even say only -- moat Nvidia has. You can duplicate the hardware, the software, but you can't duplicate the de
---
[davesque] Isn't kernel development one of their banned topics in their public facing models? The ethics of this are just so inherently dirty. They can enjoy the benefits--the sum value of all that compiled knowledge--but not us. If open models don't succeed, the future is looking pretty bleak. Really. This normally feels like such a tin hat thing to say, but damn if it doesn't feel true right now.
---
[jraph] Just before Anthropic's IPO, just after it looks like nvidia may be struggling. How convenient! How do we know it's not another lie, or full of conveniently hidden limitations? But I guess that works, investors will be appeased enough either way. AMD is not AI's bank though, so their cards are the wrong cards to run AI on (and that might be the reason we've not seen a "we can run on AMD too!" announcement earlier)
---
[AMDAnon] AMD doesn't get access to Fable or Mythos. Big problem now that non-Mythos is locked out of doing GPU development work. Nvidia has access to everything at huge discounts, including unreleased models. The "moat" is that anyone who isn't a $1+ trillion company or an AI lab is going to be locked out of the cartel going forward because they don't want you competing in their space as they consume more of the economy. So yes, Mythos can one-shot CUDA, 
---
