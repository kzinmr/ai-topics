---
title: "Build a Claude Managed Agent with Vercel Sandbox"
date: 2026-05-19
url: "https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox"
author: "Vercel"
source: "Vercel Knowledge Base"
tags: ['anthropic', 'managed-agents', 'sandbox', 'vercel', 'ai-agents', 'serverless']
extraction: raw-html
---

Claude Managed Agents (CMA) handles the agent and infrastructure for you: the harness, the session state, the tools, and the execution environment. What if you want to plug in your own environment instead? This guide shows you how, using Vercel Sandbox as the execution layer.

Check out the demo app source code, or follow the walkthrough below to build it yourself.

How it works

## Anthropic hosts the brain: Claude, the tool-calling loop, skills, and memory. The brain has no hands, so when Claude calls a tool, something on your side has to run it and post the result back. With Vercel, that &quot;something&quot; splits into two planes:

Control plane (Vercel Function): receives session.status_run_started webhooks from Anthropic and spawns one Vercel Sandbox per session.Compute plane (Vercel Sandbox): the spawned VM attaches to the session&#x27;s event stream, executes tool calls (run_shell, read_file, etc.), posts results back, and exits when the session ends.Each session runs in a fresh isolated microVM that exits when the session ends. The environment key never enters the VM: Vercel Sandbox&#x27;s credential brokering injects it on outbound requests scoped to this session, so a compromised sandbox can&#x27;t extract the key or use it to act on other sessions.

Prerequisites

## A Vercel account with Sandbox accessAn Anthropic account with environments accessNode.js 22+Vercel CLI (pnpm add -g vercel)Set up the project

## The control plane webhook, the UI, and the setup scripts all live in the same Next.js app. Scaffold it with:

pnpm create next-app cma-private-sandboxcd cma-private-sandboxpnpm add @anthropic-ai/sdk @vercel/sandbox@beta @vercel/functions mspnpm add -D tsx @types/node @types/msmkdir scripts sandboxtsx auto-loads .env.local before running any script, so no dotenv import is needed in the scripts.

Link the project to Vercel and pull credentials:

vercel linkvercel env pull .env.localThis writes a VERCEL_OIDC_TOKEN to .env.local so @vercel/sandbox can authenticate without a long-lived Vercel token.

All API calls below require two headers, which the SDK adds automatically when you pass the beta tag:

anthropic-version: 2023-06-01anthropic-beta: managed-agents-2026-04-01Create the self-hosted environment

## Create the environment in the Anthropic dashboard (Workspace → Environments → New → Self-hosted) or in code:

scripts/create-environment.tsimport Anthropic from &quot;@anthropic-ai/sdk&quot;;
async function main() { const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY }); const env = await client.beta.environments.create({ name: &quot;vercel-sandbox&quot;, config: { type: &quot;self_hosted&quot; }, betas: [&quot;managed-agents-2026-04-01&quot;], }); console.log(&quot;ANTHROPIC_ENVIRONMENT_ID=&quot; + env.id);}main();From the project root, run it once and add the printed ID to .env.local:

pnpm tsx scripts/create-environment.tsIn the console, open the environment and click Generate environment key. Save it as ANTHROPIC_ENVIRONMENT_KEY in .env.local. This key authenticates the whole worker flow: poll, ack, heartbeat, stop, and the session event stream. Ignore the on-screen instructions about an env_manager binary: Vercel Sandbox is the runtime.

Create the agent

## Create an agent with the custom tools your runner will handle. The tools array here must match exactly what runTool implements in the sandbox:

