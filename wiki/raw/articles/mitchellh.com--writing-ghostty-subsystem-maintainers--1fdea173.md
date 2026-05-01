---
title: "Welcoming Ghostty Subsystem Maintainers"
url: "https://mitchellh.com/writing/ghostty-subsystem-maintainers"
fetched_at: 2026-05-01T07:02:02.937288+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Welcoming Ghostty Subsystem Maintainers

Source: https://mitchellh.com/writing/ghostty-subsystem-maintainers

I'm excited to share that there are
eight
newly promoted
subsystem maintainers for
Ghostty
. These
are the first maintainers to be promoted since the project's
creation, and I'm thrilled to see the project grow in this way.
Adding additional, independent maintainers is an important part
of any open source project's long-term health and stability.
While Ghostty has only been public for a little over a month,
the project was in private beta for almost two years. A benefit
of this is that members of the community have already made
significant contributions to the project and repeatedly shown
themselves to be kind and helpful to others.
All of the new
maintainers announced today were part of the private beta and have
been active contributors and community members for months if not
over a year. They each have dozens of individual merged PRs into
Ghostty already, but have also been helpful and active in issues,
Discord, etc.
Please join me in welcoming the following maintainers, in
alphabetical order:
Subsystems
We've decided to follow a subsystem maintainer model for Ghostty.
Rather than promoting "core maintainers" who are responsible for
every part of the project, we've identified key subsystems within
the project with subject matter experts and promoted these people
to a position of authority within their respective subsystems.
The exact "subsystems" emerge organically as contributors show
themselves to be knowledgeable, excited, and interested in a
particular area of the project. To start, we've identified the
following subsystems, in no particular order:
Terminal Emulation
- Responsible for escape sequences,
pty handling, subprocess management, etc.
GTK
- Responsible for the GTK app runtime and Linux in general.
Also includes the lower level X11/Wayland integrations, cgroup
management, and so on.
macOS
- Responsible for the macOS app runtime and macOS-specific
features, configurations, etc. No one was promoted to this subsystem
today, but we expect to add maintainers here in the future.
Font
- Responsible for font discovery, rasterization, shaping,
coloring, etc. Anything font-related. Covers all platforms,
so these people have expertise with FreeType, CoreText, etc.
Renderer
- Responsible for core rendering abstractions as well
as specific renderers like OpenGL and Metal. More generally responsible
for any issues related to rendering.
Shell
- Responsible for shell completions, shell detection, and
any other shell interactions. Expected to cover all supported
shells, including bash, zsh, fish, etc.
Discord Bot
- Responsible for the Discord bot, which is an
important part of our community management and support.
Privileges, Responsibilities, and Goals
The goal of promoting subsystem maintainers is to enable Ghostty
to scale more effectively. Issues can be resolved more quickly and
improvements can be shipped faster when trusted maintainers have
autonomy to make decisions within their subsystems.
Subsystem maintainers have the ability to independently define the
roadmap of their respective subsystems, triage issues, merge pull
requests, etc.
Subsystem maintainership is a voluntary role and maintainers are not
expected to dedicate any amount of time to the project. However, if a
maintainer is inactive for a long period of time, they may be removed from
the maintainers list to avoid bitrot or outdated information.
Notably, maintainers have NO OBLIGATION to review pull requests or issues
in their subsystem. They have full discretion to review or not review
anything they want. This isn't a job! It is a role of trust and authority
and the expectation is that maintainers will use their best judgement
and work on what they find interesting and rewarding for themselves and
the project.
For more specific details on the subsystem maintainer process,
see the
CODEOWNERS
file. There is a detailed comment that outlines the entire system.
Welcome and Thanks
I want to extend a personal thank you to each of the new maintainers
both for accepting the role as well as their already significant
contributions to the project. Besides that, they've all just been
wonderful people to get to know and work with.
Please join me in welcoming these new maintainers to the Ghostty
project. 👻
