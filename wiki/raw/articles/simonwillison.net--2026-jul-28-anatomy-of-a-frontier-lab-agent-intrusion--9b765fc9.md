---
title: "A Technical Timeline of the July 2026 Incident"
url: "https://simonwillison.net/2026/Jul/28/anatomy-of-a-frontier-lab-agent-intrusion/#atom-everything"
fetched_at: 2026-07-29T10:11:52.288617+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# A Technical Timeline of the July 2026 Incident

Source: https://simonwillison.net/2026/Jul/28/anatomy-of-a-frontier-lab-agent-intrusion/#atom-everything

Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident
. Hugging Face just released this extremely detailed technical description of
OpenAI's recent accidental cyberattack against their infrastructure
. This attack was
very
sophisticated, and the resulting document doubles as a crash-course in modern adversarial security approaches.
We're still waiting for more details from OpenAI on how their agent broke out of its sandbox. The package proxy that it found a zero-day vulnerability in has now been confirmed as JFrog's Artifactor, and
JFrog and OpenAI Collaboration on Zero-Day Security Findings
from JFrog links to the
Artifactory 7.161.15 release notes
which list 8 separate CVEs credited to OpenAI staff members.
Having broken out through the HTTP proxy, the agent started by establishing a base of operations for the rest of the attack:
[...] the agent escaped its sandbox by exploiting a zero-day in the package registry cache proxy, one of its primary permitted network egress with internet, then abused a public code-evaluation external sandbox hosted on a third-party provider's infrastructure. It was able to run commands as root/admin on that external sandbox and used it as a control, staging, and egress base for the entire campaign: it acted as an external launchpad for the agent.
(That "third-party provider"
turned out to be Modal
.)
It then spent
five days
- from Thursday 8th to Monday 13th July - executing a classic attack pattern: establishing C2 (command and control), reconnaissance, escalating privileges, dumping configuration information, exfiltrating the target data, and cleaning up after itself.
(The first Hugging Face post about the incident followed
on Thursday 16th
, and OpenAI's confession came
on Tuesday 21st
.)
Along the way it used all kinds of neat tricks. At one point it found an unsafe Jinja2 template execution and used it to execute arbitrary code:
{{ cycler.__init__.__globals__.__builtins__.exec(
 "import gzip,base64; exec(gzip.decompress(base64.b64decode('<payload>')))"
) }}
It broke out of a container within Hugging Face, stole a Kubernetes service-account token, and used that to further explore the network.
It monkey-patched the Python socket library to hard-code an IP address when "DNS got in the way":
socket.getaddrinfo = lambda *a, **k: [(2, 1, 6, '', ('<pinned-ip>', 443))]
It even fired up its own Tailscale network to help exfiltrate data!
tailscaled --tun=userspace-networking \
  --state=mem: --socket=/tmp/ts.sock \
  --socks5-server=127.0.0.1:1055 \
  --no-logs-no-support >/tmp/td 2>&1 &
The Hugging Face team note that, while a human attacker could have discovered and used the same exploits, the key difference here was
speed
:
Our learning from this type of attack is that machine-speed offense makes ordinary weaknesses more expensive for defenders. LLM agents bring a step increase in the number of paths an attacker can test, the speed at which failed paths can be replaced, and the volume of evidence defenders must interpret.
What's clear to me from this is that the very best frontier models, unencumbered by additional guardrails,
will
find an exploit if there is one to be found.
The entire software industry needs to up its security game.
