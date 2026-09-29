---
title: "Codex, File My Taxes. Make No Mistakes."
author: Kyle Corbitt (@corbtt)
date: 2026-09-29
type: web_article
source_url: https://corbt.com/posts/codex-file-my-taxes-make-no-mistakes
ingested: 2026-09-29
tags: [coding-agents, ai-agents, openai, codex, agent-capability-evaluation]
---

# Codex, File My Taxes. Make No Mistakes.

> Raw scrape via r.jina.ai. Shared by Kyle Corbitt (@corbtt) on X: https://x.com/corbtt/status/2104988602619052513

Title: Codex, File My Taxes. Make No Mistakes. | Kyle Corbitt

URL Source: https://corbt.com/posts/codex-file-my-taxes-make-no-mistakes

Markdown Content:
I asked an accountant and an AI agent to prepare my 2025 tax return. Only one succeeded.

Last year I [predicted](https://x.com/corbtt/status/1991953280373797112) that the best coding agent of early 2026 would be able to file my taxes autonomously.

When I sat down to do my taxes this year, I wanted to put this theory to the test! That said, vibe-filing my taxes felt a lil bit irresponsible, especially since I [sold my company](https://corbt.com/posts/openpipe-coreweave) this year and my tax bill has multiple commas. So, I decided to both (1) hire an accountant and (2) put OpenAI’s Codex on the case in parallel. Because naturally, the only thing more fun than doing your taxes is doing your taxes _twice_.

How did this turn out? Let me start by saying that I still believe that in the long term an AI agent will be able to do my taxes. But are they there yet in 2026? **Read on to find out!**

![Image 1: Illustration of John Henry facing a steam engine, captioned '$2000 accountant' versus '$20/mo Codex sub'.](https://corbt.com/blog-images/codex-john-henry.webp)

Will 2026 be the [John Henry](https://en.wikipedia.org/wiki/John_Henry_(folklore)) moment for human accountants?

## Taxes are annoying

My wife says I am a simple man. Give me a hunk of fresh-baked bread with a little jam and a lot of butter and I’ll be happy.

Sadly, that simplicity doesn’t extend to my tax situation. My 2025 return includes seven sources of income, K-1s from four partnerships, charitable donations of appreciated stock, a mortgage, crypto, partial-year ACA coverage, and Washington state capital gains (which uses a different formula than the federal one!). Oh, and that company sale, which involved three types of compensation, all with distinct tax treatment.

This complexity has been growing for years. Starting in 2023, I began using an external accountant to file my return. But even with that expensive help, the process was never _easy_. The accountant necessarily relies on me to share any updates to my work or personal life that might affect taxes. But it isn’t always obvious to me which things matter. I end up having to do a lot of my own research just to know which life updates to report.

Accountants can also make mistakes! In 2024 my accountant somehow ended up re-submitting one form from the previous year, leading to a slight over-payment and a baffling correction letter from the IRS months later.

So even after doing my own research and spending thousands on tax prep each year, I never felt fully confident that (a) my taxes were done right, and (b) I wasn’t leaving money on the table.

## Enter Codex

So this year, I decided to do things differently. I’ve been [heavily using](https://corbt.com/posts/a-pocket-guide-to-surviving-the-robot-apocalypse/) OpenAI Codex and Claude Code to simplify my life, and filing my taxes felt potentially within their capabilities. I decided to use Codex (Codex 5.3 at the time) over Claude Code for this project, since in my experience Claude’s Opus model is _slightly_ more likely to quietly cut corners on hard problems, which is exactly what I don’t want when calculating taxes!

## Just the facts, please

I already had a `finances` folder on my local computer with my annual tax forms and charitable contribution receipts going back a decade.

I started a Codex conversation in that folder and asked it to read my full 2024 tax return. Once it finished, I used [Handy](https://handy.computer/) to dictate a long, rambling monologue where I explained _everything_ that might possibly impact 2025 taxes. The company sale, my youngest son’s preschool expenses, home office use, new donation workflow—anything at all that might have an impact on taxes, however unlikely. That 10-minute unstructured braindump would have been overwhelming and borderline incoherent to a human, but Codex stuck with me. After I had blabbed out everything I could think of, I asked Codex what the next steps were.

Codex used that context to put together a list of “fact-finding” questions to tackle together. Things like “would my big stock donation reduce just my federal taxes, or Washington cap gains taxes too?” and “for the state-and-local-tax deduction, should we stick to property tax, or also try to claim sales tax?”

Over the course of a few hours, Codex and I burned through that list collaboratively. It would go off and do some research to determine the exact IRS guidance on a specific deduction or tax treatment, then come back to me with a focused list of questions about the facts of my case to determine whether the deduction applied.

I’ve been through similar rounds of fact-finding in the past, and I can’t emphasize enough how much more enjoyable this process is with Codex. With an accountant or attorney, the answer to almost every question is “give us a few days to research that and get back to you.” With Codex, the same research process can be done interactively in a few minutes. And subjectively, it felt like Codex’s research was more comprehensive.

Once we’d worked through the whole list, I asked Codex to create a `taxes/2025/README.md` document that recorded _every_ tax-relevant fact about my life we’d discussed, as well as the concrete decisions we’d made about the tax treatment we expected for every income source and deduction.

Finally, I asked Codex to estimate my 2025 tax bill, just to get a feel for where we were at. The estimate it gave me at this point ended up being within 5% of the final number.

## Gathering documents

Codex now had a strong high-level understanding of my taxes, so we started locking things down. First, we needed to gather all the relevant docs. Codex knew which forms we’d need, and I told it to go find them. I suggested it first find the forms it could in my email, then follow up by searching the relevant institutions’ websites[1](https://corbt.com/posts/codex-file-my-taxes-make-no-mistakes#user-content-fn-1).

Throughout the process, Codex kept a checklist in the same `taxes/2025/README.md` doc about which forms we’d already collected and which ones we still needed. It downloaded each form to a new `taxes/2025/raw_inputs/` folder. In the end there were a few it couldn’t find that I needed to manually track down, including one that had come by physical mail. And in fact two K-1 documents _still_ haven’t arrived, so I can’t file the final return yet. Luckily neither will show 2025 income though so I can still calculate and pay my total tax bill accurately.

This ended up being a very interactive process, since I had to manually handle the sign-in on each financial institution’s site. I _could have_ given Codex access to my password store and let it cook on this fully autonomously, but an autonomous AI agent with the power to move my money is beyond what even I’m comfortable with at this stage.

While this wasn’t exactly _easy_, it was easier than previous years, where _I_ had to manually keep the checklist of which documents I’d already pulled and hope I hadn’t forgotten anything relevant.

## Outsourcing to a human

With my documents collected I had everything the accountant would need. I asked Codex to upload all the collected docs to their online portal and send them an email explaining the year’s changes.

I still wasn’t super excited about paying a human $2000+ to plug numbers into forms and confirm tax treatments that Codex had already researched. Could it take the next step and _complete the tax return itself_?

I asked Codex to research the options. Frustratingly, there were no good ones. Online platforms like TurboTax and FreeTaxUSA don’t have APIs, and I wasn’t confident Codex could reliably navigate the UI through the dozens of forms it would need to input without error. And while there are a few open source “tax solver” programs out there, none included Washington State capital gains or all the forms and worksheets necessary to manage my annoyingly complex return.

## Codex, do my taxes

This might have stopped a lesser agent, but by now I was too committed to the bit to give up. How hard can it be to code your own standards-compliant tax engine? Ok admittedly that sounds pretty hard, but I still had 60% of my $20/mo Codex subscription to burn and was feeling ambitious.

I asked Codex if it would be up to the challenge. It puttered around for a few minutes reasoning through the options, and finally responded: **no, it was not comfortable writing a tax engine from scratch**.

But we aren’t here to be comfortable. So I asked it to build one anyway.

And it turns out, this worked _great_. Building a tax engine is a fairly well-scoped task with concrete acceptance criteria. The actual math that goes into calculating each value on the return is relatively simple, and is _extremely_ well documented in IRS materials online. And we didn’t actually need to implement the full complexity of the US tax code—we could skip many paths that we knew my 2025 return wouldn’t hit, like managing farm income (maybe someday! 🐄).

So about 30 minutes later, with no help from me, Codex came back with a tax engine written in Python that ingested all my tax forms and deductions as text-file inputs, and produced a final text-file output with the correct values for each line of my tax forms.

With one more prompt, I asked it to augment the engine to not just produce the text outputs, but actually complete and save the fillable forms. After a few more minutes of background work that was done. I had my final tax packet.

![Image 2: Redacted screenshot of the first page of Kyle Corbitt's 2025 Form 1040](https://corbt.com/blog-images/codex-tax-1040-redacted.png)
## Make no mistakes

The forms looked great, and the engine spit out a number for my taxes due. But was it correct? Honestly, I had no idea. I did some rough checks (read “I asked Codex and Opus to review the work and flag any oversights”) that came back clean.

The real test would be in the accountant’s professionally-completed alternative.

A few weeks later, the accountant finally responded with my estimated tax due… and it was **$20k under Codex’s number**. Disaster.

What happened? The accountant’s email only shared the estimated tax due. I asked Codex to email him back asking for the full return so we could reconcile. And while we waited for that, I asked Codex what could have happened.

After only a few seconds of thought, it came back with a hypothesis. When I sold my company, the cash component came in multiple buckets. Most of it was wired the day the transaction closed. But there was a second, much smaller transfer that came a few months later. I had actually forgotten about this payment, and Codex had noticed it when reviewing the 214 pages of acquisition documents! This payment was held out as an “adjustment escrow” to cover any unexpected company expenses in the short period between signing and closing. Post-closing, once the acquirer reconciled the books, the payment was released.

Was it possible that the accountant forgot to track this? Using its homebrewed tax engine, Codex re-ran my return holding this payment out… and it **matched the accountant’s estimate within a few dollars**.

Codex emailed the accountant back explaining the situation and asking if perhaps they had neglected to account for the adjustment escrow. A day later, the accountant responded with a new estimate. And this time, it matched Codex’s numbers almost perfectly.

I logged Codex into my bank and told it to send the payment to the IRS.

## What I learned

Interestingly, using Codex wasn’t just cheaper than hiring human help. It was better on multiple dimensions:

*   The immediate feedback that Codex could give on any tax question helped me understand my situation and the tax code more deeply than any prior year.
*   Codex had access to many personal details about my life and company, so it was able to make better assumptions about tax treatment even beyond what I told it directly.
*   It also helped me make smarter decisions around tax planning for 2026, which I’m already putting into practice.
*   **…and it caught a Twenty Thousand United States Dollars error**.

|  | Accountant | Codex | TurboTax |
| --- | --- | --- | --- |
| **Cost** | $2,000+ | $20/mo | $203 |
| **Personalized advice** | 2–3-day turnaround | Immediate, interactive | Lol no |
| **Correctness** | Made a $20k mistake | **Caught the accountant’s $20k mistake** | N/A |

Given my experience, should accountants be worried about their jobs? It’s tough for me to say. On the one hand, most accountants I’ve met don’t love doing personal tax returns, and their other duties may be much harder to automate. On the other… well, refer to the table above. By this time next year the market for personal tax accountants might look quite different.

## One more thing

I don’t think most people should write their own tax engine, or rely on the vibe-coded one that I wrote. But I would be surprised if we don’t see a high-quality open source tax engine by 2027, given how much demand there will be, and how tractable this problem is for coding agents.

To make this whole thing more transparent and give a leg up to anyone else who wants to try the same experiment (at your own risk!!), I’ve decided to [open source](https://github.com/corbt/2025-tax-engine) the 2025 tax engine that Codex wrote. **I have reviewed none of this code and make no promises about its correctness for any tax return beyond mine**. The best outcome here would be to inspire some startup out there to build a proper, tested product around this. I’d be a user!

* * *

## Footnotes

1.   I used Codex with the Playwright MCP for this. If I were doing it today, I’d use GPT-5.4 with OpenAI’s new [playwright-interactive](https://github.com/openai/skills/tree/main/skills/.curated/playwright-interactive) skill, which I’ve found works quite well. While I generally find Claude Code+Chrome more reliable than Codex on browser manipulation tasks, that wasn’t an option here since Claude (understandably) blocks access to banking websites. Codex lets me live dangerously. 😈 [↩](https://corbt.com/posts/codex-file-my-taxes-make-no-mistakes#user-content-fnref-1)
