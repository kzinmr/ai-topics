---
title: "Scam Telegram: Uncovering a network of groups spreading crypto drainers"
url: "https://timsh.org/scam-telegram-investigation/"
fetched_at: 2026-05-01T07:01:00.413806+00:00
source: "timsh.org"
tags: [blog, raw]
---

# Scam Telegram: Uncovering a network of groups spreading crypto drainers

Source: https://timsh.org/scam-telegram-investigation/

I accidentally discovered a network of hundreds of fake DeFi support chats spreading various phishing sites with wallet stealers and drainers, including infamous Inferno Drainer.
TL;DR
While searching for a contact of a member of one DeFi project, I found a fake "Official Support" group with botted members and strange-looking instructions for users seeking help.
This made me curious if there were any other chats like that, so I started looking for them manually and later on scraping those chats to extract details of their connections, admins and the phishing websites they're spreading.
I gathered and visualised all of that data and found out all of those chats were connected to each other in multiple ways - via shared admins, users and malicious instructions.
Then I analysed the code of these drainer websites and was quite surprised to find out later that these were the instances of Inferno Drainer.
This post is my longest one yet, - a result of months-long investigation made in collaboration with other researchers:
iggisv9t
, who helped with network analisys and visualisations.
noid
and @
blackbigswan
from SEAL (
Security Alliance
), who helped me dig into the drainer code, level up the scraping and take the necessary action.
By now, we've been able to understand their operations better and report, blacklist or take down almost all of the websites we could find.
my friends from @
unvariantio
, who looked on the on-chain side of things and the smart contracts used by the scammers.
If you're a member of any web3 / DeFi protocol or someone who can influence their actions - please don't miss the
suggestions section
, which I hope could help improve the security situation in the field.
Check out the
SEAL post
as well!
And buckle up - there's a long and twisted story ahead.
How it started
Honestly, quite randomly - kinda same as with Youtube videos and Github repositories: I was looking for an official Telegram community of ListaDAO, a web3 project, - the reason why is not really important.
Anyway, as I was typing in "ListaDAO" in Telegram search, I got kinda surprised:
Can you guess which one is actually the "Official" one?
Ok, probably the
@ListaDAO
one, right?
What about the
@ListaDAOChannel
with 3 times more members?
Well, with Lista, it was kinda simple - they have a link to their official community on their website
https://lista.org/
- the
@ListaDAO
is indeed the one.
Ok, so if
@ListaDAOChannel
is not the official one - what is it?
First strange thing that I noticed immediately:
The top one is the official one: ~1% of online members is rather low, but makes total sense. The 20k/63k doesn't.
I went on to see the list of chat members - obviously, it looked like this:
Ok, so it's a chat with a bunch of botted members imitating a real one... but why?
Well, basically, that's what this whole story is about.
"Ok", I thought. "What pops up if I look up any other protocol name?"
I put in "Infinifi" as an example:
All right, this one is trickier. Apart from
Сергей
who probably has 0 clue how valuable his handle is, all of the chats look kinda same - +- same amount of members, similar titles and usernames (apart from the
@infini
t
labsofficial
).
Question is - which one is the official one?
You got it right - none of them! Infinifi, which's got around
$150m TVL
at the time of writing this, does not list any official Telegram link on their
website
, nor on discord or X.
Strange stuff... At this point, I had already got an idea that it must be some sort of fraud - so I decided to look through all of the fake chats, their attachments, links e.t.c.
And so I found this:
urls are redacted here and later on for obvious reasons
Apart from this text being quite poorly written, it also contains a step-by-step guide for solving almost any problem you might have encountered and a very strange link. Definitely not a normal-looking official project link. And it's hosted for free on
Cloudflare Pages
, which doesn't add any credibility to it.
All right, "React App" by "Neutral Protocol", what would happen if I hit "Resolve issue" or (for some reason) connect my wallet?
Obviously, nothing would be fixed apart from my balance falling to 0$.
But let's not focus on this one particular website for now - there is a whole section below about various deceptive websites that I found later.
At this point, I already had a basic idea of what to do next: I opened up DefiLlama, scrolled down to the Protocol Rankings and decided to look up every project in the Telegram search to see if they also had these fake chats.
Of course they did.
In fact, there was only one project in the top 30+ that didn't (and still doesn't) have any chats impersonating it - Curve finance (lol).
Maybe
@newmichwill
knows something others don't? :)
Soon enough I started to notice similarities between chats:
same messages like this one leading people to DMs
same stickers from a pack with flashy "ADMINS WILL NEVER DM FIRST" etc animated texts
messages from bots mimicking popular community management ones like
@Rose
and
@GroupHelp
By the way, the obsession with "Never DM first" of these guys is hilarious: every announcement, "official" message, even most of the admins have it in their name.
Speaking about admins - after checking approximately 7 protocols and their fake chats I started to notice the same names were popping up with some flare in different chats - like this lucky community manager who managed to land positions at both #1 and #2 protocols (by TVL).
Well, kudos to him.
Ok, I think that's enough of the Telegram screenshots.
As you'll see, all of these things will turn up later: admins, bots, similar messages and links.
Around that point I decided that I needed to level up my observation and data collection approach - clicking, scrolling and looking is nice, but I wanted to see the bigger picture.
Data collection & analysis
My goal was simple: collect as much as possible from as many chats as possible, structure it in a queryable form, and analyse it.
Ok, how do we do this?
tg-crawler
I had some previous experience with Telegram Bot API, but I quickly figured out that it wasn't the best fit for my requirements.
I needed to automate user activity, therefore I needed user API.
Luckily, telegram has a great Python SDK implementation of their user API called Telethon - which essentially let me automate any action that you can perform as a user in a Telegram app (with some limitations and nuances).
So I drafted a high-level plan:
I needed to create a burner telegram account (for obvious reasons) + create a telegram application to get my api creds etc.
I would join chats manually to avoid false positives (joining legit / unofficial chats with no fraudulent activity) - this was definitely a huge bottleneck if I wanted to scale this whole thing, but at the time I needed to make sure that I would only collect 100% scam stuff.
The rest should be done by the Telethon crawler: I wanted to parse all messages and users sending them + all chat admins and metadata, save it all to some db and track changes like a chat changing its name, for example.
Then I locked in and vibecoded it all in ~6 hours.
The hardest things to handle correctly (as usual) were rate limiting and errors. Although I didn't expect much from vibe-code, I figured this service would be helpful for my future Telegram-based OSINT activities that I might (will) conduct.
And voila!
The
tg-crawler
is running on my Coolify (same as every other service I run lol), writing all of the data to a Postgres DB, from where I can boot up jupyter notebook and dig into the data.
Currently, my small instance of the crawler (more on the
big
one later) crawls through 81 chat and has already collected 222k messages from 6k users - just enough for some analysis as you'll see soon.
Going with Gephi
As I loaded all tables into pandas and studied the data for a little bit, I began to understand that my "standard" pandas / mathplotlib flow wouldn't work out as it had done in some of my previous attempts in data visualisation.
My goal was to find (and show) all sorts of connections that exist between the chats, their admins, users and so on - at that point I was not aware if they had all been created by a single team or individual scammers.
Naturally, I decided to try plotting it all as a big graph and then just looking at various parts and layers of it, trying to figure out the patterns and connections.
Those who know me are aware that I'm quite obsessed with graphs and network visualisations, though until now I rarely had such a good fit dataset to go all in on graphvis (one of my latest ones may be found
here
).
After some attempts to plot the data using PyVis (which I used previously) I quickly realised that, due to the graph size and complexity, I would need some help to work it out. I decided to settle on Gephi for the graph visualisation, but immediately got stuck in the complex and 2006ish interface of it.
So I reached out to
iggisv9t
- a very experienced network visualisation professional, whose Telegram channel I'd been subscribed to for quite some time, - and asked him for help with handling Gephi in the right way.
And so he did! Huge shoutout and thanks to him.
I think it's time we look into the graphs!
Scam network visualisation
Let's start with the overview graph.
Overview
This is a complete representation of all (important) connections between the chats, their admins and users:
admins are represented as small red nodes
users are small grey nodes
chats are the "empty" nodes of different size - depending on the amount of edges (connections) they have
you won't be able to see them clearly from this graph, but phishing urls are small white nodes.
The edges (connections) in this graph are messages sent by a user or admin to a chat, coloured by their age: the oldest ones are red, the medium-age ones are closer to yellow, and the most recent ones are blue.
While it looks absolutely crazy already, there is not much we can tell from it right now - it looks a bit chaotic. Let's break it down into layers and look at them individually.
Messages from old to new
First, let's focus on the connections and hide all nodes - it will help to see the dynamics in the graph more clearly:
Let's start from the "reddest" part on the right - that is the oldest chat present in my dataset, @etherfi_OfficialGroup:
As you can see, it's almost isolated from the rest of the graphs - the only edge going out of it's orbit is the @joinhide5_bot, which was later used by lots of chats that seemed completely unrelated to this one (we'll talk about bots later).
Judging from this small sample of the data (81 chats), this is where all of it started.
Right above it is the newest-looking chat - the first message visible in it right now is dated 14.06.2025:
This one's only got a couple red edges - those leading to the network centre are both bots, and the one right in the cloud of users is the first chat admin - @Sonny_NeverDMFirst.
As I mentioned, they're obsessed with the no dm thing - probably because it actually works on web3 newbies coming for help.
To me it seems ridiculous - who would have put that in their username lol.
This one doesn't really tell us much but is very beautiful:
See how it looks like a rainbow? This is actually a rare find in this group - this indicates that it's been consistently active over a long period of time.
Seems like EigenLayer has a very proactive and united community then...
You might've already noticed a bunch of red strings closer to the network centre - these are the admins and most old, active users.
Let's get rid of users that are unique to each chat and only focus on those who are connected (=sent message) to at least 2 chats:
Better?
Well, it's still very tangled, but it helps to see some things clearly.
The conglomerate of 3 chats in the bottom right corner - these are, respectively, @EthenaENOfficial, @EtherfiENOfficial and @UniswapREAL (lol), - share a lot of their active (=messaging) users, probably for economy reasons:
You can see similar groups surrounding 2-5 chats - this is a
clear indicator
of the same scammer teams running them.
Moving on - the next thing to look at are the clusters of blue edges in the middle.
They are mostly blue because scammers try to clear out all of the old links that were already reported / marked by wallets or browsers, or simply taken down by the hosting provider.
I didn't redact this one because it's already taken down hehe
This is one of the most popular phishing sites spread across different chats, by different users - which occurred 871 times in the ~200k messages!
All of the red dots with their red edges represent admin-chat relations - let's look into them further in a separate, isolated visualisation that I rearranged a little to untangle the barn of these connections.
Chats and their admins
This one looks even better than the previous one, ain't it?
In this visualisation, orange nodes represent the admins and white ones are the chats. Apart from the lonely chat in the bottom left corner, you can clearly see how connected the rest of them are - something that's impossible in the world of legit telegram communities.
I think it should be 100% clear at this point that this is a set of (or maybe a single) organised scam chat networks targeting users of the most popular DeFi protocols.
Let's study the graph structure a little closer - you will notice that there are clusters of chats that share some or all of the admins, and then there are a couple of "central" admins, joining the clusters into a giant net - as you'll soon find out, these are
bots
(not botted users, literal bots) that help the scammers cover the suspicious chat activity, as well as spread the phishing links in form of "official announcements"
Let's start with the "human" admins - some of them only groom a single chat, while others share their "community management" responsibilities, usually across 3-4 chats.
There's no proof that all of these admins are real people though - they might be different accounts of a single person used to create a feeling of a well-organised team behind the support chat.
We already discussed the three giant white chats in the middle - they're positioned differently in this particular graph, even closer to the network centre.
Apart from the most of the fake user base, they share the same admins - like this guy, for instance:
nice looking guy
Ok, it's time to move on to the...
Bots
The scammers rely on an almost identical set of bots in every chat:
some cloned version of JoinHideBot, used to hide join messages from the chat
either
GroupHelpBot,
with almost 1m MAU, used to manage the community. and make announcements (or its clones).
or Rose bot (and its clones) - either more popular community management tool often used by legit web3 community chats.
These chats account for much more admin-chat relationships than the human admins:
This and other @joinhide* bots are used by almost every chat in the dataset for a very simple reason: they help scammers hide thousands of "@username joined the group" messages that are caused by buying botted chat members in bulk.
By the way, here's the reason they all don't use a single bot is quite simple:
source:
https://tgdev.io/bot/joinhider
To illustrate the @GroupHelpBot usage better, let's zoom out to the whole graph once again:
As you can see, a lot of the edges are blue, indicating that the bot sent messages to most of these chats quite recently.
Here's an example of such message sent to a fake Uniswap support group (not the REAL one btw lol), providing users with the instructions to "fix any error" by connecting their wallet to some random website:
kinda hilarious message below
Ok, I think it's time to wrap up the data visualisation part - I hope it helped show how deeply tangled these different chats are.
Let's move on to the next section and look at the whole deception process.
Scam flow
Let's talk about the ways the scammers lure people into losing their money - promises, formats, and the actual websites.
A chat is born
How do these chats start?
I believe that in most cases they're some old chats that were bought, stolen or maybe created a long time ago, and since then went through lots of metamorphoses - switching from one fake protocol support group to another.
While most of the chat admins are smart enough to clear out the chat history before the current protocol had been chosen, I was lucky to find a couple where they didn't bother to do so:
it's probably older than 24.10.24 and was cleared out before transforming into Layer3 group
Next, it's getting re-filled with bots - scammers have to do it periodically because Telegram detects and removes botted accounts + some of them just stop working because they're no longer maintained by whoever registered or bought them.
Then the phishing spreading begins - very often sent from the chat itself to make it look more legitimate.
had to edit the link in this one because it's still fucking live. well, not for long :)
Then in just a few days the first fake user comes in with questions - usually stupid or nonsense ones, written in very poor English.
He obviously receives an expected answer and therefore reassures any legit person looking through the chat history that the answer satisfied their question.
Scammers have to rotate domains quite often because they do get reported and taken down sometimes. Especially if anyone was in fact scammed on it.
Here's a funny little notion I spotted in the same chat:
name every red flag in this text
Anyway, time goes by, and in around 10 months $FUEL / Layer3 support chat magically transforms into the Ethena Labs one (the actual group rename messages seem to be deleted - what a strange and picky way of doing things...).
This is now a "completely new" chat that follows the same exact cycle: new bots, new fake users asking the same questions, and new announcements leading to new (or sometimes even same) phishing urls.
How to share a phishy url?
We had already looked at some of the most blunt ways of sharing the link directly in the chat, either via GroupHelpBot, the chat user itself or any admin.
However, while looking through different clusters of chats I noticed that some had been acting a bit more cautions and subtle - inviting users to DM a chat admin (who would never DM first lol), or even ... DMing them first.
By doing so they would keep the chat clean of all of the phishy urls + avoid giving people fraudulent instructions, instead simulating "normal" community support.
I believe these different methods might indicate various teams operating their clusters of chats "as they feel it" - some more cautious, some  giving +-0 fucks.
it's sad to see the real people in this bottomless pit of bots
It didn't work out seamlessly every time, but who cares?
Only a very cautious and curious user would scroll through hundreds of messages sent to these chats daily to spot some alarms that the admins were too lazy to delete.
Anyway, chats like these would rely heavily on messages asking users to DM the admins for support - like this one:
see if you can spot the irony
So in order to see the actual websites these groups were sharing I messaged some of these admins to seek help. I tried to imitate poor english + stupid questions to seem like a noob who would seek help.
What was interesting in this case:
it took almost 4 hours for the supposed support admin to send the url to me - I guess he was busy with something
he used hyperlinks (probably hoping that I don't get spooked by the shady domain)
the first url died in just a few minutes (though it was reincarnated later), so I asked for another one
This one took even more time and didn't bother with the hyperlink:
I ain't got anything in the end
Another technique that some of the chats rely on is hiding the phishing url behind a set of redirects, like bit.ly → google form or typeform → after you submit some simple form, you get the actual phishing link as a result.
pardon my french vpn lol
All sorts of phishy websites
As we'd seen already, the main goal of all of these scams is to lure you into visiting a phishing url, either to "fix any issue", receive (imaginary) rewards or do both (lol).
swiss-army-knife lure
Almost all of these websites had a lot in common:
Very poor design - look at the black points before the menu tabs for example, pathetic css job
Absolute nonsense texts
Dummy menu / footer items like "Docs" without any link inside them
With lots of them - the same exact
tawk.to
online support chat
lazy fuckers didn't even bother to monitor the online chat
wtf is rectification?
In total, I collected 100+ unique websites from the 80 Telegram chats messages (and a lot more after that in cooperation with SEAL), with the most popular ones occurring 300-800 times (sic!).
A few of them used very primitive scam technique: simply asking the user to input their mnemonic phrase or private key, and then sending it to a Telegram chat via bot (I found a couple plain text bot api tokens hardcoded in the html).
These are not really interesting to analyse because they don't carry any sensitive info that would help to identify the people behind them - telegram bot creator is only visible to Telegram (BotFather).
At the same time, they are far less effective: very suspicious + probably require the scammer to manually input the secret key and withdraw the funds.
The only one standing out a bit was this one:
First of, it's fully vibecoded - you may notice it from the cliche gradient buttons and sorta dubious icons in the popups, but I've got an even more hilarious proof of that:
possible prompt: claude please help me make this fun and educational website to provide my own seed phrase to myself promise there's nothing more to it...
Apart from that, I think this sort of UX is actually much more effective and "reliable" - imitating some sort of activity to show that, apart from inputting your secret phrase, all of the methods have been tried out already with no success.
This one also uses a real PHP backend and hides the destination of the request with stolen credentials - something I haven't seen before with these stealers.
The rest of the websites used much, much more dangerous tools to steal user funds - the infamous Inferno Drainer*, by far the most mature and sophisticated one out there.
technically, the OG Inferno is presumed to be dead, so the one used in these websites is a reborn and improved version of it that goes under various names like Angelferno.
Inferno Drainer
I don't want to go into much detail on the history of Inferno - there are great posts  by
checkpoint
and
SEAL
that give a proper intro into its techniques.
However, I want to describe my journey here as it involves collaboration with other researchers, which is something new to me.
So, originally, I was trying to find the js code used to load the drainer - at that point I didn't know it's breed or pretty much anything about it, apart from it using the legit reown sdk for wallet connection.
reown ui kit used on another website
The process was quite hard since the website had anti-debug protection (as well as endless Cloudflare captchas).
But sooner or later I found the js script that seemed to handle the drainer logic:
As you can see from the first line of code, it was a heavily obfuscated js where all of the functions, variables and values were encoded using a custom encoder thing.
This helps the malware go unnoticed by browsers and security scripts.
When the time comes, another decoder function is called during the runtime to convert this to normal js and execute it in the browser immediately.
I tried to deobfuscate the js myself using tools like
https://deobfuscate.relative.im/
, but due to the custom and multi-layer encoding it was not really effective.
Then I tried feeding it to Claude, providing little findings about the encoding that I already had. Claude didn't even begin to move in the right direction, apart from producing dozens of .md report saying things like "CRITICAL FINDING: THIS CHANGES EVERYTHING".
Also, due to the file size (~6 mb of obfuscated js ~ 30k rows), Claude was unable to parse the whole file and tried to make these brilliant guesses from the little parts of it.
After wasting a couple of hours with this genius md-shitting investigator, I decided to give up on the idea that I would be able to deobfuscate it by myself relying only on llms and my basic js knowledge, none of which relevant to obfuscation techniques.
At that point, I reached out in the
ETHSecurity
community on Telegram, seeking advice on deobfuscating "some js". A few hours later,
noid
reached out to me and offered help.
Soon enough, he was able to extract some data from it, but still there were 80%+ of obfuscated js remaining. One thing that drawn our attention and (as we soon realised) thrown us off the scent was the 2 private keys found in the deobfuscated code.
one of the keys in the partly deobf code (notice that it's still almost unreadable)
At first we thought it was a big one: "how stupid of them to hardcode their wallet pk's in the code". Initially, since the wallets had no funds on them, I thought those addresses were used to proxy the stolen funds to other wallets, acting as an intermediary in the money laundering chain.
Imagine our surprise when we logged those wallets in, opened chat.blockscan.com and found a bunch of chats there, dating back to 2024.
However, after reviewing the messages (which led us to find an alleged original owner of this wallet) and transactions associated with this address, we figured that this was just a compromised victim wallet which was stolen more than a year ago - it had a lot of malicious authorisations and EIP-7702 delegations on it to things like "Advanced Crime Enjoyor".
But why were these wallets PKs present in the code?
My guess is that they're used as decoys - to make someone trying to get to the bottom of it follow the wrong track. We didn't find any connections to the actual drainer-like transactions on these two, leaving us with almost nothing.
Right around that moment of realisation Noid offered me to connect with
@blackbigswan
from SEAL and ask for their advice on the next step.
I sent him the original obfuscated code, and 10 minutes later he was back 100% sure that this was the Inferno Drainer. He figured it out due to the privateproxy.php mentioned somewhere along the lines - a known Inferno technique to dynamically receive c2 (command and control) server url from a smart contract to later retrieve the attacker wallet addresses and transfer the stolen funds. Described in detail
here
.
Where we are now
Since then we've been actively looking into this scheme, trying to find as many fake chats and phishing websites involved in it and report them using SEAL channels, which was quite successful.
The rest is a part of an ongoing operation, so I'll stop right here - it's already a very long story with tons of insights imo.
You can read the SEAL writeup about this operation
here
- it's focused more on the scale of the operation and the various deception techniques used by the scammers.
I'm also quite proud to announce that after some communication with @blackbigswan he offered me to join SEAL as a volunteer and I happily accepted it.
Throughout the last year I've been doing research and investigations completely on my own and honestly never met anyone in person who would be as passionate about this stuff as I am.
It's a wonderful feeling to finally join forces with other researchers who manically look into similar stuff every day, just out of curiosity and desire to make the web3 world a bit safer.
Apart from finding partners in (anti)crime, I was very happy to see much more experienced people do their magic, helping to bring my initial findings to the next level.
The work is far from over, but it's already at the stage where I would never get to by myself.
Once again, huge shoutout to @
blackbigswan
and
SEAL
, @
noid
,
iggisv9t
and others who helped me along the way.
Hope you enjoyed this story!
Stay tuned for the updates on this investigation, as well as new ones - I'm definitely not going to stop here.
If you have any questions or suggestions - leave a comment below or send me an email at
[email protected]
.
This next final section contains my opinions & advice for the members of the DeFi community.
If you're a founder / part of any DeFi (or, generally, any web3-related) project - please consider reading it!
As I'd shown above, this scam scheme affects almost every DeFi protocol out there.
It puts lots of web3 users to risk and damages protocol's and the entire space reputation, especially along the newbies who just started journey in web3 and got scammed in brutal fashion.
I assume you're someone who could push for the changes in the DeFi world, so I'll get straight into my opinionated suggestions:
Always list the links to ALL of your official channels
/ chats / profiles on all of your resources.
If you don't have an official Telegram community
, for example, -
MENTION it
right next to the icons / links leading to your official resources.
I understand that it should be obvious to people that anything not present on your website is a scam, but it's not.
When you're getting started with your protocol (or even when you're already big & cool), try to
take out (reserve) every username that could potentially be used by scammers.
I understand that it might be impossible to even find all of the possible usernames that could impersonate your official accounts, but come on - usernames like
<protocol_name> + Official or Support
should not be available to scammers!
If you don't want to manage the community on Telegram or somewhere else - just turn it into a channel and put a single placeholder message there, leading users to other platforms where you do offer support.
Finally, since we're already here -
anticipate
the various ways scammers could impersonate as your members / resources and react.
You're definitely capable of looking up your own protocol name + official in the Telegram search.
If you do find something that's clearly a scam - report it to SEAL via
911 bot
, report it to Telegram and ask your real community to report it as well - I am not very optimistic when it comes to chat takedown by Telegram mods, but I believe that hundreds or thousands of reports from the legitimate users will lead to some action by Telegram.
It's definitely better than doing nothing and letting these chats live on for years.
Imo it's also important to remember that while you might consider people falling for this "idiots" who don't belong to your sophisticated trustless decentralised protocol community, as the space grows and attracts newbies, there will always be victims of such scams.
They will later go to X / Reddit to tell their story and be shamed for their insufficient discretion, leaving them alone with funds lost.
If you don't believe these people exist - go to reddit and search for
<protocol name> + scam
- trust me, you'll probably find some poor guy's message from the last couple of days.
This can't have any positive effect on the reputation of both your protocol and the web3 space in general. It's already one of the main reasons why general public considers all crypto to be nothing more than a scam.
In case you want any help or suggestions on fighting the existing chats or other forms of scam made in the name of your protocol - reach out and I'll try to help or bring in others who will.
Stay safe!
