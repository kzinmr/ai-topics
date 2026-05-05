---
title: "Measurement, benchmarking, and data analysis are underrated"
url: "https://danluu.com/why-benchmark/"
fetched_at: 2026-05-05T07:01:30.237724+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Measurement, benchmarking, and data analysis are underrated

Source: https://danluu.com/why-benchmark/

A question I get asked with some frequency is: why bother measuring X, why not build something instead? More bluntly, in a recent conversation with a newsletter author, his comment on some future measurement projects I wanted to do (in the same vein as other projects like
keyboard vs. mouse
,
keyboard
,
terminal
and
end-to-end
latency measurements), delivered with a smug look and a bit contempt in the tone, was "so you just want to get to the top of Hacker News?"
The implication for the former is that measuring is less valuable than building and for the latter that measuring isn't valuable at all (perhaps other than for fame), but I don't see measuring as lesser let alone worthless. If anything, because measurement is,
like writing
, not generally valued, it's much easier to find high ROI measurement projects than high ROI building projects.
Let's start by looking at a few examples of high impact measurement projects. My go-to example for this is Kyle Kingsbury's work with
Jepsen
. Before Jepsen, a handful of huge companies (the now $1T+ companies that people are calling "hyperscalers") had decently tested distributed systems. They mostly didn't talk about testing methods in a way that really caused the knowledge to spread to the broader industry. Outside of those companies, most distributed systems were,
by my standards
, not particularly well tested.
At the time, a common pattern in online discussions of distributed correctness was:
Person A
: Database X corrupted my data.
Person B
: It works for me. It's never corrupted my data.
A
: How do you know? Do you ever check for data corruption?
B
: What do you mean? I'd know if we had data corruption (alternate answer:
sure, we sometimes have data corruption, but it's probably a hardware problem and therefore not our fault
)
Kyle's early work found critical flaws in nearly everything he tested, despite Jepsen being much less sophisticated then than it is now:
Redis Cluster / Redis Sentinel
: "we demonstrate Redis losing 56% of writes during a partition"
MongoDB
: "In this post, we’ll see MongoDB drop a phenomenal amount of data"
Riak
: "we’ll see how last-write-wins in Riak can lead to unbounded data loss"
NuoDB
: "If you are considering using NuoDB, be advised that the project’s marketing and documentation may exceed its present capabilities"
Zookeeper
: the one early Jepsen test of a distributed system that didn't find a catastrophic bug
RabbitMQ clustering
: "RabbitMQ lost ~35% of acknowledged writes ... This is not a theoretical problem. I know of at least two RabbitMQ deployments which have hit this in production."
etcd & Consul
: "etcd’s registers are not linearizable . . . 'consistent' reads in Consul return the local state of any node that considers itself a leader, allowing stale reads."
ElasticSearch
: "the health endpoint will lie. It’s happy to report a green cluster during split-brain scenarios . . . 645 out of 1961 writes acknowledged then lost."
Many of these problems had existed for quite a while
What’s really surprising about this problem is that it’s gone unaddressed for so long. The original issue was reported in July 2012; almost two full years ago. There’s no discussion on the website, nothing in the documentation, and users going through Elasticsearch training have told me these problems weren’t mentioned in their classes.
Kyle then quotes a number of users who ran into issues into production and then dryly notes
Some people actually advocate using Elasticsearch as a primary data store; I think this is somewhat less than advisable at present
Although we don't have an A/B test of universes where Kyle exists vs. not and can't say how long it would've taken for distributed systems to get serious about correctness in a universe where Kyle didn't exist, from having spent many years looking at how developers treat correctness bugs, I would bet on distributed systems having rampant correctness problems until someone like Kyle came along. The typical response that I've seen when a catastrophic bug is reported is that the project maintainers will assume that the bug report is incorrect (and you can see many examples of this if you look at responses from the first few years of Kyle's work). When the reporter doesn't have a repro for the bug, which is quite common when it comes to distributed systems, the bug will be written off as non-existent.
When the reporter does have a repro, the next line of defense is to argue that the behavior is fine (you can also see many examples of these from looking at responses to Kyle's work). Once the bug is acknowledged as real, the next defense is to argue that the bug doesn't need to be fixed because it's so uncommon (e.g., "
It can be tempting to stand on an ivory tower and proclaim theory, but what is the real world cost/benefit? Are you building a NASA Shuttle Crawler-transporter to get groceries?
"). And then, after it's acknowledged that the bug should be fixed, the final line of defense is to argue that the project takes correctness very seriously and there's really nothing more that could have been done; development and test methodology doesn't need to change because it was just a fluke that the bug occurred, and analogous bugs won't occur in the future without changes in methodology.
Kyle's work blew through these defenses and, without something like it, my opinion is that we'd still see these as the main defense used against distributed systems bugs (as opposed to test methodologies that can actually produce pretty reliable systems).
That's one particular example, but I find that it's generally true that, in areas where no one is publishing measurements/benchmarks of products, the products are generally sub-optimal, often in ways that are relatively straightforward to fix once measured. Here are a few examples:
Keyboards: after I published
this post on keyboard latency
, at least one major manufacturer that advertises high-speed gaming devices actually started optimizing input device latency. At the time, so few people measured keyboard latency that I could only find one other person who'd done a measurement (I wanted to look for other measurements because my measured results seemed so high as to be implausible, and the one measurement I could find online was in the same range as my measurements). Now, every major manufacturer of gaming keyboards and mice has fairly low latency devices available whereas, before, companies making gaming devices were focused on buzzword optimizations that had little to no impact (like higher speed USB polling)
Computers: after I published some other posts on
computer
latency
, an engineer at a major software company that wasn't previously doing serious UI latency work told me that some engineers had started measuring and optimizing UI latency; also, the author of alacritty
filed this ticket
on how to reduce alacritty latency
Vehicle headlights: Jennifer Stockburger has noted that, when Consumer Reports started testing headlights, engineers at auto manufacturers thanked CR for giving them the ammunition they needed to make headlights more effective; previously, they would lose the argument to designers who wanted nicer looking but less effective headlights since making cars safer by designing better headlights is a hard sell because there's no business case, but making cars score higher on Consumer Reports reviews allowed them to sometimes win the argument. Without third-party measurements, a business oriented car exec has no reason to listen to engineers because almost no new car buyers will do anything resembling decent testing of well their headlights illuminate the road and even fewer buyers will test how much the headlights blind oncoming drivers, so
designers are left unchecked to create the product they think looks best regardless of effectiveness
Vehicle
ABS
: after Consumer Reports and Car and Driver found that the Tesla Model 3 had extremely long braking distances (152 ft. from 60mph and 196 ft. from 70mph), Tesla updated the algorithms used to modulate the brakes, which improved braking distances enough that Tesla went from worst in class to better than average
Vehicle impact safety: Other than Volvo, car manufacturers generally design their cars to get the highest possible score on published crash tests;
they'll add safety as necessary to score well on new tests when they're published, but not before
Anyone could've done the projects above (while Consumer Reports buys the cars they test, some nascent car reviewers rent cars on Turo)!
This post has explained why measuring things is valuable but, to be honest, the impetus for my measurements is curiosity. I just want to know the answer to a question. I did this long before I had a blog and I often don't write up my results even now that I have a blog. But even if you have no curiosity about what's actually happening when you interact with the world and you're "just" looking for something useful to do, the lack of measurements of almost everything means that it's easy to find high ROI measurement projects, at least in terms of impact on the world — if you want to make money, building something is probably easier to monetize.
Appendix: "so you just want to get to the top of Hacker News?"
When I look at posts that I enjoy reading that make it to the top of HN, like
Chris Fenton's projects
or
Oona Raisanen's projects
, I think it's pretty clear that they're not motivated by HN or other fame since they were doing these interesting projects long before their blogs were a hit on HN or other social media. I don't know them, but if I had to guess why they do their projects, it's primarily because they find it fun to work on the kinds of projects they work on.
I obviously can't say that no one works on personal projects with the primary goal of hitting the top of HN but, as a motivation, it's so inconsistent with the most obvious explanations for the personal project content I read on HN (that someone is having fun, is curious, etc.) that I find it a bit mind boggling that someone would think this is a plausible imputed motivation.
Appendix: the motivation for my measurement posts
There's a sense in which it doesn't really matter why I decided to write these posts
, but if I were reading someone else's post on this topic, I'd still be curious what got them writing, so here's what prompted me to write my measurement posts (which, for the purposes of this list, include posts where I collate data and don't do any direct measurement).
danluu.com/car-safety
: I was thinking about buying a car and wanted to know if I should expect significant differences in safety between manufacturers given that cars mostly get top marks on tests done in the U.S.
This wasn't included in the post because I thought it was too trivial to include (because the order of magnitude is obvious even without carrying out the computation), but I also computed the probability of dying in a car accident as well as the expected change in life expectancy between an old used car and a new-ish used car
danluu.com/cli-complexity
: I had this idea when I saw something by Gary Berhardt where he showed off how to count the number of single-letter command line options that
ls
, which made me wonder if that was a recent change or not
danluu.com/overwatch-gender
: I had just seen two gigantic reddit threads debating whether or not there's a gender bias in how women are treated in online games and figured that I could get data on the matter in less time than was spent by people writing comments in those threads
danluu.com/input-lag
: I wanted to know if I could trust my feeling that modern computers that I use are much higher latency than older devices that I'd used
danluu.com/keyboard-latency
: I wanted to know how much latency came from keyboards (display latency is already well tested by
https://blurbusters.com
)
danluu.com/bad-decisions
: I saw a comment by someone in the rationality community defending bad baseball coaching decisions, saying that they're not a big deal because they only cost you maybe four games a year, which isn't a big deal and wanted to know how big a deal bad coaching decisions were
danluu.com/android-updates
: I was curious how many insecure Android devices are out there due to most Android phones not being updatable
danluu.com/filesystem-errors
: I was curious how much filesystems had improved with respect to data corruption errors found by a 2005 paper
danluu.com/term-latency
: I felt like terminal benchmarks were all benchmarking something that's basically irrelevant to user experience (throughput) and wanted to know what it would look like if someone benchmarked something that might matter more; I also wanted to know if my feeling that iTerm2 was slow was real or my imagination
danluu.com/keyboard-v-mouse
: the most widely cited sources for keyboard vs. mousing productivity were pretty obviously bogus as well as being stated with extremely high confidence; I wanted to see if non-bogus tests would turn up the same results or different results
danluu.com/web-bloat
: I took a road trip across the U.S., where the web was basically unusable, and wanted to quantify the unusability of the web without access to very fast internet
danluu.com/bimodal-compensation
: I was curious if we were seeing a hollowing out of mid-tier jobs in programming like we saw with law jobs
danluu.com/yegge-predictions
: I had the impression that Steve Yegge made unusually good predictions about the future of tech and wanted to see of my impression was correct
danluu.com/postmortem-lessons
: I wanted to see what data was out there on postmortem causes to see if I could change how I operate and become more effective
danluu.com/boring-languages
: I was curious how much of the software I use was written in boring, old, languages
danluu.com/blog-ads
: I was curious how much money I could make if I wanted to monetize the blog
danluu.com/everything-is-broken
: I wanted to see if my impression of how many bugs I run into was correct. Many people told me that the idea that people run into a lot of software bugs on a regular basis was an illusion caused by selective memory and I wanted to know if that was the case for me or not
danluu.com/integer-overflow
: I had a discussion with a language designer who was convinced that integer overflow checking was too expensive to do for an obviously bogus reason (because it's expensive if you do a benchmark that's 100% integer operations) and I wanted to see if my quick mental-math estimate of overhead was the right order of magnitude
danluu.com/octopress-speedup
: after watching a talk by Dan Espeset, I wanted to know if there were easy optimizations I could do to my then-Octopress site
danluu.com/broken-builds
: I had a series of discussions with someone who claimed that their project had very good build uptime despite it being broken regularly; I wanted to know if their claim was correct with respect to other, similar, projects
danluu.com/empirical-pl
: I wanted to know what studies backed up claims from people who said that there was solid empirical proof of the superiority of "fancy" type systems
danluu.com/2choices-eviction
: I was curious what would happen if "two random choices" was applied to cache eviction
danluu.com/gender-gap
: I wanted to verify the claims in an article that claimed that there is no gender gap in tech salaries
danluu.com/3c-conflict
: I wanted to create a simple example illustrating the impact of alignment on memory latency
BTW, writing up this list made me realize that a narrative I had in my head about how and when I started really looking at data seriously must be wrong. I thought that this was something that came out of my current job, but that clearly cannot be the case since a decent fraction of my posts from before my current job are about looking at data and/or measuring things (and I didn't even list some of the data-driven posts where I just read some papers and look at what data they present). After seeing the list above, I realized that I did projects like the above not only long before I had the job, but long before I had this blog.
Appendix: why you can't trust some reviews
One thing that both increases and decreases the impact of doing good measurements is that most measurements that are published aren't very good. This increases the personal value of understanding how to do good measurements and of doing good measurements, but it blunts the impact on other people, since people generally don't understand what makes measurements invalid and don't have a good algorithm for deciding which measurements to trust.
There are a variety of reasons that published measurements/reviews are often problematic. A major issue with reviews is that, in some industries, reviewers are highly dependent on manufacturers for review copies.
Car reviews are one of the most extreme examples of this. Consumer Reports is the only major reviewer that independently sources their cars, which often causes them to disagree with other reviewers since they'll try to buy the trim level of the car that most people buy, which is often quite different from the trim level reviewers are given by manufacturers and Consumer Reports generally manages to avoid reviewing cars that are unrepresentatively picked or tuned. There have been a couple where Consumer Reports reviewers (who also buy the cars) have said that they thought someone realized they worked for Consumer Reports and then said that they needed to keep the car overnight before giving them the car they'd just bought; when that's happened, the reviewer has walked away from the purchase.
There's pretty significant copy-to-copy variation between cars and the cars reviewers get tend to be ones that were picked to avoid cosmetic issues (paint problems, panel gaps, etc.) as well as checked for more serious issues. Additionally, cars can have their software and firmware tweaked (e.g., it's common knowledge that review copies of BMWs have an engine "tune" that would void your warranty if you modified your car similarly).
Also, because Consumer Reports isn't getting review copies from manufacturers, they don't have to pull their punches and can write reviews that are highly negative, something you rarely see from car magazines and don't often see from car youtubers, where you generally have to read between the lines to get an honest review since a review that explicitly mentions negative things about a car can mean losing access (the youtuber who goes by "savagegeese" has mentioned having trouble getting access to cars from some companies after giving honest reviews).
Camera lenses are another area where it's been documented that reviewers get unusually good copies of the item. There's tremendous copy-to-copy variation between lenses so vendors pick out good copies and let reviewers borrow those. In many cases (e.g., any of the FE mount ZA Zeiss lenses or the Zeiss lens on the RX-1), based on how many copies of a lens people need to try and return to get a good copy, it appears that the median copy of the lens has noticeable manufacturing defects and that, in expectation, perhaps one in ten lenses has no obvious defect (this could also occur if only a few copies were bad and those were serially returned, but very few photographers really check to see if their lens has issues due to manufacturing variation). Because it's so expensive to obtain a large number of lenses, the amount of copy-to-copy variation was unquantified until
lensrentals
started measuring it; they've found that different manufacturers can have very different levels of copy-to-copy variation, which I hope will apply pressure to lens makers that are currently selling a lot of bad lenses while selecting good ones to hand to reviewers.
Hard drives are yet another area where it's been documented that reviewers get copies of the item that aren't represnetative. Extreme Tech has reported, multiple times, that Adata, Crucial, and Western Digital have handed out review copies of SSDs that are not what you get as a consumer. One thing I find interesting about that case is that Extreme Tech says
Agreeing to review a manufacturer’s product is an extension of trust on all sides. The manufacturer providing the sample is trusting that the review will be of good quality, thorough, and objective. The reviewer is trusting the manufacturer to provide a sample that accurately reflects the performance, power consumption, and overall design of the final product. When readers arrive to read a review, they are trusting that the reviewer in question has actually tested the hardware and that any benchmarks published were fairly run.
This makes it sound like the reviewer's job is to take a trusted handed to them by the vendor and then run good benchmarks, absolving the reviewer of the responsibility of obtaining representative devices and ensuring that they're representative. I'm reminded of the SRE motto, "hope is not a strategy". Trusting vendors is not a strategy. We know that vendors will lie and cheat to look better at benchmarks. Saying that it's a vendor's fault for lying or cheating can shift the blame, but it won't result in reviews being accurate or useful to consumers.
While we've only discussed a few specific areas where there's published evidence that reviews cannot be trusted because they're compromised by companies, but this isn't anything specific to those industries. As consumers, we should expect that any review that isn't performed by a trusted, independent, agency, that purchases its own review copies has been compromised and is not representative of the median consumer experience.
Another issue with reviews is that most online reviews that are highly ranked in search are really just SEO affiliate farms.
A more general issue is that reviews are also affected by the exact same problem as items that are not reviewed: people generally can't tell which reviews are actually good and which are not, so review sites are selected on things other than the quality of the review. A prime example of this is Wirecutter, which is so popular among tech folks that noting that so many tech apartments in SF have identical Wirecutter recommended items is a tired joke. For people who haven't lived in SF, you can get a peek into the mindset by reading the comments
on this post about how it's "impossible" to not buy the wirecutter recommendation for anything
which is full of comments from people who re-assure that poster that, due to the high value of the poster's time, it would be irresponsible to do anything else.
The thing I find funny about this is that if you take benchmarking seriously (in any field) and just read the methodology for the median Wirecutter review, without even trying out the items reviewed you can see that the methodology is poor and that they'll generally select items that are mediocre and sometimes even worst in class. A thorough exploration of this really deserves its own post, but I'll cite one example of poorly reviewed items here: in
https://benkuhn.net/vc
, Ben Kuhn looked into how to create a nice video call experience, which included trying out a variety of microphones and webcams. Naturally, Ben tried Wirecutter's recommended microphone and webcam. The webcam was quite poor, no better than using the camera from an ancient 2014 iMac or his 2020 Macbook (and, to my eye, actually much worse; more on this later). And the microphone was roughly comparable to using the built-in microphone on his laptop.
I have a lot of experience with Wirecutter's recommended webcam because so many people have it and it is shockingly bad in a distinctive way. Ben noted that, if you look at a still image, the white balance is terrible when used in the house he was in, and if you talk to other people who've used the camera, that is a common problem. But the issue I find to be worse is that, if you look at the video, under many conditions (and I think most, given how often I see this), the webcam will refocus regularly, making the entire video flash out of and then back into focus (another issue is that it often focuses on the wrong thing, but that's less common and I don't see that one with everybody who I talk to who uses Wirecutter's recommended webcam). I actually just had a call yesterday with a friend of mine who was using a different setup than I'd normally seen him with, the mediocre but perfectly acceptable macbook webcam. His video was going in and out of focus every 10-30 seconds, so I asked him if he was using Wirecutter's recommended webcam and of course he was, because what other webcam would someone in tech buy that has the same problem?
This level of review quality is pretty typical for Wirecutter reviews and they appear to generally be the most respected and widely used review site among people in tech.
Appendix: capitalism
When I was in high school, there was a clique of proto-edgelords who did things like read The Bell Curve and argue its talking points to anyone who would listen.
One of their favorite topics was how the free market would naturally cause companies that make good products rise to the top and companies that make poor products to disappear, resulting in things generally being safe, a good value, and so on and so forth. I still commonly see this opinion espoused by people working in tech, including people who fill their condos with Wirecutter recommended items. I find the juxtaposition of people arguing that the market will generally result in products being good while they themselves buy overpriced garbage to be deliciously ironic. To be fair, it's not all overpriced garbage. Some of it is overpriced mediocrity and some of it is actually good; it's just that it's not too different from what you'd get if you just naively bought random stuff off of Amazon without reading third-party reviews.
For a related discussion,
see this post on people who argue that markets eliminate discrimination even as they discriminate
.
Appendix: other examples of the impact of measurement (or lack thereof)
Electronic stability control
Some boring stuff at work: a year ago, I wrote
this
pair
of posts on observability infrastructure at work. At the time, that work had driven 8 figures of cost savings and that's now well into the 9 figure range. This probably deserves its own post at some point, but the majority of the work was straightforward once someone could actually observe what's going on.
Relatedly: after seeing a few issues impact production services, I wrote a little (5k LOC) parser to parse every line seen in various host-level logs as a check to see what issues were logged that we weren't catching in our metrics. This found major issues in clusters that weren't using an automated solution to catch and remediate host-level issues; for some clusters, over 90% of hosts were actively corrupting data or had a severe performance problem. This led to the creation of a new team to deal with issues like this
Tires
Almost all manufacturers other than Michelin see severely reduced wet, snow, and ice, performance as the tire wears
Jason Fenske says that a technical reason for this (among others) is that the
sipes
that improve grip are generally not cut to the full depth because doing so significantly increases manufacturing cost because the device that cuts the sipes will need to be stronger as well as wear out faster
A non-technical reason for this is that a lot of published tire tests are done on new tires, so tire manufacturers can get nearly the same marketing benchmark value by creating only partial-depth sipes
As Tire Rack has increased in prominence, some tire manufacturers have made their siping more multi-directional to improve handling while cornering instead of having siping mostly or only perpendicular to the direction of travel, which mostly only helps with acceleration and braking (Consumer Reports snow and ice scores are based on accelerating in a straight line on snow and braking in a straight line on ice, respectively, whereas Tire Rack's winter test scores emphasize all-around snow handling)
An example of how measurement impact is bounded: Farrell Scott, the Project Category Manager for Michelin winter tires said that, when designing the successor to the Michelin X-ICE Xi3, one of the primary design criteria was to change how the tire looked because Michelin found that customers thought that the X-ICE Xi3, despite being up there with the Bridge Blizzak WS80 for being the best all-around winter tire (slightly better at some things, slightly worse at others), potential customers often chose other tires because they looked more like the popular conception of a winter tire, with "aggressive" looking tread blocks (this is one thing the famous Nokian Hakkapeliitta tire line was much better at). They also changed the name; instead of incrementing the number, the new tire was called Michelin X-ICE SNOW, to emphasize that the tire is suitable for snow as well as ice.
Although some consumers do read reviews, many (and probably most) don't!
HDMI to USB converters for live video
If you read the docs for the
Camlink 4k
, they note that the device should use bulk transfers on Windows and Isochronous transfers on Mac (if you use their software, it will automatically make this adjustment)
Fabian Giesen informed me that this may be for the same reason that, when some colleagues of his tested a particular USB3 device on Windows, only 1 out of 5 chipsets tested supported isochronous properly (the rest would do things like bluescreen or hang the machine)
I've tried miscellaneous cheap HDMI to USB converters as alternatives to the Camlink 4k, and I have yet to find a cheap one that generally works across a wide variety of computers. They will generally work with at least one computer I have access to with at least one piece of software I want to use, but will simply not work or provide very distorted video in some cases. Perhaps someone should publish benchmarks on HDMI to USB converter quality!
HDMI to VGA converters
Many of these get very hot and then overheat and stop working in 15 minutes to 2 hours. Some aren't even warm to the touch. Good luck figuring out which ones work!
Water filtration
Brita claims that their "longlast" filters remove lead. However, two different Amazon reviewers indicated that they measured lead levels in contaminated water before and after and found that lead levels weren't reduced
It used to be the case that water flows very slowly through "longast" filters and this was a common complaint of users who bought the filters. Now some (or perhaps all) "longlast" filters filter water much more quickly but don't filter to Brita's claimed levels of filtration
Sports refereeing
Storage containers
Rubbermaid storage containers (Rougneck & Toughneck) used to be famous for their quality and durability. Of course, it was worth more in the short term to cut back on the materials used and strength of the containers, so another firm bought the brand and continues to use it, producing similar looking containers that are famous for buckling if you stack containers on top of each other, which is the entire point of the nestable / stackable containers. I haven't seen anyone really benchmark storage containers seriously for how well they handle load so, in general, you can't really tell if this is going to happen to you or not.
Speaker vibration isolation solutions
Thanks to Fabian Giesen, Ben Kuhn, Yuri Vishnevsky, @chordowl, Seth Newman, Justin Blank, Per Vognsen, John Hergenroeder, Pam Wolf, Ivan Echevarria, and Jamie Brandon for comments/corrections/discussion.
