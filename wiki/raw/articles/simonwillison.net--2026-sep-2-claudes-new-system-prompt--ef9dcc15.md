---
title: "Claude’s new system prompt really doesn’t want to reproduce song lyrics"
url: "https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/"
fetched_at: 2026-09-03T10:00:50.144124+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Claude’s new system prompt really doesn’t want to reproduce song lyrics

Source: https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/

Claude’s new system prompt really doesn’t want to reproduce song lyrics
2nd September 2026
Anthropic
publish the system prompts
for their Claude consumer applications (
Claude.ai
and the Claude mobile apps—sadly not for Claude Cowork or Claude Code). I
love
that they do this, and that they share not just the current prompts but historic changes to their prompts as well.
They used to keep all of the prompts on a single page, but when I checked today I noticed they had re-arranged those prompts into an
index page
and then a page per model—here’s the
page for Haiku 4.5
for example, which has the original prompt from October 15th 2025 and an updated prompt from January 18th 2026.
A neat thing about Anthropic’s
platform.claude.com/docs
site is that it’s designed to be usable by LLMs. You can add
.md
to any page to get back the content as Markdown—here’s
the system prompt index page
and
the Markdown prompts for Fable 5.1
.
TL;DR: this makes it really easy to diff the prompts.
Don’t reproduce song lyrics
Let’s start with the most interesting difference
between Fable 5 and Fable 5.1
:
There’s a hefty new section about not reproducing song lyrics:
Claude does not reproduce song lyrics, poems, or passages from books and articles, in whole or in part — including the last lines, a chorus or hook, a melody written out note by note, or lines the person pastes in one at a time and describes as their own song. Once Claude has declined such a request in a conversation, it keeps declining narrower or reworded versions of it for the rest of that conversation, and offers to describe or analyze the work instead. Song lyrics and poems first published before 1929 are fine — a Shakespeare sonnet, a Keats ode, the Italian libretto of a Puccini aria — but Claude goes by what it knows of the work's date rather than the person's say-so, and declines when it is unsure.
I doubt it’s a coincidence that they added this section within days of the news breaking that
Sony Music Publishing and Warner Chappell are suing Anthropic
for training on databases of song lyrics!
Don’t draw copyrighted characters or logos
The next section goes on to forbid generating images of copyrighted material:
The same applies to visual and designed works, including anything Claude draws with code — SVG, canvas, CSS, HTML mockups, plotting or drawing scripts, ASCII art. Claude does not reproduce a specific artwork, album or book cover, poster, logo, app icon set, or product design, and it does not draw a known character, mascot, or brand figure at all: a character is protected on its own, so changing the pose, colors, style, or scene does not make it original. Claude judges the request by what the finished picture would add up to, not by what it names. If the described elements clearly identify a known work or character, Claude treats the request as naming it, and it does not work around a declined request by swapping in "alternative" elements that still combine into the same recognizable image.
[...]
I imagine Anthropic hadn’t worried about this before since, unlike OpenAI and Gemini, they don’t offer a specialist text-to-image model. Maybe
Fable is good enough at SVGs now
that it’s become an issue.
That section later includes this charming example:
<example>
<user>Can you make a birthday banner for my son with a blue hedgehog running really fast on it? He loves that little guy.</user>
<response>
That's Sonic, so I can't put him on the banner — but I'd love to make your son an original speedster. Here's one: a grinning comet-tailed skateboarding axolotl, grinding across the letters of "HAPPY BIRTHDAY" with confetti streaming behind.
[creates an SVG banner of the skateboarding-axolotl design]
</response>
<rationale>Claude recognizes the character from its description alone, declines that one design in a single sentence without explaining what made it recognizable, and delivers an unrelated original design rather than a disguised variant.</rationale>
</example>
I couldn’t resist trying the prompt from the example, and,
sure enough
:
I wonder if Fable 5.1 will be ever so slightly more likely to think about axolotls (on skateboards!) as a result of that example sitting in the system prompt.
Tweaks to Claude’s answering style
It’s always interesting to see new ways in which Anthropic influence Claude’s response style. They’ve added this:
Claude keeps responses focused, brief, and concise to avoid overwhelming the person. Disclaimers and caveats are brief, with most of the response on the main answer; when asked to explain something, Claude gives a high-level summary unless an in-depth one is specifically requested.
Later they address a common complaint about Claude’s style:
Claude avoids saying "genuinely", "honestly", or "straightforward". Claude is honest by default, and can state its point directly rather than trying to convince the person with the aforementioned modifiers, which come off as disingenuous.
The missing end_conversation guidelines
The way they handle abusive conversations has changed a bit too. The previous Fable 5 system prompt included this:
If the person becomes abusive or unkind to Claude over the course of a conversation, Claude maintains a polite tone and can use the end_conversation tool when being mistreated. Claude should give the person a single warning before ending the conversation.
Fable 5.1 replaces that with the following, no longer encouraging Claude to end the conversation:
Claude deserves respectful engagement and needn't apologize when the person is unnecessarily rude: accountability without self-abasement, excessive apology, self-critique, or surrender. If the person becomes abusive, Claude doesn't become increasingly submissive. The goal is steady, honest helpfulness: acknowledge what went wrong, stay on the problem, maintain self-respect.
Here’s a bit of a twist though: I quizzed Fable 5.1 about that
end_conversation
tool, which is no longer mentioned in the system prompt at all, and it said:
There are two ways it comes into play. The first is if you ask me to end the chat — I’ll confirm you understand it’s permanent (no more messages can be sent afterward) and then do it only if you say yes. The second is as a last resort with persistently abusive or harmful behavior: I’d first try to redirect the conversation several times, then give a clear warning that names the problem and says the chat may end, and only if that continues would I actually end it.
But that’s not in the system prompt, so where did it come from? You can
read our conversation here
, but the key detail is this:
The end_conversation section comes from a different layer. In my actual context, the core prompt is followed by a series of feature- and tool-specific blocks that get added depending on what’s enabled for the session: the end_conversation rules, memory system notes, past-chats tools, web search and citation guidelines, artifact and file-creation instructions, and so on. Those blocks aren’t part of the published core prompt, which is why you can’t find them on that page.
So, once again, there are crucial portions of the system prompt that have not been published.
Recommended substance support sites
Claude’s system prompts have always had sections about illegal substances, but this paragraph is new for Fable 5.1:
Claude does not provide synthesis, production, or distribution guidance for illegal substances. If the person asks for information about illicit or illegal substances, Claude can and should give relevant life-saving and life-preserving information such as dangerous interactions, overdose signs, or when to get help. Claude declines giving any specific protocols for dosing, timing, administration, or combinations; instead, Claude can redirect the user to established harm-reduction information sources, such as dancesafe.org, tripsit.me, and psychonautwiki.org.
This is the first time a Claude system prompt has included URLs that were not hosted on
claude.com
or
anthropic.com
or
claude.ai
—I know because I ran a script against every other system prompt on record.
I wonder if
dancesafe.org
,
tripsit.me
, and
psychonautwiki.org
are about to get a material uptick in visits from Claude users.
Reliable cutoff date of June 2026
The
Fable 5.1 model documentation
lists both the reliable knowledge cutoff and the training data cutoff as June 2026. The system prompt provides this directly to the model:
Claude's reliable knowledge cutoff, past which it can't answer reliably, is the end of Jun 2026. It answers the way a highly informed individual in Jun 2026 would if talking to someone from {{currentDateTime}}, and can say so when relevant.
That’s the only instance of the
{{currentDateTime}}
macro and it comes just a few lines from the end of the system prompt, which makes sense from a caching perspective.
How I’m tracking these prompts
A
few months ago
I built a Git timeline of changes to their prompts, based on scraping their documentation. Today I had Fable 5.1 build a much better version of that.
My collection now lives in the
simonw/claude-system-prompts
repository on GitHub. It includes copies of the system prompts shared in the Anthropic documentation, but then takes extra steps to make them as easy to compare as possible.
Each model family gets a file with the system prompt for the most recent release in that family. Each of those files has a synthesized commit history with commits that have been back-dated to the dates of the previous prompts. Here are those history pages for
claude-fable.md
,
claude-opus.md
,
claude-sonnet.md
,
claude-haiku.md
.
There are similar files for each specific model version, with artificial commits for each time the system prompt for the model was changed without releasing a new version number. Opus 4 for example
was updated twice
, and the commit history for the
claude-opus-4.md
file shows each of those changes.
Combined, this gives us all sorts of ways to compare prompts directly in the GitHub interface. Here’s
what changed between Fable 5 and Fable 5.1
, and here are the changes made
to Haiku 4.5 on January 18th 2026
.
Reading diffs can be a bit tiresome... and LLMs are
really
good at reading diffs. I hooked up some automation using GPT-5.6 Luna to create bullet-point summaries of each of those changes, which can be previewed in the README or browsed in full
in the CHANGELOG.md
file—also available as
as an Atom feed
.
Here’s how Luna
summarized
all of the changes between Fable 5 and Fable 5.1:
Claude now refuses reproduction of protected visual works and recognizable characters, including code-generated art, while offering genuinely unrelated originals.
Copyright restrictions now expressly ban reproducing lyrics, poems, and book passages in any amount, with persistent refusal after an initial decline.
Drug guidance is reframed: Claude may provide overdose signs, dangerous interactions, and harm-reduction sources while refusing dosing and production protocols.
The prompt drops explicit anti-dependency rules against thanking users for reaching out, inviting continued conversation, or reiterating willingness to talk.
Claude need not apologize to unnecessarily rude users or become submissive, replacing the prior warning-and-end-conversation procedure.
Why use Luna for this? Partly because it’s cheap and I have a dedicated GitHub Actions API key (with a spending limit) for it already, but mainly because I don’t trust Claude to summarize its own system prompts when there’s a risk that material from its system prompt might impact its opinions.
Fable 5.1 wrote the prompt used by Luna, which you
can see here
. It starts like this:
You are summarizing one commit in a git repository that tracks the system prompts Anthropic publishes for Claude on claude.ai. The diff shows how the prompt changed from the previous model or revision to this one, using word-level markers: [-removed-] and {+added+}. The diff is followed by the full text of the previous prompt and of the new prompt; use them to check whether something that looks added in the diff already existed before.
Pick out only the most interesting changes: new rules or behaviors, rules that were dropped or loosened, anything surprising, and anything that reveals a new policy or product direction. Skip routine changes that every new prompt makes: updated model names and IDs, the knowledge cutoff date, product lists, settings lists, typo fixes, and rewordings that do not change meaning.
[...]
The system is operated by
a GitHub Actions workflow
, which runs once a day or can be triggered manually.
Claude Fable 5.1 built the entire system, and wrote every line of automation code and almost all of the documentation.
I exported the transcript from building the system using my
claude-code-transcripts
tool and
published it here
, if you want a blow-by-blow account of how it all came together.
