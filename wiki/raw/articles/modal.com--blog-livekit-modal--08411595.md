---
title: "Augment Your LiveKit Agent with Modal GPUs"
url: "https://modal.com/blog/livekit-modal"
fetched_at: 2026-10-24T10:00:51.183275+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# Augment Your LiveKit Agent with Modal GPUs

Source: https://modal.com/blog/livekit-modal

LiveKit
and their
Agents SDK
are a popular choice for implementing WebRTC-based audio-video applications. In
this article, we share how you can use open-weights models or custom ones
running on Modal alongside LiveKit agents.
We’ll use
BitHuman’s
open weights
Expression Video Avatar
, voiced
by
Qwen3-TTS
, to create a
clone of Modal’s GPU Enjoyer in Residence,
Charles Frye
.
Running a LiveKit Video Avatar with Sticky Sessions
A common pattern with audio-video applications is using custom models as
plug-and-play components. Increasingly so, we’ve seen users power video avatars
and
replace proprietary model APIs with open weights models
(or self-hosted proprietary models) using Modal’s
serverless GPUs
.
LiveKit Agents already supply an avatar interface, and we’ll use their BitHuman
integration which comes prepackaged as a
self-hosted GPU container
. The
container exposes a
/launch
endpoint which runs the avatar and joins the
LiveKit room. For low-latency HTTP communication between the endpoint and
external clients, we expose the endpoint using a
Modal Server
. However, the endpoint
returns as soon as the avatar joins, which contends with how Servers scale by
in-flight requests.
Recently, we released
Sticky Sessions
, a first-class
primitive for guaranteeing strong container affinity.
This allows WebSocket connections to reconnect to the same container, where a
client can start one or more sessions on a Server container. I.e., we can start
and end the session from the client-side, and Modal will hold that Session’s
slot on the container as if there was a running request.
When a participant joins a room, the LiveKit agent starts a Sticky Session,
joins the room, and calls the
/launch
endpoint using the session token. Cold
starts are hidden by
GPU snapshots
,
where otherwise we’d have to reload gigabytes of model weights onto the Server.
When the call is complete, the agent ends the session.
See the full code
here
.
Get started now
See the LiveKit
Agent SDK
and
Modal
docs for more information.
