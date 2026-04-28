---
title: "Symbiosisware"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/symbiosisware/"
fetched_at: 2026-04-28T07:01:33.609397+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Symbiosisware

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/symbiosisware/

Symbiosisware
[Simon Tatham, 2024-08-06]
“Symbiosisware” is a word I made up, some time in the early
      2000s, to describe a particular class of software I sometimes
      write for my own use.
I’ve been using the word to myself, and in conversation with
      friends, for decades. It’s time I wrote down an explanation of
      what it means, so I can point other people to a definition.
What is symbiosisware?
Simply put: symbiosisware is software designed to
      have
only one user
, and that user is yourself
      –
the one user is also the developer
. It’s
      software you write
solely
in order to use it yourself –
      and various design choices follow from that.
Some software is never symbiosisware: you write it from day one
      expecting that eventually you’ll release it, even if it’s not
      released just yet. Other software stays symbiosisware forever: a
      typical example is your
.bashrc
, or
      your
.emacs
, or things like that.
Occasionally a piece of former symbiosisware turns into a
      published program, but it takes a lot of work, for reasons I’ll
      go into below.
Ways that symbiosisware differs from released software
Symbiosisware is often less polished than published software,
      in several slightly different ways, which I’ll list below.
It’s tempting to look at the following sections and conclude
      that “symbiosisware” is just another name for “lazy hacky bodge
      job”, and to judge a programmer harshly for producing it. But I
      don’t think so. I think the lack of polish in symbiosisware
      is
sensible
– a rational choice about where your own
      effort is best spent. That’s
why
I made up a word for
      it that doesn’t sound negative or critical.
It would be a lazy hacky bodge job to write software with all
      of these flaws
intended for release
. But if you never
      intended to release it at all, I think that’s completely
      different.
(But then sometimes it turns out you have to release it anyway,
      and then you have some hard work to do and some painful
      compromises to make; see below…)
Symbiosisware has more minor bugs
When you’re deciding whether to bother fixing a bug, one way to
      consider the question is: what saves effort overall? Fixing the
      bug, which costs the programmer a load of coding, testing etc?
      Or not bothering, and letting users just put up with the bug,
      costing
them
frustration, and effort working around
      it?
If you have a
lot
of users, that skews the decision
      more often in favour of fixing the bug. Even a small
      inconvenience to 100 users might add up to more effort than one
      programmer’s time doing a fix. For 100,000 users, maybe an even
      smaller inconvenience is worth fixing. And so on.
But if there’s only
one
user, it’s very easy to find
      that it’s more effort to fix the bug than to just live with it.
One way in which this kind of decision goes wrong is that the
      costs are externalised. The programmer
mostly
considers
      their own effort in fixing the bug, and finds it easy to ignore
      the user inconvenience because all those users are out of their
      sight. This makes users angry, if they think the programmer has
      over-prioritised their own laziness and under-prioritised the
      users’ convenience.
But if the only user
is
the programmer, that’s the one
      situation in which you know every single user will be forgiving
      of the programmer’s laziness!
So symbiosisware has more bugs, because the effort equation is
      less in favour of fixing them.
However, this generally only applies to
minor
bugs:
      things like bad error reporting (e.g. a complicated Python
      traceback in place of a more easily comprehensible error
      message), or things that only occur in a weird edge case that
      hardly ever comes up. Bugs that involve the actual output being
      wrong in a realistically likely case, or any kind of data loss,
      or things like that, are a different matter.
Symbiosisware has limited generality
A side effect of writing software for your own use is that you
      know what environment it will run in, and you can code to that
      environment, and not worry about other environments.
This phenomenon comes in all flavours. You might write a
      program that only runs on your favourite OS, or your favourite
      desktop environment, and not bother to port it to anything more
      popular. You might write a program that expects a particular
      kind of input device, like a pointing device with 4 buttons, or
      a keyboard in a specific layout, because
you
know you
      always use that setup, and nobody else is going to be using the
      program. You probably won’t bother with internationalisation –
      the program is already giving all its messages in a
      language
