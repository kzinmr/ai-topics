---
title: "Regular Expression Commands"
url: "https://blog.llvm.org/2011/04/regular-expression-commands.html"
fetched_at: 2026-05-05T07:01:43.880884+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Regular Expression Commands

Source: https://blog.llvm.org/2011/04/regular-expression-commands.html

Regular Expression Commands
By Greg Clayton
Apr 22, 2011
#LLDB
4 minute read
Greetings LLDB users. I want to start writing regular blog posts for the new and cool features and things you can do in LLDB. Today I will start with one that was just added: regular expression commands.
What is a regular expression command? It is a smart alias to other commands that you can define using the "
command regex"
command. You define a regular expression command by giving it a command name followed by a series of regular expression and substitution pairs. The regular expression and substitution pairs are supplied in a standard stream editor search and replace format:
s/<regex>/<subst>/
When a command in later entered, it will strip off the regular expression command name and any spaces that follow, it and pass the raw argument string to be matched against your regular expression list in the order in which they were entered. The first
<regex
>
to match the raw argument string will then be allowed substitute in
the command defined by
<subst>
.
Lets supposed we want to use the
"f"
as a command to select a frame by frame index. The command to select a frame by the frame index is the
"frame select <num>
"
command which you might not always want to type out. We can make this a bit easier this using a regular expression command:
(lldb) command regex f 's/([0-9]+)/frame select %1/'
"command regex f"
tells the interpreter to create a new regex command named
"f"
, and when a command is entered on the command line that starts with
"f"
, it will match the remaining command text against the regular expression
"([0-9]+)"
, and it if matches, it will substitute any parenthesized subexpressions. Here we enclosed the number regular expression
"[0-9]+"
in parentheses which will save the results in the first match and allow the matching string to be substituted into the match substitution text
"frame select %1"
. When we use our new regular expression command from the LLDB command line, it will show us what command resulted from our regular expression substitution:
(lldb) f 12
frame select 12
Any leading spaces that follow the regular expression command
"f"
will always be stripped prior to matching the regular expression, but there may be trailing spaces since we are processing the remaining raw command string that follows the initial
"f"
command name. The regular expression is also just looking for any sequence of one or more digits. Our current regular expression will actually match:
(lldb) f 11 22 33
frame select 11
Since this isn't desired, we should make the regular expression more complete by checking for the start of the line (
^
) and the end of the line (
$
) and also allow for zero or more spaces (
[[:space:]]*
) to come after the number. Our newer and safer regular expression command line looks like:
(lldb) command regex f 's/^([0-9]+)[[:space:]]*$/frame select %1/'
Now we can type in a command as
"f 12 "
(note the trailing spaces), and still get correct substitutions, while our previous example of
"f 11 22 33"
will no longer match:
(lldb) f 11 22 33
error: Command contents '11 22 33' failed to match any regular expression in the 'f' regex command.
Lets take this a bit further by also using the
f
command to emulate GDB's
finish
command when it is typed without any arguments. We will also modify this command to watch for a single "+" or "-" followed by a digit to signify a relative frame change using the frame select command with the --relative option:
(lldb) frame select --relative
Multiple regular expressions can be entered in on the command line, or using the multi-line mode when typing in a live LLDB debug session. Below the text in bold is user entered:
(lldb)
commands regex f
Enter regular expressions in the form 's/
/
/' and terminate with an empty line:
s/^([0-9]+)[[:space:]]*$/frame select %1/
s/^([+-][0-9]+)[[:space:]]*$/frame select --relative=%1/
s/^[[:space:]]*$/finish/
(lldb)
f
finish
...
(lldb)
f -1
frame select --relative=-1
...
(lldb)
f +1
frame select --relative=+1
...
(lldb)
f 12
frame select 12
I hope you can see the possilbities in how you can customize your command line experience in LLDB using these commands. You can add any regular expression commands to your
~/.lldbinit
file to always have your regular expression commands defined in your debug sessions.
