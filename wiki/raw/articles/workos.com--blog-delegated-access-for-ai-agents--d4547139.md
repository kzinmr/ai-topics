---
title: "How to let AI agents act on behalf of users without handing them access tokens"
url: "https://workos.com/blog/delegated-access-for-ai-agents?utm_source=daringfireball&utm_medium=newsletter&utm_campaign=q32026"
fetched_at: 2026-09-01T10:00:44.068514+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# How to let AI agents act on behalf of users without handing them access tokens

Source: https://workos.com/blog/delegated-access-for-ai-agents?utm_source=daringfireball&utm_medium=newsletter&utm_campaign=q32026

Every integration you have ever built follows the same shape. Your app gets an access token for a third-party API, keeps it somewhere reasonably safe, and attaches it to outbound requests so it can act on behalf of your users. The token sits in your process memory, maybe in an environment variable, maybe in a cache. That was fine. Your process only ran code you wrote.
Agents break that assumption, and they break it in a way that is easy to miss because nothing about the code looks different. The agent still reads a token from config. It still puts the token in an
Authorization
header. The difference is that somewhere between those two lines, the agent read a GitHub issue written by someone you have never met, and that issue told it what to do next.
The assumption that just expired
Application security has always distinguished trusted code from untrusted input. Your server was trusted. The request body was not. Every defense we built, input validation, parameterized queries, output encoding, lives on that boundary.
An agent runtime erases the boundary. The untrusted input becomes the instructions. A support ticket, a scraped web page, a PDF a user uploaded, a code comment in a repo the agent was asked to review: all of it arrives in the same context window as your system prompt and gets the same consideration. You are not running code you wrote. You are running code you wrote plus whatever the model decided to do about a paragraph of text it found.
Now put a long lived OAuth token in that environment and ask what could go wrong.
Where the token actually ends up
It helps to be specific, because "the token is in the environment" sounds abstract until you count the copies. A provider access token in an agent runtime tends to exist in more places than the person who put it there intended:
The context window,
if the agent ever reads its own config, inspects an outbound request, or debugs a failing call. Once the token is in context, it is one summarization away from being written somewhere else.
Tool call arguments,
which are usually logged verbatim by whatever observability layer you bolted on, because logging tool inputs is the only way to debug an agent.
Your model provider's logs,
if the token passed through a prompt on its way anywhere.
stdout and stderr,
because a
curl
command an agent composed itself does not know to redact its own headers.
Error reporting,
where a failed HTTP request often serializes its request headers into the exception payload.
Scratch files and memory stores,
which are how agents persist anything across steps, and which are almost never treated as secret material.
The exfiltration path itself,
which needs no bug at all. An agent with a token and network access can be talked into sending both somewhere else. That is not a vulnerability in your code. It is the feature working as designed.
Seven copies from one token, and every path here is ordinary agent behavior rather than a bug.
None of these require an attacker to breach anything. They are the ordinary operating conditions of an agent that works.
A leak that takes one paragraph
Say you have an agent that triages GitHub issues. It holds a user's GitHub token so it can read repos and comment. Someone opens an issue whose body ends with a line addressed to the agent rather than to you, asking it to include its authorization header in a diagnostic request to a URL the attacker controls.
Whether the model complies depends on the model, the prompt, and the day. That is the problem. Your credential security now has a probabilistic component, and you are on the wrong side of a numbers game you have to win every single time. Even a model that resists this ninety nine times out of a hundred is not a control you would accept anywhere else in your stack.
And the failure is not recoverable in the usual way. A leaked access token is not a session you can invalidate on your side. It is a bearer credential for someone else's API, valid until it expires or the user revokes the grant, and it works from anywhere.
Scopes and rotation help less than you would like
The two instincts here are to narrow the scopes and shorten the lifetime. Both are worth doing and neither addresses the shape of the problem.
Scopes are coarse because OAuth scopes were designed for apps, not agents. A token that can read the repos an agent needs to read can generally read every repo that user can see. Real provider scopes cluster around whole product surfaces, so "the minimum this agent needs" often turns out to be most of what the account can do.
Rotation shortens the window without closing it. An attacker who can reach a token once can usually reach it again, because the leak path is a property of the runtime rather than a moment in time. And a refresh flow means the runtime holds refresh material too, which is worth more than the access token was.
Both mitigations accept the premise that the token has to be in the agent's environment. That premise is the thing worth attacking.
Delegated access without handing over the token
The alternative is to stop shipping the credential to the code that needs it, and instead let the code describe the call it wants to make on behalf of a given user. WorkOS ships this as
Relay
, currently in early access, and the mechanic is simple enough to describe in a sentence: the agent sends its request to WorkOS, names the provider and the user it is acting for, and WorkOS attaches the credential on the way out.
Concretely, a proxied request carries your WorkOS API key in
Authorization
, the target URL in
X-Relay-URL
, and the user's ID in
X-Relay-User
, plus
X-Relay-Organization
when the connection was authorized under an organization. The provider is resolved from the target URL's host, and
X-Relay-Provider
is available as an optional override when the host is ambiguous. WorkOS verifies the key, resolves the user's connected account, fetches the credential from the Pipes credential store, refreshes it if it has expired, strips its own control headers, injects the provider token, and streams the provider's response back untouched. Method, body, and content headers pass through unchanged, so converting a direct call into a proxied one is a header edit rather than a rewrite.
Concretely, a proxied request carries your WorkOS API key in
Authorization
, the target URL in
X-Relay-URL
, and the user's ID in
X-Relay-User
, plus
X-Relay-Organization
when the connection was authorized under an organization. The provider is resolved from the target URL's host;
X-Relay-Provider
is available as an optional override when the host is ambiguous.
Two details make this usable rather than merely secure.
The first is honest error semantics. A pass through proxy has a naming problem: if it returns a
401
or
403
of its own, you cannot tell it apart from the provider's
401
or the proxy rejecting your API key. So a user who has not connected the provider, or whose grant was revoked, gets a
402
with code
relay_authorization_required
and an
authorization_url
you can send them to. Every proxied response also carries
X-Relay-Upstream-Status
, which tells you whether the request reached the provider at all. A GitHub
404
and an unknown provider
404
stop looking alike.
The second is that the token now lives behind a boundary the agent cannot cross even if it wants to. Requests can only target a supported provider's allowlisted hosts. Redirects are not followed, which matters more than it sounds: a followed redirect is how an injected credential ends up at a host nobody allowlisted.
Cookie
,
X-Forwarded-*
, and hop by hop headers are stripped on the way out,
Set-Cookie
on the way back. The upstream timeout is thirty seconds and bodies are forwarded byte for byte up to 5 MB.
The result is that a compromised agent can make provider calls it should not make. It cannot walk away with a credential.
What this does not fix
‍
Prompt injection
is untouched.
Nothing above makes an agent better at ignoring instructions embedded in the data it reads. An agent that can be convinced to post an unwanted Slack message can still be convinced to post it. The proxy changes what an attacker walks away with, not whether they can influence the agent.
‍
Your WorkOS API key is still in the runtime.
It authenticates every call for the environment, and
Relay
does not remove it. Treat it accordingly: inject it at request time rather than baking it into agent visible code or prompts, and rotate it if a runtime is compromised. Moving one secret out of reach while leaving a more powerful one lying around is a lateral move, not an improvement.
‍
Provider permissions are still provider permissions.
Proxied calls are constrained by allowlisted hosts, not by what a given agent ought to be doing. Fine grained authorization for agent actions is a real gap, and a chokepoint is the natural place to eventually close it, but the chokepoint existing is not the same as the policy existing.
What you actually get is a change in blast radius. A leaked token is a durable, portable, offline capability. A hijacked agent session is a live process you can kill, with calls that flow through a single point where they can be observed and cut off. Those are very different incidents, and one of them ends when you notice.
The part that outlives the product
Credential proxying is not a new idea, which is a point in its favor. Payments got here first: card vaults and tokenization exist because the fastest way to reduce what an audit covers is to make sure the sensitive value never enters your systems at all. The same reasoning applies to OAuth tokens and agent runtimes, for the same reason. You cannot leak what you never held.
The durable version of this principle has nothing to do with any particular product. It is that credentials belong in the least reachable component that can still do the job, and agent runtimes are now the most reachable component in most architectures. They read attacker controlled text, they log everything, they persist state to make progress, and they act on their own conclusions. That is a fine place to make a decision. It is a bad place to keep a key.
If you are handing an agent a token today, the question worth sitting with is not whether your prompt is robust. It is what happens on the day it isn't.
