---
title: "Some thoughts on writing"
url: "https://danluu.com/writing-non-advice/"
fetched_at: 2026-05-05T07:01:29.562265+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Some thoughts on writing

Source: https://danluu.com/writing-non-advice/

I see a lot of essays framed as writing advice which are actually thinly veiled descriptions of how someone writes that basically say "you should write how I write", e.g.,
people who write short posts say that you should write short posts
. As with technical topics,
I think a lot of different things can work and what's really important is that you find a style that's suitable to you and the context you operate in
.
Copying what's worked for someone else is unlikely to work for you
, making "write how I write" bad advice.
We'll start by looking at how much variety there's been in what's worked for people, come back to what makes it so hard to copy someone else's style, and then discuss what I try to do in my writing.
If I look at the most read programming blogs in my extended social circles from 2000 to 2017, it's been Joel Spolsky, Paul Graham, Steve Yegge, and Julia Evans (if you're not familiar with these writers,
see the appendix for excerpts that I think are representative of their styles
). Everyone on this list has a different style in the following dimensions (as well as others):
Topic selection
Prose style
Length
Type of humor (if any)
Level of technical detail
Amount of supporting evidence
Nuance
To pick a simple one to quantify, length, Julia Evans and I both started blogging in 2013 (she has one post from 2012, but she's told me that she considers her blog to have started in earnest when she was at
RC
, in September 2013, the same month I started blogging). Over the years, we've compared notes a number of times and, until I paused blogging at the end of 2017, we had a similar word count on our blogs even though she was writing roughly one order of magnitude more posts than I do.
To look at a few aspects that are difficult to quantify, consider this passage from Paul Graham, which is typical of his style:
What nerds like is the kind of town where people walk around smiling. This excludes LA, where no one walks at all, and also New York, where people walk, but not smiling. When I was in grad school in Boston, a friend came to visit from New York. On the subway back from the airport she asked "Why is everyone smiling?" I looked and they weren't smiling. They just looked like they were compared to the facial expressions she was used to.
If you've lived in New York, you know where these facial expressions come from. It's the kind of place where your mind may be excited, but your body knows it's having a bad time. People don't so much enjoy living there as endure it for the sake of the excitement. And if you like certain kinds of excitement, New York is incomparable. It's a hub of glamour, a magnet for all the shorter half-life isotopes of style and fame.
Nerds don't care about glamour, so to them the appeal of New York is a mystery.
It uses multiple aspects of what's sometimes called
classic style
. In this post, when I say "classical style", I mean as the term is used by
Thomas & Turner
, not a colloquial meaning. What that means is really too long to reasonably describe in this post, but I'll say that one part of it is that the prose is clean, straightforward, and simple; an editor whose slogan is "omit needless words" wouldn't have many comments. Another part is that the clean-ness of the style goes past the prose to what information is presented, so much so that supporting evidence isn't really presented. Thomas & Turner say "truth needs no argument but only accurate presentation". An example that exemplifies both of these is this passage from Rochefoucauld:
Madame de Chevreuse had sparkling intelligence, ambition, and beauty in plenty; she was flirtatious, lively, bold, enterprising; she used all her charms to push her projects to success, and she almost always brought disaster to those she encountered on her way.
Thomas & Turner said this about Rochefoucauld's passage:
This passage displays truth according to an order that has nothing to do with the process by which the writer came to know it. The writer takes the pose of full knowledge. This pose implies that the writer has wide and textured experience; otherwise he would not be able to make such an observation. But none of that personal history, personal experience, or personal psychology enters into the expression. Instead the sentence crystallizes the writer’s experience into a timeless and absolute sequence, as if it were a geometric proof.
Much of this applies to the passage by Paul Graham (though not all, since he tells us an anecdote about a time a friend visited Boston from New York and he explicitly says that you would know such and such "if you've lived in New York" instead just stating what you would know).
My style is opposite in many ways. I often have long, meandering, sentences, not for any particular literary purpose, but just because it reflects how I think.
Strunk & White
would have a field day with my writing. To the extent feasible, I try to have a structured argument and, when possible, evidence, with caveats for cases where the evidence isn't applicable. Although not presenting evidence makes something read cleanly, that's not my choice because I don't like that the reader basically has to take or leave it with respect to bare assertions, such as "what nerds like is the kind of town where people walk around smiling" and would prefer if readers know why I think something so they can agree or disagree based on the underlying reasons.
With length, style, and the other dimensions mentioned, there isn't a right way and a wrong way. A wide variety of things can work decently well. Though, if popularity is the goal, then I've probably made a sub-optimal choice on length compared to Julia and on prose style when compared to Paul. If I look at what causes other people to gain a following, and what causes my RSS to get more traffic, for me to get more Twitter followers, etc., publishing short posts frequently looks more effective than publishing long posts less frequently.
I'm less certain about the impact of style on popularity, but my feeling is that, for the same reason that making a lot of confident statements at a job works (gets people promoted), writing confident, unqualified, statements, works (gets people readers). People like confidence.
But, in both of these cases, one can still be plenty popular while making a sub-optimal choice and, for me, I view optimizing for other goals to be more important than optimizing for popularity. On length, I frequently cover topics that can't be covered in brief easily, or perhaps at all. One example of this is
my post on branch prediction
, which has two goals: give a programmer with no background in branch prediction or even computer architecture a historical survey and teach them enough to be able to read and understand a modern, state-of-the-art paper on branch prediction. That post comes in at 5.8k words. I don't see how to achieve the same goals with a post that comes in at the lengths that people recommend for blog posts, 500 words, 1000 words, 1500 words, etc. The post could probably be cut down a bit, but every predictor discussed is either a necessary building block used to explain later predictors except the
agree
predictor or of historical importance. But if the
agree
predictor wasn't discussed, it would still be important to discuss at least one interference-reducing scheme since why interference occurs and what can be done to reduce it is a fundamental concept in branch prediction.
There are other versions of the post that could work. One that explains that branch prediction exists at all could probably be written in 1000 words. That post, written well, would have a wider audience, be more popular, but that's not what I want to write.
I have an analogous opinion on style because I frequently want to discuss things in a level of detail and with a level of precision that precludes writing cleanly in the classic style. A specific, small, example is that, on a recent post, a draft reader asked me to remove a double negative and I declined because, in that case, the double negative had different connotations from the positive statement that might've replaced it and I had something precise I wanted to convey that isn't what would've been conveyed if I simplified the sentence.
A more general thing is that Paul writes about a lot of "big ideas" at a high level. That's something that's amenable to writing in a clean, simple style; what Paul calls an elegant style. But I'm not interested in writing about
big ideas that are disconnected from low-level details
and it's difficult to effectively discuss low-level details without writing in a style Paul would call inelegant.
A concrete example of this is
my discussion of command line tools and the UNIX philosophy
. Should we have tools that "do one thing and do it well" and "write programs to handle text streams, because that is a universal interface" or use commands that have many options and can handle structured data? People have been trading the same high-level rebuttals back and forth for decades. But the moment we look at the details, look at what happens when these ideas get exposed to the real world, we can immediately see that one of these sets of ideas couldn't possibly work as espoused.
Coming back to writing style, if you're trying to figure out what stylistic choices are right for you, you should start from your goals and what you're good at and go from there, not listen to somebody who's going to tell you to write like them. Besides being unlikely to work for you even if someone is able to describe what makes their writing tick, most advice is written by people who don't understand how their writing works. This may be difficult to see for writing if you haven't spent a lot of time analyzing writing, but it's easy to see this is true if you've taken a bunch of dance classes or had sports instruction that isn't from a very good coach. If you watch, for example, the median dance instructor and listen to their instructions, you'll see that their instructions are quite different from what they actually do.
People who listen and follow instructions instead of attempting to copy what the instructor is doing will end up doing the thing completely wrong
. Most writing advice similarly fails to capture what's important.
Unfortunately,
copying someone else's style isn't easy either; most people copy entirely the wrong thing
. For example, Natalie Wynn noted that people who copy her style often copy the superficial bits without understanding what's driving the superficial bits to be the way they are:
One thing I notice is when people aren’t saying anything. Like when someone’s trying to do a “left tube video essay” and they shove all this opulent shit onscreen because contrapoints, but it has nothing to do with the topic. What’s the reference? What are you saying??
I made a video about shame, and the look is Eve in Eden because Eve was the first person to experience shame. So the visual is connected to the concept and hopefully it resonates more because of that. So I guess that’s my advice, try to say something
If you look into what people who excel in their field have to say, you'll often see analogous remarks about other fields. For example, in Practical Shooting, Rob Leatham says:
What keeps me busy in my classes is trying to help my students learn how to think. They say, "Rob holds his hands like this...," and they don't know that the reason I hold my hands like this is not to make myself look that way. The end result is not to hold the gun that way; holding the gun that way is the end result of doing something else.
And Brian Enos says:
When I began ... shooting I had only basic ideas about technique. So I did what I felt was the logical thing. I found the best local shooter (who was also competitive nationally) and asked him how I should shoot. He told me without hesitation: left index finger on the trigger guard, left elbow bent and pulling back, classix boxer stance, etcetera, etcetera. I adopted the system blindly for a year or two before wondering whether there might be a system that better suited my structure and attitude, and one that better suited the shooting. This first style that I adopted didn't seem to fit me because it felt as though I was having to struggle to control the gun; I was never actually flowing with the gun as I feel I do now. My experimentation led me to pull ideas from all types of shooting styles: Isosceles, Modified Weaver, Bullseye, and from people such as Bill Blankenship, shotgunner John Satterwhite, and martial artist Bruce Lee.
But ideas coming from your environment only steer you in the right direction. These ideas can limit your thinking by their very nature ... great ideas will arise from a feeling within yourself. This intuitive awareness will allow you to accept anything that works for you and discard anything that doesn't
I'm citing those examples because they're written up in a book, but I've heard basically the same comment from instructors in a wide variety of activities, e.g., dance instructors I've talked to complain that people will ask about whether, during a certain motion, the left foot should cross in front or behind the right foot, which is missing the point since what matters is the foot placement is reasonable given how the person's center of gravity is moving, which may mean that the foot should cross in front or behind, depending on the precise circumstance.
The more general issue is that a person who doesn't understand the thing they're trying to copy will end up copying unimportant superficial aspects of what somebody else is doing and miss the fundamentals that drive the superficial aspects.
This even happens when there are very detailed instructions
. Although watching what other people do can accelerate learning, especially for beginners who have no idea what to do, there isn't a shortcut to understanding something deeply enough to facilitate doing it well that can be summed up in simple rules, like "omit needless words".
As a result, I view style as something that should fall out of your goals, and goals are ultimately a personal preference. Personally, some goals that I sometimes have are:
Explain a technical topic that a lot of people don't seem to understand at a level that's accessible to almost any professional programmer
Make a case for a minority opinion (or one that was a minority opinion at the time, anyway):
Measure something
Discuss phenomena I think are interesting:
When you combine one of those goals with the preference of discussing things
in detail
, you get a style that's different from any of the writers mentioned above, even if you want to use humor as effectively as Steve Yegge, write for as broad an audience as Julia Evans, or write as authoritatively as Paul Graham.
When I think about major components of my writing, the major thing that I view as driving how I write besides style & goals is process. As with style, I view this as something where a wide variety of things can work, where it's up to you to figure out what works for you.
For myself, I had the following process goals when I started my blog:
Low up-front investment, with as little friction as possible, maybe increasing investment over time if I continue blogging
Improve writing technique/ability with each post without worrying too much about writing quality any specific post
Only publish when I have something I feel is worth publishing
Write a blog that I would want to subscribe to
Write on my own platform
The low-up front investment goal is because, when I surveyed blogs I'd seen, one of the most common blog formats was a blog that contained a single post explaining that person was starting a blog, perhaps with another post explaining how their blog was set up, with no further posts. Another common blog format were blogs that had regular posts for a while, followed by a long dormant period with a post at the end explaining that they were going to start posting again, followed by no more posts (in some cases, there are a few such posts, with more time between each). Given the low rate of people continuing to blog after starting a blog, I figured I shouldn't bother investing in blog infra until I knew I was going to write for a while so, even though I already owned this domain name, I didn't bother figuring out how to point this domain at github pages and just set up a default install of some popular blogging software and I didn't even bother doing that until I had already written a post. In retrospect, it was a big mistake to use Octopress (Jekyll); I picked it because I was hanging out with a bunch of folks who were doing trendy stuff at the time, but the fact that it was so annoying to set up that people organized little "Octopress setup days" was a bad sign. And it turns out that, not only was it annoying to set up, it had a fair amount of breakage, used a development model that made it impossible to take upstream updates, and it was extremely slow (it didn't take long before it took a whole minute to build my blog, a ridiculous amount of time to "compile" a handful of blog posts). I should've either just written pure HTML until I had a few posts and then turned that into
a custom static site generator
, or used
WordPress
, which can be spun up in minutes and trivially moved or migrated from. But, part of the the low up-front investment involved not doing research into this and trusting that people around me were making reasonable decisions. Overall, I stand behind the idea of keeping startup costs low, but had I just ignored all of the standard advice and either done something minimal or used the out-of-fashion but straightforward option, I would've saved myself a lot of work.
The "improve writing" goal is because I found my writing annoyingly awkward and wanted to fix that. I frequently wrote sentences or paragraphs that seemed clunky to me, like when you misspell a word and it looks wrong no matter how you try re-spelling it. Spellcheckers are now ubiquitous enough that you don't really run into the spelling problem anymore, but we don't yet have automated tools that will improve your writing (some attempts exist, but they tend to create bad writing). I didn't worry about any specific post since I figured I could easily spend years working on my writing and I didn't think that spending years re-editing a single post would be very satisfying.
As we've discussed before, getting feedback can greatly speed up skill acquisition
, so I hired a professional editor whose writing I respect with the instruction "My writing is clunky and awkward and I'd like to fix it. I don't really care about spelling and grammar issues. Can you edit my writing with that in mind?". I got detailed feedback on a lot of my posts. I tried to fix the issues brought up in the feedback but, more importantly, tried to write my next post without it having the same or other previously mentioned issues. I can be a bit of a slow learner, so it sometimes took a few posts to iron out an issue but, over time, my writing improved a lot.
The only publishing when I felt like publishing is because I generally prefer process goals to outcome goals, at least with respect to personal goals. I originally had a goal of spending a certain amount of time per month blogging, but I got rid of that when I realized that I'd tend to spend enough time writing regardless of whether or not I made it an obligation. I think that outcome goals with respect to blogging do work for some people (e.g., "publish one post per week"), but if your goal is to improve writing quality, having outcome goals can be counterproductive (e.g., to hit a "publish one post per week goal" on limited time, someone might focus on getting something out the door and then not think about how to improve quality since, from the standpoint of the outcome goal, improving quality is a waste of time).
Having a goal of writing something I'd want to subscribe to is, of course, highly arbitrary. There are a bunch of things I don't like in other blogs, so I try to avoid them. Some examples:
Breaking up what could be a single post into a bunch of smaller posts
Clickbait titles
Repeatedly blogging about the same topic with nothing new to say
A sub-category of this is having some kind of belief and then blogging about it every time a piece of evidence shows up that confirms the belief while not mentioning evidence that shows up that disconfirms the belief
Not having an RSS or atom feed
Writing on my own platform is the most minor of these. A major reason for that comes out of what's happened to platforms. At the time I started my blog, a number of platforms had already come and gone. Most recently, Twitter had acquired Posterous and shut it down. For a while, Posterous was the trendiest platform around and Twitter's decision to kill it entirely broke links to many of the all-time top voted HN posts, among others. Blogspot, a previously trendy place to write, had also been acquired by Google and severely degraded the reader experience on many sites afterwards. Avoiding trendy platforms has worked out well.
The two trendy platforms
people were hopping on when I started blogging were
Svbtle
and Medium.
Svbtle was basically abandoned shortly afterward I started my blog
when it became clear that Medium was going to dominate Svbtle on audience size. And Medium never managed to find a good monetization strategy and severely degraded the user experience for readers in an attempt to generate enough revenue to justify its valuation after raising $160M. You can't trust someone else's platform to not disappear underneath you or radically change in the name of profit.
A related thing I wanted to do was write in something that's my own space (as opposed to in internet comments). I used to write a lot of HN comments, but the half-life of an HN comment is short. With very few exceptions, basically all of the views a comment is going to get will be in the first few days. With a blog, it's the other way around. A post might get burst of traffic initially but, as long as you keep writing, most traffic will come later (e.g., for my blog, I tend to get roughly twice as many hits as the baseline level when a post is on HN, and of course I don't have a post on HN most days). It isn't really much more work to write a "real blog post" instead of writing an HN comment, so I've tended to favor writing blog posts instead of HN comments. Also, when I write here, most of the value created is split between myself and readers. If I were to write on someone else's platform, most of the value would be split between the platform and readers. If I were doing video, I might not really have a choice outside of YouTube or Twitch but, for text, I have a real choice. Looking at
how things worked out for people who made the other choice and decided to write comments for a platform
, I think I made the right choice for the right seasons. I do see
the appeal of the reduced friction commenting on an existing platform offers
but, even so, I'd rather pay the cost of the extra friction and write something that's in my space instead of elsewhere.
All of that together is basically it. That's how I write.
Unlike other bloggers, I'm not going to try to tell you "how to write usefully" or "how to write well" or anything like that. I agree with Steve Yegge when he says that
you should consider writing because it's potentially high value and the value may show up in ways you don't expect
, but how you write should really come from your goals and aptitudes.
Appendix: changes in approach over time
When I started the blog, I used to worry that a post wouldn't be interesting enough because it only contained a simple idea, so I'd often wait until I could combine two or more ideas into a single post. In retrospect, I think many of my early posts would've been better off as separate posts. For example,
this post on compensation
from 2016 contains the idea that compensation might be turning bimodal and that programmers are unbelievably well paid given the barriers to entry compared to other fields that are similarly remunerative, such has finance, law, and medicine. I don't think there was much value-add to combining the two ideas into a single post and I think a lot more people would've read the bit about how unusually highly paid programmers are if it wasn't bundled into a post about compensation becoming bimodal.
Another thing I used to do is avoid writing things that seem too obvious.
But, I've come around to the idea that there's a lot of value in writing down obvious things
and a number of my most influential posts have been on things I would've previously considered too obvious to write down:
Excluding these recent posts, more people have told me that
https://danluu.com/look-stupid/
has changed how they operate than all other posts combined (and the only reason it's even close is that a lot of people have told me that my discussions of compensation caused them to realize that they can find a job they enjoy more that also pays hundreds of thousands a year more than they were previously making, which is the set of posts that's drawn the most comments from people telling me that the post was pointless because everybody knows how much you can make in tech).
A major, and relatively recent, style change I'm trying out is using more examples. This was prompted by comments from Ben Kuhn, and I like it so far. Compared to most bloggers,
I wasn't exactly light on examples in my early days
, but one thing I've noticed is that adding more examples than I would naturally tend to can really clarify things for readers; having "a lot" of examples reduces the rate at which people take away wildly different ideas than the ones I meant. A specific example of this would be, in a post discussing
what it takes to get to 95%-ile performance
, I only provided a couple examples and
many people filled in the blanks and thought that performance that's well above 99.9%-ile is 95%-ile, e.g., that being a chess GM
is 95%-ile.
Another example of someone who's made this change is Jamie Brandon. If you read his early posts,
such as this one
, he often has a compelling idea with a nice turn of phrase, e.g., this bit about when he was working on Eve with Chris Granger:
People regularly tell me that imperative programming is the natural form of programming because 'people think imperatively'. I can see where they are coming from. Why, just the other day I found myself saying, "Hey Chris, I'm hungry. I need you to walk into the kitchen, open the cupboard, take out a bag of bread, open the bag, remove a slice of bread, place it on a plate..." Unfortunately, I hadn't specified where to find the plate so at this point Chris threw a null pointer exception and died.
But, despite having parts that are really compelling, his earlier writing was often somewhat disconnected from the real world in a way that Jamie doesn't love when looking back on his old posts. On adding more details, Jamie says
The point of focusing down on specific examples and keeping things as concrete as possible is a) makes me less likely to be wrong, because non-concrete ideas are very hard to falsify and I can trick myself easily b) makes it more likely that the reader absorbs the idea I'm trying to convey rather than some superficially similar idea that also fits the vague text.
Examples kind of pin ideas down so they can be examined properly.
Another big change, the only one I'm going to discuss here that really qualifies as prose style, is that I try much harder to write things where there's continuity of something that's sometimes called "narrative grammar".
This post by Nicola Griffith has some examples of this at the sentence level
, but I also try to think about this in the larger structure of my writing. I don't think I'm particularly good at this, but thinking about this more has made my writing easier to follow. This change, especially on larger scales, was really driven by working with a professional editor who's good at spotting structural issues that make writing more difficult to understand. But, at the same time, I don't worry too much if there's a reason that something is difficult to follow. A specific example of this is, if you read answers to questions on
ask metafilter
or reddit, any question that isn't structurally trivial will have a large fraction of answers that from people who failed to read the question and answer the wrong question, e.g., if someone asks for something that has two parts connected with an
and
, many people will only read one half of the
and
and give an answer that's clearly disqualified by the
and
condition. If many people aren't going to read a short question closely enough to write up an answer that satisfies both halves of an
and
, many people aren't going to follow the simplest things anyone might want to write. I don't think it's a good use of a writer's time to try to walk someone who can't be bothered with reading both sides of an
and
through a structured post, but I do think there's value in trying to avoid "narrative grammar" issues that might make it harder for someone who does actually want to read.
Appendix: getting feedback
As we've previously discussed
, feedback can greatly facilitate improvement. Unfortunately, the idea from that post, that 95%-ile performance is generally poor, also applies to feedback, making most feedback counterproductive.
I've spent a lot of time watching people get feedback in private channels and seeing how they change their writing in response to it and, at least in the channels that I've looked at (programmers and not professional writers or editors commenting), most feedback is ignored. And when feedback is taken, because almost all feedback is bad and people generally aren't perfect or even very good at picking out good feedback, the feedback that's taken is usually bad.
Fundamentally, most feedback has the issue mentioned in this post and is a form of "you should write it like I would've written it", which generally doesn't work unless the author of the feedback is very careful in how they give the feedback, which few people are. The feedback tends to be superficial advice that misses serious structural issues in writing. Furthermore, the feedback also tends to be "lowest common denominator" feedback that turns nice prose into Strunk-and-White-ified mediocre prose. I don't think that I have a particularly nice prose style, but I've seen a number of people who have a naturally beautiful style ask for feedback from programmers, which has turned their writing into boring prose that anyone could've written.
The other side of this is that when people get what I think is good, substantive, feedback, the most common response is "nah, it's fine". I think of this as the flip side of most feedback being "you should write it how I'd write it". Most people's response to feedback is "I want to write it how I want to write it".
Although this post has focused on how a wide variety of styles can work, it's also true that, given a style and a set of goals, writing can be better or worse. But, most people who are getting feedback
don't know enough about writing to know what's better and what's worse
, so they can't tell the difference between good feedback and bad feedback.
One way around this is to get feedback from someone whose judgement you trust. As mentioned in the post, the way I did this was by hiring a professional editor whose writing (and editing) I respected.
Another thing I do, one that's a core aspect of my personality and not really about writing, is that I take feedback relatively seriously and try to avoid having a "nah, it's fine" response to feedback. I wouldn't say that this is optimal since I've sometimes spent far too much time on bad feedback, but a core part of how I think is that I'm aware that most people are overconfident and frequently wrong because of their overconfidence, so I don't trust my own reasoning and spend a relatively large amount of time and effort thinking about feedback in an attempt to reduce my rate of overconfidence.
At times, I've spent a comically long amount of time mulling over what is, in retrospect, very bad and "obviously" incorrect feedback that I've been wary of dismissing as incorrect. One thing I've noticed is that, as people gain an audience, some people become more and more confident in themselves and eventually end up becoming highly overconfident. It's easy to see how this happens — as you gain prominence, you'll get more exposure and more "fans" who think you're always right and, on the flip side, you'll also get more "obviously" bad comments.
Back when basically no one read my blog, most of the comments I got were quite good. As I've gotten more and more readers, the percentage of good comments has dropped. From looking at how other people handle this, one common failure mode is that they'll see the massive number of obviously wrong comments that their posts draw and then incorrectly conclude that all of their critics are bozos and that they're basically never wrong. I don't really have an antidote to that other than "take criticism very seriously". Since the failure mode here involves blind spots in judgement, I don't see a simple way to take a particular piece of criticism seriously that doesn't have the potential to result in incorrectly dismissing the criticism due to a blind spot.
Fundamentally, my solution to this has been to avoid looking at most feedback while trying to take feedback from people I trust.
When it comes to issues with the prose, one thing that we discussed above, hiring a professional editor whose writing and editing I respect and deferring to them on issues with my prose worked well.
When it comes to logical soundness or just general interestingness, those are a more difficult to outsource to a single person and I have
a set of people whose judgement I trust
who look at most posts. If anyone whose judgement I trust thinks a post is interesting, I view that as a strong confirmation and I basically ignore comments that something is boring or uninteresting. For almost all of my posts that are among my top posts in terms of the number of people who told me the post was life changing for them, I got a number of comments from people whose judgement I otherwise think isn't terrible saying that the post seemed boring, pointless, too obvious to write, or just plain uninteresting. I used to take comments that something was uninteresting seriously but, in retrospect, that was a mistake that cost me a lot of time and didn't improve my writing. I think this isn't so different from people who say "write how I write"; instead, it's people who have a similar mental model, but with respect to interesting-ness instead, who can't imagine that other people would find something interesting that they don't. Of course, not everyone's mind works like that, but people who are good at modeling what other people find interesting generally don't leave feedback like "this is boring/pointless", so feedback of that form is almost guaranteed to be worthless.
When it comes to the soundness of an argument, I take the opposite approach that I do for interestingness, in that I take negative comments very seriously and I don't do much about positive comments. I have, sometimes, wasted a lot of time on particular posts because of that. My solution to that has been to try to ignore feedback from people who regularly give bad feedback. That's something I think of as dangerous to do since selectively choosing to ignore feedback is a good way to create an echo chamber, but really seriously taking the time to think through feedback when I don't see a logical flaw is time consuming enough that I don't think there's really another alternative given how I re-evaluate my own work when I get feedback.
One thing I've started doing recently that's made me feel a lot better about this is to look at what feedback people give to others. People who give me bad feedback generally also give other people feedback that's bad in pretty much exactly the same ways. Since I'm not really concerned that I have some cognitive bias that might mislead me into thinking I'm right and their feedback is wrong when it comes to their feedback on other people's writing, instead of spending hours trying to figure out if there's some hole in how I'm explaining something that I'm missing, I can spend minutes seeing that their feedback on someone else's writing is bogus feedback and then see that their feedback on my writing is bogus in exactly the same way.
Appendix: where I get ideas
I often get asked how I get ideas. I originally wasn't going to say anything about this because I don't have much to say, but Ben Kuhn strongly urged me to add this section "so that other people realize what an alien you are".
My feeling is that the world is so full of interesting stuff that ideas are everywhere. I have on the order of a hundred drafts lying around that I think are basically publishable that I haven't prioritized finishing up for one reason or another. If I think of ideas where I've sketched out a post in my head but haven't written it down, the number must well into the thousands. If I were to quit my job and then sit down to write full-time until I died, I think I wouldn't run out of ideas even if I stuck to ones I've already had. The world is big and wondrous and fractally interesting.
For example, I recently took up surf skiing (a kind of kayaking) and I'd say that, after a few weeks, I had maybe twenty or so blog post ideas that I think could be written up for a general audience in the sense that
this post on branch prediction
is written for a general audience, in that it doesn't assume any hardware background. I could write two posts on different technical aspects of canoe paddle evolution and design as well as two posts on cultural factors and how they impacted the update of different canoe paddle designs. Kayak paddle design has been, in recent history, a lot richer, and that could easily be another five or six posts. The technical aspects of hull design are richer still and could be an endless source of posts, although I only have four particular posts in mind at the moment, but the cultural and historical aspects also seem interesting to me and that's what rounds out the twenty things in my head with respect to that.
I don't have twenty posts on kayaking and canoeing in my head because I'm particularly interested in kayaking and canoeing. Everything seems interesting enough to write twenty posts about. A lot of my posts that exist are part of what might become a much longer series of posts if I ever get around to spending the time to write them up. For example,
this post on decision making in baseball
was, in my head, the first of a long-ish (10+) post series on decision making that I never got around to writing that I suspect I'll never write because there's too much other interesting stuff to write about and not enough time.
Appendix: other writing about writing
Richard Lanham:
Analyzing Prose
I think it's not easy to take anything directly actionable away from this book, but I found the way that it dissects the rhythm of prose to be really interesting
Robert Alter:
The Five Books of Moses
For the footnotes on why Robert Alter made certain subtle choices in his translation
Francis-Noel Thomas & Mark Turner:
Clear and Simple as the Truth
If you want to write in a clean, authoritative, style
People who use this as a manual typically write in an unnuanced fashion with a lot of incorrect statements, but I don't think that's necessary. Also, the writing is often compelling, which many people prefer over nuance anyway; many popular writers in tech use an analogous style
Gary Hoffman & Glynis Hoffman:
Adios, Strunk & White: A Handbook for the new Academic Essay
Tracy Kidder & Richard Todd:
Good Prose: The Art of Nonfiction
This book was recommended to me by Kelly Eskridge for its in-depth look at how an editor and a writer interact and I found it useful to keep in mind when working with an editor; reading this book is probably an inefficient way to get a better understanding of what working with a good editor looks like, but it's probably worth reading if you're curious how the author of
The Soul of a New Machine
writes; if you're not sure what an editor could do for you, this is a nice read
Steve Yegge:
You Should Write Blogs
In particular, for "Reason #3", the Jacob Gabrielson / Zero Config story, although the whole thing is worth reading
Lawrence Tratt:
What I’ve Learnt So Far About Writing Research Papers
Well written, just like everyone else from Lawrence. Also, I think it's interesting in that Lawrence has a completely different process than mine in most major dimensions, but the resultant style is relatively similar if you compare across all programming bloggers (certainly more similar than any of the authors mentioned in the body of this post)
Julia Evans:
How I write useful programming comics
Nice explanation of what makes Julia's zines tick; also completely different from my approach, but this time with a completely different result
Yossi Kreinen:
Blogging is hard
(the title is a contrast to his next post, "low level is easy")
A rare example of a first post that's basically "I'm going to write a blog" that's both interesting and has interesting future posts that follow; also Yossi's writing philosophy
Phil Eaton:
What makes a great technical blog
A brief summary of properties that Phil likes in technical blogs. It's sort of the opposite of what people usually take away from Thomas and Turner's Clear and Simple as the Truth
Appendix: things that increase popularity that I generally don't do
Here are some things that I think work based on observing what works for other people that I don't do, but if you want a broad audience, perhaps you can try some of them out:
Use clickbait titles
Swearing or saying that something "is cancer" or "is the Vietnam of X" or some other highly emotionally loaded phrase seems to be particularly effective
Talk-up prestige/accomplishments/titles
Use an authoritative tone and/or style
Write things with an angry tone or that are designed to induce anger
Write frequently
Get endorsements from people
Write about hot, current, topics
Provide takes on recent events
Use deliberately outrageous / controversial framings on topics
Appendix: some snippets of writing
In case you're not familiar with the writers mentioned, here are some snippets that I think are representative of their writing styles:
Joel Spolsky:
Why I really care is that Microsoft is vacuuming up way too many programmers. Between Microsoft, with their shady recruiters making unethical exploding offers to unsuspecting college students, and Google (you're on my radar) paying untenable salaries to kids with more ultimate frisbee experience than Python, whose main job will be to play foosball in the googleplex and walk around trying to get someone...anyone...to come see the demo code they've just written with their "20% time," doing some kind of, let me guess, cloud-based synchronization... between Microsoft and Google the starting salary for a smart CS grad is inching dangerously close to six figures and these smart kids, the cream of our universities, are working on hopeless and useless architecture astronomy because these companies are like cancers, driven to grow at all cost, even though they can't think of a single useful thing to build for us, but they need another 3000-4000 comp sci grads next week. And dammit foosball doesn't play
itself
.
and
When I started interviewing programmers in 1991, I would generally let them use any language they wanted to solve the coding problems I gave them. 99% of the time, they chose C. Nowadays, they tend to choose Java ... Java is not, generally, a hard enough programming language that it can be used to discriminate between great programmers and mediocre programmers ... Nothing about an all-Java CS degree really weeds out the students who lack the mental agility to deal with these concepts. As an employer, I’ve seen that the 100% Java schools have started churning out quite a few CS graduates who are simply not smart enough to work as programmers on anything more sophisticated than Yet Another Java Accounting Application, although they did manage to squeak through the newly-dumbed-down coursework. These students would never survive 6.001 at MIT, or CS 323 at Yale, and frankly, that is one reason why, as an employer, a CS degree from MIT or Yale carries more weight than a CS degree from Duke, which recently went All-Java, or U. Penn, which replaced Scheme and ML with Java
Paul Graham:
A couple years ago a venture capitalist friend told me about a new startup he was involved with. It sounded promising. But the next time I talked to him, he said they'd decided to build their software on Windows NT, and had just hired a very experienced NT developer to be their chief technical officer. When I heard this, I thought, these guys are doomed. One, the CTO couldn't be a first rate hacker, because to become an eminent NT developer he would have had to use NT voluntarily, multiple times, and I couldn't imagine a great hacker doing that; and two, even if he was good, he'd have a hard time hiring anyone good to work for him if the project had to be built on NT.
and
What sort of people become haters? Can anyone become one? I'm not sure about this, but I've noticed some patterns. Haters are generally losers in a very specific sense: although they are occasionally talented, they have never achieved much. And indeed, anyone successful enough to have achieved significant fame would be unlikely to regard another famous person as a fraud on that account, because anyone famous knows how random fame is.
Steve Yegge:
When I read this book for the first time, in October 2003, I felt this horrid cold feeling, the way you might feel if you just realized you've been coming to work for 5 years with your pants down around your ankles. I asked around casually the next day: "Yeah, uh, you've read that, um, Refactoring book, of course, right? Ha, ha, I only ask because I read it a very long time ago, not just now, of course." Only 1 person of 20 I surveyed had read it. Thank goodness all of us had our pants down, not just me.
This is a wonderful book about how to write good code, and there aren't many books like it. None, maybe. They don't typically teach you how to write good code in school, and you may never learn on the job. It may take years, but you may still be missing some key ideas. I certainly was. ... If you're a relatively experienced engineer, you'll recognize 80% or more of the techniques in the book as things you've already figured out and started doing out of habit. But it gives them all names and discusses their pros and cons objectively, which I found very useful. And it debunked two or three practices that I had cherished since my earliest days as a programmer. Don't comment your code? Local variables are the root of all evil? Is this guy a madman? Read it and decide for yourself!
and
Jeff Bezos is an infamous micro-manager. He micro-manages every single pixel of Amazon's retail site. He hired Larry Tesler, Apple's Chief Scientist and probably the very most famous and respected human-computer interaction expert in the entire world, and then ignored every goddamn thing Larry said for three years until Larry finally -- wisely -- left the company. Larry would do these big usability studies and demonstrate beyond any shred of doubt that nobody can understand that frigging website, but Bezos just couldn't let go of those pixels, all those millions of semantics-packed pixels on the landing page. They were like millions of his own precious children. So they're all still there, and Larry is not.
Micro-managing isn't that third thing that Amazon does better than us, by the way. I mean, yeah, they micro-manage really well, but I wouldn't list it as a strength or anything. I'm just trying to set the context here, to help you understand what happened. We're talking about a guy who in all seriousness has said on many public occasions that people should be paying him to work at Amazon. He hands out little yellow stickies with his name on them, reminding people "who runs the company" when they disagree with him. The guy is a regular... well, Steve Jobs, I guess. Except without the fashion or design sense. Bezos is super smart; don't get me wrong. He just makes ordinary control freaks look like stoned hippies.
Julia Evans:
Right now I’m on a million-hour train ride from New York to Montreal. So I’m looking at the output of strace because, uh,
strace
is cool, and it is teaching me some things about how the command line tools I use all the time work.
What
strace
does is capture every single system call that gets called when executing a program. System calls are the interface between userspace programs and the kernel, so looking at the output from strace is a fun way to understand how Linux works, and what’s really involved in running a program.
For example!
killall
! I ran
strace killall ruby1.9.1 2> killall-log.
Appendix: how GPT-4o thinks people write
[2024 update]
I've seen quite a few people fawn over GPT-3, GPT-3.5's, and GPT-4's ability to "imitiate" somebody and create work that's in their style, allowing you to read hypotheetical essays or have hypothetical conversations with someone. I haven't found this to work very well in general. Below are examples of what you get with the prompt "Generate a 200 word quote about Microsoft that's something X might write." (I tried other prompts and to equally bad results, in that the content, tone, and style are not much like what any of these people actually produce):
Joel Spolsky:
Microsoft is a study in the complex interplay between engineering excellence and business acumen. They're not just a company that builds software; they're a sprawling, multi-tentacled beast that has, over decades, managed to insert itself into almost every corner of the tech industry. They’ve had their missteps—anyone remember Clippy or the Zune?—but they’ve also had spectacular successes. The magic of Microsoft lies in their ability to pivot and adapt, often turning what seems like a colossal blunder into an integral part of their strategy.
Their initial dominance was built on Windows and Office, a formidable combo that defined personal and enterprise computing for decades. But what’s really fascinating is how they’ve evolved. Under Nadella, Microsoft transformed from a lumbering giant into a nimble innovator, diving headfirst into the cloud with Azure and embracing the open-source community they once shunned. They’ve created a developer ecosystem that’s robust and, dare I say, fun to work in. Microsoft is not just about software anymore; it's about platforms, services, and an ever-growing universe of connected tools. They’re proof that even the biggest companies can stay relevant if they’re willing to rethink and reinvent themselves continually
Paul Graham:
Microsoft's journey is a quintessential example of how adaptability trumps inertia in the tech world. In its early days, the company epitomized the startup ethos of seizing opportunities, transforming from a scrappy two-man team into a juggernaut by outmaneuvering larger, more established competitors. They mastered the art of commoditizing software and built an ecosystem that turned personal computing into a universal reality. Yet, success bred complacency. For years, Microsoft clung to its Windows and Office cash cows, missing the mobile and internet revolutions as younger, nimbler rivals reshaped the industry. But Microsoft’s story didn't end there. Under Satya Nadella’s visionary leadership, the company rediscovered its startup roots, pivoting towards the cloud and embracing open source with a zeal reminiscent of its early days. This ability to transform, to reimagine itself in the face of profound industry shifts, is what keeps Microsoft relevant. It's a lesson to every startup and tech giant alike: the key to longevity is not just innovation but the relentless pursuit of reinvention. In Microsoft's world, the only constant is change, and the company's true genius lies in its unwavering ability to adapt and thrive.
Microsoft is a fascinating entity to explore, especially if you love to dive into the details of technology and see how they scale complexity. For a long time, they were the behemoth that you couldn’t avoid if you were using a computer. Windows and Office were like the air you breathed—ubiquitous and essential. But what's really interesting is how Microsoft has evolved. They’ve gone from being the gatekeepers of the desktop to pioneers in the cloud and champions of open-source.
Think about Azure. It’s this massive infrastructure that powers everything from small startups to large enterprises, enabling developers to deploy code globally with just a few clicks. And then there’s their embrace of open source. Remember when they acquired GitHub? That was a signal that Microsoft was serious about supporting the developer community. It wasn’t just a PR move; they’re contributing to and even leading projects that millions of us rely on.
Their tools have become indispensable for so many of us. Visual Studio Code, for instance, is a joy to use. It’s light, fast, and extensible—a perfect example of how Microsoft has learned to build products that developers love. It’s a company that’s not afraid to reinvent itself and, in doing so, makes our tech lives better and more interesting.
Thanks to Yossi Kreinin, Ben Kuhn, Laurence Tratt, Heath Borders, Jamie Brandon, Julia Evans, Vegard Nossum, Julien Kirch, Bram Delver, and Pam Wolf for comments/corrections/discussion.
