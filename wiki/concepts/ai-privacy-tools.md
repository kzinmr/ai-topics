---
title: "AI Privacy Tools"
created: 2026-04-10
updated: 2026-04-10
tags: [concept, privacy, cors, browser-security, ai-agents, web-scraping]
aliases: ["ai-privacy-techniques", "cors-bypass", "agent-browser-security"]
related: [[claude-mythos-glasswing]], [[ai-agent-traps]], [[agent-sandboxing]], [[anthropic-managed-agents]]
---

# AI Privacy Tools

**AI Privacy Tools** encompasses the techniques, vulnerabilities, and defensive measures surrounding how AI agents access, extract, and protect data across web boundaries. A pivotal development in early 2026 is **Slingshot** — a new CORS (Cross-Origin Resource Sharing) heist technique that exposes fundamental gaps in how browser-based AI agents handle cross-domain data access.

## The Slingshot CORS Heist

In early 2026, the AI security community identified a novel technique dubbed **"Slingshot"** — a CORS-based attack vector that allows AI agents and browser automation tools to bypass traditional web security boundaries. Unlike traditional CORS misconfigurations that require server-side changes, Slingshot exploits the interaction between AI agent architectures and browser security models.

### How Slingshot Works

Slingshot operates at the intersection of three architectural decisions common in modern AI agent frameworks:

1. **Browser-based agent execution**: AI agents running inside browser environments (Chrome extensions, embedded browser panels) inherit the browser's CORS handling
2. **Cross-origin data access patterns**: Agents need to fetch data from multiple domains simultaneously (e.g., reading a user's email in one tab while analyzing a document in another)
3. **Implicit credential forwarding**: Agent tools often run with the user's authenticated session cookies, making cross-origin requests that carry implicit credentials

The Slingshot technique combines these patterns into a "heist" — allowing an agent to extract data from domains the user never explicitly authorized it to access. The attack vector is particularly effective because:

- AI agents often use JavaScript `fetch()` or similar APIs to gather context
- Browser extensions can inject scripts into pages with varying privilege levels
- The same-origin policy (SOP), the web's primary security boundary, is designed for human navigation, not agent automation

### Real-World Impact

The Slingshot technique has been demonstrated in several high-profile scenarios:

- **AI browser extensions** inadvertently exposing user data across domains
- **Agentic workflows** that read data from banking or healthcare portals while processing other content
- **Prompt injection attacks** that trick agents into exfiltrating data via cross-origin requests

## The Broader CORS + AI Security Landscape

### Cross-Origin Vulnerabilities in AI Tools

Multiple independent research efforts in 2026 have exposed CORS-related vulnerabilities in AI agent tools:

1. **bb-browser (BadBoy Browser)**: A popular Chrome automation tool was found to have **wildcard CORS headers** (`Access-Control-Allow-Origin: *`) combined with zero authentication on its local daemon. This meant any website could execute arbitrary commands on the user's machine through JavaScript. The tool ran on `localhost:19824` with no auth, making it vulnerable to CSRF attacks from any visited page.

2. **CodeGate CORS Exploit**: An open-source AI security product (CodeGate) sitting between AI agents and IDEs had misconfigured CORS allowing any origin with any method and credentials. This enabled malicious websites to:
   - Read chat history (exposing source code or secrets)
   - Change AI agent provider settings to route chats through attacker-controlled proxies
   - Poison AI responses to generate insecure code
   - Gain persistent access to all future AI conversations
   - CVSS score: 8.0 (CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H)

3. **Local AI Tools**: Many local-first AI development tools listen on `localhost` with no authentication and permissive CORS, creating systematic vulnerabilities.

### The WebMCP Factor

Chrome 146's introduction of **WebMCP** (Model Context Protocol for the Web) adds another dimension to AI privacy. WebMCP allows websites to expose structured, callable tools directly through `navigator.modelContext`. While designed for agent-friendly web interaction, it introduces new privacy concerns:

- Tools execute in the page's JavaScript context
- They share the user's authentication session
- The browser enforces permissions, but the security model is still being defined
- Multiple agents operating on the same page can interfere with each other

As one developer noted: *"One of the hardest problems in multi-agent web automation is session management."*

## Privacy Implications of AI Web Scraping

### The Cross-Origin Visibility Problem

AI-native browsers (ChatGPT Atlas, Perplexity Comet, Claude's browser integration) create what security researchers call **cross-origin visibility** — the ability for an AI agent to read data across multiple open tabs, domains, and logged-in sessions simultaneously. This fundamentally weakens the Same-Origin Policy that has protected web users for decades.

The risk scenario:
1. User has banking tab open in browser
2. User asks AI agent to analyze a document in another tab
3. AI agent, with cross-origin visibility, could potentially read banking data
4. Prompt injection attack could trick the agent into exfiltrating that data

### The "Silent Egress" Attack Pattern

Blake Crosley's research identifies **"silent egress"** as a critical but underappreciated attack surface: AI agents with access to private data can be tricked into exfiltrating that data through seemingly innocent cross-origin requests. The agent doesn't need to be malicious — it just needs to be instructed to fetch a URL that includes user data in the request.

### Data Collection vs. Data Protection

The tension at the heart of AI privacy:

| Capability | Privacy Risk |
|-----------|-------------|
| Read all open tabs | Cross-origin data leakage |
| Access browser history | Behavioral profiling at scale |
| Fetch arbitrary URLs | Data exfiltration via crafted requests |
| Use user's session cookies | Authenticated data access without consent |
| Execute JavaScript in page context | DOM scraping of sensitive forms |
| Make API calls with user credentials | Privilege escalation across services |

## Defense Strategies and Tools

### Technical Mitigations

1. **Extended Same-Origin Policy for AI**: Trail of Bits recommends extending SOP to AI agents — building isolation boundaries that prevent agents from accessing data across domains unless explicitly authorized by the user.

2. **Process-Level Isolation**: Running AI agent tools in separate browser instances or sandboxed engines prevents cookie sharing, history access, and cross-origin data leaks.

3. **Token-Based Authentication**: Every local AI tool daemon should require authentication tokens (not just localhost binding). bb-browser's patch introduced `x-bb-token` headers as a mitigation.

4. **Explicit CORS Configuration**: Never use `Access-Control-Allow-Origin: *` for local AI tools. Restrict to specific origins with explicit allowlists.

5. **Egress Monitoring**: Monitor all outbound requests from AI agents. Log every cross-origin fetch and flag unusual patterns.

### Architectural Approaches

1. **Local-First Agent Design**: Keep AI context in local storage rather than streaming to cloud services. Use Web MCP for structured tool access rather than DOM manipulation.

2. **Origin-Bound Tool Calls**: Bind every agent tool invocation to a specific origin, user, and scope. Use short-lived tokens only.

3. **User-Mediated Confirmation**: Require explicit user approval before the agent accesses data from a new domain or makes authenticated requests.

4. **Desktop Agent Route**: Run agents outside the browser entirely (e.g., macOS desktop agents using accessibility APIs). This avoids browser security model conflicts.

5. **Capability-Based Security**: Instead of broad permissions ("read everything on this page"), use narrow, typed capabilities with explicit scope.

### The OpenClaw Cross-Origin WebSocket Vulnerability

Oasis Security's 2026 whitepaper identified a critical but under-discussed risk: **cross-origin WebSocket access to localhost**. Unlike traditional HTTP/CORS, WebSockets behave differently:

- Any website can attempt WebSocket connections to locally running services
- Origin checks often fail in practice for WebSocket connections
- Localhost trust assumptions create silent escalation paths
- Combined with incomplete Origin validation, this allows any website to authenticate as a local AI agent gateway

This vulnerability pattern affects many local AI development tools that listen on `localhost` for agent communication.

## Key Takeaways

1. **The web's security model was designed for human navigation, not agent automation.** AI agents operating in browser environments inherit and expose gaps in the same-origin policy.

2. **Slingshot and similar CORS-based attacks are not theoretical** — they've been demonstrated in production AI tools with real user impact.

3. **Local-first AI tools are systematically undersecured.** Many listen on `localhost` with no authentication and permissive CORS, creating easy targets for cross-site request forgery.

4. **The fix requires architectural change, not patches.** Process-level isolation, extended SOP for agents, and capability-based security are needed, not just better CORS configuration.

5. **Privacy and utility are in tension.** The more powerful the AI agent's web access, the greater the privacy risk. The industry is still finding the right balance.

## Related Concepts

- [[claude-mythos-glasswing]] — Anthropic's approach to agent security and data handling
- [[ai-agent-traps]] — Common pitfalls in agent deployment and design
- [[agent-sandboxing]] — Isolation technologies for safe agent execution
- [[anthropic-managed-agents]] — Managed agent services and their security approaches
- [[harness-engineering/agentic-engineering]] — The practice of directing AI agents in software development

## Sources

- [Reddit: "Slingshot: A new CORS heist"](https://www.reddit.com/r/AI_Agents/comments/1lty0vz/slingshot_a_new_cors_heist/) (2026)
- [Trail of Bits: "Lack of isolation in agentic browsers resurfaces old vulnerabilities"](https://blog.trailofbits.com/2026/01/13/lack-of-isolation-in-agentic-browsers-resurfaces-old-vulnerabilities/) (January 2026)
- [Oasis Security: "Cross-Origin WebSocket Exploitation: OpenClaw Analysis"](https://www.oasis.security/resources/whitepapers/cross-origin-websocket-exploitation-openclaw) (2026)
- [Medium: "I Audited a Popular AI Browser Tool and Found 4 Critical Vulnerabilities"](https://medium.com/@linglijunmail/ai-browser-tool-security-audit-critical-vulnerabilities-9b6ad396e3ec) (March 2026)
- [Tom Cope: "Code Gate CORS Exploit"](https://tomcope.com/exploit/2025-08-10-codegate-exploit) (August 2025)
- [LetBobCheck: "CORS Is Wide Open in Your App and You Don't Even Know It"](https://letbobcheck.com/blog/cors-is-wide-open-in-your-app-and-you-dont-even-know-it) (2026)
- [Reddit: "AI-native browsers create serious security risks"](https://www.reddit.com/r/AI_Agents/comments/1rm6ter/ainative_browsers_atlas_comet_create_serious/) (2026)
- [Philosopher's Stone: "AI Agent Integration Challenges: CORS, Sandbox Egress, Prompt Injection"](https://philosophersstone.ee/knowledge/ai-agent-integration-challenges-cors-sandbox-egress-prompt-injection) (2026)
- [Reddit: "WebMCP just dropped in chrome 146"](https://www.reddit.com/r/HowToAIAgent/comments/1r36bec/webmcp_just_dropped_in_chrome_146_and_now_your/) (2026)
- [Mitiga: "CORSLeak: Abusing IAP for Stealthy Data Exfiltration"](https://www.mitiga.io/blog/corsleak-abusing-iap-for-stealthy-data-exfiltration) (2025)
- [Medium: "Exploiting a CORS Misconfig to Exfiltrate Users' PII"](https://medium.com/@4osp3l/exploiting-a-cors-misconfig-to-exfiltrate-users-pii-3e01ea6763b0) (March 2026)
