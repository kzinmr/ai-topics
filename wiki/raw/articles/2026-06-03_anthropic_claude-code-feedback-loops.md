# Feedback loops: Help Claude Code complete ambitious tasks with less babysitting

**Source:** X Article (id: 2060308122531418112), bookmarked 2026-06-03
**Author:** Anthropic / Claude Code team
**Original URL:** https://x.com/i/article/2060308122531418112
**Content extracted from:** X Article plain_text (full content via xurl bookmark fetch)

---

As we delegate more ambitious tasks to Claude, it becomes increasingly important that it can verify its own work.

The more Claude can self-verify:
- the more independently it can work on long-running tasks
- the better the quality of the final result
- the fewer back and forths it takes to get there

The good news is that Claude already self-verifies against deterministic signals like type errors, lint errors, failing tests, and runtime errors. And as models improve, this will only get better. What Claude can't always infer are the manual checks you run after it responds, and later on, before you merge code into production.

The more of those checks you can encode, the closer Claude's first response gets to the final result you had in mind. You spend less time babysitting, and Claude can keep going while you work on something else.

## Write down your processes

A good place to start is to write down the best-practices version of what you or your team already do. For frontend, that's usually: run the dev server, open the browser, check the console for errors, click around as the user would and look out for things like layout shift or slow navigations.

Every domain has its own version. For each of those steps, there's likely a tool Claude can use for verification.

## Encode your process as a skill

Once the process is clear, encode as much of it as possible as a skill. Install the `skill-creator` plugin, then ask Claude to interview you:

```
/skill-creator Create a skill for verifying frontend changes end-to-end. Interview me about my workflow.
```

If you're struggling to put your process into words, ask Claude for the domain best practices first and let it show you what an end-to-end verification flow might look like.

Taste and judgment are difficult to codify, but many checks have criteria Claude can measure against: a performance budget, an accessibility checklist, design system rules, good vs bad examples.

For example, a frontend skill might include instructions to capture a performance trace through the Chrome DevTools MCP or Agent browser.

Other checks are more qualitative than pass/fail, like comparing data against historical norms. For these, you can work with Claude to set a rubric for evaluating output.

## Review the code before merging with a second agent

Everything above happens inside the agentic loop. There's a second verification step, the moment before you merge, where you can ask another agent to review.

A new agent won't carry the same biases as the one that wrote the code. It has its own context, and isn't influenced by the previous conversation. This isolation makes the review more honest, and catches things the first agent might have missed.

A few options, from manual to automated:
- **/review** (built in skill) - a quick single-pass read of a PR in your terminal.
- **/code-review** (installable plugin) - spins up several subagents in parallel, each reading the diff from a different angle, scores findings for confidence, and posts the result on the PR.
- **Claude Code Review** - a managed service that runs automatically on every PR through GitHub, for Team and Enterprise plans.

Whichever you pick, it's helpful to have a last line of defense before merging to production.

## Putting it together

You now have two layers:
- verification that runs while Claude is building
- a review before merge from an agent that didn't write the code.

Both belong to the same development lifecycle. Think about your current manual steps: you make a change, clean it up, confirm it works, commit, open a PR, get it reviewed, and watch CI.

You can roll all those steps into one workflow by writing a skill that calls other skills. For example, the Claude Code team has a skill they run when working on features, it bundles:
- The `/simplify` skill to clean up the diff
- A custom `/verify` skill to confirm the change works end-to-end
- A design check if the diff touched UI
- A step to open and subscribe to a PR
- A skill to watch CI and fix failures as they come in

While your workflow may look different, creating feedback loops and bundling skills allows Claude to verify and execute more work end-to-end.

## Key References

- Chrome DevTools MCP: https://github.com/ChromeDevTools/chrome-devtools-mcp/
- Claude Code Review: https://code.claude.com/docs/en/code-review
- `/code-review` plugin: https://claude.com/plugins/code-review
- Agent Browser: https://agent-browser.dev/react

## Example: frontend-verify skill

```markdown
---
name: frontend-verify
description: Verify frontend changes in a browser. Run whenever a UI (page, component, typography, CSS style) change is made.
---

# Frontend verify

- Run a two-step verification pass in a real browser.
- Fix issues and re-verify before responding to the user.

## Step 1 — Verify the change behaves as expected

1. Open the URL in a browser:
   - In the Claude Code desktop app, use the embedded preview.
   - In the CLI, use the Chrome DevTools MCP.
2. Interact with the new element and confirm it renders and behaves as expected.

## Step 2 — Verify the change passes a mobile audit

1. Open the URL in a new page via the Chrome DevTools MCP
2. Run a performance trace and audit Core Web Vitals
```
