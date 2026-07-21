---
title: "Fitting a regular expression to a list of words"
url: "https://www.johndcook.com/blog/2026/07/19/fitting-a-regex/"
fetched_at: 2026-07-20T07:01:17.578249+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Fitting a regular expression to a list of words

Source: https://www.johndcook.com/blog/2026/07/19/fitting-a-regex/

Suppose you want to search for a list of words. If you're using grep, you can add the
-f
flag provide a file of regular expressions, and you can add the
-F
to tell it that the regular expressions are in fact just words. I did something like this
a couple days ago
when searching for diagnosis codes.
grep -w -F -o -f icd10codes.txt notes.txt
Now you might want to combine your list of words into a singular regular expression, for efficiency or possibly for some other reason. Apparently ripgrep does this because when I tried replacing grep with ripgrep in the command above I got an error saying "Compiled regex exceeds size limit of 104857600 bytes."
Beating brute force
Say you wanted to search for the strings "bluecross", "blueshield", and "bluey". You could simply form the brute force regular expression
bluecross|blueshied|bluey
but that doesn't take advantage of the fact that all three strings begin with "blue." A smaller regular expression would be
blue(shield|cross|y)
Finding the shortest regular expression that matches a list of words is a hard problem, but finding a regular expression that's shorter than brute force is not. The Python package
trieregex
will do this. According to the documentation,
trieregex creates efficient regular expressions (regexes) by storing a list of words in a trie structure, and translating the trie into a more compact pattern.
Let's try our blue example with trieregex.
import re
from trieregex import TrieRegEx as TRE

words = ['bluecross', 'blueshield', 'bluey']
tre = TRE(*words) 
print(tre.regex())
This produces the same regular expression as above, except it adds
?:
to make the parentheses non-capturing.
blue(?:shield|cross|y)
Prefixes versus suffixes
The library builds a trie data structure using common prefixes. That works well in the example above, but the result is disappointing when we have common suffixes rather than common prefixes. The following code
words = ['javascript', 'typescript']
tre = TRE(*words) 
print(tre.regex())
produces the regular expression
(?:javascript|typescript)
which is no better than brute force, whereas we might have hoped for
(?:java|type)script
HCPCS examples
As mentioned at the top of the post, ripgrep failed to search on a list of ICD-10 codes. The list of HCPCS codes is about 10x smaller, and more compressible. Ripgrep was able to fit all HCPCS codes into a single regex and was able to search the test file much faster than grep. The command
grep -w -F -o -f icd10codes.txt notes.txt
took 73.426 seconds to execute, while the command
rg -w -F -o -f icd10codes.txt notes.txt
took 0.078 seconds, three orders of magnitude faster.
The following code will read a list of HCPCS codes from a file and create a regular expression.
tre = TRE()
with open('hcpcs.txt', 'r') as file:
    for line in file:
        tre.add(line.strip())
print(len(tre.regex()))
This shows that the resulting regular expression has 17,198 characters. The file of codes has 8725 five-character codes, so the regex compresses the code characters by roughly a ratio of 5 to 2.
