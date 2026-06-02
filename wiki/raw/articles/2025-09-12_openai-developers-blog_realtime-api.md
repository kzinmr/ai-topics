---
title: "Developer notes on the Realtime API"
url: "https://developers.openai.com/blog/realtime-api/"
date: "2025-09-12"
source: "OpenAI Developers Blog"
tags: ["openai", "developer-blog", "realtime-api", "voice", "speech", "agents", "mcp", "responses-api", "audio", "compaction"]
---

# Developer notes on the Realtime API

We recently announced our latest speech-to-speech
model, gpt-realtime, in addition to the general availability of the Realtime API and
a bunch of new API features. The Realtime API and speech-to-speech (s2s) model graduated to general availability (GA) with major improvements in model quality, reliability, and developer ergonomics.

gpt-realtime

While you can discover the new API features in
the docs and API reference, we want to highlight a few you may have missed and provide guidance on when to use them.
If you’re integrating with the Realtime API, we hope you’ll find these notes interesting.

## Model improvements

The new model includes a number of improvements meant to better support production voice apps. We’re
focusing on API changes in this post. To better understand and use the model, we recommend the announcement blog post and
realtime prompting guide. However, we’ll point out some specifics.

A few key pieces of advice for using this model:

Experiment with prompting in the realtime playground.
Use the marin or cedar voices for best assistant voice quality.
Rewrite prompts for the new model. Due to instruction-following improvements, specific instructions are now much more powerful.

For example, a prompt that said, “Always say X when Y,” may have been treated by the old model as vague guidance, whereas the new the model may adhere to it in unexpected situations.
Pay attention to the specific instructions you’re providing. Assume instructions will be followed.

- Experiment with prompting in the realtime playground.

- Use the marin or cedar voices for best assistant voice quality.

marin

cedar

- Rewrite prompts for the new model. Due to instruction-following improvements, specific instructions are now much more powerful.

For example, a prompt that said, “Always say X when Y,” may have been treated by the old model as vague guidance, whereas the new the model may adhere to it in unexpected situations.
Pay attention to the specific instructions you’re providing. Assume instructions will be followed.

For example, a prompt that said, “Always say X when Y,” may have been treated by the old model as vague guidance, whereas the new the model may adhere to it in unexpected situations.
Pay attention to the specific instructions you’re providing. Assume instructions will be followed.

- For example, a prompt that said, “Always say X when Y,” may have been treated by the old model as vague guidance, whereas the new the model may adhere to it in unexpected situations.

- Pay attention to the specific instructions you’re providing. Assume instructions will be followed.

## API shape changes

We updated the Realtime API shape with the GA launch, meaning there’s a beta interface and a GA interface. We recommend that clients migrate to integrate against the GA interface, as it gives new features, and the beta interface will eventually be deprecated.

A complete list of the changes needed for migration can be found in the beta to GA migration docs.

You can access the new gpt-realtime model with the beta interface, but certain features may be unsupported. See below for more details.

gpt-realtime

### Feature availability

The Realtime API GA release includes a number of new features. Some of these are enabled on older models, and some are not.

*Because the beta model lacks async function calling, pending MCP tool calls without an output may not be treated well by the model. We recommend using the GA model with MCP.

### Changes to temperature

The GA interface has removed temperature as a model parameter, and the beta interface limits
temperature to a range of 0.6 - 1.2 with a default of 0.8.

temperature

0.6 - 1.2

0.8

You may be asking, “Why can’t users set temperature arbitrarily and use it for things like making the response more
deterministic?” The answer is that temperature behaves differently for this model architecture, and users are nearly always best served by setting temperature to the recommended 0.8.

0.8

From what we’ve observed, there isn’t a way to make these audio responses deterministic with low temperatures, and higher
temperatures result in audio abberations. We recommend experimenting with prompting to control
these dimensions of model behavior.

## New features

In addition to the changes from beta to GA, we’ve added several new features to the Realtime API.

All features are covered in the docs and API reference, but here we’ll highlight how to think about new features as you integrate and migrate.

### Conversation idle timeouts

For some applications, it’d be unexpected to have a long gap of input from the user. Imagine a phone call—if we didn’t hear from the person on the other line, we’d ask about their status. Maybe the model missed what the user said, or maybe the user isn’t sure if the model is still speaking. We’ve added a feature to automatically trigger the model to say something like: “Are you still there?”

Enable this feature by setting idle_timeout_ms on the server_vad settings for turn detection.
The timeout value will be applied after the last model response’s audio has finished playing—
i.e., timeout value is set to the response.done time plus audio playback duration plus timeout time. If VAD does not fire for that period, the timeout is triggered.

idle_timeout_ms

server_vad

response.done

When the timeout is triggered, the server sends an input_audio_buffer.timeout_triggered event, which then commits the empty audio segment to the conversation history and triggers a model response.
Committing the empty audio gives the model a chance to check whether VAD failed and there was a user utterance
during the relevant period.

input_audio_buffer.timeout_triggered

Clients can enable this feature like so:

```
{
  "type": "session.update",
  "session": {
    "type": "realtime",
    "instructions": "You are a helpful assistant.",
    "audio": {
      "input": {
        "turn_detection": {
          "type": "server_vad",
          "idle_timeout_ms": 6000
        }
      }
    }
  }
}
```

{
  "type": "session.update",
  "session": {
    "type": "realtime",
    "instructions": "You are a helpful assistant.",
    "audio": {
      "input": {
        "turn_detection": {
          "type": "server_vad",
          "idle_timeout_ms": 6000
        }
      }
    }
  }
}

### Long conversations and context handling

We’ve tweaked how the Realtime API handles long sessions. A few things to keep in mind:

