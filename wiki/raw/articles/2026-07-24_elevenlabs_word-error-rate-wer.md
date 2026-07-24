---
title: "What is word error rate (WER) and how do you use it"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/word-error-rate-wer"
scraped: "2026-07-24T06:00:35.555866+00:00"
lastmod: "2026-07-22T18:58:34.357Z"
type: "sitemap"
---

# What is word error rate (WER) and how do you use it

**Source**: [https://elevenlabs.io/blog/word-error-rate-wer](https://elevenlabs.io/blog/word-error-rate-wer)

Blog
Word error rate (WER): Key concepts, formula, and uses
Written by
Jack
Limebear
Published
Jul 21, 2026
Last updated
Jul 22, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Sign up
Learn more
On this page
Introduction
Summary
What is word error rate?
Why does word error rate matter in speech recognition systems?
How to calculate word error rate: Formula and example
Comparing word error rate and other recognition metrics
Levenshtein distance examples: The mathematics behind WER
Common pitfalls and misconceptions around word error rate
Industry benchmarks for WER
Get started with ElevenAPI to boost recognition accuracy
Word error rate FAQ
In theory, word error rate (WER) is a metric for determining the accuracy of an Automatic Speech Recognition (ASR) tool. A low WER means your final transcript is more accurate, with a higher error rate showing mis-transcribed information.
In practice, WER could be the difference between medical transcription software that writes that a patient needs ‘fifteen milligrams’ and ‘fifty milligrams’ of a prescription. It’s the gap between a support tool that accurately transcribes a customer’s needs and one that leaves your user feeling frustrated.
In this article, we’ll break down what WER is, how to calculate it, and how to use it to benchmark your own ASR provider.
Summary
Word error rate counts three error types across substitutions, deletions, and insertions, divided by the number of words in the reference transcript.
The formula for WER is WER = (S + D + I) / N.
Lower WER scores mean the final output is more accurate.
Under 5% WER is a good benchmark, although legal or medical transcriptions may require even lower Word Error Rate.
WER treats all errors as equal, meaning it’s not a perfect metric for contextual reading. Emerging metrics, such as Semantic Word Error Rate (SWER) attempt to answer this by measuring whether the meaning of an utterance was preserved.
What is word error rate?
Word error rate (WER) is the standard metric for measuring speech recognition accuracy in speech to text models. It’s a representation of 0-1 (0.8 would represent an 80% error rate) of what an STT system gets wrong when transcribing, mapped out against its substitutions, deletions, and insertions.
A substitution is when a word is replaced with the wrong one. Deletion is where a word was missed entirely. Finally, insertion is where the transcript has a word added that was never spoken. WER uses all three of these components and then divides by the number of words in the correct transcript, giving a number you can use to compare against other vendors.
Here’s the formula for WER written out:
WER = (S + D + I) / N
Where:
S: Substitutions (word is wrong)
D: Deletions (word is missing)
I: Insertions (additional word is present)
N: Total words in the reference transcript
You can express WER as either a decimal or a percentage. The lower the WER, the better your score was as the model made fewer errors when transcribing.
In practice, a 10% WER means roughly 1 in 10 words in your meeting transcript needs a second look.
Why does word error rate matter in speech recognition systems?
Word error rate provides an objective metric that teams can use to compare different providers. It cuts through any marketing claims and gives clear visibility of how accurate a speech recognition model is. By leading with evidence, any enterprise that’s assessing its options has a clear view of which models are the current leaders in this space.
Source:
Artificial Analysis
accessed July 10th, 2026.
As of July 2026, independent research by
Artificial Analysis
ranks ElevenLabs’ Scribe v2 as having the lowest WER in the industry on the AA-AgentTalk dataset for non-streaming transcription models, scoring 1.5% WER.
Beyond vendor evaluation, WER has a real-world impact at the product level. Medical transcription software with a 12% WER could introduce critical errors to patient charting. Mis-transcriptions in a customer support call could lead to downstream failures, such as inaccurate sentiment analysis or poor categorization.
Beyond these use-case-specific issues, when ASR systems fail, the people who are affected most are often those for whom the transcript is the only way to access spoken content at all. The
World Wide Web Consortium
offers extensive documentation on the minimum standards that are expected by accessibility initiatives for more context.
How to calculate word error rate: Formula and example
Calculating word error rate is an easy process once you know the steps. As examined above, the formula you’ll use is WER = (S + D + I) / N. All terms are described above, but for quick reference they are substitutions, deletions, insertions, and N for total words in the transcription.
Here is how you calculate WER:
Create a reference transcript:
Use human transcription and verification to produce an accurate transcription of an audio clip.
Use your STT tool:
Use an ASR platform to transcribe the audio clip, producing an AI transcript that you’ll use as your test.
Align the two versions:
Use dynamic programming (specifically the Levenshtein algorithm) to find the minimum number of edits. We’ll expand upon that algorithm in a later section.
Apply the formula:
Count the total number of errors in the AI-generated version against the human-verified copy and then use WER = (S + D + I) / N to calculate the exact WER.
This seems fairly technical on paper, but is actually much easier in practice. Here’s a practice example to show you what we mean.
Reference transcript:
Mrs. Dalloway said she would buy the flowers herself.
ASR output:
Miss Dalloway said she would buy flowers herself.
Word
Reference
ASR output
Error type
1
Mrs.
Miss
Substitution
2
Dalloway
Dalloway
Correct
3
said
said
Correct
4
she
she
Correct
5
would
would
Correct
6
buy
buy
Correct
7
the
—
Deletion
8
flowers
flowers
Correct
9
herself
herself
Correct
If we calculate the total errors, we have 1 S and 1 D out of 9 total words.
Using the formula, we get: WER = 2 / 9 = 0.222 = 22.2%.
Calculating the word error rate with Python
While the manual method works great, you can save time by calculating WER with python. The
jiwer library
handles all of this completely automatically.
Using the jiwer documentation, you can install the package, which is specifically built for evaluating an ASR system and producing core metrics like WER. Once downloaded, you can use the following code to quickly calculate WER with python:
from
jiwer
import
wer

reference =
"the quick brown fox jumps over the lazy dog"
asr =
"the quick brown fox leaps over the last lazy dog"
print
(wer(reference, asr))
# 0.222
Notice how, in this example, the ASR output differs from the original reference in two places. The word ‘jumps’ was incorrectly transcribed as ‘leaps’ (a substitution) and ‘last’ was inserted before ‘lazy’ (an insertion). With two errors across the nine words in the reference transcript, this results in a Word Error Rate (WER) of 0.222 or 22.2%.
Comparing word error rate and other recognition metrics
While WER is the standard metric to calculate accuracy in an ASR, there are other tools you can use. For example:
Character Error Rate (CER):
Much like WER, it measures transcription accuracy at the character level rather than at the word level. Best for languages that don’t have clear word boundaries (scriptio continua) or spelling-sensitive tasks.
Match Error Rate (MER):
Measures the proportion of transcription errors while treating substitutions, insertions, and deletions slightly differently from WER. It focuses on the proportion of errors that are wrong in a sentence.
Word Information Lost (WIL):
An estimation of how much of the original information was lost during transcription, providing a measure of intelligibility rather than WER’s direct error count.
Embedding Error Rate (EmbER):
Offers a semantic analysis between the transcriptions. It goes beyond WER to give insight into the semantic distance between the correct word and the incorrect transcription.
Each of these metrics is best for a different scenario. Here’s a table you can reference:
Level of analysis
WER
Word
CER
Character
MER
Word
EmbER
Semantics
Best for
WER
ASR benchmarking and assessment
CER
ASR languages without word boundaries
MER
Error decomposition
EmbER
Semantic-aware evaluation
Metric
Level of analysis
Best for
WER
Word
ASR benchmarking and assessment
CER
Character
ASR languages without word boundaries
MER
Word
Error decomposition
EmbER
Semantics
Semantic-aware evaluation
Levenshtein distance examples: The mathematics behind WER
Word error rate is really a measure of the distance between the original and the hypothesis output. To understand that difference mathematically, we use the Levenshtein distance.
The Levenshtein distance counts the minimum number of single-unit edits required to transform one sequence into another. What that means for WER is specifically the edits of substitutions, insertions, and deletions. For example, if we wanted to transform Cat into Mat, you’d have to move one letter ‘C’ to ‘M’, giving a Levenshtein distance of 1.
While you’d see a lot more of this in CER calculations, WER takes the Levenshtein distance and scales it up to the word level. Each unit is a whole word instead of a character, with the true distance measuring how many word edits it would take to transform our ASR output into the accurate original.
We build a matrix where each cell represents the total distance between the original transcript and the ASR transcript. The Levenshtein distance then fills out the matrix from top-left to bottom-right, with the final cell giving you the total number of word-level edits. Dividing that number by N is your WER.
While this matrix is usually calculated with individual characters, here is a scaled-up version of our previous example for simplicity.
Common pitfalls and misconceptions around word error rate
Especially as
STT APIs
become more accessible and ASR software becomes a common part of wider agent stacks, we’re going to see a lot of comparisons between different tools.
Before calculating any of your own word error rates, there are a few common issues and misconceptions you should understand.
All errors are equal:
WER treats every error as equally significant. While in many contexts that may be fine, some use cases make this unacceptable. For example, in a hospital, a 5% error which would be considered a good WER may still be incomprehensible, as even one or two errors could put a patient at risk. This limitation has led to the development of newer metrics, such as Semantic Word Error Rate (SWER), which attempts to measure whether the meaning of a sentence was preserved rather than whether every word matched exactly.
WER goes beyond 100%:
While we previously stated WER goes between 0 and 1, you can still find a WER of over 100%. That’s because the insertion error can create more words than the total from the original transcript. A common one here is transcribing ‘I’m’ as ‘I am’, where one becomes two.
Lower WER isn’t, technically, always better:
A WER of 5% is, on paper, better than a WER of 10%. But, if the errors that contributed to that 5% significantly changed the context of a sentence while those in the 10% didn’t, then the whole story isn’t represented. Context still matters significantly here, with metrics such as SWER being developed specifically to capture this semantic impact.
Back in 2024, Apple published an interesting study that explored the last point above. When humans assessed a WER calculation of 9.4% looking at whether or not the ASR was readable, they gave the same passage a
WER of only 2.2%
. In the example they tested, humans saw the ‘errors’ as insignificant in many cases, producing a Human WER over 4x more forgiving than machines.
Industry benchmarks for WER
The ideal WER is heavily dependent on the industry or use case you’re using ASR technology in. While <5% is an industry benchmark for WER, specific industries like medical or legal transcription need a much lower rate.
In the
Artificial Analysis
July 2026 study, ElevenLabs’ Scribe v2 scored a 1.5% WER. However, it’s important to remember that these statistics are typically conducted around English as a primary language. STT technology in other languages may not be as effective.
The ElevenLabs Docs break down the
general WER bands
across all of the languages that Scribe v1 and Scribe v2 support.
Get started with ElevenAPI to boost recognition accuracy
When you’re building an application or product where transcription quality matters, the gap between a well-chosen ASR API and a mediocre one shows up first in your WER and then in your users’ experiences.
ElevenLabs Scribe is the
Speech to Text
layer accessible through
ElevenAPI
. Alongside 90+ languages and an industry-leading WER, it offers features like speaker diarization, word-level timestamps, keyterm prompting, and entity detection.
Explore the
ElevenLabs Docs
to learn more about ElevenAPI or get started by
signing up
today.
Word error rate FAQ
What is a good word error rate?
For the vast majority of use cases, a WER of <5% will create an accurate transcription. Anything over 20% would require additional review by a human.
Can word error rate be above 100%?
WER exceeds 100% when the total number of errors is greater than the number of words in the reference. Insertions to a sentence make this possible.
What’s the formula for WER?
The formula for WER is WER = (S + D + I) / N. Substitutions plus deletions plus insertions, divided by the number of words in the reference.
What does word error rate mean?
WER measures how many words an automatic speech recognizer tool got wrong in a transcript when compared to an accurate human reference transcript.
Can you use BLEU or ROUGE instead of WER?
BLEU and ROUGE are two scores for evaluating machine translation and text summarization, respectively. While they could measure textual similarity between a reference transcript and the ASR output, they’re generally less suitable than WER as they mainly focus on overlapping phrases rather than substitutions, deletions, and insertions.
