---
title: "The day GIF became free to use, forever"
url: "https://dfarq.homeip.net/the-day-gif-became-free-to-use-forever/?utm_source=rss&utm_medium=rss&utm_campaign=the-day-gif-became-free-to-use-forever"
fetched_at: 2026-10-02T10:01:06.695833+00:00
source: "dfarq.homeip.net"
tags: [blog, raw]
---

# The day GIF became free to use, forever

Source: https://dfarq.homeip.net/the-day-gif-became-free-to-use-forever/?utm_source=rss&utm_medium=rss&utm_campaign=the-day-gif-became-free-to-use-forever

October 1, 2006 was a good day. It was the day that the last of the patents covering the GIF file format finally expired and GIF became free to use. Today GIF is a staple of social media, but it was also a staple of the early web, and, indeed, telecommunications before the Internet became accessible to the average household.
Origins of GIF
A tangled web of companies had intellectual property tied up in the GIF file format preventing its free use.
Originally, GIF was a file format developed by
CompuServe
and released in
June 1987
to provide a cross-platform graphics format their subscribers could use to share graphics online. The format caught on and proliferated throughout online services and bulletin boards. Almost anyone who was online prior to the World Wide Web becoming popular downloaded at least one GIF file at some point. GIF was free for anyone to use as far as CompuServe was concerned, at least in those early days.
When the World Wide Web came along in the early ’90s and made the Internet more accessible to all, GIF was one of the graphics file formats it supported. It was widely understood, it had widespread software support, gave excellent compression on images that didn’t originate as photos, and it decompressed and rendered faster than JPEG because it originated at a time when 8 MHz was a fast CPU. In fact, the web supported GIF before it supported JPEG.
It was unusual to visit a Web page in 1994 and for it to not have at least one GIF image in it. Early web designers used them to provide graphical elements to break up the wall of text, but we also used them in more subtle ways. One example was using them as a background pattern. By default, the Web was black text on a gray background. Designers would make patterns to make the background a little more visually interesting than one of 216 solid background colors. Technically, any computer on the Web could display at least 256 colors, but there were 216 of them that were always the same regardless of browser and platform. Creating seamlessly repeating textures that used combinations of those 216 colors was an easy way to dress up a Web page in the early days.
The invisible GIF hack
But it wasn’t long before the GIF took on another important element. Early HTML didn’t give a lot of control over the text. You could change the font, you could boldface some or all of it, and you could do the same for italics and underlining, and you could change the size. But you didn’t really have the degree of control over it that graphic designers were used to having in other media.
The trick was to use a single pixel transparent GIF file as a spacer. You could drop that image anywhere on the page and specify a height or width in pixels to force white space there. It was a trick to change the line spacing in your text or to put a variable width space somewhere in your text if you wanted it.
I don’t know who invented this technique. I read about it in a book titled
Web Sites that Work
by Roger Black and Sean Elder.
Here’s a blog post I wrote about that back in 2002
. I had at least two different people tell me about Black’s book within 30 days of each other. I had a friend who worked in a bookstore, so he used his employee discount to get me a copy.
It wasn’t long before everyone I knew was using that trick on their web pages. Suddenly, we could do most of things we learned how to do in our graphic design classes on the web. It was great.
A funny story about the invisible GIF
Fast forward a few years. I was using this trick in an early version of this blog, when someone emailed me and accused me of using the blog to spy on him. I asked what he meant. He told me I was using web bugs, and he pointed me to my invisible GIF file. I said I was using that for line spacing and paragraph spacing. He insisted I was using it to track what he was reading.
There were people who used an invisible GIF file to do some tracking. The trick was to host that file on a web server somewhere, embedded in an email message or something else, and then when someone retrieved that file, they would have an entry in your server log.
So it was possible to use the invisible GIF file as a crude tracking mechanism. But that’s not what I was doing. Some things about the Internet never change: Everyone’s an expert.
Painting the whole screen with GIFs
Cyberrebate’s web page was very heavy on GIFs. Every clickable element, the banner up top, and the sidebar on the right are all GIFs.
A more extreme design technique was to draw the major design elements of a page in Photoshop, then slice it into smaller GIFs, and reassemble the pieces in HTML. This allowed designers complete control over how the page rendered, including placement of elements and the ability to use any fonts they wanted. The tradeoff was speed. Designers would code pages specially to line the elements up so the page was halfway readable while the GIFs slowly downloaded and populated the screen at dialup speed.
In the example on the right, the old
Cyberrebate.com page
, everything on the page that wasn’t Times New Roman was a GIF, including the banner, the sidebar, all the logos, and the clickable buttons.
When you pull up an old page on archive.org and see blank squares missing, that’s an artifact of that type of design.
This technique is completely obsolete today but was common in the late 1990s, at least until patents made it dangerous.
Why GIF wasn’t truly free
The problem keeping GIF from being truly free was that it used a compression algorithm, Lempel-Ziv-Welch, or LZW, that was still protected by a patent. When it was just private individuals sharing images with each other, nobody really cared. CompuServe wasn’t aware of the patent at the time it used LZW. But once it started looking like people would start using the Internet for commercial purposes, those patents became a problem. Of course the patent holder,
Unisys
, was going to
try to monetize that
.
Commercial graphics software was already paying a royalty on the patent, so it wasn’t necessarily a huge deal for someone using commercial graphics software to create their Web page. But software that didn’t cost anything was another problem. Most software of that type stopped supporting the file format. When Unisys announced owners of non-commercial and private web sites had the “opportunity” to obtain a license for a one-time payment of $5,000 or $7,500, there was understandable backlash.
Alternatives to GIF
Some websites started using the JPEG file format exclusively. But some implementations of JPEG made certain types of images, especially line drawings, look terrible. It would introduce artifacts that made it impossible to draw a straight line, for example.
The PNG file format was a reaction against the GIF patents. The goal was to make a non-lossy file format that used a compression method not covered by any patent. They chose Deflate, the method used by Phil Katz’
ZIP
. And while they were at it, they made it possible to support 24-bit images with 16.8 million colors, rather than stopping at 8-bit images with 256 colors. PNG also had transparency.
The only thing it didn’t have was support for animation. I didn’t miss that, but I was probably in the minority on that.
It wasn’t terribly long before HTML matured to the point where you didn’t need hacks involving invisible GIFs to adjust line spacing and position elements on a page. I just got out of the habit of using the file format at all. When I did need a graphical element, I just used JPEG or PNG and got on with life.
I think a lot of other people did the same, so it’s likely the GIF patents didn’t turn into the revenue source everyone expected.
Choosy browsers choose GIF
Unisys’ patents expired worldwide in 2003 and 2004, but IBM held a relevant patent that didn’t expire until 2006. While few really expected IBM to take the hard line Unisys had, given IBM’s problems with
SCO
, there wasn’t much reason to take chances. On October 1, 2006, that final IBM patent expired. GIF was free for any and all use.
Not long after that last patent expired, animated GIFs came back with a vengeance. It was a convenient file format for sharing short videos on social media. Animation was the one thing GIF did that PNG didn’t. Animated versions of PNG such as APNG existed, but
Internet Explorer
didn’t support them. Internet Explorer
did
support GIF, so GIF became the cross-browser animated file format standard by default. When Edge switched to Chromium, it supported all of the file formats Chrome and Firefox did, but GIF had momentum by then. With no financial incentive to switch, GIF stuck this time.
Today it may seem hard to believe that the file format virtually vanished from the Internet for about 10 years. We’re still
arguing how to pronounce it though
.
David Farquhar is a computer security professional, entrepreneur, and author. He has written professionally about computers since 1991, so he was writing about retro computers when they were still new. He has been working in IT professionally since 1994 and has specialized in vulnerability management since 2013. He holds Security+ and CISSP certifications. Today he blogs five times a week, mostly about retro computers and retro gaming covering the time period from 1975 to 2000.
Related stories by Dave Farquhar