Realtime sessions can now last up to 60 minutes, up from 30 minutes.
The gpt-realtime model has a token window of 32,768 tokens. Responses can consume a maximum of 4,096 tokens. This means the model has a maximum input of 28,672 tokens.
The session instructions plus tools can have a maximum length of 16,384 tokens.
The service will automatically truncate (drop) messages when the session reaches 28,672 tokens, but this is configurable.
The GA service will automatically drop some audio tokens when a transcript is available to save tokens.

- Realtime sessions can now last up to 60 minutes, up from 30 minutes.

- The gpt-realtime model has a token window of 32,768 tokens. Responses can consume a maximum of 4,096 tokens. This means the model has a maximum input of 28,672 tokens.

gpt-realtime

- The session instructions plus tools can have a maximum length of 16,384 tokens.

- The service will automatically truncate (drop) messages when the session reaches 28,672 tokens, but this is configurable.

- The GA service will automatically drop some audio tokens when a transcript is available to save tokens.

#### Configuring truncation settings

What happens when the conversation context window fills up to the token limit is that after the limit is reached, the Realtime API
automatically starts truncating (dropping) messages from the beginning of the session (the oldest messages).
You can disable this truncation behavior by setting "truncation": "disabled", which instead throws an error
when a response has too many input tokens. Truncation is useful, however, because the session continues even if the input size grows too large for the model. The Realtime API doesn’t do summarization or compaction of dropped messages, but you can implement it on your own.

"truncation": "disabled"

A negative effect of truncation is that changing messages at the beginning of the conversation busts the token prompt cache. Prompt caching works by identifying identical, exact-match content prefixing your prompts. On each subsequent turn, only the tokens that haven’t changed are cached. When truncation alters the beginning of the conversation, it reduces the number of tokens that can be cached.

We’ve implemented a feature to mitigate this negative effect by truncating more than necessary whenever truncation occurs. Set retention ratio
to 0.8 to truncate 20% of the context window rather than truncating just enough to keep the input
token count under the ceiling. The idea is to truncate more of the context window once, rather than truncating a little bit every time, so you bust the cache less often. This cache-friendly approach can keep costs down for long sessions that reach input limits.

0.8

```
{
  "type": "session.update",
  "session": {
    "truncation": {
      "type": "retention_ratio",
      "retention_ratio": 0.8
    }
  }
}
```

{
  "type": "session.update",
  "session": {
    "truncation": {
      "type": "retention_ratio",
      "retention_ratio": 0.8
    }
  }
}

### Asynchronous function calling

Whereas the Responses API forces a function response immediately after the function call, the Realtime API allows clients to continue a session while a function call is pending. This continuation is good for UX, allowing realtime conversations to continue naturally, but the model sometimes hallucinates the content of a nonexistent function response.

To mitigate this issue, the GA Responses API adds placeholder responses with content we’ve evaluated and tuned in experiments to ensure the model performs gracefully, even while awaiting a function response. If you ask the model for the results of a function call, it’ll say something like, “I’m still waiting on that.” This feature is automatically enabled for new models—no changes necessary on your end.

### EU data residency

EU data residency is now supported specifically for the gpt-realtime-2025-08-28 and gpt-4o-realtime-preview-2025-06-03. Data residency must be explicitly enabled for an organization and accessed through https://eu.api.openai.com.

gpt-realtime-2025-08-28

gpt-4o-realtime-preview-2025-06-03

https://eu.api.openai.com

### Tracing

The Realtime API logs traces to the developer console, recording key events during a realtime session, which can be helpful for investigations and debugging. As part of GA, we launched a few new event types:

Session updated (when session.updated events are sent to the client)
Output text generation (for text generated by the model)

- Session updated (when session.updated events are sent to the client)

session.updated

- Output text generation (for text generated by the model)

### Hosted prompts

You can now use prompts with the Realtime API as a convenient way to have your application code
refer to a prompt that can be edited separately. Prompts include both instructions and
session configuration, such as turn detection settings.

You can create a prompt in the realtime playground, iterating on it and versioning it as needed, and then a client can reference that prompt by ID, like so:

```
{
  "type": "session.update",
  "session": {
    "type": "realtime",
    "prompt": {
      "id": "pmpt_123", // your stored prompt ID
      "version": "89", // optional: pin a specific version
      "variables": {
        "city": "Paris" // example variable used by your prompt
      }
    },
    // You can still set direct session fields; these override prompt fields if they overlap:
    "instructions": "Speak clearly and briefly. Confirm understanding before taking actions."
  }
}
```

{
  "type": "session.update",
  "session": {
    "type": "realtime",
    "prompt": {
      "id": "pmpt_123", // your stored prompt ID
      "version": "89", // optional: pin a specific version
      "variables": {
        "city": "Paris" // example variable used by your prompt
      }
    },
    // You can still set direct session fields; these override prompt fields if they overlap:
    "instructions": "Speak clearly and briefly. Confirm understanding before taking actions."
  }
}

If a prompt setting overlaps with other configuration passed to the session, as
in the example above, the session configuration takes precedence, so a client can either
use the prompt’s config or manipulate it at session time.

### Sideband connections

The Realtime API allows clients to connect directly to the API server via WebRTC or SIP. However, you’ll most likely want tool use and other business logic to reside on your application server to keep this logic private and client-agnostic.

Keep tool use, business logic, and other details secure on the server side by connecting over a sideband control channel. We now have sideband options for both SIP and WebRTC connections.

A sideband connection means there are two active connections to the same realtime session: one from the user’s client and one from your application server. The server connection can be used to monitor the session, update instructions, and respond to tool calls.

For more information, see documentation for sideband connections.

## Start building

We hope this was a helpful way to understand what’s changed with the generally available Realtime API and new realtime models.

Now that you have the updated framing, see the realtime docs to build a voice agent, start a connection, or start prompting realtime models.
