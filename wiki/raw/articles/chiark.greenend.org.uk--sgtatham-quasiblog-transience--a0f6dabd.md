---
title: "Policy of transience"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/transience/"
fetched_at: 2026-04-27T07:56:53.589300+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Policy of transience

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/transience/

Policy of transience
[Simon Tatham, 2025-05-09]
Introduction
I have several habits in my computer usage which are unusual by
      many people’s standards (although some more so than others), and
      which all kind of point in the same direction.
At the time I adopted each one, I didn’t recognise this. Each
      habit seemed desirable in its own context for one reason or
      another, but it wasn’t a lot later until I spotted the common
      theme running through them all. The theme wasn’t always the
      reason I adopted the habit in the first place – but I think it’s
      the reason I’ve
kept
all these habits, after trying
      them out for some other reason.
In this article I’ll describe the habits I’m thinking of, and
      the more general idea that they’re all instances of, which I now
      think of as a “policy of transience”.
I’m not trying to persuade anyone else that they should adopt
      this general policy, or even any of the specific habits. I just
      put the ideas out here in case they’re of interest, for people
      to consider, and decide
whether
they’d find any or all
      of it useful. If any of this is useful to you, great – and if
      you decide it’s not for you, that’s fine too.
The habits
Here’s a list of the habits that I now classify under the
      general heading of “policy of transience”. I
think
these are in roughly chronological order of me adopting them,
      though it’s hard to be sure.
Turn off persistent shell history
I use the Linux command line, specifically
bash
.
      Like many other modern Unix shells,
bash
keeps a
      history of the commands you’ve typed, so that you can recall
      them and run them again, or modify a previous one slightly to do
      a new thing.
This can be used in the immediate short term: type a command,
      it doesn’t quite work, recall it and edit one typo, try again.
      But it can also be useful over the long term: recall a command
      you ran last week, or last year, or that thing you do about once
      a month. To support the long-term uses of this
      feature,
bash
saves your shell history to a file
      when you exit the shell (by
      default
~/.bash_history
), and reloads that file
      when it starts up. So you can still recall a command even if
      you’ve logged out or rebooted the whole machine since running
      it.
Many people find this persistent history feature very useful,
      and go to some lengths to improve it further – you can configure
      a larger number of stored commands, some shells will sync their
      history constantly instead of just on exit, there are plugins to
      help you search it more easily, and so on. The general view
      seems to be: shell history is good, more and easier-to-use
      history is even better.
But I go the opposite way. My unusual habit is:
turn
      off the history file completely
, by putting the command
      ‘
unset HISTFILE
’ in my
.bashrc
. I
      still get history within a single instance of the shell, so I
      can edit my last command ten times until it works properly; but
      history isn’t shared between my terminal windows, or preserved
      when I log out and log in again.
All
the shell history
      I allow myself is localised and short-term.
I started doing this very early in my Linux-using career, very
      soon after I found out the history file existed in the first
      place. I think my initial motivation was an extremely vague
      privacy concern: it just felt
creepy
that my shell
      would be remembering that much detail about stuff I’d done in
      the past.
There are certainly valid
specific
privacy concerns
      about shell history. Sometimes you write an actual secret, such
      as a password, on a command line by mistake. (Oops, had focus in
      the wrong window.) And sometimes you just have to hold your nose
      and put a secret on a command line on purpose, because some
      badly designed tool won’t let you pass it in any other way.
      (That’s already a danger, of course, because other users of the
      system can see it in
ps
– but it’s one thing to
      take that risk very briefly while the command is actually
      running, and quite another to have a copy of the secret
      preserved in
~/.bash_history
for months or years.)
      But I don’t think I had anything that specific in mind to begin
      with: I just felt generically uneasy with the idea.
(Of course, if you
know
you’ve just written a secret
      on a command line, you can delete the command from that shell’s
      history on purpose, before it gets saved to the file. But if you
      did it by accident, you might not realise you need to; and if
      you had to recall the command and retry it a few times, you
      might not manage to clean up every instance of it.)
