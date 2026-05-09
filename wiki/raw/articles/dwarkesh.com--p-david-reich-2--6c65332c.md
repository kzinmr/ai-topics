---
title: "David Reich - Why the Bronze Age was an inflection point in human evolution"
url: "https://www.dwarkesh.com/p/david-reich-2"
fetched_at: 2026-05-09T07:01:09.013351+00:00
source: "dwarkesh.com"
tags: [blog, raw]
---

# David Reich - Why the Bronze Age was an inflection point in human evolution

Source: https://www.dwarkesh.com/p/david-reich-2

David Reich
is back.
He and collaborator
Ali Akbari
just
published a paper
that overturns a long-standing consensus about human evolution — that natural selection has been dormant in our species since the agricultural revolution.
By scaling ancient DNA sequencing and developing a new statistical method, they found that selection has actually sped up.
Selection went especially bonkers during the Bronze Age (around 3,000 years ago).
That’s when gene frequencies for everything from immune function to body fat to intelligence were most in flux.
Over the last 10,000 years, selection pushed the genetic predictor of cognitive performance up by roughly a full standard deviation — most of it between 4,000 and 2,000 years ago.
After we finished recording, David sketched out on a whiteboard his new heretical model about who the Neanderthals really were. Luckily, I took out my iPhone and managed to record it.
He thinks the standard story (that Neanderthals are some separate archaic lineage we interbred with a little) just doesn’t fit the evidence. Instead, he proposes that Neanderthals are essentially genetically-swamped modern humans.
A small population somewhere around the Caucasus invented Middle Stone Age technology roughly 300,000 years ago and expanded outward. The ones that moved into Europe interbred with local archaic humans, got genetically swamped, and became Neanderthals. The same expansion went into Africa, met much more diverged archaic Africans, and that mixture became us.
This means Neanderthals and modern humans share the same cultural ancestry — the only difference is which archaic humans they mixed with afterward.
David is a brilliant and rigorous scholar. It was a real delight to learn from him again.
Watch on
YouTube
; listen on
Apple Podcasts
or
Spotify
.
Cursor
was super useful as I prepped for this episode. Whenever I had a question, I’d have Cursor kick off a few different models simultaneously and then compare their responses. I found that this led to better results than I could get out of any individual LLM. If you’ve only used Cursor for coding, you should try using it for research. Check it out at
cursor.com/dwarkesh
Jane Street
uses an internal currency called “hive bucks” to allocate compute through a real-time auction – and anyone can change anyone else’s bids or even kill their jobs! Everyone just trusts each other to act in the firm’s best interest, which is what lets the system work in the first place. If this weird and high-trust culture sounds like your kind of thing, Jane Street’s hiring at
janestreet.com/dwarkesh
Crusoe’s
ML infra team built fastokens, an open-source tokenizer that delivers a ~9x speedup over Hugging Face and up to 40% faster time-to-first token – on real production workloads! Crusoe achieved these results by parallelizing things and using some clever engineering to handle duplicates without cross-thread coordination. Learn more at
crusoe.ai/dwarkesh
(00:00:00) – Ancient DNA suggests strong selection over last 10,000 years
(00:15:45) – Natural selection intensified during the Bronze Age
(00:35:02) – Why didn’t evolution max out intelligence?
(00:57:21) – Evolution is limited by time, not population size
(01:09:02) – Why no farming before the Ice Age?
(01:17:13) – The Neanderthal puzzle David can’t stop thinking about
(01:54:10) – The methodology behind this breakthrough
Dwarkesh Patel
I am back with
David Reich
, who is a professor of
ancient DNA
at Harvard
. How do you describe what it is that you study?
David Reich
I’m a geneticist, and I work on human history and how ancient people relate to each other and people living today.
Dwarkesh Patel
We did an interview two years ago
, which ended up being one of the most popular interviews I’ve ever done. I think people found it really compelling that there’s so much about human history we don’t know and are just learning about now as a result of the kinds of techniques your lab is using.
You have a new preprint
that’s very exciting, and I wanted to talk to you about it. Can you give me a little bit of context on what we’re talking about today?
David Reich
The dream was that when this ancient DNA field started, more than 16 or 17 years ago, we were going to learn a lot about biology —about how people’s biology changed over time— by getting DNA out of ancient human remains and tracking changes over time. And that dream has really not been realized since the beginning of this field.
The field has been a big success with regard to learning about human history. It’s resulted in surprising findings about human migrations —people not being descended from the people who lived in the same place hundreds or thousands or tens of thousands of years before— and mixture being common in human history, and sex-biased processes being common. And there have been things that were not expected from archaeology. The field’s been a big success from that perspective, but what’s not been successful is learning about biology and biological change.
One big reason has been that the sample sizes have been too small. When you have a single person’s DNA, it provides a tremendous amount of information about history. That’s because when you look at one person’s DNA, it’s not a single person. It’s many people. It’s your two parents, your four grandparents, your eight great-grandparents, 16 great-great-grandparents, and so on. Going back in time, thousands, tens of thousands, even hundreds of thousands of ancestors are contributing to people today.
When you look at the DNA of a single person’s
genome
or a
Neanderthal
genome, you have effectively tens of thousands of ancestors all represented in your data. And you can position that individual exquisitely with respect to other people from whom you have data. But when you are interested in how a particular genetic variant—that affects something like your skin pigmentation, or your ability to digest cow’s milk into adulthood, or a behavioral trait—changes over time, a single person gives you only one sample, or maybe two samples: the one in their mother and the one in their father.
To get a high-resolution picture of how the frequency changes over time, you need very big sample sizes, truly very large numbers of people. We just didn’t have that until the last few years. What motivates the study we’re talking about today, and the work that hopefully a number of groups will be doing in the coming years, is the fact that we now finally have those numbers. We can do something with the data to see how frequency changes over time.
Dwarkesh Patel
Can I ask a question? I’ll be asking a lot of naive questions through the next few hours, but why are frequency changes especially interesting?
David Reich
What we’re interested in is using the experiment of nature that’s occurred in our history, over the last tens of thousands of years, to understand what’s biologically significant in our DNA. If there has been a change in environment that a population has experienced—for example, people shifted to agriculture, began living close to domesticated animals, or moved from a cold place to a warm place, or a low place to a high place—then there’s pressure on the population to adapt to these new stresses and new needs.
The way you’re going to detect that is by seeing that the frequency of a genetic variant—that for example might allow you to live at higher altitude, or that might nudge you to have a different behavioral pattern advantageous in the new situation—pushes systematically in some direction in a way that is enough for you to detect. It’s very hard to detect slight shifts in frequency by a few percent or ten percent unless you have a very big sample size. What we’re looking for are those changes in frequency that are too extreme to be due to chance. That will tell us there have been pushes against the biology as a result of the changes in environment that people have experienced.
Dwarkesh Patel
Interesting. What did you guys find?
David Reich
Seven years ago,
Ali Akbari
, who at the time was a postdoctoral scientist in my laboratory and a few years later became a permanent staff scientist, set out to use the data we were producing to learn about biological change over time. I think the reason he was interested in our laboratory rather than other places was that a focus of our lab has been generating truly large amounts of data from ancient humans. We’ve been trying to industrialize the process, make it very inexpensive, make it high quality, and generate large numbers of samples with lots of good data for this purpose.
There’s been this large amount of data we’ve generated. And it made it possible to conceive again of asking whether there have been frequency changes over time. The mainstream view in human evolution in the last several decades has been that
natural selection
has been pretty quiescent over the last several hundred thousand years of human history.
There are several lines of evidence that have been deployed to document this. One is that if you compare diverse populations from different continents around the world, for example Europeans and East Asians, and you look at mutations that differ in frequency between these groups—all mutations differ a little bit in frequency, sometimes a lot—you can say, “What are the most different mutations in terms of frequency between Europeans and East Asians?” And there are almost no genetic changes that are 100% different in frequency between Europeans and East Asians.
Europeans and East Asians descend from a common ancestral population 40,000 or 50,000 years ago that came out of Africa and the Middle East. This population had a set of gene frequencies, and these variants bopped around randomly—a process known as
genetic drift
—or perhaps under selection in one direction or another. The time that’s passed since 40,000 or 50,000 years ago is sufficiently small on an evolutionary timescale that there’s just not much genetic differentiation on average between these two groups.
However, if there’s been natural selection, for example to help people in one place digest alcohol better, or digest milk better, what you might expect is that there would be some mutation that would have rocketed up to very high frequency. Forty or fifty thousand years is a lot of time, it’s maybe 1,500-2,000 generations. That might easily be enough time to see a 100% difference in frequency. Yet you don’t see any more than what you would expect by chance.
This combination of things made it seem that selection has just been quiescent. Maybe a few hundred thousand years ago, the ancestral human population got to some kind of optimum, and after that there hasn’t been much genetic change in one way or the other.
There have been small amounts of natural selection, or selection to remove bad mutations that are constantly raining down on the genome, but not what we call
directional selection
. That would be newly arising mutations, or mutations being pushed in a systematic direction, to help the population get to a different adaptive set point more favorable for the conditions that population is living in.
We were able to partition how much of the changes in frequencies of all the mutations that we’re seeing in the DNA—we’re looking at about 10 million positions that vary—is due to directional selection (adaptation) versus other factors, especially genetic drift. And 98% of it is other factors, especially genetic drift. It’s overwhelmingly migrations and population structure causing fluctuations in frequency.
As a result, it’s super hard to detect the signals of adaptive natural selection because they’re a tiny fraction of the total frequency change. The vast majority of it are these migrations and mixtures. Nevertheless, there’s so much natural selection, as our study has shown, that it’s actually been rampant in the genome.
Dwarkesh Patel
Can I ask a clarifying question here? Why are we discounting
population admixture
or replacement as selection? If you think about it at a group level, if one population replaces another population, isn’t that selection?
I remember from the last episode you were explaining how there have been huge changes in what kinds of people are in a specific area. One population came in and replaced the previous one, and then a new population came in and replaced that one. To the extent that the genetics are relevant to why that population replaced the other one, why should that not count towards what we understand to be selection over the last 10,000 years?
David Reich
It could count, and may count, and probably should count in some respects. But it could also be that this population replacement is due to some cultural phenomenon —technology held by one of these groups and not others. And maybe there are some genetic mutations that are contributing to this. Who knows? It’s possible.
But what you’re seeing is a whole-genome shift. What we’re looking to see is whether there’s one place in the DNA that is driving the change in a way that’s different from the rest of the genome. From a statistical point of view, what happens at these times of migration is there are just huge fluctuations in frequencies. These are extremely uninformative times for detecting natural selection. The best moments to detect natural selection are when migrations and population admixtures are not happening for a few hundred years. During these times, you can actually see the mutation slowly blowing in one direction as a result.
The way we think about the history of Europe and the Middle East for the purpose of this study is as an archipelago of little populations in space and time, each pretty isolated from each other. You have a little population in Britain isolated for a few hundred years, or a little population in Hungary isolated for a few hundred years, between big events of migration and mixture. In each of those little experiments of nature, we can ask: does this mutation slightly increase in frequency? Does that same mutation slightly increase in frequency? If all the arrows point in the same direction, we win. They’re telling us that natural selection is occurring.
For example, 4,500 years ago in Europe, almost all mutations went through huge frequency changes. That’s not because of natural selection. It’s because of the steppe migration from
north of the Black and Caspian Sea
. 40-80% of the DNA becomes
Yamnaya
from steppe pastoralists. Their frequencies of mutations were different not because of selection necessarily, but just because they had evolved in different places for thousands and tens of thousands of years. When you look at the descendant populations, there are huge changes in frequency. What you need to do is see if natural selection is explaining a shift more than you would expect by chance.
Dwarkesh Patel
So you found these locations that seem to be under selection. I have another clarifying question. You say you found 3,800 locations which you’re 50% confident have been under selection in the last 10,000 years.
David Reich
It’s 7,200 where we’re 50% confident. We’re getting about 7,200 positions in the DNA that have 50% confidence of being real. Only half of those are real—we don’t know which ones—so 3,600 of them are real.
Dwarkesh Patel
Does that also mean that outside of those 7,200, you’re confident the other locations in the genome are not under selection?
David Reich
No. If you look at the 25% probability cutoff, there will be tens of thousands, and there will be many real ones there too. In fact, multiple analyses we do suggest that the genome is vibrating with natural selection.
There are all sorts of weaker effects that would be picked up in even larger studies than we’ve done. In fact, almost every position in the DNA is correlated to another position that is being dragged in one way or the other by natural selection. Instead of being quiescent, natural selection is everywhere. Even though it’s only 2% of the frequency change, it’s tugging the positions in one direction or the other everywhere.
So we analyzed these positions that we had identified, the hundreds of positions we were super confident about. We looked to see whether they were randomly distributed in the DNA or whether they had patterns. We looked at maybe 100 or so traits where there had been genome-wide association studies for all sorts of different traits, associated with immunity or autoimmunity or behavior or metabolism, and other things.
For each of these we could ask: do the genetic variations that are known to affect these traits from genome-wide association studies have an unusual number of genetic selection signals? What we found is that there was a vast enrichment, by about four or five-fold, for immune traits. There was a super concentration of selected signals in immune traits. We also saw a strong enrichment for metabolic traits—things that might impact obesity or fat traits or Type 2 diabetes—and almost no detectable enrichment, as far as we could tell, for behavioral or psychiatric traits.
Dwarkesh Patel
Just to make sure I understand. This is not to say that behavioral or psychiatric or cognitive traits are not under selection. It’s just that the individual sites where such traits are controlled are not especially likely to be among the locations you’ve identified as under selection.
David Reich
That’s exactly right. It might seem from the results of that analysis that immune traits are highly selected and that there’s been no selection for behavior in the last 18,000 years in this part of the world. But that’s a wrong conclusion, and we have evidence that it’s a wrong conclusion. There’s clear evidence of selection also on behavioral traits.
The reason we think we see much weaker signals for behavioral traits is that behavioral traits, we know from medical studies, are underpinned by much larger numbers of genes than immune traits, which are underpinned by relatively small numbers of genes of strong
effect
. Behavioral traits are shaped genetically by a very large number of genes of weak effect, and we just don’t have the statistical power to detect these very weak signals.
When we do an analysis looking at our very strong signals of selection, that collection of very strong results is very effectively querying the immune traits, but is not very effectively querying the behavioral traits. It may still be the case, and I guess it is, that immune traits are the most selected category. But it is not at all the case—and we can prove it’s not the case—that behavioral traits are not selected.
Dwarkesh Patel
Interesting.
David Reich
We’ve been able to prove that there are two ways to reconcile the previous observations with our new observations. Remember, the previous observation is that natural selection seems to have been quiescent over a timescale of hundreds of thousands or many tens of thousands of years. Reason? That you don’t see 100% difference in frequency variance across Europeans and East Asians.
Now we’re seeing hundreds of positions that are rocketing up in frequency with selection rates of 1% or more in a lot of cases. A 1% or more selection rate will mean a rapid doubling over periods of dozens of generations. Over the 1,500 or 2,000 generations separating Europeans and East Asians, shouldn’t you see many genetic variants that are 100% different in frequency across populations?
We were able to show that this is explained by at least two factors. One is that in this part of the world—Europe and the Middle East—we are actually in a period of accelerated natural selection. One way to see this is to look at the enrichment pattern we’re observing, where immune traits are unusually associated with these selection signals. We could compare the last 5,000 years of our time period, what’s called the
Bronze Age
and further onward, to the previous 5,000 years. What we see is that this intensification of selection around immune traits, and similarly the intensification around metabolic traits, has accelerated over this time period.
It’s not like natural selection has been at the same rate over all places and times. It’s increasing over the time period we’re analyzing. Plausibly the whole time period has increased compared to previous periods. We’re in a period of intensified selection. That’s not implausible, because this is a population that went through a huge shock in terms of the way people live and the culture. Almost everyone we’re analyzing are farmers or food producers in one way or another. Farming was invented for the first time anywhere in the world in the Middle East 11,000 or 12,000 years ago. The people who invented farming exploded into Europe after 8,500 years ago, spread across the continent, and expanded rapidly.
In the Bronze Age, there was an intensification of how people lived, with much higher population densities. People were living more and more next to their animals and getting their diseases, and exchanging their diseases with the animals and with each other. This is a period of rapid change in how people are living, resulting in different biological needs of this population. It’s not surprising, perhaps, that in the context of these dramatic changes, the biology of the population might not be ideally adapted.
There might be what some people call an
evolutionary mismatch
, where you take a genetic variation that evolved in hunter-gatherers and put it into farmers or pastoralists, and it’s not exactly right. What you’re seeing is the DNA of this population, which descended from hunter-gatherers only 10,000 years ago, reacting to the shock of having been moved into an agricultural, Bronze Age, high-population-density, urban environment. A hypothesis is that what we’re seeing is the adaptation that occurs as a result.
Dwarkesh Patel
In the paper you have many examples of this intensification of selection around the Bronze Age. It might be helpful to go through some of these.
David Reich
One of the things we do in this work is look carefully at many of these positions in the DNA. We actually have an internet browser called the
AGES
browser, which Ali and a colleague of his—who’s a co-author of our paper—built. It allows you to query each of these 10 million positions and see the trajectories at each position and the evidence for selection.
One of the things we see is that, while for the most part the signals of natural selection we detect are consistent with constant natural selection over time, in a handful of them we’re able to see that there’s been a reversal or a radical change in natural selection. Very often that occurs in the period between 5,000 to 2,000 years ago, which is the Bronze Age and the
Iron Age
, a period of rapid population growth and rapid movement to intensive use of many technologies that were not used that way before.
An example of this is the
TYK2
genetic variant that is a major risk factor for severe tuberculosis, which is the most important infectious disease killer in the world today. If you look at this major risk factor for tuberculosis, this variant rockets up in frequency from 8,000 or 6,000 years ago to maybe 9% or 10% in this part of the world. Then it rockets down in frequency in the last 3,000 years. In both cases, there’s very clear evidence of natural selection, in the first case to increase in frequency, and in the next case to decrease in frequency.
A possible reason is the spread of tuberculosis. It maybe becomes endemic in the population 2,000 or 3,000 years ago. That’s potentially consistent with pathogen sequence data and other lines of evidence. And maybe this variant was protecting against something before then, but then tuberculosis became significant after that point, and it was so bad that it pushed in the opposite direction. That’s speculative.
Dwarkesh Patel
The thing it was protecting against was probably another disease?
David Reich
Maybe.
Dwarkesh Patel
One of the big takeaways for me from the paper was just that something weird happened in the Bronze Age. As you said, across trait after trait, the selection intensifies during the Bronze Age.
This makes sense for some things. For example, why do we see
lactase persistence
, where adults can process milk, intensified during this period? This is the time when we start using cattle not just for the meat, but also for milk and wool and other secondary products. So it makes sense why lactase persistence would matter more.
But then there are other things that seem like they should have been relevant since the dawn of agriculture. I forget the exact name of the allele, but was it
FADS1
, which helps convert plant fatty acids into long-chain fatty acids that your body needs? That’s obviously relevant when you move from a diet of meat as a hunter-gatherer to a diet of cereals.
That is also one I think you found was under especially high selection 5,000 to 3,000 years ago. So what’s going on? Why is the Bronze Age so special across all these different traits that you’re observing?
David Reich
So this FADS1/2 variant is a vegetarian/meat-eating adaptation. Already in work prior to this, Ian Mathieson, who worked with me in 2015,
identified this as a very strongly selected variant
. It’s actually ancient. You see copies in
archaic humans
too.
One of the findings of our paper is the
ABO blood system
. You get your blood typed as A, B, and O. The B variant has increased up to 10% at the expense of A, but previous work has shown that A and B were both already present in the ancestor of humans and gibbons and other apes. Some of these mutations have been going back and forth and fluctuating over different time periods.
But we’re talking about changes in the Bronze Age. The TYK2 variant for tuberculosis risk, a multiple sclerosis risk variant, inflected and increased in frequency before the Bronze Age, and then 2,000 or 3,000 years ago reversed in that period. There are differences in Northern Europe where this process is super strong, very strong positive selection, very strong negative selection. And then in Southern Europe, only a little bit, and not even very strong negative selection.
For
haemochromatosis
, which is pathogenic iron buildup that causes problems in Europe, that too has reversed around this period. In some of the complex traits that maybe we’ll talk about later, these traits too have periods of intensification of natural selection. For example, depigmentation: Europeans have gotten lighter skin over the last 10,000 years. You can see it in our data. The period of strongest depigmentation is between about 4,000 to 2,000 years ago, and then after that it’s much less.
This seems to be a very impactful, eventful, important period where a lot of the processes we are seeing become very powerful. It’s surprising on first principles. You might think, before you walked into this genetic data, that the big change is going to be starting to grow plants and maybe farm animals. That happens in the
Neolithic
, beginning 10,000-12,000 years ago, and spreads into Europe after 8,500 years ago. But actually, the intensification happens 5,000 years ago, 4,000 years ago.
It’s really interesting. This observation of that being an inflection point tells us something about when humans, at least in this part of the world, were wrenched into a way of living that was so different from how their hunter-gatherer ancestors lived that the organism had to adapt very strongly. It may be that the degree of that wrenching process moving into the Bronze Age was qualitatively greater than the degree of the wrenching process that happened from the initial transition to growing plants. That’s surprising, because our cartoon picture is that the big transition is farming. But the biological readout is saying our genome is reacting much more strongly to these events that happened 5,000 years ago.
Dwarkesh Patel
You did some work with Bhatia and many other colleagues in 2014 where you were
looking at 20,000 or 30,000 African American genomes today
. You were saying, “Look, there’s 80% West African DNA and then 20% European DNA. Can we look at their genomes today and see that their allele frequencies are much different than we’d expect from this admixture?” Correct me if I’m wrong, but you found that they weren’t.
That is to say, over 200 or 300 years of extremely intense environmental change—going from chattel slavery to a completely new environment—there’s no effect of natural selection. So we see episodes like this where we don’t see natural selection, but then the Bronze Age apparently must have had an even stronger effect, where the change in environment is even stronger than what we see from Africans in Africa being migrated to the New World and living under slavery.
David Reich
That may be the case. It also may be the case that that period is just too short to see much effect. In the Bhatia et al. paper, where we looked at about 30,000 African Americans, we looked to see whether—instead of the average percentage of around 80% West African ancestry—there were some places in the DNA with significantly more than 80%, or significantly less than 80%. That’s what you would expect if there were natural selection for some genetic variant from Europeans or from Africans.
We didn’t see any place in the DNA that was significantly different from what you would expect by chance. One possible explanation is just that there’s only a handful of generations, maybe five, over which natural selection would operate. So if the selection was 2% a generation, you would still only see a 10% compounded effect, and there’s just not enough time to detect it.
But the Bronze Age is not 300 years, it’s 3,000 years. It’s the power of compound interest, and you have enough time to begin to see a strong effect. This really, really does seem to be a very impactful time in terms of human history, and you can see it in our complex traits. Look at pigmentation, for example, which is the strongest signal of selection for a complex trait in our data set. You look at genetic mutations that are known to affect pigmentation. You add up their effect across all of the DNA, there’s dozens or hundreds of them. You look to see when natural selection is strongest, and the time period is really 2,000 to 4,000 years ago.
For some of these other traits as well, you see again that the time period over which selection is strongest is 2,000 to 4,000 years ago. For example, if you look at genetic variants that affect measures of cognitive performance, such as performance on intelligence tests in white British people today. This is of course a very strange trait to measure in the past because there were no intelligence tests and there was no school. But it is a predictor today, and you can look at how it’s changed in the past.
We see very strong natural selection for this combination of genetic variants that predicts people’s performance on IQ tests and is also highly correlated to the predictor of the number of years of school or the household wealth of people. All crazy traits in the past because there was no wealth in the past, there was no school in the past. But if you look at the predictors today, there is a strong movement in a systematic direction, a large effect, about a standard deviation on the scale of modern variation.
We can do this trick of looking to see whether there are periods of time when this natural selection has occurred more intensely or less intensely. We drag a 2,000-year window through our data, and we repeat our whole analysis, not on 18,000 years, but just on a short 2,000-year window. We can measure the strength of selection in each of these 2,000-year windows. What you see when you look at intelligence is that this maxes out in the Bronze Age, between 5,000 and 2,000 years ago.
The impact in the last 2,000 years is almost nothing. There’s no evidence of natural selection at all. Your bias coming into this, my bias perhaps, might be that if there’s any signal of natural selection on this trait at all, that it would be unusually strong in the last 2,000 years. Maybe this is a time of industrialization. Maybe this is a time of greater need for this particular trait. But in fact, there’s no evidence of natural selection at all in the last 2,000 years. There’s very strong evidence between 2,000 and 4,000 years ago, where instead of a one standard deviation strength of selection, it’s a two standard deviation strength, averaged over this time period.
Dwarkesh Patel
The standard deviation here is how much the polygenic score for the trait itself moves?
David Reich
How much the polygenic score for the trait moves over a 10,000-year period within a population that is held constant in terms of its ancestry. What we’re actually doing is looking in our data set at a heterogeneous group of people. There’s Southern Europeans and Northern Europeans and hunter-gatherers and farmers. At different times in the past, those groups are more or less represented.
The whole strength of the methodology Ali Akbari developed is that it corrects for that changing ancestry over time. Really what’s being asked here is that we’ve divided up our whole data set into an archipelago of little populations in different places in space and time. We’re asking in each place in space and time: a little pocket of people in Britain from 4,000 years ago to 3,500 years ago, a little pocket of people in Hungary, a little pocket of people in Italy from 2,000 years ago to 1,500 years ago. In each of these places, where the ancestry is relatively similar without being too disrupted in that short period by migrations, we watch to see if the genetic changes blow in the same direction. We’re measuring the strength of selection at each point in time after correcting for the big population changes that have occurred.
Dwarkesh Patel
The effect here is huge then. One standard deviation above the median would be somebody in the 85th percentile. You’re saying the effect of selection has been so strong that comparing 10,000 years ago to now, the median has gone to the 85th percentile. That’s just a huge effect over the last 10,000 years on something like intelligence or the thing that predicts household income.
Especially given that this is only 2% of the change in allele frequencies, and the 98% is coming from migration… It’s stupendous to think about what the impact of migration is, if this alone is driving a standard deviation change in these kinds of qualities, at least among the kind of variation we see in the world today.
David Reich
One thing you can see in the data is that the migration impact is huge. For example, if you look at the trajectory for measures of cognitive performance—scores on intelligence tests in white British people today—but you look at the predictor of that in people in ancient times, the estimate for the hunter-gatherers of Europe is three standard deviations below the modern mean. So that’s hugely different.
Then you see a huge jump from them to the farmers, who are at the mean, at zero. That’s migration. What you’re seeing is that those two groups had different set points for those traits. And then the steppe pastoralists have a lower set value.
You see huge fluctuations in the predictor of this trait over time. That doesn’t prove selection. That’s just migration. But what our test is telling you is: in addition to those fluctuations due to migration, is there a consistent effect of natural selection blowing the trait in the same direction over all places and times? That’s what we’re detecting.
Dwarkesh Patel
There’s this theory called the
collective intelligence hypothesis
, which is the idea that selection for intelligence has actually been in the opposite direction. As society has developed, there’s been more specialization, and if there’s more specialization, each person only needs to understand a smaller and smaller part of the world. Therefore, the ancients were actually much smarter than us, and we’ve evolved down in intelligence.
Your results seem to point in the opposite direction. Although there hasn’t been selection in the last 2,000 years as society has gotten more complicated, at least when society began, there was more need for the kind of thing that predicts intelligence today.
The reason that’s surprising is, if you think about hunter-gatherers—reading your colleague
Joseph Henrich’s
book
—the amount of information they needed to hold onto and assess, everything from how to process food, to how to build shelters, fire, et cetera, compared to my world, where I just need to know how to set up mics and ask questions… It seems like the demands on intelligence should have been way higher in the ancestral environment. So it’s very surprising that the beginnings of civilization increased the selection on intelligence.
David Reich
This is the power of data. I think if you asked Joe prior to this work what the hunter-gatherer selection would be and where their set point for this particular trait would have been… I think he probably wouldn’t have made a very strong prediction, but he would have said, “Maybe you would have expected it to have a high predicted value of this trait because these people were really having to do a lot of things and figure a lot of stuff out. Maybe once you have more complex societies, there would be more of a collective brain, and maybe there’d be selection against this trait.” In fact, it’s the opposite in some ways.
It’s the power of data. It’s not what you expect.  It’s actually the value of data to try to make sense of all these things. It’s very interesting. The genetic predictor of intelligence, there are lots of things that are confusing about it, so it’s worth talking about. Or the
genetic predictor of years of schooling
, which is highly correlated to it and is measured even better.
If you look at the genetic predictor of years of schooling, there’s another
amazing study from 2017
from a group in Iceland that looked at this measure over the last hundred years in Iceland. It looked at older people and younger people born more recently. There’s an estimated 0.1 standard deviation decrease in the genetic predictor of intelligence in Iceland just within one century. It’s an absolutely huge effect over a short period. This is selection against years of schooling. If I said intelligence, I didn’t mean to. It’s selection against the genetic predictors of the number of years of school.
One possible interpretation of this—hand-wavy—is that what’s being measured here is not selection for years of schooling or for real intelligence, but for another trait altogether that’s correlated to both of them. For example, the predictor of the number of years of schooling is very strongly correlated to the age at which women have their first kid. If you control for that, all of the signal of years of schooling goes away. So maybe what you’re measuring is women’s decision about when to have children.
If you have children earlier, you don’t go to school as much. If you have children later, you go to school more. Maybe it’s some kind of measurement of delaying gratification or putting things off or planning. The same trait is correlated to body mass index, to obesity, and to walking pace. So is this really intelligence as we think about it, or is it something else that manifests itself differently at different times in the past?
Dwarkesh Patel
Obviously, a trait like years of schooling was not itself a meaningful thing in the past. The underlying things for it seem to have been under strong selection. Whatever in the genome predicts years of schooling seems to have been under strong selection. How should we think about this? What’s the actual thing that’s changing in the genome?
David Reich
There are two things going on that you need to think about. Years of schooling is connected to so many other things genetically. If you look at the genetic predictor of years of schooling—this trait has been measured in millions of people now—it’s correlated to really surprising things. It’s correlated to the age at which women have their first kid. It’s correlated to people’s obesity. It’s correlated to people’s walking pace. It’s correlated to people’s household wealth. It’s correlated to a variety of other traits that seem quite different from it.
If you think you’re actually measuring the genetic prediction of intelligence, or actual studiousness, you should think again because there are many things that it’s correlated to. There seems to be some kind of general trait that you could maybe think of as
executive function
or a propensity to defer gratification—I’m just waving my hands—that is under selection. It pushes all these traits in the same direction one way or the other, and at different times in the past, it’s advantageous or disadvantageous.
When we found this signal of the genetic propensity to go to school for more years as it manifests itself in white British people today, we were incredulous. How could this be? Maybe this is a problem. So we did a few tests to try to figure out whether this was real. One of the tests we did was that we looked for a study where this measurement of the number of years of school was done not in Europeans, but in Chinese people in China. We looked at the effect size of many variants as they affected the number of years of school in China, and we saw whether they had a correlation to the trajectory of those same genetic variants in Europeans over the last 10,000 years.
These are two parts of the world where the populations have been essentially completely disconnected. There’s no way by chance that the trajectory in Europeans over the last 10,000 years would have anything to do with the effect on years of schooling in China today. But there’s actually a huge statistical correlation, a five or six standard deviation correlation between the effect size of variants on the number of years of school in China today and the trajectory in Europe. It’s just as strong, actually, as the effect size of variants in Europeans on years of school to the trajectory in Europeans. We just could not see a way this could happen by chance. Once we saw that, we felt quite convinced that this was a real signal and that somehow there has been natural selection to increase the genetic changes that today manifest themselves as predicting more years of schooling.
Dwarkesh Patel
Just to make sure I understood, you’re looking at this ancient DNA in Europe. You’re saying it seems to predict years of schooling for modern people in Europe, or at least selection on that ancient DNA seems to predict more years of schooling in modern Europe. You also find that the same variants predict more years of schooling for Chinese people in China. So this is not just some weird artifact from the way these
GWAS
were done in Europe. These parts of the genome seem to robustly predict the kind of thing that actually leads to more years of schooling, at least in people today.
David Reich
Correct.
Dwarkesh Patel
Stepping back, I want to understand what this tells us about what actually changed in our environments over the last 18,000 years. We talked a little about what happened after the Bronze Age. We were talking about this during the collective intelligence part of the conversation. It’s surprising to me that things like intelligence, or lack of schizophrenia—things that just seem robustly good—were not maxed out before the Bronze Age.
The diversity among different populations was so big that you have the European hunter-gatherers having three standard deviations less predicted value for what they would score on an intelligence test if it existed. But they were existing in the real world in a place where intelligence matters.
How can it be that this was not a trait… You just look at the human body or any animal, and evolution has been acting on it so strongly to make it functional for the things it needs to do. And this one thing, which seems so relevant—especially to what human hunter-gatherers needed to do—doesn’t seem to have been under that strong selection in the
Mesolithic
or
Paleolithic
eras?
David Reich
I think that’s a great question. As we talked about before, selection is very effective. It can move the mean value of traits within hundreds or thousands of years in one direction or the other if that’s adaptive in a particular environment. So you might wonder, isn’t intelligence good in all contexts and places in time? There are a number of ways to think about that.
First of all, we are speaking from the point of view of a society which intensely values this particular trait, the ability to score well on IQ tests or things like them, or to go to school for a long time. I think it’s unprecedented in human history that we live in a time like this. If you look at the Hebrew and Christian Bible, and you look at how much intelligence is valued, it’s basically not at all.
Dwarkesh Patel
But when the Bible was being written,
especially the Old Testament
, that’s exactly when selection for intelligence is at the highest point it’s apparently ever been.
David Reich
Exactly. But there it’s about strength or courage or religiosity. Those are the values. If you read
Homer
or the texts of other religions, it’s not intelligence. It’s beauty and other things. This value system which has a hyper-focus on smarts is not obviously a trait value that’s been common in the past. You might think that in certain communities there might be valuation of things that are more proximate to years of schooling. But really broadly, it’s not been a high value in the population.
Dwarkesh Patel
Obviously, the thing we care about is not direct performance on an IQ test, especially in the past. The thing I’m trying to understand better is intelligence more broadly. Maybe IQ-test intelligence is just not that correlated with, “Here is a new-world environment, go figure out how to process food there and make shelter and everything else.”
Your colleagues like Joseph Henrich have talked about how modern people underestimate the difficulty of doing this kind of thing with a small band of people. Maybe that’s not IQ-test intelligence, and that’s why we don’t see that strong a selection effect on this thing. But intuitively, regardless of the value system, it just seems very valuable to have this trait maxed out.
David Reich
I’m being very speculative. Let me give you two examples of how I’m thinking about this, not that I’m a particularly good authority on these things. As I mentioned, a lot of these traits, which are quite disparate, are highly correlated to each other. Obesity, years of schooling, walking pace, performance on IQ tests, household wealth, all these crazy traits seem to be governed to a substantial extent by a shared combination of genetic variants.
Let’s think about what this might mean. In Iceland in the last hundred years, there’s been selection against this combination of variants. One possible interpretation is that it’s basically selection for two ways of investing in your children: having many kids and not investing a lot in them, or having few kids and investing more in them. If you invest in deferring having kids, having more wealth, having more resources, and putting more into each kid, you’re going to have lower fertility and fewer kids. That’s going to result in lower fertility, but those kids might survive more and do better in society. Alternatively, you can just have as many kids as you can and invest less in them. They might individually have less good outcomes, but in a time of plenty—which is potentially Iceland in the 20th century—it might make sense to have more kids and invest less in them.
There’s a toggle between having more kids and investing less in them, and having fewer kids and investing more in excelling in various ways. You can imagine that at different times and in different places… In ecology, there are different ways. Mammals often invest a lot with a pregnancy and a small number of children, whereas fish will spawn huge numbers of offspring into the river, the great majority of whom will be eaten. But that is an effective way to produce offspring in certain conditions. So there will be a toggle depending on the environmental conditions back and forth between investing in large numbers of offspring with less investment, or smaller numbers of offspring with more investment. Maybe we’re just seeing that move back and forth over different places and times.
Similarly, for schizophrenia and bipolar disease, how could this ever be advantageous? Maybe what we’re seeing with these diseases is a readout of some spectrum of traits that in some contexts might be advantageous. Maybe being anxious, imaginative, or neurotic might be helpful in a shamanistic tradition or a religious tradition which values people who can have visions or be creative. Maybe these are subclinical versions of schizophrenia or bipolar disease that in certain times may be advantageous and in other times may be disadvantageous. You might just be seeing selection for different types of creativity or other thinking that can be valuable in different contexts.
I’m waving my hands here, but my sense is that these complex traits have not pushed in one direction because there are advantages to both ends of the spectrum, and there are multidimensional impacts of these different traits.
Dwarkesh Patel
Julian Jaynes
has this famous theory in
The Origin of Consciousness in the Breakdown of the Bicameral Mind
. I’m butchering this, but fundamentally, the way I understand it is that up until Homer, basically everybody was schizophrenic. People genuinely thought that gods were real people that you were communicating with. His claim is that ancient texts seem to show people behaving in this way.
David Reich
You’re being asked to believe in visions. Even today, there’s valuation in some religious communities in communicating with God, having visions, and having supernatural communions. So I just don’t know.
But I think it’s super interesting to ask the question of why certain traits are not always advantageous. For schizophrenia and bipolar disease, there is a sense in which most of the mutations are disadvantageous. We can see that from the patterns of variation, where the variants that are risk factors tend to be low frequency and they tend to be small effects.
Dwarkesh Patel
So another trait you find under selection is the trend away from body fat since the
agricultural revolution
. Why is that?
David Reich
What you see is a reduction in the combination of genetic mutations that make you at risk for obesity, body mass index, and similarly very correlated to it, higher fat mass, higher waist-to-hip ratio, and higher type 2 diabetes risk. There is clear selection, by about a standard deviation on the scale of modern variation for these traits, reducing over the last 10,000 years in this part of the world.
What can be going on there? Why wasn’t there selection for this combination of traits before? There’s a longstanding idea known as the
thrifty gene hypothesis
. The idea is that once you have hunter-gatherer populations that move into a farming environment where there’s plentiful food, there is no longer a need to the same extent to be able to build up body fat to survive in times of stress, because there are more constant stores of food.
As a result, there will be natural selection against body fat once you move into an agricultural environment and into periods of food plenty. Maybe what you’re seeing is that this group of people in Europe and the Middle East over the last 10,000 years has moved into a period of relatively more stable food, where building up stores of fat is not as advantageous, and there’s been selection against this combination of traits. Europeans are actually relatively better protected genetically against type 2 diabetes than some other populations around the world, like African Americans and Native Americans, that have perhaps not been exposed to agriculture for as much time. So you may be seeing the effect of more exposure to more stable food accessibility.
Dwarkesh Patel
This is also another way in which the data go against a common story. The common story is that hunter-gatherers actually had much more stable diets because they were more varied, and they weren’t reliant on a single cereal or crop for their calories. If one game went away, they had other things they could scout for. They could move locations more easily because they weren’t tied down to the land. So they were more food-stable. But if there’s been selection against storage of body fat, that suggests that as unstable and as common as famines might have been in agricultural societies, it’s at least more stable than what the hunter-gatherers had.
David Reich
There’s a timescale issue. You’re absolutely right. As I understand it, I’m no anthropologist, when there’s a hunt in traditional societies or communities that hunt, people will often gorge themselves, eat a huge amount, build up a temporary store of fat, and then go multiple days without eating meat until the next hunt. There is this boom-and-bust access to high-value nutrition that is not true to the same extent in farming communities.
On the flip side, famines are something that occurs more commonly in agricultural societies, but the timescale and the tempo of them is very different from the hunting tempo. Maybe there’s a famine every three years. Indeed, if you look at the bones of farmers, at least in some communities, there’s more stress in them, maybe due to a famine every three years or every five years. But selection might not be acting on that three-year time period. Your fat store from the latest hunt is not going to carry you through to the famine three years later. Survival of famines is a different thing than building up body fat to be able to survive two weeks later.
Dwarkesh Patel
A random question I have. You were mentioning that compared to these other things which matter much more for fitness in the ancestral environment—the immune system, especially after the Bronze Age—all these other things have mattered more than intelligence. They’ve been under much more selective pressure than intelligence.
That makes you wonder whether there’s much more room at the top for intelligence. If humans had been selected especially for intelligence, they could have been much smarter. The reason that’s relevant is that we’re currently building AI systems, which we’re trying to make as smart as possible. In fact, the only goal of the training process is intelligence. We don’t have to worry about at the same time making their immune systems powerful—
David Reich
We have lots of energy to spend on it.
Dwarkesh Patel
And at the same time making sure they’re not schizophrenic. I guess we kind of do worry about that. But if intelligence has not been the dominant trait under selection for humans over the last 10, 20, or 100,000 years, does that mean there’s more room at the top for this trait?
David Reich
I think there’s more room at the top for a lot of these traits. You can move height extremely in one direction, much more than it is today. You can move any of these traits much more extreme in the other direction. There are probably very strong negatives to doing that. You’re probably sacrificing other things, and there are trade-offs. But it’s highly likely that if natural selection pushed any of these traits more in one direction than it is, the mean would move.
Dwarkesh Patel
So all of this evolution since
“Out of Africa”
is acting on alleles that already existed in the pool of human variation from that first group we were talking about last time, on the order of 10,000 people, that exploded out of Africa. Is it surprising that across all these different traits, from cognitive profiles to disease resistance to height, that one pool of people contained so much latent variation that they could supply enough stretchiness to accommodate all of these different traits you’re studying now?
David Reich
That’s a rich question, and I think the human population has within it a tremendous amount of variation for complex traits. There’s a huge amount of variation that affects height. There’s a huge amount of variation that affects body mass index. If you take all these mutations and set them to the high-height variant, a person will be extremely tall, like as tall as a tall building. Of course, that will never happen.
But if you take all these variants that affect schizophrenia risk and you point them all in the same direction, there will be extreme risk or extreme protection for schizophrenia. For complex traits, ones underpinned by many mutations, all the variation already exists to move the population to a different adaptive set point that’s optimal in the environment it’s in.
If you push the population into a new environment, within hundreds or thousands of years, the population can rapidly move to a new adaptive set point. There are some unusual traits, like the
ability to digest cow’s milk
or protection against sickle cell anemia, that require a single very important mutation that may not yet exist in the population. You have to wait for the mutation to occur in some people. When the populations are relatively small, only 10,000 people, you might have to wait dozens or hundreds of generations for that mutation to arise. But when the populations are large, there’s no mutation limit anymore.
Every mutation that can occur does occur. There are eight billion people in the world. There are maybe 30 new mutations every generation, so that’s 240 billion new point mutations every generation. There are only three billion DNA bases in the genome, so every mutation that can occur does occur about 100 times every generation. We’re not mutation-limited anymore. The mutations can arise again. They do arise again. But when the population is only 10,000, you sometimes have to wait dozens or hundreds of generations for the new mutation to occur.
Dwarkesh Patel
How likely is it that the thing that changed with the Bronze Age is just that the human population was big enough? By 3000 BC, you go to a population of 50 million-ish people. The population is big enough, and the
gene flow
between different areas is high enough, such that things which don’t have an overwhelming selection coefficient, which aren’t overwhelmingly favored by evolution, are finally visible to selection.
David Reich
I think that’s not likely to be true, but it’s an extremely interesting thing to think about. Already when population sizes are on the order of a million or so, every mutation that can occur does occur within a few generations. That’s well before the Bronze Age if you take the population even of a place like Europe, but also of other places. Or maybe it’s at the dawn of the Bronze Age or the farming period. The question you’re asking is whether, when the population is small, maybe natural selection doesn’t work effectively.
A common thing people think about with natural selection, which is true, is that in small populations selection doesn’t work effectively. That’s because mutations bop around in frequency from generation to generation a lot in a small population, just randomly. If you have a population size of 1,000, mutations will bop around by a frequency of one over 1,000 every generation. If the selection coefficient is less than that, it will be drowned in the random bopping around of frequencies due to genetic drift. But that is already for a population of 1,000. A 0.1% selection coefficient is very weak. We’re talking about 1% effects, and that’s very strong. It will work very well even in a population of size 1,000 or 10,000.
If you are talking about mutations of the type that will start rising only in large populations but not small populations, those are selection coefficients on the scale of one over 10,000 or one over 100,000. Those will take 10,000 or 100,000 generations to rise in frequency, which is hundreds of thousands or millions of years. That’s not going to do anything over the timescale we’re talking about. There’s just a timescale issue. We’re talking about strong, measurable selection coefficients on the order of half a percent or more in this study. All of those are going to work in small populations or large populations. It’s not going to be affected by the population size.
Dwarkesh Patel
Interesting. You’re saying that more generally, once you hit a given threshold of population, the dominant factor is time span, not population size.
David Reich
Correct. It’s very interesting, and it’s actually not widely understood.
Dwarkesh Patel
Speaking of data contradicting what you might have otherwise assumed, one of the papers you sent me beforehand,
Mallick 2016
, found that there are no fixed differences between modern and archaic humans 50,000 years ago. We know this is the period in which the so-called cognitive revolution happened, and modernity started, and
people are making art
. Does this suggest that nothing biological changed to make modern humans modern? The thing that happened was some cultural change? How do we understand what this data tells us?
David Reich
Right. 100,000 to 50,000 years ago, there’s a quickening of the pace of change in culture. You see the first extensive representational art, bead necklaces, drawings on the wall, and a rapidly increasing pace of innovation in the types of tools that people use. The thought might be that there would have been some important genetic switch, a kind of important genetic change that occurred in the population and swept to high frequency that everybody soon had. That made it possible to do these things. Maybe some genes allowed people to have complex, representational language, for example.
One thing we did in 2016 in this paper by Swapan Mallick and colleagues was look across the DNA for places that might be expected to look like this, where nearly all people living today share a common ancestor maybe 100,000 or 200,000 years ago. We looked really hard, and right across all the DNA we could look at, we couldn’t find anything more recent than four or five hundred thousand years ago.
This is a crazy result because it looks like there are no key selective sweeps that have occurred in this period that are ancestral to everyone living today. We talked before about no selective sweeps between Europeans and East Asians, but there don’t even seem to be any selective sweeps shared between all humans in this really important period when a lot of evidence in the material culture record appears. It could be that there’s biological adaptation in this period, but it’s polygenic. There are lots of mutations that all shift in the same direction to help the population move to a new set point, but there’s no key biological change that rises to high frequency in this time.
Dwarkesh Patel
This group 50,000 years ago, are they the ancestors of everybody out of Africa or also some Africans?
David Reich
This is 100,000 to 50,000 years ago. This is the population that’s ancestral to West Africans, to most East Africans, to all non-Africans.
There are a couple of populations in Africa that have substantial ancestry coming from more divergent groups. For example,
Khoisan
from Southern Africa or Central African rainforest hunter-gatherers have substantial fractions of their ancestry from groups that diverged maybe 200,000 years ago from the other lineages. But all of these groups today are able to go to college and do everything everybody else does. There is no evidence that there is any key mutation lacking in some groups that is not present in the others.
Dwarkesh Patel
The differences we see between different groups of people, especially if this group 50,000 to 100,000 years ago had a very small population size… I think last time we were discussing on the order of 10,000 people. So almost everybody in the world, or the variance we see between different humans today, was latent in this group.
I get your point that if you just stack up different things across the genome, stacking them up really has a big effect. But it’s interesting that we have so many different groups in the world today, and all that diversity comes from a very small population size.
David Reich
A lot of us in human genetics think that our population contains within it the clay that’s needed to make almost any trait. And that depending on environmental conditions or selection conditions, the mean value of these traits will move in different directions. There’s an empirical question about how much selection there’s been in different human populations over time.
One of the things this new work we’re involved in is showing is that at least in the last 18,000 years in this part of the world, there has been significant movement, at least for a handful of important traits. We looked at more than 500 traits. About 100 complex traits showed significant movement in a systematic direction over this time period. It really does seem that there is a response to the environments people are living in that has occurred over this period, and that is potentially stronger than in previous periods.
Dwarkesh Patel
We were talking earlier about how there are no fixed differences between humans 30,000 years ago and humans today. So if there’s no genetic basis for the kind of thing that allowed humans to have more symbolic representation, have farming, et cetera—I think I asked you this question last time we talked, but especially with this context—why no farming before the
Ice Age
? Genetically we were there.
David Reich
That is such an interesting question. Genetically we’re there. The common ancestral population has all of the ingredients for farming 50,000 years ago. These people are distributed into different parts of the world:  the Americas 15,000 years ago or whatever it is, New Guinea 40,000 years ago, East Asia, Europe, West Africa. No farming developed before 11,000 or 12,000 years ago. It only developed in the last 12,000 years, the period known as the
Holocene
, which is the end of the Ice Age.
If you talk to climate scientists and archaeologists—I keep asking people this question every time I meet someone who’s an expert in this—how can it be that farming develops in all these places? Are we really living in such an unusual time? People tell me, indeed, we’re living in a very unusual time on a scale of two million years. That is, 12,000 years ago we switched into this period of not just warmth, but climate stability.
It’s hard to believe that we’re living in such a special time. But if you look at data from the bottoms of ponds where you can measure the fluctuations of temperatures using isotopic signatures, apparently we’re in a period where it’s fluctuating a lot less year to year, 10 years to 10 years, and 100 years to 100 years. It’s a period of relative stability that we are miraculously living in.
When this period of relative stability happens, it follows that multiple groups independently turn to agriculture, even though they all have the same genetic complement that arose 50,000, 100,000, 200,000, 300,000 years ago. It’s a crazy observation that people just accept, but it’s unbelievable.
Dwarkesh Patel
Oh, so you increased the range there. You said 100,000, 200,000, 300,000 years ago. Based on the genetic differences between modern people and people from 300,000 years ago. Do you basically think they’re modern 300,000 years ago?
David Reich
I don’t know. This is actively what I’m thinking about all the time right now. There’s a big transformation in terms of the culture of humans 300,000 or 400,000 years ago: this invention of
Levallois technology
, the ability to make stone tools out of cores.
The
Middle Stone Age Revolution
, or the
Middle Paleolithic Revolution
depending on what you call it in Africa or Eurasia, is a new way of making stone tools that’s shared by
Neanderthals
and by modern humans, but is not shared in East or South Asia. It’s a big change, and it presumably involves a cognitive change in order to make this sort of technology.
Then there’s a further change to the
Upper Paleolithic Later Stone Age
, maybe 100,000 to 50,000 years ago, when there’s a second transition with a new type of tool making, but it’s not as revolutionary as the earlier one. So when the cognitive leap happens is unclear.
The diversification of the lineages leading to people living today, like Khoisan Southern Africans and rainforest hunter-gatherers, all occurs more on the timescale of 300,000 or 200,000 years. All of these people are capable of going to college and doing everything. So it’s not obvious that the cognitive toolkit, the behavioral toolkit, and the genetic abilities were not all in place 200,000 or 300,000 years ago, and that even Neanderthals had them. It’s not obvious that this was not the case.
I just don’t know. You distribute these people descended from this diversification that happened 200,000 or 300,000 years ago to different parts of the world, and then after 12,000 years ago, you start having agriculture popping up in different places. It’s an outstanding mystery of human history. I find it unbelievable that we live in a time period that climatologically is so unique on a scale of two million years, but my colleagues tell me it’s true.
Dwarkesh Patel
The climate thing seems surprising given there are so many different environments in which agriculture was independently developed. I understand that across environments the variance could have gone down. If it had only happened in one place at one time, I could have bought that explanation. But the fact that they’re making maize in the New World and they’ve got cereals in the Old World in very different environments makes it surprising.
David Reich
It’s very, very surprising. We accept it, but it’s a crazy observation that most normal people don’t realize.
The thing that basically everybody accepts is that the common ancestral population of almost everybody in the world, except for rainforest hunter-gatherers and Khoisan, is around 70,000 years ago. Everybody accepts that these people all have in place the cognitive, behavioral, and intellectual ingredients that are necessary for the farming revolution and building state societies. Because when these descendants get distributed to West Africa, East Africa, the Americas, Europe, South Asia, East Asia, New Guinea, and so on, their descendants all do this. They do it independently, semi-independently, or demonstrably completely independently in all these different parts of the world.
The cognitive resources for doing this must have all been in place, but it’s a very long fuse. It delays for 40,000 or 60,000 years in all these different places after the common ancestral population splits up, and then ignites into agriculture and all these other things after that point.
It’s a crazy claim. Then you could argue about whether the actual fuse is 300,000 years, from when Neanderthals separated and from when different lineages of extant modern humans separate, and that’s also plausible. It’s a crazy set of things that we’re being asked to believe.
Dwarkesh Patel
Is it possible that agriculture existed, but you didn’t have modern metallurgy or whatever it was that allowed populations to explode starting in 5000 BC with the Bronze Age? Population-wise, it doesn’t seem like much is happening from 10,000 BC to 5000 BC in the early Neolithic. Is it possible that they had farming but they didn’t have copper or tin, which you needed to go to the Middle East for, to develop a civilization that could make use of bronze at a large scale, and so they just disappeared from the historical record?
David Reich
I think we would see their archaeology. There are extraordinary developments in the Americas which are entirely Stone Age.
Dwarkesh Patel
You would see them today if they had completely vanished?
David Reich
Oh, yeah. We should go for a trip to Teotihuacán in Mexico. It’s so impressive. When I went there when I was 20, it was totally as impressive as ancient Egypt. It’s huge. It’s massive. It’s without metal.
Dwarkesh Patel
It’s even more impressive because it’s not only without metal, but without animals and without wheels, which is crazy. The marble is just hauled without wheels.
David Reich
Right. Take any person who has an old world superiority and take them to these places, and they will not have it anymore. It’s just extraordinary what’s in these places. These are people who separated 20,000 years ago at least from the ancestors of East Asians and 40,000 years ago from the ancestors of West Eurasians.
They just had the same biological and cultural shared toolkit from then, but there’s a long fuse delay until all this stuff happens. It’s an amazing thing, and we don’t question it.
Dwarkesh Patel
What are other questions you are either investigating right now or want to investigate, these kinds of big picture questions of human history?
David Reich
I’m perplexed. I don’t know if we talked about it before, but I remain very confused about the relationships between archaic and modern humans.
We have genome sequences now from archaic humans who lived in Europe, West Eurasia, and Central Eurasia, and the Neanderthals. We have archaic sequences from these enigmatic
Denisovans
, who we now have a skeleton for since we last talked. There’s now a
skull that’s been shown to be a Denisovan
. We have data from lots of modern humans, and there are really big mysteries about the relationships amongst these groups.
Genetically, the Denisovans and the Neanderthals are sisters. They descend from a common ancestral population 500,000 or 600,000 years ago. That group descends 700,000 or 800,000 years ago from the common ancestors of modern humans. Genetically, the whole genome data says that Neanderthals and Denisovans are archaic humans from a common ancestral archaic population.
But there are so many things shared between Neanderthals and modern humans that don’t seem to be shared with East Asians. They both share Middle Stone Age stone tools, Levallois technology, this cognitively unique way of making stone tools that wasn’t used in East Asia. They both have the same
mitochondrial DNA
and
Y chromosome
sequence.
The Y chromosome sequence of Neanderthals and the mitochondrial DNA of Neanderthals, is actually modern human that came through interbreeding 200,000 or 300,000 years ago and then shot up to 100% frequency. Neanderthals and modern humans are both the
product of mixture events
that happened between archaic and modern humans 300,000 or 200,000 years ago, demonstrably through patterns of variation in ancient and modern DNA.
It feels that there’s something shared between Neanderthals and modern humans that’s not shared with Denisovans, even though the vote of the whole genome says that Denisovans and Neanderthals are related. One wonders whether there’s something connecting Neanderthals and modern humans that’s different from Denisovans, even though genome-wide, Denisovans and Neanderthals cluster. I’m thinking about that all the time now.
Dwarkesh Patel
Connecting them would be interbreeding events or being in the same place at the same time that we missed?
David Reich
There’s a
known interbreeding event
from the lineage leading to modern humans into Neanderthals, but it’s supposed to be only 5%.
I’m interested in the possibility that that 5% is actually a sign of something much more impactful, that somehow Neanderthals are in some sense deeply modern in some ways, and even though they get swamped by archaic genes, they actually have more of a modern impact than one would think. The Middle Stone Age and Middle Paleolithic Revolution that they share with modern humans is more fundamentally a part of who they are, in some sense, than we think.
Dwarkesh Patel
Interesting. Sorry, when was this interbreeding event?
David Reich
300,000 to 200,000 years ago.
Dwarkesh Patel
So the common ancestor between Neanderthals and most humans alive today is potentially more recent than the common ancestor between all humans alive today.
David Reich
Oh, for sure.
Dwarkesh Patel
Which is crazy.
David Reich
Well, the divergence to all the archaic humans, including Denisovans, is within human variation.
Dwarkesh Patel
Wait, what?
David Reich
Yes. The average time to the common ancestor of any two human genes is one or two million years ago. If you look at the copy of chromosome 3 you get from your mother and the copy of chromosome 3 you get from your father, the typical time they share a common ancestor is one or two million years ago. That’s before the split from Neanderthals and Denisovans. So there are many places in your DNA where you’re more closely related to a Neanderthal on your mother’s side than you are to your father.
Dwarkesh Patel
I’m sure there’s a simple explanation, but how?
David Reich
It’s the same reason that if you have a sister, in some places in your DNA you’re more closely related to her than you are to me because you share a parent. But in other places you’re more closely related to me than you are to your sister because you happen not to share the same DNA from your parents.
It’s just that the DNA we get from our common ancestral population was already quite variable 500,000 years ago, 700,000 years ago, a million years ago, and some of us descend from some of those ancestors and others descend from other of those ancestors. Neanderthals split from our lineage really close in time on human evolutionary timescales, such that in some places in our DNA we’re more closely related to Neanderthals than to each other.
Dwarkesh Patel
Interesting. What are the other big questions?
David Reich
That’s the main thing I’m thinking about a lot these days. I continue to be very obsessed with questions about the spread of human populations around the world and trying to reconstruct that with ancient DNA.
The thing I’ve been thinking about a lot recently is the possibility that maybe we’re not thinking in the right way about the relationship between archaic and modern humans. The standard model is one where Denisovans—these archaic humans that were found from ancient DNA—and Neanderthals descend from a common ancestral population 500,000 or 600,000 years ago, and these two separate earlier, maybe 700,000 to 800,000 years ago, from the ancestors of modern humans, people like us. That’s the big result of a lot of studies since 2010.
But there’s also evidence of an interbreeding event that happened maybe 200,000 to 300,000 years ago that resulted in modern humans contributing DNA to the ancestors of Neanderthals. So maybe 5% of the DNA of Neanderthals comes from this interbreeding event, and a lot of studies have shown this. I’m very interested in this because, from the archaeological record, Neanderthals and modern humans look quite similar to each other, much more similar to each other than a lot of them do to Denisovans, these archaic humans in East Asia.
For a lot of history, people have thought that Neanderthals are our sisters. But in 2010, the sequencing of the Denisovan genome made it very clear that on average,
Denisovans are closer to Neanderthals than to modern humans
. This was a very confusing result. Most people now think that Neanderthals and Denisovans descend from a common ancestral population that separated earlier from the ancestors of modern humans.
I’m interested in the possibility that the right way to think about Neanderthals is actually as somehow culturally modern humans, even though genetically they’re mostly Denisovans. The model I’m thinking about is motivated by this archaeological phenomenon known as the Middle Stone Age Revolution. If this is Africa and this is Europe, we know that the new way of making stone tools—with cores that were very carefully mined far away from the locations they were used, made out of high-quality stone like flint—starts being used 300,000 or 400,000 years ago, first in the Caucasus, places like Georgia today, or East Africa.
This way of making stone tools is quite revolutionary. It is known in Europe as the Middle Paleolithic and in Africa as the Middle Stone Age, and is associated with much more widespread use of fire and moving stone around at much further distances than before.
I’m interested in the idea that this is something shared between modern humans and Neanderthals. There’s somehow some shared cultural feature that’s absent in East Asia, and that might have a relationship in the genetic data and is somehow related to this 5% DNA.
The idea I’m interested in is the possibility that there is a population here that invents the Middle Stone Age and the Middle Paleolithic, sometimes called Levallois technology, and that people from this population expand into Europe and mix with the local archaic humans who are there. That is what this 5% interbreeding event is. It happens 200,000 to 300,000 years ago. It produces a group that, as it expands across this landscape in Europe, mostly picks up the local DNA and becomes mostly archaic genetically, but retains its modern human culture, the way of making stone tools and some of its traditions.
One of the things that’s super interesting about this is that if you actually look at the genetics, across the whole genome, Neanderthals and Denisovans cluster. But if you look at the mitochondrial DNA—which humans and Neanderthals get from their moms—Neanderthals and modern humans cluster. If you look at the mitochondrial DNA, Denisovans and modern humans share an ancestor well more than 700,000 or 800,000 years ago, as you’d expect from the history. If you look at the Y chromosome that you get from your dad, Denisovans and modern humans share an ancestor more than 700,000 or 800,000 years ago, which is consistent with this history.
But if you look at the Neanderthal mitochondrial DNA, it’s only 300,000 to 450,000 years. If you look at the Y chromosome, it’s only 300,000 to 450,000 years. What the current genetic work is asking us to believe is that even though this is only 5% of the whole genome, it introduces mitochondrial DNA and Y chromosomes, and they jump up to 100% frequency. It’s kind of a crazy claim because the probability of this occurring by chance is low, maybe 5% times 5%, a very small number. It’s what we actually all believe, but it’s a very surprising event. Somehow it’s accreted to all the findings in the literature so that we make ourselves believe this, but it seems unlikely on first principles that somehow only 5% would introduce both the Y chromosome and mitochondrial DNA.
And it really does look like this. There’s amazing data from a site in Spain that’s 300,000 to 400,000 years old, called
Sima de los Huesos
. They have a nuclear genome that looks Neanderthal-like for most of the genome, but their mitochondrial DNA and Y chromosome are Denisovan-like. So it really looks like there was a population related to modern humans that pushed into this Sima de los Huesos-like population, displaced its mitochondrial DNA and Y chromosome, but kept the rest of its genome. It really looks like something like this happened.
The idea I’m playing with—and probably it’s wrong, who knows—is that there’s a landscape… This is Europe and you can break up into a hundred or so
demes
, little areas. Modern humans get introduced at the bottom right corner, in the Middle East or somewhere, and they spread into Europe. As this population spreads, there’s a wave front of expansion, and they’re interacting with the local archaic humans.
The theory from simulations and studies of different species like mammals and birds shows that even if there’s a small amount of interbreeding—when there’s an invasion or a movement of expansion of one group into the territory occupied by another—there’s massive introgression of local genes. The pioneers at the wave front will sometimes interbreed with the local population. There are so many of them around that their DNA will get swamped by the local group, so by the time they make it to the other side, they’re largely local.
Maybe this is what we’re seeing. You have a modern human population that’s matrilineal, for example, where the transmission of making stone tools this way is happening from mother to child. That’s why they’re retaining their mitochondrial DNA, but by the time they get to the other end of Europe, they’re mostly local archaic. You end up with a 95% population replacement. This would explain why the mitochondrial DNA is shared between Neanderthals and modern humans, and it would also explain why the mixture proportion is only 5%.
The really interesting thing is that there’s other evidence from studies of modern humans showing that modern humans are also admixed. The right way to think about this is that modern humans are a mixture of two groups that diverged maybe 1.5 million years ago, and they come together 200,000 to 300,000 years ago with maybe 20% ancestry from this archaic African group and 80% ancestry from this early modern lineage. And that same group then mixes with Neanderthals, and it’s 5% modern and 95% local.
So you actually have this key population that makes the Middle Stone Age or Levallois technology. It appears and expands in all directions—into Europe and into Africa 200,000 to 300,000 years ago—bringing this technology, new ideas, and perhaps some genetic adaptations. It expands into archaic humans in Europe, mixes with the local population, and gets 95% replaced but still retains its cultural features and maybe some genetic features.
It expands in Africa too, but here it’s not 95% replaced, it’s only 20% replaced. Probably the reason is that this group is much more diverged. It’s 1.5 million years diverged rather than 700,000 to 800,000 years. As a result, there are many more genetic incompatibilities and barriers to gene flow. But there’s still a lot of mixing, maybe 20%, and
we have evidence that this is a big mixture event
.
So what you’re actually seeing is a modern human expansion both into Europe and into Africa. In one place, it forms Neanderthals. In another, it forms the ancestors of everybody living today. But all of these groups are descended from this key revolutionary event that happens here.
We often talk about the revolutionary events 50 to 100,000 years ago, the more symbolic behavior and so on, that first appears in Africa and the Middle East and spreads beyond. But there’s also this earlier event, and it is contemporaneous with the breakup of all the different groups in Africa today, the Khoisan Southern Africans and the Central African rainforest hunter-gatherers. One wonders whether this is an equally important formative event.
If that’s true, it makes you think of Neanderthals as somehow our cousins. Their shared Y chromosome, their shared mitochondrial DNA, they share the formation of this 200,000 or 300,000-year-old event, and their shared toolkit. Even though the genome is telling us they’re cousins of Denisovans, the correct way to think about them may, in an important sense, be as close cousins of modern humans.
Dwarkesh Patel
I have so many questions. Do you have 15 more minutes? First of all, what is going on with this group of archaic Africans 1.5 million years ago? Where in Africa are they, and what happens to the portion of them that don’t form modern humans? Do they survive?
David Reich
This is not from ancient DNA, but from analysis of modern DNA from different people, mostly in Africa, but also non-Africans. In
multiple studies
—there’s at least three, maybe four or five studies that I know about—they have looked at the patterns of variation in people today and say the data in modern people today, including in Africans, is not consistent with a homogeneous population.
It looks like a population that split well more than a million years ago into multiple groups—at least two, but maybe many—and then came together a few hundred thousand years ago. The papers have different models that they fit, but they all have this feature of a split-up more than a million years ago, and then on the order of a few hundred thousand years ago, a coming together and a remixture event forming the ancestors of anatomically modern humans.
Dwarkesh Patel
This includes the Khoisan and whatever other groups?
David Reich
Yes. All of these groups have this, maybe in slightly different proportions. So you ask, where are these people living? Who knows. In this scenario, the 80% is coming from the Caucasus or Northeast Africa, where the Middle Stone Age forms. It’s from this population that the Middle Stone Age comes. They mix with local groups, and who knows where they are: Southern Africa, Western Africa, Central Africa, Eastern Africa.
We don’t have any ancient DNA, but this is a very rich environment. People have been living there for seven million years at least, and there would have been different groups of people everywhere. Probably it’s not just two groups, it’s probably more.
The important theme here is there’s evidence of substructure that’s well more than a million years old. This place would have been a landscape full of archaic humans that would have been differently related to these expanding people and would have admixed with them when they came through.
Dwarkesh Patel
So with the Neanderthals, the first time around 300,000 years ago, our ancestors share culture with them. They share the Middle Stone Age technology, but they don’t replace the population. The technology spreads through culture, basically.
David Reich
It spreads through genes too. If you look at Yamnaya in India, there’s almost no Yamnaya ancestry in India. It’s just diluted down. As Yamnaya expanded into Central Asia and into Europe, it makes the
Corded Ware
. There’s a 25% dilution. It expands back across Central Asia. It goes through the Hindu Kush and gets into northern South Asia. It admixes more with local people. Today, the most Yamnaya ancestry you see in India is 20% or 10%. Most people have less than 10% or 5%.
There’s been a lot of mixture on the way, but it is the tracer dye. It tracks Indo-European languages, and important aspects of Indo-European culture are coming through Yamnaya. So if you know where to look, that tracer dye is only 10%, 5%, or 2% in some groups. But it’s the languages people speak, and important shared cultural elements, that connect them to people on the other side of the Indo-European-speaking world. So this 5%, you shouldn’t sneeze at it. That’s tracing something important in this model.
Dwarkesh Patel
I understand that if things are transmitted more through women… Sorry, let me back up. I don’t understand why the maternal mitochondrial DNA and the Y chromosome would be especially privileged as the spreading is happening. Can you explain that?
David Reich
The reason I’m talking about these matrilineal or patrilineal expansions is that I’m really troubled, and have been troubled for many years—especially in the last three or four years—by the fact that the mitochondrial DNA and Y chromosome cluster Neanderthals and modern humans, but the rest of the genome clusters Neanderthals and Denisovans.
This is a crazy result that is not seen in any other species. I’m very interested in patterns that would explain it. If you assume that there was a matrilineal or a patrilineal expansion—it could be either—then modern humans, when they were expanding across the landscape of Europe, retained their identity along one of the lines.
If it’s matrilineal, when they incorporate a male from the local community, he’s brought into the community, and the kids are raised based on the culture of the mothers. If it’s a patrilineal expansion and they incorporate a female from the community, she’s raised with the culture of the fathers. If that happens, it guarantees that one of these two parts of the genome looks like it does, because it’s a modern human expansion. If it’s patrilineal, it will retain the Y chromosome. If it’s matrilineal, it will retain the mitochondrial DNA. So it will solve one of your two problems.
Dwarkesh Patel
But not both.
David Reich
It won’t solve the other one, so you need to solve the other one. You can solve it either by natural selection or by
social selection
. By the way, patrilineality and matrilineality are the rule, not the exception, in human communities. Usually communities have continuity along the male or the female line. Usually it’s patrilineality, sometimes it’s matrilineality.
You can also have phenomena like social selection. It could be that once you have kids of someone whose father, for example, is from the outside community… Usually in most communities, females all reproduce. That’s typical today. Usually women have kids if they can. But men in traditional societies are actually very variable in their reproductive success. A large fraction of men never have kids. Then there’s a subset of men who have many kids with many women.
There’s competition among men for kids. In this context, where males are competing for access to females, female mate choice begins to be an important process. You have a phenomenon where if your dad is an archaic male, it could be the case that you’re not going to be as successful in the competition for local females as if your dad is a non-archaic male.
Some simple social phenomenon like that could explain the data, and we actually see this in human society. For example, if I remember right, in Central African rainforest hunter-gatherers, there’s different treatment of boys and girls depending on whether their dad or mom is one group or the other.
Dwarkesh Patel
I guess I don’t understand how the maternal… The group spreads, and it gets to the next front. They have kids. From the humans that have just entered, the kids will have the mitochondrial DNA from the humans. But from the existing people, they will have the mitochondrial DNA of the archaic humans. Why are the people with the archaic mitochondrial DNA not surviving?
David Reich
It’s a question. There are multiple possible explanations, but it’s much easier to explain that than both the mitochondrial DNA and the Y chromosome. One possibility is that the mitochondrial DNA was less biologically fit. Another possibility is that there’s social discrimination against people based on whether their parents are archaic or not, which is not at all surprising in a human context. It’s the weakest link in this argument. This argument’s probably wrong, but I’m just telling you what I’m thinking about.
Dwarkesh Patel
Okay, the Neanderthals. So 300,000 years ago our lineage interacts with them, but mostly their lineage survives, and there’s cultural and genetic diffusion. And then is it 70,000 years ago that we interact again?
David Reich
Yes.
Dwarkesh Patel
And they don’t survive.
David Reich
The genetic ancestry doesn’t survive.
Dwarkesh Patel
The genetic ancestry doesn’t survive. Presumably there was also other contact between 300,000 years ago and 70,000 years ago.
David Reich
Probably. But these are the ones we are detecting currently.
Dwarkesh Patel
Is it just contingent that one time there’s this kind of diffusion where most of the archaic genome survives, and the other time it’s total replacement?
David Reich
This is not at all surprising given the context. If you think about this model, this is 700,000 or 800,000 years ago. This is 300,000 years ago. So this is 400,000 years separated. You talked about the Bhatia paper with me earlier. That’s two populations 70,000 years separated. There are no biological incompatibilities between West Africans and Europeans. There’s no natural selection against biological incompatibilities.
We know when Neanderthals and modern humans met and mixed, there were biological incompatibilities. That was 700,000 years ago. As populations become further apart, biological incompatibilities rapidly develop, probably as the square of the separation distance, because you need pairs of interacting genes. Here, it would have been maybe only 400,000 years separated between this lineage and that lineage. But here, it’s 1.2 million years. That’s a lot. These are at the edge of not being able to produce children. These are quite different humans. These are actually three times closer than these.
If you look at mixtures of humans today, there are mixtures in Southern Africa of people who are half this distance. If you look at Khoisan and
Bantu
people mixing in Southern Africa, like the
Xhosa
, which is the population of Nelson Mandela, these are groups that are separated by almost 200,000 years, which is half of this. Totally compatible.
What you’re seeing is a group that’s actually completely permeable genetically, or nearly completely permeable. This other one almost certainly has substantial biological incompatibilities. Because 200,000 or 300,000 years later, we see interbreeding between Neanderthals and modern humans, or between Denisovans and modern humans, and there’s clear evidence of incompatibility at that point. But this would be even bigger.
What you would expect to see is that as this group spread, they would be moving into a territory full of archaic humans. There would be some interbreeding, but the kids would not be very fit. They would die off. There would be a lot of infertility. The barriers to gene flow and to interbreeding would be greater.
To me, it’s not at all surprising that as this group moves into Eurasia, you have Eurasian archaics—the ancestors of Denisovans—who are only 400,000 years diverged from these people over here. And then you have African archaics, and these are 1.2 million years diverged. They just don’t interbreed as much, and you don’t get as much gene flow.
But the key thing is the timing. It’s the same time. It really feels like the signature of an explosion of people from one place, interacting with people here and interacting with people there. It’s the same cultural or technological revolution impacting this place and that place, and creating populations that are impacted by this cultural revolution, which we know is the case because they share the same toolkit.
Some people argue that Levallois technology is independently invented. But it’s very similar, and this model would be a way that it could have the same origin. So there’s a culturally shared thread, this shared toolkit. There’s a mitochondrial DNA and Y chromosome thread. And then there is a shared timing thread, which is they both form by mixture.
Dwarkesh Patel
Because otherwise you’d have to believe that Neanderthals independently developed Stone Age tools.
David Reich
Yes, which is not inconceivable. But it’s a little bit like believing that farming independently developed in multiple parts of the world.
Dwarkesh Patel
Right. But it did.
David Reich
It did. So as I said, this is probably wrong. I’m trying to tell you that we don’t really know the world we live in. This is not obviously wrong. In fact, to me, this is much more plausible than the model we currently write down. It’s probably wrong, but it’s much more plausible. It explains many more things, and it’s no more complicated.
Dwarkesh Patel
Do you want to recapitulate the thing you were saying about the analogy to Ptolemy and the epicycles? I thought that was quite interesting.
David Reich
I think the model that we’ve put together collectively about the relationships between archaic and modern humans has accreted over time. There was this idea that modern humans are distinct and that Neanderthals and Denisovans are sisters of each other. Over time, we detected additional mixture events, like this modern human into Neanderthal, and then these other ones I didn’t even talk about, like a super-divergent lineage going into Denisovans and all this other stuff. We still say, “Oh, the whole genome says Neanderthals and Denisovans are sisters, so that’s the truth.”
We’ve patched it all together and gotten it all to work. You look at the mitochondrial DNA and the Y chromosome, and they have this odd pattern, and it’s improbable, but we can get that to work if we invoke natural selection, things like this. You patch it all together.
It reminds one of what happened in the ancient world, where there was this idea that the sun revolves around the Earth, but it doesn’t quite explain the movements of the planets properly. In order to get the movements of the planets to work right,
Ptolemy
and the astronomers made up these
epicycles
, these special extra rotations and movements to make everything work about right. It was such a convoluted model. When
Copernicus
and colleagues suggested instead that
everything is revolving around the sun
, it simplified things ever so much.
What was happening is that as astronomical information accumulated, it kept being contradictory to the standard model, but it could be made to work by proposing another complication and another complication and another complication. This is not as fantastic as proposing that everything revolves around the sun rather than the Earth, but it is much simpler. And it actually explains many things.
Dwarkesh Patel
What is counterintuitive or unexpected or hard to accept about this alternative model? What is the hesitation that people have for adopting this?
David Reich
I don’t know. Nobody’s thinking about this model right now. It just seems obviously a very natural model to me.
Dwarkesh Patel
The reason I ask is that
Aristarchus
, the ancient Greek, had the heliocentric theory because he had
deduced how far the Earth is from the sun and noticed other things
. But it was not adopted, because his fellow Athenians were like, “Look, if we believe that the Earth revolves around the sun, for it to be the case that we don’t see
relative movement of the stars to the Earth
, the only possible explanation is that the stars are so far away that it is just incomprehensible and implausible.” So the heliocentric theory was dismissed.
What I’m trying to ask is, what is the equivalent here of “for this to work, the stars have to be so far away that it’s inconceivable,” where actually the stars are so far away? Maybe we should adopt the implausible implication that this theory gives us.
David Reich
That’s a great question. I think we have to assume that there’s a linkage between the cultural transformations in Africa and Eurasia at this time, and that’s not something the community has really put together with the genetic data.
There’s this thread in the genetics about substructure in Africans, and then there’s this whole world based on ancient DNA, and they’ve never been put together. Nobody’s put together the now extensive work on modern human substructure with the extensive work based on ancient DNA of archaic human relationships to modern humans.
If you put them together, you realize they line up in terms of their time of substructuring. I don’t know if that’s improbable. It seems parsimonious to me.
Dwarkesh Patel
It also seems significant that different groups of humans at this time were capable of adopting Stone Age technology. Once one group had figured it out, the genetic difference between different human lineages was not so big that you could not show people how to use stone tools.
David Reich
Who knows? It could be that this was genetically driven. We talked before about the time to the common ancestor of human genes. There’s nothing at 100,000 years or 150,000 years, but there’s a lot at 400,000 or 500,000 years.
If that’s what happens, and you have a mutation that occurs in the Caucasus, somewhere in the Middle East, or Northeast Africa, there could be key genetic mutations that make people able to do this. Then this population expands. When it moves into Europe, it’s swamped by local genes, but there could be retention of those genes through selection as it expands.
Maybe what you’re seeing is that there are genetic developments. Most of the discussion has been focused on the 50,000 to 100,000-year event, which is anatomically modern human behavior. But a lot of archaeologists think this is an equally—if not more—profoundly significant event in many ways. Why is that not the event we should be talking about?
Dwarkesh Patel
You’re talking about how there are no fixed differences between modern humans and the humans 50,000 years ago. Do we know if there are any fixed differences between the people 50,000 years ago and the people 300,000 years ago?
David Reich
I think there are.
Dwarkesh Patel
Other than obviously these interbreedings.
David Reich
If you look at the genetic variation going back 300,000 or 400,000 years, there do begin to be places where all modern humans share common ancestry. That’s another way of saying there begin to be fixed differences at that time depth. That is where you start seeing evidence for possible fixed differences.
What’s happening, if everybody shares a common ancestor 400,000 or 500,000 years ago, is that there’s a single ancestor at that time. If you compared it to another population, they would descend from a different lineage, so any mutation that occurred ancestral to that single ancestor would be a fixed difference. This is the time at which you can begin to see fixed differences.
Dwarkesh Patel
But anatomically modern, cognitively modern humans exist by the beginning of the Middle Stone Age, before we’re breeding with this ancient group of Africans or breeding with Neanderthals.
David Reich
Anatomically modern humans occur exactly here. It’s the same moment. This is when they occur. The people who have skeletal features like ours, and Neanderthals, appear exactly then.
This is when it all happens. There is this disconnect between anatomically modern humans in the skeletal record and behaviorally modern humans, which is 50,000 to 100,000 years ago. Anatomically modern humans appear at this time, and recognizable Neanderthals appear roughly around this time, too.
Dwarkesh Patel
Interesting. But we don’t know what exactly happens, if anything, between 200,000 years ago and 50,000 years ago that goes from just anatomical modernity to behavioral modernity.
David Reich
My understanding is no. They’re busy making Levallois stone tools like Neanderthals for 200,000 years, and they are not more impressive than Neanderthals in any obvious way, as I understand it.
Then there begins to be in the archaeological record a quickening of behavioral traits, which could be not genetic at all, or could be genetic. There are lots of arguments about this. We were obsessed with intelligence earlier in our conversation. People are obsessed with art and these things that seem important to us but who knows what’s important?
Dwarkesh Patel
Interesting. Cool, thanks for the digression.
David Reich
The work that I’ve been involved in has consistently shown that I was wrong in my biases coming into the work, and I’ve really been almost traumatized by this. Again and again, I’ve come into a project with some kind of guess about what the data was showing, and then the data doesn’t show that.
For example, when I got involved in the
Neanderthal genome project
helping to analyze data looking at how archaic Neanderthals were related to modern humans, I was part of a group of scientists who had established that non-Africans were a simple subset of African variation and that there was no evidence at all of Neanderthal interbreeding into the ancestors of modern humans or other archaic interbreeding. Different analyses that I and many other people had done made it look like non-African variation was just a subset, a small sample of that in Africa, and that could have fully explained the data.
So when I was involved in analyzing the Neanderthal DNA sequences, what happened was I found this very strong evidence of Neanderthals being more closely related to non-Africans than to Africans. It was very surprising, and I thought it must be a mistake. I was quite incredulous. I thought it was unlikely to be true because other evidence that had been found before seemed to point in the other direction. So I spent several years trying to make these results go away, as did my colleagues, and we just couldn’t make the results go away. They just kept getting stronger.
And this experience working on natural selection was the same. What we were convinced of was that natural selection had been pretty quiescent in our species over the last several hundred thousand years. Therefore, if we look at patterns of variation in non-African people today, or in any people today, we should see not a lot of selection going on. Indeed, the first ancient DNA studies, beginning in 2015 with
this paper
that we were involved in with
Ian Mathieson
and colleagues, seemed to show relatively small numbers of genetic positions associated with natural selection.
In 2015, we analyzed data from about 200 Europeans and Middle Easterners to try to understand frequency changes over time. We compared those ancient people who were the sources of modern Europeans to people in Europe today, and we looked at frequency differences that were too extreme to be due to chance. We were very excited to find 12 positions that we were convinced were highly different in frequency between Europeans today and what we would expect, based on the history that we and others had identified as the history relating modern to ancient Europeans. Some of these were known and some of these were not known, and this was very exciting.
We hoped that as the numbers of samples would increase and we got higher resolution to be able to appreciate differences in frequencies over time, it would make it possible to detect far more. What was quite disappointing over the subsequent decade is that that didn’t happen. For example, the
largest study of that type in 2024
by a group in Copenhagen analyzed much better data than we had in 2015 and found only 21 positions that were highly different in frequency across time. While that was exciting—it was almost twice as many as we had found in 2015—in a lot of ways it was disappointing because the sample size and data quality had gone up so much, and yet this is all that was found.
That suggested we might be hitting an asymptote and might not be able to get beyond where we currently were. This approach to learning about biology, which was very promising in theory, might not produce a high yield. Maybe natural selection was quiescent, and the reason we’re seeing so few changes is that there has not been a lot of adaptive directional selection. That was the situation we found ourselves in until just a few years ago when we carried out this study in our research group led by Ali Akbari.
What we did is we deployed a few innovations to try to improve our power to detect natural selection. One of them was that we just pumped a lot of data into the system, increasing the amount of data by about 14-fold. The main thing that we do in this study is report new data from about 10,000 individuals. This is a very big increase in the amount of data in the literature. The total dataset size of ancient individuals distributed over the last 18,000 years is about 16,000 people. This is a large dataset. It’s much larger than was previously possible, and when you have more data, you can estimate frequency changes with much more subtlety.
The data comes from only one part of the world, which is Europe and the Middle East. It’s not a more important part of the world than other places, but it’s the place where maybe 70-80% of the data in the ancient DNA literature so far comes from due to historical reasons. It provides us with a natural laboratory where we can see what happens to the genome in one place over time as environments change. It’s really interesting to imagine doing this type of analysis in other parts of the world, and the comparative analyses are super important and interesting, but this study right now is about this one place in the world where we have particularly fantastic data.
The other thing we did is that we developed an entirely new methodology that hadn’t been used in this area before. The methodology is based on a technique that had been developed for finding risk factors for a disease in medical studies. A simple way to explain it is that we ask how to predict the genetic type a person has based on their pattern of relatedness to other people. We have a dataset of about 16,000 ancient people, and 22,000 people if we include the modern people. Then we look at how closely related each of these 22,000 people are to each other, and we predict the genetic type at each position in the DNA—at 10 million positions—based on the pattern of relatedness to all of the other 22,000 people.
Then we ask if natural selection blowing the frequency of the mutation in the same direction in all geographic places and at all times predicts the data a little bit better than just knowing the relatedness to all the other samples in the database. We’re simply asking if the alternative hypothesis—that selection has been blowing in the same direction at all times—explains the data better. That’s a dumb assumption, because of course, the truth is that natural selection will have changed in frequency over time. But we’re just asking the simplest of questions: whether assuming a constant rate of selection explains the data more than not doing so.
Dwarkesh Patel
To summarize to make sure I’ve understood, you’re trying to make a model that predicts allele frequency changes over time. You have two different parts. One part is this genetic relatedness matrix, which captures how similar different genomes are to each other. That should capture the impact of different bottlenecks, of drift, of population admixtures, and all those things which affect the entire genome.
Then you have the separate thing, which is, if we look at specific locations, can we just say that, “Oh, this location has been selected at whatever coefficient over time”? And if we add some coefficient, does it become easier to predict the allele frequency changes than you would have just seen from this other artifact, which is just looking at, “Oh, if you look at the whole genome, are these guys in the same, have they gone through the same bottlenecks? Have they gone through the same drift,” etc.?
David Reich
That’s precisely right.
Dwarkesh Patel
Okay, what did we learn?
David Reich
When we analyzed the data this way, we looked at 10 million positions in the DNA across these 22,000 people, 16,000 of whom were ancient. We looked to see if there was more change in this consistent direction over time than you would expect by chance. When we analyzed the data, we found many hundreds of places in the DNA that were changing too much over time and in too consistent a way to be explained by chance.
There’s a bit of a statistical problem in figuring out how many there are because they’re so densely packed that they’re close to each other and interfering with each other. But when you try to piece them out and say, “Let’s count only one in each place in the DNA and blank out the others,” we find at least 479 positions that are all independently pushing in the same way. We are 99% confident that those positions are real. By another criteria of being more than 50% confident that they’re real, we think that about 3,800 positions are all pushing in the same direction. This is a crazy number of results given that in our previous work and other people’s work, there were at most a couple of dozen discoveries coming from a single scan.
So when we got this result, we were very surprised. We thought it must be wrong, and we spent the next couple of years trying to make the results go away, but they just kept getting stronger. We were trying to look for some independent type of evidence to tell us whether these positions were real. We stumbled on something really powerful for this purpose that had not been used in this way before. It relied on the fact that we had very large numbers of discoveries, many hundreds of discoveries or even thousands.
We took a completely independent dataset, which was the corpus of genome-wide association studies. These are studies that people have carried out in hundreds of thousands of people, looking for whether particular genetic mutations are more common in people with high blood pressure than with low blood pressure, or something like this. We took the
UK Biobank
, which is about 500,000 people from Great Britain who have been measured for hundreds of traits. The whole genomes of all these people have been sequenced. For each of these traits, we could look at whether each of these 10 million positions are connected to this trait in a convincing way. Out of 10 million positions, about 15%—about 1.5 million positions in the DNA—are predictive of at least one of these several hundred traits.
Then we could ask a question: is our natural selection signal, our statistic, related to whether a mutation causes high blood pressure or some other trait? We slid our statistic for natural selection upward, to a value of one, two, three, four, or five. As we did that, the enrichment for genetic mutations that affect traits got higher and higher. Whereas it was only 15% when we didn’t use our selection statistic, when we required the selection statistic to be above about five, there was about a five-fold enrichment for mutations that cause traits.
Dwarkesh Patel
Sorry, what is a selection statistic?
David Reich
This is the statistic we use to measure whether a mutation is changing over time significantly in a non-zero way. It can be approximately thought of as a normally distributed statistic, a
Gaussian statistic
, which is the number of standard deviations the statistical value is away from zero, where zero is no natural selection.
It’s not exactly that, but it’s close to that. If the statistic is above five, we see about a five-fold enrichment in mutations that affect a trait. Instead of 15% of the mutations that are at random affecting the trait, it’s 60% or 70% that are affecting the trait when we slide our statistic upward. This provides completely independent evidence that these sites are real, and as you slide above five, there’s no more enrichment. Our interpretation of these results—which we were able to validate and show made sense using computer simulations of our process—is that once you slide the statistic above five, essentially all the signals of natural selection are real.
Dwarkesh Patel
Okay, just to make sure I understand. You’re saying, in order to figure out what
alleles
have been under selection, your model assigns a statistic saying, “In order to explain why this allele has a specific frequency, we’re going to give it a selection statistic.” Independently, we run these studies on modern populations where we say, “If you look at height, eye color, intelligence, or whatever trait, what are the parts of the genome that are correlated with that trait?” The higher the statistic you give it in your study to explain allele frequency changes over time as a result of selection, the more probable it is that that region in the genome is associated with traits that have some functional thing we can measure.
David Reich
That’s exactly right. This is a brilliant idea that Ali had. It abandons the traditional approach of assigning statistical significance to mutations that cause a trait because we’re just using an external piece of information—the correlation to traits, measured in a completely different way—to read off the probability mutations are real.
We can ask how much enrichment for real signal is there given a particular selection statistic. If it’s halfway enriched to the plateau, we’re able to show the correct interpretation is that 50% of the mutations are really selected. If it’s three-quarters of the way toward the plateau, there’s a three-quarters probability that the mutation is real. If it’s 99% of the way to the plateau, there’s a 99% probability that it’s real. That gives us a calibrated estimate of the probability that a particular position is really under natural selection.
A major concern here is that what we’re actually seeing is not that these mutations are really under selection, but rather that both association to a disease and our selection signal are due to some third thing that’s causing both of them, which is a type of selection which is not what we’re after, not selection to adapt to new environments, but what’s called background selection: selection against newly arising bad mutations that are removed from the population that tend to be concentrated in genes. Genes are also the parts of the genome that tend to be associated to traits. This common process is causing both the enrichment for trait signals and is also causing the enrichment for selection signals that we’re observing. That’s the concern. We were super concerned about this.
So what we did is we repeated this enrichment analysis in slices of the DNA that all were affected to the same extent by background selection, by this rain of slightly bad mutations, and we get exactly the same pattern. We also repeated this experiment just using mutations of the same frequencies because there’s different statistical power to detect these signals at different frequencies. We see the same pattern where above a value of the selection statistic of around five, we get this plateau.
Dwarkesh Patel
The thing that changed that allowed you to increase the amount of sequences you’re generating by two orders of magnitude is just the statistical method you’re using to identify which part is human? Or what exactly changed in 2014 and since then?
David Reich
There’s been a whole series of improvements. The big ones have been the huge drop in sequencing cost, which made it possible to generate ancient DNA in the first place. The drop in cost has been a millionfold since the late 2000s, and another maybe one to two orders of magnitude from 2010 to today. That’s one big change.
Another change has been in-solution enrichment. It’s been this way of taking a sample that has very small percentages of human DNA, but then suddenly creating a process that will mean that the great majority of the sequences that one’s analyzing will be useful for analyses. The approach that we used was we took the DNA samples that we had, most of which were very low percentages of human DNA—less than 10%, often less than 1%—which is such a low proportion that it’s prohibitively expensive to sequence them and to just brute-force sequencing them given the technology that we had available at the time.
We took these samples and washed them over an artificially synthesized set of short DNA fragments that targeted positions of the DNA that we were interested in analyzing. This is more than a million positions that are highly variable in people, and we picked many of these to be biologically interesting. We had a whole set of known biological targets that affected traits in genome-wide association studies, which is the way that people look to see if there are particular genetic variants in modern people that have particular impacts in phenotypes and traits.
And so, what we did is we had this artificially synthesized set of DNA fragments that we washed our ancient sample over, and it bound the parts of the DNA that we targeted. The resulting sequence that we generated was very enriched for the parts of the genome that were informative about history. Even though only 10% or 1% of the DNA was human, it ended up that a very large fraction was from the parts of the genome that we were interested in, and it became economically efficient to do it.
Dwarkesh Patel
What was the other 99% of the DNA?
David Reich
It’s mostly microbial. It’s from bacteria and fungi that colonize a person’s body after they die. Depending on how they die, there’ll be more or less of these bacteria and fungi. When you typically sequence DNA from a person, it’ll just be full of microbial sequence. Sometimes the microbial sequence is very interesting; it might be pathogens that a person died of. There’s amazing work, for example, about different plagues of malaria and Black Death and hepatitis B and so on that have been obtained from the sequences of these pathogens in people’s teeth and other parts of their body when they died.
But we’re focusing here on the human DNA. This changed the amount of data that was possible to produce from tens per year to hundreds per year, and then we further roboticized and industrialized the process so that there were many hundreds or even thousands per year. Just in our laboratory, we’ve been generating genome-scale data from more than 5,000 individuals per year. I know this is true also of several other laboratories in the world now.
This huge jump in data, this semi-exponential or even super-exponential jump in some cases, has made it possible to ask and answer questions. While we were only on the order of 10 genome sequences from humans in 2010, this year it’s passed more than 20,000 reported sequences. There are several orders of magnitude increase, and the questions we were able to ask in 2014 are just not the same as the ones we can ask today.
Dwarkesh Patel
Awesome. Excellent. David, thanks for your time.
David Reich
Thank you, Dwarkesh.
