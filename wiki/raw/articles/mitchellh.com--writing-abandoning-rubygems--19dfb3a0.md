---
title: "Abandoning Rubygems"
url: "https://mitchellh.com/writing/abandoning-rubygems"
fetched_at: 2026-05-01T07:02:04.201853+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Abandoning Rubygems

Source: https://mitchellh.com/writing/abandoning-rubygems

Vagrant 1.1+ no longer supports
RubyGems
as an installation method. Instead, you must install Vagrant 1.1+ using
pre-made packages or installers
. For folks used to the gem-based installation, this has caused a mixture of confusion and disdain. In this post, I enumerate my reasons for abandoning RubyGems, and why it is better for the Vagrant community long-term.
I initially released Vagrant as a RubyGem over 3 years ago. Vagrant is written in Ruby, and at the time I was already comfortable with making RubyGems, so I decided it was a natural distribution mechanism.
I don't regret this decision for a moment. The Ruby community is very open to cutting edge technologies, and I think that distributing as a RubyGem improved my initial adoption of the project.
Since then, however, I've grown and learned that RubyGems is no longer the best choice, for many reasons.
In this post, I'm going to explain why installers make life better for Vagrant users. In a future post, I'll explain how installers affect plugin developers and that ecosystem.
Non-Rubyists
Since the initial release of Vagrant in 2010, Vagrant has grown to be used by hundreds of companies and thousands of people. While I don't have hard numbers to back this up, a majority of the Vagrant users I meet are not Ruby developers.
Prior to making installers, the top complaint I would receive about Vagrant was about RubyGems. As a Ruby person myself, I always considered RubyGems to be simple. But for anyone outside the Ruby community, I learned that the burden of having to learn RubyGems, install Ruby, and so on was a high enough barrier to entry that many people didn't even try to install Vagrant.
On the other hand, packages that bundle all of Vagrant's dependencies (including Ruby), make installing Vagrant extremely simple.
Bugs
Vagrant has a lot of external dependencies: Ruby, RubyGems, OpenSSL, zlib, JSON, and more. With the RubyGems approach, users were left to manually install these dependencies, either from source or their package manager of choice.
Given this flexibility, I was unable to test Vagrant in every conceivable environment. I knew Vagrant worked on my system with my installed versions of dependencies, but didn't know if it would work in every system.
Because of this, it was common to receive bugs where Vagrant was used with dependencies that were too old, had bugs, or were simply broken due to permission errors and so on.
I don't care whether this is perceived as my fault or the user's fault. I don't blame users for not installing proper versions, especially if they just installed what their package repository had.
However, it is a
huge problem
when Vagrant crashes due to a broken environment, and then people perceive this as an instability in Vagrant itself, when 9 times out of 10, it was due to a misconfigured environment.
With installers, I am able to ship Vagrant with all the dependencies it needs, and promise the user that Vagrant will work with those dependencies. This is especially helpful in Windows environments.
Flexibility
Because I strictly control the environment, I'm able to improve and fine tune the dependencies Vagrant relies on.
In Vagrant 1.1, I replaced the old, slow pure-Ruby
tar
library i was using with
libarchive
, a high performance, stable, and flexible application and library written in C. libarchive is now shipped with every Vagrant installer, so users don't have to install another dependency, and don't really need to care Vagrant is using it.
In Vagrant 1.2, I replaced the downloader from using pure-Ruby HTTP to using
cURL
. This is much faster and supports many more network protocols, such as FTP. Every installer will ship with cURL pre-installed within it. Again, users don't need to care.
In the future, I'll be replacing the pure-Ruby SSH library with a more stable, well maintained SSH library written in C. Once again, users don't need to care, but they'll notice that SSH becomes more stable.
With all of these changes, I'm able to make significant dependency changes without the user noticing. In fact, all the user notices is that the Vagrant experience just got a lot better. Things got faster, things don't crash, and Vagrant supports more features.
Overall, Vagrant got a lot better because I was able to make changes I couldn't safely make by distributing via RubyGems.
