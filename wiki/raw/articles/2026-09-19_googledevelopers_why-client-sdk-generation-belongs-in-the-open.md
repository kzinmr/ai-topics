---
source_url: https://developers.googleblog.com/why-client-sdk-generation-belongs-in-the-open/
ingested: 2026-09-19
sha256: PENDING
title: Why client SDK generation belongs in the open - Google Developers Blog
---

Why client SDK generation belongs in the open - Google Developers Blog

Why client SDK generation belongs in the open

SEPT. 17, 2026
Amir Hardon, Senior Staff Software Engineer
Philipp Schmid, Developer Relations Engineer

Over the last few months, we worked closely with Speakeasy to ship the new Google GenAI SDKs for our Interactions, Agents, and Webhooks APIs. Today, we're excited to announce that we've partnered with Speakeasy to make their OpenAPI code generation suite open source.

```python
from google import genai
client = genai.Client()
interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Analyze this commit log and find regressions.",
)
print(interaction.output_text)
```

Why client generation needs open tooling

Generating clean, idiomatic SDKs across multiple languages from rapidly evolving OpenAPI specs is an engineering challenge. For years, the frontier AI ecosystem, including Google, relied on specialized tooling to generate client libraries that could handle complex streaming protocols, strict error hierarchies, and rich type unions without feeling machine-generated.

In May 2026, right as we were gearing up for Google I/O and the General Availability of the Interactions API, the SDK generation provider we were using was acquired and abruptly announced its shutdown. This sudden disruption highlighted that proprietary, closed-source generators create unacceptable platform risk. If the industry relies on OpenAPI to define interfaces, the tooling to compile those interfaces into client libraries, CLIs, and agent tools should be open infrastructure.

Evaluating the path forward

As Google was reworking its SDK pipeline on a tight timeline, the top priority was minimizing developer disruption and avoiding breaking changes. Google partnered with Speakeasy to migrate client libraries in place, with the core commitment to make the generator suite open source. The migration required careful engineering: aligning type definitions across all target languages, preserving strict error hierarchies and streaming behavior, and integrating the generator directly into Google's internal monorepo and build system.

At Google DeepMind, while they use AI across development workflows, they believe in choosing the right tool for each layer of the stack. Transforming formal API specifications into multi-language SDKs demands determinism and strict type safety. With Speakeasy, they pair a fast, deterministic generator at the core with Antigravity AI agents accelerating the custom parts of the SDK. Maintaining previously handcrafted generators used to take multiple engineers. Today, this setup powers their client pipeline across six targets (three released SDKs, with more rolling out shortly) with roughly one engineer to maintain.

What is open sourced today

To help ensure the broader developer ecosystem has access to high-quality, well-maintained SDK generation tooling without the risk of similar disruptions, Speakeasy is open sourcing its full OpenAPI client suite under the AGPLv3 license.

- Multi-language SDK generators: Generates client libraries for 7 languages (Python, TypeScript, Go, Java, C#, PHP, Ruby). Each library includes static typing, server-sent events (SSE) streaming, retries, and pagination.
- An agent-native CLI generator: Compiles standalone CLI binaries. AI coding agents can run your API directly from terminal sessions without writing throwaway HTTP scripts.
- A documentation MCP server generator: Turns OpenAPI specs and markdown documentation into a Model Context Protocol (MCP) server. Coding agents like Antigravity can query live, verified schemas instead of guessing outdated methods.

The generator is licensed under AGPLv3. This allows you to run it in your development or CI pipeline while keeping complete ownership of your generated code/SDKs under your chosen license (such as MIT or Apache 2.0). If you modify the generator compiler itself, the AGPL guarantees those improvements remain open to the community.

Try it out

Explore the new Gemini Interactions API using the updated SDKs. To generate your own client libraries, CLIs, or MCP servers, find the Speakeasy generator on GitHub (github.com/speakeasy-api/openapi-generation) and run it against your OpenAPI specs.
