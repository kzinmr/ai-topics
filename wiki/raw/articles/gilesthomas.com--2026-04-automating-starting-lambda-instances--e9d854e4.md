---
title: "Automating starting Lambda Labs instances"
url: "https://www.gilesthomas.com/2026/04/automating-starting-lambda-instances"
fetched_at: 2026-04-29T07:02:02.689131+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# Automating starting Lambda Labs instances

Source: https://www.gilesthomas.com/2026/04/automating-starting-lambda-instances

Archives
Categories
Blogroll
I've been trying to get an 8x A100 instance on Lambda Labs to do a training run for my
LLM from scratch series
, but they're really busy at the moment,
and it's rare to see anything.
Thanks to the wonders of agentic coding, I spent an hour today getting something up
and running to help, which I've called
lambda-manager
.
It has three commands:
list-instance-types
, which prints which kinds of instances are available.
list-instance-type-descriptions
, which prints out all of the possible instance types (available or not)
with both their "friendly" names -- what you'd see on the website -- and the
instance type names that the API uses.
launch-when-available
, which polls the API until it sees a specified type of
instance, at which point it starts one and sends a Telegram message.
Let's see if that helps -- though it's been running for six hours now, with no luck...
