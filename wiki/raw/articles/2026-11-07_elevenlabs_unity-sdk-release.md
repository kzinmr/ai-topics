---
title: "Add a voice agent to your Unity game with ElevenAgents"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/unity-sdk-release"
scraped: "2026-11-07T06:00:42.822967+00:00"
lastmod: "2026-11-06T15:37:20.306Z"
type: "sitemap"
---

# Add a voice agent to your Unity game with ElevenAgents

**Source**: [https://elevenlabs.io/blog/unity-sdk-release](https://elevenlabs.io/blog/unity-sdk-release)

Blog
Product
Give your Unity NPCs a voice with ElevenAgents
Written by
Tadas
Petra
Published
Nov 5, 2026
Last updated
Nov 6, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
View on GitHub
Read the docs
On this page
Introduction
Start a conversation
What's in the SDK
Platform support
Get started
Players can now walk up to a character in your Unity game and talk to them out loud. The new ElevenAgents Unity SDK connects a scene to an ElevenLabs voice agent. It listens through the player's microphone, plays the agent's voice through an
AudioSource
, and runs the session through the
Conversation
API.
The same code runs in the Editor, desktop builds, and WebGL, and iOS, Android, and XR are in beta.
Start a conversation
A session needs the ID of an agent you've created in the ElevenLabs dashboard, which holds the prompt and the voice. In our
GettingStarted sample
, included with the SDK, a trigger collider around the character opens the session when the player walks in and closes it when they walk out:
private Conversation activeConversation;

private void OnTriggerEnter(Collider other)
=>
_ = StartTalkingAsync();
private void OnTriggerExit(Collider other)
=>
_ = StopTalkingAsync();

private async Awaitable StartTalkingAsync()
{
var
options = new ConversationOptions { AgentId = agentId };
    activeConversation =
await
Conversation.StartSessionAsync(options);
}

private async Awaitable StopTalkingAsync()
{
if
(activeConversation ==
null
)
return
;
await
activeConversation.EndSession();
    activeConversation =
null
;
}
StartSessionAsync
returns once the connection is open and the audio devices are ready, and it picks the right transport for the build target.
EndSession
does nothing if the session has already ended.
What's in the SDK
Voices that come from the character
By default the agent's voice plays in 2D. Pass your own
AudioSource
as
OutputAudioSource
and the voice comes from the character instead.
GetOutputVolume()
returns the agent's current level from 0 to 1 on every platform. The sample uses it to make the cube bob while it talks, and it can drive a mouth animation the same way.
One agent, many characters
Dynamic variables fill placeholders like
{{mood}}
in the agent's prompt and first message, so each character can send its own values when its session starts. Values can be strings, numbers, or booleans. In the sample, a yellow happy cube and a red angry cube share one agent:
var
options = new ConversationOptions
{
    AgentId = agentId,
    OutputAudioSource = audioSource,
    DynamicVariables = new Dictionary<string, object>
    {
        [
"color"
] =
"red"
,
        [
"mood"
] =
"angry"
,
    },
};
For bigger changes,
Overrides
replace part of the agent's configuration for one session, such as the first message or the voice. Each override has to be turned on in the agent's
Security
settings first.
Characters that know what's happening
SendContextualUpdate
tells the agent about game events mid-conversation, without interrupting it or adding a turn the player didn't say:
activeConversation.SendContextualUpdate(
"The player picked up the cellar key."
);
Characters that act in the game
Client tools
let the agent trigger game code. Define the tool in the agent's settings, then register a handler under the same name:
activeConversation.RegisterTool<OpenDoorParams,
string
>(
"open_door"
,
parameters
=>
{
    DoorRegistry.Open(parameters.
DoorId
);
return
$
"Door {parameters.DoorId} is open."
;
});
The SDK deserializes the tool's parameters with Newtonsoft Json and sends whatever the handler returns back to the agent. Handlers can return an
Awaitable
for work that takes time, and throw a
ClientToolException
to tell the agent why something failed.
Events and controls
Events such as
UserTranscriptReceived
,
AgentResponded
,
ModeChanged
, and
Interrupted
fire on Unity's main thread, so you can update UI straight from them. Methods cover text input with
SendUserMessage
, muting with
SetMicMuted
,
SetVolume
, frequency data for visualizers, and switching input or output devices mid-session. The
Unity SDK docs
list them all.
Platform support
The SDK picks the transport for each target.
Platform
Status
Transport
Editor and desktop (macOS, Windows, Linux)
Supported
WebSocket
WebGL
Supported
WebSocket or WebRTC
iOS, Android, XR
Beta
WebSocket
iOS and Android:
request microphone permission before you start a session.
WebGL:
turn on
Use WebAssembly.Table
in
Publishing Settings
. The SDK fails the build with instructions if it's off. Play Mode doesn't work while WebGL is the active build target, so test on a desktop target.
WebGL audio:
the voice plays through the Web Audio API, so some
AudioSource
settings, like mixer routing and doppler, don't carry over. WebRTC sessions ignore
OutputAudioSource
.
The
compatibility notes
have the full list.
Get started
Create an agent
in the ElevenLabs dashboard. For a first test, turn off
Authentication
in its
Security
settings, so the game can connect with the agent ID alone.
In Unity, open
Window
>
Package Manager
>
+
>
Install package from git URL
, and pin the release:
https://github.com/elevenlabs/unity.git#v0.1.0
Import the GettingStarted sample, paste in your agent ID, and press Play.
Warning:
Before you ship, turn
Authentication
back on. Your own server then requests a short-lived
signed URL
, and the game passes it as
SignedUrl
instead of
AgentId
. Never put your ElevenLabs API key in a game build.
The
getting started walkthrough
takes about 10 minutes and ends with a cube that greets you when you walk up. For everything else, read the
Unity SDK docs
, and send bugs and feature requests to
GitHub issues
.
Written by
Tadas Petra
View profile
Tadas is a Developer Relations Engineer helping developers build with ElevenLabs product suite. Before he was a founder of a developer education platform, a Lead Developer Advocate at Agora, an instructor at Zero To Mastery, and built an audience on YouTube teaching developers.
