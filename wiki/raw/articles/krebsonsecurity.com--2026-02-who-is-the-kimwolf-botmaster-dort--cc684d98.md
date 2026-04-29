---
title: "Who is the Kimwolf Botmaster “Dort”?"
url: "https://krebsonsecurity.com/2026/02/who-is-the-kimwolf-botmaster-dort/"
fetched_at: 2026-04-29T07:02:06.362466+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# Who is the Kimwolf Botmaster “Dort”?

Source: https://krebsonsecurity.com/2026/02/who-is-the-kimwolf-botmaster-dort/

In early January 2026, KrebsOnSecurity revealed how a security researcher disclosed a vulnerability that was used to build
Kimwolf
, the world’s largest and most disruptive botnet. Since then, the person in control of Kimwolf — who goes by the handle “
Dort
” — has coordinated a barrage of distributed denial-of-service (DDoS), doxing and email flooding attacks against the researcher and this author, and more recently caused a SWAT team to be sent to the researcher’s home. This post examines what is knowable about Dort based on public information.
A public “dox” created in 2020 asserted Dort was a teenager from Canada (DOB August 2003) who used the aliases “
CPacket
” and “
M1ce
.” A search on the username CPacket at the open source intelligence platform
OSINT Industries
finds a
GitHub
account under the names Dort and CPacket that was created in 2017 using the email address
jay.miner232@gmail.com
.
Image: osint.industries.
The cyber intelligence firm
Intel 471
says jay.miner232@gmail.com was used between 2015 and 2019 to create accounts at multiple cybercrime forums, including
Nulled
(username “Uubuntuu”) and
Cracked
(user “Dorted”); Intel 471 reports that both of these accounts were created from the same Internet address at Rogers Canada (99.241.112.24).
Dort was an extremely active player in the Microsoft game
Minecraft
who gained notoriety for their “
Dortware
” software that helped players cheat. But somewhere along the way, Dort graduated from hacking Minecraft games to enabling far more serious crimes.
Dort also used the nickname
DortDev
, an identity that was active in March 2022 on the chat server for the prolific cybercrime group known as
LAPSUS$
. Dort peddled a service for registering temporary email addresses, as well as “
Dortsolver
,” code that could bypass various CAPTCHA services designed to prevent automated account abuse. Both of these offerings were advertised in 2022 on
SIM Land
, a Telegram channel dedicated to
SIM-swapping
and account takeover activity.
The cyber intelligence firm
Flashpoint
indexed 2022 posts on SIM Land by Dort that show this person developed the disposable email and CAPTCHA bypass services with the help of another hacker who went by the handle “
Qoft
.”
“I legit just work with Jacob,” Qoft said in 2022 in reply to another user, referring to their exclusive business partner Dort. In the same conversation, Qoft bragged that the two had stolen more than $250,000 worth of
Microsoft Xbox Game Pass accounts
by developing a program that mass-created Game Pass identities using stolen payment card data.
Who is the Jacob that Qoft referred to as their business partner? The breach tracking service
Constella Intelligence
finds the password used by jay.miner232@gmail.com was reused by just one other email address:
jacobbutler803@gmail.com
. Recall that the 2020 dox of Dort said their date of birth was August 2003 (8/03).
Searching this email address at
DomainTools.com
reveals it was used in 2015 to register several Minecraft-themed domains, all assigned to a Jacob Butler in Ottawa, Canada and to the Ottawa phone number 613-909-9727.
Constella Intelligence finds jacobbutler803@gmail.com was used to register an account on the hacker forum Nulled in 2016, as well as the account name “M1CE” on Minecraft. Pivoting off the password used by their Nulled account shows it was shared by the email addresses
j.a.y.m.iner232@gmail.com
and
jbutl3@ocdsb.ca
, the latter being an address at a domain for the
Ottawa-Carelton District School Board
.
Data indexed by the breach tracking service
Spycloud
suggests that at one point Jacob Butler shared a computer with his mother and a sibling, which might explain why their email accounts were connected to the password “jacobsplugs.” Neither Jacob nor any of the other Butler household members responded to requests for comment.
The open source intelligence service
Epieos
finds jacobbutler803@gmail.com created the GitHub account “
MemeClient
.” Meanwhile, Flashpoint indexed a deleted anonymous Pastebin.com post from 2017 declaring that MemeClient was the creation of a user named CPacket — one of Dort’s early monikers.
Why is Dort so mad? On January 2, KrebsOnSecurity published
The Kimwolf Botnet is Stalking Your Local Network
, which explored research into the botnet by
Benjamin Brundage
, founder of the proxy tracking service
Synthient
. Brundage figured out that the Kimwolf botmasters were exploiting a little-known weakness in residential proxy services to infect poorly-defended devices — like TV boxes and digital photo frames — plugged into the internal, private networks of proxy endpoints.
By the time that story went live, most of the vulnerable proxy providers had been notified by Brundage and had fixed the weaknesses in their systems. That vulnerability remediation process massively slowed Kimwolf’s ability to spread, and within hours of the story’s publication Dort created a Discord server in my name that began publishing personal information about and violent threats against Brundage, Yours Truly, and others.
Dort and friends incriminating themselves by planning swatting attacks in a public Discord server.
Last week, Dort and friends used that same Discord server (then named “Krebs’s Koinbase Kallers”) to threaten a swatting attack against Brundage, again posting his home address and personal information. Brundage told KrebsOnSecurity that local police officers subsequently visited his home in response to a swatting hoax which occurred around the same time that another member of the server posted a door emoji and taunted Brundage further.
Dort, using the alias “Meow,” taunts Synthient founder Ben Brundage with a picture of a door.
Someone on the server then linked to a cringeworthy (and NSFW) new Soundcloud
diss track
recorded by the user DortDev that included a stickied message from Dort saying, “Ur dead nigga. u better watch ur fucking back. sleep with one eye open. bitch.”
“It’s a pretty hefty penny for a new front door,” the diss track intoned. “If his head doesn’t get blown off by SWAT officers. What’s it like not having a front door?”
With any luck, Dort will soon be able to tell us all exactly what it’s like.
Update, 10:29 a.m.:
Jacob Butler responded to requests for comment, speaking with KrebsOnSecurity briefly via telephone. Butler said he didn’t notice earlier requests for comment because he hasn’t really been online since 2021, after his home was swatted multiple times. He acknowledged making and distributing a Minecraft cheat long ago, but said he hasn’t played the game in years and was not involved in Dortsolver or any other activity attributed to the Dort nickname after 2021.
“It was a really old cheat and I don’t remember the name of it,” Butler said of his Minecraft modification. “I’m very stressed, man. I don’t know if people are going to swat me again or what. After that, I pretty much walked away from everything, logged off and said fuck that. I don’t go online anymore. I don’t know why people would still be going after me, to be completely honest.”
When asked what he does for a living, Butler said he mostly stays home and helps his mom around the house because he struggles with autism and social interaction. He maintains that someone must have compromised one or more of his old accounts and is impersonating him online as Dort.
“Someone is actually probably impersonating me, and now I’m really worried,” Butler said. “This is making me relive everything.”
But there are issues with Butler’s timeline. For example, Jacob’s voice in our phone conversation was remarkably similar to the Jacob/Dort whose voice can be heard in
this Sept. 2022 Clash of Code competition
between Dort and another coder (Dort lost). At around 6 minutes and 10 seconds into the recording, Dort launches into a cursing tirade that mirrors the stream of profanity in the diss rap that Dortdev posted threatening Brundage. Dort can be heard again at around 16 minutes; at around 26:00, Dort threatens to swat his opponent.
Butler said the voice of Dort is not his, exactly, but rather that of an impersonator who had likely cloned his voice.
“I would like to clarify that was absolutely not me,” Butler said. “There must be someone using a voice changer. Or something of the sorts. Because people were cloning my voice before and sending audio clips of ‘me’ saying outrageous stuff.”
Further reading:
Jan. 8, 2026: Who Benefited from the Aisuru and Kimwolf Botnets?
Jan. 20, 2026: Kimwolf Botnet Lurking in Corporate, Govt. Networks
Jan. 26, 2026: Who Operates the Badbox 2.0 Botnet?
Feb. 11, 2026: Kimwolf Botnet Swamps Anonymity Network I2P
Mar. 19, 2026: Feds Disrupt IoT Botnets Behind Huge DDoS Attacks
