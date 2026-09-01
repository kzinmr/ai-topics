---
title: "Reducing codebase cognitive debt through... quizzes?"
url: "https://martinalderson.com/posts/codebase-cognitive-debt-quizzes/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-09-01T10:00:43.885230+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Reducing codebase cognitive debt through... quizzes?

Source: https://martinalderson.com/posts/codebase-cognitive-debt-quizzes/?utm_source=rss&utm_medium=rss&utm_campaign=feed

Like many, when I'm building with coding agents, one of the "worst" problems is the codebase
feels
like it is often evolving faster than I can keep up with it. This cognitive debt builds up quietly - nothing is broken, but you gradually have this feeling of not being
totally
on top of what is going on.
One remarkably effective technique I stumbled on is asking the agent to
quiz
you on the code base. A simple prompt like:
hi, please quiz me about this codebase.
i want 5 questions of increasing difficulty - then explain to me at the end what i got wrong about my understanding. use the askuserquestiontool
Produces a simple quiz you can answer.
The best bit is chatting to the agent about the ones you got wrong. It has the context of what you thought versus what the code actually does, so it can explain the gap far better than it could if you'd just asked it to describe that part of the codebase itself.
You can of course use this for non code tasks too, e.g. complex spreadsheets or document sets.
I've had a lot of success with this - if I'm working on a complex refactor with a difficult plan, asking the agent to quiz me
about
the plan or part of the project in question before starting seems to make me catch issues more than trying to read pages upon pages of
Claudish
.
I've tended to find my
perception
of the cognitive debt is (usually!) far more than the reality, and this helps nullify the sinking feeling that the codebase/project is running far ahead of my understanding.
You could go a step further and enforce you passing a quiz about a PR too before you allow the agent to create one.
Sometimes with agents the best options are the simplest.
