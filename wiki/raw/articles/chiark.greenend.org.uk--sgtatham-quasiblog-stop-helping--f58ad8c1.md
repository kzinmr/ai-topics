---
title: "Stop helping!"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/stop-helping/"
fetched_at: 2026-04-28T07:01:34.373992+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Stop helping!

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/stop-helping/

Stop helping!
Command-line tools: don’t print long help text with an error message
[Simon Tatham, 2023-09-02]
Command-line utilities typically have an option to explicitly
      request online help text. Canonically this option is
      spelled
--help
, though a few tools prefer
      alternatives like
-h
or
-?
.
$ do-the-thing --help
usage: do-the-thing [options] <this> [<that>]

arguments:

  this              a file to do the thing with
  that              a file to be used in a different way. If omitted,
                      default behaviour is to manage without it somehow.

options:

  -v, --verbose     witter at length about doing the thing
  -s, --silent      do the thing, but shut up about it
  -r, --reverse     do the thing backwards, for a laugh
  --help            display this text
$
Usually there’s some way to get the command-line syntax wrong.
      When that happens, the tool should
at least
print an
      error message telling you what part of the command line was
      incorrect:
$ do-the-thing --quiet -r this that
do-the-thing: unknown option '--quiet'
$
Sometimes, that’s all you need, because your typo was obvious,
      or because you already knew you couldn’t quite remember whether
      (as in this example) it was
--silent
or
--quiet
. But sometimes – especially if you’ve
      rarely or never used this tool before – you’re confused enough
      to want to consult the help to understand your mistake.
To help out those users, some tools will also
      suggest
how
the user can find out more about the
      mistake they made, by reminding them of what the help option
      is:
$ do-the-thing --quiet -r this that
do-the-thing: unknown option '--quiet'
Try 'do-the-thing --help' for more information.
$
Other tools don’t even make the user
type
that extra
      command. Instead, after printing the error message, they’ll
      display the entire help text straight away, on the theory
      that the user might find it useful:
$ do-the-thing --quiet -r this that
do-the-thing: unknown option '--quiet'
usage: do-the-thing [options] <this> [<that>]

arguments:

  this              a file to do the thing with
  that              a file to be used in a different way. If omitted,
                      default behaviour is to manage without it somehow.

options:

  -v, --verbose     witter at length about doing the thing
  -s, --silent      do the thing, but shut up about it
  -r, --reverse     do the thing backwards, for a laugh
  --help            display this text
$
Which of those design choices is best?
My opinion:
don’t
print the whole help text because
      of an error. It’s counterproductive!
Why not?
1. It’s visually overwhelming
In that last display above, the error message is
tiny
,
      and the help text is enormous. The user might very well not
      even
notice
the error message.
A lot of the text appearing in terminal sessions is useless to
      the user. Users work out very quickly that they don’t really
      need to read it all. So they pattern-match the overall shapes of
      things to pick out the parts they
do
need to read.
At first glance, this display with an error message plus help
      text looks
almost exactly the same
as the display
      with
just
the help text. It is entirely possible to
      miss the error completely, simply because it was lost in the
      noise.
If a user has enough of the right instincts for debugging and
      some experience of other command-line tools, they’ll be able to
      zero in on the error message by thinking: “Hold on, I didn’t ask
      ‘
do-the-thing
’ to show me its help text. Why did it
      show it anyway? Perhaps just before the help text there might be
      a message telling me why it was about to print it.” That thought
      process will draw their eye to the top of the help message, and
      then they’ll find the one-line error just above it – but only if
      they
have
that thought process.
But who’s most likely to make errors in your tool’s command
      line? Less experienced users, who are less likely to have those
      instincts and that experience already.
And if you do miss it, what will you do? Again,
the right
      instincts and experience
might lead you to hunt around
      harder for the cause of the confusion. But without those, you
      might well scratch your head for a moment, shrug it off with
      ‘computers are incomprehensible, who knows’ – an extremely
      plausible answer in the modern day – and give up on getting your
      thing done.
2. It can scroll the error message off the top of the window
Maybe you (the command-line tool developer) use a nice large
      terminal window. But not everybody does. Some users have smaller
      screens; other users do have a big screen but prefer to divide
      it into lots of small windows instead of covering it with one
      big one.
If your help text is longer than the user’s window,
      then
the only thing
they’ll see after a mistake is the
      bottom half of the help text. They’ll have to scroll back up in
      their terminal to see the error message,
even if they guess
      that there might be one
. But the error message was the part
      they needed most!
3. It’s patronising
If I actually, genuinely, don’t know anything yet about how to
      use your program, then
maybe
I’ll appreciate it being
      proactively explained to me.
But if I already knew most of it, and I’d just forgotten that
      one option, I’m not particularly going to appreciate you
      explaining all the other options to me just in case I needed to
      know them. This is also true if most of the options in the help
      aren’t needed for the thing I’m trying to do right now.
And if I hadn’t forgotten
anything
, and had just made
      a typo (say, ‘
--sikent
’ in place of
      ‘
--silent
’), then there’s absolutely no point in
      you
explaining
anything to me at all. I already know
      it. It’s insulting for you to judge that I don’t, and it’s
      inconvenient in practical terms for you to use up my screen
      space with it. All you need to do is to draw my attention to
      which option in my command was a problem, and I can do the rest
      without needing any more help. Or any
      more
--help
.
Conclusion
It’s reasonable to tell the user how the help option is
      spelled. Even if every program in the world spelled it the same
      way, every user would still run into this problem for the first
      time
once
. And in fact, programs disagree: it’s
      not
always
‘
--help
’. So there’s nothing
      wrong with letting them know what the help option is.
But wait for them to
ask for it
before volunteering
      the entire screenful of text. Trying harder to help is less
      helpful!
