---
title: "UI backwards compatibility"
url: "https://danluu.com/ui-compatibility/"
fetched_at: 2026-05-05T07:01:31.314822+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# UI backwards compatibility

Source: https://danluu.com/ui-compatibility/

About once a month, an app that I regularly use will change its UI in a way that breaks muscle memory, basically tricking the user into doing things they don’t want.
Zulip
In recent memory, Zulip (a slack competitor) changed its newline behavior so that
ctrl + enter
sends a message instead of inserting a new line. After this change, I sent a number of half-baked messages and it seemed like some other people did too.
Around the time they made that change, they made another change such that a series of clicks that would cause you to send a private message to someone would instead cause you to send a private message to the alphabetically first person who was online. Most people didn’t notice that this was a change, but when I mentioned that this had happened to me a few times in the past couple weeks, multiple people immediately said that the exact same thing happened to them. Some people also mentioned that the behavior of navigation shortcut keys was changed in a way that could cause people to broadcast a message instead of sending a private message. In both cases, some people blamed themselves and didn’t know why they’d just started making mistakes that caused them to send messages to the wrong place.
Doors
A while back, I was at Black Seed Bagel, which has a door that
looks 75% like a “push” door from both sides
when it’s actually a push door from the outside and a pull door from the inside. An additional clue that makes it seem even more like a "push" door from the inside is that most businesses have outward opening doors (this is required for exit doors in the U.S. when the room occupancy is above 50 and many businesses in smaller spaces voluntarily follow the same convention). During the course of an hour long conversation, I saw a lot of people go in and out and my guess is that ten people failed on their first attempt to use the door while exiting. When people were travelling in pairs or groups, the person in front would often say something like “I’m dumb. We just used this door a minute ago”. But the people were not, in fact, acting dumb. If anything is dumb, it’s designing doors such that are users have to memorize which doors act like “normal” doors and which doors have their cues reversed.
If you’re interested in the physical world,
The Design of Everyday Things
, gives many real-world examples where users are subtly nudged into doing the wrong thing. It also discusses general principles in a way that allows you to see the general idea and apply and avoid the same issues when designing software.
Facebook
Last week, FB changed its interface so that my normal sequence of clicks to hide a story saves the story instead of hiding it. Saving is pretty much the opposite of hiding! It’s the opposite both from the perspective of the user and also as a ranking signal to the feed ranker. The really “great” thing about a change like this is that it A/B tests incredibly well if you measure new feature “engagement” by number of clicks because many users will accidentally save a story when they meant to hide it. Earlier this year, twitter did something similar by swapping the location of “moments” and “notifications”.
Even if the people making the change didn’t create the tricky interface in order to juice their engagement numbers, this kind of change is still problematic because it poisons analytics data. While it’s technically possible to build a model to separate out accidental clicks vs. purposeful clicks, that’s quite rare (I don’t know of any A/B tests where people have done that) and even in cases where it’s clear that users are going to accidentally trigger an action, I still see devs and PMs justify a feature because of how great it looks on naive statistics like
DAU
/MAU.
API backwards compatibility
When it comes to software APIs, there’s a school of thought that says that you should never break backwards compatibility for some classes of widely used software. A well-known example is
Linus Torvalds
:
People should basically always feel like they can update their kernel and simply not have to worry about it.
I refuse to introduce "you can only update the kernel if you also update that other program" kind of limitations. If the kernel used to work for you, the rule is that it continues to work for you. … I have seen, and can point to, lots of projects that go "We need to break that use case in order to make progress" or "you relied on undocumented behavior, it sucks to be you" or "there's a better way to do what you want to do, and you have to change to that new better way", and I simply don't think that's acceptable outside of very early alpha releases that have experimental users that know what they signed up for. The kernel hasn't been in that situation for the last two decades. ... We do API breakage
inside
the kernel all the time. We will fix internal problems by saying "you now need to do XYZ", but then it's about internal kernel API's, and the people who do that then also obviously have to fix up all the in-kernel users of that API. Nobody can say "I now broke the API you used, and now
you
need to fix it up". Whoever broke something gets to fix it too. ... And we simply do not break user space.
Raymond Chen quoting Colen
:
Look at the scenario from the customer’s standpoint. You bought programs X, Y and Z. You then upgraded to Windows XP. Your computer now crashes randomly, and program Z doesn’t work at all. You’re going to tell your friends, "Don’t upgrade to Windows XP. It crashes randomly, and it’s not compatible with program Z." Are you going to debug your system to determine that program X is causing the crashes, and that program Z doesn’t work because it is using undocumented window messages? Of course not. You’re going to return the Windows XP box for a refund. (You bought programs X, Y, and Z some months ago. The 30-day return policy no longer applies to them. The only thing you can return is Windows XP.)
While this school of thought is a minority, it’s a vocal minority with a lot of influence. It’s much rarer to hear this kind of case made for UI backwards compatibility. You might argue that this is fine -- people are forced to upgrade nowadays, so it doesn’t matter if stuff breaks. But even if users can’t escape, it’s still a bad user experience.
The counterargument to this school of thought is that maintaining compatibility creates technical debt. It’s true! Just for example, Linux is full of slightly to moderately wonky APIs due to the “do not break user space” dictum. One example is
int recvmmsg(int sockfd, struct mmsghdr *msgvec, unsigned int vlen, unsigned int flags, struct timespec *timeout);
. You might expect the timeout to fire if you don’t receive a packet, but the manpage reads:
The
timeout
argument points to a
struct timespec
(see clock_gettime(2)) defining a timeout (seconds plus nanoseconds) for the receive operation (
but see BUGS!
).
The BUGS section reads:
The
timeout
argument does not work as intended. The timeout is checked only after the receipt of each datagram, so that if up to
vlen-1
datagrams are received before the timeout expires, but then no further datagrams are received, the call will block forever.
This is arguably not even the worst mis-feature of
recvmmsg
,
which returns an
ssize_t
into a field of size
int
.
If you have a policy like “we simply do not break user space”, this sort of technical debt sticks around forever. But it seems to me that it’s not a coincidence that the most widely used desktop, laptop, and server operating systems in the world bend over backwards to maintain backwards compatibility.
The case for UI backwards compatability is arguably stronger than the case for API backwards compatability because breaking API changes can be mechanically fixed and,
with the proper environment
, all callers can be fixed at the same time as the API changes. There's no equivalent way to reach into people's brains and change user habits, so a breaking UI change inevitably results in pain for some users.
The case for the case for UI backwards compatibility is arguably weaker than the case for API backwards compatibility because API backwards compatibility has a lower cost -- if some API is problematic, you can make a new API and then document the old API as something that shouldn’t be used (you’ll see lots of these if you look at Linux syscalls). This doesn’t really work with GUIs since UI elements compete with each other for a small amount of screen real-estate. An argument that I think is underrated is that changing UIs isn’t as great as most companies seem to think -- very dated looking UIs that haven’t been refreshed to keep up with trends can be successful (e.g., plentyoffish and craigslist). Companies can even become wildly successful without any significant UI updates, let alone UI redesigns -- a large fraction of linkedin’s rocketship growth happened in a period where the UI was basically frozen. I’m told that freezing the UI wasn’t a deliberate design decision; instead, it was a side effect of severe technical debt, and that the UI was unfrozen the moment a re-write allowed people to confidently change the UI. Linkedin has managed to
add a lot of dark patterns
since they unfroze their front-end, but the previous UI seemed to work just fine in terms of growth.
Despite the success of a number of UIs which aren’t always updated to track the latest trends, at most companies, it’s basically impossible to make the case that UIs shouldn’t be arbitrarily changed without adding functionality, let alone make the case that UIs shouldn’t push out old functionality with new functionality.
UI deprecation
A case that might be easier to make is that shortcuts and shortcut-like UI elements can be deprecated before removal, similar to the way evolving APIs will add deprecation warnings before making breaking changes. Instead of regularly changing UIs so that users’ muscle memory is used against them and causes users to do the opposite of what they want, UIs can be changed so that doing the previously trained set of actions causes nothing to happen. For example, FB could have moved “hide post” down and inserted a no-op item in the old location, and then after people had gotten used to not clicking in the old “hide post” location for “hide post”, they could have then put “save post” in the old location for “hide post”.
Zulip could’ve done something similar and caused the series of actions that used to let you send a private message to the person you want cause no message to be sent instead of sending a private message to the alphabetically first person on the
online
list.
These solutions aren’t ideal because the user still has to retrain their muscle memory on the new thing, but it’s still a lot better than the current situation, where many UIs regularly introduce arbitrary-seeming changes that sow confusion and chaos.
In some cases (e.g., the no-op menu item), this presents a pretty strange interface to new users. Users don’t expect to see a menu item that does nothing with an arrow that says to click elsewhere on the menu instead. This can be fixed by only rolling out deprecation “warnings” to users who regularly use the old shortcut or shortcut-like path. If there are multiple changes being deprecated, this results in a combinatorial explosion of possibilities, but if you're regularly deprecating multiple independent items, that's pretty extreme and users are probably going to be confused regardless of how it's handled. Given
the amount of effort made to avoid user hostile changes
and the dominance of the “move fast and break things” mindset, the case for adding this kind of complexity just to avoid giving users a bad experience probably won’t hold at most companies, but this at least seems plausible in principle.
Breaking existing user workflows arguably doesn’t matter for an app like FB, which is relatively sticky as a result of its dominance in its area, but most applications are more like Zulip than FB. Back when Zulip and Slack were both young, Zulip messages couldn’t be edited or deleted. This was on purpose -- messages were immutable and everyone I know who suggested allowing edits was shot down because mutable messages didn’t fit into the immutable model. Back then, if there was a UI change or bug that caused users to accidentally send a public message instead of a private message, that was basically permanent. I saw people accidentally send public messages often enough that I got into the habit of moving private message conversations to another medium. That didn’t bother me too much since I’m used to
quirky software
, but I know people who tried Zulip back then and, to this day, still refuse to use Zulip due to UI issues they hit back then. That’s a bit of an extreme case, but the general idea that users will tend to avoid apps that repeatedly cause them pain isn’t much of a stretch.
In studies on user retention, it appears to be the case that an additional 500ms of page-load latency negative impacts retention. If that's the case, it seems like switching the UI around so that the user has to spend 5s undoing and action or broadcasts a private message publicly in a way that can't be undone should have a noticable impact on retention, although I don't know of any public studies that look at this.
Conclusion
If I worked on UI, I might have some suggestions or a call to action. But as an outsider, I’m wary of making actual suggestions -- programmers seem especially prone to coming into an area they’re not familiar with and telling experts how they should solve their problems. While this occasionally works, the most likely outcome is that the outsider either re-invents something that’s been known for decades or completely misses the most important parts of the problem.
It sure would be nice if shortcuts didn’t break so often that I spend as much time consciously stopping myself from using shortcuts as I do actually using the app. But there are probably reasons this is difficult to test/enforce. The huge number of platforms that need to be tested for robust UI testing make testing hard even without adding this extra kind of test. And, even when we’re talking about functional correctness problems, “move fast and break things” is much trendier than “try to break relatively few things”. Since UI “correctness” often has even lower priority than functional correctness, it’s not clear how someone could successfully make a case for spending more effort on it.
On the other hand, despite all these disclaimers, Google sometimes does the exact things described in this post. Chrome recently removed
backspace
to go backwards; if you hit
backspace
, you get a note telling you to use
alt+left
instead and when maps moved some items around a while back, they put in no-op placeholders that pointed people to the new location. This doesn't mean that Google always does this well -- on April fools day of 2016, gmail replaced
send and archive
with
send and attach a gif that's offensive in some contexts
-- but these examples indicate that maintaining backwards compatibility through significant changes isn't just a hypothetical idea, it can and has been done.
Thanks to Leah Hanson, Allie Jones, Randall Koutnik, Kevin Lynagh, David Turner, Christian Ternus, Ted Unangst, Michael Bryc, Tony Finch, Stephen Tigner, Steven McCarthy, Julia Evans, @BaudDev, and an anonymous person who has a moral objection to public acknowledgements for comments/corrections/discussion.
If you're curious why "anon" is against acknowledgements, it's because they first saw these in Paul Graham's writing, whose acknowledgements are sort of a who's who of SV. anon's belief is that these sorts of list serve as a kind of signalling. I won't claim that's wrong, but I get a lot of help with my writing both from people reading drafts and also from the occasional helpful public internet comment and I think it's important to make it clear that this isn't a one-person effort to combat
what Bunnie Huang calls "the idol effect"
.
In a future post, we'll look at empirical work on how line length affects readability. I've read every study I could find, but I might be missing some. If know of a good study you think I should include,
please let me know
.
