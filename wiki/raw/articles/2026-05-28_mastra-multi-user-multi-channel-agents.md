---
type: x_article
x_article_title: "The Rise of Multi-User, Multi-Channel Agents"
x_article_author: "Mastra"
x_article_url: "https://x.com/i/article/2059808126468243457"
getxapi: false
date: 2026-05-28
tags: [mastra, multi-agent, slack, discord, telegram, channels, harness-engineering, context-engineering, multi-user]
---

# The Rise of Multi-User, Multi-Channel Agents

An agent in 2025 was single-player: it lived in a browser, your local CLI or code editor.
Agents today are multi-player: built for Slack, Discord, etc. 
Agents are evolving from assistants into coworkers. 
So: what changes when an agent stops talking to one user 1:1 in web chat and starts talking to a room full of users, all of whom can type at once?

It turns out, a lot. 

We recently shipped channels — a new option on Mastra agents that connects them directly to platforms like Slack, Discord, and Telegram.

Along the way, we touched concurrency, attribution, permissions, memory scoping, tool approval, sandbox isolation. Every layer of the stack needed a re-think for the multi-user case.

We'll walk through Slack as the example here, but each Slack-specific detail has an analog on Discord, Telegram, and the other supported platforms.

## Getting started: connecting your agents to Slack

On the surface, the Mastra API you use to create an agent that can read/write from Slack is simple.

```typescript
const agent = new Agent({
  name: 'helper',
  model: 'openai/gpt-5-mini',
  channels: {
    adapters: {
      slack: slackAdapter,
    },
  },
});
```

Under the hood, there's a lot.

We started with Vercel's chat SDK adapters, primarily because they normalize data shape coming from each source and provides a unified set of handlers: onDirectMessage, onNewMention, onSubscribedMessage, onAction for button clicks and onReaction for emoji.

While the chat SDK handles parsing and messaging messaging shares, Mastra owns everything that gets you a working botToken and keeps you there. Again, for Slack (with equivalents on other platforms):

- **OAuth + programmatic app creation.** SlackManifestClient calls Slack's Apps Configuration API (refresh-token-based) to create the app, set scopes, and register event subscriptions.
- **Request signature verification.** HMAC-SHA256 with a 5-minute replay window, run before events reach the adapter.
- **Webhook routes.** /slack/events/:webhookId, /slack/oauth/callback, /slack/connect, etc— surfaced via provider.getRoutes() and merged into Mastra's apiRoutes.
- **Credential storage + encryption.** ChannelInstallation records in ChannelsStorage. AES + HKDF. Every credential is encrypted at rest.
- **Token rotation.** Slack rotates config tokens; onTokenRotation fires; Mastra re-encrypts and re-persists.
- **Multi-tenant adapter lifecycle.** SlackProvider keeps a Map<installationId, SlackAdapter>, restoring and re-registering on startup via __registerAdapter(..., { managesRoutes: true }).

For what it's worth, the wire protocol is uniform across platforms; but their auth model is wildly different. Slack uses HMAC + manifest API. Discord uses interactions endpoints. Telegram uses long-polling. Teams uses OAuth + bot framework.

## Managing perms / memory

Agents in your CLI are single-tenant. Agents in your Slack are multi-tenant.

The same agent is now talking to multiple users in DMs, channels, and threads concurrently — different identities, different access boundaries, different conversation histories. We have a two-tiered approach:

**Threads.** Every platform thread maps 1:1 to a Mastra thread. chatThread.id is stable per conversation (channel + thread timestamp on Slack, thread ID on Discord, chat ID on Telegram) and becomes the Mastra thread ID. Each DM, each channel thread, each top-level mention gets its own memory scope and message history.

**Resources.** The user becomes the Mastra resourceId: ${platform}:${userId} (e.g. slack:U06CK1E9HN2). Working memory is keyed by resource, so user X's context follows X across threads and stays invisible to user Y.

In multi-user threads (a Slack channel with five participants), the resourceId is bound to whoever started the thread. Everyone else's messages still land in the same Mastra thread, so the agent reads the full conversation.

The mapping to Mastra threads allow other features like input/output processors, observational memory, and tracing to work.

## Fetching prior thread context

If your agent is working in a thread, you'll want to give it context about what else is in the thread. So:

On the first non-DM mention in a thread, we call chatThread.messages and pull up to threadContext.maxMessages (default 10) prior messages from that thread.

Prepended to the user message as a single text block — not as separate user messages — because some providers reject consecutive user roles (e.g. DeepSeek).

Each line gets prefixed with the author's name and the platform message ID so the model can refer back to specific messages.

It's worth calling out that we only fetch messages from the current thread.

By default, if you tag the agent in a thread that's a reply to a top-level channel message, the agent doesn't see the channel conversation around it.

And if you reference "what we discussed in #engineering yesterday," the agent doesn't see that either.

This is somewhat by omission and somewhat on purpose. We'll probably ship a config option to grab surrounding context by default.

But we already pass the channel ID into the request context. And we're shipping fetchMessages / sendDM / postToChannel tools so the agent can pull cross-thread context (or take cross-thread action) on demand when it needs to.

**This is the difference between context engineering and harness engineering.**

Context engineering says "give the agent all the context up front." 
Harness engineering says "give it the tools to go get the context it needs."

## Surfacing what the agent is doing to users

There are three pieces: agent activity status (Thinking….), the actual message, and tool calls.

The response renders into one channel message that grows in place as the stream arrives — chatThread.post() for the first chunk, adapter.editMessage() for everything after.

Tool display. Slack renders tool calls as collapsible Block Kit cards. Platforms without rich UI fall back to text. Default: cards where supported.

