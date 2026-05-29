---
type: raw-article
source_url: "https://x.com/27upon2/status/2040975201068810670"
author: "@27upon2"
author_name: "Sriraam"
downloaded: 2026-05-29
tags:
  - continual-learning
  - reinforcement-learning
  - coding-agents
  - open-source
  - agent-training
---

# Continual Learning with Prime Intellect: part 1

Author: Sriraam (@27upon2) — post-training research @chakra_ai, previously Harvard

After reading Cursor's real-time RL blog where they release a new Composer checkpoint almost every five hours, I wanted to build a similar system. Turns out we already have the tools and infra needed in the open-source ecosystem! I made a CLI that simplifies the loop to these commands:

I'm using Prime Intellect's hosted training platform and an RL environment I made on top of their base OpenCode environment that allows me to use a new checkpoint from every training run and use it in my local OpenCode session!

For context, I've got around 2.18 billion tokens of Codex usage sitting on my laptop. There's a lot of useful signal in every message I send and this is rich real-world multi-turn training data that is hard and expensive to curate.

There are a few ways to use this data for continual learning but I'm building a batch-incremental online RL system where the model is trained on a new batch of data sampled from the last deployed checkpoint.

I do want to point out that I am not focusing on optimizing storage of code and the datasets. I want to show that with a little bit of plumbing anyone can build a personalized continually learning coding agent with open models and infrastructure. Yes, prime-rl is open-source.

The hard parts are still the same: data, evals, and rubrics. I will show how I tackle these in later posts. The cool part about the Prime ecosystem is that you can fork my environment and customize it!

## Architecture

The idea is to give an agent a snapshot of a codebase at every turn so that the model produces real rollouts in a sandbox and gets rewarded instead of some variant of SFT based on the content of the user messages, tool outputs, etc. Here's an overview of the entire flow:

1. Add the base model via Prime's Inference to OpenCode. Use it.
2. An OpenCode plugin snapshots every codebase I work on at every user and assistant turn with git bare repos. Why every turn? Cuz I can edit code after the agent finishes before I send my next message, so snapshotting at every turn allows me to get insights on whether the agent's edits persist. This is a metric Cursor uses too btw.
3. Push the git bare repos to GitHub and the OpenCode sessions to a HuggingFace dataset.
4. Write a base TOML file for Prime Intellect's hosted training
5. Start an RL run
6. Deploy the checkpoint if the model improved and update the OpenCode config to use this new model
7. Continue

## Environment

I made a simple environment and a placeholder binary reward based on whether the agent succeeded or not. You can fork it and add your own rewards. The reward I'm going to add is brevity.

One behavior that I want in my coding agents is to write concise code. Today the default behavior is to write a lot of defensive code, reinventing abstractions, writing duplicate code, ignoring the existing types or not writing new types, etc. So in my next post I'll share my learnings of what worked and broke.

## Usage

Since it's still required to experiment with different data mixes, batch sizes, LoRA configs, etc I'm not baking in complete automation into the CLI itself. This means that after every run you have the choice to pass in a new config file for the next run.

The datasets have an auto-incrementing batch_id column that you can use to ensure that each run uses a new batch of data.

When you use the continue command the CLI will automatically push the repos and the dataset but there are also primitives to do this beforehand for more flexibility.

## Next steps

Now that I've got the tools in place there are a few challenges to actually make this work:

- **Evals**: It's not enough for just the rewards to go up, we need a good eval set that decides if we deploy a checkpoint or not.
- **Data quality**: Right now I'm using the session data as is, but depending on the task it is necessary to filter the data. I also need to sanitize because the paths in the sessions need to be changed to match paths in the sandbox to prevent wasted tool calls realizing that the agent is in a different environment. This also includes removing PII and sensitive data.
- **Data transforms**: I want to experiment to see if I can transform the agent sessions to remove a lot of messages in the middle and just keep the start and end at arbitrary turns for gold examples that indicate the original request and the ideal result. This would result in good SFT data to instill efficient behaviors that don't require the users to follow up over several turns.
- **Task and Reward design**: Brevity is one behavior I am interested in, but a couple others are: improved visual understanding of screenshots because the models confidently say they tested an app by taking screenshots but are often wrong, deleting code correctly without leaving dead code.

## References

- GitHub: [13point5/rollouts](https://github.com/13point5/rollouts)
- Prime Intellect hosted training: [docs.primeintellect.ai](https://docs.primeintellect.ai/hosted-training/getting-started)
- Prime RL: [PrimeIntellect-ai/prime-rl](https://github.com/PrimeIntellect-ai/prime-rl)
- Environment: [app.primeintellect.ai/dashboard/environments/13point5/opencode-continual-learning](https://app.primeintellect.ai/dashboard/environments/13point5/opencode-continual-learning)
- Inspired by: [Cursor real-time RL blog](https://cursor.com/blog/real-time-rl-for-composer)
