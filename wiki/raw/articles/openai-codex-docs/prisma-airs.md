---
title: "Prisma AIRS"
source_url: https://learn.chatgpt.com/docs/prisma-airs.md
ingested: 2026-09-26
sha256: d25c37b4523d5dfd7b68613266f05dfc90883be0f5b72eb17b7e88977900dfae
collection: openai-codex-docs
---

# Prisma AIRS

> For the complete documentation index, see [llms.txt](https://learn.chatgpt.com/llms.txt). Markdown versions of documentation pages are available by appending `.md` to the page URL.

Connect Palo Alto Networks Prisma AIRS to apply your security policies to
Codex prompts before they reach the model. Workspace admins configure the
integration once for their workspace.

Prisma AIRS can apply the protections configured in your security profile, such
as data loss prevention, prompt injection detection, and malicious URL
detection.

## Before you begin

You need:

- A ChatGPT workspace with Prisma AIRS access enabled. Contact your OpenAI
  account team to request access.
- Workspace administrator permissions.
- A Prisma AIRS API key, a configured security profile, and the service endpoint
  for your deployment.

## Connect Prisma AIRS

1. Open [Codex Data controls](https://chatgpt.com/codex/cloud/settings/data) as
   a workspace administrator.
2. Under **External guardrails**, find **Prisma AIRS**. If this section isn't
   available, ask your OpenAI account team to enable access for your workspace.
3. Enter your **API key**, **Security profile** name or ID, and **Endpoint
   URL**.
4. Choose an **Enforcement mode** and the behavior **On AIRS failure**.
5. Select **Save connection**. Codex validates the connection and encrypts your
   API key.
6. Select **Test connection** to verify the saved configuration.
7. Turn on **Enable Prisma AIRS** to start scanning prompts across the
   workspace.

Saving the connection doesn't enable scanning. You must also turn on **Enable
Prisma AIRS**.

## Choose an endpoint

Use the approved endpoint for your Prisma AIRS deployment:

| Region        | Endpoint                                                 |
| ------------- | -------------------------------------------------------- |
| United States | `https://service.api.aisecurity.paloaltonetworks.com`    |
| Germany       | `https://service-de.api.aisecurity.paloaltonetworks.com` |
| India         | `https://service-in.api.aisecurity.paloaltonetworks.com` |
| Singapore     | `https://service-sg.api.aisecurity.paloaltonetworks.com` |

Codex uses the United States endpoint by default. Workspace data-residency
requirements can restrict which endpoint you can use.

## Choose how to handle prompts

**Enforcement mode** determines what happens when Prisma AIRS flags a prompt:

- **Block**: Stop the prompt before it reaches the model. This is the default.
- **Alert only**: Record the detection and allow the prompt to continue.

**On AIRS failure** determines what happens if Prisma AIRS is unavailable or
doesn't respond:

- **Allow prompts**: Continue without a completed scan. This is the default.
- **Block prompts**: Stop the prompt until Prisma AIRS can scan it.

Choose **Block prompts** when your security policy requires every covered prompt
to receive a scan decision.

## Understand what gets scanned

Codex sends newly submitted prompt text to the configured Prisma AIRS endpoint
for inspection. This applies to covered Codex workflows, including the app, CLI,
IDE extension, and cloud, when users authenticate to the configured ChatGPT
workspace. Sessions authenticated with a Platform API key aren't covered. See
[Enforce a login method or workspace](https://learn.chatgpt.com/docs/auth#enforce-a-login-method-or-workspace)
to require the intended sign-in method and workspace.

Prisma AIRS doesn't scan assistant responses, tool calls, tool results, files,
or images through this integration. Your configured security profile determines
which threats and sensitive data Prisma AIRS detects.

Codex encrypts your API key and never displays it after you save it. Review Palo
Alto Networks' data-handling, retention, and residency policies before enabling
prompt inspection. Those policies apply to prompts sent to Prisma AIRS.

## Manage the connection

Return to [Codex Data controls](https://chatgpt.com/codex/cloud/settings/data)
to manage the integration:

- Select **Test connection** to verify your saved API key, security profile,
  and endpoint.
- Enter a new key and select **Rotate API key** to replace the saved key
  without changing the other settings.
- Turn off **Enable Prisma AIRS** to stop scanning while preserving the saved
  configuration.
- Select **Disconnect**, then confirm, to stop scanning and delete the saved
  connection and API key.

For broader workspace setup and policy management, see the
[Admin rollout guide](https://learn.chatgpt.com/docs/enterprise/admin-setup) and
[Managed configuration](https://learn.chatgpt.com/docs/enterprise/managed-configuration).