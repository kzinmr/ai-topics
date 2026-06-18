---
title: "ART·E: An Email Research Agent That Beats o3"
date: 2025-04-29
author: Kyle Corbitt / OpenPipe
source_url: https://openpipe.ai/blog/art-e-mail-agent
type: blog_post
tags:
  - reinforcement-learning
  - grpo
  - agent-training
  - openpipe
  - reward-function
  - email-agent
  - language-models
  - open-source
---

# ART·E: An Email Research Agent That Beats o3

## Introduction

Today we're releasing ART·E, an email research agent trained with reinforcement learning that outperforms OpenAI's o3 model on our email research benchmark. ART·E is built on Qwen 2.5 32B and trained using GRPO (Group Relative Policy Optimization), demonstrating that smaller open-source models can be trained to match or exceed much larger proprietary models on specialized tasks.

## The Problem

Email research is a challenging task that requires:
- Understanding complex email threads with multiple participants
- Navigating through attachments and linked documents
- Synthesizing information from multiple sources
- Following chains of references and citations
- Understanding temporal context and relationships

Traditional approaches using RAG (Retrieval-Augmented Generation) or simple prompting often struggle with these tasks because they require iterative reasoning and the ability to follow complex chains of information.

## Our Approach

We approached this problem using reinforcement learning to train an agent that can:
1. Search through email repositories using various queries
2. Open and read emails and attachments
3. Follow links and references
4. Synthesize information from multiple sources
5. Provide accurate, well-sourced answers

### The ART Framework

ART·E is built on our ART (Agent Reinforcement Training) framework, which allows us to train language models using reinforcement learning in agentic environments. The framework provides:

- A structured environment for agent interactions
- Tools for defining reward functions
- Support for GRPO and other RL algorithms
- Easy integration with various LLM backends

### GRPO Training

GRPO (Group Relative Policy Optimization) is particularly effective for training agents because it:

1. **Doesn't require a critic model** - Unlike PPO, GRPO estimates advantages by comparing outputs within a group, eliminating the need for a separate value network
2. **Is sample efficient** - By comparing multiple outputs from the same prompt, GRPO can learn from relative differences
3. **Handles sparse rewards well** - The group-based comparison naturally handles tasks where only some trajectories receive positive rewards

For ART·E, we used GRPO with groups of 8 completions per prompt, training on our email research dataset.

## The Reward Function

Designing an effective reward function was crucial for training ART·E. We used a multi-component reward function that evaluates:

### Answer Accuracy (Primary Reward)
The main reward component measures whether the agent's final answer matches the expected answer. We use a fuzzy matching system that can handle:
- Different phrasings of the same answer
- Partial matches for multi-part questions
- Synonyms and related terms

### Tool Use Efficiency (Penalty)
We penalize inefficient tool use to encourage the agent to:
- Use the minimum number of queries necessary
- Avoid redundant searches
- Prioritize relevant information

### Format Compliance (Bonus)
We provide small bonuses for:
- Proper citation of sources
- Clear reasoning traces
- Well-structured responses

### The Complete Reward Function

```python
def compute_reward(prompt, response, expected_answer):
    # Primary reward: answer accuracy
    accuracy_score = compute_accuracy(response.final_answer, expected_answer)
    
    # Penalty for excessive tool use
    efficiency_penalty = -0.01 * response.num_tool_calls
    
    # Bonus for proper formatting
    format_bonus = 0.1 if has_proper_citations(response) else 0
    
    # Combine components
    total_reward = accuracy_score + efficiency_penalty + format_bonus
    
    return total_reward
```

## Training Process

### Dataset
We curated a dataset of email research tasks consisting of:
- 5,000 training examples
- 500 validation examples
- 1,000 test examples

Each example includes:
- A research question
- Access to an email repository
- The expected answer
- Metadata about difficulty and required information

### Training Configuration

- **Base Model**: Qwen 2.5 32B
- **Training Steps**: 500
- **Batch Size**: 64 (8 groups of 8)
- **Learning Rate**: 1e-6 with cosine scheduling
- **KL Penalty**: 0.01 (to prevent reward hacking)
- **Hardware**: 8x A100 GPUs
- **Training Time**: ~12 hours

### Training Dynamics

The training process showed several interesting patterns:

1. **Early Phase (Steps 0-100)**: The model learned basic tool usage patterns, discovering how to effectively search and retrieve emails.

