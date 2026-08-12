---
title: "Pluralistic: Model collapse (12 Aug 2026)"
url: "https://pluralistic.net/2026/08/12/insurance-value-of-biodiversity/"
fetched_at: 2026-08-12T10:18:35.324275+00:00
source: "pluralistic.net"
tags: [blog, raw]
---

# Pluralistic: Model collapse (12 Aug 2026)

Source: https://pluralistic.net/2026/08/12/insurance-value-of-biodiversity/

Today's links
One of my favorite rhetorical and analytical moves is joining things together (showing that two different, seemingly unrelated ideas are aspects of the same phenomenon) and taking them apart (resolving a paradox by demonstrating that what appears to be one, contradictory thing is actually two different things that have been lumped together).
"Taking things apart" is a very useful framework for understanding AI. How do we resolve the (seeming) paradox that some skilled workers report wonderful results from their work with AI, while others are full of dire warnings about the lurking defects in their AI-assisted outputs? Simple: the first group are "centaurs" (humans who are assisted by machines) and the second are "reverse centaurs" (humans who have been pressed into service as peripherals for machines):
https://pluralistic.net/2025/12/05/pop-that-bubble/#u-washington
What are we to make of the people who've been fired by bosses who replaced them with AI, in light of the fact that AI is demonstrably not able to do their (former) jobs? Again, it's simple if you separate out two distinct phenomena: "AI can do your job" is the first. The second is: "Your boss is a credulous dolt who is infinitely horny for replacing lippy workers with pliable machines, which made him an easy mark for an AI salesman who convinced him to fire you and replace you with an AI that
can't
do your job":
https://pluralistic.net/2025/03/18/asbestos-in-the-walls/#government-by-spicy-autocomplete
This is also a useful move for understanding the AI investment bubble. It's not just billionaires who don't think other people are as real as they are and consequently their jobs can be done by chatbots. It's
also
billionaires who believe that bosses can be sold AI and don't care if the AI is defective, because that's your boss's problem after he buys the AI and fires you. They don't have to believe in AI in order to think it's a good investment: like an investor betting that Joe Rogan can sell millions of dollars' worth of peptides to desperate young men, they are assessing the sales potential, not the merits of the thing for sale:
https://pluralistic.net/2026/08/03/andor/#either
As useful as "taking things apart" is, "putting things together" is also a
very
important technique for assessing, critiquing and improving AI. In a
stellar
essay entitled "Temperature Zero for Culture: Why Everything Is Starting to Look the Same" by the data scientist Lauren Leek, we get a top-notch example of "putting things together":
https://laurenleek.substack.com/p/temperature-zero-for-culture-why
Leek's essay is one of those fabulous, wide-ranging, cross-disciplinary pieces, touching on urban design, music trends, synthetic LLM crowds, Netflix recommendation algorithms, and several other subjects, all seeking to resolve a(nother) (seeming) paradox: how is it that we have so much
potential
variety, but
everything
is so manifestly
the same
?
The answer is complicated and nuanced, but Leek's foundational point is that in a data-driven society, "predictions" are self-fulfilling prophecies. As Leek puts it: "Once prediction shapes the choices in front of us, we lose the ability to tell the difference between what people wanted and what the system made easy to want."
This is a pervasive issue across many domains. Leek says that economists call it "performativity," while machine learning researchers call it "model collapse" and urbanists call it "placelessness."
"Performativity" describes how, once a market has been modeled by economists, that model becomes the foundation for economic policy, which pushes the market to conform to the model:
https://press.princeton.edu/books/paperback/9780691138497/do-economists-make-markets
"Model collapse" describes how machine learning models that are trained on their own predictions become incredibly bland, with all variety disappearing from the system's predictions:
https://pluralistic.net/2024/03/14/inhuman-centipede/#enshittibottification
This is hugely consequential: it's why bias proliferates through predictive policing algorithms: train a model with data from racist stop-and-frisks and it will predict that all the weapons and drugs in a city are to be found in Black and brown peoples' pockets. Turn those predictions into recommendations telling cops where to go look for weapons and drugs and they will double down on racist stops, producing even more biased training data, which turns into still more bias in the predictions:
https://hrdag.org/2016/10/10/predictive-policing-reinforces-police-bias/
"Placelessness" is the urbanist's name for "when everywhere optimises toward the same template." I think of it as Flinstones Syndrome, where the same background is looped behind Fred and Barney as they drive through Bedrock. In New York City, it's Citibank-bodega-Chipotle-Walgreens; in the Chicago suburbs, it's the strip malls with a Chili's, a gas station, and a big box store.
Leek proposes that these are all expressions of the same underlying phenomenon, a failure mode of data science that takes a world of "granular personal data" and arrives at a world where "personalisation produc[es] more sameness."
To these excellent examples, I'd add another one, from the world of monetary policy: Goodhart's Law, which holds that "When a measure becomes a target, it ceases to be a good measure":
https://en.wikipedia.org/wiki/Goodhart%27s_law
Goodhart's Law captures a wide variety of phenomena. When Google first deployed Pagerank, they showed that by counting the inbound links to all the pages on the web, you could extract a signal about which pages were most important (because there was no reason to link to a page unless you found it noteworthy).
But once Pagerank became the dominant means by which web users found pages, counting links stopped being useful: first, because people used Pagerank to find the best pages and link to them, making it impossible for new pages to get the inbound links needed to supersede incumbent pages; and second, because it's easy for fraudsters to create inbound links for low-quality pages in bulk, once there's a reason to do so.
Counting inbound links was a world-beating
retrospective
way of predicting which page would best match a searcher's query, but once it shaped the world it sought to analyze, it ceased to be a good
prospective
way to predict which page would best match your queries.
Leek is a brilliant data scientist and an even better science communicator, with a knack for crisp, readily understood explanations. How can a world of granular, highly varied data turn into a world of homogeneous choices? Simple: start with a set of items ("cuisines, genres, shop types") and a standard algorithm for sorting them. Let users choose from those recommendations. The mode (average) of those choices "gets shown more, so it gets picked more, so the model grows more confident the mode is what people want, and the tails starve." Run this for a few rounds and the evenly distributed catalog of choices "collapses onto one dominant option."
This is intrinsic in the choices we make in designing recommendation algorithms, tilting them towards the likelihood of a successful recommendation. A recommender that wants to succeed every time will make the safest possible recommendations, "so an algorithm that is uncertain about you, and it is always at least a little uncertain, hedges toward the average."
Then she busts out a beautiful,
perfect
little statistics aphorism: "Personalisation under a standard loss function is regression to the collective mean with extra steps." That is to say, "regression to the mean" (the tendency of varied things to become more standardized) cannot be avoided with the standard personalization algorithm. That algorithm is going to play it safe, showing you things that are broadly palatable, and because your choices are constrained to the average, you will choose average things.
This is how recommendation systems – and other analytical tools that produce predictions that are then turned into action – force so many diverse phenomena (streets, markets, media recommendations) into sameness. The fact that these recommenders are self-fulfilling prophecies means that "they don't have to be
right
," only "listened to."
This explains the sameness of so many of London's high streets. Leek examines 640 shopping streets, characterizing 18,000 food places spread out across them, flagging all the chain restaurants. Her analysis shows that any two London streets will, on average, share about half of their "food profile."
Obviously, this is most pronounced on streets with chain outlets, and it doesn't take that many chain outlets before a street's sameness shoots up: "A relatively small number of repeated names is enough to make otherwise different streets resemble one another more." So why do streets with chains resemble one another so much? Because the chains use an algorithm (weighting footfall, proximity to train stations, demographics, and competitors) to decide where to put their restaurants. If a street with a Gail's Bakery on it feels like every other street with a Gail's Bakery, that's because Gail's only puts its restaurants in places that have highly similar characteristics, measured to a high degree of accuracy and controlled by a narrow set of tolerances.
In other words, every street that
feels
like it should have a Gail's will
eventually
get a Gail's, whereupon that street will feel even more like all the other streets that have a Gail's, because it will share one more common factor with those other streets (a Gail's).
Leek points here to her earlier work on pub closures in the UK. The UK has experienced an epidemic of pub closures, with thousands of pubs disappearing since 2016:
https://laurenleek.substack.com/p/britain-lost-14000-third-places-they
Her research found that the biggest predictor of a pub surviving was its similarity to the median pub; which is to say that the more distinctive a pub was, the more "character" it had, the more likely it was to close. Pubs that are different from the average pub are harder to categorize, which means they're harder for a bank manager to assess for creditworthiness or for a landlord to justify extending a long-term lease to. The algorithms used to allocate capital and real estate are
also
recommenders, and they
also
drive variety out of the system.
This same phenomenon acts on culture. In an age of music recommendation algorithms, hit songs are changing; today's songs use a smaller vocabulary of unique words and repeat those words more often:
Vocabulary richness, distinct words relative to length, has fallen by more than a quarter since the early 1960s, while the share of repeated lines has climbed by nearly a third. The modern hit says less and says it more often, because the hook that works gets repeated.
But that's not the whole story! While each song resembles
itself
more ("saying less more often"), within that constraint, there's far
more
variety today than before: a given song's (constrained) vocabulary has grown
more
distinct when compared to all the other songs' vocabularies. Songs repeat the words they use, but the words repeated in songs are getting more different.
For Leek, this is the key to understanding the whole phenomenon and (more importantly)
doing something
about it. Music recommendation systems optimized for a singable hook, but did not optimize on any of the other variables in songs, so those dimensions acquired a broader range, even as the optmized variable got flatter and narrower.
This means that the tendency of recommenders to "flatten the world" isn't a single blunt outcome: it depends on which dimension we choose to flatten through recommendation, and
who
chooses to flatten that dimension.
A media recommender optimizes for consumption, showing you a tractable set of things it believes you'll watch, read or listen to. When you choose from among this limited set, the recommender takes note of that fact and shows you more of the same, pushing everything to a greige median. All the movies, books and songs you might have liked that were omitted from that initial set are excluded from being recommended in the future. The features of that media that you might have appreciated "decay out of consideration." They are never tested for desirability. The model collapses.
How badly does it collapse? Leek cites Movietweetings' data on which movies people watch: out of a million public movie ratings, half relate to the top 2% of movies in the set. There's 38,000 films in the set, but just
380
titles account for 40% of the ratings. Leek argues (persuasively) that this isn't because recommenders are good at "knowing your taste" – rather, they are good at "narrowing the menu."
Leek relates this to her work on creating LLM "personas" – synthetic populations meant to mimic the tastes and proclivities of real groups of people, that you can interrogate "before you spend money asking actual humans." While this would be useful for many applications, "it fails in exactly the way this whole essay is about."
Leek went to enormous lengths to reproduce the traits that make people interesting to study in aggregate, painstakingly replicating the ways that social connections, psychological outlook and demographic factors predict people's beliefs. The result was a set of LLM personas with "elaborate stories" about how they differed from one another, but whose survey responses about planned actions were homogeneous in a way that real populations are not.
This, Leek writes, is the same force that homogenizes other data-driven predictors. Because she'd ordered her LLM to reproduce the statistically validated relationships between different factors that predict a person's beliefs, each synthetic persona was a homogenized average. It's like the paradox of "The Average Man," where military uniforms sized to the average of all service personnel fit no one, because no one is average:
https://archive.org/details/DTIC_AD0010203
The thing is (as Leek points out) the idea that synthetic personas are a good way to understand the preferences of a real population is not a harmless delusion: it's a product that's being actively sold to governments, campaigning politicians and marketers. It's a self-fulfilling prophecy that drives governance, political campaigns and product design to the same homogeneous median that is making every shopping street in London feel the same.
This matters. As Leek writes, ecologists have long understood the importance of variety for systemic resilience: they call it "the insurance value of biodiversity." A diverse system has reservoirs of species and variation that may not be optimized for how things stand
now
, but that can move into niches created when things
change
in ways that lay waste to the previously dominant organisms. As anyone whose favorite banana went extinct can tell you, homogeneity
works
well, but diversity
fails
well:
https://en.wikipedia.org/wiki/Gros_Michel
The brittleness of algorithm-induced homogeneity is compounded by the fact that recommenders obscure the
true
preferences of people. If you watch two Scandinavian crime dramas after Netflix recommends them to you, it will keep showing you more Scandy crime for the next decade – even if there's another kind of programming that you'd vastly prefer (if only you knew about it). This means that decision-makers who choose which shows will get made in the future will keep on funding their safe Danish detectives, to the exclusion of whatever might emerge from the same weird attractor that produced the K-Pop Demon Hunter fortune.
Transpose this failure mode onto states, bank managers and landlords, and we see whole ranges of policies, businesses and activities that never come into existence, despite the popularity, prosperity and joy they might bring us.
But Leek doesn't end with this worrisome note. Instead, she identifies this whole thing – model collapse, placelessness, performativity, even Goodhart's Law – as an expression of one of the best-understood tradeoffs in computer science: "exploration vs exploitation":
Any system learning from feedback has to divide its effort between exploiting what already scores well and exploring options it hasn’t tried, in case they’re better.
Computer scientists have long understood that focusing on exploitation to the exclusion of exploration is a trap that locks you into "the first decent option" so you can never discover the best one.
Which means that this algorithmic homogeneity has a well-understood corrective: "forcing exploration back in." The problem is that markets
hate
this kind of exploration. A company that lives and dies by how many clicks it gets is never going to sacrifice 20% of its traffic by showing its users weird, untested options that score worse than the median because these weird things have never had a chance to prove that they are desirable.
This is a classic market failure, and, as Leek points out, there are regulatory responses in the UK (the Digital Markets, Competition and Consumers Act) and the EU (the Digital Services Act), both of which require the largest platforms to open up their recommendation systems, but so far, regulators have focused on "online harms" rather than variety (though the DSA does require platforms to offer algorithmic recommendations that are not based on your personal traits).
Leek identifies this willingness of states to set conditions for algorithm design as a means by which "exploration" can be forced back into the system. She's also bullish on interoperability, so that users can leave platforms with bad recommenders, without losing access to their media or social circles. As she writes, "the deepest discipline on a feed that has trapped you is the credible ability to leave it and take your data with you." I couldn't agree more:
https://pluralistic.net/2023/01/08/watch-the-surpluses/
She's less hopeful about individual responses. Demanding that you be an "adventurous consumer" is a way of letting systems off the hook. When every street has the same restaurants and every bookshop has the same books and the people in your life are all locked into one of two social media platforms, "choosing wisely" only gets you so far. Shopping isn't politics!
https://pluralistic.net/2026/05/21/purity-culture/#stop-fucking-that-chicken
Leek is a superb writer. After reading this piece yesterday, I sent it to half a dozen people and then read everything else in Leek's newsletter archives. Not only is it all brilliant, but I also realized that she'd written one of the most memorable articles about cities and platforms I've read in the last year, "How Google Maps quietly allocates survival across London’s restaurants – and how I built a dashboard to see through it":
https://laurenleek.substack.com/p/how-google-maps-quietly-allocates
I should have added Leek's newsletter to my RSS reader when I read that last December. I've rectified that oversight! What a fantastic thinker, scientist and communicator! If she isn't being relentlessly pestered by editors and literary agents offering her a book deal, then it really does prove that the recommender systems are elevating the bland median over the thoroughly, delightfully spiky outliers.
Hey look at this (
permalink
)
Object permanence (
permalink
)
#25yrsago Awful, stupid Wired report on Dutch hacker camp
https://web.archive.org/web/20011007084604/https://www.wired.com/news/culture/0,1284,46033,00.html
#25yrsaog Excellent NYT story about the internal contradictions of the DMCA
https://memex.craphound.com/2001/08/13/excellent-nyt-story-about-the/
#20yrsago Our faulty intuition about open systems
https://www.ft.com/content/64167124-263d-11db-afa1-0000779e2340
#20yrsago Defending against the last plot won’t save us from the next one
https://www.schneier.com/blog/archives/2006/08/terrorism_secur.html
#20yrsago NBC: Hair-gel terrorists posed no risk last week
https://web.archive.org/web/20060813194630/http://www.msnbc.msn.com/id/14320452/
#15yrsago AT&T merger leak: it’s all about raising prices and reducing competition
https://web.archive.org/web/20110920222524/http://www.broadbandreports.com/shownews/Leaked-ATT-Letter-Demolishes-Case-For-TMobile-Merger-115652
#10yrsago What’s inside a Tiki Bird?
https://miehana.blogspot.com/2016/08/fancy-feathers-restoring-tiki-room-birds.html
#5yrsago End of the line for Reaganomics
https://pluralistic.net/2021/08/13/post-bork-era/#manne-down
#5yrsago Smart cities are neither, 2021 edition
https://pluralistic.net/2021/08/13/post-bork-era/#our-streets
#1yrago Maga's boss class think they are immune to American carnage
https://pluralistic.net/2025/08/13/then-they-came-for-me/#boss-politics
Upcoming appearances (
permalink
)
Recent appearances (
permalink
)
"The Reverse-Centaur's Guide to AI," a short book about being a better AI critic, Farrar, Straus and Giroux, June 2026
https://us.macmillan.com/books/9780374621568/thereversecentaursguidetolifeafterai/
"Canny Valley": A limited edition collection of the collages I create for Pluralistic, self-published, September 2025
https://pluralistic.net/2025/09/04/illustrious/#chairman-bruce
"Enshittification: Why Everything Suddenly Got Worse and What to Do About It," Farrar, Straus, Giroux, October 7 2025
https://us.macmillan.com/books/9780374619329/enshittification/
"Picks and Shovels": a sequel to "Red Team Blues," about the heroic era of the PC, Tor Books (US), Head of Zeus (UK), February 2025 (
https://us.macmillan.com/books/9781250865908/picksandshovels
).
"The Bezzle": a sequel to "Red Team Blues," about prison-tech and other grifts, Tor Books (US), Head of Zeus (UK), February 2024 (
thebezzle.org
).
"The Lost Cause:" a solarpunk novel of hope in the climate emergency, Tor Books (US), Head of Zeus (UK), November 2023 (
http://lost-cause.org
).
"The Internet Con": A nonfiction book about interoperability and Big Tech (Verso) September 2023 (
http://seizethemeansofcomputation.org
). Signed copies at Book Soup (
https://www.booksoup.com/book/9781804291245
).
"Red Team Blues": "A grabby, compulsive thriller that will leave you knowing more about how the world works than you did before." Tor Books
http://redteamblues.com
.
"Chokepoint Capitalism: How to Beat Big Tech, Tame Big Content, and Get Artists Paid, with Rebecca Giblin", on how to unrig the markets for creative labor, Beacon Press/Scribe 2022
https://chokepointcapitalism.com
"The Post-American Internet," a geopolitical sequel of sorts to
Enshittification
, Farrar, Straus and Giroux, 2027
"Unauthorized Bread": a middle-grades graphic novel adapted from my novella about refugees, toasters and DRM, FirstSecond, April 20, 2027
"Enshittification, Why Everything Suddenly Got Worse and What to Do About It" (the graphic novel), Firstsecond, 2027
"The Memex Method," Farrar, Straus, Giroux, 2027
Today's top sources:
Currently writing:
“Once Is Enemy Action,” a science fiction novel about the origins of modern technofascism. Today's words: 546 (4161 total).
"The Post-American Internet," a sequel to "Enshittification," about the better world the rest of us get to have now that Trump has torched America. Fourth draft completed. Submitted to editor.
A Little Brother short story about DIY insulin PLANNING
This work – excluding any serialized fiction – is licensed under a Creative Commons Attribution 4.0 license. That means you can use it any way you like, including commercially, provided that you attribute it to me, Cory Doctorow, and include a link to pluralistic.net.
https://creativecommons.org/licenses/by/4.0/
Quotations and images are not included in this license; they are included either under a limitation or exception to copyright, or on the basis of a separate license. Please exercise caution.
How to get Pluralistic:
Blog (no ads, tracking, or data-collection):
Pluralistic.net
Newsletter (no ads, tracking, or data-collection):
https://pluralistic.net/plura-list
Mastodon (no ads, tracking, or data-collection):
https://mamot.fr/@pluralistic
Bluesky (no ads, possible tracking and data-collection):
https://bsky.app/profile/doctorow.pluralistic.net
Medium (no ads, paywalled):
https://doctorow.medium.com/
Tumblr (mass-scale, unrestricted, third-party surveillance and advertising):
https://mostlysignssomeportents.tumblr.com/tagged/pluralistic
"
When life gives you SARS, you make sarsaparilla
" -Joey "Accordion Guy" DeVilla
READ CAREFULLY: By reading this, you agree, on behalf of your employer, to release me from all obligations and waivers arising from any and all NON-NEGOTIATED agreements, licenses, terms-of-service, shrinkwrap, clickwrap, browsewrap, confidentiality, non-disclosure, non-compete and acceptable use policies ("BOGUS AGREEMENTS") that I have entered into with your employer, its partners, licensors, agents and assigns, in perpetuity, without prejudice to my ongoing rights and privileges. You further represent that you have the authority to release me from any BOGUS AGREEMENTS on behalf of your employer.
ISSN: 3066-764X
