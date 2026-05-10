---
title: "The Pain and the Poetry of Python"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/pain-poetry-python/"
scraped: "2026-05-10T01:27:58.500296+00:00"
lastmod: "2023-09-01T20:24:40Z"
type: "sitemap"
---

# The Pain and the Poetry of Python

**Source**: [https://www.pinecone.io/blog/pain-poetry-python/](https://www.pinecone.io/blog/pain-poetry-python/)

←
Blog
The Pain and the Poetry of Python
Zachary Proser
Aug 31, 2023
Engineering
Share:
Jump to section:
Abandon all hope ye who enter dependency hell
Patterns for Python projects
Why we chose Poetry for the Pinecone Python client
From pain to poetry and beyond
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
The ecosystem of tools for packaging, testing, distributing, and testing Python projects is overwhelming, especially if you’re coming to Python from other languages.
In this post, we’ll survey the evolution of Python tooling from its inception in 1991 through the present day, touching on significant milestones. We’ll explain each tool’s benefits, the problems it addresses, and any configuration files you’ll find associated with it in Python projects.
After reading this post, you’ll have a richer understanding of the many setup, testing, and packaging patterns you’re likely to find in open-source Python projects and be better equipped to work with them. You’ll see how to migrate your project to a modern dependency management and packaging tool such as
Poetry
.
We’ll explain why we are
converting
the
Pinecone Python client
to Poetry, the new contributor-facing guides we’ve added to ease this migration, and how this makes the project easier to develop locally and even within Jupyter Notebooks and alongside popular libraries such as LangChain.
Along the way, we’ll take an unflinching look at some of the pain involved in developing Python projects to set the stage for understanding how the latest tooling can make developers’ lives easier.
Abandon all hope ye who enter dependency hell
Guido van Rossum released Python on February 20, 1991. At the time of this writing, that was 32 years ago. To understand why today’s preferred tools work the way they do, we must first look backward to understand the evolution of Python.
If you’ve ever worked with Python, you’re probably familiar with the following tools, patterns, digital duct tape, and the headaches that come with a scattered landscape of options.
Most readers familiar with Python have probably run
pip install -r requirements.txt
to tell the pip package manager binary to read a requirements text file, which lists the dependencies (external libraries) required by a given Python script.
pip install
is probably the most common and straightforward way to get up and running with a given Python program. Now, consider why this typical pattern is fraught with complexity and suffering.
Until macOS Catalina (10.15), released in 2019, Python 2 was pre-installed on your OSX machine, requiring developers who needed Python 3 to install it separately. Folks in a hurry could accidentally execute commands against
python
instead of
python3
, leading to errors.
The two versions also had dependency conflicts because each maintained a separate
site-packages
, the directory where Python installs packages, leading to potential duplicate packages and version incompatibility on the same system.
The shebang lines at the top of Python scripts that signal which interpreter were equally confusing.
#!/usr/bin/env python
defaulted to Python 2, which could be problematic for code intended to be run by Python 3.
This confusion spread to the use of pip itself. You might have meant to
pip3 install
a given requirements.txt file because
pip3
is not the same binary as
pip
. If you have Python 2 and Python 3 installed on your system,
pip
and
pip3
will install packages in different locations to avoid conflicts.
However, if you only have Python 3 installed, pip might be an alias for
pip3
; in that case, they would install packages in the same location.
Plenty of shims, patches, and bandaids emerged to help address this pain. The
python-is-python3
package explains: “This is a convenience package which ships a symlink to point the
/usr/bin/python
interpreter at the current default
python3
. It may improve compatibility with other modern systems, whilst breaking some obsolete or 3rd-party software.“
Pyenv is a tool for managing multiple versions of Python on a single machine, so you can quickly toggle between versions (which might be necessary to fix a bug in library A and then continue developing your project B - both of which use incompatible Python versions).
Pyenv is very convenient if you regularly need to toggle between Python versions, yet it adds complexity and may not play nicely with external scripts and tools that just want to call
python
.
Don’t forget that you need to modify your shell configuration to get
pyenv
to work correctly - and remember to do so across every machine you work on. It can also automatically read
.python-version
files if you include them in your project, which is a nice technical solution. But there’s also the human element; not everyone on your team may want to run Pyenv.
Patterns for Python projects
We’ve surveyed some of the gotchas in managing different versions of Python on a single machine. Let’s now take a step back and consider the evolution of tooling from the open-source Python project maintainer’s perspective.
At Pinecone, I’m fortunate to work with highly experienced developers.
We're hiring
if you’re looking to join a team with extensive engineering talent.
In a recent conversation with a colleague who has been using Python for 25 years, I was lamenting the many tools and patterns you need to grok to maintain Python projects. “It used to be a lot worse,” he explained.
You used to go and get your Python “eggs” from “The Cheese Shop,” which was the original name for the PyPi (Python Package Index) we know and use today; whenever you
pip install
a dependency.
The Cheese Shop referenced Monty Python’s The Cheese Shop sketch, featuring a Cheese Shop devoid of actual cheese. The reference was a tongue-in-cheek indication that the index was mostly empty yet had potential.
Here’s a chronological list of the methods for maintaining Python projects and their dependencies (as well as, in some cases, handling everyday needs such as packaging and isolation via tools like virtualenv):
1. Manual Dependency Management (Pre-2000s)
Benefits
: Full control over installed packages.
Downsides
: Tedious, error-prone, and lacks version management.
2. distutils (1998)
External Tooling
: None
Dependency File
: None
Benefits
: Standardized way of building and installing Python packages.
Downsides
: No built-in way to manage package dependencies.
3. setuptools and Egg Format (2004)
External Tooling
: easy_install
Dependency File
: setup.py
Benefits
: Extended distutils, simplified package installation, and allowed specifying dependencies. It introduced the egg format for binary package distribution.
Downsides
: No automatic dependency resolution; easy_install is now considered outdated.
4. virtualenv (2007)
External Tooling
: virtualenv
Dependency File
: requirements.txt
Benefits
: Environment isolation, solved dependency hell for individual projects by allowing developers to install packages without affecting the global Python installation. It allowed each project to have its dependencies, avoiding conflicts. It creates a self-contained directory containing a Python interpreter and a copy of the
pip
library, enabling packaging management within that isolated environment.
Downsides
: Added cognitive overhead. Required activation/deactivation, extra disk space, and didn't handle transitive dependencies well. Developers need to remember and think about which virtual environment is active in a given shell.
5. pip (2008)
External Tooling
: pip
Dependency File
: requirements.txt
Benefits
: Replaced easy_install, offered better dependency resolution, and became the de facto package installer.
Downsides
: No environment isolation by default.
6. conda (2012)
External Tooling
: conda
Dependency File
: environment.yml
Benefits
: Not just Python-specific, offered both package management and environment isolation.
Downsides
: Heavier tool, a separate ecosystem from PyPI.
7. Wheel Format (2012)
External Tooling
: pip
Dependency File
: setup.py
Benefits
: Faster and more efficient binary package distribution than egg.
Downsides
: Required changes in how packages were created and distributed.
8. pipenv (2017)
External Tooling
: pipenv
Dependency File
: Pipfile and Pipfile.lock
Benefits
: Combined pip and virtualenv, simplified dependency management with lock files.
Downsides
: Slower dependency resolution, another tool to learn and manage.
9. Poetry (2018)
External Tooling
: poetry
Dependency File
: pyproject.toml
Benefits
: Simplified dependency management and packaging, embraced PEP 517/518 standards.
Downsides
: Yet another tool, initial learning curve, and not fully compatible with setuptools.
10. PEP 517/518 (2018)
External Tooling
: Build backends like flit and poetry
Dependency File
: pyproject.toml
Benefits
Downsides
: Early adoption issues; complicates migration for older projects.
Why we chose Poetry for the Pinecone Python client
No perfect tool can solve everyone’s problems and cover all use cases neatly in a backward-compatible way. Humans write imperfect software and tooling, and we’ll likely continue doing so, at least for the foreseeable future.
Ultimately, engineering comes down to tradeoffs and choosing the best fit amongst those tradeoffs. We settled on Poetry to manage the Pinecone Python client, which you can use to create, upsert into, and query Pinecone vector database indexes, because we felt it provided the most benefits to our internal maintainers, customers, and community contributors.
Poetry will manage the Pinecone Python client soon once
this pull request
is merged. If you’re wondering how to migrate your existing Python project to use Poetry, you can see how we did it by reviewing that pull request.
Here’s why we chose Poetry:
Simplified local development.
Take a look through
our new Contribution guide
to see how you can use Poetry to create a virtualenv that allows you to A.) make changes to the Pinecone python client and see those changes immediately reflected in scripts where you
import pinecone
and B.) track those changes in git so you can open a pull request to contribute them back. Poetry supports dependency resolution and virtualenv management via a single interface, simplifying project setup for new contributors.
Plays nicer with common dependencies such as LangChain.
pinecone-client
and
langchain
are commonly
pip install
ed into Jupyter Notebooks, such as our
example notebooks demonstrating the latest AI patterns
. In some cases, such as improving bottlenecks or adding features, maintainers must be able to modify both
langchain
and the
pinecone-client
that it wraps simultaneously and track their changes in git. Again, Poetry simplifies this workflow.
Mostly backward compatible.
If you’re not a maintainer or open-source contributor but a user of the Pinecone Python client, you should not notice much difference at all. You still have the option of pinning to Pinecone python client versions earlier than the Poetry cutover, but the user-facing experience and interfaces to the library have not changed.
From pain to poetry and beyond
Python is the predominant language for AI use cases, but as we’ve written here, we believe
most folks underestimate JavaScript for AI application development
.
Meanwhile, developers eagerly anticipate project
Mojo
, which will likely significantly improve the Python developer experience again.
Python has come a long way and continues receiving outstanding contributions and enhancements. We’re excited to continue shipping Python tooling and libraries as the developer experience improves.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
