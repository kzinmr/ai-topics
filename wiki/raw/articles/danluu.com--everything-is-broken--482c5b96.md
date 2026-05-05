---
title: "One week of bugs"
url: "https://danluu.com/everything-is-broken/"
fetched_at: 2026-05-05T07:01:34.431665+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# One week of bugs

Source: https://danluu.com/everything-is-broken/

If I had to guess, I'd say I probably work around hundreds of bugs in an average week, and thousands in a bad week. It's not unusual for me to run into a hundred new bugs in a single week. But I often get skepticism when I mention that I run into multiple new (to me) bugs per day, and that this is inevitable if we don't change how we write tests. Well, here's a log of one week of bugs, limited to bugs that were new to me that week. After a brief description of the bugs, I'll talk about what we can do to improve the situation. The obvious answer to spend more effort on testing, but everyone already knows we should do that and no one does it. That doesn't mean it's hopeless, though.
One week of bugs
Ubuntu
When logging into my machine, I got a screen saying that I entered my password incorrectly. After a five second delay, it logged me in anyway. This is probably at least two bugs, perhaps more.
GitHub
GitHub switched from Pygments to whatever they use for Atom,
breaking syntax highlighting for most languages
. The HN comments on this indicate that it's not just something that affects obscure languages; Java, PHP, C, and C++ all have noticeable breakage.
In a GitHub issue
, a GitHub developer says
You're of course free to fork the Racket bundle and improve it as you see fit. I'm afraid nobody at GitHub works with Racket so we can't judge what proper highlighting looks like. But we'll of course pull your changes thanks to the magic of O P E N S O U R C E.
A bit ironic after the recent keynote talk by another GitHub employee titled
“move fast and break nothing”
. Not to mention that it's unlikely to work. The last time I submitted a PR to linguist, it only got merged after I wrote
a blog post pointing out that they had 100s of open PRs, some of which were a year old
, which got them to merge a bunch of PRs after the post hit reddit. As far as I can tell, "the magic of O P E N S O U R C E" is code for the magic of hitting the front page of reddit/HN or having lots of twitter followers.
Also, icons were broken for a while. Was that this past week?
LinkedIn
After replying to someone's “InMail”, I checked on it a couple days later, and their original message was still listed as unread (with no reply). Did it actually send my reply? I had no idea, until the other person responded.
Inbox
The Inbox app (not to be confused with Inbox App) notifies you that you have a new message before it actually downloads the message. It takes an arbitrary amount of time before the app itself gets the message, and refreshing in the app doesn't cause the message to download.
The other problem with notifications is that they sometimes don't show up when you get a message. About half the time I get a notification from the gmail app, I also get a notification from the Inbox app. The other half of the time, the notification is dropped.
Overall, I get a notification for a message that I can read maybe 1/3 of the time.
Google Analytics
Some locations near the U.S. (like Mexico City and Toronto) aren't considered worthy of getting their own country. The location map shows these cities sitting in the blue ocean that's outside of the U.S.
Octopress
Footnotes don't work correctly on the main page if you allow posts on the main page (instead of the index) and use the syntax to put something below the fold. Instead of linking to the footnote, you get a reference to anchor text that goes nowhere. This is in addition to the other footnote bug I already knew about.
Tags are only downcased in some contexts but not others, which means that any tags with capitalized letters (sometimes) don't work correctly. I don't even use tags, but I noticed this on someone else's blog.
My Atom feed
doesn't work correctly
.
If you consider performance bugs to be problems, I noticed so many of those this past week that they
have their own blog post
.
Running with Rifles (Game)
Weapons that are supposed to stun injure you instead. I didn't even realize that was a bug until someone mentioned that would be fixed in the next version.
It's possible to stab people through walls.
If you're holding a key when the level changes, your character keeps doing that action continuously during the next level, even after you've released the key.
Your character's position will randomly get out of sync from the server. When that happens, the only reliable fix I've found is to randomly shoot for a while. Apparently shooting causes the client to do something like send a snapshot of your position to the server? Not sure why that doesn't just happen regularly.
Vehicles can randomly spawn on top of you, killing you.
You can randomly spawn under a vehicle, killing you.
AI teammates don't consider walls or buildings when throwing grenades, which often causes them to kill themselves.
Grenades will sometimes damage the last vehicle you were in even when you're nowhere near the vehicle.
AI vehicles can get permanently stuck on pretty much any obstacle.
This is the first video game I've played in about 15 years. I tend to think of games as being pretty reliable, but that's probably because games were much simpler 15 years ago. MS Paint doesn't have many bugs, either.
Update: The sync issue above is caused by memory leaks. I originally thought that the game just had very poor online play code, but it turns out it's actually ok for the first 6 hours or so after a server restart. There are scripts around to restart the servers periodically, but they sometimes have bugs which cause them to stop running. When that happens on the official servers, the game basically becomes unplayable online.
Julia
Unicode sequence causes match/ismatch to blow up with a bounds error.
Unicode sequence causes using a string as a hash index to blow up with a bounds error.
Exception randomly not caught by catch. This sucks because putting things in a try/catch was the workaround for the two bugs above. I've seen other variants of this before; it's possible this shouldn't count as a new bug because it might be the same root cause as some bug I've already seen.
Function (I forget which) returns completely wrong results when given bad length arguments. You can even give it length arguments of the wrong type, and it will still “work” instead of throwing an exception or returning an error.
If API design bugs count, methods that work operation on iterables sometimes take the stuff as the first argument and sometimes don't. There are way too many of these to list. To take one example,
match
takes a regex first and a string second, whereas
search
takes a string first and a regex second. This week, I got bit by something similar on a numerical function.
And of course I'm still running into the
1+ month old bug that breaks convert
, which is pervasive enough that anything that causes it to happen renders Julia unusable.
Here's one which might be an OS X bug? I had some bad code that caused an infinite loop in some Julia code. Nothing actually happened in the
while
loop, so it would just run forever. Oops. The bug is that this somehow caused my system to run out of memory and become unresponsive. Activity monitor showed that the kernel was taking an ever increasing amount of memory, which went away when I killed the Julia process.
I won't list bugs in packages because there are too many. Even in core Julia, I've run into so many Julia bugs that I don't file bugs any more. It's just too much of an interruption. When I have some time, I should spend a day filing all the bugs I can remember, but I think it would literally take a whole day to write up a decent, reproducible, bug report for each bug.
See
this post
for more on why I run into so many Julia bugs.
Google Hangouts
On starting a hangout: "This video call isn't available right now. Try again in a few minutes.".
Same person appears twice in contacts list. Both copies have the same email listed, and double clicking on either brings me to the same chat window.
UW Health
The latch mechanism isn't quite flush to the door on about 10% of lockers, so your locker won't actually be latched unless you push hard against the door while moving the latch to the closed position.
There's no visual (or other) indication that the latch failed to latch. As far as I can tell, the only way to check is to tug on the handle to see if the door opens after you've tried to latch it.
Coursera, Mining Massive Data Sets
Selecting the correct quiz answer gives you 0 points. The workaround (independently discovered by multiple people on the forums) is to keep submitting until the correct answer gives you 1 point. This is a week after a quiz had incorrect answer options which resulted in there being no correct answers.
Facebook
If you do something “wrong” with the mouse while scrolling down on someone's wall, the blue bar at the top can somehow transform into a giant block the size of your cover photo that doesn't go away as you scroll down.
Clicking on the activity sidebar on the right pops something that's under other UI elements, making it impossible to read or interact with.
Pandora
A particular station keeps playing electronic music, even though I hit thumbs down every time an electronic song comes on. The seed song was a song from a Disney musical.
Dropbox/Zulip
An old issue is that you can't disable notifications from
@all
mentions. Since literally none of them have been relevant to me for as long as I can remember, and
@all
notifications outnumber other notifications, it means that the majority of notifications I get are spam.
The new thing is that I tried muting the streams that regularly spam me, but the notification blows through the mute. My fix for that is that I've disabled all notifications, but now I don't get a notification if someone DMs me or uses
@danluu
.
Chrome
The Rust guide is unreadable with my version of chrome (no plug-ins).
Google Docs
I tried co-writing a doc with
Rose Ames
. Worked fine for me, but everything displayed as gibberish for her, so we switched to hackpad.
I didn't notice this until after I tried hackpad, but Docs is really slow. Hackpad feels amazingly responsive, but it's really just that Docs is laggy. It's the same feeling I had after I tried fastmail. Gmail doesn't seem slow until you use something that isn't slow.
Hackpad
Hours after the doc was created, it says “ROSE AMES CREATED THIS 1 MINUTE AGO.”
The right hand side list, which shows who's in the room, has a stack of N people even though there are only 2 people.
Rust
After all that, Rose and I worked through the Rust guide. I won't list the issues here because they're so long that our hackpad doc that's full of bugs is at least twice as long as this blog post. And this isn't a knock against the Rust docs, the docs are actually much better than for almost any other language.
WAT
What's going on here? If you include the bugs I'm not listing because the software is so buggy that listing all of the bugs would triple the length of this post, that's about 80 bugs in one week. And that's only counting bugs I hadn't seen before. How come there are so many bugs in everything?
A common response to this sort of comment is that it's open source, you ungrateful sod, why don't you fix the bugs yourself? I do fix some bugs, but there literally aren't enough hours in a week for me to debug and fix every bug I run into. There's a tragedy of the commons effect here. If there are only a few bugs, developers are likely to fix the bugs they run across. But if there are so many bugs that making a dent is hopeless, a lot of people won't bother.
I'm going to take a look at Julia because I'm already familiar with it, but I expect that it's no better or worse tested than most of these other projects (except for Chrome, which is relatively well tested). As a rough proxy for how much test effort has gone into it, it has 18k lines of test code. But that's compared to about 108k lines of code in
src
plus
Base
.
At every place I've worked, a 2k LOC prototype that exists just so you can get preliminary performance numbers and maybe play with the API is expected to have at least that much in tests because otherwise how do you know that it's not so broken that your performance estimates aren't off by an order of magnitude? Since complexity doesn't scale linearly in LOC, folks expect a lot more test code as the prototype gets bigger.
At 18k LOC in tests for 108k LOC of code, users are going to find bugs. A lot of bugs.
Here's where I'm supposed to write an appeal to take testing more seriously and
put real effort into it
. But we all know that's not going to work. It would take 90k LOC of tests to get Julia to be as well tested as a poorly tested prototype (falsely assuming linear complexity in size). That's two person-years of work, not even including time to debug and fix bugs (which probably brings it closer to four of five years). Who's going to do that? No one. Writing tests is like writing documentation. Everyone already knows you should do it. Telling people they should do it adds zero information.
Given that people aren't going to put any effort into testing, what's the best way to do it?
Property-based testing. Generative testing. Random testing. Concolic Testing (which was done long before the term was coined). Static analysis.
Fuzzing
.
Statistical bug finding
. There are lots of options. Some of them are actually the same thing because the terminology we use is inconsistent and buggy. I'm going to arbitrarily pick one to talk about, but they're all worth looking into.
People are often intimidated by these, though. I've seen a lot of talks on these and they often make it sound like this stuff is really hard.
Csmith
is 40k LOC.
American Fuzzy Lop
's compile-time instrumentation is smart enough to
generate valid JPEGs
.
Sixth Sense
has the same kind of intelligence as American Fuzzy Lop in terms of exploration, and in addition, uses symbolic execution to exhaustively explore large portions of the state space; it will formally verify that your asserts hold if it's able to collapse the state space enough to exhaustively search it, otherwise it merely tries to get the best possible test coverage by covering different paths and states. In addition, it will use symbolic equivalence checking to check different versions of your code against each other.
That's all really impressive, but you don't need a formal methods PhD to do this stuff. You can write a fuzzer that will shake out a lot of bugs in an hour. Seriously. I'm a bit embarrassed to link to this, but
this fuzzer
was written in about an hour and found 20-30 bugs, including incorrect code generation, and crashes on basic operations like multiplication and exponentiation. My guess is that it would take another 2-3 hours to shake out another 20-30 bugs (with support for more types), and maybe another day of work to get another 20-30 (with very basic support for random expressions). I don't mention this because it's good. It's not. It's totally heinous. But that's the point. You can throw together an absurd hack in an hour and it will turn out to be pretty useful.
Compared to writing unit tests by hand: even if I knew what the bugs were in advance, I'd be hard pressed to code fast enough to generate 30 bugs in an hour. 30 bugs in a day? Sure, but not if I don't already know what the bugs are in advance. This isn't to say that unit testing isn't valuable, but if you're going to spend a few hours writing tests, a few hours writing a fuzzer is going to go a longer way than a few hours writing unit tests. You might be able to hit 100 words a minute by typing, but your CPU can easily execute 200 billion instructions a minute. It's no contest.
What does it really take to write a fuzzer? Well, you need to generate random inputs for a program. In
this case
, we're generating random function calls in some namespace. Simple. The only reason it took an hour was because I don't really get Julia's reflection capabilities well enough to easily generate random types, which resulted in my writing the type generation stuff by hand.
This applies to a lot of different types of programs. Have a GUI? It's pretty easy to prod random UI elements. Read files or things off the network? Generating (or mutating) random data is straightforward. This is something anyone can do.
But this isn't a silver bullet. Lackadaisical testing means that
your users will find bugs
. However, even given that developers aren't going to spend nearly enough time on testing, we can do a lot better than we're doing right now.
Resources
There are a lot of great resources out there, but if you're just getting started, I found
this description of types of fuzzers
to be one of those most helpful (and simplest) things I've read.
John Regehr has
a udacity course on software testing
. I haven't worked through it yet (Pablo Torres just pointed to it), but given the quality of Dr. Regehr's writing, I expect the course to be good.
For more on my perspective on testing,
there's this
.
Acknowledgments
Thanks to Leah Hanson and Mindy Preston for catching writing bugs, to Steve Klabnik for explaining the cause/fix of the Chrome bug (bad/corrupt web fonts), and to Phillip Joseph for finding a markdown bug.
I'm experimenting with blogging more by spending less time per post and just spewing stuff out in 30-90 minute sitting. Please
let me know
if something is unclear or just plain wrong. Seriously.
