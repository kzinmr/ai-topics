---
title: "Quantum Y2K"
url: "https://www.johndcook.com/blog/2026/03/31/quantum-y2k/"
fetched_at: 2026-04-29T07:02:07.827998+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Quantum Y2K

Source: https://www.johndcook.com/blog/2026/03/31/quantum-y2k/

I’m skeptical that quantum computing will become practical. However, if it does become practical before we’re prepared, the world’s financial system could collapse. Everyone agrees we should prepare for quantum computing, even those of us who doubt it will be practical any time soon.
Quantum computers exist now, but the question is when and if a cryptographically relevant quantum computer (CRQC) is coming. At the moment, a quantum computer cannot factor 21 without cheating (i.e. not implementing circuits that you know
a priori
won’t be needed). But that could change suddenly. And some believe quantum computers could quickly go from being able to factor numbers with two digits to being able to factor numbers with thousands of digits (i.e. breaking RSA encryption) without much incremental transition between.
The move to post-quantum encryption may be a lot like Y2K, fixing vast amounts of 20th century software that represented years with two digits. Y2K turned out to be a big nothingburger, but only because the world spent half a trillion dollars on preparation to make sure it would be a big nothingburger.
Programmers in the 1970s obviously knew that the year 2000 was coming, but they also knew that they needed to conserve bytes at the time. And they assumed, reasonably but incorrectly, that their software would all be replaced before two-digit dates became a problem.
Programmers still need to conserve bytes, though this is less obvious today. Quantum-resistant signatures and encryption keys are one or two orders of magnitude bigger. This takes up bandwidth and storage space, which may or may not be a significant problem, depending on context. Programmers may conclude that it’s not (yet) worth the extra overhead to use post-quantum encryption. Like their counterparts 50 years ago, they may assume, rightly or wrongly, that their software will be replaced by the time it needs to be.
Moving to post-quantum cryptography ASAP is not a great idea if you can afford to be more strategic. It takes many years to gain confidence that new encryption algorithms are secure. The SIKE algorithm, for example, was a semi-finalist the NIST post-quantum encryption competition, but someone found a way to break it using an hour of computing on a laptop.
Another reason to not be in a hurry is that it may be possible to be more clever than simply replacing pre-quantum algorithms with post-quantum analogs. For example, some blockchains are exploring zero-knowledge proofs as a way to aggregate signatures. Simply moving to post-quantum signatures could make every transaction block 100 times bigger. But replacing a set of signatures by a (post-quantum) zero-knowledge proof of the existence of the signatures, transaction blocks could be
smaller
than now.
As with Y2K, the move to post-quantum cryptography will be gradual. Some things have already moved, and some are in transition now. You may have seen the following warning when connecting to a remote server.
** WARNING: connection is not using a post-quantum key exchange algorithm.
** This session may be vulnerable to "store now, decrypt later" attacks.
** The server may need to be upgraded. See https://openssh.com/pq.html
Key sizes don’t matter as much to
sftp
connections as they do to blockchains. And the maturity of post-quantum algorithms is mitigated by OpenSSH using hybrid encryption: well-established encryption (like ECDH) wrapped by newer quantum-resistant encryption (like MK-KEM). If the newer algorithm isn’t as secure as expected, you’re no worse off than if you had only used the older algorithm.
When clocks rolled over from 1999 to 2000 without incident, many people felt the concern about Y2K had been overblown. Maybe something similar will happen with quantum computing. Let’s hope so.
Related posts
