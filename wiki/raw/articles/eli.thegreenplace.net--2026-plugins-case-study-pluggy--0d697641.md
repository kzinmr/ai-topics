---
title: "Plugins case study: Pluggy"
url: "https://eli.thegreenplace.net/2026/plugins-case-study-pluggy/"
fetched_at: 2026-06-14T07:00:54.731046+00:00
source: "eli.thegreenplace.net"
tags: [blog, raw]
---

# Plugins case study: Pluggy

Source: https://eli.thegreenplace.net/2026/plugins-case-study-pluggy/

Recently I came upon
Pluggy
,
a Python library for developing plugin systems. It was originally developed
as part of the
pytest
project - known for its rich plugin ecosystem - and
later extracted into a standalone library. You're supposed to reach out for
Pluggy if you want to add a plugin system to your tool or library and want
to use something proven rather than rolling your own.
In this post I will share some notes on how Pluggy works, and will
then review how it aligns with the
fundamental concepts of plugin infrastructures
.
Using Pluggy
Pluggy is built around the concept of
hooks
: functions that host
applications or tools (from here on, just "hosts") expose and plugins implement.
A host exposes hooks by using
a decorator returned from
pluggy.HookspecMarker
and a plugin implements this
hook using a decorator returned from
pluggy.HookimplMarker
.
Pluggy's
documentation
explains
this fairly well; in this post, I'll show how to implement the
htmlize
tool
with some plugins, introduced in
the original article in my plugin series
.
As a reminder,
htmlize
is a toy tool that takes markup notation similar to
reStructuredText, and converts it to to HTML. It supports plugins to handle
custom "roles" like:
some text :role:`customized text` and more text
As well as plugins that do arbitrary processing on the entire text.
Defining hooks
Out host
defines two hooks:
import
pluggy
hookspec
=
pluggy
.
HookspecMarker
(
"htmlize"
)
@hookspec
(
firstresult
=
True
)
def
htmlize_role_handler
(
role_name
):
"""Return a function accepting role contents.
The function will be called with a single argument - the role contents, and
should return what the role gets replaced with.
"""
pass
@hookspec
def
htmlize_contents
(
post
,
db
):
"""Return a function accepting full document contents.
The function will be called with a single argument - the document contents
(after paragraph splitting and role processing), and should return the
transformed contents.
"""
pass
A hook is created by calling
HookspecMarker
with the project's name. This
project name has to match between the host and its plugins. Pluggy is permissive
about what hooks accept as parameters and what they return; for maximal
flexibility and to stay true to the original
htmlize
example, our hooks
return functions.
To accompany this
HookspecMarker
, the host also defines a
HookimplMarker
with
the same name:
hookimpl
=
pluggy
.
HookimplMarker
(
"htmlize"
)
This is used by plugins to attach to hooks when they're loaded.
Loading plugins in the host
The host's main function loads plugins at startup as follows:
pm
=
pluggy
.
PluginManager
(
"htmlize"
)
pm
.
add_hookspecs
(
hookspecs
)
pm
.
load_setuptools_entrypoints
(
"htmlize"
)
hookspecs
is our Python module containing the hooks shown above.
load_setuptools_entrypoints
is Pluggy's helper for loading plugins that
were
pip
-installed into the same environment and registered as
setuptools
entry points
.
It's a way to signal - in one's
setup.py
or
pyproject.toml
file - some
metadata that projects can review at runtime. In our project, the plugins
register themselves with this section in the
pyproject.toml
file:
[project.entry-points.htmlize]
tt = "tt"
This says "for entry point
htmlize
, define a new entry named
tt
".
Pluggy's
load_setuptools_entrypoints
then uses
importlib.metadata
to access this information.
Note that Pluggy doesn't require using this mechanism. Hosts can implement any
plugin discovery method they want, and add plugins directly to their
PluginManager
with the
register
method. But this is the mechanism used
for
pytest
and many other projects; it makes it very easy to
automatically discover and register plugins that are installed with
pip
and
equivalent tools.
Invoking plugins
Once
PluginManager
loads the plugins, invoking them is straightforward;
here's how
htmlize
invokes the contents hooks :
# Build full contents back again, and ask plugins to act on
# contents.
contents
=
''
.
join
(
parts
)
for
handler
in
plugin_manager
.
hook
.
htmlize_contents
(
post
=
post
,
db
=
db
):
contents
=
handler
(
contents
)
return
contents
Generally, hook invocations return a
list
of all the hooks attached to by
different plugins (a single host application can have multiple plugins installed
and attaching to the same hook). When the host invokes the hook as shown above,
the default order is LIFO, but plugins can affect this with
hook options
like
tryfirst
and
trylast
.
Implementing hooks in plugins
Here's our entire
narcissist
plugin that's attaching to the contents hook:
import
htmlize
@htmlize
.
hookimpl
def
htmlize_contents
(
post
,
db
):
repl
=
f
'<b>I (
{
post
.
author
}
)</b>'
def
hook
(
contents
):
return
re
.
sub
(
r
'\bI\b'
,
repl
,
contents
)
return
hook
Some notes:
It expects
htmlize
to be installed; as discussed previously, we rely on
Pluggy's default install-based approach where both the host and plugins are
installed into the same Python environment and can thus find each other.
However, Pluggy supports any custom discovery method.
It uses the
hookimpl
exported value shown earlier.
It returns a function that acts on contents; this is the
htmlize
-specific
contract (ABI, if you will) we've discussed before.
Fundamental plugin concepts in this case study
Let's see how this case study of Pluggy measures against the
Fundamental plugin concepts
that were covered
several times on this blog
.
It's important to remember that Pluggy is not a specific host application with
a bespoke plugin system; rather, it's a reusable library for creating such
plugin systems. Therefore, this is more of a
meta
case study.
Discovery
Generally, Pluggy leaves discovery logic to the user's discretion. Its
PluginManager
has a
register
method for adding plugins, and these can
be discovered in any way the application chooses.
That said, Pluggy comes with one discovery mechanism built in - through the
entry points process of Python packaging, as shown above. This is hugely
convenient for a large number of applications, as long as both the application
and its plugins are installed via standard Python packaging tools (which is
a very reasonable assumption in the Python ecosystem).
Registration
In the entry point process, plugins register themselves by adding a
[project.entry-points.<HOST-ID>]
section in their
pyproject.toml
file.
Otherwise - as in the previous section - users are free to devise their own
registration schemes.
Hooks
This one is easy, since it's called
hooks
in Pluggy parlance as well!
Pluggy's implementation of hooks is rather elegant, with function decorators
available for plugins to set. We've seen an example of this above with
@htmlize.hookimpl
decorating
htmlize_contents
.
Exposing an application API to plugins
Since Pluggy is designed for Python hosts and Python plugins, this one is
fairly straightforward. The plugins typically assume the host project is
already installed in the Python environment and its modules can be imported.
In our example,
hookimpl
is imported from
htmlize
by the plugin to
accomplish this. It also shows how host data is passed to the plugin - the
post
and
db
parameters. These are APIs exposed by the host for the
plugins' use.
Conclusion - is Pluggy worth it?
In footnote 2 of my original
fundamental concepts of plugin infrastructures
post, I wrote :
This is probably why there are very few well-established plugin frameworks
in existence (even in low-level languages like C or C++). It's too easy (and
tempting) to roll your own.
I still believe my statement is true - plugin frameworks are very easy
to create, and the functionality they provide is relatively small compared to
their large surface area. In other words, this is a
shallow API
.
That said, Pluggy does provide some nice functionality for the more advanced
uses of plugins:
Automatic entry point registration mechanism - if you need it
Signature validation
Consistent plugin result collection across multiple hook attachments in a
single plugin and across many plugins
Plugin ordering with
firstresult
,
tryfirst
,
trylast
, etc.
Hook "wrappers" for some special use cases
Are these worthwhile for your project? It really depends on the project,
and it's always worth keeping the
tradeoff between dependencies and project
effort
in mind.
