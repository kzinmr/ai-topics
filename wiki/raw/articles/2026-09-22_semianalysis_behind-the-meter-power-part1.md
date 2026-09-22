---
source_url: https://newsletter.semianalysis.com/p/what-is-so-hard-about-behind-the
ingested: 2026-09-22
sha256: 550e2caa24b66bc118478f114eddb95265bab33b41b9db50b0d796fc61ccf58c
---

# What is So Hard About Behind-The-Meter Power For Datacenters? Part 1

**Source:** SemiAnalysis (newsletter.semianalysis.com)
**Authors:** Ellie Holbrook, Robert Boswall, Jeremie Eliahou Ontiveros, Dylan Patel (+1)
**Date:** 2026-09-10 (paywalled; captured excerpt below)

=====TEXT=====
What is So Hard About Behind-The-Meter Power For Datacenters? Part 1

Subscribe Sign in

What is So Hard About Behind-The-Meter Power For Datacenters? Part 1
Dumb Science Experiments vs. Money Printing Machines
Ellie Holbrook , Robert Boswall , Jeremie Eliahou Ontiveros , and 2 others
Sep 10, 2026
∙ Paid

136

2

12

Share

Last year we were the first to call out Onsite Gas Generation as the primary method adopted by AI Labs and Hyperscalers to solve power constraints . Our positive view was far from being consensus: behind-the-meter primary power solutions have been called all sorts of names, such as “ science experiments ”, “ Dark Gigawatts ”, and “ literally the dumbest thing that human beings have ever attempted to do ”!
But since then, that supply chain has witnessed a massive acceleration. Our Energy Model now tracks 75GW of firm, binding orders in the supply chain only for for behind-the-meter AI compute - of which ~20GW alone ordered in Q2 2026. What started as an Elon Musk experiment is now mainstream for every single AI Lab and hyperscaler. To be clear, this data does not include the hundreds of GWs of speculative, baseless announcements that many other analysts track in their numbers - we only focus on binding orders received by OEMs specifically serving BTM AI compute, tracked at the project-level.

Sources: SemiAnalysis Energy Model ; sales@semianalysis.com
The path from firm equipment order to delivered project is still long and challenging. There is substantial execution risk and that’s what we’ll focus on in this report. But the industry is more experienced than you’d think: by the end of the year, ~3GW of operational US datacenter IT capacity will be powered behind-the-meter, and that number will experience multiple straight years of triple-digit growth. Our Energy and Datacenter models account for all potential delays, as we’ve explained in depth in our piece Stop Saying Half of 2026 US Datacenter Capacity is Canceled .

Source: SemiAnalysis Energy Model , sales@semianalysis.com
Some of the most strategic projects developed by leading AI labs and hyperscalers are relying on behind-the-meter, supporting hundreds of billions of future revenue. Adoption has never been more broad-based. A few examples:
In 2026 year-to-date, Microsoft has signed over 5GW of behind-the-meter nameplate capacity, of which 2.7GW with Joulent & Chevron, and well over 2GW through turnkey datacenter leases with companies like Crusoe. That 5GW encompasses a broad range of different types of power equipment; full breakdown available to our Energy Model subscribers .

Google, historically the most reluctant to onsite gas, is deploying 930MW of off-grid aeroderivative turbines in a flagship campus in Armstrong County. In addition, the Search Giant will deploy 900MW of Bloom Energy Fuel Cells in Wyoming - as we called out back in February 2026 as a huge positive for Bloom Energy. They’ll be paired with >1GW of Mitsubishi J-class turbines.

Both Anthropic and Meta have signed 300-500MW deals with Enchanted Rock, a supplier of 0.5MW gensets built around a 21.9-liter V12 gas engine. Separately, Anthropic’s flagship campus in Texas, backstopped by Google, will also deploy over 1.5GW of off-grid generation; full breakdown of Anthropic’s exact datacenter facilities available to our Datacenter Model subscribers.

OpenAI will imminently start operations in its flagship off-grid 1.4GW (IT capacity) campus in Shackelford County, TX, using over five hundred 4.25MW Jenbacher J624 engines . We show below a portion of the campus. Combined with their 1.3GW IT site in New Mexico, that represents over $150B of contracted spending that OpenAI signed with Oracle relying on behind-the-meter power.

