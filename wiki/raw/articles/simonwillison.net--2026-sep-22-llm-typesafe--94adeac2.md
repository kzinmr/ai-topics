---
title: "llm-typesafe 0.1a0"
url: "https://simonwillison.net/2026/Sep/22/llm-typesafe/"
fetched_at: 2026-09-23T10:01:02.264772+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# llm-typesafe 0.1a0

Source: https://simonwillison.net/2026/Sep/22/llm-typesafe/

I built this new plugin for
LLM
to add support for
TypeSafe AI's new Jev model
. Install it like this:
llm install llm-typesafe
Then set an API key (
get one here
, the waitlist seems to move pretty fast):
llm keys set typesafe
# Paste key
And now you can ask yes/no "noul" questions like this:
llm -m jev 'Please refund my last payment.' \
  -s 'Does this message explicitly request a refund?'
Output:
{"type": "noul", "noul": 0.99}
Or choice questions like this:
cat message.txt
|
llm -m jev \
  -s
'
Which team should handle this message? If billing and technical issues both occur, choose billing.
'
\
  -o answer_type choice \
  -o criteria
'
{
"billing":"Charges, invoices, payments, or refunds",
"technical":"Problems installing or using the product",
"other":"Neither category fits"
}
'
Or scoring questions like this:
cat report.txt
|
llm -m jev \
  -s
'
How reproducible is the problem described in this report?
'
\
  -o answer_type score \
  -o criteria
'
[
"No reproduction instructions",
"Some instructions, but important steps are missing",
"Complete steps with expected and actual results"
]
'
See
the README
for more details.
