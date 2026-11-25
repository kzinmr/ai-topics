---
title: "Jevons Paradox in AI: Cheaper Tokens Will Not Pay for Capex"
created: 2026-11-25
updated: 2026-11-25
type: article
source: "https://philippdubach.com/posts/cheaper-ai-tokens-wont-pay-for-capex/"
status: complete
sources:
  - "https://philippdubach.com/posts/cheaper-ai-tokens-wont-pay-for-capex/"
  - "https://news.ycombinator.com/item?id=50625888"
sha256: e4499ee8b0eb3f11f62d3e016c7dcdda37dbc942ecfa618443fef1f3a13a16cb
---

# Jevons Paradox in AI: Cheaper Tokens Will Not Pay for Capex

Source: https://philippdubach.com/posts/cheaper-ai-tokens-wont-pay-for-capex/

## Article

Jevons Paradox in AI: Cheaper Tokens Won't Pay for Capex Skip to content Philipp D. Dubach 
 
 Contents

 Contents Key takeaways Token volume and token prices are moving at roughly the same speed, so cheaper inference on its own does not grow AI revenue. Token volume and token prices are moving at roughly the same speed, so cheaper inference on its own does not grow AI revenue.
 The price of a fixed level of capability collapses each year, while the cost of running frontier models rises; the revenue sits at the frontier.
 Closing the gap between capex and revenue needs money that today pays for labor, and outcome pricing is how vendors are reaching for it.
 The capex and cash flow figures from March have grown worse: five hyperscalers spent $560 billion in the first three quarters of 2026.
 
 In March I wrote that the hyperscalers’ answer to collapsing inference prices is Jevons: cheaper tokens create so much demand that total spending grows anyway.
 On volume, they look right. Google processed 9.7 trillion tokens a month in May 2024 . In May 2026 it was 3.2 quadrillion, 330 times as many. Amazon, Microsoft, Alphabet, Meta and Oracle spent $230 billion on capex in the third quarter of 2026 alone, almost four times what they spent two years earlier.
 But tokens aren’t dollars. Revenue is price times volume, and the price is falling too. So my question is: does demand for tokens grow faster than the price of a token collapses?
 The arithmetic
 If the price of a token falls 10x and volume grows 10x, revenue is flat. Revenue only grows when volume grows faster than the price falls.
 Google’s first-party model APIs went from 7 billion tokens a minute in Q3 2025 to nearly 32 billion in Q3 2026 , up 4.6x. Google’s tokens across all products grew 6.7x between the I/O keynotes of 2025 and 2026. OpenRouter went from 0.5 trillion to 128 trillion tokens a week in 20 months , about 27x a year. On the price side, MIT researchers find that the price of reaching a fixed benchmark score falls 5 to 10x a year, and Epoch AI finds that cost per task at fixed performance falls about 13x a year.

 Volume and price move at about the same speed. That proves nothing by itself, because Google’s tokens aren’t sold at fixed-capability prices (like the ones Epoch measures). But it lines up with what Mert Demirer, Andrey Fradkin, Nadav Tadelis and Sida Peng found when they used OpenRouter and Azure data to estimate short-run price elasticities “just above one” and concluded that this leaves “limited scope for Jevons-Paradox effects.” At an elasticity of one, a 10x price cut buys 10x the tokens for the same money.
 That matches how a lot of buyers behave. Say a bank’s head of operations has $2 million approved for AI contract review, and then the vendor cuts its token prices tenfold. The bank can now review ten times as many contracts, which is great. The budget still says $2 million. To spend more, the head of operations would have to walk into the CFO’s office and argue that the product got cheaper and so deserves a bigger budget, and I wouldn’t want to make that case. So the bank spends the same $2 million. The vendor can say, truthfully, that token volume grew tenfold.
 But I guess there’s also a counterargument. Cheaper tokens change what people build. When inference is nearly free, developers design agents that call a model hundreds of times per task, and a recent theory paper argues this can make demand rise faster than prices fall. That may happen.
 Two price curves
 “The price of a token” hides two curves that move in opposite directions. (1) The price of a fixed level of capability is falling. GPT-4-level answers cost a small fraction of what they did in 2023, and the decline continues. (2) The cost of using the best model available is rising. The same MIT paper finds that the cost of running frontier models on benchmarks rises 3 to 18x a year , because each generation is larger and reasons for longer.
 A concrete case: to run the Artificial Analysis benchmark suite, Claude Opus 5.5 at maximum effort used 218 million output tokens , almost three times the median model, at about $10 per task. At low effort the same model used about a tenth of the tokens.
 Spending probably follows the frontier curve (at least up until now). In enterprises, open-weight models now handle 19% of tokens but get 4% of spend , while frontier labs take 69% of deployment dollars. Cheap tokens and expensive tokens are close to two separate markets (the cheap one grows fast in volume and barely registers in revenue).
 The volume is real
 I don’t want to wave the demand away. Google’s token count is the clearest public series we have, and it’s steep.

 Agents account for much of it. A paper by Bai, Brynjolfsson, Pentland and co-authors finds that agentic coding tasks use about 1,000 times more tokens than chat about the same code. Anthropic reported in 2025 that multi-agent systems use about 15 times more tokens than chat . OpenRouter dates February 6, 2026 as the last day humans used more tokens on its platform than agents did.
 Where the money has to come from
 If cheaper tokens alone don’t grow revenue, the money has to come from somewhere else. Bain estimates AI needs $2 trillion of annual revenue by 2030 to fund the compute being built, and that it will still be $800 billion short even if companies reinvest every dollar AI saves them in sales, marketing, support and R&D.
 You can already see vendors reaching for that money in their pricing. Intercom charges $0.99 for each customer case its Fin agent resolves , a price set against the cost of a support agent’s time, whatever the tokens cost. Salesforce has changed its Agentforce pricing three times since 2024. The direction is clear. Vendors want to be paid per outcome, and an outcome is priced against a (human) wage.
 Workers aged 22 to 25 in the jobs most exposed to AI saw a 13% relative drop in employment compared with less exposed peers. US employers cited AI in about 121,000 announced job cuts in the first ten months of 2026, about a fifth of all announced cuts.
 Related 
 Reconciling Enterprise AI Revenue Receipts
 Spending grew faster than I expected when I wrote in March. Back then the five companies guided to $660 to $690 billion for 2026. Their SEC filings show $560 billion of cash capex in the first three quarters, with $230 billion in Q3 alone. That excludes finance leases, so the full figure is higher.

 The cash flow squeeze I described has arrived. Oracle spent 174% of its operating cash flow on capex in its fiscal 2026 and Amazon 94% in 2025. Microsoft is at 63%, Meta at 60% and Alphabet at 56%, all well above where they were a few years ago.

 Who keeps the money
 So far the clearest winner is the company selling the equipment. Nvidia reported $116 billion of revenue at a 75% gross margin in its latest quarter, and its revenue has grown in step with hyperscaler capex for three years.

 The model labs sit lower. Press reports put OpenAI’s gross margin at 33 to 39%, depending on the quarter. Anthropic’s S-1 shows about an 85% gross margin , but it books training compute under R&D, so the figure only measures the cost of serving existing models. Even so, it suggests the cost of serving tokens may be falling faster than their price.
 Markets have priced the split. Since ChatGPT launched, the semiconductor index has roughly tripled while software stocks and the S&P 500 are both up about 70%. Chips have also fallen 41% from their June peak, so the market is less sure than it was in the summer.

 Disclaimer: Journalism, not investment advice or a recommendation. Not directed at UK persons; not a financial promotion under FSMA s.21. The author may hold positions in instruments discussed and receives no compensation from issuers. Full disclaimer → 

 Related reading
 AI Capex Arms Race: Who Blinks First? The March post set out the capex and cash flow problem that this follow-up checks against eight months of new data.

 Does AI mean the demand on labor goes up? My earlier look at AI and working hours asks the labor question that the capex math now depends on.

 AI Models Are the New Rebar The rebar comparison explains why cheap model tokens earn so little, the market this post separates from the frontier.

 New essays, once a month
 One email a month with new writing on quantitative finance, AI and macro strategy.
 Email address 
 Subscribe 

 No tracking . Unsubscribe anytime.
 Past issues 

 Philipp D. Dubach