Sources: SemiAnalysis Datacenter Model ; SemiAnalysis Energy Model ; Sales@semianalysis.com
Why is this happening, and why have many energy experts been so wrong? It comes down to understanding AI economics. We’ve discussed this at length in many other articles and in our Tokenomics Model . As a quick reminder, the value of megawatts for end-users is skyrocketing. A power plant supporting an islanded 1GW IT datacenter typically costs ~$5B. In today’s environment, inference API revenue can yield $100B per GW per year, at 90%+ gross margins. Paying 2x more money or accepting 30% lower efficiency for faster speed of deployment becomes a no-brainer . Said differently, Anthropic and its peers can pay back the value of a power plant in 20 days of inference revenue . As we discussed six months ago, most of the value in the AI infrastructure stack is shifting to frontier model developers .
The grid simply cannot keep up with demand. Building new generation can easily take over five years, and on the demand-side, interconnecting a datacenter takes years. Read more in our article on US Grid Constraints .

Sources: SemiAnalysis Tokenomics Model ; SemiAnalysis Inference Simulator ; sales@semianalysis.com
That market context is overwhelmingly positive for behind-the-meter power to overcome such constraints. But these datacenter onsite power solutions are increasingly divergent from their grid-connected peers. As predicted a year ago, winners have not only been the incumbents like GEV and Siemens Energy. The biggest beneficiaries have been the dozens of suppliers of reciprocating engines, of various shapes and forms, with solutions from 0.5MW per unit to 20MW per unit being adopted at scale. A year ago, we counted 12 distinct manufacturers that had secured multi-hundred-MW datacenter off-grid orders; but today that count is 22 and will continue to grow. Our Energy Model tracks quarter-by-quarter manufacturing capacity, orders, deliveries, and availability for over 30 OEMs.

Sources: SemiAnalysis Energy Model ; sales@semianalysis.com

Subscribe

While the bright side of this is innovation, the flip side is the looming execution challenges facing the industry. Many of these things have never been done at this scale or speed. Cracks are starting to emerge. Permitting delays have caused high-profile sites, like Oracle Project Jupiter and Nebius New Jersey, to perform emergency pivots to less polluting alternatives (Bloom fuel cells). Pipeline delays have also impacted Oracle’s 1.3GW IT Project Jupiter (as our Energy Model called out in May 2026 , well before the headlines). Market chatter of reliability issues is increasingly frequent. Labor shortages are surging. Design and up-time considerations are challenging and slowing down some FIDs. A secondary market for turbines is starting to emerge as a result of firm orders tied to failed projects.
In today’s report, we dive into the world of “datacenter microgrids”. We consider the challenges and doubts regarding the BTM buildout and look at how it is being done.
What even is ‘Behind-the-Meter’. Detailing the ways a datacenter can relate to the grid, between primary and back-up power; including when something is a phony microgrid. How does one define behind-the-meter?

How projects succeed or fail. We lay out the six key stages & challenges of BTM projects: contracts & bankability, permitting, fuel supply, equipment procurement, workforce, and the physics of operating without a grid-connection. We start with the financing wall, with chicken-and-egg situations being increasingly common for developers, and the rise of the new “BTM utilities”.

Where we go from here. ‘To grid or not to grid’; what happens to these plants when grid power finally arrives; export-to-grid, stay primary power, become backup, or move elsewhere. At the same time what happens with these order books and the manufacturing capacity that has scaled so hard to meet the moment. We’ll also give our view on the implications for BTM in Texas.

Over recent months we have published significant research for our Energy Model clients, laying out winners & losers in the equipment landscape (turbine, recips, fuel cells), contractors like AGX, BoP equipment like MV UPS systems and how new LVRT regulations could have negative impact to certain huge industrial companies. Behind the paywall of this report, we have included some of this work for Substack subscribers now to enjoy.
Conferences: in September members of SemiAnalysis’ Energy Model team will be at Gastech in Bangkok 14-17th; Data Center World Power in Dallas 21-23rd; Yotta in Las Vegas, and Gulf Coast Power Association in Austin, both 28-30th. Email energy@semianalysis.com and lets talk power!
We thank Michele Tarawneh from Celsius Industries for his valuable input to this report!
What even is “BTM”?

