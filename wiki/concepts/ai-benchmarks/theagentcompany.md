---
title: "TheAgentCompany"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags: [benchmark, evaluation, ai-agents, software-engineering]
sources:
  - title: "TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks"
    arxiv: "2412.14161"
    year: 2024
related_concepts:
  - "[[crmarena-pro]]"
  - "[[swe-bench]]"
  - "[[mle-bench]]"
  - "[[remote-labor-index]]"
---

# TheAgentCompany

TheAgentCompany is a benchmark that evaluates LLM agents by placing them in a simulated full-company environment and testing their ability to perform consequential real-world work tasks. Rather than testing isolated skills, TheAgentCompany creates a sandbox that mimics the tools, workflows, and interactions of an actual software company, providing one of the most holistic evaluations of agent work capability.

## What It Measures

TheAgentCompany evaluates agents on their ability to:

- **Perform professional work tasks**: Complete realistic tasks that mirror what employees at a software company do — writing code, reviewing pull requests, writing documentation, managing projects
- **Navigate workplace tools**: Use simulated versions of common workplace tools including Git, project management software, communication platforms, and internal wikis
- **Collaborate and communicate**: Interact with simulated colleagues to gather requirements, ask questions, and coordinate work
- **Manage multi-step projects**: Handle tasks that span multiple days and require coordination across different tools and systems
- **Follow organizational processes**: Adhere to company workflows, coding standards, and review processes

The benchmark provides end-to-end evaluation of an agent's ability to function as a productive member of a professional team.

## Data/Methodology

TheAgentCompany creates a comprehensive simulated work environment:

- **Full company simulation**: The benchmark includes a simulated company with an organizational structure, codebase, communication channels, project boards, and internal documentation
- **Diverse task types**: Tasks span software engineering, data analysis, project management, documentation, and administrative work
- **Realistic tool integrations**: Agents interact with simulated versions of GitLab, RocketChat, ownCloud, Plane (project management), and other common workplace tools
- **Multi-day workflows**: Some tasks require sustained effort across multiple interaction sessions, testing the agent's ability to maintain context and progress
- **Colleague interactions**: Agents can ask simulated colleagues for clarification, code reviews, and approvals, testing interpersonal and collaborative capabilities
- **Automated and human evaluation**: Task completion is verified through a combination of automated checks (e.g., did the code pass tests?) and evaluation rubrics for subjective quality

## Key Results

- Agents can complete many individual tasks but struggle with complex multi-step workflows that require sustained context management
- Software engineering tasks (code writing, debugging) are more tractable for agents than tasks requiring communication and project management skills
- The ability to effectively use workplace tools (navigation, search, collaboration) is a significant differentiator between successful and unsuccessful agent runs
- Agents frequently fail not because they lack technical capability but because they cannot navigate the organizational context — missing relevant documentation, asking the wrong colleagues, or not following established processes
- Performance varies significantly across task categories, with the largest gaps appearing in tasks that require cross-functional coordination

## Related Benchmarks

- **[[crmarena-pro]]**: Evaluates agents on business scenarios using Salesforce; TheAgentCompany provides a broader workplace simulation
- **[[swe-bench]]**: Tests software engineering tasks in isolation; TheAgentCompany embeds SWE tasks in a realistic work context
- **[[mle-bench]]**: Focuses on ML engineering competitions; TheAgentCompany covers broader professional work
- **[[remote-labor-index]]**: Measures automation of remote work, complementing TheAgentCompany's workplace simulation approach

## Connections to Other Wiki Concepts

TheAgentCompany is directly relevant to [[ai-and-labor]] and the [[future-of-work]] discourse. The benchmark provides concrete evidence about which professional tasks AI agents can and cannot handle, informing discussions about [[job-displacement]] and [[human-ai-collaboration]]. It connects to [[digital-workplace]] concepts and the growing ecosystem of [[ai-productivity-tools]]. TheAgentCompany also raises questions about [[ai-deployment]] — how organizations should integrate AI agents into existing workflows, and what guardrails are needed for responsible deployment.