scripts/create-agent.tsimport Anthropic from &quot;@anthropic-ai/sdk&quot;;
const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
async function main() { const agent = await client.beta.agents.create({ name: &quot;Vercel Sandbox Agent&quot;, model: &quot;claude-opus-4-7&quot;, system: &quot;You are a coding assistant with a Linux environment.&quot;, tools: [ { type: &quot;custom&quot;, name: &quot;run_shell&quot;, description: &quot;Run a shell command in the sandbox. Returns stdout.&quot;, input_schema: { type: &quot;object&quot;, properties: { command: { type: &quot;string&quot; }, }, required: [&quot;command&quot;], }, },Still in scripts/create-agent.ts, add a read_file tool the same way:

scripts/create-agent.ts { type: &quot;custom&quot;, name: &quot;read_file&quot;, description: &quot;Read the contents of a file at the given path.&quot;, input_schema: { type: &quot;object&quot;, properties: { path: { type: &quot;string&quot; }, }, required: [&quot;path&quot;], }, }, ], betas: [&quot;managed-agents-2026-04-01&quot;], }); console.log(&quot;ANTHROPIC_AGENT_ID=&quot; + agent.id);}main();Run it and save the printed ID as ANTHROPIC_AGENT_ID in .env.local:

pnpm tsx scripts/create-agent.tsWrite the sandbox tool runner

## This is the code that runs inside each spawned sandbox. It reconciles any tool calls that arrived before it attached, then streams new ones and posts results back.

Create sandbox/runner.ts with the imports and constants:

sandbox/runner.tsimport Anthropic from &quot;@anthropic-ai/sdk&quot;;import { execSync } from &quot;node:child_process&quot;;import { readFile } from &quot;node:fs/promises&quot;;
const ENV_ID = process.env.ENVIRONMENT_ID!;const WORK_ID = process.env.WORK_ID!;const SESSION_ID = process.env.SESSION_ID!;const BETA = &quot;managed-agents-2026-04-01&quot;;
// Auth is injected at the sandbox firewall via credential brokering,// so the SDK only needs a placeholder here. The real key never enters the VM.const client = new Anthropic({ authToken: &quot;_brokered_&quot; });const handled = new Set&lt;string&gt;();The released SDK uses one credential for everything: poll, ack, heartbeat, stop, and session events. The control plane will configure the sandbox&#x27;s network policy to inject that credential on outbound requests to api.anthropic.com, so this code never sees the raw token.

In the same file, define your tool implementations:

sandbox/runner.tsasync function runTool(name: string, input: unknown): Promise&lt;string&gt; { if (name === &quot;run_shell&quot;) { const cmd = (input as { command: string }).command; return execSync(cmd, { encoding: &quot;utf8&quot;, timeout: 30_000 }); } if (name === &quot;read_file&quot;) { return await readFile((input as { path: string }).path, &quot;utf8&quot;); } return `unknown tool: ${name}`;}Still in sandbox/runner.ts, start the heartbeat to keep the work-item lease alive:

sandbox/runner.tslet last: string | undefined;const hb = setInterval(async () =&gt; { try { const r = await client.beta.environments.work.heartbeat( WORK_ID, { environment_id: ENV_ID, expected_last_heartbeat: last, betas: [BETA] }, ); last = r.last_heartbeat; } catch {}}, 30_000);Still in sandbox/runner.ts, post results back for each tool call:

sandbox/runner.tsasync function handleTool(ev: { id: string; name: string; input: unknown }) { const output = await runTool(ev.name, ev.input).catch( (e: Error) =&gt; `error: ${e.message}` ); await client.beta.sessions.events.send(SESSION_ID, { events: [{ type: &quot;user.custom_tool_result&quot;, custom_tool_use_id: ev.id, content: [{ type: &quot;text&quot;, text: output || &quot;(no output)&quot; }], }], }); handled.add(ev.id);}Still in sandbox/runner.ts, list existing events to catch up on anything emitted while the sandbox was booting, then switch to the live stream. This top-level try block is the entry point (no main() wrapper needed: tsx runs the file directly):

