---
title: "Apr '26 Notes - Susam Pal"
url: "https://susam.net/26d.html"
fetched_at: 2026-05-01T07:13:05.460532+00:00
source: "susam.net"
tags: [blog, raw]
---

# Apr '26 Notes - Susam Pal

Source: https://susam.net/26d.html

Apr '26 Notes
By
Susam Pal
on 30 Apr 2026
This is my fourth set of
monthly notes
for this year where I write down interesting facts and ideas I have
  explored during my spare time.  There were three things in
  particular that occupied my leisure time this month.  First, I
  managed to learn the proof of Tutte's famous theorem that any \( s
  \)-arc-transitive finite cubic graph must satisfy \( s \le 5.  \)  I
  learnt the proof from Norman Biggs's book
Algebraic Graph
  Theory
.  The original proof appears in Tutte's 1947 paper 'A
  family of cubical graphs'
  (
DOI
).
  Biggs's presentation differs considerably from Tutte's original
  argument and relies heavily on the properties of stabiliser
  sequences of arcs.  I should say that Biggs's proof, while complete,
  is extremely condensed.  The proof reads more like a high-level
  outline that moves rapidly from one main result to the next without
  sufficiently explaining the intermediate steps.  As a result, it
  took considerable effort to work out the proofs of the intermediate
  results.  Biggs presents the proof in roughly nine pages spread
  across two chapters.  However, when I worked through it in full
  detail while ensuring that every step is justified, my notes
  eventually grew to around 18 pages of
A4 paper
.  The proof is quite
  involved, so I have not included it in these notes.  Perhaps
  someday, when I have more time, I will distil my handwritten notes
  and publish them here on my website.
That was the first thing I spent time on this month.  The second was
  revisiting some elementary results in group theory concerning
  cosets.  I have found cosets to be an extremely useful concept that
  plays a central role in many areas of mathematics, including coding
  theory, Galois theory, field extensions and graph theory.  In fact,
  Biggs's proof of Tutte's theorem discussed above also relies
  substantially on the theory of cosets.  Since these results are
  relatively elementary and easier to write up, they are included in
  this set of notes.
Apart from mathematics, I also spent part of my spare time improving
  my new web project named
Wander
  Console
.  These notes include some updates about this tool.
Contents
Coset Results
Subgroup
Cosets
Coset Membership
Coset Equality
Partitioning a Group into Disjoint Cosets
Computing
Wander Console Updates
Flush Output
Other Stuff
Coset Results
This section presents some very elementary results about cosets,
  together with brief proofs.  These results appear repeatedly across
  many areas of mathematics and I often find myself using them almost
  instinctively, without consciously thinking through the underlying
  arguments each time.  But once in a while, I like to sit back and
  ponder about their proofs from first principles, reflect on why they
  work and appreciate their elegance.  The subsections below collect
  some of these little proofs.
Subgroup
Definition.
Let \( G \) be a group with operation \( \cdot.  \)  Then a subset \(
  H \subseteq G \) is called a subgroup of \( G \) if \( H \) itself
  forms a group under the same operation and we write \( H \le G.  \)
Cosets
Definition.
Let \( G \) be a group, \( H \le G \) and \( a \in G.  \)  The left
  coset of \( H \) by \( a \) is the set

  \[
    aH = \{ ah : h \in H \}.
  \]

  Similarly, the right coset of \( H \) by \( a \) is

  \[
    Ha = \{ ha : h \in H \}.
  \]
Coset Membership
Theorem.
Let \( G \) be a group with identity \( e, \) \( H \le G \) and \( a
    \in G.  \)  Then \( aH = H \) if and only if \( a \in H.  \)
Proof.
Suppose \( aH = H.  \)  Then

  \[
    aH = H
    \implies ae \in aH = H
    \implies a \in H.
  \]

  Conversely, suppose \( a \in H.  \)  Let \( x \in aH.  \)  Then \( x =
  ah \) for some \( h \in H.  \)  Then by the closure property of the
  subgroup \( H, \) we get

  \[
    a, h \in H
    \implies ah \in H
    \implies x \in H.
  \]

  Thus \( aH \subseteq H.  \)  To show the reverse inclusion, let \( x
  \in H.  \)  Since \( a \in H, \) we have \( a^{-1} \in H, \) so

  \[
    x \in H
    \implies a^{-1} x \in H
    \implies a(a^{-1} x) \in aH
    \implies x \in aH.
  \]

  Therefore \( H \subseteq aH.  \)  As a result, \( H = aH.  \)
Coset Equality
Theorem.
Let \( G \) be a group with identity \( e, \) \( H \le G \) and \(
    a, b \in G.  \)  Then \( aH = bH \) if and only if \( a^{-1} b \in
    H.  \)
