# SOURCE: https://eva.ac/blog/llms/
# Fetched: 2026-11-02

in recent times i've been asked a lot the question of "what ai model did you find to use this?", practically for all of the articles on this blog. the answer has always been my brain, i have never used ai for any kind of research i published, ever.

the next question is often why, followed up with "you would be so unstoppable with claude mythos" this article should explain why i don't like using ai for my research, and my general opinions on llms in both development and cybersecurity

why i don't use ai
it's as simple as i do this for fun, and i don't find giving an ai all the fun at poking at something instead of doing it myself fun. put it another way, i like using my brain

i like coding, i like staring at devtools, binary ninja, or whatever else for hours, i like exploring weird library source code and tracing it with nothing but github code search and a dream, it is fun to me. i don't do anything on this blog for money, i do it for fun, the money part is just a nice side effect

but why don't you just offload the tedious bits to ai?
a lot of the tedious bits are still fun, there's some that aren't, but i also cannot take credit for something an llm did for me, and i am wildly uncomfortable with publishing something an llm did for me on my personal blog as a writeup

this blog is mine, all the work on it is mine, or is shared research with other people that are explicitly credited. i cannot take credit for something an llm did for me, and i also cannot credit an llm properly, as they aren't a person

using an llm makes me lose my mind
i truly have tried to use llms before, just to try it out. nothing i was going to publish as research, but i really couldn't and it left me never wanting to use an llm again

i don't know how more people don't experience this, but staring at an llms output be confidently wrong eventually to get there in the process, or looking at the commands its running and see some really stupid things its doing drives me crazy to the point i will just stop it before it answers, i cannot handle something being that confidently wrong (even though it'll probably still get there in the end)

i'm not denying these models are powerful
llms are quite powerful machines, we've seen that as of recent, that's for sure, they are still wildly marketed as being more powerful then they are, but i cannot argue that they are infact not powerful, because they are

llms still need guidance
if you threw an llm at the linux kernel and told it to find an rce without any other guidance, it probably couldn't. you still need skill and experience to guide an llm at the current state

all of these vulnerabilities that we've been panicking over have been found by skilled researchers using llms, likely at a big firm to give them all the tokens they want. because llms still need guidance and not anyone can just do this, no matter what openai or anthropic try to tell you

marketing and php2shell
ai companies have hooked onto cybersecurity as their marketing strategy and it shows, a good example is php2shell. where three companies:

calif (research firm)
openai (you know who openai is)
wiz (research firm)

all collaborated on it and released their own blogposts, all seemingly with different narratives

calif went with the narrative of an ai found these php vulns with the help of a human guiding it, while openai went with the agent uncovered critical vulnerabilties, and wiz went with a middle point, still pretty openai-like

"patch the world"
openai talked a lot about how they were helping maintainers patch these issues, and mitigate them faster and for more people. which i'm sure they did to an extent, but i don't think they did all they could

they could easily backport these security fixes to older versions of php with the help of ai if they wanted to, it's not like they don't have the compute, they do, they have a lot of it, they're openai

dropping poc videos before patch
this has been a common trend in the recent days of ai-based cybersecurity where researchers and otherwise companies, drop poc videos of unpatched 0days on twitter, for some reason

this is so clearly marketing, and it does nothing but make everything worse in terms of security. these poc videos contain quite a lot of useful information, no matter how much you hide (which, a lot of them don't hide much) and just do nothing but fearmonger

hashes are also apart of this, hashes have always been a way to claim proof over a vulnerability or generally acomplishment before it becomes public, not as a way of fearmongering. you shouldn't include the name of the product next to a hash, that is just not what a hash exists for.

but a lot of companies and generally people now drop them like candy, and it causes panic for no reason. at least with a poc video you know what the vuln is, with just a hash and a product name you don't even know that, you just know some vuln exists

tailworm
this was a less big story, but still pretty big. on bluesky, a "security researcher" claimed to have found a 0day in tailscale. they did this by dropping a hash with the caption of "tailscale privilege escalation"

obviously, this got people very very worried. what could tailscale privilege escalation mean? could someone bypass all ACL rules, what can happen?

don't worry! cause we slowly get information of the vulnerability fed to us over a bluesky thread

so, what was the point of that? you posted barely any information, posted more but cryptic information an hour after, and then an hour after you just gave away where the vulnerability is?

i assumed that there was some responsible disclosure happening here, and that's why the hash got tweeted, etc.

would you believe me that this wasn't even responsibly disclosed?

next day, the (single-person) company this person owns drops this website on bluesky:

a full website, obviously vibe-coded, with all of their findings, a lot of which completely do not matter or just aren't critical. while the "privilege escalation" was real, it required you to already have acl rules to a machine, and have it's tailscale ssh enabled

the vulnerability was just the fact that you could privilege escalate on that machine specifically to root. that's it. that's what was fearmongered about so much, and then they dropped it publicly next day, without even contacting tailscale to let them patch it

it was given a fancy name, a catchphrase, even. but no one thought to responsibly disclose it, instead posting it on a social media platform

the reason this happened was pretty clear: it was to advertise the company, not to help make the world better. it was to make everyone think about the company who exposed critical issues in tailscale, and maybe ask them for an audit

it's not all ai finding these vulnerabilities
the biggest of them all, in my opinion, was eMudhra. you know, the company who had their CA private key as the number Four. this wasn't found by an ai, but just a human using a old ass library made by google called paranoid_crypto to scan through keys for fun out of curiosity

that's whats beautiful about it in my opinion, the biggest thing of them all was missed by all these ais but rather was just by a human just doing random shit

conclusion
i think that people have been way too lost in this wave of ai everything, that they are disregarding doing things themselves by a whole lot. it is still extremely fun to just, write code yourself, debug things yourself, stare at minified js bundles for hours at a end, cycle through random interesting looking subdomains, it's all fun! and i feel people have forgotten that a bit

while an ai "can just do things", it is fun to do them yourself. i totally get using ai for work, as we live in a world where software engineers are expected to move faster then ever, and in my opinion, that isn't a good precedent, but it's what we have to live with

personal projects are the place where you get to have fun, do something you enjoy. and i think giving those to an ai even just ruins your enjoyment of creating things

for me, at least, the process of getting somewhere is more interesting then the end product. cause i enjoy learning along the way and i enjoy banging my head against the wall on a primitive that goes nowhere

i mess with a lot of things, and i find a lot of things. but almost none of them go on this blog, simply because i have a feeling i need to one-up myself with every new blogpost, and i keep challenging myself to find something even funnier and also more critical at the same time. it makes me learn a lot more then i already knew

writing code itself is fun, and an ai writing it for you even if you gave it a plan on how to write it, you are missing out on so many learning opportunities by not writing it yourself, because there's no such thing as a perfect infrastructure plan, things change as you go, while you are in the flow of writing code

go reverse engineer that old iot device, mitm that weird looking chinese automatic pet feeder that requires an internet connection with the number four, make a new frontend for a website you use a lot that has a really bad frontend. you learn a lot by tinkering

ps. next writeup soon™
