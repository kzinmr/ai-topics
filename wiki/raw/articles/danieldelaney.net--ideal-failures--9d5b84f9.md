---
title: "Ideal failures - Daniel De Laney"
url: "https://danieldelaney.net/ideal-failures/"
fetched_at: 2026-05-14T07:00:37.709317+00:00
source: "danieldelaney.net"
tags: [blog, raw]
---

# Ideal failures - Daniel De Laney

Source: https://danieldelaney.net/ideal-failures/

The way I used to design UI was to sit with paper sketches, or Figma, or a React prototype with no back end. Imagine every failure mode. Design beautiful flows for each.
I slipped into this mistake while working on
LanWhisper
, a voice dictation app. I designed for the failure modes I could imagine, drew the flows, and shipped the app. Then real users hit failure modes that I hadn’t anticipated.
For example, the AI transcription model can return hallucinated text even if the input audio is empty. I had imagined that if the model returned text at all then the app was working. This failure wasn’t in my carefully designed list of
ideal failures
. Whoops.
The problem is that a representation of a system only contains what you put into it. The failure modes it shows you are exclusively the ones you already thought of.
This is the same mistake as designing for users you’ve never talked to. Designers know that’s a trap. The same logic applies to the systems we design: imagined systems aren’t a substitute for real ones.
When designing non-trivial systems, imagination is no longer your best source of truth. The system itself is. And increasingly, designers can build it themselves. Do. Build it, instrument it, surface every piece of state. You can see and feel how the system works instead of projecting the ideal behavior onto some drawings you linked together.
Your list of ideal failure modes isn’t real.