But after I adopted this policy, and put ‘
unset
      HISTFILE
’ in the standard snippet of
.bashrc
that I share between all my Unix accounts, I found it had
      another benefit: it forces me to keep things more organised.
If I type a shell command that’s
valuable
– one that
      did something useful enough that I might want it again in
      future, and long and complicated enough that I’d be annoyed to
      have to figure it out a second time from scratch – then I can’t
      rely on it just happening to be in
      my
.bash_history
. So instead I put it somewhere
      else: maybe a shell function in my
.bashrc
, or
      maybe a shell script in my directory of random useful
      scriptlets. Or maybe just in a file of notes jotted down to
      myself about useful shell runes to remember.
I find this a more useful way to remember shell commands.
      Firstly, this procedure separates the
working
version
      of the command from all the failed attempts just before it. Even
      within the context of one instance of
bash
I’ll
      sometimes accidentally recall a
wrong
version of a
      command when I was aiming for the corrected one two commands
      later; the idea of having a
year’s worth
of my own
      false starts available for accidental recall seems horrifying!
      Instead, I deliberately save
just
the working version,
      and let all the failed attempts go in the trash when I close the
      shell.
Secondly, when I save a command on purpose in any of these
      ways, I give it a name, and write a comment explaining what it
      was useful for, and what I might find it useful for again. And
      most likely I commit it to one of my small personal Git
      repositories, so that it stays around, is shared between my
      machines, and I can keep it up to date later if it doesn’t quite
      work in some new context.
Of course, this means it’s more effort at the moment
      I
do
save the command for later. But my impression is
      that the effort pays off in the long run.
Clear my GUI desktop regularly
I mostly don’t stay logged in to a single GUI session for
      months on end.
(This is probably one of the
less
unusual things on
      the list, but this is where it appears in the chronological
      order of me adopting the habits.)
I turn laptops completely off more often than I suspend them. I
      see suspending as a tool for very temporary pauses in what I’m
      doing: if I was using my laptop on a train and now I have to get
      up and change to another train, that seems like a good use for a
      20-minute suspend. But when I reach my final destination, I’ll
      shut the laptop down completely. I never leave a laptop
      suspended overnight (except by mistake).
Machines that also function as remote login servers, or build
      machines, or both, have to stay on. But even there, I don’t like
      to leave a single login session live for a long time. In years
      when I have an office desktop machine (though right at the
      moment I’m using a laptop), I’ll log in at the start of the day
      and log out before going home, rather than just locking my
      screen and leaving all my windows there until the next
      morning.
Even if I don’t actually log out of a machine on a daily basis,
      I’ll
apt upgrade
it on a daily basis, and
      reboot
promptly
if
apt
tells me I need to,
      like because it’s installed a kernel update – I’m not one of
      those people who leaves a reboot pending for months because of
      all the stuff in my open windows that I don’t want to lose. So
      nothing I run will normally have an uptime of more than a couple
      of weeks. And more often than
that
, even if I don’t
      actually log out, I’ll close all my open applications, clear the
      desktop, and start again from scratch.
Of course, this adds a bit of effort to my morning routine when
      I power up a machine, log in, and start doing something with it.
      I minimise that by having a streamlined workflow for opening the
      usual applications I use – a mixture of keyboard shortcuts (I
      don’t have to click through the GUI start menu for any of my
      usual tools) and smart window-manager configuration (my WM
      places the windows automatically in the locations I prefer).
Why did I start behaving like this? I think it’s more that I
      never
stopped
behaving like it. When I was a child, the
      computers in the house were shared with other family members, so
      you couldn’t leave your session running for ages, because
      someone else wanted to use the machine. ‘Suspend’ and ‘Switch
      User’ weren’t a thing on that generation of computers. And there
      wasn’t usually any point leaving a machine on all the time,
      because it wasn’t connected to the network, so it wouldn’t be
      doing anything useful.
But I do have some more specific reasons not to want to leave a
      session, or even a particular pile of terminal windows, running
      forever.
One reason is that it’s a defence against accumulated state
      changes. In a particular terminal, I might have messed about
      with environment variables like
