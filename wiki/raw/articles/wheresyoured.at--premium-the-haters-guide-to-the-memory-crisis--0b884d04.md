---
title: "Premium: The Hater's Guide To The Memory Crisis"
url: "https://www.wheresyoured.at/premium-the-haters-guide-to-the-memory-crisis/"
fetched_at: 2026-07-11T07:00:47.487829+00:00
source: "wheresyoured.at"
tags: [blog, raw]
---

# Premium: The Hater's Guide To The Memory Crisis

Source: https://www.wheresyoured.at/premium-the-haters-guide-to-the-memory-crisis/

Hi premium readers! I’ll be taking a week off of the premium next week — July 17 — to have some well-earned rest. This will mark only the second time I’ve missed a premium piece since I started this newsletter in June 2025, and I hope you’ll forgive me for the (short) break.
Don’t worry. Today’s piece is also an absolute banger.
Everything’s more expensive, and it’s all AI’s fault.
It really is that simple.
An AI data center is full of servers, which are in turn full of (for the most part) NVIDIA GPUs. Each NVIDIA GB300 has two B300 GPUs, the two of which have 576GB of High Bandwidth Memory (HBM, or HBM3e to be specific), and a CPU, which has 480GB of lower-power LPDDR5X RAM (the kind usually used in cellphones and other mobile devices). These systems
tend to be sold
in an
NVL72 rack with 18 compute trays, bringing us to 36 GB300s
, for a total of 20.7
terabytes
of HBM and 17 terabytes of LPDDR5X RAM, and that’s before you get to the RAM associated with the high-speed networking gear and other associated components.
Analyst estimates
have the cost of the high bandwidth memory of a single NVL72 GB300 at around $15.27 per gigabyte, for a total of around $316,000 of HBM, and while I can’t seem to find a stable source for pricing around LPDDR5X, I think a fair estimate is around $4 per gigabyte
based on this piece
, so around $68,000 worth per NVL72 rack.
At around 150kW of power draw per NVL72
, a 1GW data center (with 740MW of critical IT load) would have around 4,933 NVL7s racks — for a total of $
1.894 billion in HBM and LPDDR5X costs,
or around $2.559 million of HBM and LPDDR5X RAM per megawatt of IT load.
Oh, and each of these NVL72s can hold as much as a
petabyte
of expensive solid state storage, costing an additional tens of thousands of dollars.
Because HBM takes up more space on a wafer — the slice of semiconductor material that is etched using photolithography (
read: molten tin
) and then cut into separate dies (individual chips) — and generally has much higher margins (thanks to the triopoly of Samsung, SK Hynix and Micron), memory manufacturers are dedicating more space on their manufacturing lines to it than to regular consumer RAM, which allows (thanks to said triopoly) said manufacturers to charge effectively whatever they want for consumer RAM.
And thanks to AI —
to quote Tom’s Hardware and Counterpoint Research
— NVIDIA is buying that LPDDR5X RAM at the scale of an Apple or a Samsung:
"The bigger risk on the horizon is with advanced memory as Nvidia's recent pivot to LPDDR means it is a customer on the scale of a major smartphone maker — a seismic shift for the supply chain which can’t easily absorb this scale of demand," said MS Hwang, research director at Counterpoint Research.
The net result is pretty simple: every single consumer electronic of any kind is getting more expensive.
Valve’s Steam Machine console debuted at a 30% higher price point than planned
,
Apple hiked the prices of its MacBooks and iPads
and
will likely have to do the same for its next iPhone
.
Nintendo
,
Microsoft
and
Sony
increased the cost of their consoles, and the
PS5
and
Xbox Series
now cost more today than they did when they first retailed, almost six years ago.
On the Android front,
Samsung has bumped the price of its Galaxy smartphones
, and manufacturers in this space (which tends to have smaller margins than those enjoyed by Apple) are likely to
limit the number of new devices shipping with 16GB of RAM, as well as re-introduce models with 4GB of RAM
.
Meanwhile, memory manufacturers are having record quarters,
with Micron’s revenue quadrupling year-over-year in Q3 2026
and its gross margin improving by
ten percent (from 74.9% to 84.9%) quarter-over-quarter,
and
Samsung’s profits growing from $38 billion to $59 billion quarter-over-quarter
thanks to the spiralling cost of revenue caused by…well…the companies setting the price of memory at whatever they’d like.
This is a problem caused by the fact that these three companies — SK Hynix, Micron and Samsung — produce more than 90% of the world’s RAM,
which is why there’s a price fixing lawsuit against them
, per Polygon:
The class action lawsuit filed by 14 individuals and three businesses accuses Samsung, SK Hynix, and Micron of conspiring to fix prices and supply of DDR3 and DDR4 RAM, resulting in higher costs. “This lawsuit seeks to recover for—and stop—concerted anticompetitive behavior by three oligopolists in the market for dynamic random access memory, more commonly called DRAM,” the opening line of the suit reads.
The suit says that the firms have “fixed supply and prices for DRAM, engaging in conduct that makes no economic sense absent collusion and that has driven up the price of conventional DRAM (sometimes called commodity DRAM) approximately 700% in a four-year period.”
To be clear, HBM is
more expensive
to make than regular RAM, and takes up significantly more space (
about 4x more
) on the wafer, but because of the incredible demand for AI servers, Samsung, SK Hynix, and Micron can charge effectively whatever they want for it,
much like they are for the regular RAM
that’s in short supply. The same is becoming increasingly true for the solid state storage that these companies (and others like Sandisk) sell too.
Now, you may think it’s a little rich to suggest that memory manufacturers are colluding to rig their prices, perhaps a little
judgmental
, and you’d be
wrong
because they’ve
done it before.
Quoting
Polygon
again
:
The lawsuit points out that between 1998 and 2002, these same three companies, Samsung, Hynix (the predecessor of SK Hynix), and Micron, took part in a criminal conspiracy to fix the prices of DRAM sold to major American computer companies. After the Department of Justice prosecuted the case, Samsung pleaded guilty and paid a $300 million fine, Hynix pleaded guilty and paid $185 million, and Micron avoided a fine by reporting the conspiracy and cooperating. As a result, several Samsung executives went to prison. The trio of companies was also investigated by the Chinese government during a RAM price spike between 2016 and 2018.
To be clear, I am not saying — nor can I prove — that there is any kind of price-fixing or collusion going on. Nevertheless, there are three companies that effectively make all the world’s RAM, all raising prices at the same time, all seeing record profits, all riding high at a time when everybody else is suffering as a direct result.
The Wall Street Journal put it best
:
We are witnessing an enormous transfer of cash from the providers of AI—and, perhaps one day, AI users—to the memory-chip makers. Profit shifts of this scale are rare events, and investors should be paying attention to where the money’s coming from, where it’s being spent and how long it will keep flowing.
In the quarter ending May 28, Micron increased prices for DRAM chips more than 60% on the previous three months, while increasing shipments by a low single-digit percentage, it said this week. Prices for NAND flash memory, also used in data centers, jumped more than 80%.
What makes this particular memory crisis so distinctly dangerous is that it isn’t a result of
consumer demand
so much as it is
capital expenditures from very large companies making bets that don’t connect with reality.
Microsoft, Google, Amazon, and Meta aren’t spending $765 billion in capex in 2026
because of rapid demand
by consumers
for AI services, but
a desperation caused by a lack of hypergrowth ideas
,
circular financing with Anthropic and OpenAI
, and a vague concern that if
they stop spending
that
the other guy will do something as a result.
As I discussed earlier in the week
, nobody can make a compelling case for building more data centers other than “we must do so, because of AI.” Nobody is having trouble accessing ChatGPT, Claude or another major AI service because of a lack of compute, outside of Anthropic and OpenAI’s continual rapacious
hunger
for more compute that doesn’t ever seem to involve them turning away business. While price increases generally help moderate demand for goods or services, none of that matters when you have four companies willing to spend a trillion dollars a year
on the off chance that they might get something out of it
.
As a result, Micron, Samsung, and SK Hynix can charge effectively as much as they want, and NVIDIA and others building black holes for AI capex can then pass those costs onto Microsoft, Google, Amazon, and Meta, who have given themselves a blank check to build whatever it is that they think will come out of the large language model era.
Put another way, the capex spend of four of the largest companies of the world —
all of whom are now funding their capex using debt
— has now led to the single-largest increase in the price of consumer electronics in history, for the most part thanks to one company, NVIDIA, becoming
the largest purchaser of HBM in the world
because those four companies are buying so many GPUs.
To give you an idea of how bad that is,
NVIDIA takes up roughly 65% of all high bandwidth memory, with the other 35% (mostly) going to specialist ASICs from Google and Amazon, and AMD’s Instinct line of AI GPUs.
This is a unique — and uniquely dangerous — bubble, because demand isn’t based on
actual revenues
or
events happening outside of those in the imaginations of Sundar Pichai, Mark Zuckerberg, Andy Jassy and Satya Nadella.
They didn’t start buying these GPUs because consumers demanded them. In fact, they did so without really checking whether consumers gave a shit, which is why I’m so worried about what comes next.
Only 23% of total DRAM wafers are taken up by HBM
, but it’s accounting for a remarkable chunk of revenues, at least for SK Hynix,
where it took up 40% of all DRAM sales back in Q3 2025
, the most-recent number I can get.
While I can’t find definitive numbers from Samsung or Micron, the situation is bad no matter which way you spin it. Either they’re increasingly-relying on HBM as a revenue driver to the point it’s crowding out the revenue from their other DRAM businesses (making them dependent on GPU and ASIC revenue), or their revenues are spiking because they’re able to crank up the cost of DRAM.
This is setting everybody up for a dramatic and painful collapse, largely based on the strange nature of how memory is built and sold, unless cooler heads prevail and capex doesn’t accelerate based on hopium.
What happens when hyperscalers reduce their capex, or
when banks stop issuing data center debt
? NVIDIA stops needing all that HBM, which means any and all capex dedicated to expanding manufacturing  infrastructure to produce more HBM — which is not particularly valuable outside of AI GPUs — will have been built to capture demand that doesn’t exist. While that capacity could be re-engineered to make useful DRAM with mass appeal, doing so will also drag down the profits of every memory manufacturer in the process, creating a supply glut the likes of which we’ve never seen in history.
The memory industry has gambled its financial future on the idea that there’s near-infinite amounts of capital available for data center capex, adjusting its supply chains and fabs to focus on scooping up demand that’s increasingly only made possible by the availability of debt. Microsoft, Google, Amazon and Meta have turned NVIDIA into a single point of failure for the entire tech industry, creating a painful present for consumers and a brutal future for suppliers, all because they decided to spend more than a trillion dollars on a dead end industry.
The longer it takes for hyperscaler capex to retract, the more expensive everything becomes. The more GPUs that get sold, the more capacity that gets put toward high bandwidth memory, and the more that Micron, SK Hynix and Samsung can charge for it, which makes it more expensive to buy AI GPUs, which increases the amount that hyperscalers are
spending
on AI capex for effectively the same amount of gear. The longer that hyperscalers sustain this pace, the larger the return needs to be, and at this point,
none of them
have disclosed their AI revenues, which heavily suggests there’s yet to be a dollar of profit.
Yet the more they commit, the more committed they have to be. Pulling back at this point will prove to the markets that they’ve committed to too much capacity. Yet
not
pulling back means that hyperscalers will continue to turn their free cash flows negative in pursuit of an indeterminate goal. It’s a vicious cycle made worse by the fact that every spin of the capex wheel increases the price of
just about every consumer electronic in the world
, creating a market-wide inflation for what amounts to a speculative asset bubble.
And If even one hyperscaler cuts their capex, the cartel-like memory industry is in for a nightmare scenario, one larger and uglier than any they’ve ever faced.
In the end, it all comes down to whose problem this high bandwidth memory becomes. Will SK Hynix, Samsung, and Micron have already built the RAM and face waves of cancellations, resulting in a bunch of fallow inventory it can’t use or sell? Or will they already have shipped it off to NVIDIA and ASIC builders, only for it to sit in warehouses waiting for the day it can finally be melted down?
Who will end up holding the bag? The cartel of horrible fab-gargoyles, Jensen Huang’s Wallet Inspection Firm, one of the four simpleton hyperscalers, Broadcom, or one of the Taiwanese ODMs?
Just to be clear: everybody loses, unless the AI bubble continues in perpetuity.
This is the Hater’s Guide To The Memory Crisis — and the terrible tale of the boom-and-bust memory industry.
