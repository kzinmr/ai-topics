---
title: "Regular expression speed and error rates"
url: "https://www.johndcook.com/blog/2026/07/17/regex-speed-error/"
fetched_at: 2026-07-18T07:00:46.991191+00:00
source: "johndcook.com"
tags: [blog, raw]
---

# Regular expression speed and error rates

Source: https://www.johndcook.com/blog/2026/07/17/regex-speed-error/

Seven years ago
I wrote a post about regular expressions to match diagnosis codes. I wanted to revisit that post looking at speed and error rates.
Regular expressions usually do not exactly match what you’re looking for and nothing else. They have error false positives and false negatives. But they also have advantages, and context determines whether the advantages make the error rates tolerable.
The post mentioned above gave the following regular expression for ICD-10 diagnosis codes.
[A-TV-Z][0-9][0-9AB]\.?[0-9A-TV-Z]{0,4}
As cryptic as this may look at first glance, it’s straight-forward to interpret. It says that an ICD-10 code
Begins with a capital letter, excluding U
Followed by a digit
Followed by a digit or A or B
Optionally followed by a period
Followed by up to 4 digits or capital letters, excluding U.
Speed
Now suppose you want to scan a text document for ICD-10 codes. One approach would be to use the regex above. Another would be to compare every alphanumeric sequence in the document to a list of ICD-10. Currently this list has 74,719 codes.
I tested both approaches on a 800kb text file. The regex search
egrep -o '[A-TV-Z][0-9][0-9AB]\.?[0-9A-TV-Z]{0,4}' notes.txt
took 18 milliseconds. Searching against the list of codes
grep -w -F -o -f icd10codes.txt notes.txt
took 386 seconds, about six and a half minutes or five orders of magnitude longer.
Error rates
The regex
[A-TV-Z][0-9][0-9AB]\.?[0-9A-TV-Z]{0,4}
had a false negative rate of zero at the time it was written. I tested the regex against the current list of codes with the following command.
egrep -v '[A-TV-Z][0-9][0-9AB]\.?[0-9A-TV-Z]{0,4}' icd10codes.txt
The
-v
flag reverses the sense of the search, reporting lines that do not match the regular expression. This returned three matches: U070, U071, and U099. So 3 out of 74,719 valid ICD-10 codes were reported as invalid.
Codes beginning with U are designated for provisional/emergency/special purposes, but these three have become essentially permanent. A change in the application of the ICD-10 standard caused an error in the regular expression.
But the change would also have caused an error in code that did an exhaustive search against the list of ICD-10 codes at the time. In fact, every new code not starting with U would also be reported in error. So the regex is actually more future-proof than an exhaustive search. Presumably the simplified regex
[A-Z][0-9][0-9AB]\.?[0-9A-Z]{0,4}
will remain valid for the foreseeable future.
We’ve looked at false negatives. What about false positives? That depends on context. The false positive rate when searching medical notes is low: a word matching the regex above in a medical record is most likely an ICD-10 code. But the number of conceivable false positives is enormous. If you were searching a file of randomly generated alphanumeric text, the regex matches would overwhelmingly be false positives [1].
The number of strings matching
[A-Z][0-9][0-9AB]\.?[0-9A-Z]{0,4}
would be
26 × 10 × 12 × (1 + 36 + 36
2
+ 36
3
+ 36
4
) = 5,390,127,600.
Out of over five billion strings matching the regular expression, only around 75,000 are valid ICD-10 codes. So a naive theoretical calculation would say the false positive rate is 99.9986%, whereas in practice the false positive rate is very low, though there’s no way to say
a priori
exactly how low.
Related posts
[1] You could argue that all positives would be false positives in this context because you’re looking at noise. You couldn’t find an ICD code, though you could find a string of characters that coincides with an ICD code. That may sound like a pedantic distinction, but it matters in the context of evaluating deidentification quality: you want to find instances of PHI, not instances of strings that match the character pattern of PHI.