## Handling human-in-the-loop tool approval

Mastra tools support approval at the tool definition itself:

```typescript
const deletePR = createTool({
  id: 'delete-pr',
  requireApproval: true,
  // ...
});
```

When the agent calls a requireApproval tool mid-run, the run suspends and waits for an approval signal.

In chat, the user has to be the one doing that — which means the channel has to render some kind of approval affordance and capture the click.

**Platforms with buttons (Slack, Discord, Telegram).** We render the approval as a card with Approve / Deny buttons. The action IDs encode the tool call: tool_approve:<toolCallId> and tool_deny:<toolCallId>.

```typescript
chat.onAction(async event => {
  if (!event.actionId.startsWith('tool_approve:') && !event.actionId.startsWith('tool_deny:')) return;
  const approved = event.actionId.startsWith('tool_approve:');
  const toolCallId = event.actionId.split(':')[1];
  // ...look up the runId, edit the card to show Approved/Denied,
  // resume via agent.approveToolCall / agent.declineToolCall.
});
```

**Platforms without buttons (WhatsApp, iMessage, etc).** There's nothing to click, so we fall back to autoResumeSuspendedTools: true on the agent stream.

The user replies in natural language — "yes" or "no". Mastra runs an LLM-as-judge call to classify the reply as approval or rejection, then resumes the suspended tool call with the structured result.

We don't make the user opt in here — AgentChannels checks each platform's resolved toolDisplay mode at runtime — if the mode can render buttons (cards, timeline, grouped, hidden), we use buttons; if it can't (text), we auto-enable autoResumeSuspendedTools for that thread. Same agent definition, different behavior per channel.

## Merging concurrent messages

In a 1:1 chat, the agent sees one message at a time. In Slack or Discord, multiple users can post into the same thread simultaneously, including mid-stream.

Treating each inbound message as a separate call to agent.stream() would produce two simultaneous runs writing to the same thread — incoherent.

The fix is our Signal API. Every inbound message calls agent.sendSignal with the potential to interrupt. "Stop" or "actually, also do X" reaches the model as a signal mid-stream.

Inbound concurrency has four modes: queue, debounce, batch, skip. AgentChannels defaults to queue (one signal at a time per thread, in order).

## Attributing messages to users

LLM APIs natively model messages as either user messages or system messages. There's no concept of multiple users.

In a multi-participant Slack thread, that means the model treats every message as "the user," even when multiple humans are sending them.

So we add two pieces of metadata bridge the gap.

Each inbound message's username is attached as a signal attribute, so the model sees who sent what alongside the text.

The agent also receives a system message describing whether it's in a 1:1 DM or a public channel.

## Routing file attachments

Different platforms handle attachments differently. 

Slack attachments are private — you need auth to fetch them, via the adapter's attachment.fetchData(). Discord attachments are public CDN URLs at attachment.url. AgentChannels tries the authenticated fetch first and falls back to the URL.

On fetch failure, the agent receives a placeholder: Attachment unavailable: <name> (<mimeType>). The model knows the file existed and can surface that to the user.

What reaches the model is decided by inlineMedia. Inline-eligible types become file parts; everything else is described as text metadata so the agent still knows the file exists. Default: image/png, image/jpeg, image/webp, application/pdf. 

Models that handle more can pass inlineMedia: ['image/*', 'video/*', 'audio/*'] or a custom predicate.

inlineLinks does the same for URLs in message text. A YouTube link becomes a video/* file part so the agent sees the content, not just the URL.

## Reconciling edited messages

Most messaging platforms (Slack, Discord, Telegram, even iMessage) let users edit a message after sending.

So what's the right behavior here — surface the final message like Slack with "(edited)"? Surface the event stream like iMessage?

We're planning a follow-up on each inbound event, diff recent platform messages against what the agent has already received, and surface the diff as a signal.

## Isolating work per thread

Mastra workspace model (which includes sandboxes and filesystems) defaults to one workspace per agent, shared across every conversation. That's fine where you're the only one talking to it.

If you've built your internal coding agent, put it in Slack, and five people are talking to it in ten different threads, you'll need ten different workspaces on a per-thread basis. With Mastra, you can do this with requestContext:

```typescript
const agent = new Agent({
  name: 'engineer-bot',
  model: 'openai/gpt-5-mini',
  channels: { adapters: { slack: slackAdapter } },
  workspace: ({ requestContext }) => {
    const channel = requestContext.get('channel');
    return new Workspace({
      // Stable per-thread sandbox identity — same thread reuses the same sandbox.
      id: `slack-${channel.threadId}`,
      sandbox: new ComputeSDKSandbox({ provider: 'e2b' }),
    });
  },
});
```

The resolver runs at tool execution time, on every tool call. AgentChannels already puts the platform context into requestContext under the channel key — platform, channelId, threadId, userId, messageId. 

The resolver pulls whatever isolation boundary the use case actually wants: thread ID for one-sandbox-per-conversation, user ID for one-sandbox-per-engineer, channel ID for one-sandbox-per-team.

Pair that with a sandbox provider that does lazy resource management (ComputeSDKSandbox wraps E2B, Daytona, Modal, Docker) and you get Devin-style fanout without exposing any sandbox infrastructure to the user.

## Conclusion

Most of the engineering above is about one shift: **multi-user agents** — humans in the same thread, sending messages concurrently, sharing state, interrupting, attributing, forking work. 

Single-user agents in 1:1 web chat are the easy version of the same problem. Multi-user agents is life on hard mode.

But if you're building an AI colleague or collaborator, the patterns above will hit you in the order they appear.

There's an easier path: use Mastra.
Try it: `npm create mastra@latest`.