you
understand. You might leave out error
      checks for types of error that you think you personally aren’t
      likely to make. And so on.
Sometimes you end up with a really weird mixture of portability
      and restrictions. For example, I use both Linux and Windows, and
      once, I decided I wanted to have a collection of convenient hot
      keys for common actions that work the same way in both
      environments. But on Linux I always run the same X11 window
      manager with a convenient interface for sending it commands
      (namely Sawfish). So I wrote a piece of symbiosisware that
      implements cross-platform hot key configuration, which knows how
      to get the same set of things done on Windows, and on Linux in
      an X session running Sawfish. But it doesn’t have any idea how
      to do those things in any
other
Linux-based GUI
      environment, because I haven’t done the research to find out a
      more general way of doing those things on Linux. That’s enough
      for me!
Polished release-quality software often puts some thought into
      having a simple and consistent “metaphor” for its user
      interface.
The idea is that the end user doesn’t have to understand the
      low-level details of what the program is really doing. They only
      have to understand the metaphor, which is designed to be
      simpler. Reasoning about the simple metaphor should be enough to
      predict reliably what things the software can and can’t do, and
      for each thing it can do, where to find the UI action that does
      it.
Sometimes this costs considerable
extra
programming
      effort, in arranging that things work in a consistent way (from
      the user perspective) even when that’s harder work from the
      programmer perspective.
For a user who doesn’t already understand the program, a UI
      metaphor saves effort. They can learn the simple metaphor,
      instead of the much more complicated details of the actual
      program. The more users there are, the more this effort saving
      is compounded, and it quickly outweighs the extra programming
      effort to make the metaphor work.
Conversely, the
fewer
users there are,
      the
less
effort is saved by having a nice UI metaphor.
      But even more: if the only user is the developer, then
      they
do
already understand the program. If I want to
      predict what my program does, and I already know in detail
      exactly how it works, why do I even
need
a separate
      metaphor? I can use my existing understanding. So designing and
      using a carefully constructed UI metaphor adds
extra
effort!
Symbiosisware adapts the user and the program
      equally to each other
I’ve described several differences between symbiosisware and
      released software. In some sense, you can look at all of them as
      different instances of the same underlying phenomenon.
When a piece of software and its users don’t work well
      together, you have to choose whether to change the behaviour of
      the software, or whether to try to change the behaviour of the
      users. (For example, by documenting the software’s behaviour
      better, or providing tutorials on how best to get things done
      with it.)
When there are a lot of users and they don’t want to change,
      you generally end up deciding in favour of changing the
      software. But the unusual feature of symbiosisware is that
      changing the software and changing the user are
about as
      easy as each other
– so you end up doing each one about
      half the time.
That’s why I gave the concept this name in the first place. In
      biology,
symbiosis
refers to a pair of organisms that
      have adapted to each other, for mutual benefit, at the cost of
      it being hard to separate them. Here, the organisms are the
      program and its single user.
I have quite a few pieces of symbiosisware I’ve been using for
      decades. Their user interfaces are weird, and full of quirks
      that would be confusing, inconsistent, and surprising to anyone
      else – but they’re what I’m used to, and it would confuse me to
      change to something more consistent and sensible. Half of that
      is because I’ve adapted the software to what
I
      personally
find natural, or intuitive, or easy to remember,
      without regard for what anyone else would prefer. The other half
      is that I’ve adapted
myself
to anything in the software
      that was too hard to change, by adjusting my own expectations
      and re-training my reflexes.
So, just like biological symbiosis,
neither
one of us
      would be as effective without the other! If I do decide I need
      to turn a piece of symbiosisware into a released piece of
      software for other people to use, then I have to do two lots of
      work. One is redesigning the software so that it has fewer bugs,
      more generality, and a more consistent UI: the software must
      adapt to survive in an environment where it can’t depend on
      having me around. But the other is re-training
myself
to use the released version, which will usually end up very
      different from the original. I must adapt to survive in an
      environment where I can’t depend on having (the original version
      of) that software around!