A meter is a device that counts electricity; it is stationed at the point where the project’s wires meet the grid’s wires. Everything on the grid side of that point, the substations, the pylons, the power plants, is “front of the meter”; everything on the project’s side, the switch-gear, the batteries, and onsite generators, is “behind the meter”.
There are then specific terms but in practice they get used interchangeably: “behind-the-meter”, “off-grid”, “islanded”, “co-located”, and “micro-grid”. This is frustrating and leads to common disagreements over the definitions, but one way to think about them is by connection configuration:

Source: SemiAnalysis
Grid-supplied: The grid supplies the datacenter; on-site generation is backup only. Power plants supply the public network, which supplies the datacenter.

Grid-parallel: Local generation and grid imports can both supply the datacenter. Exports are optional depending on the rights and connections.
The relative sizes of the datacenter, its local generation, and its permitted grid imports can vary substantially. ERCOT’s Withdrawal-Limited Private Use Network, or WLPUN, framework expressly accommodates on-site generation reducing the transmission capacity a large load requires.

Consider three illustrative configurations, each serving a 1,000 MW datacenter :
Grid-led: 250 MW of local generation and a 1,000 MW import limit. Local generation offsets part of grid consumption; when producing 250 MW at full datacenter load, it leaves 750 MW to import.

Plant-led, full-sized import connection: 1,200 MW of local generation and a 1,000 MW import limit. The plant can cover normal demand, while the import limit is large enough to accommodate the entire datacenter load.

Plant-led, limited import connection: 1,200 MW of local generation and a 250 MW import limit. At full load, at least 750 MW must come from local resources. Losing all local generation would require replacement supply or at least 750 MW of load reduction.

Export-only: Local generation supplies the datacenter; the grid connection permits exports but not imports to serve the load.

Off-grid: Local generation supplies the datacenter without an operating grid connection.

Net metering

In this context, net metering means netting the datacenter’s consumption against associated generation at the relevant grid-facing metering or settlement boundary. ERCOT describes it as reducing the customer’s metered consumption from the grid; it is not necessarily the retail rooftop-solar arrangement that credits exports against consumption over a billing cycle.
Freestone is an example: ERCOT reports PUCT approval in May 2026 of an arrangement between a 1,099 MW gas plant and a 760 MW datacenter in Freestone County.
Why Export-only is not Off-grid

The datacenter does not need a separate grid feeder to remain electrically connected. If its supply circuit connects into the plant’s grid-connected AC system, it is connected to the grid through the plant; the site participates in the interconnection’s frequency dynamics and shared inertial response even while exporting net power. Depending on how well run the grid is this arrangement can be beneficial to the datacenter with improved electrical reliability and quality.
Existing generation adds a regulatory distinction

Regulators can also distinguish new generation from a plant that previously supplied the grid. Texas Utilities Code §39.169, “Co-location of Large Load Customer With Existing Generation Resource,” covers certain net-metering arrangements involving an operating facility registered as a stand-alone generation resource as of September 1, 2025 ; it requires ERCOT notification and PUCT review, subject to exemptions and a deemed-approval provision.
Diverting existing output to a new load can reduce supply available to the wider grid. ERCOT says the two netting arrangements approved by May 2026 required the datacenters to reduce consumption or switch to backup, and the plants to return their full output to the grid within 30 minutes of an ERCOT instruction.
Operating states and deployment: island, bridge power, grid as backup

“Islanded” is an operating state: a grid-connected datacenter opens the breaker and runs on its own generation. Then related but separate, the Department of Energy defines a “Microgrid” as “a group of interconnected loads and distributed energy resources within clearly defined electrical boundaries that acts as a single controllable entity with respect to the grid,” and its Grid Deployment Office adds that a microgrid “can operate in either grid-connected or in island mode, including entirely off-grid applications”. In this piece, “islandable microgrid” means a grid-connected site that can separate; “off-grid microgrid” means a site with no connection at all. Many BTM projects use the term loosely, perhaps because it avoids saying “gas”.
In practice, this may change a lot over time. Many BTM projects plan for a grid connection and use BTM as a “bridge” - once the utility delivers the connection, the generators can shift into a backup role. We described this in depth the Onsite Gas Deep Dive as the most popular approach because electricity systems benefit from substantial economies of scale in both cost and reliability. xAI’s Colossus 1 in Memphis has taken this route.
Other projects plan for a grid connection that will serve as “backup”, i.e. as a new energy resource that 
