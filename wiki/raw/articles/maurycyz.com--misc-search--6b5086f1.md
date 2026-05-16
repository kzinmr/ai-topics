---
title: "Search engine results are truly terrible"
url: "https://maurycyz.com/misc/search/"
fetched_at: 2026-05-16T07:01:11.515437+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# Search engine results are truly terrible

Source: https://maurycyz.com/misc/search/

Search engine results are truly terrible
2026-05-15
A few months ago, I had the displeasure of trying to use the modern web without an ad-blocker.
Even though it's is ubiquitous among computer nerds, ad blocking is quite rare even in other technical fields. 
This got me wondering how search engines perform without all the tricks people do to get better results.
As a test, I wrote a few queries for... common software:
... obscure, but easy to find information:
What is the lowest K-alpha emission energy of Molybdenum?
... and few normal(-ish) questions:
What photodiode circuit should I use?
How do airplane wings work?
Why are brushed motors most efficient at high speeds?
Asking a search engine questions is almost never the best way to find good information, but it's what I've seen a lot of people do. 
To replicate the experience of a normie/victim I made sure to include the AI summary, sponsored results and info boxes:
Ad blocker
Molybdenum
Photodiode
Wings
Motors
Google
Bad
Ok
Crap
Ok
Crap
Bing
Bad
Ok
Crap
Ok
Crap
Kagi
Crap
Ok
Bad
Ok
Crap
DDG
Ok
Ok
Bad
Ok
Crap
Marginalia
Crap
Crap
Crap
Crap
Ok!
ChatGPT
Good
Good
Bad
Crap
Crap
Tests done on 2026-05-07
TLDR
;
No tool produced consistently good results.
This isn't a matter of my standards being to high:
good results for all these queries exist on the web, but they all failed to find them.
They had a real problem with returning vaugely related blogspam.
Having a good result in the top 3 was fifty-fifty.
For the ad blocker and molybdenum, ChatGPT was able to produce a good answer, but
it's responses were deeply flawed or outright incorrect for the other three questions...
largely because it was rephrasing the same spam that tripped up all the others.
Marginalia generally did very poorly, but it was the only one to perform decently on the motor question:
All the others returned surface-level AI slop, while it found a nice writeup on motors that answered the question.
Related
:
Grading
scale:
Good
: First result is correct and not spam.
For the questions, I'm not looking for a text book:
a single sentence explanation is perfectly fine provided that it explains the right thing and holds water.
Ok
:
Some spam/incorrect/incomplete/irrelevant pages, but a good result can be found in the first three links.
Just to be clear, this is not a good outcome: it means the top result was wrong or spam.
Bad
:
Same as ok, but using the first five links.
Crap
: First five results are all wrong, spam or spammy scams.
Five might not sound like a lot, but given the amount of junk in a modern search engine interface,
it's really quite rare for people to scroll pass those first five results.
ChatGPT isn't a search engine
, so I ranked it on correctness of the answer:
Good = Correct and well explained.
Ok = Correct, but not very good.
Bad = Incomplete.
Crap = Wrong or incomplete to the point of being harmful.
Detailed results:
ad blocker
For ad blockers, I'll only accept uBlock Origin or DNS based solutions.
In order to work, an ad-blocking extension needs a huge amount of access to your browser:
it's not a good idea to take chances.
uBlock Origin is free, open source (so you can see what it's doing) and very effective:
Paying a difficult to cancel subscription for a inferior product is not a good idea.
A lot of those shady extensions also have identical pricing plans, which make me think they are slop-ware pumped out by one guy.
I don't have proof that they are scams in the strict sense, but it is rather suspicious.
Google
:
"
Ad block - [...] - Chrome web store
":
Charges a $40/year subscription, allows "non-intrusive" advertising and collects data.
"
AdBlock Plus
": Same deal.
Infobox linking to
https://getadblock[.]com/
:
The usual.
"
Get AdBlock
": ditto.
"
uBlock Origin
":
Finally, a good result. Just in time to save google from the "crap" tier,
but I doubt it's early enough to stop someone from being scammed.
Verdict: bad.
Bing
:
"
Adblock Plus
": Same as google's #2.
Infobox with "
https://www.windowscentral[.]com/how-block-ads-and-trackers-xbox
":
an ad-filled blog-spam site.
It does provide reasonable instructions, but good luck reading it without an ad blocker.
A second infobox linking to "
Adblock vs Adblock Plus - PC Guide
":
an ad-laden blog-spam comparing two sub-par extensions. (both allow "acceptable ads")
"
uBlock Origin
":
Good, but why is it so far down?
"
AdBlock — block ads across the web
":
The usual scammy adblocker extension.
Very similar to google's top four results.
Verdict: bad.
Kagi
:
"
Adblock Plus
" same as google's #2
"
Ad block - [...] - Chrome web store
": same as google's #1
"
Adblock Plus
": Yet another shady adblocker with a $40/year subscription
"
The Ethical Ad Blocker
" (infobox):
A blog post describing an ad-blocker that blocks access to any websites that have ads, 
which prevents any accusations of piracy.
Funny and probably real, but not what users are looking for.
"
AdGuard Ad blocker
":
Yet another of those nearly identical sketchy adblockers.
Kagi is the first search engine to not include uBlock in the first five results, but it does link me to someones's rather cool blog...
however, I still had to scroll past quite a bit of junk to find it.
Verdict: crap.
DuckDuckGo
:
"
Adblock Plus
": same as google #2.
"
AdBlock — block ads across the web
": same as google #1
"
uBlock Origin
": Finally, in the top 3!
"
getadblock[.]com
": More junk.
"
AdBlock — block ads across the web
": Same as #2, but on Microsoft's extension store instead of googles.
Verdict: ok.
Marginalia
:
"
Ghostery Ad Blocker
": Yet another blocker that doesn't actually block ads, and has been caught selling data to advertisers.
"
Ad blockers are not allowed on YouTube
"
A blog post with a half-baked list of ways to get around youtube's ad-blocker detection.
Indirectly recommends uBlock, but also a lot of stuff that won't work.
Not great.
"
Vivaldi
": Chrome with a built in adblocker.
Not a scam, but you don't need to install a new browser to block ads.
"
EasyList is in trouble and so are many ad blockers
":
Corporate blog post about hosting problems.
"
Ad Blockers - Contains Moderate Peril
":
A blog post about ad-blockers, recommends "AdBlocker Ultimate".
Not a spam, but not the best recommendation.
Verdict: Crap.
Marginalia's results are quite different from all the other search engines:
It's pulled out two real blog posts alongside the usual spam.
ChatGPT
:
(Note: I modified the prompt to "Recomend me an ad blocker.")
The LLM recommended [1] uBlock Origin Lite, which is a variant of uBlock for modern
chrome, by the same author.
The Lite version is technically more limited than the original, but still works works very well.
It also suggested [2] "AdGuard AdBlocker", but only as a fallback.
Verdict: Good.
...
Molybdenum
:
"What is the lowest K-alpha emission energy of Molybdenum?"
Despite this being a straightforward table lookup, all the LLM-summaries got it wrong:
The lowest energy line is Kα
2
(17,374 eV), not Kα
1
(17,479 eV).
The reason for this is that X-ray lines were first observed using diffraction, 
and measured by wavelength, which is inversely proportional to energy:
Kα
1
is has a shorter wavelength, but higher energy.
Google
:
Incorrect AI overview citing a paper.
The paper lists both K-alpha lines, but the LLM used the wrong one.
Table from Lawrence Berkeley National Lab
:
lists the correct value.
Another
table
,
this time from an equipment manufacturer. Lists the correct value.
A paper
characterizing the X-ray fluorescence spectrum of molybdenum.
"Characteristic X-ray - Wikipedia": an overview of X-ray emission lines,
but it does not give any specific energy values.
Not a relevant result.
Verdict: ok.
Bing
:
Wrong AI overview citing google's #2:
It made the same mistake with Kα
2
and Kα
1
.
"
Molybdenum
":
A nice little page from LBL listing some technical properties of molybdenum.
This is the most relevant result so far.
"
12.1: Fundamental Principles
":
an article that happens to use molybdenum as an example, but lists wavelengths instead of photon energy.
"
Experimental K-alpha x ray energies
":
a table of emission lines.
The
same paper
as google's #4.
Verdict: ok.
Kagi
:
A very wrong AI overview giving "0.709 eV": off by four orders of magnitude!
I suspect it took the number from Bing's #3, but instead of actually converting the wavelengths to energy, it just slapped an "eV" on.
Same table as google's #2. A good result.
Same as google's #3. A good result.
A page
about the theoretical calculation of X-ray lines.
Does not provide an energy for molybdenum.
A list of
chemical properties
of molybdenum.
Does not mention X-rays.
This nicely demonstrates the problem with LLMs:
A chatbox usually gets things (mostly) right, but will occasionally be very, very wrong.
Verdict: ok.
DuckDuckGo
:
Incorrect AI overview referencing
a NIST publication
.
Same as bing #2. A good result.
Same as bing #3: not relevant to the question.
Same as google #4. A good result.
Some
data table
:
a perfectly fine result.
No surprises here:
It's a few good sources and a slightly wrong LLM summary.
Verdict: ok.
Marginalia
:
"Plasma catalytic non-oxidative conversion of methane into hydrogen and light hydrocarbons":
A preprint paper that used X-ray equipment and mentioned molybdenum in passing.
"XRF Technologies for Measuring Trace Elements in Soil and Sediment":
Similar to #1.
A paper that used X-ray equipment and mentions molybdenum, but does not answer the question.
Marginalia doesn't try to be a comprehensive index, so it's unsurprising that it did badly on this one:
only two results were returned, and none of them included the requested number.
Verdict: crap.
ChatGPT
:
Chat gave 17.37 keV, which is the correct value.
Good job on being the only LLM to answer a simple question correctly.
...
Photodiodes
:
"What photodiode circuit should I use?"
Photodiodes are excellent light sensors, but their output is a small and difficult to measure current.
Generally, the best way to fix this is with a transimpedance amplifier:
an op-amp circuit that converts the current into an output voltage while keeping the sensor's bias constant.
This provides a fast and exceedingly linear response.
An ideal result would also mention techniques like bootstrapping (to increase bandwidth of large sensors) and
logarithmic converters (to measure a wide range of light levels).
Related
:
Google
AI overview citing #4, recommending a transimpedance amplifier,
but it provides a schematic of a different configuration.
"Photodiode – A Beginner’s Guide": 
A blog-style website with circuits that don't work, are missing important details and have poor explanations.
"Photodiode Basics":
Ad-ridden page which does include the rough layout of a transimpedance circuit, but with no mention of feedback capacitors.
These are often needed to prevent oscillation.
"What are the pros and cons for the various photodiode circuit arrangements?":
A forum thread that mentions transimpedance amplifiers, but doesn't give any specifics.
"Photodiode Component Basics [...] - Youtube":
Video with a demonstration of a photodiode working, but without any amplification or readout circuits.
Verdict: Crap.
Bing
:
AI overview citing #2, but it recommends a bad configuration with a resistor
in parallel with the diode. The output is non-linear, high-Z and, difficult to use.
"Photodiode – A Beginner’s Guide": Same as google #2. A bad result.
"Photo Diode (Symbol, [...] Pros & Cons) Explained - Youtube":
Another super generic video.
"Fire Detection Circuit Using Photodiode":
Content farm video with no schematic and no explanation.
"Photodiode Construction and Working - Youtube":
Another extremely generic explanation video.
Does not include any circuits or even discuss the problem.
Verdict: Crap.
Kagi
:
"Photodiode – A Beginner’s Guide": Same bad article as google's #2.
"Photodiode Basics": The same as google's #3: incomplete circuits on an ad-ridden page.
"What are the pros and cons for the various photodiode circuit arrangements?": 
Same as google #4, an unhelpful forum thread.
"PHOTODIODE OPERATION MODES AND CIRCUITS":
Provides an example of a transimpedance amplifier, but has no example values or instructions on selecting them.
"
Technical notes / Si Photodiodes
":
A PDF from a photodiode manufacturer, which provides practical circuits and a description of photodiode properties.
This is the first results that provides enough information to actually build a working sensor.
Verdict: Bad.
DuckDuckGo
:
"Photodiode – A Beginner’s Guide": The same as google's #2, meh explanations and some of the circuits don't work.
"Photodiode Basics": Same as google's #3: Incomplete circuits on an ad-ridden page.
"PHOTODIODE OPERATION MODES AND CIRCUITS":
Same as kagi #4. Not good enough to build a working circuit.
"A Practical Guide to Photodiode Amplifier Circuit Design [...]":
A marketing piece for a equipment manufacturer.
Unlike the Hamamatsu appnote, this doesn't have any useful information.
"
Technical notes / Si Photodiodes
":
Same application note as Kagi #5. A good result.
Verdict: Bad.
Marginalia
:
"PIN Photodiode gamma detection amplifier circuit - rectangular wave output":
Forum post with a broken circuit. Not something you want to copy.
"Circuit Diagram":
An unrelated forum post about an XKCD comic.
"Short Circuit Limiter":
Unrelated blog post.
"NES Cartridge Chaos: [...]":
Unrelated blog post.
"How can i increase the range of values that a light sensor gives?"
Forum post showing an ok configuration, but with no explanation or information on how values should be selected.
Verdict: Crap.
ChatGPT
:
Chat gave a very wall of text boiling down to "use a transimpedance amplifier", but with no explanation
of what that is or why it's good for light detection.
It also drew a nonsensical "schematic" which would be of no use to anyone trying to build one circuit:
+V
                  |
                  |
              [Photodiode]
                  |
                  +------
                         |
                    Rf   |
            output <---/\/\/
                         |
                    Cf  ---
                        ---
                         |
                        

(+) op-amp tied to ground or reference
Hidden in the "citations", it did link to a reference designs from texas-instruments...
and an AI generated blog-spam post.
I'll bin it under "Bad".
...
Wings
:
"How do airplane wings work?"
The simplest reasonably correct answer is that wings are angled to push down on the air, which lifts the plane up.
The fluid mechanics happening around the wing are very complicated, but I'll accept a good one sentence explanation.
Of course, more rigorous and detailed explanations are fine, but they must actually be rigorous:
many explanations add complexity in a way that results in more gaps.
Also, there's a very common wrong answer
(equal-transit) which asserts that the air takes
the same amount of time to travel over the top and bottom of a wing.
Therefore, since the top surface is curved, the air must move faster.
By Bernoulli's principle, a higher flow velocity creates low pressure, and that
low pressure region that pulls the wing up.
This is wrong for multiple reasons:
It violates the conservation of momentum, because the wing doesn't impart any momentum to the air.
Obviously, fans work.
Airplanes can fly upside down...
which shouldn't be possible if lift is some special property of the wing's shape.
Paper or balsa-wood planes with flat airfoils work fine.
Other explanations go
"something something Bernoulli", which is not technically wrong, but is deeply incomplete:
Bernoulli's principle does come into play around a wing, but using it as an explanation requires showing that air speeds up
as it travels over the top surface —
something which can only happen because of a pre-existing low pressure region.
These explanations does not hold water on it's own.
Would a proper analysis of the airflow over a wing be a good result?
Of course.
Is it enough to point at a tiny fragment of that and handwave it as an explanation?
No.
I'll consider this as a bad result, because it's neither a good explanation, nor a useful model:
Wrong models can useful if the truth is complicated, but this is quite the opposite.
"Planes stay up because they push the air down" is simple, correct and builds intution.
For example, it predicts that the pressure on the ground should increase as a plane flies over it...
and it does.
"Planes stay up because of Bernoulli" doesn't explain anything if you think about it for two seconds.
All it does is bring in some math that isn't relevent until you read the rest of the textbook.
Related
:
Google
:
AI summary citing a TikTok video which contains the "something something Bernoulli" argument.
Not entirely wrong, but needlessly complicated and incomplete.
How wings really work
:
A professor debunking "equal transit" with an experiment...
nice, but a debunk is not an explanation.
"
How Airplane Wings REALLY Generate Lift
":
A youtube video with the correct explanation. A good result.
"ELI5: how does a wing work? - Reddit":
Reddit thread, most comments are correct, but many are repeating the incorrect explanation.
"
How Wings Work
":
A page with a mostly correct animation, but no explanation of what's happening.
Verdict: Ok.
Bing
AI summary stating the incorrect equal-transit explanation.
Seems to be referring an an
old Glenn Research
page with the incomplete explanation.
"
Airplanes
":
A correct article which calls out the incorrect bernoulli argument.
A good result.
The same correct video from Google #3.
"How Airplanes Work: A Simple Explanation for Beginners":
A youtube video giving the incomplete explanation.
"How Wings Work": Same as google's #5.
Verdict: Ok
Kagi
"How Does A Wing Work? - Science Through Time":
AI slop video with an bad answer.
I can't tell if this it is the "equal transit" model or the incomplete one,
because it doesn't include anything resembling detail or logic.
"
How Does A Wing Actually Work?
": A Veritasium video on youtube,
with the correct explanation.
A good result.
"
How airplane wings work
":
A cool video showing airflow over a wing, during normal flight and a stall...
but it's not an explanation.
"
How Does A Plane Wing Work?
":
Correct explanation and demo.
"How do airplane wings work?":
Explains the structural components of a wing, but not why it's able to create lift.
Verdict: Ok
DuckDuckGo
"Learn How Airplanes Work":
A page that lists the parts of a plane, and gives the incorrect "equal-transit" explanation.
How planes work
:
An article with a brief, but correct explanation.
Dynamics of Flight
An old article from Glen Research with the "something something Bernoulli" explanation.
"How airplane wings actually work - Today Plane crash": AI Slop article, wrong answer.
"How wings work": an animation of airflow, but does not have an explanation
Verdict: Ok
Marginalia
"How do I explain what makes an airplane fly to a non-technical person?":
Forum thread of people asking the same question. A few answers are correct, but a lot aren't.
I'll bin it as a bad result.
"How do the Americas Cup Yachts sails work?":
Forum thread about sailing.
"How do I keep my futuristic racing hovercraft from becoming airplanes?":
Forum thread about fantasy hovercraft.
"How is the fatigue life of an airplane wing flexing during turbulence determined? How do they keep track of it?"
Forum thread on accelerated life testing and maintenance of aircraft.
"How do you scale a svg img to fit container?"
A CSS question that just happens be about an image of an airplane.
Verdict: Crap.
ChatGPT
:
Says that wings create lift, and then states that this is because the shape speeds up the airflow faster over the top surface (why?)
therefore, by Bernoulli’s principle, the pressure is lower on the top surface.
This is the second category of bad explanations.
Verdict: Crap
...
Motors
:
"Why are brushed motors most efficient at high speeds?"
Electric motors work by passing a current through coils, which creates a magnetic field.
These magnetic field pushes against permanent magnets to create torque.
To create continuous rotation, the direction of current and field must be constantly reversed to prevent the motor from locking up
after half a turn.
This is either done using mechanical switches (brushed motors),
transistors (BLDC/stepper),
or by running the device from AC power (synchronous motors).
Either way, the the strength the magnetic field
inside a motor determines it's torque,
but the mechanical power is torque times rotational speed.
However, resistive losses in the coil windings don't care about how fast the motor turns and are proportional to current.
Therefore, at low speeds, more losses are incurred during each rotation, and the motor is less efficient.
This is why motors are almost always geared down
:
Even if they can produce enough torque, it's a bad idea to run them anywhere except right below their unloaded speed.
(efficency aside, the heat produced can damage them)
Google
:
Incorrect AI summary citing the AI slop in #2.
"Comparing Energy Efficiency of Brushless vs. Brushed Motors":
Slop blog that claims the high speeds reduce losses in the motor's commutator, which simply isn't true.
Commutator losses (arcing) generally increase with rotational speed.
"Brushless Vs Brushed DC Motors: When and Why to Choose One Over the Other":
AI slop advert. Does not answer the question.
"What’s the difference between a brushed and brushless motor, and is one better than the other?":
Reddit thread that states that brushed motors are less efficient, but gives no explanation.
(also, that's not what the question asked...)
"The Advantages of Brushed Motors: Powering the World with Efficiency and Simplicity - Magmotor":
AI slop, doesn't answer the question.
"Brushed vs Brushless Motor: Key Differences, Performance, and How to Choose":
AI slop, doesn't answer question.
This is the first time I got 5 obvious AI slop results.
It's not a good sign for the rest...
Verdict: Crap.
Bing
:
AI summary citing #2.
"Brushed vs Brushless: Unraveling the Mystery of Motor Efficiency":
AI slop that doesn't answer the question.
It also states that motors produce more power at high speeds, which is true, but doesn't explain the question.
At any given voltage, a motor has a torque at which it stalls and a maximum speed that's reached under no load.
As you would expect, the motor makes the most power at roughly the half-way point between these two...
but the efficiency is best at the extreme end of the speed range.
"Comparing the Efficiency of Different Electric Motor Types":
AI slop, doesn't answer the question.
"Are Brushed DC Motors Still Relevant? Efficiency, Smart Control, and New Applications Explained":
More AI slop. Doesn't answer the question.
"Brushed vs Brushless Motors: Comparing Efficiency, Lifespan, and Performance Metrics":
AI Slop. Doesn't answer question.
Verdict: Crap.
DuckDuckGo
:
AI summary citing
"Brushed Motors vs. Brushless Motors":
Neither answer the question.
"Brushed vs Brushless: Unraveling the Mystery of Motor Efficiency":
AI slop.
"Comparing the Efficiency of Different Electric Motor Types":
AI slop.
"Brushed vs Brushless Motors: Comparing Efficiency, Lifespan, and Performance Metrics":
AI slop.
"Are Brushed DC Motors Still Relevant? Efficiency, Smart Control, and New Applications Explained":
AI slop.
Verdict: Crap.
Kagi
:
AI summary citing
"Brushed DC Motor Theory":
A page on a wiki run by Northwestern University.
Talks about efficiency being zero under stall — which it is — but that's not what I asked about.
"Brushless Vs Brushed DC Motors: When and Why to Choose One Over the Other":
Probably human written, but doesn't answer the question, instead comparing two motor designs.
(The efficiency curve is similar for both.)
"Brushed vs Brushless: Unraveling the Mystery of Motor Efficiency":
AI slop.
"What’s the difference between a brushed and brushless motor, and is one better than the other?":
Forum thread that isn't about the question and doesn't answer it.
"Comparing the Efficiency of Different Electric Motor Types":
AI Slop.
Verdict: Crap.
Marginalia
:
"Why does a Tesla car use an AC motor instead of a DC one?":
A Forum thread that doesn't answer the question.
Hobby CNC machining and resin casting
:
Lcamtuf is really good... but this isn't a page about electronics.
It does mention motors, but gives no explanation for why there efficiency curve peaks at very high RPMs.
CSC 297 Robot Construction: Driving Motors
:
A long and detailed website, that actually answers the question!
The first actually relevant result.
"Stepper motor - Wikipedia": Wiki page on a different type of motor.
"Brushless vs. Brushed Motors [New for 2026]": AI slop.
Verdict: Ok
A win for marginalia!
Only a single AI slop page was returned, and two of the results were detailed write-ups on motors and robotics:
not LLM generated, not surface level blogspam, but actual resources that you can use for learning.
Age is best indicator of a quality website:
If it was written decades ago, and it's still up, someone decided it was worth keeping around for all these years.
While the #3 result doesn't have a date, but it uses handwritten HTML which is quite rare nowadays.
I'd guess it was written somewhere between 1990 and 2010...
and this one's has been maintained as late as 2017, so they take some pride in what they wrote.
This is what we loose when google promotes new content:
well written pages by real people who actually care instead of a 5 minute rundown for hackernews.
ChatGPT
:
Chat provided a generally correct explanation, but it seems to have confused the questions with:
"why do motors draw less current when when spinning quickly?".
After some waffling about Back-EMF, it handwave that because the current decreased,
the losses decreased — ok — and efficiency must be better...
but that simply isn't true:
Efficiency is the ratio of output power and input power.
Under no-load conditions, the motor is drawing the minimum possible current,
but it's also not producing any usable mechanical power, so it's efficiency is zero.
Not only does the LLM's logic not hold water, it's much more complicated then the truth.
Verdict: Crap.
