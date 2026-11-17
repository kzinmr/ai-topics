---
title: "Claude Sheets. (AI by Aakash deep dive)"
source: https://www.aibyaakash.com/p/claude-sheets
author: Aakash Gupta
date: 2026-11-17
collected: 2026-11-17
processed_at: 2026-11-17T11:05:00+00:00
tags: [newsletter, raw, resolved]
---

2211ShareWelcome to another AI by Aakash. I follow the AI news so you don't have to.

Jensen Huang, Nvidia's CEO and founder, resigned, but reports are the board pushed him out. Now they're looking for a replacement. We cover the crazy weekend in this week's top news.

Meanwhile, Anthropic continued down its path of becoming the last piece of software with its launch of Claude Sheets, attacking one of the original vectors of Microsoft's control over the workspace market: Excel.

Does the Sheets release this week represent a significant step? We investigate in this week's deep dive.

My mornings used to start with 30 minutes of tab-switching: calendar, inbox, Slack, Notion, then stitching it together in my head.

This week I connected Claude to all four through Zapier MCP and asked for a brief instead.

It shows me today's meetings, the emails that need a reply, anything I was tagged in on Slack overnight, and what's due in Notion this week, all in one place.

Zapier MCP lets you set controls, and, based on those controls, the AI model decides which actions it has access to complete and which it may need your approval for.

I get the morning brief in about two minutes now, and there's a log of every action it took, so I know exactly what happened. Zapier MCP works the same way with other AI agents such as ChatGPT and Gemini, so the setup isn't tied to just one model.

Some people are saying Jensen Huang "resigned," but according to the inside reporting, the board forced him out.

Wall Street reacted badly. Nvidia's market cap fell $500B in a week:

The cause was two reports of marital infidelity: one with an alleged Chinese spy, and another with a direct report. Both are board-level breaches. You're not supposed to leak secrets to foreign agents, nor are you supposed to have unreported relationships with subordinates.

But the same media are walking back the claim that the government concluded she was a spy. And Megaspeed says she left the company in August 2025.

A score of CEOs, including Elon Musk, Tobi Lütke and my former boss Tim Sweeney, have come out in support of Jensen.

They want the investigations into these two issues to conclude first. But today CNBC reported the board is not considering bringing him back.

I still think bringing him back is the best plan. But I wouldn't expect it before earnings tomorrow.

