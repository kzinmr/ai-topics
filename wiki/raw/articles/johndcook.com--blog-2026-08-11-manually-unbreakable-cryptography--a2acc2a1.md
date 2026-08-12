---
title: "Manually unbreakable cryptography"
url: "https://www.johndcook.com/blog/2026/08/11/manually-unbreakable-cryptography/"
fetched_at: 2026-08-12T10:18:35.146597+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Manually unbreakable cryptography

Source: https://www.johndcook.com/blog/2026/08/11/manually-unbreakable-cryptography/

Suppose you were able to go back in time, to an era before computers, and give someone contemporary cryptography. Encryption methods that are essentially unbreakable now would certainly be unbreakable then. But there’s a catch: not only do attackers not have computers, neither do users.
Manual cryptography
If you told someone about RSA encryption, for example, you’d lose them right after you said “First you find a couple 1000-digit primes.” But there’s no need for using 1000-digit primes if no attacker has a computer. You could use 100 digit primes. Could you use 10 digit primes? If you chose primes just big enough to make the method unbreakable by hand, could someone implement it by hand?
Kirchoff’s principle says the strength of an encryption method should depend only on keeping the key secret, not the method. If you
could
keep the method secret, RSA would be unbreakable because nobody thought of anything like it before computers. But to make our thought experiment more interesting, let’s suppose that an enemy has also traveled back in time. If you tell your side about RSA, he can tell his side about it as well. So we’re back to Kirchoff’s principle.
An encryption method combinining substitution and permutation would have been practical to carry our manually. The
ADFGVX
cipher from 1918 was a start in this direction. That idea could been extended further, with a larger substitution set and longer permutations, and with more than one round of substitution and permutation, approaching what would be come the approach used in modern symmetric encryption. Such a method might have been manually implementable without being manually breakable.
Mechanized cryptography
World War II was a time of transition from manual cryptography to computerized cryptography. Encryption machines were attacked by cryptanalysis machines, though these machines were general-purpose computers. If you could implement a symmetric encryption method like AES in a mechanical device, no mechanical device could break it.
You could use something like
DES
, simpler than AES but still unbreakable at the time. DES is considered broken because now you could throw enough compute power at it to break it by brute force, but that would not be possible with only mechanical devices.
My hunch is that the best approach would be stream ciphers. Maybe it would be practical to implement one of these by hand or with the aid of simple calculating machines. Something like PCG, which is not cryptographically secure today [1], would have been then, though I don’t know how practical it would have been to carry out PCG, say, in the 1940s.
More pre-computer cryptography
[1] In 2020, Charles Bouillaguet, Florette Martinez,
and Julia Sauvage were able to break PCG using 20,000 CPU-hours. See their paper Practical seed-recovery for the PCG Pseudo-Random Number Generator. IACR Transactions on Symmetric Cryptology. ISSN 2519-173X, Vol. 2020, No. 3, pp. 175–196.
