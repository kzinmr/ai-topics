---
title: "Issues with Google's Bug Prediction Algorithm"
url: "https://boyter.org/2015/07/issues-googles-bug-prediction-algorithm/"
fetched_at: 2026-05-05T07:02:02.132842+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Issues with Google's Bug Prediction Algorithm

Source: https://boyter.org/2015/07/issues-googles-bug-prediction-algorithm/

December 2011 the Google Engineering team published a blog post about
bug prediction at Google
. The topic caused quite a lot of discussion at the time over the internet on forums such as Hacker News and the Reddit programming sub-reddit.
How bug prediction works
In a nutshell the prediction works by ranking files against checking the file commit history and seeing how many changes have been flagged as bug fixes. Of course this means that code which was previously buggy will still appear in the list. This issue was also addressed in the post and the results were weighted over time to deal with this issue.
Issues with bug prediction
Since that time the topic has been reposted a few times and we have since discovered that the system has been discontinued at Google. Thankfully the author of the original post was able to respond and has given one of the
main reasons why it was discontinued
.
TL;DR is that developers just didn’t find it useful. Sometimes they knew the code was a hot spot, sometimes they didn’t. But knowing that the code was a hot spot didn’t provide them with any means of effecting change for the better. Imagine a compiler that just said “Hey, I think this code you just wrote is probably buggy” but then didn’t tell you where, and even if you knew and fixed it, would still say it due to the fact it was maybe buggy recently. That’s what TWR essentially does. That became understandably frustrating, and we have many other signals that developers can act on (e.g. FindBugs), and we risked drowning out those useful signals with this one.
Some teams did find it useful for getting individual team reports so they could focus on places for refactoring efforts, but from a global perspective, it just seemed to frustrate, so it was turned down.
From an academic perspective, I consider the paper one of my most impactful contributions, because it highlights to the bug prediction community some harsh realities that need to be overcome for bug prediction to be useful to humans. So I think the whole project was quite successful… Note that the Rahman algorithm that TWR was based on did pretty well in developer reviews at finding bad code, so it’s possible it could be used for automated tools effectively, e.g. test case prioritization so you can find failures earlier in the test suite. I think automated uses are probably the most fruitful area for bug prediction efforts to focus on in the near-to-mid future.
Another paper released which analyses the results of the Google bug predictor can be found
Does Bug Prediction Support Human Developers? Findings From a Google Case Study (PDF)
.
Another interesting thought is that the system requires a reasonably amount of code comment discipline. Some people and teams use bug fix commit’s to resolve feature requests. The result is that this system would mark actively developed code as being a bug hot spot. In this case being a poorly organised team or individual would not see their code appear. This is especially problematic where performance is being measured against these sort of metrics.
If you are interested in trying this yourself there are some open source implementations of the algorithms presented in the Google Paper. See
bugspots in github
as an example of one which will work against any git repository.
