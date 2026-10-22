---
title: "Microspeak: Drain the slide, back-up slides"
url: "https://devblogs.microsoft.com/oldnewthing/20261020-00/?p=112784/"
fetched_at: 2026-10-22T10:01:03.810006+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Microspeak: Drain the slide, back-up slides

Source: https://devblogs.microsoft.com/oldnewthing/20261020-00/?p=112784/

Recall that Microspeak is not merely for jargon exclusive to Microsoft, but it’s jargon that you need to know to survive at Microsoft. Even if you don’t use it yourself, you need to know what it means when others say it.
To
drain the slide
is,
as Mark Myers explains it
, reading the contents of a slide to the audience when giving a presentation. At least at Microsoft, the term is frequently used by a speaker in the negative, such as “I don’t want to drain the slide here…”
My theory is that the phenomenon of draining the slide has multiple sources.
One is simply the result of inexperience on the part of the presenter. They don’t know what to say when giving a presentation, so they end up just reading out the text that they wrote on the slide.
A more insidious source is the result of tension between the multiple reason for creating a slide deck.
One reason to create a slide deck is to accompany a presentation. The focus of the presentation is the speaker, and the slide deck is there merely as a visual aid.
Another reason to create a slide deck is to provide a lasting record of the presentation and to serve as a reference for the future. If the topic is “How to perform process X”, then you want to make sure that all of the necessary steps are spelled out on the slides, so that you can share a link to the slide deck in the invitation for others to refer to both during the presentation but mostly for reference afterwards. People will refer back to the slides the next time they need to do process X, and they probably don’t want to have to scrub through a one-hour recording just to extract the five steps they need to follow.
Yet another reason for creating a slide deck is when presenting to a senior executive, such as for use in a
placemat review
. There is probably a standard template for the meeting, such as an “Accomplishments since the last meeting”, perhaps broken into “What’s going well”, “What’s not going well”, and followed by an “Items of future concern”. The meeting may run into a time crunch (because
they always run over
), and you may not get enough time to get through all your slides, so you want to be able to say, “You can read the rest of the slides after the meeting.” (An extreme case of this is where other teams in the placemat meeting run long and leave you with no time at all!)
A related reason for creating a slide deck is as a “proof of work”. Going into the placement review, you don’t have much to report, but you have to fill the slide. If you don’t, it looks like you haven’t done anything.
I was reminded of this last reason when I worked with a colleague to prepare our team’s weekly placemat report. My colleague would fill the slide with information, and I would recommend replacing most of the bullet points with a much more succicient summary, or just removing the items outright.
Partner Team X is considering the possibility of deploying a version that uses widgets before all of the widget features are fully implemented and rolled out to customers. They understand the consequences, such as impaired reverse widget flow. Some of these missing features will
light up
when the implementation is ready, but others will be stuck in a broken state unless explicit remediations are performed after the implementation rolls out, and a small number of features will be irreparably broken, with the only recourse being to destroy all the affected widgets and recreate them. Partner Team X has been advised of the various failure modes and how they can recover from the ones that are recoverable, and they are assessing whether they want to proceed with early deployment.
I simplified it to
Partner Team X understands the consequences of and limited recovery from using widgets in production before our work is fully implemented and deployed.
The people who are receiving this slide deck are not interested in the fine details. They want the 25-word summary of how things are going so that they can either decide that our feature is not a point of concern, or decide to ask follow-up questions to understand the issue better. In that case, we can present a so-called
back-up slide
with the details.
A
back-up slide
is a slide in a slide deck that you hope that you won’t need to use, but which you create just in case it is needed. You mark it as hidden or put it in an appendix so that it doesn’t show up in the normal presentation flow. But if the audience you are presenting to (usually someone higher up the executive chain) asks a follow-up question about one of your slides, you can reach into your deck and pull out your back-up slide to answer it. “I was ready for that question, so I already have a slide with the data you are asking for.”
Bonus PowerPoint jargon
:
PowerPoint Karaoke and the eye chart
.
