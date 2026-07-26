---
title: "Excel column numbering"
url: "https://www.johndcook.com/blog/2026/07/25/excel-column-numbering/"
fetched_at: 2026-07-26T10:22:50.698869+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Excel column numbering

Source: https://www.johndcook.com/blog/2026/07/25/excel-column-numbering/

I was working with a wide spreadsheet from a client the other day and I had to convert between Excel column labels and column numbers. I had never paid attention to how Excel labels columns and implicitly thought it was base 26 using letters rather than digits. But then I realized that’s not right.
Excel labels columns A through Z, then AA through AZ, then BA through BZ, etc. If this is base 26, then does A correspond to 0? That could work for A through Z, but then what about AA? Then you’d have to say the first A corresponds to 26 but the second A corresponds to 0.
Does Z correspond to 0? If so then the column numbers would be 1 through 25, followed by 0, then 27. And it would mean that columns ZA through ZZ are the same as A through Z.
In fact nothing in Excel column labeling corresponds to 0. The labels cannot be interpreted as a positional number system.
There’s a name for this kind of number system:
bijective base 26
. The concept extends generally to bijective base
b
for any positive integer
b
. The idea is ancient, but the name was coined recently. It has also been called
k
-adic numbering. For most of history it didn’t have a name.
The motivation behind the name bijective base
b
is that there is a bijection (a one-to-one correspondence) between these symbols and positive integers; there’s no possibility of leading zeros that would keep the mapping from being a bijection, unlike say 7 and 07 representing the same number.
Excel limits
Before 2007, an Excel file could have a maximum of 2
8
= 256 columns, and so the largest column label was IV.
Then in 2007 the column limit was increased to 2
14
= 16,384 and the largest column label is XFD.
Conversion code
Converting from column labels to integers is easy; going the other way is a little more complicated.
letter_to_ordinal = lambda c: ord(c) - ord('A') + 1
ordinal_to_letter = lambda n: chr(ord('A') + n - 1)

def label_to_num(label):
    label = label.upper()
    n = 0
    for c in label:
        n = n*26 + letter_to_ordinal(c)
    return n

def num_to_label(n):
    letters = []
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        letters.append(ordinal_to_letter(remainder + 1))
    return ''.join(reversed(letters))
Tests
The following code verifies the assertions above about the maximum number of Excel columns over time.
assert(num_to_label(256) == "IV")
assert(label_to_num("IV") == 256)

assert(num_to_label(2**14) == "XFD")
assert(label_to_num("XFD") == 2**14)
The conversion routines are not limited to actual Excel labels but work for arbitrarily large integers and bijective base 26 representations. For example, the following code shows that the bijective base 26 representation of Avogadro’s number is MUAEKAUDYDXEWOSDD.
avogadro = 602_214_076_000_000_000_000_000
assert(label_to_num(num_to_label(avogadro)) == avogadro)
print(num_to_label(avogadro))
Related posts
