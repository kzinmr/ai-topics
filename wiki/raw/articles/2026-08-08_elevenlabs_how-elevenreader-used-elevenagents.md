---
title: "ElevenAgents case study: ElevenReader lifts listening by 24%"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/how-elevenreader-used-elevenagents"
scraped: "2026-08-08T06:00:32.513771+00:00"
lastmod: "2026-08-07T14:36:45.788Z"
type: "sitemap"
---

# ElevenAgents case study: ElevenReader lifts listening by 24%

**Source**: [https://elevenlabs.io/blog/how-elevenreader-used-elevenagents](https://elevenlabs.io/blog/how-elevenreader-used-elevenagents)

Blog
Product
How ElevenReader Voice Chat lifted average listening time by 24% with ElevenAgents
Written by
Christoph
Kührer
Jack
McDermott
Jake
Tennant
Published
Aug 7, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
On this page
Introduction
Why we built ElevenReader Voice Chat
How we built it
What’s next
Try it yourself
We're rolling out ElevenAgents across our business, powering interactions in operations, hiring, product, and more.
One example is
ElevenReader
Voice Chat, which we recently launched to increase user engagement by providing a more interactive reading experience. Users can talk to the same voice narrating their audiobook to ask about a character, clarify a plot point, or dig into a theme, without leaving the story.
Since launch, more than 50,000 unique users have engaged with Voice Chat across a dozen languages, and these users have shown a 24% increase in listening time. The entire experience is built on
ElevenAgents
.
Why we built ElevenReader Voice Chat
Readers often want more than narration mid-book. They want to ask a quick question, look up a fact, or get context on something they just heard, then get back to listening. Before introducing Voice Chat, ElevenReader had no way to support that. Other tools handle this narrowly. A "look this up" feature typically just opens a web search or dictionary. It answers the question but drops the reader out of the book and out of the experience.
ElevenReader Voice Chat provides an immersive experience that results in users listening more and finishing books at a higher rate. Voice Chat has all of the book's context and uses the same voice that narrates the book, so asking questions feels like talking to the narrator. Readers get their answer and drop straight back into listening. Comparing each user's listening in the month before and after their first conversation, we see a 24% increase in listening hours.
We also see a strong correlation between Voice Chat engagement and book completion rate, with book completion rate climbing to 78% for users with 5+ Voice Chat sessions.
How we built it
Voice Chat runs on ElevenLabs' native mobile agent SDKs for
Android
and
iOS
, integrated directly into the ElevenReader app. Text-based conversation is also supported, with seamless switching between voice and text. Our ElevenAgents SDK handles this out of the box, letting users keep listening to the book while chatting with the agent on the side.
The system prompt defines the agent as a reading companion. Its job is to help readers understand, enjoy, and reflect on what they are reading, and to give clear, accurate insight into storylines, characters, themes, and ideas. It helps readers make sense of what they have read or anticipate what comes next, without spoiling anything unless the reader asks.
Giving the agent context with variables
The agent's context comes from a set of variables tied to what the reader is doing at that moment: book title, description, author, a summary of the book and the current chapter, and the current paragraph. This is what lets it answer questions specific to exactly where someone is in the story, rather than giving a generic answer about the book as a whole.
Next, we are adding tool calls so the agent can control the playback experience directly, for example jumping to a chapter or resuming narration after a conversation ends.
Testing and guardrails
We implemented
guardrails
to keep the agent from going off topic. Before launch, the team tested these by actively trying to break our own guardrails inside the app.
The agent does a good job of getting back to the book when asked off-topic questions. For example, when listening to
Treasure Island:
User: “What type of fast food do you like the best?”
Agent: “Oh I don’t eat food, but I do love a good story about pirates and treasure. Want to talk more about what Jim found in that sea chest?”
In the first few days after release, we reviewed conversations by hand several times to find new ways the guardrails could be broken and to strengthen them accordingly.
Evaluating usage
Beyond the volume of conversations, we use a set of evaluation criteria to classify what each conversation is actually about: the reader's intent, the theme of the conversation, and whether it counts as a positive interaction. That combination is what lets us understand the main ways readers are using Voice Chat, not just how often.
The top query is to summarize the plot (40% of conversations), but we also get hundreds of conversations weekly on quote analysis from specific passages, which is why it is important to provide the agent context on the user’s specific location in the book.
What’s next
We see novel experiences with content and IP as a significant opportunity. Examples are already emerging elsewhere, like MasterClass letting you speak with a well-known coach to learn a skill. We expect reading and audiobooks to become far more interactive than they are today, forming deeper bonds between readers and content, authors and readers, and even characters and readers.
Try it yourself
Voice Chat is built entirely on ElevenAgents and our native mobile SDKs. If you want to build a similar experience into your own app, try out
this
template, or take a look at the
Android SDK
or
iOS SDK
.
