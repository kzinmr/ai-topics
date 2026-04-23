---
title: Should You Use a Lambda Monolith (Lambdalith) for Your API?
category: other
status: active
---

# Should You Use a Lambda Monolith (Lambdalith) for Your API?

**Source:** https://rehanvdm.com/blog/should-you-use-a-lambda-monolith-lambdalith-for-the-api
**Author:** Rehan van der Merwe
**Date:** 2026-04-16

## Core Thesis
- Applies to API-facing Lambda functions
- Per-route single-purpose Lambdas optimize too early, add deployment bloat, misplace security boundaries
- Blast radius should be defined at API/service level, not per-route
- Default to Lambdalith for APIs unless leveraging advanced AWS REST API Gateway features or requiring maximum compute-layer portability

## Pros & Cons of a Lambdalith

### Advantages
- **Single CloudWatch Log Group:** Fewer metric filters, subscription filters, and alarms
- **Centralized Logic & Tests:** Consistent error handling, shared code, unified test suites reduce context switching
- **Higher ROI:** Faster development, easier maintenance, simpler deployments for typical API workloads
- **Reduced Cognitive Load:** No duplicate code, consistent flows, centralized testing

### Disadvantages
- **Loose Fine-Grained Control:** Harder to set route-specific permissions, timeouts, environment variables, memory limits
- **Perceived Upgrade Risk:** Updating one route technically deploys the entire function (mitigated by proper testing & service boundaries)
- **Package Size:** Larger deployment bundles can increase cold start times (mitigated by bundlers)

## Actionable Escape Hatches

### 1. Route-Specific Resource Allocation
```text
/{proxy+} → Default Lambda (standard memory/timeout)
/invoice → Separate Lambda (same codebase, higher memory/timeout)
```
- Keeps tests identical while granting heavy routes needed resources

### 2. Compile-Time Code Splitting
- Use bundlers like **ESBuild** to split heavy dependencies at build time
- Proxy route won't load invoice-specific packages, shrinking cold start impact without runtime complexity

### 3. Cold Start & Latency Reality
- Cold starts affect **<0.25%** of total invokes
- Prioritize optimizing **average latency (p50)** over tail latency (p99.99)
- Bundle code into single file (drop `node_modules`) to minimize package size and cold start duration

### 4. Centralized Logging & Querying
- Enforce **consistent JSON log format** across all routes
- Use **CloudWatch Logs Insights** to extract route-specific metrics from single log group without needing separate subscriptions

## AWS Best Practices: Claims vs. Reality

| AWS Claim | Author's Rebuttal & Reality |
|:---|:---|
| **📦 Large package size slows cold starts** | ✅ True, but cold starts are rare. Bundlers (ESBuild) solve this. Obsessing over p99.99 ignores more impactful bottlenecks (DB queries, caching). |
| **🔒 Hard to enforce least privilege (IAM)** | 🚫 Per-route IAM is overkill. Traditional servers don't do this. Security boundary belongs at **service level**. Shared permissions are safe if least privilege is practiced correctly. |
| **⬆️ Harder to upgrade / limits blast radius** | 🚫 Assumes zero shared code (unrealistic). Shared code means route-level updates still risk whole API. Split by **domain/service**, not route. |
| **🧠 Harder to maintain / high cognitive load** | 🚫 Monoliths *reduce* cognitive load: no duplicate code, consistent flows, centralized tests. Split only when project scales (Conway's Law). |
| **♻️ Harder to reuse code** | 🚫 False. Monoliths make reuse trivial. Single-purpose forces package publishing, version syncing across 100s of routes, and distributed deployments → **hurts velocity**. |
| **🧪 Harder to test** | 🚫 Test complexity remains identical. Monoliths actually require *fewer* duplicate tests (e.g., one CORS test vs. per-route). |
| **🐦 Canary releases are easier** | 🚫 Route-level canaries add deployment overhead/resources. Only valuable if code isn't shared (rare in APIs). |

## Key Quotes
> `The argument to limit the blast radius on a per route level by default is too fine-grained, adds bloat and optimizes too early. The boundary of the blast radius should be on the whole API/service level, just as it is and always has been for traditional software.`

> `What's always been so surprising is that internally at Amazon teams spend far less time on this than I see external customers obsessing over it. Ppl are here worrying about their <.25% of invokes when PC exists for a reason, while ignoring slow DB queries and poor caching`  
> **— Chris Munns (@chrismunns)**

> `I can never advocate for duplicating code. This just creates tech debt, which, if incurred must be paid off later and will slow velocity.`

## Final Recommendation
1. **Default to a Lambdalith** for API workloads to maximize development velocity, simplify logging, reduce deployment complexity
2. Use escape hatches (route-specific resources, compile-time splitting, centralized logging) to mitigate cons
3. Only split into per-route Lambdas when there's a clear, measurable benefit that cannot be achieved within the monolith
