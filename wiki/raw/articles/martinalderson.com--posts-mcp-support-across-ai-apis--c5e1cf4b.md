---
title: "Beyond the Hype: Real-World MCP Support Across Major AI APIs"
url: "https://martinalderson.com/posts/mcp-support-across-ai-apis/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-28T07:02:44.518422+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Beyond the Hype: Real-World MCP Support Across Major AI APIs

Source: https://martinalderson.com/posts/mcp-support-across-ai-apis/?utm_source=rss&utm_medium=rss&utm_campaign=feed

MCP is probably the most exciting development in AI and software development I can remember. The ability to connect tools in a LLM-agnostic way so easily really opens an almost paralysing level of new opportunities. It also introduces a whole host of new potential security vulnerabilities (Simon Willson has an
excellent writeup
of the main one).
Recently, I feel I've went all in with Anthropic - upgrading the "Max" plan, using Claude Code daily, and using Claude.ai for most "general" LLM chat. Anthropic introduced MCP so it certainly makes sense that MCP (generally) works great inside Anthropic tools.
I was recently working on a small project for a friend and wanted to use MCPs within the standard LLM API workflow. Given the amount of hype around MCP, I assumed that the "big 3" (OpenAI, Google and Anthropic) had good support in their APIs, even if UI support was lagging a bit behind.
However, I didn't find this the case at all.
Please note I didn't spend a huge amount of time looking into workarounds for this, so I may well have missed something, and by the time you read this it may be outdated.
Gemini API - no real MCP support
I watched the recent Google I/O presentation and had mistakenly assumed that Gemini API at least had good support for MCP. Turns out I was quite wrong on this.
When you go to the MCP section of the documentation, you'll see this:
However, this isn't what I consider "true" MCP support. It just enumerates the MCP tools on the host that is running the LLM query and places them into the tool definition. It doesn't work the same way as the other providers, where the LLM provider itself discovers the tools
and runs them
from their side. This IMO is far preferable to doing all the lifting on your side calling them, as the round trips will quickly add up and overall feels very fragile.
Furthermore, it's only 'supported' in the Javascript and Python SDKs.
I was disappointed to see how poor this is given the excellent tool calling Gemini web UI can do with Google services.
OpenAI API - Good approach, but couldn't get it working
Next I moved on to OpenAI. OpenAI supports full remote MCP support where you can put a MCP URL in and it will do all the heavy lifting, and call the tools remotely.
Unfortunately, I couldn't get it working at all. I can see in the debug logs it discovers the remote tools (hosted using the streamable-http transport, with no auth required).
I just get the following error when trying to call my tools (which works fine with MCP Inspector, Claude and even direct JSON-RPC calls):
"error": {
  "type": "mcp_protocol_error",
  "code": 32600,
  "message": "Session terminated"
},
So it looks promising, but doesn't work. I suspect more testing work needs to be done on it.
Claude AI - (unsurprisingly) works out of the box
Anthropic works out of the box, with a very similar approach. Tool calling works perfectly and it takes a few seconds to add existing remote MCP servers to a prompt - the experience I expected from the other providers.
The drawback with Claude is the price of their API, which while not a total apples to apples comparison, is a lot more expensive than Gemini 2.5 Flash, which is my preferred model for a lot of simpler use cases. Given how quickly MCP can consumer tokens this makes it hard to use for a lot of use cases.
Conclusion
I was surprised to see such a variation in support for MCP in the major providers LLMs. Anthropic, like in many other areas, is way ahead and (potentially) justifies their premium pricing - not because of their model capabilities - but because they make it so easy to use tooling with their products.
Hopefully this will change soon - but it's really surprising to me that Google and OpenAI have got so far behind on having a polished out of the box experience for developers with remote MCP servers.
This is a very similar story with coding agents, where Claude Code feels very far ahead of the Google and OpenAI alternatives. Again - not because of the model, but because the tool calling and management works so seamlessly.
Finally - I think there is a very big opening for someone that hosts open weights models like Qwen3 or (ironically) gpt-oss to deliver a very polished and slick MCP integration option on their hosted API endpoints. I haven't managed to come across one yet, but I'd love to test any -
feel free to reach out to me
if you'd like me to test it and I'm happy to update this blog with new providers.