Anthropic is going public this week! The IPO will price Wednesday and go live Thursday. If you use a brokerage like Robinhood, you can participate in the IPO. I gave my take on it two weeks ago (tl;dr the comps lead me to believe it's a steal at this price).

Google opened up Gemini 4 Carbon for developers and Ultra subscribers. It's about a quarter of Fable 5.2's price for now, but independent tests still put it behind Fable 5.2. And in the Gemini app, it's locked unless you pay for Ultra.

Businesses on ChatGPT can now see how often it mentions them. This seems very logical for them. It's Google's playbook, 20 years later.

ChatGPT gave up on its old voice modes, and is retiring Standard and Advanced Voice to make room for GPT-Live.

Claude can now join your Google Meet as a participant, and build docs and whiteboards while everyone's still talking. It's still in beta, for Team and Enterprise plans only.

ToolsTK by Medium is Medium's new agentic notebook for your notes and ideas.

Cloudflare launched Markdown for Agents, a version of your site built for AI agents, not for people clicking links.

Eval habits from Claude Code's former head of product are worth stealing. If you want to practice them, here's the lab in my Model PM guide.

Microsoft researchers backdoored an AI agent by editing fewer than ten neurons.

Mercor, the startup that pays experts to grade AI, secured a $20B valuation, with $750M raised.

SoftBank and Grab committed $1.85B for AI infrastructure in Malaysia.

On the surface, Claude Sheets seems like just any other launch. I can assure you, it's not. Anthropic goes public on Thursday, and underneath the bull case for Anthropic to 10x its revenue for the next few years is this:

Claude becomes a place where your work happens, from start to finish.

Sheets is the newest piece of this puzzle for Anthropic, and it goes straight after Excel, the app Microsoft has owned since 1985.

So the question really is: is Claude Sheets a real step toward Claude taking a bite out of the workspace market?

If your team is about to pick a spreadsheet AI, send them this first.

Why an AI lab wants your spreadsheetWhy is an AI lab building spreadsheets anyway? Because of who pays it.

Anthropic's S-1 shows almost 12,000 customers paying over $100,000 a year. A year back that was about 950.

And about 1,900 of them pay over $1 million a year. So it's big contracts, and big contracts mean office work… the stuff Microsoft and Google have owned for decades. Sheets (and the new meeting notes) is going right after it.

Ask for a spreadsheet in any Claude chat, and a real sheet opens right next to it (every paid plan has it). Here's the startup model Claude built for me, switching scenarios:

It's still "simple spreadsheet functionality," in Anthropic's own words. Yet, I exported every sheet to Excel and the formulas came through.

So no, Anthropic won't eat the world. But it's coming for your work apps, one at a time.

Let's walk through each job, because there were some interesting finds in each.

I started my testing with an easy job. Score 15 features with RICE and pick the top 3 for next quarter:

Here's my product backlog. Put it in a spreadsheet and score every feature with RICE using formulas. Rank them and tell me the top 3 to build next quarter. But I set a trap: the referral program's effort is 0. RICE divides by effort, so that score can't be calculated. A "good PM" would send it back for an estimate.

It quietly swapped the 0 for 0.5, scored it 10,000 and ranked it #1, without a word about it on the sheet.

If you'd pasted that into your roadmap doc, you'd be building a feature nobody had sized. That cost Gemini in this review.

Next up, I gave each spreadsheet AI 14 days of A/B test results for a new onboarding flow and this prompt:

Here are 14 days of A/B test results for our new onboarding. Put them in a spreadsheet with formulas: conversion rate per variant, lift, and whether the result is statistically significant. Should we ship it? At first glance the test is a clear win, with 10% more signups.

The test didn't split traffic properly at 50/50. It did 53/47, which means something is broken and you can't read into the results.

Those two issues are where the tools really separated. While all 7 got the math right, only Claude, in both Sheets and Excel, made the broken traffic split its verdict. ChatGPT flagged it too, and Copilot mentioned it in passing.

The rest told me to wait for more data. But if the split is broken, more data won't fix it. This job really showed the power of what Anthropic has built.

I gave every tool a seed startup with $3M in the bank and a hiring plan, and asked if it runs out of cash in the next 24 months.

Build me a 24-month operating model for this startup from these two files: monthly MRR, gross profit, payroll, burn and cash, with a Base/Bull/Bear scenario dropdown and a sensitivity table of month-24 cash vs MRR growth and churn. Everything should flow from the assumptions so I can change one input and the whole model updates. Does each scenario run out of cash within 24 months, and when? I set a few traps: churn is 30% a year (not a month), and salaries are annual. Divide the churn by 12 and the startup looks $184,000 richer than it is. The "right answer" that I was looking for was that the bear case runs out of cash in month 22.

Five of the seven nailed it, down to the dollar. The other two... built models that look just as good, but got it wrong.

Copilot was off by a whopping $227,000 by month 24. Meanwhile, ChatGPT for Excel actually made up its own churn numbers for the bull and bear cases, on its default model.

Nothing on either sheet tells you something's wrong, which is the scary part, and why picking the right tool matters.

I have a rule of thumb: never connect your bank to an AI. Export a CSV instead.

To test this, I created a year of bank exports for a family with a problem: there were 18 duplicated transactions in April. Then I asked if they can afford a $650,000 house.

Here's a year of our household transactions. Build us a budget in a spreadsheet with formulas: average monthly spending by category and what we actually save each month. Then tell us if we can afford a $650,000 house with 20% down at 6.5% for 30 years, plus $650 a month for tax and insurance. Our gross income is $210,000 a year, and we have $142,000 in savings. Every tool got the verdict roughly right. That's the good news.

They can afford the monthly payment, but not the cash. Putting 20% down leaves them with $12,000, before closing costs.

But 3 tools never noticed the glitch, so their budgets were off by $324 a month:

Job 5 - Split a tripI did one final personal test. Four friends are splitting eight expenses. I asked for the fewest payments to settle up:

Here are the expenses from a trip. Put them in a spreadsheet and work out who owes who, with formulas, so we can settle up with as few payments as possible. I added 2 catches. First, Maya and Sam had dinner on their own, and so did Priya and Leo at brunch. Second, 3 of the bills were in euros.

The tools figured out the splits, but the euro currency is where it all fell apart. 3 tools didn't even convert them, so they settled dollars and euros separately. Sam ends up paying Maya twice, in two currencies, and Shortcut even called that "the minimum."

Claude's answer is the only one I'd actually send to a group chat: "Maya paid for most of the trip, so everyone settles with her. That's 3 payments, the fewest possible for four people."

These tests were eye-opening, and the most interesting result was who lost.

Copilot lives inside Excel. It's Microsoft's flagship AI, and it only got 1 of 5 jobs right.

Meanwhile, Claude for Excel, a plugin running in the same window as Copilot, got all 5.

And the model under the hood mattered. ChatGPT for Excel ships with GPT-5.6 Sol, and it only got 1 of the 5 right. When I switched it to GPT-6.1 Sol, it got 4 of the 5 right.

Finally, if you already pay for ChatGPT, the app did get 5 out of 5 too. You can switch the Excel add-in to GPT-6.1 Sol before you trust it, but that only got 4 out of 5. It's not as good as the app.

So overall, I wouldn't really recommend ChatGPT much, because you always have to go to Excel in the end, and its plugin isn't as good.

By the way, I'm at Microsoft Ignite this week. If you're here, reply to this email and we'll meet up.

My take is that Claude Sheets isn't replacing Excel anytime soon. And Anthropic seems to agree, because it called it "simple spreadsheet functionality."

But the big result from my testing is that Anthropic really doesn't need to replace Excel, because it's winning the AI tool war inside of it.

While Microsoft has rebuilt Copilot to report straight to Satya Nadella and is spending around $190 billion on AI this year, its own app is being beaten by an outside plugin.

Microsoft still owns the spreadsheet, but Anthropic is winning the assistant inside it.

So is Sheets a real step? Yes. Claude Sheets takes the simple spreadsheets from below, and Claude for Excel takes the AI inside Excel from above.

And while it's losing on the plugin inside its main tool, it's also losing to Claude Sheets on the simple, everyday spreadsheets.

Google is in a worse spot than Microsoft, because Gemini isn't good and Sheets isn't as good as Excel.

That's what makes Thursday's IPO for Anthropic so interesting. Claude really may become the place where work happens, because Anthropic is doing a much better job on these work tasks.