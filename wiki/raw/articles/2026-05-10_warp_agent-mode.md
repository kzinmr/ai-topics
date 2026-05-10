---
title: "Agent Mode: LLM embedded in the terminal for multi-step workflows"
source: "Warp Blog"
url: "https://www.warp.dev/blog/agent-mode"
scraped: "2026-05-10T01:27:06.792588+00:00"
lastmod: "2026-04-24T14:39:18.000Z"
type: "sitemap"
---

# Agent Mode: LLM embedded in the terminal for multi-step workflows

**Source**: [https://www.warp.dev/blog/agent-mode](https://www.warp.dev/blog/agent-mode)

Product
Agent Mode: LLM embedded in the terminal for multi-step workflows
Michelle Lim
June 17, 2024
Today we are announcing the release of Agent Mode in Warp AI, a new way to interface with AI from the command line so developers can accomplish multi-step workflows without leaving the terminal.
Agent Mode can:
Understand plain English (not just commands)
Execute commands and use that output to guide you
Correct itself when it encounters mistakes
Learn and integrate with any service that has public docs or –help
Agent Mode raises the level of abstraction in the terminal. Using natural language, you can ask the terminal to accomplish any high level task without worrying about the specific commands you need.
Agent Mode knows when it needs more information to help you complete a task. It will ask permission to run commands on your machine and use the outputs to guide you, step-by-step. It’s also self-correcting when it runs into errors.
Because Agent Mode executes tasks through the CLI, it integrates with practically any service with zero configuration. If the service has a CLI, an API, or publicly available docs, you can use Agent Mode for the task. Agent Mode has inherent knowledge of most public CLIs, and you can easily teach it how to use internal CLIs by asking it to read their help content.
Watch Agent Mode in action:
Browse more examples and learn how it works.
‍
Work through any dev task with Agent Mode
Agent Mode makes it easy (and even fun!) to work through development tasks that would otherwise require a lot of time and context switching.
For example, if you would previously browse through the AWS console to figure out how to provision a new instance or upgrade your database, with Agent Mode you can type “help me upgrade an AWS database” and get guidance without leaving your terminal. Provide a little context (e.g. the region, the service) and Agent Mode will walk you through the process step by step, gathering info and fixing errors until you have completed the task together.
Because the CLI is already a universal interface, Agent Mode is automatically “integrated” with almost any dev tool out of the box. You can use Agent Mode to interface with Github (gh), AWS/GCP (aws/gcp), kubernetes, Datadog (dog), and any other tool with a CLI. You can use curl to read web pages and interact with APIs. It can even interact with internal CLI tools. As long as the tool has a --help option, you can ask Agent Mode to learn it, and then immediately have Agent Mode start doing tasks with it. You can also attach specific output or errors for the AI to reference.
Much more than codegen or a chatbot, you can use Agent Mode for use cases like debugging, devops and analysis.
Agent Mode in action
Let’s start with the simplest example: Say you’ve run into the super-common “port 3000 already taken” error. You can type “fix it,” attach the error context, and Agent Mode will respond to help.
You can attach context to an AI query and type natural language, like "fix it."
Agent Mode will ask to run
kill $(lsof -t -i:3000)
—a command that kills the process on port 3000. It not only knows to kill the process, but it also fills in the command with the port information from the error output. There’s no need to copy and paste console outputs or to fill in parameters manually.
Agent Mode makes a suggestion to kill a process using a port.
If the AI agent doesn’t have enough context, it will attempt to gather context by running commands on your machine with your approval at every step. For example, when solving an out-of-date node dependency for you, it first asks to run “which nvm” to check which node manager you use. It is only when it knows your node manager that it suggests you install the right node version
nvm install 18.19.1
.
Agent Mode asks to check the node version manager before suggesting an upgrade.
Notably, the AI agent is self-correcting. When it makes a mistake, it adjusts itself until it completes the task for you. For example, if Agent Mode suggests a command with an incorrect flag, it will follow up with another command with the right flag. Agent Mode will make sure commands work and are suited to your system.
Privacy, security, and natural language detection
When you have auto-detection enabled for natural language, Warp AI will automatically detect when you are entering plain English on the command line and switch into Agent Mode.
Auto-detection happens locally. The Warp app has a local classifier that checks input strings. Nothing you type in the input ever leaves your machine during the natural language detection classification. After auto-detection occurs, you must take explicit action to send a request to Warp AI. You can disable auto-detection at any time.
You have total, explicit, and granular control over any information that is sent to Warp AI. You get to opt-in specific terminal outputs (if any) to send to the AI.
Once you are engaging with Agent Mode, Warp AI will read the command outputs for any command you authorize it to run during the session as it gathers information in pursuit of completing a task. In other words, if Agent Mode requests that you run a command on its behalf, it will read the output of that command. You are always in the driver’s seat to approve each command it runs.
Agent Mode’s approach to context-gathering is transparent since it is all done through terminal commands. For example, if Warp AI needs the name of your git branch, it will ask to run git branch and read the output. You will be able to approve or reject the command. We’ve designed Agent Mode so that you know exactly what information is leaving your machine.
Since Warp AI uses OpenAI, OpenAI’s servers will receive all input. OpenAI does not train their models on this data. If your organization requires Zero Data Retention or the option to bring your own LLM, these features are available on Warp’s Enterprise plan.
Contact us to learn more
.
Updates to Warp AI
Existing Warp users will notice that new Agent Mode has replaced the first-generation Warp AI chat panel.
Agent Mode can handle all of your Warp AI chat use cases and more. It’s much more powerful and does not require you to copy and paste as you go.
AI Command Suggestions
(press “#” to ask Warp AI) will remain supported for the short-term. You may find this helpful as a way to get quick suggestions without engaging Agent Mode in a session. As we confirm that Agent Mode can deliver accurate suggestions for commands with equal speed and success, it’s likely we’ll sunset this feature in favor of the Agent Mode experience.
Try Agent Mode today
Agent Mode is available today for Warp users on every plan tier. The Free plan includes up to 40 AI requests per month and higher requests are available on Warp’s Pro, Team, and Enterprise plans.
Compare plans
.
To learn more about Agent Mode:
Check out the examples gallery
Visit the docs
Give it a try and let us know what you think! We’d love for you to share your first impressions and use cases with us on X (Twitter) @warpdotdev.
‍
Download Warp
Related articles
Apr 28, 2026  ·  7 min
Warp is now open-source
Warp is now open-source, and the community can participate in building it using an agent-first workflow managed by Oz, our cloud agent orchestration platform.
Apr 14, 2026  ·  2 min
Introducing Universal Agent Support: level up any coding agent with Warp
Warp now supports the most popular CLI coding agents — including Claude Code, Codex, Gemini CLI, and OpenCode — with vertical tabs, notifications, native code review, rich input, and remote control, making it the best terminal for multi-threaded agentic development.
Mar 24, 2026  ·  7 min
Build vs buy: how to deploy coding agents at scale
Should you build an in-house agent orchestration system or buy one off the shelf? Here's how to think about the decision and where the real complexity lies.
