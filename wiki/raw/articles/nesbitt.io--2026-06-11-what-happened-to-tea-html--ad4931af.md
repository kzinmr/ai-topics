---
title: "What Happened to tea.xyz"
url: "https://nesbitt.io/2026/06/11/what-happened-to-tea.html"
fetched_at: 2026-06-12T07:00:52.395292+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# What Happened to tea.xyz

Source: https://nesbitt.io/2026/06/11/what-happened-to-tea.html

On June 4th,
tea.xyz
launched what it had been promising since 2022: a cryptocurrency that pays open source maintainers. Within the first hour of official trading, the token fell 75% from its opening price. A week later it trades about 90% below its first-day high, the company’s GitHub org has been near-silent for six months, and the founder’s public commits are going to a different project entirely.
Their own blog post from June 8th, titled
The Work Continues
, concedes “the right response is not to pretend the launch went the way we wanted. It did not.” I’ve been pulling the public data: GitHub commit history, on-chain trading records, and the long paper trail tea left across the package registries.
Where tea came from
tea was founded by Max Howell, the creator of Homebrew, with Timothy Lewis. It
came out of stealth in March 2022
with $8M led by Binance Labs, followed by
an $8.9M seed round in December 2022
. The pitch had two halves: a new package manager (the
tea
CLI), and a blockchain protocol that would reward the maintainers of open source packages with tokens. Howell wrote Homebrew and made nothing from it, and the pitch leaned on that history, famous Google interview rejection included.
The two halves split in October 2023, when the package manager was renamed
pkgx
and moved to its own GitHub org (
the old teaxyz/cli repo still redirects there
) while the teaxyz org kept the crypto protocol. pkgx is a decent piece of software, and it never had a token in it. But the separation was only organisational: the company and founders stayed the same, and pkgx remained part of tea’s pitch as the eventual “cryptographically aware package register” for the protocol.
The incentive design
The
white paper
describes a mechanism called Proof of Contribution. Every package gets a score called
teaRank
, computed over the dependency graph and explicitly modelled on Google’s PageRank. The more packages depend on yours, the higher your rank, and rewards scale with rank. To claim a package you add a
tea.yaml
file to its repository containing your wallet address.
The protocol paid out tokens in proportion to how many packages you controlled and how connected they were. Registering a thousand packages paid better than one, and declaring dependencies between them pushed their ranks higher still. Nothing in the design was costly to fake, since a package name costs nothing to register and a dependency is one line in a manifest. In February 2024 tea opened
an incentivized testnet
, a trial version of the protocol where points earned would convert to tokens at launch, and reported
nearly 200,000 signups and 500 projects in the first week
.
The spam
The farming started immediately, with pull requests on GitHub adding
tea.yaml
files to other people’s projects, trying to claim repos the submitter didn’t own. Howell called the PRs
“disgusting and counter productive”
. On the registries,
Phylum documented
new npm package publications climbing from mid-February 2024 to over seven times normal daily volume, with around 14,000 tea-registered packages across npm, PyPI, RubyGems, and crates.io.
Sonatype counted roughly 15,000
on npm alone, with single accounts publishing hundreds of packages.
RubyGems published
an incident report
describing empty gems created to farm rewards, including one six-year-old gem with over 100,000 downloads whose owner retroactively added a
tea.yaml
to cash in on it. In response they tightened publishing limits and blocked the accounts responsible. By August 2024,
DEVCLASS reported research
estimating that of roughly 890,000 packages published to npm in the prior six months, around 70% were tea farming spam.
In November 2025, Endor Labs analysed the
“IndonesianFoods” campaign
: 43,000+ packages from at least 11 npm accounts over nearly two years, with auto-generated names from word lists.
Amazon Inspector tied over 150,000 packages
to the same token-farming campaign. Some coverage called it a worm, though
Socket’s analysis
found automation rather than self-propagation. The spam packages declared dependencies on each other to inflate teaRank, which meant installing any one of them pulled in the whole tree.
An academic paper
published in 2025 measures the abuse. The cleanup costs landed on npm, RubyGems, PyPI, and every mirror and security scanner downstream.
tea
responded that November
by halting rewards distribution for the affected period and promising redesigned anti-spam rules. Howell
told The Register
the protocol would slash farmers’ rewards.
The launch
In September 2025, eight months before the protocol went live, tea ran
a public sale on CoinList
, a site that runs token sales for crypto projects: 4 billion TEA at $0.0005 each, implying a $50M valuation for the full 100 billion token supply. The terms unlocked 100% of the tokens on day one. Token sales usually stagger when buyers can sell, releasing tokens over months or years so early buyers can’t all exit at once.
The launch plan,
announced May 12th
, put trading on Aerodrome, an exchange that runs as a program on Base, a blockchain built by Coinbase, rather than as a company matching orders. Prices on this kind of exchange come from a pool of paired tokens, TEA on one side and a dollar-pegged token on the other, and each trade moves the price along a curve. The smaller the pool, the more each trade moves it. tea seeded the pool with 2% of the token supply and scheduled the launch for 00:00 UTC on June 4th.
$0
$0.0001
$0.0002
$0.0003
$0.0004
$0.0005
$0.0006
Jun 4
Jun 5
Jun 6
Jun 7
Jun 8
Jun 9
Jun 10
Jun 11
official launch, 00:00 UTC Jun 4
Hourly $TEA price on Aerodrome (TEA/USDC pool), data from GeckoTerminal
The pool received its tokens from 22:47 UTC on June 3rd, and
the first trade executed at 23:54 UTC
, six minutes before the official launch. tea’s June 8th post describes this as “onchain liquidity activity occurred ahead of the coordinated plan”: the pool was live and tradeable before the launch sequence finished. In those six minutes the price was bid up to $0.00065, above the CoinList sale price. In the first official hour, from 00:00 to 01:00 UTC, the price fell from $0.00046 to $0.00011 on $332,000 of volume, down 75% in 60 minutes.
The CoinList sale’s full unlock meant every September buyer was free to sell from the first minute, into a pool holding 2% of supply. The price has kept falling since and now sits around $0.00007,
86% below what CoinList buyers paid
eight months ago, valuing the entire 100 billion token supply at roughly $7M against the $50M the sale implied.
The collapse didn’t need anyone to withdraw the tokens backing the pool, and the pool still holds around $280K. Per
the project’s own pre-launch transparency filing
, about 20% of supply was circulating at launch, ten times what the pool held.
The GitHub record
Monthly commits across
the teaxyz org
and
the pkgxdev org
show how much of the company was still working by launch day:
0
100
200
300
400
Jan 2024
Jul 2024
Jan 2025
Jul 2025
Jan 2026
pkgxdev (package manager)
teaxyz (protocol)
Commits per month to non-fork repos in each GitHub org, via the GitHub API
Commits to the protocol org ramped through late 2024 as the team built
chai
, their open package dataset, and the token contracts, and even the December 2024 peak was only 100 commits. Activity declined through 2025: chai’s main developer stopped committing in August, the dataset repo’s last commit was in September, and the token contract repo’s last sustained work was in October and November. After November 2025, the month tea halted rewards over the farming campaign, the org had 2 commits in December, 1 in January, 2 in February, and none since.
The chart excludes forks, which hides the one place engineering continued: tea’s forks of go-ethereum and Optimism, the infrastructure for their blockchain, received steady commits from a single contributor through May 17th, 2026, two and a half weeks before launch.
Howell wrote 236 commits to pkgxdev repos in January 2025 and kept a steady pace through May, then made only scattered commits until stopping entirely in November 2025. His public GitHub activity in June 2026 is in
automic-vault
, a new org created in April with no connection to tea or pkgx, while
he remained tea’s CEO in press coverage
as recently as December.
pkgx itself is now mostly the work of one maintainer, Jacob Heider, who has carried the package-building pipeline more or less alone since mid-2025, lately assisted by Claude Code-generated pull requests that he reviews and merges. User-filed issues on the pkgx repo (then still teaxyz/cli) peaked at 78 a quarter in early 2023 and have arrived at a rate of 2 a quarter in 2026.
In tea’s Discord, the conversation since launch is upset token holders: testnet participants who completed identity verification say they’re not eligible for the airdrop, the free distribution of tokens they spent two years earning points toward, and a week after launch the official line in the channel is that nobody has said there won’t be one. “The current price is a complete joke for everyone who participated in the project,” as one user put it, while the moderation bot issues warnings for bad word usage. The member list shows two people with the Core Contributor role, and neither is a founder. The channels for the open source side of the project, the dev and package dataset discussion, have had no real activity since 2025.
tea’s post blames a bad week for crypto generally, and the wider market fell that week too. But the same post admits to “decisions, timing factors, and execution details that we are reviewing internally”, and the commit history shows few people left to conduct that review. Four years, roughly $17M in disclosed venture funding, and
about $2M more from the public sale
produced several hundred thousand spam packages and a cleanup bill paid by registries that never had any relationship with tea. The maintainers tea set out to pay, the ones with real packages and dependents, are left holding the same token as the farmers.
Data notes: commit counts are author-dated commits to non-fork repos in each GitHub org, collected via the GitHub API on June 11th 2026. Price data is GeckoTerminal hourly
OHLCV
for the Aerodrome TEA/USDC pool on Base. Issue counts exclude pull requests, bots, and tea team accounts. The raw data and chart scripts are in
data/tea on GitHub
.
