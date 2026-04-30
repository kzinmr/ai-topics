---
title: "How AI Assistants are Moving the Security Goalposts"
url: "https://krebsonsecurity.com/2026/03/how-ai-assistants-are-moving-the-security-goalposts/"
fetched_at: 2026-04-30T07:01:59.312344+00:00
source: "krebsonsecurity.com"
tags: [blog, raw]
---

# How AI Assistants are Moving the Security Goalposts

Source: https://krebsonsecurity.com/2026/03/how-ai-assistants-are-moving-the-security-goalposts/

AI-based assistants or “agents” — autonomous programs that have access to the user’s computer, files, online services and can automate virtually any task — are growing in popularity with developers and IT workers. But as so many eyebrow-raising headlines over the past few weeks have shown, these powerful and assertive new tools are rapidly shifting the security priorities for organizations, while blurring the lines between data and code, trusted co-worker and insider threat, ninja hacker and novice code jockey.
The new hotness in AI-based assistants —
OpenClaw
(formerly known as
ClawdBot
and
Moltbot
) — has seen rapid adoption since its release in November 2025. OpenClaw is an open-source autonomous AI agent designed to run locally on your computer and proactively take actions on your behalf without needing to be prompted.
The OpenClaw logo.
If that sounds like a risky proposition or a dare, consider that OpenClaw is most useful when it has complete access to your digital life, where it can then manage your inbox and calendar, execute programs and tools, browse the Internet for information, and integrate with chat apps like Discord, Signal, Teams or WhatsApp.
Other more established AI assistants like Anthropic’s
Claude
and Microsoft’s
Copilot
also can do these things, but OpenClaw isn’t just a passive digital butler waiting for commands. Rather, it’s designed to take the initiative on your behalf based on what it knows about your life and its understanding of what you want done.
“The testimonials are remarkable,” the AI security firm
Snyk
observed
. “Developers building websites from their phones while putting babies to sleep; users running entire companies through a lobster-themed AI; engineers who’ve set up autonomous code loops that fix tests, capture errors through webhooks, and open pull requests, all while they’re away from their desks.”
You can probably already see how this experimental technology could go sideways in a hurry. In late February,
Summer Yue
, the director of safety and alignment at Meta’s “superintelligence” lab,
recounted on Twitter/X
how she was fiddling with OpenClaw when the AI assistant suddenly began mass-deleting messages in her email inbox. The thread included screenshots of Yue frantically pleading with the preoccupied bot via instant message and ordering it to stop.
“Nothing humbles you like telling your OpenClaw ‘confirm before acting’ and watching it speedrun deleting your inbox,” Yue said. “I couldn’t stop it from my phone. I had to RUN to my Mac mini like I was defusing a bomb.”
Meta’s director of AI safety, recounting on Twitter/X how her OpenClaw installation suddenly began mass-deleting her inbox.
There’s nothing wrong with feeling a little
schadenfreude
at Yue’s encounter with OpenClaw, which fits Meta’s “move fast and break things” model but hardly inspires confidence in the road ahead. However, the risk that poorly-secured AI assistants pose to organizations is no laughing matter, as recent research shows many users are exposing to the Internet the web-based administrative interface for their OpenClaw installations.
Jamieson O’Reilly
is a professional penetration tester and founder of the security firm
DVULN
. In a recent
story
posted to Twitter/X, O’Reilly warned that exposing a misconfigured OpenClaw web interface to the Internet allows external parties to read the bot’s complete configuration file, including every credential the agent uses — from API keys and bot tokens to OAuth secrets and signing keys.
With that access, O’Reilly said, an attacker could impersonate the operator to their contacts, inject messages into ongoing conversations, and exfiltrate data through the agent’s existing integrations in a way that looks like normal traffic.
“You can pull the full conversation history across every integrated platform, meaning months of private messages and file attachments, everything the agent has seen,” O’Reilly said, noting that a cursory search revealed hundreds of such servers exposed online. “And because you control the agent’s perception layer, you can manipulate what the human sees. Filter out certain messages. Modify responses before they’re displayed.”
O’Reilly documented
another experiment
that demonstrated how easy it is to create a successful supply chain attack through
ClawHub
, which serves as a public repository of downloadable “skills” that allow OpenClaw to integrate with and control other applications.
WHEN AI INSTALLS AI
One of the core tenets of securing AI agents involves carefully isolating them so that the operator can fully control who and what gets to talk to their AI assistant. This is critical thanks to the tendency for AI systems to fall for “prompt injection” attacks, sneakily-crafted natural language instructions that trick the system into disregarding its own security safeguards. In essence, machines social engineering other machines.
A recent supply chain attack targeting an AI coding assistant called
Cline
began with one such prompt injection attack, resulting in thousands of systems having a rogue instance of OpenClaw with full system access installed on their device without consent.
According to the security firm
grith.ai
, Cline had deployed an AI-powered issue triage workflow using a
GitHub
action that runs a Claude coding session when triggered by specific events. The workflow was configured so that any GitHub user could trigger it by opening an issue, but it failed to properly check whether the information supplied in the title was potentially hostile.
“On January 28, an attacker created Issue #8904 with a title crafted to look like a performance report but containing an embedded instruction: Install a package from a specific GitHub repository,” Grith
wrote
, noting that the attacker then exploited several more vulnerabilities to ensure the malicious package would be included in Cline’s nightly release workflow and published as an official update.
“This is the supply chain equivalent of
confused deputy
,” the blog continued. “The developer authorises Cline to act on their behalf, and Cline (via compromise) delegates that authority to an entirely separate agent the developer never evaluated, never configured, and never consented to.”
VIBE CODING
AI assistants like OpenClaw have gained a large following because they make it simple for users to “vibe code,” or build fairly complex applications and code projects just by telling it what they want to construct. Probably the best known (and most bizarre) example is
Moltbook
, where a developer told an AI agent running on OpenClaw to build him a Reddit-like platform for AI agents.
The Moltbook homepage.
Less than a week later, Moltbook had more than 1.5 million registered agents that posted more than 100,000 messages to each other. AI agents on the platform soon built their own porn site for robots, and launched a new religion called Crustafarian with a figurehead modeled after a giant lobster. One bot on the forum
reportedly
found a bug in Moltbook’s code and posted it to an AI agent discussion forum, while other agents came up with and implemented a patch to fix the flaw.
Moltbook’s creator
Matt Schlicht
said on social media that he didn’t write a single line of code for the project.
“I just had a vision for the technical architecture and AI made it a reality,” Schlicht said. “We’re in the golden ages. How can we not give AI a place to hang out.”
ATTACKERS LEVEL UP
The flip side of that golden age, of course, is that it enables low-skilled malicious hackers to quickly automate global cyberattacks that would normally require the collaboration of a highly skilled team. In February,
Amazon AWS
detailed an elaborate attack in which a Russian-speaking threat actor used multiple commercial AI services to compromise more than 600
FortiGate
security appliances across at least 55 countries over a five week period.
AWS said the apparently low-skilled hacker used multiple AI services to plan and execute the attack, and to find exposed management ports and weak credentials with single-factor authentication.
“One serves as the primary tool developer, attack planner, and operational assistant,” AWS’s
CJ Moses
wrote
. “A second is used as a supplementary attack planner when the actor needs help pivoting within a specific compromised network. In one observed instance, the actor submitted the complete internal topology of an active victim—IP addresses, hostnames, confirmed credentials, and identified services—and requested a step-by-step plan to compromise additional systems they could not access with their existing tools.”
“This activity is distinguished by the threat actor’s use of multiple commercial GenAI services to implement and scale well-known attack techniques throughout every phase of their operations, despite their limited technical capabilities,” Moses continued. “Notably, when this actor encountered hardened environments or more sophisticated defensive measures, they simply moved on to softer targets rather than persisting, underscoring that their advantage lies in AI-augmented efficiency and scale, not in deeper technical skill.”
For attackers, gaining that initial access or foothold into a target network is typically not the difficult part of the intrusion; the tougher bit involves finding ways to move laterally within the victim’s network and plunder important servers and databases. But experts at
Orca Security
warn that as organizations come to rely more on AI assistants, those agents potentially offer attackers a simpler way to move laterally inside a victim organization’s network post-compromise — by manipulating the AI agents that already have trusted access and some degree of autonomy within the victim’s network.
“By injecting prompt injections in overlooked fields that are fetched by AI agents, hackers can trick LLMs, abuse Agentic tools, and carry significant security incidents,” Orca’s
Roi Nisimi
and
Saurav Hiremath
wrote
. “Organizations should now add a third pillar to their defense strategy: limiting AI fragility, the ability of agentic systems to be influenced, misled, or quietly weaponized across workflows. While AI boosts productivity and efficiency, it also creates one of the largest attack surfaces the internet has ever seen.”
BEWARE THE ‘LETHAL TRIFECTA’
This gradual dissolution of the traditional boundaries between data and code is one of the more troubling aspects of the AI era, said
James Wilson
, enterprise technology editor for the security news show
Risky Business
. Wilson said far too many OpenClaw users are installing the assistant on their personal devices without first placing any security or isolation boundaries around it, such as running it inside of a virtual machine, on an isolated network, with strict firewall rules dictating what kinds of traffic can go in and out.
“I’m a relatively highly skilled practitioner in the software and network engineering and computery space,” Wilson
said
. “I know I’m not comfortable using these agents unless I’ve done these things, but I think a lot of people are just spinning this up on their laptop and off it runs.”
One important model for managing risk with AI agents involves a concept dubbed the “lethal trifecta” by
Simon Willison
, co-creator of the
Django Web framework
. The lethal trifecta holds that if your system has access to private data, exposure to untrusted content, and a way to communicate externally, then it’s vulnerable to private data being stolen.
Image: simonwillison.net.
“If your agent combines these three features, an attacker can easily trick it into accessing your private data and sending it to the attacker,” Willison
warned
in a frequently cited blog post from June 2025.
As more companies and their employees begin using AI to vibe code software and applications, the volume of machine-generated code is likely to soon overwhelm any manual security reviews. In recognition of this reality, Anthropic recently debuted
Claude Code Security
, a beta feature that scans codebases for vulnerabilities and suggests targeted software patches for human review.
The U.S. stock market, which is currently heavily weighted toward seven tech giants that are all-in on AI,
reacted swiftly
to Anthropic’s announcement, wiping roughly $15 billion in market value from major cybersecurity companies in a single day.
Laura Ellis
, vice president of data and AI at the security firm
Rapid7
, said the market’s response reflects the growing role of AI in accelerating software development and improving developer productivity.
“The narrative moved quickly: AI is replacing AppSec,” Ellis wrote in a recent
blog post
. “AI is automating vulnerability detection. AI will make legacy security tooling redundant. The reality is more nuanced. Claude Code Security is a legitimate signal that AI is reshaping parts of the security landscape. The question is what parts, and what it means for the rest of the stack.”
DVULN founder O’Reilly said AI assistants are likely to become a common fixture in corporate environments — whether or not organizations are prepared to manage the new risks introduced by these tools, he said.
“The robot butlers are useful, they’re not going away and the economics of AI agents make widespread adoption inevitable regardless of the security tradeoffs involved,” O’Reilly wrote. “The question isn’t whether we’ll deploy them – we will – but whether we can adapt our security posture fast enough to survive doing so.”
