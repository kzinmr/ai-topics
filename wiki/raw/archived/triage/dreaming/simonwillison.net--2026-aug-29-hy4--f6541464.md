---
title: "Introducing Hy4 Preview"
url: "https://simonwillison.net/2026/Aug/29/hy4/"
fetched_at: 2026-08-30T10:01:00.075005+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Introducing Hy4 Preview

Source: https://simonwillison.net/2026/Aug/29/hy4/

29th August 2026 - Link Blog
Introducing Hy4 Preview
. New open weight text input (no vision)  LLM from Chinese company Tencent today: 770B total parameters, 49B active parameters, 1M token context window,
1.56TB on Hugging Face
.
This is a big size increase from their previous
Hy3
in July, which was 295B, 21B active, 256,000 context, 598GB.
I recently started using model chat templates to better understand their capabilities. Here's Hy4's
chat_template.jinja
on Hugging Face, which includes this section:
{%
-
if
not
reasoning_effort
is
defined
%}
{%
-
set
reasoning_effort
=
'high'
%}
{%
-
elif
reasoning_effort
not
in
[
'high'
,
'no_think'
]
%}
{%
-
if
reasoning_effort
is
none
%}
{{- raise_exception('reasoning_effort error : None, should be no_think/high') }}
{%
-
else
%}
{{- raise_exception('reasoning_effort error : ' + reasoning_effort + ', should be no_think/high') }}
{%
-
endif
%}
{%
-
endif
%}
So it looks like there are just two reasoning effort levels: "high" (the default) and "no_think" (reason by disabled).
I tried my "Generate an SVG of a pelican riding a bicycle" prompt with the default high reasoning
via OpenRouter
and
got this
:
Quoting the reasoning trace:
[...] Let's maybe add a helmet? It could improve riding theme, but may obscure head. Maybe a small cycling cap or helmet? The user didn't ask; can add red helmet? Might be cute. But pelican with big beak; a helmet might obscure. Better maybe no.
Maybe add sunglasses? no.
Maybe add water? no.
It's interesting how the reasoning trace uses slightly truncated English, presumably because perfect grammar isn't useful or token efficient for hidden reasoning text.
