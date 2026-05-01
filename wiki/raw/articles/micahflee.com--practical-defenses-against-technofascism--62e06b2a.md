---
title: "Practical Defenses Against Technofascism"
url: "https://micahflee.com/practical-defenses-against-technofascism/"
fetched_at: 2026-05-01T07:02:06.538906+00:00
source: "micahflee.com"
tags: [blog, raw]
---

# Practical Defenses Against Technofascism

Source: https://micahflee.com/practical-defenses-against-technofascism/

I gave the Saturday morning keynote at BSidesPDX! I spoke honestly and frankly about the terrifying reality that Americans are facing under Trump's fascist regime, alongside practical advice for communities to defend themselves.
Watch my talk below. Of if you prefer reading articles over watching video, I've added a copy of my whole talk below the video, mildly edited, and with added links to my sources.
VIDEO
Sign up for micahflee
Hi, I'm Micah. I help journalists, researchers, and activists stay safe and productive.
No spam. Unsubscribe anytime.
Good morning, BSides Portland! I’ve worked in journalism for over a decade, but this is the first time I’ve traveled to an
active war zone
!
It’s hard to believe that we’re not even one year into Trump’s fascist takeover of the government. The onslaught of horrifying news is happening too fast to keep track of. But what’s clear to me is that the Trump administration, and ICE in particular, is tooling up for technological repression that Americans have
never
been subject to before.
Today I’ll go over the disturbing signs of the coming Age of Technofascism, along with practical ways to defend yourself and your communities against it.
I’m Micah Lee. I’m an independent security researcher, a journalist, and a software engineer. I spent the last decade and a half reporting on classified documents, helping journalists protect their sources, building open-source privacy tools, and teaching people how to analyze leaked datasets. These days, I work closely with journalists, researchers, and activists, doing what I can to keep them safe and productive.
The views I’m expressing in this talk are entirely my own, and not the views of any of the organizations that I work with.
Technofascism
Since Trump’s inauguration, the US has slid into
technofascism
.
Fascism is a slippery ideology that’s difficult to define. Sometimes it borrows from conservatives, or from liberals, or even from Leftists. But in the end, none of those beliefs are genuine. It’s all about accumulating
unlimited power
for an in-group, at the expense of
everyone else
.
💡
fascism
(noun)
Imperialism turned inward.
One common definition of fascism is “imperialism turned inward.”
Here's a bit of recent US imperialism history, since September 11, 2001:
We launched
wars of aggression
, based on lies, in Afghanistan and Iraq.
We ran a
covert torture program
, and
imprisoned and tortured innocent people for decades
at Guantanamo Bay.
We built a
global surveillance system
and spied on
entire populations
, all without probable cause.
We ran a massive
drone assassination program
, bombing wedding across the Middle East and Africa in countries we weren't at war with, in the name of American freedom.
Right now, we’re
funding and arming Israel while it commits genocide in Gaza
.
Huge swaths of the world are subjected to intense state repression, violence, surveillance, and censorship. In many places, this repression is explicitly supported by the US government and by US companies.
The thing that makes the Trump era different is
fascism
. Under Trump, this complete disregard for human rights is now pointed
inward
, at the “enemies within,” as Trump calls Americans he doesn’t like.
What we’ve been seeing on the streets of the US, with ICE kidnappings and military invasions of cities, is the normal American disregard for human rights, but this time turned inward,
targeted against us
.
💡
technofascism
(noun)
A form of fascism that uses modern technologies to attain its ends.
And the American tech industry is totally on board with it.
Elon Musk, the richest and
most divorced
person in the world, donated hundreds of millions of dollars to make sure Trump got elected. He then bought Twitter and turned it into X, a cesspool of propaganda, disinformation, and hate.
Mark Zuckerberg got a haircut, went on Joe Rogan, and shut down Meta’s
diversity
program.
Jeff Bezos, owner of Amazon and the Washington Post,
personally
intervened to prevent the Post from endorsing Kamala Harris, and he restructured its opinion page to make it
friendly to fascism
.
Tim Cook
personally donated one million dollars
to Trump’s inauguration committee.
You know how right now, while the government is shut down and food stamps for millions of Americans are set to expire one week from now, Trump is tearing down the East Wing of the White House to build himself a privately funded ballroom? Some of the companies who are funding Trump’s ballroom include: Amazon, Apple, Coinbase, Google, Meta, and Microsoft.
This talk
mostly
isn’t about reactionary tech billionaires and their complicit companies. Instead, it’s about attacks that we should be prepared for during this Age of Technofascism, and ways we can defend against them.
In this talk, I’m going to try to give some specific, actionable advise about three three topics: mercenary spyware, device searches, and app censorship.
But don’t think of this as a checklist that all you have to do is finish and then you’re good. Ultimately, what we all need to do, is build an intentional and forgiving
security culture
. These are things to talk over with your friends, colleagues, and family members as shared practices.
Fascists are targeting
everyone
outside their in-group. If we want to keep our communities safe, our defenses need to be
collective
, not individual.
I also want to warn you that this talk is pretty intense. So, just to lighten the mood a bit, I’m going to wear some frog eyes.
This is when I put on the frog eyes, though I accidentally called them "frog ears"
I’m not going to sugarcoat the awful reality of our current situation. But, at least I’ll be somewhat dressed up like a frog while I’m giving you all anxiety.
Mercenary Spyware
It used to be that government spy agencies, like the NSA, developed the most sophisticated hacking tools in the world in-house. But over the last decade or so, this has shifted to the private sector.
Now, private companies make the world’s most sophisticated hacking tools. And they sell them basically as
subscription services
to government agencies and police departments around the world, many of which would
never
have been able to build these capabilities in-house themselves.
Forbidden Stories:
About the Pegasus Project
Americans have been largely shielded from this type of attack.
NSO Group’s Pegasus spyware is typically configured to not be able to target US phone numbers (though, they could easily disable this setting if they decide to target US phone numbers).
Mercenary spyware firms are on US sanctions lists.
And in 2023, Biden published an executive order prohibiting mercenary spyware use by the US government without first  going through a review process.
Those days
are over
. Mercenary spyware is officially
welcome
in America.
Last year, during the Biden administration, ICE tried to sign a contract with Paragon Solutions, another sketchy Israeli firm that makes spyware called Graphite. But the Biden administration blocked this contract from going through.
But a few months ago, the “stop-work” order was dismissed, and
ICE’s contract with Paragon officially began
. According to
this reporting
by Jack Poulson, the US company REDLattice acquired Paragon Solutions. Now that Paragon is American-owned, ICE is allowed to use the Graphite spyware.
From Paragon Solution's website
Paragon bills Graphite as the “ethical alternative” to Pegasus. The difference between Graphite and Pegasus is that Pegasus takes over the entire phone. It does location tracking, listens through the microphone, steals all the data it can get, and so on. But Graphite is narrowly targeted at just spying on encrypted messaging apps like Signal, WhatsApp, and iMessage.
But
obviously
governments abuse it to violate human rights too.
Here’s a
recent report from The Citizen Lab
, published in June, where they caught Graphite being used against prominent journalists in Europe. In this case, Graphite relied on a zero-click vulnerability in iOS that exploited a bug in iMessage.
And here’s
an earlier Citizen Lab report
, published in March. In this one, they helped discover and fix a zero-click exploit for WhatsApp that targeted dozens of people in Italy, including journalists and the founder of the Italian organization that
rescues migrants
from the Mediterranean Sea.
404 Media has
launched a Freedom of Information Act lawsuit against ICE
, demanding documents related to its contract with Paragon. In this post, the journalists mention Paragon’s stance that it’s an “ethical alternative” in the spyware industry. It says, quote:
Selling to ICE, an agency that has flaunted due process, accountability, and transparency, may complicate that stance for Paragon. ICE has arrested people who were
following the steps necessary for legal immigration
; waited outside courtrooms to immediately detain people after
their immigration cases were dismissed
to rush them out of the country;
“de-documented” people who had valid work permits
in order to deport them; and continues to pick up people around the country while masking their faces and declining to provide their names.
CNN:
37 people arrested and American kids separated from parents after ICE raid at Chicago apartments
There’s nothing ethical about
anything
that ICE does. There’s
no way
that ICE will use Graphite in a way that
isn't
abusing human rights.
But, hey, at least the Trump administration isn’t using Pegasus, right?
Earlier this month,
news broke
that American investors appear to have purchased NSO Group. Right now, NSO Group is still on the US sanctions list. Biden’s executive order making it harder for the government to use mercenary spyware is still in effect. There’s a trail of dozens of US officials that were hacked with Pegasus, which normally wouldn’t be a good sign for NSO Group.
But in the Age of Technofascism, I really don’t see those old rules lasting much longer. I wouldn’t be surprised at all if we started to find Pegasus infections on the phones of immigrant defense activists. Or advocates for trans health care. Or even people just trying to get an abortion.
Also, just to add to the absurdity of this, the main investor is Robert Simonds, a Hollywood producer of B-movie films. If you haven’t heard of Robert Simonds before, perhaps you’ve heard of this 1996 Adam Sandler film…
Photo of Simonds by Alex Berliner,
CC BY-SA 3.0
Robert Simonds produced Happy Gilmore, along with a bunch of other Adam Sandler films. His entire experience is in the entertainment industry, not in tech or cybersecurity. He also has a bunch of business dealing with Chinese companies.
According to
the Israeli tech site Calcalist, for some reason he’s been on the board of NSO group’s parent company for a few years. And in 2023, he tried, and failed, to purchase NSO Group. It appears that he just tried again and was successful.
Also in this article, it mentions that in 2018, Sophie Watts, the president of his production company STX Entertainment, complained of harassment, and called him “obsessive.”
Quite likely,
this guy
is the new owner of the most notorious mercenary spyware firm in the world. And quite likely, he’s going to be selling Pegasus to fascist law enforcement agencies under Trump.
Reuters:
Inside the UAE’s secret hacking team of American mercenaries Ex-NSA operatives reveal how they helped spy on targets for the Arab monarchy — dissidents, rival leaders and journalists
But even if the current rules against Pegasus stick, there are plenty of American technofascists who don’t have any qualms with violating human rights.
Remember how I said that the most sophisticated hacking tools used to be developed in-house by agencies like the NSA? This was a big story back in 2019, when
Reuters exposed
that over a dozen former NSA operatives went to work for the United Arab Emirates
royal family
, helping them spy on dissidents, journalists, and activists.
It’s a
bad sign
that the US government is embracing mercenary spyware from sketchy Israeli firms. And that US companies are buying up those firms, presumably to make it easier to sell to the government.
But I honestly think there’s enough home-grown and talented American technofascists to support a domestic spyware industry anyway, even
without
the Israeli technology.
Last month, Bruce Schneier
blogged about
Digital Threat Modeling Under Authoritarianism. It’s worth a read. He wrote:
Imagine there is a government official assigned to your neighborhood, or your block, or your apartment building. It’s worth that person’s time to scrutinize everybody’s social media posts, email, and chat logs.
In it, he described the “shifting risks of decentralization,” which is something I hadn’t considered before.
Spyware is
targeted
surveillance, not
mass
surveillance, which means that it doesn’t scale easily. If all you had to worry about is staying off the radar of high-level fascists like JD Vance and Kash Patel, then most people probably don’t need to worry too much about it for themselves
But if repression is
decentralized
, with every state and city having its own
local fascists
in charge of picking targets they don’t like, then
everyone
needs to fear it. It’s too early to know how mercenary spyware will be abused by the Trump administration, but it’s prudent for
everyone
to get prepared
now
.
Defenses Against Mercenary Spyware
This is bad, but it’s not hopeless. There’s a
lot
that we can do to defend ourselves against mercenary spyware.
Zero-click exploits – which can hack your device without any interaction from you – can feel like magic, and like it’s hopeless to even try to defend against them. But it’s
not
magic.
Exploits are only possible because of
bugs
. And these bugs are routinely fixed in
software updates
. Zero-day exploits cost attackers millions of dollars to purchase, which means it’s
very expensive
to hack a fully updated phone or laptop. Exploits for bugs that are already patched, though, are
basically free
.
Never put off installing updates.
You should not only always install updates, but you should also get
everyone you know
to always install updates too.
Apple added
Lockdown Mode
to iOS in 2022. If you enable it, it prevents your phone from using certain features that are frequently exploited. Basically, it reduces your
attack surface
.
For example, it blocks fonts in Safari, which might make some websites look worse and the icons might be missing, but it cuts off an
entire attack vector
. I’ve been using Lockdown Mode in iOS since it came out and it’s actually quite usable.
In the Age of Technofascism, you should not only turn on Lockdown Mode, but get
everyone you know who uses an iPhone or a Mac
to do the same. To my knowledge, no researchers have found a successful infection of a device while Lockdown Mode was turned on.
You, and
everyone you know who uses an iPhone
, should also enable
Advanced Data Protection
in your iCloud account. Without it, iCloud is basically a government backdoor into your phone. If your phone gets backed up to iCloud, including your messages, photos, and all the data in all your apps, Apple can give this data to the police, the FBI, ICE, or whoever else asks.
If you use Advanced Data Protection, most of this data is encrypted with a key that only
you
control. The recovery key is a long sequence of random characters, so everyone who enables it either needs to keep this key written on a piece of paper, or store it in a password manager. If you’re helping people in your community enabled Advanced Data Protection for iCloud, it might be a good idea to also make sure they get set up with a password manager.
Earlier this year, Google launched
Android Advanced Protection
, which works in similar ways. If you use Android,
enable this
, and you’ll be far less vulnerable to mercenary spyware.
I don’t have much love for Apple. As I’ll talk about soon, they recently categorized ICE officers as a “targeted group” in order to comply with Trump’s censorship demands. But I
am
excited about
Memory Integrity Enforcement
, which is built into the hardware of the new iPhone 17.
Basically, if you’re using the new hardware, every time software allocates a block of memory, this memory is tagged with a secret. If the software ever tries accessing that memory again without the correct tag, the request is blocked, and the process is killed.
This should effectively
eliminate entire classes
of memory corruption bugs, including buffer overflows, use-after free, and out-of-bound bugs.
Apple:
Memory Integrity Enforcement: A complete vision for memory safety in Apple devices
This diagram shows an analysis of
real exploit chains
– these were the exploits included in actual mercenary spyware – and how each class of bug would perform against an iPhone with Memory Integrity Enforcement. It would prevent
all
of them from fully hacking the device.
So, if you can afford it, this is one of the few reasons I’d recommend considering buying a new iPhone. Of course, if you do get a new iPhone, you should
also
enable Lockdown Mode on it, and enabled iCloud Advanced Data Protection.
Device Searches
Mercenary spyware relies on exploits to hack your devices
remotely
. But there’s a whole different set of
local
attacks against devices too. Device searches have been a risk for as long as people have carried around computers with personal data. But in the Age of Technofascism, we should prepare for device searches
way
more frequently.
Cellebrite – another Israeli surveillance company – is the most notorious firm that does device searches. They make products that are currently already used by law enforcement across the US, but they’re aiming for a
much
bigger slice of the market. Last year, Cellebrite
announced
that it formed a US-based subsidiary specifically for selling to the federal government.
Cellebrite makes hardware and software used to break into locked phones and extract all the data from them. It works by exploiting vulnerabilities in lock screens, by brute forcing passcodes, including using exploits to bypass rate limits, and by rooting devices to get access to all the data in them.
Signal:
Exploiting vulnerabilities in Cellebrite UFED and Physical Analyzer from an app's perspective
This photo is from a 2021 post on the Signal blog by Moxie Marlinspike. He said, “By a truly unbelievable coincidence, I was recently out for a walk when I saw a small package fall off a truck ahead of me.” It turns out, it was Cellebrite equipment. Specifically, just the software used to extract data from phones, and a bunch of cables, but not the actual hardware that hacks into phones.
Moxie also wrote about some security vulnerabilities he discovered in it. He discovered that, “it’s possible to execute arbitrary code on a Cellebrite machine simply by including a specially formatted but otherwise innocuous file in any app on a device that is subsequently plugged into Cellebrite and scanned.”
Like other Israeli surveillance firms, Cellebrite has a history of being abused to violate human rights:
In 2020, police in the African country Botswana used Cellebrite to break into the phones of detained journalists,
according to
Committee to Protect Journalists.
In 2021 during the protests in Hong Kong, Chinese police used Cellebrite to hack the phones of pro-democracy protesters,
according to
reporting in The Intercept.
In 2022, Russia used Cellebrite to hack the phones of anti-Putin opposition activists,
according to
reporting in Haaretz.
Last month, ICE entered
a new $11 million contract
with Cellebrite. But ICE already has a long history of working with them. In 2017, they first spent $2.2 million on a Cellebrite contract, immediately after Trump’s travel ban. In 2019, they spent somewhere between $30 and $35 million on another contract. And now, they’re starting a
new
$11 million contract.
It’s fair to assume that ICE is using Cellebrite to hack the phones, and steal all the data, from
every single person
they arrest, regardless of immigration status.
When your device is searched, authorities
stealing your data
is only one of the risks that you face. Another is that they might
install spyware
, and hope that you keep using it. Here’s
an article
from last year about a pro-Ukraine activist in Russia named Kirill Parubets.
Armed FSB agents violently raided his house. From the article:
On April 18, 2024, six FSB agents armed with machine guns burst into Parubets and his wife’s apartment in Moscow at around 6:30 in the morning. “They threw us to the floor, they dragged my wife into a small room, I was lying in the hallway. They didn’t let us get dressed,” according to his recollection of the events, which Parubets wrote in a document he shared with TechCrunch.
One of them picked up his Android phone and said, “What’s your fucking password?” And Parubets told them. From the article:
“What’s your f—king password?” one of the agents asked Parubets when they picked up his Android phone, according to his recollection of the events. Intimidated, Parubets said he gave away its password.
They threatened to keep him in prison unless he agreed to spy on Ukrainians for the Russians, so he agreed, even though he says he didn’t plan on actually doing it. When they released him, they gave him back his phone and it had spyware on it.
According to
an analysis of Parubets’s Android phone
by The Citizen Lab and the legal assistance group First Department, the spyware they found “allows the operator to track a target device’s location, record phone calls, keystrokes, and read messages from encrypted messaging apps, among other capabilities.”
And the report also point out:
Any person whose device was confiscated and later returned by [a security service] should assume that the device can no longer be trusted without detailed, expert analysis.
In the Age of Technofascism, this applies when your device is seized by DHS, ICE, CPB, the FBI, and in many situations probably local police too.
Sometimes it’s legal for authorities to search your device, and sometimes it’s illegal. But all of that is pretty abstract when it’s clear that the Trump administration doesn’t care about breaking the law, and gets away with it all the time.
Whenever you cross a border or go to a protest, you should be prepared for the fact that authorities
might
try to search your devices.
It’s still important to
know your rights
, even if fascist authorities are likely to violate them. You should consult actual lawyers for legal advice, but here are just some quick tips:
You have the right to remain silent, so
don't talk to the police
except to assert your rights.
Police are kind of like vampires, they can only legally enter your home if you invite them in. So if police or federal agents show up at your house or your business,
do not invite them in
. If they say they have a warrant, it needs to be a valid warrant, signed by a real judge. ICE tries to use their own fake warrants, and those aren’t legally binding.
If they try to search you, tell them you
do not consent
.
If they want you to unlock your phone or computer,
don't comply
, and
don't share your passwords
. There’s a good chance that this will result in them stealing your devices, but at least they’ll be encrypted.
Before I go into the defenses against device searches, I want to take a minute to plug the
Access Now Digital Security Helpline
.
Researchers at places like The Citizen Lab, Access Now, and Amnesty International have done an
amazing
job exposing spyware firms and their flagrant abuse of human rights. Detecting spyware is hard, and none of this research is possible without the cooperation of the victims of spyware.
If you think your device has been hacked by the Trump administration, or
if there is anyone in your community who might have been hacked
, please reach out to the Access Now Helpline for help. If anyone you know has had their phone seized by federal agents, and then later given back to them, they should
definitely not trust that phone
, and contact the Access Now Helpline.
Defenses Against Device Searches
While I can’t give you legal advice, I
can
give you technical advice on defenses against device searches. These mostly all revolve around disk encryption.
If someone gains access to your phone or computer and you aren’t using disk encryption,
nothing
stops them from accessing all your data. But even with disk encryption, your data is only as secure as how you’re able to unlock your device, as well as your lock screen settings.
For example, let’s say you have an iPhone and a strong passcode, but you unlock your phone with your face. This means that when you get arrested at a protest, the cop can
also
unlock your phone with your face, and then access all the data in your phone.
Because of tools like Cellebrite, your phone’s passcode is also really important. It’s orders of magnitude harder to hack into a phone with 10-digit passcode than with a 6-digit passcode.
You should also harden your devices. If these defenses against device searches look familiar, it’s because they’re
also
defenses again mercenary spyware.
Cellebrite, and similar tools that attack computers, rely on vulnerabilities to help them bypass your lock screen or brute force your password without rate limiting. Install updates. When you’re using the latest version of your OS, there are fewer vulnerabilities in your lock screen that can be exploited.
And again, enable Lockdown Mode in iOS and macOS. And enable Advanced Protection in Android.
When your device is seized, but in a locked state, you also should be careful about what information is on your lock screen. They can access that data without even needing to hack your device. Make sure that sensitive notifications – like the content of your Signal messages – don’t get displayed on your lock screen. This applies to both computers and phones.
The Windows 95 shut down screen
If you have disk encryption, the very best thing you can do to keep your device secure is to
completely power off your device
when you’re not using it. A powered off device, before you’ve entered any password to unlock the encryption, is much harder to hack into than one that’s powered on but locked.
So, when you’re going through a security checkpoint at the airport, completely power of your phone and your computer
first
.
When you’re at a protest, if it looks like you might get arrested imminently, power off your phone before you get detained. You can always power it back on when you’re safe.
And finally, turn off all of your computers
every night
when you’re not using them. Police most often raid people’s homes in the middle of the night or the very early morning. Powering off your computers every night means that if you get raided, your devices will be harder to hack into, giving your disk encryption a fighting chance.
People often talk about anonymous burner phones. Except in very specific situations, truly anonymous burner phones aren’t that useful. Using a
secondary phone
that you don’t even try to keep anonymous, on the other hand, is easy to maintain, and it has some major benefits. If you get detained at an airport, or you get arrested at a protest, the authorities either already know who you are, or they’re about to, so anonymity isn’t important here.
When you set up a secondary device, use a separate Google or Apple account, so it can't access the data in your main account. Make a separate Signal account, and just add the contacts and groups you'll need. If authorities hack into your secondary device, there won’t be much data to extract. It won’t have your messaging apps, your contacts, your browser history, your photos, your documents, or anything else like that.
Since secondary devices are just for temporary use – to take on an international trip, or to bring to a protest – you should factory reset them between uses. This should protect you in case they install spyware on your device and give it back to you. Although, ideally you should contact the Access Now Helpline to let researchers to get a sample of that spyware first.
Even on your main devices,
minimize
the data that you retain.
They can't steal your data if you don't have anything to steal.
We’ll all be better off if we start treating most online communication as ephemeral and delete it after we’ve read it. If you want to retain anything, take a screenshot, but delete everything else.
If you go into the Signal app, you can go to Settings, Privacy, Disappearing Messages, and set Signal to use disappearing messages by default for every chat. And while you’re at it, get everyone you know to stop sending you messages in iMessage, WhatsApp, Instagram DMs, or anything else, and switch to Signal.
You should minimize other data too, not just in messaging apps. Basically, think about what data you have on your phones and computers, and regularly take steps to reduce your risk if those devices are ever searched.
Cell-Site Simulators
This isn’t about mercenary spyware or device searches, but I wanted to slip this into my talk too. We’ve known for years that ICE, and local police departments across the US, use
cell-site simulaors
. Here’s
recent reporting
from earlier this month about yet another ICE contract for these street level surveillance devices.
If you’re not familiar with cell-site simulators, which are also called IMSI catchers or Stingrays, they’re devices that pretend to be legitimate cell phone towers, tricking all nearby phones into connecting directly to them rather than real towers. We know that these are in use across the US, but there’s a real challenging in detecting them.
Rayhunter
is open-source custom firmware for cheap mobile hotspots that can detect cell-site simulators. It’s developed by Cooper Quintin and others at EFF. You need to plug in a SIM card, but you don't need to pay for phone service, so it’s a cheap one-time cost. It’s incredibly easy to flash the Rayhunter firmware onto these. If you’re interested in trying to detect cell-site simulators, check out the Rayhunter project.
There's NOT an App for That
A different way that technofascism is expressing itself is app censorship. Apple and Google, the companies that control exactly what software anyone is allowed to install on their phones, are actively collaborating with the Trump administration by censoring their App Stores without even a fight.
A few weeks ago, at the request of the Trump administration, Apple
kicked
the ICEBlock app out of the App Store. This was an iPhone app that allowed users to anonymously report ICE sightings within a 5 mile radius and get notifications when others reported ICE sightings near them.
The developer, Joshua Aaron, points out that:
ICEBlock is no different from crowd sourcing speed traps, which every notable mapping application, including Apple's own Maps app, implements as part of its core services.
To justify its decision, Apple has decided to treat ICE officers as a “targeted group,” and to treat apps that help inform the public about abuses by ICE agents – whose job is
racial profiling
and
violence against people based on their national and ethnic origin
– as the same as
discriminating
against people for their religion, race, sexual orientation, gender, or national or ethnic origin.
To be clear, the government didn’t send a court order to Apple demanding that they do this. The Justice Department asked Apple, and Apple simply agreed without a fight.
Here’s a quick video of Attorney General Pam Bondi
lying to the Senate
about ICEBlock:
October 7, 2025: Attorney General Pam Bondi lies to the Senate Judiciary Committee about ICEBlock (
YouTube link
)
First, ICEBlock did
not
post “where ICE officers live.” They just posted ICE
sightings
, which then automatically got deleted after a few hours. Also, ICEBlock was never available for Android.
But don’t worry,
Google
also
voluntarily
chose to collaborate
with the fascists
at the request of the Trump administration. And in fact, they used pretty much the same justification. Both Apple and Google removed the
Red Dot app
from their app stores.
Red Dot is an app that’s similar to ICEBlock, in that it lets people report ICE sightings and get alerts when they’re nearby. Since it’s been banned by both Apple and Google, it’s now
only
available for Android as an APK that you can sideload.
Google
claims
that the Justice Department didn’t ask them to ban Red Dot, but I find that kind of hard to believe considering Pam Bondi keeps giving interviews saying that she asked Google to ban these apps.
But even more disturbingly, Google’s justification for banning Red Dot is that working at ICE makes you part of a vulnerable group that is “associated with systemic discrimination or marginalization.”
This is just offensive.
And even worse, Apple
banned an app called Eyes Up
from the App Store. Unlike ICEBlock and Red Dot, Eyes Up doesn’t do any real-time tracking or alerting of ICE sightings. It simply archives verified videos of ICE abuse, and puts them on a map to
preserve evidence of their crimes
.
Also unlike ICEBlock or Red Dot, Eyes Up is a
web application
. So it’s still online and active at
eyesupapp.com
. Here’s a screenshot of Eyes Up, zoomed into part of Portland.
Apple is
voluntarily helping the fascists censor videos of violence
from DHS officers like this one:
See the original video at
Eyes Up
.
It’s not just Apple and Google though. Last week, Facebook
deleted a group
called “ICE Sighting-Chicagoland” with
over 80,000 members in it
, at the request of Attorney General Pam Bondi. Just like Apple and Google’s excuses, Meta claimed that this Facebook group was violating policies “against coordinated harm.”
On a
recent episode
of the podcast On the Media, the 404 Media reporter Joseph Cox spoke about this Facebook group:
I have seen a limited archive of that Facebook page. It’s difficult to access now, of course, because it has been taken offline. But the section that I scrolled through, I did not see any evidence of ICE officials being doxed, or specifically targeted. It was more just reporting, ‘Hey, there are ICE officials at this location,’ very much in the same sort of way that apps like ICEBlock were doing.
Here's a recording from the podcast:
Excerpt from On the Media episode: Big Tech is Silencing the ICE Watchers. Plus, Why a Scholar of Antifa Fled the Country.
So in other words, in the Age of Technofascism, American tech companies are collaborators.
Before going to solutions, I want to share one final story from earlier this week.
This article
describes a search warrant that ICE sent to Meta, demanding real-time metadata about who a WhatsApp user was communicating with.
WhatsApp messages are end-to-end encrypted, but Meta freely gives law enforcement all of the metadata. If you’re using WhatsApp for any sort of antifascist activism,
stop and switch to Signal
. Signal has features like Sealed Sender that prevent them from even accessing the metadata themselves, and so they can’t be forced to hand it over to ICE.
From the article:
The warrant reviewed by
Forbes
, filed towards the end of last week, now allows the government to force unlock that suspect’s phone by applying the defendant’s fingerprints to the device, or holding up the phone to their face, depending on what, if any, biometric access features they’re using.
This warrant also specifically allows the government to unlock the suspects phone using their biometrics. So again,
don't use biometrics
for unlocking your phone or your computer.
The Open Web is Our Best Hope
Of these four instances of censorship, ICEBlock, Red Dot, Eyes Up, and the “ICE Sighting-Chicagoland” Facebook group, Eyes Up is the only one that’s still online. And the reason is because it’s a
website
.
What this censorship tells me is that companies like Apple, Google, and Meta cannot be trusted or relied on.
If you want to make an app that the Trump administration won’t like, unfortunately, you should make it with censorship in mind. Just like Eyes Up, make it a website that works without a native app, so when Apple and Google turn on your, your tool can still be useful.
The internet is a global network. There are domain name registrars and hosting providers all over the world, including many that won’t cooperate with the US government.
There isn’t much internet censorship in the US, yet. But if that changes, thanks to activists in places like China, Iran, and Russia, we have decades of experience circumventing online censorship. We can use the same techniques here if we need to.
Finally, we should all step back from our computers, put down our phones, and devote real energy into strengthening our communities.
Things are
really bad
right now, and it’s easy to feel isolated and alone. Whenever possible, talk with people
in person
instead of in group chats or video calls.
People are facing harassment from Trump-supporting fascists. Their loved ones are getting disappeared by the secret police. The state is making example out of people for trying to get gender affirming or reproductive health care, or for protesting genocide.
When they come after you, your friends, or your neighbors, the
worst
thing you can do is to keep staring at your phone. We need real community ties with people who have our backs. And we need to have solidarity with
everyone else
they’re going after.
People living under repressive regimes have learned throughout history is the importance of
security culture
. A security culture is a set of customs and measures shared by a community to keep everyone safe.
As shit gets more real, keeping your community safe is everyone's responsibility.
Don’t panic if you haven’t done all of the things I proposed in this talk. Don’t judge others who haven’t done them either. It takes time to incorporate these practices into our communities as a security culture, but we’ll all be better off if we commit to it.
The fascists are probably going to start hacking our phones.
They’re going to plug them into Cellebrite to try to see see exactly who we’re talking to and what we’re saying.
They might try to plant spyware on them and hope we keep using them.
They’re going to pressure tech platforms to prevent us from organizing – they already are.
And they’re going to use data from companies like Google and Meta to decide which of us to target.
It’s not enough to just lock down your own devices.
If we want to stay safe and productive in the Age of Technofascism, we all need to work together.
If you found this interesting,
subscribe
to get these posts emailed directly to your inbox. If you want to support my work, considering becoming a paid supporter.
