---
title: "Cryptographic Keys and Decks of Cards"
url: "https://www.johndcook.com/blog/2026/07/28/keys-and-cards/"
fetched_at: 2026-07-29T10:11:52.430593+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Cryptographic Keys and Decks of Cards

Source: https://www.johndcook.com/blog/2026/07/28/keys-and-cards/

The
previous post
looked at the idea of storing a cryptographic key in the order of a deck of cards. A deck of 52 cards can store 225 bits of data because
⌊log
2
(52!)⌋ = 225.
Here ⌊
x
⌋ is
x
rounded down to the nearest integer.
If we want to store bigger keys, we’re going to need a bigger deck of cards.
Bitcoin
A Bitcoin key has 256 bits, which would require a deck of 58 cards. There is a card game called Zwicker that uses a deck of 58 cards, the usual 52 cards plus six jokers. So you could store a Bitcoin key in the permutation of a Zwicker deck.
You could also use a deck of 52 cards, plus 2 jokers, if you also consider orientation. 30 cards are rotationally symmetric, 22 are not, and neither are jokers. So, including two asymmetric jokers, you could add 24 additional bits. Permutations of a 54 card deck can encode 237 bits, and with 24 orientation bits, this is a total of 261 bits.
RSA
RSA key sizes vary, but 2048 and 3072 are common. A 2048-bit key would require a deck of 301 cards. Casinos often use a shoe of 312 cards, combining six decks of 52 cards, to deal Baccarat or Blackjack. However, casinos combine identical decks. If you were to combine six unique decks, you could store a 2048-bit key.
Storing a 3072-bit key would require a deck of 422 cards. You could make a deck of 432 cards by combining 8 distinguishable packs of 54 cards (52 + 2 jokers).
ML-KEM
ML-KEM is a proposed quantum-resistant replacement for RSA. As with RSA, key sizes for ML-KEM vary, the smallest being ML-
KEM-512
with a key size of 1632 bytes, which equals 13056 bits. This would require a deck of 1442 cards. You could combine 28 distinct packs of 52 cards, but that’s unwieldy.
This illustrates one of the difficult trade-offs with post-quantum cryptography: key sizes are much bigger. If you wanted to create a deck of 1442 cards, you’d probably want to make your “cards” something other than standard playing cards. You’d want to use permutations of something else.
Verification
The following Python code verifies the calculations above.
from math import log2, factorial, floor

def capacity(cards):
    return floor(log2(factorial(cards)))

def verify(bits, cards):
    return capacity(cards) >= bits and capacity(cards-1) < bits

print(verify(237, 54))
print(verify(256, 58))
print(verify(2048, 301))
print(verify(3072, 422))
print(verify(1632*8, 1442))
For more on how I came up with the deck sizes, see the
next post
on computing the inverse factorial.