PATH
, and then that
      terminal isn’t in its default state any more. Probably I did
      that because it was sensible for a particular thing I was using
      that terminal window for. But if I forget I’ve done it, and
      reuse the same window for something else, then the leftover
      state could confuse me. In the
good
case, something I
      wanted to do doesn’t work. In the bad case, something I
      try
does
work, which wouldn’t work in the terminal’s
      default state, and then I put it in a script (or worse, send it
      to somebody else) and it unexpectedly fails later when it runs
      in an unmodified environment! For this kind of reason, I’ll
      often avoid using the same terminal window for two unrelated
      projects: it’s a habit to ^D the window and open a fresh one in
      the same screen location if I’m going to stop working on (say)
      PuTTY and start working on (as it might be) my puzzle games.
But another reason is: I find closing all my applications
      regularly imposes a useful discipline on me. If I’m still half
      way through some coding when I shut my laptop down (for example
      because the train has arrived), then
because
I’m about
      to shut it down, I’ll make sure to leave it all in a good state:
      make local git commits from my work, write some notes to myself
      about what I still have to do, and generally make sure that when
      I next boot the laptop up and try to resume what I was doing, I
      can remember what it was and where I’d got to. This clarifies my
      thoughts in any case, and allows me to come back with a fresh
      mind next time, re-read my notes, and maybe have new ideas.
It also helps transferrability between machines. After I make
      those git commits of my half-finished work, I’ll often push them
      to another machine (at least if I have networking at the time).
      Partly that’s a defence against data loss. But also, if the next
      time I work on the same thing is on another machine like my home
      desktop, I can pick up
there
where I left off on the
      laptop. If all my working state was contained in the laptop’s
      GUI session, I’d
have
to keep working on the laptop,
      even if I’d got back home where I have a bigger display.
Close my entire web browser frequently
In the previous section I mentioned that I close
all
my GUI applications frequently, including the web browser. But
      it goes further than that: I close the web browser
      much
more
often than I close the terminal and editor
      windows alongside it.
A lot of the time, if I’m working on something like coding, I
      don’t have a browser open at all. If I need to refer to
      web-based documentation, as often as not I’ll have to start
      Firefox up from scratch in order to do it. I might open a
      handful of tabs as I follow hyperlinks, but when I’m done, I’ll
      make the effort to close those tabs, and ideally, close the
      whole browser.
One thing I
don’t
do is to use the open browser’s list
      of tabs as a long-term to-read list. (Not even “to read over the
      course of today”, much less over weeks.) I know that’s a common
      way that many people use browsers, to the extent of needing
      browser plugins or extensions to help manage hundreds or
      thousands of tabs. If I ever have 100 tabs open in a browser,
      it’s because I opened them all in rapid succession for some
      immediate purpose (either with a script, or by clicking every
      hyperlink on a large index) and I’m about to go through them all
      right now looking for whatever I was after, and then close them
      again as quickly as possible to get rid of the horrible mess.
Why do I work this way? Again, one reason is that it made sense
      a couple of decades ago when machines were smaller – your
      browser consumed memory which you wanted to use for something
      else, so you’d only have it open when needed. So this
      is
somewhat
a 1990s habit that I never bothered to
      change.
But, again, I have some more specific reasons too. One is my
      cookie-management policy. I configure Firefox to
      delete
all
cookies when I close the browser, apart from
      a very small number of sites I configured as exceptions. That
      seems to me like a good balance between allowing all cookies
      (everything tracks you everywhere) and refusing cookies
      completely (some sites don’t even work). This way, my
      browser
accepts
the cookies for some website I want to
      use, so nothing actually fails to work – but the next time I use
      the website, the browser has no memory of them. But this only
      delivers a privacy benefit if I didn’t leave the browser running
      between those visits, and closing the whole browser many times a
      day is a good way to do that.
And the other effect of not using my tab bar as my to-read list
      is that if I
do
want to maintain a to-read list, I have
      to do it some other way – and that way will likely involve
      writing the URL down somewhere, with a reminder to myself about
      what it was
