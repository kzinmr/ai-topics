---
title: "Readers can't identify watermarked AI text"
url: "https://seangoedecke.com/readers-cant-identify-watermarked-ai-text/"
fetched_at: 2026-08-21T10:01:07.073481+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# Readers can't identify watermarked AI text

Source: https://seangoedecke.com/readers-cant-identify-watermarked-ai-text/

In the last few weeks, I’ve been
complaining
that everyone is wrong about AI watermarking: it isn’t really anti-consumer and it doesn’t make the outputs any worse. The watermarking
papers
demonstrate
that this is true, but I thought it might be interesting to put it to a practical test. Given examples of watermarked and unwatermarked answers to the same prompt, could readers tell which is which?
To find out, I vibed up
https://sgoedecke.github.io/watermark-quiz/
, a static site that quizzes readers. I used Qwen3-30B-A3B-Instruct-2507 on a rented H200 to generate thirty responses: three responses per question, one of which was secretly watermarked with SynthID-Text. The rented GPU cost around two dollars. To measure results, I just sent users to a different page for each score, and aggregated visitors-per-page in my analytics
. This would be easily spoofable if anyone cared enough to do so, but for a casual test I think it’s acceptable.
The first round of traffic I got to the quiz (278 participants) had these slightly puzzling results:
Score
Participants
0
6
1
15
2
36
3
64
4
54
5
39
6
51
7
10
8
3
9
0
10
0
Pure random choice would lead to an average score of 3.33/10. However, the mean score here is 3.92. There is indeed a spike around 3/10, as expected, but there’s also a second weird spike at 6/10. Why is that? It turned out that the SynthID response was option A in six of the ten questions, so users who just selected the first answer for every question would get 6/10. Oops.
I re-shuffled the questions and got these results:
Score
Participants
0
1
1
3
2
14
3
21
4
20
5
11
6
2
7
1
8
0
9
0
10
0
Now the mean is 3.4/10, much closer to the expected 3.333. There’s no spike around 6. We only had 73 people take the quiz after I shuffled the questions — most people saw it and took it immediately after I posted it to my LinkedIn and Hacker News — but given the previous results, I think that’s still enough to feel confident that people were just guessing randomly.
So no,
people can’t identify the presence of AI watermarks
. Obviously this wasn’t exactly a scientific study, but it’s still pretty suggestive. If watermarks were really choosing random words that the model would never pick, you’d be able to sometimes tell from three side-by-side responses which one went down the weird watermarked road, right? I also hope that something like this can serve as a persuasive tool: if you’re worrying about what impact watermarking is going to have, and your intuition is unmoved by the mathematical explanations,
having a read
of the watermarked and unwatermarked responses might convince you that there’s really no difference in quality.
Here's a preview of a related post that shares tags with this one.
AI text watermarking is not a big deal
People are
pretty
unhappy
about Anthropic’s recent
announcement
that they’re planning to include a hidden watermark in Claude model outputs. Will this lead to a mass exodus from Anthropic models? Will the introduction of watermarking be a meaningful change for users?
No. AI text watermarking is not a big deal. It doesn’t make the text worse, it doesn’t make AI outputs more detectable in practice, it doesn’t violate user privacy, and everyone’s going to be doing it by 2027 regardless.
Continue reading...
