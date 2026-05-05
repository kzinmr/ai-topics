---
title: "Data-driven bug finding"
url: "https://danluu.com/bugalytics/"
fetched_at: 2026-05-05T07:01:34.941480+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Data-driven bug finding

Source: https://danluu.com/bugalytics/

I can't remember the last time I went a whole day without running into a software bug
. For weeks, I couldn't invite anyone to Facebook events due to a bug that caused the invite button to not display on the invite screen. Google Maps has been giving me illegal and sometimes impossible directions ever since I moved to a small city. And Google Docs regularly hangs when I paste an image in, giving me a busy icon until I delete the image.
It's understandable that bugs escape testing. Testing is hard. Integration testing is harder. End to end testing is even harder. But there's an easier way. A third of bugs like this – bugs I run into daily – could be found automatically using analytics.
If you think finding bugs with analytics sounds odd, ask a hardware person about performance counters. Whether or not they're user accessible, every ASIC has analytics to allow designers to figure out what changes need to be made for the next generation chip. Because people look at perf counters anyway, they notice when a
forwarding path
never gets used, when
way prediction
has a strange distribution, or when the prefetch buffer never fills up.
Unexpected distributions in analytics
are a sign of a misunderstanding, which is often a sign of a bug.
Facebook logs all user actions. That can be used to determine user dead ends. Google Maps reroutes after “wrong” turns. That can be used to determine when the wrong turns are the result of bad directions. Google Docs could track all undos. That could be used to determine when users run into misfeatures or bugs.
I understand why it might feel weird to borrow hardware practices for software development. For the most part, hardware tools are decades behind software tools. As examples: current hardware tools include simulators on Linux that are only half ported from windows, resulting in some text boxes requiring forward slashes while others require backslashes; libraries that fail to compile with `default_nettype none; and components that come with support engineers because they're expected to be too buggy to work without full-time people supporting any particular use.
But when it comes to testing, hardware is way ahead of software. When I write software, fuzzing is considered a state of the art technique. But in hardware land, fuzzing doesn't have a special name. It's just testing, and why should there be a special name for "testing that uses randomness"? That's like having a name for "testing by running code". Well over a decade ago, I did
hardware testing
via a tool that used constrained randomness on inputs, symbolic execution, with state reduction via structural analysis. For small units, the tool was able to generate a formal proof of correctness. For larger units, the tool automatically generated and used coverage statistics and used them to exhaustively search over as diverse a state space as possible. In the case of a bug, a short, easy to debug, counter example would be produced. And hardware testing tools have gotten a lot better since then.
But in software land, I'm lucky if a random project I want to contribute to has tests at all. When tests exist, they're usually handwritten, with all the limitations that implies. Once in a blue moon, I'm pleasantly surprised to find that a software project uses
a test framework
which has 1% of the functionality that was standard a decade ago in chip designs.
Considering the relative cost of
hardware bugs vs. software bugs
, it's not too surprising that a lot more effort goes into hardware testing. But here's a case where there's almost no extra effort. You've already got analytics measuring the conversion rate through all sorts of user funnels. The only new idea here is that clicking on an ad or making a purchase isn't the only type of conversion you should measure. Following directions at an intersection is a conversion, not deleting an image immediately after pasting it is a conversion, and using a modal dialogue box after opening it up is a conversion.
Of course, whether it's ad click conversion rates or cache hit rates, blindly optimizing a single number will get you into a local optima that will hurt you in the long run, and setting thresholds for conversion rates that should send you an alert is nontrivial. There's a combinatorially large space of user actions, so it takes judicious use of machine learning to figure out reasonable thresholds. That's going to cost time and effort. But think of all the effort you put into optimizing clicks. You probably figured out, years ago,
that replacing boring text with giant pancake buttons gives you 3x the clickthrough rate
; you're now down to optimizing 1% here and 2% there. That's great, and it's a sign that you've captured all the low hanging fruit. But what do you think the future clickthrough rate is when a user encounters a show-stopping bug that prevents any forward progress on a modal dialogue box?
If this sounds like an awful lot of work, find a known bug that you've fixed, and grep your logs data for users who ran into that bug. Alienating those users by providing a profoundly broken product is doing a lot more to your clickthrough rate than having a hard to find checkout button, and the exact same process that led you to that gigantic checkout button can solve your other problem, too. Everyone knows that adding 200ms of load time can cause 20% of users to close the window. What do you think the effect of exposing them to a bug that takes 5,000ms of user interaction to fix is?
If that's worth fixing, pull out
scalding
,
dremel
,
cascalog
, or whatever your favorite data processing tool is. Start looking for user actions that don't make sense. Start looking for bugs.
Thanks to Pablo Torres for catching a typo in this post