for
, maybe where I got it from, and (if
      applicable) what I planned to do with the page when I got to it.
(Even with only a handful of tabs and a short time lapse I can
      be quite absent-minded about that last part! For websites like
      my employer’s CI system, which I might want to open for lots of
      different detailed reasons, it’s not at all unusual for me to
      open a tab with a specific intention, get to it two minutes
      later, and have forgotten what I wanted it for. Remembering the
      point of a URL after a week is right out.)
Turn off X11 session management
At some point in my Linux-using career, desktop environments
      introduced a feature to save the layout of your desktop on
      logout – which applications you had open, where each one’s
      windows were on the screen, and what each one was doing.
      The
idea
is that even if you have to log out, power
      down, and log back in again when you next turn the machine on,
      you can still pick up where you left off.
I expect this might work all right, if you’re the kind of
      computer user who mostly runs office-suite applications. You
      could certainly imagine that a word processor or a spreadsheet
      application would be able to record the important aspects of its
      working state in very little information – “I had a
      window
this
size,
here
, editing
this
document [specified by pathname], with the viewport
      showing
this
section of the document, and the cursor
      right
here
” – and set all of that back up when
      restarted with the right option.
But if you’re mostly a terminal user, who uses the GUI as a
      convenient way to switch focus between half a dozen shell
      prompts and maybe the occasional text editor or web browser,
      it’s hopeless. There’s no possible way to save the state of a
      shell session so that you can pick it up where you left off the
      next day. Or rather, there is, but it involves saving the
      complete internal state of all processes involved – in other
      words, hibernating the machine rather than shutting it down. And
      some things, like an SSH session, wouldn’t even survive that.
For this reason I turned off session management as soon as I
      encountered it. I couldn’t see the point of
      respawning
half
my windows, and not only that, the half
      that weren’t that hard to recreate by hand.
(I’ve also never got round to implementing the application side
      of the session management API in any of my GUI software. It
      wouldn’t make much sense in PuTTY or
pterm
, for the
      reason I’ve just mentioned, but my puzzle collection could
      support this much more easily. However, nobody’s ever complained
      about the lack of it.)
You can probably guess what the running theme is going to be by
      now: because I don’t rely on the system to restart everything in
      the same state I left it, I have to make an effort to remember
      myself what that state
was
. Ideally, this is done by
      making the state simple in the first place, like finishing up a
      task completely and not starting the next. If I do have to leave
      a thing half done (and I’m not just doing a quick reboot and
      getting right back into it), I’ll write down some notes to
      myself to remind myself where I’d got to. And if the half-done
      thing was relying heavily on a particular terminal’s shell
      history (like I kept recalling some complicated test command to
      re-run after each build), that command too is copied into my
      notes, or into a tiny
test.sh
file, or some such,
      so that it’s still available when I start a fresh terminal after
      the next boot.
Use a tmpfs on
~/mem
as my main scratch
      space
When I first got a machine with an SSD instead of an
      old-fashioned spinning-rust hard disk, I had heard of SSD wear,
      and I was a bit worried about it, but I wasn’t quite
      sure
how
worried I ought to be, and wanted to err on
      the side of caution.
I happened to be working on something at the time that involved
      a lot of vigorous disk access in every run,
and
needed
      to be run a lot of times. (It involved databases, so it was
      doing a lot of
fsync
. I was only ever planning to
      run it once on
live
data – it was a one-time format
      conversion – but I had to run it again and again on test data
      until I got it right.) I didn’t want my first act as an SSD user
      to be wearing the whole thing out in the first week by running
      that unfinished program too many times.
My computer at the time had enough RAM that I was able to solve
      the problem by simply making a Linux ‘tmpfs’ – a filesystem
      backed only by RAM (and swap if you have any enabled), which
      vanishes on reboot, or even on umount. I just ran a pair of
      commands along the lines of
mkdir ~/mem
sudo mount -t tmpfs -o size=32g none ~/mem
and then I did all my test runs of that disk-heavy conversion
      tool in there, so it wouldn’t be writing to my nice new SSD at
      all.
