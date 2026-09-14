---
source_url: https://www.vals.ai/blogs/fable-solves-cyphral-distich
ingested: 2026-09-14
sha256: de543194f9d3a617cacb66839ebdfe19e26604ca30ea331c0c137f6ab628f85f
---

# Vals AI — Fable 5.1 Solves the Cyphral Distich, a 370-year-old cipher

We gave Claude Fable 5.1 an open task: solve Sir Thomas Urquhart's Cyphral Distich.
It appears to have actually solved it, and the solution is quite embarrassing for humans in hindsight.

At the end of Urquhart's *Logopandecteision* is a cryptogram consisting of two lines of 32 numbers each, called the Cyphral Distich. A cryptogram is a short message deliberately encoded so it can't be read without knowing the rule that produced it. Here the entire puzzle input is these 64 numbers, and the goal is to recover the hidden plaintext:

5.3.27.38.32.14.21.8.66.8.70.39.5.9.12.18.2.3.56.5.1.7.3.2.13.19.3.25.9.3.16.6.

25.15.13.6.11.20.5.1.2.12.1.20.20.49.20.20.35.33.4.6.8.35.5.33.5.5.18.10.3.11.32.42.

This cipher has remained seemingly unsolved for centuries. It was posed as an open problem in *Notes and Queries* in 1899, appeared again in 20th-century cryptography literature, and was later listed by historical-cipher researcher Klaus Schmeh among his Top 50 unsolved encrypted messages.

Various people attempted to decipher it, but it seems they were missing one crucial hint. They tried methods like frequency analysis, substitution, and homophonic substitution, and none of these approaches worked.

That's because they missed one easy clue.

## Solution

After 44 minutes, 176k tokens, and zero interjections from me, Fable 5.1 arrived at a solution. It tried a few approaches, but was finally able to solve it with two central realizations.

First: the cryptogram is printed immediately after Urquhart's *32 Proquiritations*, and Urquhart even goes out of his way to emphasize that number. He says: "there can no number like that of two and thirty … be pitched upon"

Second: the poem accompanying the cipher promises that an honest reader will find in it "his own heart's wishes, and the Author's minde." The Proquiritations themselves repeatedly conclude with formulations like "is the desire," "wish," or "hope of."

If you put these clues together: 32 Proquiritations. 32 numbers in the first cipher line. 32 numbers in the second. "Wishes."

Most historical attempts assumed the key was external: a cipher alphabet, or some mapping of numbers to letters or words, that had to be reconstructed from outside the text. But the key was not an external cipher alphabet at all. The key was the book itself.

The rule was simple: for the i-th number in a cipher line, go to the i-th Proquiritation, use that number as a word index, and take the first letter of that word.

With this, you get:

O GOD UPHOLD KING CHARLS THE SECOND AND

MAKE HIM THE SUPREME RULER OF THIS LAND

And the result is extremely self-verifying. Each line contains exactly 32 letters and ends "and" / "land" (a rhyming 2 line verse), consistent with the promised distich. It also makes historical sense: Urquhart was a committed Royalist. Hiding a prayer for Charles II in the text is entirely consistent with his politics.

Urquhart left a second, much larger cryptogram in the book, which remains unsolved.

## Key facts

- Task: autonomous open-ended cryptanalysis of the Cyphral Distich (posed as open problem 1899; listed in Klaus Schmeh's Top 50 unsolved ciphers).
- Model: Claude Fable 5.1 (Anthropic), via Vals AI agentic eval harness.
- Cost: 44 minutes, ~176k tokens, zero human interjections.
- Decoded plaintext: "O GOD UPHOLD KING CHARLS THE SECOND AND MAKE HIM THE SUPREME RULER OF THIS LAND" — self-verifying (32 letters per line, rhyme, Royalist context).
- Insight class: the cipher key was internal to the book (self-key / book cipher using the 32 Proquiritations), not an external alphabet — humans' assumption of an external key was the blocking bias.
- HN discussion: https://news.ycombinator.com/item?id=49688695 (1021 points, 446 comments, Sep 13 2026 — top HN story of the window).
