---
title: "Passive Voice Considered Harmful"
url: "https://refactoringenglish.com/chapters/passive-voice-considered-harmful/"
fetched_at: 2026-05-01T07:01:25.708886+00:00
source: "refactoringenglish.com"
tags: [blog, raw]
---

# Passive Voice Considered Harmful

Source: https://refactoringenglish.com/chapters/passive-voice-considered-harmful/

Your high school English teachers probably warned you that passive voice is dangerous and forbidden. Then, when you were an adult, some guy in a leather jacket told you that passive voice is cool and should be used whenever it’s desired.
Well, the tide has turned again. If you’re a software developer, stop using the passive voice.
Wait, what’s passive voice?
🔗
In English, sentences can have one of two structures: passive voice or active voice.
Active voice is when you construct a sentence as “actor → verb → object.”
Active voice
Jane
tested
the new chat feature.
Passive voice is when you construct a sentence as “object → verb → actor.”
Passive voice
The new chat feature
was tested
by
Jane.
Passive voice also allows you to construct the sentence as “object → verb” with no actor at all.
Passive voice (omiting actor)
The new chat feature
was tested.
Recognizing passive voice
🔗
You can recognize passive voice from two signature features:
A form of the verb “to be” (e.g., is, was, will be)
The past participle of a verb (e.g., downloaded, tested)
Here are a few examples:
Passive voice structure
The product launch
is
canceled.
The developer responsible
was
identified.
Their employment
has been
terminated.
A replacement
will be
chosen.
What’s wrong with passive voice?
🔗
If you forgot what passive voice is, you definitely forgot why you’re not supposed to use it.
You may have a hazy recollection that passive voice is grammatically incorrect (it’s not). Maybe you recall teachers telling you that passive voice is “poor style,” but that’s vague and hand-wavey.
Regardless of what you remember, there are clear, concrete reasons to avoid the passive voice.
Passive voice omits important information
🔗
Passive voice’s greatest sin is that it omits critical information.
When I review design documents, I often find lines like this:
For security, the message is signed, and the signature is validated before further processing.
That sentence creates a lot of questions:
Who signs the message?
Who validates the message?
Who performs further processing?
Here’s a rewrite of that sentence using the active voice:
For security, the client signs the message using the client private key. The client then sends the meessage to the orchestration server.
When the orchestration server receives the message, it forwards the message to the authentication service. The authentication service then validates the message’s signature.
If the authentication service successfully validates the message’s signature, the orchestration server sends the message to the queuing service.
If the authentication service rejects the message, the orchestration server drops the message and responds to the client with an HTTP 400 error.
If the authentication service fails to respond within 5 seconds, the orchestration server drops the message and responds to the client with an HTTP 500 error.
“Hang on!” You might be thinking. “That wasn’t a rewrite to the active voice. That’s completely different text.”
But that’s exactly the point.
Passive voice draws the reader’s attention away from missing information, like a magician using misdirection. Converting a sentence to active voice exposes missing details.
You’ll often find that converting a sentence from passive voice to active voice reveals gaps in your thinking or designs.
Passive voice increases cognitive load for the reader
🔗
Most English sentences take the form of actor → verb → object. This structure is familiar to the reader, and it allows them to parse the sentence easily.
Passive voice inverts the typical sentence structure, which adds mental burden for the reader. When they see a verb before seeing its corresponding actor, they effectively have to push it onto their memory stack and then mentally reconfigure the concept into “actor → verb → object” order.
You’re allowed to challenge the reader, but save it for when you have a difficult topic to explain, not when you want to use a particular sentence structure.
When is passive voice useful?
🔗
Despite all the reasons not to use passive voice, there are a few cases where it’s acceptable and, I’ll admit: helpful.
As a rule of thumb, whenever you encounter passive voice in your writing, consider a rewrite. But also consider the possibility that, in certain cases, passive voice’s benefits outweigh its costs.
Use passive voice to focus on solutions rather than assigning blame
🔗
When you discuss problems with teammates, it’s important to focus on solving the problem rather than pointing fingers.
Imagine that you were performing a postmortem on a website outage, and you included this sentence:
Michael accidentally shut down
the production server, which caused a three-hour outage on our website.
The phrasing leads the reader to believe that Michael is the problem. If Michael hadn’t been so stupid and careless, the outage would never have happened.
Here’s a rewrite in the passive voice:
The production server
was accidentally shut down
, which caused a three-hour outage on our website.
The passive voice shifts focus away from the individual and leads the reader’s attention to the systems that allowed the problem:
Why should there be an outage if one server shuts down?
Why is it possible to shut down a critical server by mistake?
Why does it take three hours to get a critical server back online?
These questions are likely to yield more robust systems than simply blaming the issue on one person’s carelessness.
Use passive voice to communicate mistakes tactfully
🔗
I find passive voice effective in pointing out someone’s mistake in a friendly, professional way, especially if I don’t know the person well.
For example, if a customer forgot to include their logs with a bug report, this would be a particularly hostile way of letting them know:
It looks like
you ignored my instructions
and
failed to include the log file
in your bug report.
Instead, I would use the passive voice to avoid sounding accusatory:
It looks like
the log file was accidentally omitted
from the bug report. Could you try reattaching your log file and emailing it to me?
Use passive voice to exclude irrelevant details
🔗
Passive voice omits details, but sometimes that’s what you want. Some details are irrelevant and deserve omission.
I
was fired
from my last job for bringing my pet puma to work.
The sentence above uses passive voice to omit details, but that’s okay.
Maybe the person who fired you was named Gary, and he was a junior HR associate. He dreamt of winning the national Scrabble championship, and his favorite color was purple.
The reader doesn’t care about Gary.
They care about why you have a pet puma, why you thought it was a good idea to bring it to work, and what happened when you did. In that case, it’s perfectly acceptable to use passive voice to edit Gary out of your story.
Practice recognizing the passive voice
🔗
When I’ve campaigned to teammates about the evils of passive voice, they usually agree that passive voice creates problems, but they struggle to recognize it in their writing.
To help readers who have difficulty identifying the passive voice, I created a short exercise to test your ability to identify the passive voice:
