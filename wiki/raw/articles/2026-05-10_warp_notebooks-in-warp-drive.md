---
title: "Introducing Notebooks in Warp Drive"
source: "Warp Blog"
url: "https://www.warp.dev/blog/notebooks-in-warp-drive"
scraped: "2026-05-10T01:27:53.649310+00:00"
lastmod: "2026-04-24T14:39:45.000Z"
type: "sitemap"
---

# Introducing Notebooks in Warp Drive

**Source**: [https://www.warp.dev/blog/notebooks-in-warp-drive](https://www.warp.dev/blog/notebooks-in-warp-drive)

Product
Introducing Notebooks in Warp Drive
Noah Zweben
April 2, 2024
Notebooks are like runbooks that live next to your command line in the terminal. They’re easy to find, run, and edit. Every Notebook can include executable commands or Workflows, so you can step through multi-step playbooks without copy, pasting, or context-switching. Plus, you can export Notebooks in Markdown format, so there’s no lock in.
New Notebooks in Warp Drive
are available today.
Your team’s runbooks should live in the terminal
Traditional documentation solutions aren’t ideal for terminal workflows.
Most teams keep contextual documentation for projects in README files. If you want to run a command referenced in a file, you have to copy / paste the code. If you want to edit a README, you have to open a text editor and check-in a pull request. But, what do you do with your more universal documentation that doesn’t tie neatly to any one project or repo?
Teams that want to centralize their docs might adopt a browser-based documentation solution. These apps move the docs further away from where engineers are getting work done. It’s a long journey to the browser with ample room for distractions. If you manage to locate the right doc, you still have to copy / paste the commands into your terminal, slowing you down at every step. If you find content that’s out-of-date, you have to completely stop what you’re doing to go make a change.
Documentation ends up sprawled out and stale, in every place except where your team needs it: on the command line.
What if we could make terminal-specific documentation easier to find, edit, and run with less context switching?
Terminal-based Notebooks are easier to find, run, and edit
With new Notebooks in Warp Drive, your terminal-specific documentation stays in your terminal.
Notebooks are Markdown-flavored, like you’d expect from your favorite note editors, but they can also include interactive code blocks with runnable commands, like a Jupyter notebook.
With Notebooks, you can execute commands with a click or a keypress, in a pane right next to your command line input.
When you need to find documentation, you can use Command Search to find Notebooks by name or contents in the same place you’d browse your command history. There’s no need to open your web browser or pop into a different application.
The lightweight editor in Warp Drive lets you make and save changes immediately. Changes sync in real-time to everybody who has access, so your docs stay fresh and up-to-date.
Now your whole team can find the right docs where they need them. Everybody can work through complex multi-step processes faster.
Publish updates across multiple Notebooks with atomic Workflows
One of the more novel aspects of Notebooks in Warp is that they’re composable with other objects in your Warp Drive, like Workflows. Workflows are basically parameterized commands you can name, save, and reuse—more powerful than aliases but simpler than a script.
Now you can also embed those Workflows into your Notebooks.
If you ever need to edit a shared Workflow because the right command for a tool or process changed, you can make that edit at the Workflow level and it will sync to every Notebook where it’s referenced.
Suddenly you’ve updated a whole set of docs at once, instead of going through each one file by file.
Your Warp Drive contains a “single source of truth” for the correct workflows to use, and those correct workflows show up everywhere you need them.
Simplify onboarding for teams with Notebooks
While Notebooks were in a private beta, we heard from engineering leaders who found Notebooks especially useful for getting new teammates up-and-running.
Dan Murdock is a Software Quality Assurance Analyst at Palo Alto Software. Dan has been using Notebooks as an easy way to onboard new team members. Here’s what Dan had to say,
“Warp is so user friendly for new people, especially for engineers who are less familiar with the terminal. The Notebooks include the commands with parameters they need to run to set up their dev environments and they can learn what to put in their host files.”
“We use lots of different tools for documentation. Documentation gets everywhere. When I can, I find it beneficial to have documentation in Warp Drive because you can open the side panel and click through, step by step.”
“It’s a lot easier to keep docs up-to-date in Warp Drive because your command line is right there. You can edit on the fly. And being able to find a Notebook or Workflow with the command bar is glorious.”
That’s some pretty glorious feedback!
How to create your first Notebook
When you’re ready to create your first Notebook, navigate to Warp Drive and click the + icon to start a new Notebook. (Or, use the keyboard shortcut SHIFT + OPTION + CMD + J)
Name your Notebook and start typing. The editor will recognize Markdown conventions like ### for headings or
`
for code blocks.
Use the + icon in the editor to embed existing Workflows.
To share your Notebook with your team, drag it from your Personal drive into a shared Team drive. This will allow your colleagues to find your Notebook and give them edit access, too.
If you need a little more guidance, look for the system-created Notebook named Getting started with Notebooks in your Personal drive. You can search for it using the Command Palette (CMD - P). This example Notebook includes supported markdown types and more helpful keyboard shortcuts you can use.
What’s next for Notebooks
We’re working on some nice enhancements for Notebooks including better linkability across objects in Warp Drive and permalinks so you can link out to Warp Notebooks from your docs in other apps.
This week’s release will also include the ability to export your Notebooks in .md format, so you don’t need to worry about getting locked in.
Be sure to check the
weekly Changelog
for updates.
Try Notebooks in Warp Drive today
Notebooks are available for all users and you can create as many as you’d like in your Personal Warp Drive. For teams using a shared Warp Drive, shared Notebooks are in free preview.
Please give Notebooks a try for your terminal-specific documentation, and let us know what you think!
You can
file an issue on GitHub
or chat with us in
Warp’s Discord community
.
‍
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
