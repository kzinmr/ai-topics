---
title: "What We Lost When We Quit Using Crappy Old Web Forums"
url: "https://feed.tedium.co/link/15204/17371410/online-web-forums-retrospective"
fetched_at: 2026-07-02T07:01:30.904740+00:00
source: "tedium.co"
tags: [blog, raw]
---

# What We Lost When We Quit Using Crappy Old Web Forums

Source: https://feed.tedium.co/link/15204/17371410/online-web-forums-retrospective

Today in Tedium:
Recently, I passed 20,000 followers on Bluesky, which I didn’t really say anything about. Sure, I thought about it, but then I had decided to myself, what’s the point? Soon, there will be another mark I can point to and feel weird about. The thing about social media these days is that the good stuff all too often pulls you in, but at the end of the day, you end up feeling hollow. Perhaps it’s for this reason that, when I spotted a thread asking about what my favorite social network of all time was, my answer wasn’t Twitter or Bluesky or even Tumblr. It was, of all things, a forum for news designers that existed in the mid-2000s called Visual Editors. It barely worked, honestly: It had a chat option that was popular with designers waiting for their pages to get proofed late in the evening, but it would often go down with no warning. But from a community standpoint, it was spectacular. Why don’t many modern social networks feel like that? Today’s Tedium ponders the fate of the web forum.
— Ernie @ Tedium
110k
The number of newsgroups
that many modern Usenet providers, including
GigaNews
and
SuperNews
, promote as being available on their services. The Usenet system, with roots in the late 1970s, was the first forum-like system many early internet users relied on, with the other primary option being email listservs. But by the late 1990s, the not-particularly-graphical Usenet was already falling out of favor.
For laypeople who have never used one: Forums function not unlike bulletin boards covered in rows of Post-It notes. (
Patrick Perkins/Unsplash
)
Why the Web eventually moved in the direction of forums
If you think about it,
the web forum was a terrible fit for the way the Web worked. We already technically had a tool that allowed people to communicate with one another in a forum setting in the early ’90s—
Usenet
.
Or, at least, that’s what it seemed like. So I wondered, well, what did people think about the growth of web forums on Usenet? And that led me in the direction of a fascinating post from modern-day futurist Eric Hunting.
Posting on alt.hypertext in the thread “
Forums in the Web
,” in April 1994, Hunting more or less predicted what web forums would become in just a couple of years:
One of the things lacking in the environment of the Web is a means of using Web pages as a medium for conducting open discussions or forums as you have in USENET. The reason for this is probably that there is no means of packaging pages, along with all their associated graphics and multimedia data, like forum posts nor would it be practical to distribute such potentially huge amounts of data among forum servers as with USENET.
His post, which is a bit wordy, describes the concept of threads, URLs as organizing structures, and what might or might not work. Essentially, the addition of images and multimedia, a second-class citizen on a text-based forum like Usenet, would significantly reshape how people interacted on forums. One area where he was wrong, unfortunately, is a common one. He assumed that the lack of anonymity would lead people to behave a bit better online:
It’s one thing to toss out a hundred lines of spontaneous vindictiveness to the faceless USENET server, another thing to have to maintain that mass of nastiness for a specific period of time on one’s own computer. A Web Forum post wouldn’t be a message on a paper airplane tossed to the aether. It would be a billboard in your own home.
Welp, not so much. But Hunting wouldn’t have to wait long to see an implementation of a web forum in the wild. In June 1994, CERN’s Ari Luotonen
developed
what is believed to be the first Web-based forum software,
WWW Interactive Talk
(WIT).
“[Bear] in mind that this was put together in a big hurry in a few days
so forgive me if it doesn’t do yet all the things that it could do,”
Luotonen wrote
.
The software did not live for long, and no longer appears on the W3C website—a surprise because much of its early work has more or less stayed online. Not this, though—though a little Internet Archive Wayback-foo eventually helped me find where the archive file was hiding.
In hopes of kicking back off a trend in W3C-generated forums, I uploaded the software to
GitHub
. And for kicks, I got it to run in a Docker container.
If you can believe it, this forum actually works.
(Want to try it yourself?
I put it on the Web here
. Watch out for falling spam.)
While the W3C was first, there are lots of examples of similar tools out there. For example, the
Collaborative Cork Board
(CoCoBoard) was developed at the University of Illinois’ National Center for Supercomputing Applications (NCSA), the same place that launched Mosaic into the world. That tool essentially turned email replies into forum threads.
It wasn’t long before this pie in the sky concept, once the experimental territory of early Web developers working in CGI and Perl, found interest with big businesses. These were promoted as one of many examples of
groupware
. Odds are, you probably did not get your first experience posting on a Web forum using an open-source tool, but a commercial one.
One of the first companies to successfully launch a web forum startup was Lundeen & Associates, which created the WebCrossing forum tool, which was announced in the fall of 1995. Within a year, a number of major publications, including the Minneapolis
Star-Tribune
,
The New York Times
, and
Salon
, had put the software to work—in the
Times
’ case, it was part of its 1996 election coverage. While later tools became better known,
WebCrossing
may be one of the few internet-native software tools to remain in active development for more than 30 years.
(A testament to its legacy:
Salon
used the software as the anchor of its digital community for more than 15 years, only
shutting it down in 2011
out of concerns it wasn’t where the Web was going. With another 15 years of retrospect, can we argue that this was probably a bad move? Perhaps.)
But WebCrossing was far from alone.
The website Perlwatch
has a list of literally hundreds of different forum systems, some of which vary in levels of obscurity. The list, as far as I can tell, has not been updated in years, despite the site claiming otherwise. But it is an excellent historic document of what it was like looking for a bulletin board system in the late ’90s and early 2000s.
The copyright notice for WWWBoard, the widely used forum-hosting software released by Matt’s Script Archive in the late ’90s.
But even with all this competition, the most dominant player in ’90s forum software benefited from being the free option.
Matt’s Script Archive
, a collection of Perl-based website tools (including guestbooks and page counters), hit on something important with WWWboard.
That tool, a primitive forum technology that barely worked, nonetheless made threaded discussions accessible by normal people, even if it meant forums that extended well past the point of loadability and security issues that never get patched. (We wrote
a whole thing about it
last week in case you want to dive in more.)
We quickly surpassed the limited capabilities of WWWBoard. But the forum itself would eventually get left in the dust, too.
An example of a phpBB forum, one of the most common types you’d see online in the early 2000s. (Wikimedia Commons)
Five key examples of web forum software that are essential to internet history
Ultimate Bulletin Board
.
This software, later known as UBB and UBB.classic, found broad popularity on the internet thanks in large part to its low cost. It was a significant step up from WWWboard, in a good way. The software was originally developed around 1996 by Social Strata, which exists today under the name
CrowdStack
. (That said, its history is a bit winding, so not every version may work the same.)
Slash
.
Developed by Rob Malda in 1998 as a way to help manage the forums on his popular tech-news site
Slashdot
, Slash proved supremely influential as a community management tool. (A big part of the reason? It came with really strong self-moderation features that were later copied by platforms like Hacker News, Digg, and Reddit.) While it’s not totally clear if Slashdot itself still uses Slash today (Malda, for one, left years ago), the site
SoylentNews
is known to use a direct fork of it.
vBulletin
.
This is one of the more recognizable forum platforms on the internet, in part because of its use on some very prominent forums. Notably, Something Awful’s
infamous forums
use vBulletin, but that’s only half the story there: The software was forked years ago, and has been heavily modified and customized by SA’s moderators and owners over the past two decades. At this point, it’s more theirs than vBulletin’s.
phpBB
.
While vBulletin, which came out around the same time as phpBB, is a commercial tool, phpBB has always been free and open source, and as a result, has found a massive community of people willing to write extensions for it. The similar
nodeBB
is a modernization of the phpBB approach and mostly works the same.
Discourse
.
While it’s not the only tool of its kind, the decision by Jeff Atwood, Robin Ward, and Sam Saffron to build a new type of forum software was a big deal in 2014. After all, it was a medium in severe need of reinvention. (The move to a Ruby codebase, for example, was an important shift at a time when many forums still ran on PHP or Perl.) It can be seen as a continuation of Stack Exchange, a popular platform for programmer discussions that Atwood co-founded in 2008.
1985
The year that The Whole Earth ‘Lectronic Link,
also known as
The Well
, first got its start. It is one of the longest continuously running online communities in digital culture, and unlike most bulletin boards or online services of its kind, it successfully made the jump to the Web. It remains active today as a paid private community. (The Well actually sponsored Tedium a million moons ago, which I realize is a cool thing to be able to say.)
A list of some of BBCode’s layout options, as offered by the Something Awful Forums.
Before there was Markdown, there was BBCode
One challenge that a lot of early forums had to navigate was the necessity of sanitizing the text that people posted in forums. People could post literally anything in a form, and it could break the site, encourage exploits, the whole bit.
(When you don’t sanitize, you run into issues like making it possible to
put CSS on MySpace pages
.)
But on the other hand, you still wanted your websites to have at least
some
style to them, in a controlled way, without a lot of extra junk. These days, a lot of platforms use Markdown to solve this problem, in part because of
its ubiquity
. But before that, people posting on forums needed alternative options that made room for fun if not for putting malware on your forum.
That led to the creation of BBCode in 1998, first starting with UBB, then spreading to other forum platforms like phpBB and vBulletin. (There is a BBCode dot org dedicated to this scripting language, but I refuse to link to it because it’s now a Web3 SEO play.) While it doesn’t get the modern level of attention Markdown does, it is both older and more capable than Markdown is, for better or worse.
A subset of HTML, it effectively replaced the
<
or
>
with
[
and
]
, and removed the ability to add a bunch of extra stuff that the HTML spec was capable of doing. Forum owners naturally appreciated this because it gave them a bit of control over what users could do on their platform. JavaScript might be off the table, but 300 point text? Suddenly possible. A library of common images? Absolutely, they were called image macros. And features that make the forum more usable? You bet.
This lingo would sometimes shape the community as a whole. Fans of Something Awful, for example, likely remember the forums had a number of image macros, most notably :10bux:, which displayed an image of a $10 bill, reflecting the forum’s infamous one-time entry fee. And on some forums, BBCode would end up getting used in experimental ways, helping to generate some early meme culture. In its own way, BBCode was what made forums more than just Usenet in HTML format.
The downside is that the security reasons were more pronounced in theory than in practice.
A 2005 blog post by developer Chris Shiflett
argued that the security reason for BBCode was a lot weaker than it seemed:
As regular readers of Security Corner know, input must always be filtered. When you’re allowing users to enter very complex data, creating a whitelist of acceptable characters can be very difficult. Because of this, many developers employ very weak filtering rules for such input and rely on the escaping performed by
htmlentities()
for protection.
While
htmlentities()
can save you from poorly filtered data, relying on escaping alone is not ideal. Because an attacker can send any type of data, it’s equally unwise to rely on BBCode for protection—you can’t assume that the attackers will abide by your rules unless you enforce those rules in your programming logic.
But even if the security reasons didn’t matter so much, Shiflett conceded that it was good for users and may in some cases even be easier to remember than actual HTML. (Though on the other hand, one presumes BBCode did discourage some people from trying out forums entirely. Those were the people who eventually went to Facebook.)
A similar concept in content management systems associated with WordPress, the
shortcode
, became a popular technique for helping visually modify or organize content on a page. (Tedium uses shortcodes with Markdown.)
More video games should be programmed with a little BBCode.
But what may be the most interesting legacy for BBCode in the modern day might not even be forums. The game development tool Godot
has adopted the scripting language
for writing formatted text within its node-driven interface. Which, given Godot’s
surge in popularity
over the past few years, likely means that a lot of modern games you enjoy might be secretly taking advantage of a tool developed for forum software built in Perl roughly 30 years ago.
Guess we can
indirectly blame Unity
for helping give BBCode a second wind. What a story arc.
“We’re shrinking the world. It used to be that just a few people saw your photo. Now many do. We helped people in Tunisia broadcast what was happening, and they could hear people around the world supporting them.”
— Dick Costolo,
the former CEO of Twitter (in the pre-Elon days), discussing what made Twitter such a powerful tool. While this shrinking of our world might seem like a good thing (with the Arab Spring a go-to example at the time Costolo was leading the company), recent thinking has moved in a different direction. “There is something terribly wrong with social media,” psychologist Nigel Barber
argued in 2024
. “The problem is that they are run by an engagement algorithm that ignores the principles of successful communities.” The concept of content collapse likely also plays a role here. “The problem is not lack of context,”
cultural anthropologist Michael Wesch
wrote in 2009 about the then-new concept of YouTube. “It is context collapse: an infinite number of contexts collapsing upon one another into that single moment of recording.”
Why did forums lose out to social media?
I think the short answer comes down to novelty. Much like Usenet a decade earlier, we were ready for something different, having seen the weaknesses of forums in the late 1990s and early 2000s. We were ready to let someone else handle the technology part.
Plus, there’s the issue of scale. In so many ways, having a forum run by someone in a community on shared hosting meant that you couldn’t have a community unless there was someone willing to take on that commitment. They were on the hook not just to pay for the hosting, but to spend a terrible night managing things when the server got full, hacked, or simply overheated because Slashdot linked one of your threads.
In many ways, the technical argument made it an easy target for Web 2.0. There’s a reason why Digg, Reddit, and StackOverflow are perhaps the best manifestations of that era of technology. They were purpose-built community platforms that modernized things just enough that people who were looking for something a little better than we were getting from the thing that your friend built.
We tried the forum thing. We wanted something else. Not necessarily because it was better, though sure, maybe it was. But because it was different.
Visual Editors, the forum where I posted for way too many years before I discovered a thing called Twitter. Would I have been better off sticking with VizEds?
I want to pose a question: Is it possible that online users just have nonstop shiny object syndrome, and even if forums worked correctly and did the job, users would still move onto something else because we’re never happy? I think the argument is pretty strongly yes.
That said, I do think that as the internet matures into something that is more furniture in our lives, perhaps some of us will slow down. Maybe we’ll log into a forum and realize what we actually wanted out of our online experience was never the ability to reach everyone, but to reach the small number of people that think kind of like us. Maybe the “collisions” that modern social networks create just make things worse, even if it means we don’t get the occasional ego boost of Patton Oswalt replying to our tweet or whatever.
There was charm to all that barely-working PHP and Perl code that I think we’re still trying to recapture a quarter-century later.
--
Find this one an interesting read?
Share it with a pal
!
And we just added a bunch of new items to the
Tedium Shopping Network
. Maybe you might see something there you don’t need. Check it out.
