---
type: article
date: 2026-01-05
source: https://hugobowne.substack.com/p/how-to-build-an-ai-agent-with-ai
title: "How to Build an AI Agent with AI-Assisted Coding"
author: Hugo Bowne-Anderson
tags: [ai-assisted-coding, agent, coding-agent]
---

Workshops

## How to Build an AI Agent with AI-Assisted Coding

## Or 7 Ways to Supercharge your AI-Assisted Dev Stack

Hugo Bowne-Anderson , Isaac Flath , and Eleanor Berger Jan 05, 2026 25 5 3 Share Eleanor Berger (OKIGU, ex-Microsoft, ex-Google) and Isaac Flath (Kentro Tech, ex-Answer.AI) recently showed me how to build a simple multi-agent system from scratch: context-setting, spec-first, delegation, observability... all using AI-assisted coding!

This workshop will save you 100s of hours if you internalize & practice the lessons about AI usage in coding.

I decided to write a post for those who do not have 90 minutes to watch the entire workshop.

This post captures the key concepts, tools, and methodologies. All the code is here .

👉 Eleanor & Isaac are teaching their next cohort of their Elite AI Assisted Coding course starting January 13. They’re kindly giving readers of Vanishing Gradients 25% off. Use this link . 👈

We’re also doing a free livestreamed podcast about Effective AI-Assisted Coding on January 12, if you’d like to join! ​ Register here to join live or get the recording afterwards .

Thanks for reading Vanishing Gradients! Subscribe for free to receive new posts and support my work.

Subscribe

## Key Takeaways for Using AI Assistants Effectively

## Overall Philosophy and Mindset

- Don’t “vibe code.” Eleanor & Isaac advocate for a structured approach rather than “vibe coding,” which they describe as going aimlessly and trying different things.

- Stay mentally active and use it as a learning tool. Isaac advises, “make sure you’re staying active, make sure you’re thinking about how things are working, make sure you’re learning the whole time.” He also mentions that when an AI introduces something new, it’s an opportunity to learn and upskill.

- The more you lean on AI to write the code, the more value you bring into the equation by being engaged, opinionated, and in control.

## Planning and Specification

- Plan before you implement. Eleanor emphasizes taking things “step by step” and doing “planning with AI” before starting implementation. This is demonstrated by having AI generate a detailed plan.md file before writing any code.

- Be verbose and specific with instructions. Eleanor states that if you don’t give the agent specific instructions, “it just sort of imagines something” that might not be what you want. She prefers the agent to follow her explicit directions and design .

- Consider dictating your prompts. Eleanor finds that dictating helps her be “more verbose” and “clearer” without filtering herself. Also that LLMs are very good at interpreting the spoken word!

- Review the AI’s plan. Isaac stresses the importance of reading the plan the AI generates to ensure it makes sense and to correct any misunderstandings or poor choices, which Eleanor then demonstrates by removing an unnecessary library from the plan.

- Use “living documentation” for context. They create an AGENTS.md file with project-level instructions and tell the agent to treat it as “living documentation,” appending new information and learnings to it as the project progresses.

## Execution and Workflow

- Break the work into controlled steps. The initial prompt explicitly tells the agent to work in three distinct, planned steps and to stop after each one is complete and tested. This is then executed by giving separate commands for each step.

- Manage the context window actively. Eleanor prefers to “exercise control and actually start a new session” for each major task rather than relying on a long conversation history. She avoids relying on automatic conversation.

## The Project: A Wikipedia Flashcard Generator

The goal was to build a command-line tool that takes a user’s topic, researches it on Wikipedia, synthesizes the information, and generates educational flashcards.

The architecture is a sequential multi-agent system where the output of one agent becomes the input for the next:

- Wikipedia Search Agent : Receives a user query, searches Wikipedia for 2-3 relevant articles, and fetches their full text.

- Analysis & Summary Agent : Combines the text from the articles and produces a coherent summary of 500-1500 words.

- Flashcard Generator Agent : Processes the summary to create 20-50 question-and-answer flashcards.

The final output is a Markdown file containing the flashcards. The tech stack includes Python 3.12+, Pydantic AI for agent orchestration, the OpenAI GPT-5.1 model (though the agent later defaulted to GPT-5), and the Wikipedia Python library.

## Setting the Stage: The AGENTS.md Context File

- Before implementing the AI assistant, Eleanor established a foundational context in an agents.md file. This file provides high-level, persistent instructions that guide the agent’s behavior throughout the project. Key instructions included:

Git Workflow : Commit frequently with clear messages, sign commits to distinguish AI work from manual work, and work within a single branch for this workshop.

- Research : Consult up-to-date documentation via web searches rather than relying solely on pre-trained knowledge.

- Environment Management : The agent is responsible for installing necessary packages.

- Coding Style : Follow PEP 8, prioritize readability over premature optimization, write modular code, and use docstrings. For this project, tests were explicitly excluded to save time.

- Living Documentation : The agent was instructed to treat AGENTS.md as a living document, adding notes, discovered links, or relevant information as it worked.

The Living Documentation is such a useful practice because it’s is the closest we’ve got and the simplest possible implementation of a learning agent that gets better over time.

Eleanor Burger : These agents are very good at git these days because it’s well represented in training data, right? But they’re very proficient. They can write commit messages which are a bit long sometimes but we can fix that.

## The Core Technique: Specification-Driven Development

The session’s central theme was replacing improvisational coding with a deliberate, plan-first approach . Instead of giving the AI a vague goal, Eleanor dictated a comprehensive specification covering the entire project.

Eleanor Burger : If we don’t give the agent instructions... the AI never comes back and says like, “Hey, you didn’t give me enough instructions, compile error,” right? It always does something. And when you don’t specify what it is you want it to do, it just sort of imagines something.

She used voice dictation to provide a verbose and detailed prompt. This method encourages a more natural, stream-of-consciousness flow of instructions, which LLMs are well-equipped to parse. The detailed specification covered the roles of each of the three agents, their data models (using Pydantic for structured inputs/outputs), and the exact three-step implementation process to follow.

## Phase 1: AI-Assisted Planning

With the specification dictated, the first task assigned to the AI was not to write code, but to create a detailed implementation plan . Using a capable reasoning model (GPT-5, in this case), the agent was instructed to:

- Research the specified libraries (Pydantic AI, Wikipedia, Tavily for Search. etc…).

- Formulate a detailed, step-by-step plan for building the application.

- Save this plan to a temporary file (tmp/plan.md).

This step is critical. Before implementation, the developer must review and refine the AI’s plan . During the review, Eleanor removed an unnecessary alternative library the AI suggested and trimmed boilerplate sections like “Future Enhancements,” ensuring the final plan was lean and perfectly aligned with the project goals.

Key point : Eleanor’s process really demonstrated the value of knowing the model well; GPT-5 tends to to be overly verbose and suggest things you didn’t ask for in detail that isn’t necessary, Claude is prone to taking actions you didn’t specific, etc ... when you know the model well, you can adapt how you control it.

## Phase 2: Step-by-Step, Controlled Execution

Once the plan was finalized, the implementation began. This phase highlighted several advanced techniques:

- Model Switching : Eleanor switched from GPT-5 (used for planning) to Claude Sonnet for the implementation phase. This demonstrates choosing the right tool for the job: a powerful model for complex reasoning and planning , and a faster, more cost-effective model for code generation and execution .

- Executing in Chunks : Instead of asking the AI to build the whole project at once, she instructed it to execute the plan one step at a time (e.g., “execute step one of the plan”).

- Managing Context : For each new step, she started a fresh chat session. This prevents the context window from becoming cluttered with irrelevant history, a phenomenon known as “context rot,” which can degrade model performance. The plan file and the code itself serve as the persistent, reliable context between steps.

Key point : managing context in a persistent markdown file means you have visibility and control over it. In contrast, letting the agent manage the context as part of the conversation obscures things and gives you less control.

Following this process, the agent autonomously created the file structure, wrote the Python code for each of the three agents, tested its work, and committed the changes, completing the project’s core functionality with minimal human intervention.

## Phase 3: Instrumenting for Observability

- With the application working, the final task was to add observability using Pydantic’s Logfire . The AI was prompted to research and integrate Logfire to trace the application’s execution. In a few minutes, it added the necessary instrumentation.

The Logfire dashboard provided a detailed, hierarchical view of the agent’s operations. It traced each LLM call, showing the exact prompts, model parameters, and outputs. This level of visibility is invaluable for debugging complex agentic systems, making it easy to understand why an agent behaved in a certain way.

Key point : a combination of good documentation and a model that is directed to read and follow it resulted in quick and accurate followup. That’s better than relying on the model’s baked-in knowledge.

## Summary of Workflow

The step-by-step workflow for building software with AI assistants is as follows:

Set Up Project Context : Create a foundational context file (e.g., AGENTS.md) that provides the AI with high-level instructions. This includes rules for the development process (like Git usage), coding style, and instructing the AI to treat the file as “living documentation” that it can update with its findings].

- Provide a Detailed Specification : Verbally dictate a comprehensive overview of the project to the AI. This “brain dump” includes the project’s architecture, the specific agents to be built, their individual tasks, the desired tech stack (Pydantic AI, OpenAI models, etc.), and the overall program flow. Dictation is used because it encourages being more verbose and clear.

- Generate an Implementation Plan : Task the AI with taking the detailed specification, conducting any necessary research on libraries and tools, and creating a detailed, step-by-step implementation plan. The plan is to be saved in a separate file (e.g., plan.md).

- Review and Refine the Plan : The human developer must carefully read and review the plan generated by the AI. This is a crucial step to correct the AI’s course, remove any irrelevant suggestions (like an alternative library or “free enhancements”), and ensure the plan aligns with the project’s goals before any code is written.

- Execute the Plan in Controlled Steps : Instead of implementing the whole project at once, the developer instructs the AI to execute the plan one step at a time. A new chat session is started for each major step to keep the context window clean and focused. For example, the first prompt is to “read plan.md and execute step one of the plan”.

- Iterate Through Each Step : This process is repeated for each subsequent step outlined in the plan. After the first step is complete, a new chat is started to instruct the AI to work on step two, and then again for step three. This creates a controlled, sequential, and iterative workflow.

- Verify Functionality : Throughout the process, the AI is instructed to test its changes before committing. The human developer also manually runs the script after each major step is completed to confirm that the implementation is working correctly.

- Conduct a Final Review : Before releasing the project, the speaker emphasizes the need for a final, thorough code review to ensure it is free of issues, secure, and efficient. This review can also be assisted by AI code review tools.

## Key Takeaways

- Plan, then execute : A detailed, human-reviewed plan is the key to controlling AI agents and ensuring the final product meets your requirements.

- Use AI as a thought partner : Collaborate with AI during the planning phase. Use its research capabilities to structure the project before writing a single line of code.

- Break down complex tasks : Guide the AI through a project in discrete, logical steps. Starting a fresh session for each major step maintains a clean context and improves reliability.

- Choose the right model for the task : Leverage different models for their strengths, such as using powerful models for planning and faster, cheaper models for implementation.

- Observability is crucial : For any non-trivial agentic system, instrumenting with tools like Logfire is essential for debugging and understanding agent behavior.

- Maintain human oversight : The developer’s role shifts from a line-by-line coder to an architect, planner, and quality assurer. Always review AI-generated code before deployment.

## Conclusion

I hope you learnt a few things here that will help you use AI agents more effectively!

I’ve found moving from ad-hoc prompting to a structured, specification-driven workflow has helped transform my use of AI assistants from unpredictable and unreliable tools into more powerful and reliable collaborators. This type of discipline approach helps me build complex systems far quicker than ever before (including systems I would never have dreamt of building previously!) and I also get to stay firmly in control of the architecture and quality. May you live in interesting times!

The complete code from this session is available here on GitHub .

👉 Eleanor & Isaac are teaching their next cohort of their Elite AI Assisted Coding course starting January 13. They’re kindly giving readers of Vanishing Gradients 25% off. Use this link . 👈

We’re also doing a free livestreamed podcast about Effective AI-Assisted Coding on January 12, if you’d like to join! ​ Register here to join live or get the recording afterwards .

## Want to Support Vanishing Gradients?

If you’ve been enjoying Vanishing Gradients and want to support my work, here are a few ways to do so:

🧑‍🏫 Join (or share) my AI course – I’m excited to be teaching Building AI Applications for Data Scientists and Software Engineers again in March with Stefan Krawczyk (Agentforce, Salesforce). It’s our final cohort and we’re offering Vanishing Gradients readers 25% off with this link . If you or your team are working with LLMs and want to get hands-on, I’d love to have you.

📣 Spread the word – If you find this newsletter valuable, share it with a friend, colleague, or your team. More thoughtful readers = better conversations.

📅 Stay in the loop – Subscribe to the Vanishing Gradients calendar on lu.ma to get notified about livestreams, workshops, and events.

▶️ Subscribe to the YouTube channel – Get full episodes, livestreams, and AI deep dives. Subscribe here .

💡 Work with me – I help teams navigate AI, data, and ML strategy. If your company needs guidance, feel free to reach out by hitting reply.

Thanks for reading Vanishing Gradients! Subscribe for free to receive new posts and support my work.

Thanks for reading Vanishing Gradients! Subscribe for free to receive new posts and support my work.

Subscribe If you’re enjoying it, consider sharing it, dropping a comment, or giving it a like —it helps more people find it.

Until next time ✌️

Hugo

Thanks for reading Vanishing Gradients! Subscribe for free to receive new posts and support my work.

Subscribe 25 5 3 Share A guest post by Isaac Flath Isaac is an independent consultant who has helped many companies incorporate AI into their products. I've taught AI efficiency to companies for years and worked for tech startups and cutting edge labs. A guest post by Eleanor Berger intellectronica.net ・ agentic-ventures.com ・ okigu.com Subscribe to Eleanor