sandbox/runner.tstry { for await (const ev of client.beta.sessions.events.list( SESSION_ID, { limit: 1000 } )) { if (ev.type === &quot;agent.custom_tool_use&quot; &amp;&amp; !handled.has(ev.id)) await handleTool(ev); else if (ev.type === &quot;user.custom_tool_result&quot;) handled.add(ev.custom_tool_use_id); }
const stream = await client.beta.sessions.events.stream(SESSION_ID); for await (const ev of stream) { if (ev.type === &quot;agent.custom_tool_use&quot; &amp;&amp; !handled.has(ev.id)) await handleTool(ev); }} finally { clearInterval(hb); await client.beta.environments.work .stop(WORK_ID, { environment_id: ENV_ID, betas: [BETA] }) .catch((e) =&gt; { if (e?.status !== 409) throw e; });}The reconcile pass matters because the webhook may take a moment to spawn the sandbox. Listing first and deduplicating with handled ensures no tool call is dropped or processed twice. A 409 from work.stop means another runner already stopped it, which is safe to swallow.

Build the sandbox snapshot

## Installing the Anthropic SDK and copying in the runner on every spawn would add noticeable latency to each session. Build a snapshot once, then every sandbox boots from that prebuilt image with no install step:

scripts/build-snapshot.tsimport { Sandbox } from &quot;@vercel/sandbox&quot;;import { readFileSync } from &quot;node:fs&quot;;
async function main() { const sandbox = await Sandbox.create({ runtime: &quot;node24&quot; }); await sandbox.writeFiles([ { path: &quot;/vercel/sandbox/package.json&quot;, content: Buffer.from(&#x27;{&quot;type&quot;:&quot;module&quot;}&#x27;) }, { path: &quot;/vercel/sandbox/runner.ts&quot;, content: readFileSync(&quot;./sandbox/runner.ts&quot;) }, ]); await sandbox.runCommand(&quot;npm&quot;, [&quot;install&quot;, &quot;@anthropic-ai/sdk&quot;, &quot;tsx&quot;]); const snapshot = await sandbox.snapshot(); console.log(&quot;SANDBOX_SNAPSHOT_ID=&quot; + snapshot.snapshotId); await sandbox.stop();}main();Run it from the project root and save the printed ID to .env.local:

pnpm tsx scripts/build-snapshot.tsRebuild the snapshot whenever you change sandbox/runner.ts or bump the SDK version.

Build the webhook control plane

## Register a webhook in the Anthropic dashboard for session.status_run_started. Each delivery triggers one poll, ack, and spawn pass.

Create app/api/webhook/route.ts with the imports and shared constants:

app/api/webhook/route.tsimport Anthropic from &quot;@anthropic-ai/sdk&quot;;import { Sandbox } from &quot;@vercel/sandbox&quot;;import { waitUntil } from &quot;@vercel/functions&quot;;import ms from &quot;ms&quot;;
const ENV_ID = process.env.ANTHROPIC_ENVIRONMENT_ID!;const ENV_KEY = process.env.ANTHROPIC_ENVIRONMENT_KEY!;const SNAPSHOT_ID = process.env.SANDBOX_SNAPSHOT_ID!;const WEBHOOK_SECRET = process.env.ANTHROPIC_WEBHOOK_SECRET!;const BETA = &quot;managed-agents-2026-04-01&quot;;
const client = new Anthropic({ authToken: ENV_KEY });In the same file, add pollAndAck. The client is already authenticated with the environment key, so ack needs no per-call headers:

app/api/webhook/route.tsasync function pollAndAck() { const work = await client.beta.environments.work.poll(ENV_ID, { reclaim_older_than_ms: 2000, betas: [BETA], }); if (!work || work.data.type !== &quot;session&quot;) return null;
await client.beta.environments.work.ack(work.id, { environment_id: ENV_ID, betas: [BETA], });
return { workId: work.id, sessionId: work.data.id };}Still in app/api/webhook/route.ts, add spawn. It boots a sandbox from the snapshot and runs sandbox/runner.ts detached. The networkPolicy brokers the environment key at the firewall, scoped to just this session and work item: outbound calls to /v1/sessions/&lt;sessionId&gt;/... and /v1/environments/&lt;envId&gt;/work/&lt;workId&gt;/... get the Authorization: Bearer &lt;key&gt; header injected on the wire; anything else (e.g. work/poll or another session ID) gets no auth and is rejected by Anthropic. Matchers require @vercel/sandbox@beta:

app/api/webhook/route.tsasync function spawn(sessionId: string, workId: string) { const inject = [{ headers: { authorization: `Bearer ${ENV_KEY}` } }];
const sandbox = await Sandbox.create({ source: { type: &quot;snapshot&quot;, snapshotId: SNAPSHOT_ID }, runtime: &quot;node24&quot;, timeout: ms(&quot;1h&quot;), networkPolicy: { allow: { &quot;api.anthropic.com&quot;: [ { match: { path: { startsWith: `/v1/sessions/${sessionId}/` } }, transform: inject, }, { match: { path: { startsWith: `/v1/environments/${ENV_ID}/work/${workId}/`, }, }, transform: inject, }, ], }, }, }); await sandbox.runCommand({ cmd: &quot;npx&quot;, args: [&quot;tsx&quot;, &quot;runner.ts&quot;], cwd: &quot;/vercel/sandbox&quot;, env: { ENVIRONMENT_ID: ENV_ID, WORK_ID: workId, SESSION_ID: sessionId, }, detached: true, });}process.env.ANTHROPIC_ENVIRONMENT_KEY is undefined inside the spawned VM. Even if an agent jailbreak or compromised tool ran console.log(process.env), there&#x27;s no key to leak, and the scoped matchers mean a malicious request to work/poll or another session ID won&#x27;t be authenticated. Adding more domains to the runner (e.g. a customer API) means extending the allow map. The default mode is deny-all once you set a network policy, so anything not in allow is blocked at the firewall.

detached: true returns immediately, leaving the runner running inside the VM. Still in app/api/webhook/route.ts, export the POST handler. client.beta.webhooks.unwrap() verifies the HMAC signature, checks the timestamp, and parses the event in one call, so there&#x27;s no hand-rolled crypto:

app/api/webhook/route.tsexport async function POST(req: Request): Promise&lt;Response&gt; { const body = await req.text();
let event; try { event = client.beta.webhooks.unwrap(body, { headers: Object.fromEntries(req.headers), key: WEBHOOK_SECRET, }); } catch { return new Response(&quot;bad signature&quot;, { status: 401 }); }
if (event.data.type !== &quot;session.status_run_started&quot;) return new Response(&quot;ignored&quot;);
const item = await pollAndAck(); if (!item) return new Response(&quot;no_work&quot;);
waitUntil(spawn(item.sessionId, item.workId)); return new Response(&quot;ok&quot;);}waitUntil hands the spawn off so the function returns 200 immediately while Sandbox.create finishes in the background.

For local development without deploying the webhook, copy the same pollAndAck and spawn helpers into scripts/poll.ts and run a blocking poll loop:

pnpm tsx scripts/poll.tsKeep only one control plane running at a time. If the deployed webhook and pnpm tsx scripts/poll.ts both run, they will compete for the same work items.

Deploy and register the webhook

## Push the project to Vercel and set the production environment variables:

vercel deployvercel env add ANTHROPIC_API_KEYvercel env add ANTHROPIC_ENVIRONMENT_IDvercel env add ANTHROPIC_AGENT_IDvercel env add ANTHROPIC_ENVIRONMENT_KEYvercel env add SANDBOX_SNAPSHOT_IDvercel env add ANTHROPIC_WEBHOOK_SECRETvercel deploy --prodIn the Anthropic dashboard, add a webhook subscribed to session.status_run_started pointing at https://your-project.vercel.app/api/webhook. Save the webhook signing secret as ANTHROPIC_WEBHOOK_SECRET.

If your Vercel project has Deployment Protection enabled, Anthropic&#x27;s delivery will be blocked with a 401. Append a bypass token to the URL so it gets through:

https://your-project.vercel.app/api/webhook?x-vercel-protection-bypass=&lt;bypass-secret&gt;The bypass secret is in your Vercel project settings under Deployment Protection.

Add a UI

## With the Next.js project in place, the UI is two API routes plus a client page. The browser never talks to Anthropic directly: app/page.tsx calls your API routes, which hold the API keys server-side.

Create app/api/session/route.ts. It creates the session and sends the first message:

app/api/session/route.tsimport Anthropic from &quot;@anthropic-ai/sdk&quot;;
const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });
export async function POST(req: Request) { const { message } = await req.json(); const session = await client.beta.sessions.create({ agent: process.env.ANTHROPIC_AGENT_ID!, environment_id: process.env.ANTHROPIC_ENVIRONMENT_ID!, betas: [&quot;managed-agents-2026-04-01&quot;], }); await client.beta.sessions.events.send(session.id, { events: [{ type: &quot;user.message&quot;, content: [{ type: &quot;text&quot;, text: message }], }], }); return Response.json({ sessionId: session.id });}Create app/api/session/[id]/route.ts. It streams session events as SSE: catch up on history, then switch to live streaming. The SDK exports BetaManagedAgentsSessionEvent as a discriminated union, so a switch on ev.type narrows each branch without manual casts.

Start the route file with imports and the GET handler shell:

// app/api/session/[id]/route.tsimport Anthropic from &quot;@anthropic-ai/sdk&quot;;import type { BetaManagedAgentsSessionEvent } from &quot;@anthropic-ai/sdk/resources/beta/sessions/events&quot;;
const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });export const dynamic = &quot;force-dynamic&quot;;
export async function GET( _req: Request, { params }: { params: Promise&lt;{ id: string }&gt; },) { const { id } = await params;
const stream = new ReadableStream({ async start(ctrl) { const send = (event: string, data: unknown) =&gt; ctrl.enqueue(new TextEncoder().encode( `event: ${event}\ndata: ${JSON.stringify(data)}\n\n`, ));Still in app/api/session/[id]/route.ts, translate each session event into an SSE frame. Returning true from forward signals the turn is over:

// app/api/session/[id]/route.ts (inside GET → start) const forward = (ev: BetaManagedAgentsSessionEvent): boolean =&gt; { switch (ev.type) { case &quot;agent.message&quot;: send(&quot;message&quot;, { text: ev.content .map(c =&gt; &quot;text&quot; in c ? c.text : &quot;&quot;).join(&quot;&quot;), }); return false; case &quot;agent.custom_tool_use&quot;: send(&quot;tool_use&quot;, { name: ev.name, input: ev.input }); return false; case &quot;user.custom_tool_result&quot;: send(&quot;tool_result&quot;, { content: ev.content }); return false; case &quot;session.status_idle&quot;: if (ev.stop_reason?.type === &quot;end_turn&quot;) { send(&quot;done&quot;, { sessionId: id }); return true; } return false; default: return false; } };Still in app/api/session/[id]/route.ts, catch up on history, then stream live events until the turn ends:

// app/api/session/[id]/route.ts (inside GET → start) try { for await (const ev of client.beta.sessions.events.list( id, { limit: 1000 } )) { if (forward(ev)) return; } const evStream = await client.beta.sessions.events.stream(id); for await (const ev of evStream) { if (forward(ev)) break; } } finally { ctrl.close(); } }, });
return new Response(stream, { headers: { &quot;Content-Type&quot;: &quot;text/event-stream&quot;, &quot;Cache-Control&quot;: &quot;no-cache&quot;, }, });}Replace app/page.tsx with a client component that POSTs to /api/session, then opens an EventSource on /api/session/&lt;id&gt;:

app/page.tsx&quot;use client&quot;;
import { useState, useRef } from &quot;react&quot;;
export default function Home() { const [message, setMessage] = useState(&quot;&quot;); const [status, setStatus] = useState&lt;&quot;idle&quot; | &quot;running&quot; | &quot;done&quot;&gt;(&quot;idle&quot;); const esRef = useRef&lt;EventSource | null&gt;(null);
async function run() { if (!message.trim() || status === &quot;running&quot;) return; setStatus(&quot;running&quot;);
const res = await fetch(&quot;/api/session&quot;, { method: &quot;POST&quot;, headers: { &quot;Content-Type&quot;: &quot;application/json&quot; }, body: JSON.stringify({ message }), }); const { sessionId } = await res.json();
esRef.current?.close(); const es = new EventSource(`/api/session/${sessionId}`); esRef.current = es;
es.addEventListener(&quot;tool_use&quot;, (e) =&gt; { console.log(&quot;tool&quot;, JSON.parse(e.data)); }); es.addEventListener(&quot;message&quot;, (e) =&gt; { console.log(&quot;agent&quot;, JSON.parse(e.data).text); }); es.addEventListener(&quot;done&quot;, () =&gt; { setStatus(&quot;done&quot;); es.close(); }); }
return ( &lt;main&gt; &lt;textarea value={message} onChange={e =&gt; setMessage(e.target.value)} /&gt; &lt;button onClick={run} disabled={status === &quot;running&quot;}&gt;Run&lt;/button&gt; &lt;/main&gt; );}Start the dev server and open the UI:

pnpm devWhen you click Run, the flow is: app/page.tsx → POST /api/session → Anthropic creates the session → webhook (or pnpm tsx scripts/poll.ts) spawns a sandbox running sandbox/runner.ts → GET /api/session/&lt;id&gt; streams events back to the browser.

Stream long-running sessions with Vercel Workflow

## The UI above attaches SSE directly to Anthropic&#x27;s session event stream. That is enough for a demo, but serverless functions can time out on long sessions, and you lose durable replay on refresh.

If you need a production chat UI with durable polling, multi-turn conversations, and full event replay, see Build a Claude Managed Agent with Vercel Workflow: a Vercel Workflow run polls session events, writes them to a durable stream, and the client reads them over SSE. The workflow run is both the execution engine and the event log.

Test locally

## These scripts live under scripts/ and read .env.local via tsx. Run them from the project root.

Create a session (scripts/test-session.ts): same API calls as app/api/session/route.ts, but from the CLI. Use this to get a sesn_01... ID without starting the UI:

pnpm tsx scripts/test-session.tsHandle tools on your machine (scripts/run-session.ts): skips Vercel Sandbox entirely and executes run_shell locally. Pass the session ID from the step above:

scripts/run-session.tsimport Anthropic from &quot;@anthropic-ai/sdk&quot;;import { execSync } from &quot;node:child_process&quot;;
const SESSION_ID = process.argv[2];const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });const handled = new Set&lt;string&gt;();
async function handleTool(ev: { id: string; name: string; input: unknown }) { const cmd = (ev.input as { command: string }).command; const output = execSync(cmd, { encoding: &quot;utf8&quot;, timeout: 30_000 }); await client.beta.sessions.events.send(SESSION_ID, { events: [{ type: &quot;user.custom_tool_result&quot;, custom_tool_use_id: ev.id, content: [{ type: &quot;text&quot;, text: output }], }], }); handled.add(ev.id);}Still in scripts/run-session.ts, catch up on existing events, then stream new ones until the session ends:

scripts/run-session.tsasync function main() { const isEnd = (ev: { type: string; stop_reason?: { type: string } }) =&gt; ev.type === &quot;session.status_idle&quot; &amp;&amp; ev.stop_reason?.type === &quot;end_turn&quot;;
for await (const ev of client.beta.sessions.events.list( SESSION_ID, { limit: 1000 } )) { if (ev.type === &quot;agent.custom_tool_use&quot; &amp;&amp; !handled.has(ev.id)) await handleTool(ev); if (ev.type === &quot;user.custom_tool_result&quot;) handled.add(ev.custom_tool_use_id); if (isEnd(ev as { type: string; stop_reason?: { type: string } })) return; }
const stream = await client.beta.sessions.events.stream(SESSION_ID); for await (const ev of stream) { if (ev.type === &quot;agent.custom_tool_use&quot; &amp;&amp; !handled.has(ev.id)) await handleTool(ev); if (ev.type === &quot;agent.message&quot;) { const text = (ev as { content: Array&lt;{ text?: string }&gt; }) .content.map(c =&gt; c.text ?? &quot;&quot;).join(&quot;&quot;); console.log(text); } if (isEnd(ev as { type: string; stop_reason?: { type: string } })) break; }}main();# Terminal 1: create a sessionpnpm tsx scripts/test-session.ts# → Session ID: sesn_01...
# Terminal 2: handle tool calls locally (no sandbox)pnpm tsx scripts/run-session.ts sesn_01...
# Or: full E2E (poll → ack → spawn sandbox → wait for completion)pnpm tsx scripts/test-e2e.ts
# Debug: dump all events for a sessionpnpm tsx scripts/read-session.ts sesn_01...For the full sandbox path locally, run pnpm tsx scripts/poll.ts in one terminal (same logic as app/api/webhook/route.ts) and pnpm tsx scripts/test-session.ts in another. Stop the deployed webhook first, or the two control planes will compete for work items.

Why Vercel Sandbox

## Self-hosting the CMA compute plane with Vercel Sandbox is the right choice when:

Tools touch private infrastructure: your runner needs to reach internal databases, private APIs, or services not reachable from Anthropic&#x27;s compute. Vercel Sandbox lets you run the compute inside or adjacent to your own network with low-latency, secure connectivity.You are handling per-customer credentials: in a SaaS context each user has their own API tokens. Passing those tokens as env vars to the runner works, but any code that runs in the sandbox can read them. Vercel Sandbox&#x27;s credential brokering injects tokens at the firewall level instead: the sandbox calls fetch(&quot;https://api.example.com/...&quot;) with no auth header, and the firewall adds it before forwarding. console.log(process.env) inside the sandbox reveals nothing.You need egress control: Vercel Sandbox lets you define a domain allowlist and deny everything else, which matters when your runner processes private data and you want to prevent exfiltration.The platform itself is also a good fit for this kind of work:

Battle-tested infrastructure: Vercel has been running microVM sandboxes for 10 years to power its build system. The same infrastructure handles over a billion deployments and has hardened defenses against the kinds of attacks agent code can run into, like cryptominer abuse and container escapes.Built for TypeScript developers: the Sandbox SDK and CLI follow the same DX principles as Next.js, AI SDK, and Turborepo. Secure OIDC authentication, no long-lived tokens, and a small surface area that fits cleanly into the rest of your toolchain.Low-latency connectivity to your cloud: sandboxes have direct egress to your AWS workloads with low data transfer costs, which matters more here than with general-purpose sandbox providers like Daytona or Cloudflare when your agent&#x27;s tools need to reach private services.Using credential brokering

## Instead of passing tokens as env vars:

env: { SESSION_ID: sessionId, CUSTOMER_API_KEY: customerToken, // readable by any sandbox code}Configure injection on the sandbox&#x27;s network policy:

networkPolicy: { allow: [ { domain: &quot;api.anthropic.com&quot; }, { domain: &quot;api.example.com&quot;, inject: [{ requestHeaders: { Authorization: `Bearer ${customerToken}` }, }], }, ],}The runner&#x27;s fetch calls to api.example.com are authenticated. The token never enters the sandbox. You can also scope injection to specific paths and methods using matchers:

inject: [{ match: { path: { startsWith: &quot;/v1/write&quot; }, method: [&quot;POST&quot;, &quot;PUT&quot;, &quot;PATCH&quot;], }, requestHeaders: { Authorization: `Bearer ${writeToken}` },}]Using network policy

## Lock down egress to exactly what the runner needs:

networkPolicy: { allow: [ { domain: &quot;api.anthropic.com&quot; }, { domain: &quot;your-internal-db.example.com&quot; }, ],}Policies can be updated on running sandboxes without restarting. A useful pattern: start with allow-all to install dependencies, then tighten the policy before running agent-generated code or processing sensitive data.

Deploy

## Check out the source or deploy the complete working implementation to Vercel in one click, then run pnpm tsx scripts/create-environment.ts, pnpm tsx scripts/create-agent.ts, and pnpm tsx scripts/build-snapshot.ts locally to fill in the environment variables before Anthropic&#x27;s first webhook fires.

