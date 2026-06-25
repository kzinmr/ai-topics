---
title: "API authentication and key management: A practical guide"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/api-authentication-and-key-management"
scraped: "2026-06-25T06:00:58.835058+00:00"
lastmod: "2026-06-24T17:00:03.645Z"
type: "sitemap"
---

# API authentication and key management: A practical guide

**Source**: [https://elevenlabs.io/blog/api-authentication-and-key-management](https://elevenlabs.io/blog/api-authentication-and-key-management)

Blog
Resources
API authentication and key management for ElevenAPI
Written by
Tadas
Petra
Jack
Limebear
Published
Jun 24, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Get started
Learn more
On this page
Introduction
TL;DR
What is API authentication?
What is key management?
Why API key security matters: the threat model
The cardinal rule: keep API keys server-side
Single-use tokens for client-side apps
Scoping keys to least privilege
API Key rotation
Workspace access controls and permissions
Audit and detection
Incident response
Compliance posture: SOC 2, HIPAA, and data retention
What good API key security looks like
Secure your ElevenAPI integration
FAQs about API authentication and key management
API authentication is how a service verifies that an incoming request is allowed to act on an account. For example, with
ElevenAPI
, API credentials authorize requests that consume metered credits, generate speech and music at scale, and ,in some deployments, touch sensitive audio.
A leaked key costs money and can be used to generate content under your account. It may also provide over-permissioned access to your platforms, creating the potential for data leaks and other attack vectors. Even back in 2020, over 90% of developers used APIs in at least one daily process. Now, with the rise of model context protocols (MCPs) and AI usage, APIs are absolutely everywhere.
This article covers how to authenticate APIs correctly and how to manage keys across their full lifecycle: scoping, rotation, organizational controls, auditing, and incident response. It will help you set up API authentication and key management properly in your team. For reference while you read, keep the
authentication reference
and the
single-use tokens
reference open.
TL;DR
ElevenAPI authenticates every request through a single secret, the xi-api-key header, meaning anyone who holds a key can spend credits and generate audio under the account.
Never ship a long-lived API key in a browser, mobile app, or any other artifact a user could inspect. Keep them on a server you control.
Client-side use cases must authenticate with short-lived, single-use tokens minted server-side and never the long-lived key.
You can reduce the blast radius of a leak by scoping keys to least privilege, separating keys per environment, and rotating on a schedule.
Auditing and anomaly detection help to prevent key leaks and surprises.
What is API authentication?
API authentication is how a service confirms that an incoming request is allowed to act on a specific account before it begins work. A requester presents the credential, a service then verifies it, and upon verification, provides a response.
Simply put, it answers: Is this request authorized to act for this account? It’s important to note that this process is different from API authorization, which outlines what an authenticated request is permitted to do within your system.
What is key management?
Key management refers to the wider set of practices you use to govern an API key across its lifecycle. It determines how you create, store, use, rotate, and revoke access to keys. These systems are in place to ensure the security of an API key from end-to-end.
With rigorous key management systems in place, you’re able to prevent leaky keys and decrease the risk of them becoming publicly accessible.
Why API key security matters: the threat model
Now that authentication and key management are defined, it’s worth being precise about what goes wrong when a key is mishandled. Examining the threat model first means that every subsequent practice we explore has a clear purpose: each one reduces either the chance a key leaks or the damage it does when it leaks.
ElevenAPI authenticates through a single secret-bearing mechanism: the xi-api-key header. Anyone who holds the key is authorized, and there is no second factor on the request itself.
With your key they can spend your credits. Text to Speech, Speech to Text, music, and sound effects are all metered, and an attacker with a valid key can generate continuously until your quota or balance is exhausted.
They can generate at scale, and our rate-limiting model makes this situation more significant than it first appears. The limit is based on concurrency, not a simple requests-per-minute quota. A key on a plan with a concurrency limit of five for a given model family can sustain a meaningful number of simultaneous generations, and an attacker who understands these limits will parallelize the abuse.
They can produce content under your account. Any audio generated with your key is attributed to your workspace, and depending on the voices and inputs involved, that can be a reputational and occasionally a legal concern.
The ways keys escape are mundane, and they are the same failure modes that leak every other kind of credential:
API keys in client-side code:
A key shipped inside a browser bundle, a mobile binary, or a single-page app is, for practical purposes, public. Minification is not obfuscation.
API keys in repositories:
Hardcoded keys committed to Git, including private repos that later become public or are cloned widely, and including files like .env that were never meant to be tracked.
API keys in logs and traces:
Request loggers, error trackers, and observability pipelines routinely capture HTTP headers. A key in xi-api-key ends up in your log store, your APM vendor, and anyone with read access to either.
API keys in CI and screenshots:
Build logs, support tickets, and shared terminals.
Each section below maps to reducing the probability or the impact of one of these.
The cardinal rule: keep API keys server-side
Everything else in this article offers insight into API key authentication and management risk reduction. This one rule is the foundation of that and is something you should implement above all else.
Because the mechanism is so simple, the cardinal rule is that a long-lived API key belongs only on a server you control. It must never ship in a browser, a mobile app, a desktop client, or any artifact a user can download and inspect. If the key is in client-side code, treat it as already compromised.
The SDK reads ELEVENLABS_API_KEY automatically, so the cleanest code passes nothing at all and initializes the client once.
import
{ ElevenLabsClient }
from
"@elevenlabs/elevenlabs-js"
;
// Reads process.env.ELEVENLABS_API_KEY when apiKey is omitted - never a literal.
const
elevenlabs
= new ElevenLabsClient();
const
audio
=
await
elevenlabs.textToSpeech.convert(
"JBFqnCBsd6RMkjVDRZzb"
, {
text:
"Generated entirely server-side."
,
modelId:
"eleven_flash_v2_5"
,
outputFormat:
"mp3_44100_128"
,
});
In production it should be populated from a secret manager (AWS Secrets Manager, GCP Secret Manager, HashiCorp Vault, or your platform's equivalent) at process start, not baked into an image or a .env committed to the repo.
Single-use tokens for client-side apps
The cardinal rule is absolute, but many legitimate use cases need the client itself to reach ElevenAPI: a browser playing streamed Text to Speech, a mobile app capturing audio for transcription, and a real-time agent running in the user's tab. The long-lived key cannot go there. The solution is to give the client a credential that is low-risk if it leaks: a short-lived, single-use token.
Your server holds the long-lived key, authenticates and authorizes the user with your own session logic, then mints a short-lived token and hands only that to the client. The token expires quickly and is scoped to the operation it was issued for, so a leaked token is worth little and soon worth nothing. See the single-use tokens reference for the supported endpoints and exact request shape.
Here is the essential logic of a broker endpoint. It authorizes the user with your own session logic, then mints a token against the documented tokens endpoint. The request goes out with the long-lived xi-api-key from the server, and only the resulting short-lived token comes back to the client.
// ... express app and route boilerplate
app.post(
"/api/voice-token"
,
async
(
req
,
res
)
=>
{
// 1. Authorize the user with YOUR session/auth system first.
if
(!req.session?.
user
)
return
res.status(
401
).json({
error:
"unauthorized"
});
// 2. Mint a short-lived token server-side. The long-lived key travels only
//    in this server-to-server request, never to the browser.
const
response
=
await
fetch(
"https://api.elevenlabs.io/v1/tokens"
, {
method:
"POST"
,
headers:
{
"xi-api-key"
:
process.env.
ELEVENLABS_API_KEY
as
string
,
"Content-Type"
:
"application/json"
,
    },
body: JSON
.stringify({}),
// populate per the tokens reference
});
// 3. Return only the short-lived token. The API key never leaves the server.
res.json({
token:
await
response.json() });
});
The browser then uses that token to connect, and the long-lived key never enters the page.
Scoping keys to least privilege
Least privilege is a principle that designates that every key should only carry the permissions that its job requires, and nothing more. ElevenAPI allows you to implement several permissions-based restrictions that bind what a key can and can’t do.
A single all-powerful key is the worst case for blast radius, and it is also the easy default. A better approach is to assume any one key will eventually leak and to ensure that when it does, it can do only as much as the job requires.
Start with scope restriction, which limits which API endpoints a key can call. A key used only for transcription does not need
Text to Speech
access; a key for a music feature does not need to touch voice management.
Next is the credit quota. Assigning a custom credit limit per key caps the financial damage of a leak while also containing runaway loops in your own code.
IP whitelisting goes further. You can restrict a key to specific IP addresses or CIDR ranges, and requests from non-whitelisted IPs are rejected with a 403. This is an Enterprise feature currently in preview, available through your account manager.
Finally, do not share a key across development, staging, and production. Issue a distinct key per environment, each with its own scope and quota. Per-environment keys keep a developer-laptop leak away from production credits, let you rotate one environment without disturbing the others, and make usage logs interpretable because the traffic is already segmented by origin.
API Key rotation
Key rotation is the practice of replacing a key with a fresh one on a regular basis. It’s also an action you can take whenever you suspect a breach or exposure.
On a schedule, rotation also shrinks the window in which an unnoticed leak can be exploited. Rotation is only painless if your code was built for it, so design for rotation before you need it.
The core technique is overlapping keys, which gives you a zero-downtime cutover:
Generate a new API key:
Provision a new key alongside the existing one, with the same scope, quota, and IP restrictions. Both are now valid.
Update key:
Roll the new key out by updating the secret in your secret manager and letting instances pick it up (a restart, a re-read, or a secret-manager refresh, depending on your setup).
Confirm traffic:
Verify that traffic is flowing on the new key. Watch usage to confirm the old key has gone quiet.
Remove key access:
Revoke the old key once it shows no traffic for a safe window.
Because both keys are valid during the overlap, there is never a moment where requests fail for lack of a credential. The overlap window has a second benefit: a misconfigured instance reveals itself by continuing to use the old key, so you can find it before you cut that key off.
For the overlap to be a non-event, structure your code so rotation is a configuration change and never a code change. Read the key from one place, at a point where it can be refreshed, and let a single switch decide which secret is live.
// Rotation is driven by configuration, not code edits. The secret manager (or
// the deploy that injects env vars) is the single point of change.
// ELEVENLABS_KEY_ACTIVE selects which slot is live, enabling overlap.
let
client: ElevenLabsClient |
undefined
;
function
activeKey():
string
{
const
slot
= process.env.
ELEVENLABS_KEY_ACTIVE
??
"primary"
;
const
name
= slot ===
"primary"
?
"ELEVENLABS_API_KEY_PRIMARY"
:
"ELEVENLABS_API_KEY_SECONDARY"
;
return
process.
env
[name]
as
string
;
}
function
getClient(): ElevenLabsClient {
return
(client ??= new ElevenLabsClient({
apiKey:
activeKey() }));
}
// Call after a secret refresh to pick up the rotated key without a deploy.
function
resetClient():
void
{
  client =
undefined
;
}
During an overlap, you keep both PRIMARY and SECONDARY populated and flip ELEVENLABS_KEY_ACTIVE. The application code never changes.
For cadence, a routine rotation every 90 days is a reasonable default for backend keys, more frequently for high-value or widely accessed keys, and immediately on any exposure. This can be automated with a scheduled job that provisions, rolls, verifies, and revokes, which turns rotation from an event into a background process.
Workspace access controls and permissions
While scoping and rotation secure individual keys, workspace controls govern who can mint them in the first place. It offers a space to define and follow organizational policy, which will then influence all of your key management practices in the future.
Begin by separating human and machine credentials. People sign in to the dashboard with their own accounts and permissions; services authenticate with keys or, better, service accounts. Do not let a service run on a key minted from an individual's personal access, and do not let people share a single machine key. The reason is offboarding: when a person leaves or a service is retired, you want to revoke exactly the right credential without collateral damage.
Service accounts serve the same goal. They give machine workloads an identity that is not tied to a human, with their own scoping, which keeps your audit trail honest.
Then map access to roles rather than to individuals one at a time. Workspaces support group and member permissions for exactly this. Grant the least privilege that lets each group do its work, review membership periodically, and aim for an arrangement where no single credential, human or machine, can do more than its role requires.
Audit and detection
In the previous stages, we’ve outlined how to reduce the damage of a leak. In this stage, we’ll outline how to detect whether a leak has happened in the first place. Good detection rests on three habits.
The first is recording which key (by identifier, never the secret value) served which class of request, from where, and at what volume. Scrub the xi-api-key header from every logging and tracing layer. A redaction rule in your HTTP middleware and in your APM configuration shuts down the single most common way keys end up in log stores in the first place.
The second is monitoring credit consumption for anomalies. Track per-key credit burn over time and alert on deviations from the baseline: a sudden spike, generation at unusual hours, or a key that is supposed to be idle suddenly becoming active.
The third is watching the concurrency headers. We return the current and maximum concurrent requests on every response in the current-concurrent-requests and maximum-concurrent-requests headers. They tell you how much headroom you have, and a sustained pin at the maximum that you did not initiate is a strong abuse signal. Using the raw HTTP endpoint exposes the response headers directly:
const
resp
=
await
fetch(
"https://api.elevenlabs.io/v1/text-to-speech/JBFqnCBsd6RMkjVDRZzb"
, {
method:
"POST"
,
headers:
{
"xi-api-key"
:
process.env.
ELEVENLABS_API_KEY
as
string
,
"Content-Type"
:
"application/json"
,
  },
body: JSON
.stringify({
text:
"Monitoring headroom."
,
model_id:
"eleven_flash_v2_5"
}),
});
const
current
= resp.headers.get(
"current-concurrent-requests"
);
const
maximum
= resp.headers.get(
"maximum-concurrent-requests"
);
// Emit these to your metrics pipeline; alert on sustained saturation you did not cause.
These should cause alerts to go off. A dashboard that no one watches does not provide detection. Wire credit-spike and concurrency-saturation signals into the same alerting path you use for outages, with a clear owner.
Incident response
Even with the best security and monitoring systems possible, you still need to assume that a key will eventually leak. Planning for that eventuality with a list of steps to limit damage gives you a response roadmap that saves time and decreases impact.
Here is a pre-defined incident response pathway for API key exposure:
Revoke the leaked key immediately:
Do not wait to understand the full scope. A revoked key cannot generate, and revocation is reversible in the sense that you can always issue a replacement. This is the single highest-value action.
Rotate to a fresh key:
If the leaked key was serving production traffic, use the overlap procedure in reverse: bring up a new key, cut traffic over, then confirm the leaked key is dead. Because your code reads the key from configuration, this is a config flip, not a code change.
Assess the blast radius from usage logs:
With the leak contained, quantify it. How long was the key valid and exposed? What credits were consumed during the window, and does the pattern match legitimate traffic or abuse? What endpoints did it touch?
Rotate dependent secrets:
A key rarely leaks alone. If it was exposed in a repo, a log store, or a CI pipeline, assume neighboring secrets in the same place are also exposed and rotate them too.
Close the leak path:
Find how the key escaped and fix that, or it will happen again: add the file to .gitignore and purge history, add header redaction to the logger, move the secret out of the build artifact, and tighten access to the CI system.
Write the post-mortem:
Document the timeline, the blast radius, the root cause, and the concrete controls added (scope tightening, IP whitelisting, a secret scanner in CI, and faster rotation cadence).
By following these steps, you’ll have a go-to process in place for your API exposure disaster scenarios.
Compliance posture: SOC 2, HIPAA, and data retention
Authentication is one input to a broader compliance evaluation, and it is worth being careful about what can and cannot be claimed here. Treat the following as factual starting points, not as a determination for your use case.
ElevenLabs is
SOC 2 compliant
. For eligible plans and use cases, HIPAA compliance and zero-retention modes are available. Zero-retention means request content is not stored after processing, which matters when your inputs or generated audio are sensitive.
Whether a given mode applies depends on your plan, your configuration, and the specifics of what you are processing. Confirm eligibility and the exact terms for your account before relying on any of them, and pair them with the access controls described above. Compliance certifications govern how the platform handles your data; key management governs who can act on your behalf, and you own that half.
What good API key security looks like
Server-side-only keys remove the largest leak surface. Single-use tokens extend that guarantee to the clients that genuinely need to reach our API. Scoping and per-environment separation bound the damage of any one leak. Rotation built into configuration makes recovery routine instead of risky. Workspace controls keep human and machine identities distinct. Auditing turns abuse into an alert instead of a surprise on your bill. A written runbook turns an incident into a procedure.
It is the same credential hygiene that protects any high-value secret, applied to a key whose particular value is that it spends money and generates audio at scale.
When you are ready to wire this up against the real request shapes, the authentication reference and the single-use tokens reference have the current list of supported endpoints. To understand the concurrency model your monitoring should track, the models reference and the API quickstart are the right next reads.
Secure your ElevenAPI integration
Strong API authentication is a foundational control upon which numerous other security practices build on. Taking measures like using server-side-only keys, deploying single-use tokens for clients, least privilege scoping, and building rotation into key management help prevent risk at scale.
For more information on supported endpoints and the exact header format to use, reference the
ElevenAPI documentation
. If you’re ready to get started, request an
API key from ElevenLabs
to start building today.
FAQs about API authentication and key management
How do you authenticate an API?
Most APIs authenticate each request by using a secret credential that the server references before responding. The requester sends their API key in a request header, which the server then validates and checks permissions for. The server will either fulfill the request or completely reject it based on whether that API key is allowed to act on a given account.
How should you store an API key?
The best way to store an API key is within a secret manager, loading it into your active environment whenever needed. Committing a key to a repository or shipping it in an inspectable artifact would potentially expose the key. Never use long-lived keys on client-side applications.
What is API key rotation?
An API key rotation is the process of replacing an existing key with a new one at a regular interval or whenever a breach is suspected by your team. Rotating keys are a low-effort method of reducing the total time an undetected leak can use a key for. If you overlap the old and new keys for a brief validation window, API key rotation can work without introducing any downtime to your system.
What’s the difference between authentication and authorization with API keys?
API authentication is a process that confirms the person making a request has access. Authorization then decides what that person can do within your system after they have access. API keys do both at once: checking for access and validating the scope of endpoints it can reach or, in some systems, how many credits it can spend.
How do you secure API keys in client-side apps?
The most effective way of securing API keys in client-side apps is by holding the key on your server, authenticating the user with your own session logic, then minting a single-use, short-lived token that you give to the client. Never use a long-lived key on anything shipped to the client, as this could essentially become public.