2. **Middle Phase (Steps 100-300)**: The model developed more sophisticated strategies, such as following citation chains and cross-referencing information from multiple sources.

3. **Late Phase (Steps 300-500)**: Performance plateaued as the model refined its strategies and learned to handle edge cases.

## Results

### Benchmark Performance

We evaluated ART·E against several baselines on our email research benchmark:

| Model | Accuracy | Avg. Tool Calls | Avg. Latency |
|-------|----------|-----------------|--------------|
| GPT-4o | 72.3% | 12.4 | 8.2s |
| Claude 3.5 Sonnet | 74.1% | 11.8 | 7.9s |
| o3 | 78.5% | 10.2 | 12.4s |
| **ART·E** | **81.2%** | **9.8** | **6.1s** |

ART·E outperforms o3 by 2.7% while using fewer tool calls and achieving lower latency.

### Error Analysis

Analyzing the remaining errors revealed:

1. **Complex temporal reasoning** (23% of errors): Questions requiring understanding of event sequences over long time periods
2. **Multi-hop inference** (31% of errors): Information spread across many documents requiring multiple reasoning steps
3. **Ambiguous references** (28% of errors): Pronouns or references that could refer to multiple entities
4. **External knowledge** (18% of errors): Questions requiring knowledge not present in the emails

### Ablation Studies

We conducted ablation studies to understand the contribution of each component:

| Component Removed | Accuracy Drop |
|-------------------|---------------|
| GRPO Training | -12.3% |
| Efficiency Penalty | -3.1% |
| Format Bonus | -0.8% |
| KL Penalty | -4.5% (reward hacking) |

These results confirm that GRPO training is the primary driver of performance, with the KL penalty being crucial for stable training.

## Key Insights

### 1. RL Training Unlocks Agent Capabilities
Our experiments show that reinforcement learning can unlock agent capabilities that are difficult to achieve through supervised fine-tuning alone. The agent learns strategies that weren't explicitly demonstrated in the training data.

### 2. Reward Function Design is Critical
The multi-component reward function was essential for training effective agents. Pure accuracy-based rewards led to inefficient tool use, while pure efficiency rewards led to incomplete research.

### 3. Smaller Models Can Match Larger Ones
With proper RL training, a 32B parameter model can match or exceed the performance of much larger models on specialized tasks. This suggests that training methodology can be as important as model scale.

### 4. GRPO is Effective for Agent Training
GRPO's sample efficiency and ability to handle sparse rewards make it particularly well-suited for training agents in complex environments.

## How to Use ART·E

ART·E is available as part of the ART framework. Here's a quick example:

```python
from art import ARTAgent, EmailTools

# Initialize the agent
agent = ARTAgent.from_pretrained("openpipe/art-e-email-agent")

# Set up email tools
tools = EmailTools(
    email_server="imap.example.com",
    credentials=("user", "password")
)

# Run a research query
result = agent.research(
    query="What were the key decisions made in the Q4 planning meeting?",
    tools=tools
)

print(result.answer)
print(result.sources)
```

## Future Work

We're continuing to improve ART·E and the ART framework:

1. **Multi-modal support**: Extending the agent to handle images, PDFs, and other document types
2. **Longer context**: Training agents that can handle larger email repositories
3. **Collaborative agents**: Training multiple agents that can work together on complex research tasks
4. **Domain adaptation**: Fine-tuning ART·E for specific industries or use cases

## Try It Yourself

You can try ART·E today:

1. **ART Framework**: [github.com/openpipe/ART](https://github.com/openpipe/ART)
2. **ART·E Model**: [huggingface.co/openpipe/art-e-email-agent](https://huggingface.co/openpipe/art-e-email-agent)
3. **Documentation**: [docs.openpipe.ai/art](https://docs.openpipe.ai/art)

## Conclusion

ART·E demonstrates the power of reinforcement learning for training specialized AI agents. By combining GRPO training with carefully designed reward functions, we've created an email research agent that outperforms much larger models while being more efficient.

We believe this approach can be applied to many other domains where complex, multi-step reasoning is required. We're excited to see what the community builds with the ART framework.

---

*Kyle Corbitt is the CEO and co-founder of OpenPipe. He previously led the ML infrastructure team at Anyscale and is passionate about making AI training more accessible.*

---

**Note**: This article was originally published at https://openpipe.ai/blog/art-e-mail-agent. All credit for the content goes to OpenPipe and the original author.