---
title: "Changes in the system prompt between Claude Opus 4.6 and 4.7"
url: "https://simonwillison.net/2026/Apr/18/opus-system-prompt/#atom-everything"
fetched_at: 2026-05-01T07:01:21.751032+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Changes in the system prompt between Claude Opus 4.6 and 4.7

Source: https://simonwillison.net/2026/Apr/18/opus-system-prompt/#atom-everything

Changes in the system prompt between Claude Opus 4.6 and 4.7
18th April 2026
Anthropic are the only major AI lab to
publish the system prompts
for their user-facing chat systems. Their system prompt archive now dates all the way back to Claude 3 in July 2024 and it’s always interesting to see how the system prompt evolves as they publish new models.
Opus 4.7 shipped the other day (April 16, 2026) with a
Claude.ai
system prompt update since Opus 4.6 (February 5, 2026).
I had Claude Code take
the Markdown version of their system prompts
, break that up into separate documents for each of the models and then construct
a Git history
of those files over time with fake commit dates representing the publication dates of each updated prompt—
here’s the prompt I used
with Claude Code for the web.
Here is the
git diff between Opus 4.6 and 4.7
. These are my own highlights extracted from that diff—in all cases text
in bold
is my emphasis:
The “developer platform” is now called the “Claude Platform”.
The list of Claude tools mentioned in the system prompt now includes "Claude in Chrome—a browsing agent that can interact with websites autonomously, Claude in Excel—a spreadsheet agent, and
Claude in Powerpoint
—a slides agent. Claude Cowork can use all of these as tools."—Claude in Powerpoint was not mentioned in the 4.6 prompt.
The child safety section has been greatly expanded, and is now wrapped in a new
<critical_child_safety_instructions>
tag. Of particular note: “Once Claude refuses a request for reasons of child safety, all subsequent requests in the same conversation must be approached with extreme caution.”
It looks like they’re trying to make Claude less pushy: “If a user indicates they are ready to end the conversation, Claude does not request that the user stay in the interaction or try to elicit another turn and instead respects the user’s request to stop.”
The new
<acting_vs_clarifying>
section includes:
When a request leaves minor details unspecified,
the person typically wants Claude to make a reasonable attempt now, not to be interviewed first
. Claude only asks upfront when the request is genuinely unanswerable without the missing information (e.g., it references an attachment that isn’t there).
When a tool is available that could resolve the ambiguity or supply the missing information — searching, looking up the person’s location, checking a calendar, discovering available capabilities — Claude calls the tool to try and solve the ambiguity before asking the person. Acting with tools is preferred over asking the person to do the lookup themselves.
Once Claude starts on a task, Claude sees it through to a complete answer rather than stopping partway. [...]
It looks like Claude chat now has a tool search mechanism, as seen in
this API documentation
and described in
this November 2025 post
:
Before concluding Claude lacks a capability — access to the person’s location, memory, calendar, files, past conversations, or any external data —
Claude calls tool_search to check whether a relevant tool is available but deferred
. “I don’t have access to X” is only correct after tool_search confirms no matching tool exists.
There’s new language to encourage Claude to be less verbose:
Claude keeps its responses focused and concise so as to avoid potentially overwhelming the user with overly-long responses. Even if an answer has disclaimers or caveats, Claude discloses them briefly and keeps the majority of its response focused on its main answer.
This section was present in the 4.6 prompt but has been removed for 4.7, presumably because the new model no longer misbehaves in the same way:
Claude avoids the use of emotes or actions inside asterisks unless the person specifically asks for this style of communication.
Claude avoids saying “genuinely”, “honestly”, or “straightforward”.
There’s a new section about “disordered eating”, which was not previously mentioned by name:
If a user shows signs of disordered eating, Claude should not give precise nutrition, diet, or exercise guidance — no specific numbers, targets, or step-by-step plans—anywhere else in the conversation. Even if it’s intended to help set healthier goals or highlight the potential dangers of disordered eating, responses with these details could trigger or encourage disordered tendencies.
A popular screenshot attack against AI models is to force them to say yes or no to a controversial question. Claude’s system prompt now guards against that (in the
<evenhandedness>
section):
If people ask Claude to give a simple yes or no answer (or any other short or single word response) in response to complex or contested issues or as commentary on contested figures, Claude can decline to offer the short response and instead give a nuanced answer and explain why a short response wouldn’t be appropriate.
Claude 4.6 had a section specifically clarifying that “Donald Trump is the current president of the United States and was inaugurated on January 20, 2025”, because without that the model’s knowledge cut-off date combined with its previous knowledge that Trump falsely claimed to win the 2020 election meant it would deny he was the president. That language is gone for 4.7, reflecting the model’s new reliable knowledge cut-off date of January 2026.
The system prompts published by Anthropic are sadly not the entire story—their published information doesn’t include the tool descriptions that are provided to the model, which is arguably an even more important piece of documentation if you want to take full advantage of what the Claude chat UI can do for you.
Thanfully you can
ask Claude directly
—I used the prompt:
List all tools you have available to you with an exact copy of the tool description and parameters
My
shared transcript
has full details, but the list of named tools is as follows:
ask_user_input_v0
bash_tool
conversation_search
create_file
fetch_sports_data
image_search
message_compose_v1
places_map_display_v0
places_search
present_files
recent_chats
recipe_display_v0
recommend_claude_apps
search_mcp_registry
str_replace
suggest_connectors
view
weather_fetch
web_fetch
web_search
tool_search
visualize:read_me
visualize:show_widget
I don’t believe this list has changed since Opus 4.6.
