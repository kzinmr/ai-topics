---
title: "Johnnie Manzari on X: \"Portrait mode launched 10 years ago today. I think it resonated with people because it didn’t feel digital. It felt analog. And this was likely because the inspiration behind its technique went all the way back to oil painting. Sometimes pure math isn’t enough; you need to… / X"
url: "https://x.com/johnnie/status/2114007844605612167"
fetched_at: 2026-10-26T10:03:30.719504+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Johnnie Manzari on X: "Portrait mode launched 10 years ago today. I think it resonated with people because it didn’t feel digital. It felt analog. And this was likely because the inspiration behind its technique went all the way back to oil painting. Sometimes pure math isn’t enough; you need to… / X

Source: https://x.com/johnnie/status/2114007844605612167

Portrait mode launched 10 years ago today. 

I think it resonated with people because it didn’t feel digital. It felt analog. And this was likely because the inspiration behind its technique went all the way back to oil painting. Sometimes pure math isn’t enough; you need to combine it with insights from the liberal arts. 

If you recall Portrait mode shipped a month after the iPhone did. This was because this insight about oil painting took a while to figure out. 

Initially, Portrait mode was seen as a giant math problem. You’d do disparity calculations on the two sensors and output a depth map. The problem was this approach feels and looks digital; it feels fake. In areas without texture, it’s impossible to do this calculation. In areas with ultra fine detail, a lower resolution depth map leads to terrible transitions and a full resolution depth map takes forever to compute. One solution would be to reduce the amount of bokeh so the issues are not as obvious. But then you lose the whole point of the feature, which was to make it look like you had a large, wide-open lens.

The solution to this conundrum—the tradeoff between artifacts and the amount of blur— was quite elegant, but it took a while to stumble across. There’s a saying in painting that if you get the eyes right, nothing else matters. Inspired by this principle from oil painting, the idea was to make sure we never got the eyes wrong. We brought in a machine learning block to find the eyes, and draw a mask layer that protected them, then paired that with the disparity depth map. Counterintuitively, the solution was not to decrease the amount of blur, it was to increase it. The additional blur that we could add once the eyes were protected allowed us to hide the artifacts that were create by bad depth calculation. We let the ears go soft, let the nose go a bit soft. This is that wide open look that people loved, even if people didn’t realize that the ears going soft was why.

I was thinking about this recently with regard to AI. We’ll be able to do more amazing things… we just need to study the masters who came before us.