Once this exercise had given me the idea of mounting a tmpfs
      inside my home directory, I thought I’d leave it around for a
      while, because I could see other ways it might be useful. I
      ended up keeping it as a permanent part of my workflow, and now
      I’ve set up the same arrangement on all the Linux machines where
      I have root.
In particular, I often want to download some piece of
      software’s source code (via
git clone
,
apt
      source
or just downloading and unpacking a tarball), in
      order to find out one tiny thing about it. Usually, once I’ve
      done that, I don’t need the source code any more – but at the
      moment I’ve answered my initial question, I’m
      never
quite
sure of that, so I’ll leave it around in
      case I want to know something else half an hour later. And then
      of course I forget to delete it.
I used to do that kind of thing in
~/tmp
, which
      was (and is) an ordinary persistent directory on my disk. Of
      course it gradually got more and more full of source trees I
      downloaded once and never used again, and other similar kinds of
      clutter, like large data files I’d
      generated,
strace
logs, etc. Going through and
      cleaning up
~/tmp
was a chore every so often to
      stop my disk filling up.
But it never happens to me any more, because now I put all
      those one-off downloads and log files in
~/mem
, and
      they automatically vanish on the next reboot.
(I still have a
~/tmp
, but now it’s used
      for
less
temporary things – stuff that might need to
      persist for a week or two and survive a reboot, instead of the
      next half hour. I deal with the cleanup issue by datestamping
      most of its subdirectories, so I can see at a glance that
      something was from last year or last decade and guess it’s not
      needed any more.)
Of course, the flip side of this is that I risk losing data I
      actually wanted to keep. But when I put a file or a source tree
      in
~/mem
, I
know
that’s what I’ve done, so
      I keep an eye open for any reason I might want to keep it. And
      if I do want to keep it, I don’t just migrate it
      to
~/tmp
with the same throwaway name: I think of
      somewhere more organised to put it, and give it a more sensible
      name, and maybe write myself a README about what I wanted it
      for. That would be a huge effort if I did it for
every
one-shot download, but it’s not so bad at all if I only do it
      for the small number of things I promote out
      of
~/mem
to persistent storage.
Policy of transience
The common theme between all of those habits is probably
      obvious by now, but I’ll state it more formally anyway.
I consider all of these habits to be instances of a general
      “policy of transience”, which says:
things should either
      be
deliberately
permanent in an organised way, or
      strictly temporary
. I dislike things
accidentally
      turning out
to last for ever.
All the habits I’ve described above can be seen through this
      lens:
My shell history is either temporary (vanishes when I close
        that shell), or deliberately permanent (saved a command in a
        script with a name and an explanation).
A cluster of related applications on my desktop, like a
        terminal and a text editor and a
gitk
or
        something, is either temporary (I close the whole lot
        frequently and in any case it goes away when I log out or
        reboot), or deliberately permanent (if I keep wanting the same
        cluster a lot then I make hot keys and short command aliases
        to restart it any time I want).
Files on my computer are either temporary (because they’re
        in
~/mem
which will be emptied on the next
        reboot), or deliberately permanent (in a sensible directory so
        I’ll know where to find them again, and with an explanation if
        needed).
URLs I want to do something with are either temporary (in my
        browser, which I keep closing down completely) or deliberately
        permanent (saved somewhere else, again with an explanation).
The idea of making things deliberately permanent “in an
      organised way” is fairly vague. Some things I think are often
      important (although not all of them apply in every case):
Stored somewhere reliable
. If I’m going to make
        something permanent, it should live somewhere that’s properly
        backed up. Even worse than a temporary thing accidentally
        becoming permanent is a permanent thing accidentally becoming
        temporary: that’s called “data loss”, and we hates it,
        preciouss.
Easy to find
. It should be named in a way that
        matches how I expect to look for it later. I’ve had some
        remarkable successes with this, sometimes finding a
        15-year-old item exactly where I expected my past self to have
        left it. I’ve also had some spectacular failures, and I know
        which I prefer to encourage!
Explained
. If I find it in passing while looking
        for something else, I shouldn’t need to scratch my head and
        wonder what it’s there for.
Change-controlled
. If it’s evolved over time, it
        should be possible to remember how it changed and what all the
        changes were for, typically by keeping it in version control.
Portable
. If it’s going to be long-term useful to
        me, it’ll probably be useful on more than one machine, so I
        should be able to transfer it between machines: it should live
        in a git repository or something like that, and should have
        minimal (and ideally documented) dependencies on stuff
        provided by the host machine.
Usable by other people
. I haven’t talked about this
        aspect much, because most of my examples above have been about
        my personal workflow. But “save that useful command in a
        script”, taken one step further, becomes “write a man page for
        the script and publish it”, and that can be useful too! In the
        next section I’ll mention another case where this comes
        up.
Other related practices
In this section I’ll mention a couple of practices that other
      people do, which also seem to me as if they’re in line with this
      policy of transience. I don’t impose these on myself personally
      (although in one case I’m considering it), but they’re relevant.
Corporate records management: scheduled deletion of email
Some companies have an internal policy of deleting all email
      older than some specified age (say, a year).
The usual reason, as I understand it, is related to the
      ‘discovery’ stage of a lawsuit, in which (in some circumstances)
      the opposing company gets quite far-reaching rights to dig out
      stuff from inside your company like internal emails, and try to
      find evidence supporting their case. Even if they don’t find the
      evidence they wanted, they still get to find out lots
      of
unrelated
stuff from those emails, which could be
      disadvantageous to you even if they lose the actual lawsuit. For
      both reasons, the less there is for them to dig up in the first
      place, the better.
Of course, if you hastily deleted all your email
after
a lawsuit started, that would be obviously illegal destruction
      of evidence. So the idea is to have a fixed policy in advance,
      and follow it, so that you have defensible grounds for having
      deleted relevant emails: “we’ve been doing that all along on the
      same schedule, it’s our standard policy, it had nothing to do
      with you suing us”. Even so, you probably have to suspend your
      one-year deletion policy while a particular suit is ongoing. But
      at least this way, when the lawsuit starts, they only have one
      year of dirt from
before
the start date to dig up.
I don’t know that I approve of this in general, either
      ethically or from a systems-design perspective. (Surely if the
      discovery rules have over-broad scope, or whatever it is, then
      that’s a problem that should be fixed rather than worked
      around?) But just like a lot of my own habits above, a policy
      adopted for one reason can have unrelated side benefits.
If you’re in an organisation which subjects you to this policy,
      what do you do? Your email archive probably has actually useful
      information in it, and if you have to delete it after a year,
      you’ll lose stuff you wanted to keep.
So you get into the habit of
knowing
that things in
      email are temporary, and if you receive any particuarly
      useful-looking information in email, you make an effort to put
      it somewhere else more sensible. And, just like all the other
      cases above, you put it in a well-thought-out location, directly
      related to its subject matter. That makes it
      actually
easier
to find later than if you had to dig it
      up in your email by a vague memory of who had sent it to
      you.
(I don’t think this violates the spirit of the
      records-management doctrine from the company’s point of view.
      The kind of thing I’m thinking about saving here is more in the
      area of “useful coding and debugging tips” or “how to do some
      complicated thing with that internal web system”, not “juicy
      gossip about who claimed who had violated whose IP rights”!)
In a corporate environment, another thing you’re probably
      concerned about (or should be) is reducing ‘bus factor’: there
      shouldn’t be any important task that only one person can do, or
      important information that only one person knows. That’s another
      reason why keeping useful stuff in your disorganised email
      archive is a bad idea: if you’re on holiday the day someone
      needs to know that crucial fact, or have completely left the
      company, maybe nobody else has that email saved to look it up
      in. So when you copy useful information out of an email you just
      received, you might also make the effort to copy it to
      somewhere
shared
, like your team’s wiki, or a git
      repository full of documentation, or whatever your organisation
      uses for that kind of thing. The scheduled deletion policy helps
      to encourage that, because once it’s forced you to move the
      useful information
somewhere
, it’s not a lot more
      effort to put it somewhere shared than somewhere private.
      (Perhaps even
less
effort.)
I don’t adopt this practice for my personal email, though! It’s
      one thing to have it imposed on you by an employer and look for
      the silver lining, but I wouldn’t do it on my own initiative.
Automated operating system setup from a recipe
Another kind of data that’s not well organised and lasts a long
      time is the configuration of a specific computer. On Linux, I’m
      thinking of all those files you found reasons to edit
      in
/etc
, over the course of years, probably
      forgetting half of the changes you made a week after you’d done
      each one; the precise set of distro packages you installed, and
      why; the stuff you did with
update-alternatives
or
      similar; and so on. On Windows it’d be Control Panel settings
      and registry tinkering, the set of applications you’d installed
      from all over the place (on Windows it’s less likely it’s all
      come from the same place, unless you use nothing but the Store).
      And on both OSes the applications themselves may maintain
      ongoing state of some kind, in
/var
or wherever the
      Windows analogue is.
Of course, you back the whole system up, if it’s important to
      you. But that seems like a wasteful way of doing things. It
      would surely be possible in principle to
describe
the
      configuration of any one of my computers in a small text file,
      along the lines of ‘start from version [
n
] of [distro],
      install [list of packages], make [these] changes to config
      files, run [this] set
      of
mkdir
,
chown
,
chmod
commands etc and [that] set
      of
update-alternatives
’. A file like that would
      contain all the important details of what the system is like,
      and you’d be able to manage it much more easily. It would take
      up Kb rather than Gb; you’d keep it in version control; and you
      could lay out the file itself in a way that was easy to read,
      with each cluster of related changes (even if they were in
      different config files) kept together with a comment explaining
      what they’re there for.
In the containers world, there’s a thing exactly like this: the
      Dockerfile. (Personally I
      use
Podman
in preference to
      Docker itself, because of the really nice rootless mode, but the
      Dockerfile format is common between the two.) I keep a
      collection of rarely-used OS configurations in the form of
      Dockerfiles for various purposes, such as the very minimal
      Kerberos installation I occasionally boot up to test PuTTY’s
      Kerberos integration; it’s convenient not to have the fully
      installed version of that system taking up space all the time,
      and it’s also nice that every time I remake it fresh I know it
      matches the config file, and hasn’t gradually diverged over
      years of accidentally-undocumented tweaking.
But I don’t run my
physical
machines in this way.
      Those are installed in a more conventional way, and are subject
      to exactly this problem – if I did have a total backup failure
      and had to reinstall one of my machines completely from scratch,
      I’m sure it would be months before I stopped tripping over
      missing packages or confusingly different behaviour and got the
      system back to more or less how it had started out. If I could
      even remember.
(I’m mostly talking about
systemwide
configuration
      here. Home directories are a separate consideration, although an
      individual user’s collection of dotfiles has some of the same
      properties. I’m more on top of that side of things: I do have an
      organised git repository containing some of my standard
      dotfiles, and scripts to set up the configuration I like in
      others.)
I think this has something to do with the metaphor I’ve heard
      here and there of treating computer systems “as cattle” –
      relatively interchangeable and somewhat disposable – rather than
      “as pets”, where you have an ongoing relationship with a single
      one and if it died it would be like losing a member of your
      family.
I’m vaguely aware that there
are
methods of managing
      physical computer systems via configuration files of some kind.
      Words like ‘Ansible’ and ‘Puppet’ spring to mind. But I’ve never
      gone to the effort of learning one and deploying it in my
      personal computing infrastructure. I keep toying with the idea,
      though. My firewall machine in particular has been reinstalled
      from scratch at least twice more than is reasonable (though
      because it changed CPU architecture, rather than because the
      backups failed). Even if I only converted
that
machine
      into a tiny config file of some kind, it’d be a win. The bigger
      things like desktop boxes could come later.
Another advantage of managing machines this way is that it
      would be easier to rearrange roles later. If I have a machine
      that currently does two separate jobs, and later I decide there
      should be a separate machine for each of those jobs, it wouldn’t
      be too hard to go through a well commented Dockerfile or similar
      thing and work out which parts of it related to which of the
      tasks, and then I could set up two new install scripts for the
      separated systems.
So I don’t do this
currently
, but I’m tempted by the
      idea, and some day I may start!
Exceptions to the policy
I don’t apply this policy of transience to
all
parts
      of my life, or even all parts of my computer use. It’s not a
      thing I decided on early and planned my whole life around: it’s
      a thing I gradually
noticed
seemed to be a recurring
      theme about how I behave. But it’s not universal.
The biggest exception, as I’ve already mentioned above, is that
      I keep all my personal email permanently – I don’t
      records-manage it as if I were a lawsuit-fearing company.
Another exception is my web browser
history
. I keep my
      open tab collection very small, and I keep my bookmarks well
      organised and version-controlled; but the history of pages I’ve
      visited is persistent and uncontrolled in just the way I didn’t
      want my shell history to be. And I do use it, when I want to dig
      up that page I visited some time last week for some reason I
      couldn’t have predicted in advance (like somebody else has just
      asked me about it).
Why are these two things exceptions to my usual policy? I’m not
      100% sure, because I didn’t do it on purpose. But I have a
      thought. Email and browser history have two things in
      common:
They’re content created by other people, not by me (or at
        least not
mostly
by me).
It’s difficult to predict in advance which parts of them
        will turn out to be useful later.
My shell history (to take an example I
do
treat as
      transient) has neither of these properties. It’s
      almost
all
commands I wrote myself – so if I do
      occasionally lose a useful command from my history, I’m not too
      bothered, because I created it from scratch last time and I’m
      confident I can do that again. A draconian policy of discarding
      history might occasionally waste me a bit of time rewriting
      something, but it’s much rarer that it makes me lose
      something
irreplaceable
. And most shell commands are
      totally boring (the usual round
      of
cd
,
mv
,
rm
and the
      absolutely endless
ls
); the ones that are
      even
potentially
worth saving are easy to spot, because
      they’re the ones that stretch across three lines of my terminal
      and took ten tries to get right.
But emails from friends, family and ex-lovers (for example)
      have sentimental value, and obviously wouldn’t be at all the
      same if I rewrote them myself from scratch later. (Not even my
      own emails
to
those people would be.) And emails about
      technical stuff can come in handy later for all kinds of
      hard-to-predict reasons: for example, someone reports a weird
      error message in a program of mine and I find it was reported
      once before, and now I can maybe see what thing the two cases
      have in common – but it could be
any
of those past
      problem reports, and the vital clue could be any part of the
      message.
Similarly with my browsing history: a lot of the URLs in there
      were delivered to me by websites when I followed links, without
      me typing them in on purpose, and again, it’s hard to
      predict
which
one I’m suddenly going to realise next
      week is just the thing I need to help someone out.
But I do at least promote things from browser history into my
      bookmarks, as soon as I notice I’ve recalled the same one more
      than once or twice. I go to the history for things I couldn’t
      have known in advance I was going to need again, but as soon as
      I
can
reasonably predict I’ll need a thing again, it’s
      worth making it into a bookmark.
So these two things aren’t subject to my usual policy of
      transience. I feel vaguely dissatisfied about that (the browsing
      history in particular), but don’t currently have any plans to
      change it.
Conclusion
As I said at the start, I’m not intending to
persuade
anyone of the rightness of behaving this way. It works for me,
      but different things work for different people.
But I think a lot of the opposite habits are treated as ‘the
      default’ without really considering it. So perhaps some people
      reading this article might not have even
considered
some of these possibilities, and might be doing the opposite
      thing (for example,
increasing
their reliance on shell
      history instead of reducing it) simply because it seemed like
      the only possibility.
So I offer all of this simply as possibilities to think about.
      If any of these things seems useful to you, great – and if you
      think about it and decide you still don’t want to do it, also
      fine.