Proof.
Suppose \( aH = bH.  \)  Then

  \begin{align*}
    aH = bH
    & \implies b \in bH = aH \\
    & \implies b = ah \tag{for some \( h \in H \)}\\
    & \implies a^{-1} b = h \\
    & \implies a^{-1} b \in H.
  \end{align*}

  Conversely, suppose \( a^{-1} b \in H.  \)  Let \( h = a^{-1} b.  \)
  Then

  \begin{align*}
    h = a^{-1} b
    & \implies ah = b \\
    & \implies (ah)H = bH \\
    & \implies a(hH) = bH \\
    & \implies aH = bH \tag{since \( hH = H \)}.
  \end{align*}
Corollary.
Let \( G \) be a group with identity \( e, \) \( H \le G \) and \(
    a, b \in G.  \)  Then \( aH = bH \) if and only if \( a \in bH.  \)
Proof.
\[
    aH = bH
    \iff b^{-1} a \in H
    \iff b (b^{-1} a) \in bH
    \iff a \in bH.
  \]
Partitioning a Group into Disjoint Cosets
Theorem.
Let \( G \) be a group with identity \( e, \) \( H \le G \) and \(
    a, b \in G.  \)  Then either \( aH \cap bH = \varnothing \) or \(
    aH = bH.  \)
Proof.
Suppose \( aH \cap bH \ne \varnothing.  \)  Then there exists some
  element \( x \in aH \cap bH.  \)  Then

  \[
    x = ah_1 = bh_2
  \]

  for some \( h_1, h_2 \in H.  \)  Therefore

  \[
    a^{-1} b = h_1 h_2^{-1} \in H.
  \]

  Then by section
Coset Equality
,

  \[
    aH = bH.
  \]
Computing
Wander Console Updates
Wander Console
is a new project I
  developed in
March
while taking a short break
  from my algebraic graph theory studies.  It is a tiny,
  decentralised, self-hosted web console that allows visitors to a
  website to explore other interesting personal websites.  It is
  similar to the now-defunct service named
StumbleUpon
,
  but unlike StumbleUpon it has no central service and no server-side
  logic.  Wander is hosted entirely on independent personal websites.
  Wander Consoles link to one another and fetch web page
  recommendations from each other.  The entire tool consists of just
  two files:
an HTML file
and
a JS file
.  Everything, including
  connecting to other Wander Consoles in the network and recommending
  webpages, happens entirely on the client side in the user's web
  browser.  See
codeberg.org/susam/wander
for more details.
Two
releases
of Wander were made this month.  One notable feature introduced this
  month is the console network crawler.  You can visit any Wander
  console and use this feature to crawl the network reachable from it.
  To see this in action, go to my console at
wander/
, click the
Console
button at the top and then click the
Crawl
button.
Since different consoles link to different sets of peers, each one
  has its own neighbourhood, so the crawler output varies from console
  to console.
Due to the decentralised nature of the tool, it is difficult to know
  exactly how many people have set up Wander Console on their
  websites.  Nevertheless, I used the crawler with a known set of
  consoles to explore as much of the network as possible.  The result
  is available at
susam.codeberg.page/wcn/
.
  It currently shows over 50 consoles recommending more than 1400 web
  pages from the small web of personal sites.  For a project that is
  only six weeks old, these seem like decent numbers.
Flush Output
When I log into my Debian 13.2 system via SSH, I find
  that
ctrl
+
o
does not enable output discarding.
$
stty -a | grep 'discard\|flush'
werase = ^W; lnext = ^V; discard = ^O; min = 1; time = 0;
echoctl echoke -flusho -extproc
$
ping 127.0.0.1
PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.021 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.030 ms
^O
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.026 ms
64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.049 ms
^C
--- 127.0.0.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3079ms
rtt min/avg/max/mdev = 0.021/0.031/0.049/0.010 ms
On macOS 15.3.2, with the Terminal app, it does work as expected.
$
stty -a | grep 'discard\|flush'
-echoprt -altwerase -noflsh -tostop -flusho pendin -nokerninfo
cchars: discard = ^O; dsusp = ^Y; eof = ^D; eol = <undef>
$
ping 127.0.0.1
PING 127.0.0.1 (127.0.0.1): 56 data bytes
64 bytes from 127.0.0.1: icmp_seq=0 ttl=64 time=0.087 ms
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.221 ms
^O^C
--- 127.0.0.1 ping statistics ---
9 packets transmitted, 9 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 0.068/0.171/0.362/0.087 ms
Other Stuff
My initial draft of this post had a few additional sections that have
  since been moved to their own posts:
