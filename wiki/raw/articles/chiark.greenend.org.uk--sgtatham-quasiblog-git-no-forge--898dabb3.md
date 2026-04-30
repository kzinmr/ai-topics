---
title: "Git without a forge"
url: "https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/git-no-forge/"
fetched_at: 2026-04-30T07:00:47.110610+00:00
source: "chiark.greenend.org.uk/~sgtatham"
tags: [blog, raw]
---

# Git without a forge

Source: https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/git-no-forge/

Git without a forge
[Simon Tatham, 2025-03-05]
Introduction
I’ve written quite a lot of free software in my life. Most of
      it was from scratch: projects I started myself. So I get to
      choose where to host them – or rather, I
have
to choose
      where to host them.
These days, all my projects are held in Git. And mostly, I put
      them in ‘bare’ git repositories on my personal website.
I don’t use any git ‘forge’ system layered on top of Git, like
      Gitlab or Github, which automatically makes a bug tracking
      database for each project, and provides a convenient button for
      a user to open a merge request / pull request. I just use plain
      Git. People can ‘
git clone
’ my code, and there’s a
      web-based browsing interface (the basic
gitweb
) for
      looking around without having to clone it at all. But that’s all
      the automated facilities you get.
Occasionally this confuses people, so I thought I should write
      something about it.
Purposes of this article
Sometimes people just can’t work out how to send me patches at
      all. Or they can think of several ways, and aren’t sure which is
      best. So one purpose of this article is to be a public statement
      of my own preferences, which I can link to when people ask that
      question.
But it’s also a bit of a musing about
why
I don’t use
      a ‘forge’ style system like Gitlab or Github. People sometimes
      ask me that too – “why don’t you do what everyone else does?” or
      words to that effect.
How to interact with a bare git repo
People who are used to git forges look for a ‘pull request’
      button. When they don’t find it, they sometimes get confused.
If you can’t find a button on a website to submit a patch, how
      do you send your patch to the maintainer?
You send the author an email. And in the email, you put one of
      these things:
A URL to your own clone of the repository, containing your
        patches on top of the ‘upstream’ code.
The actual patches, in some form of email attachment.
Either of these works. For option 2 there are multiple ways to
      do it in detail, and all of
those
work too.
It doesn’t have to be by email, either. Any method of sending
      this data to the maintainer is fine. For example, I’m on
      Mastodon – so you could send me a repository URL via Mastodon if
      you really wanted to (provided you didn’t mind my responses
      being very short). Or you could send patches via any other
      communications medium that you and the maintainer are both on,
      if it lets you attach files to messages.
What do I prefer in particular?
But some people don’t just want to know
any
way to
      send patches. They want to know which is the
best
way,
      or at least the way I prefer.
So here’s my own list, in descending order: most preferred at
      the top, least at the bottom.
BEST: URL of a git repository + branch name
This is my
absolute
favourite way to receive patches.
      If there’s anywhere on the Internet you can put a clone of my
      git repository with some extra patches, then the best thing is
      to do that, and send me an email saying something like
I have some patches to [project] to [make some change]. You
        can find them in the branch called [whatever] here: [URL]
The URL can be anything that’s convenient, as long as it’s
      either something I can give to
git clone
, or a
      human-readable web page
containing
something I can give
      to
git clone
. It can be anything from a git forge
      page (just because
I
don’t host my code on Github
      doesn’t mean you can’t put your patched version there for me to
      look at) to a static site where you’ve uploaded a repository and
      run
git update-server-info
.
When you get right down to it, this is exactly what the
      formalised ‘pull request’ or ‘merge request’ in a git forge
      system
is
. That’s why you start by forking (i.e.
      cloning) the target repository and put your changes in a branch
      of your fork. A PR communicates to the maintainer: “Hey, see
      this repo over here, this branch in particular? It has changes
      I’d like you to take.” The formal PR button in a forge is a way
      to do that with one click, but a short email with all the same
      information is just as good.
Why I like it
: This is my favourite way to receive
      patches because the patches themselves don’t go through my
      email. This saves space for me in the long term (I keep all my
      email), and it saves me messing about with moving attachments
      around (I read email on a different machine from the one I
      develop on). All I need is to paste the URL from the email into
      my git command line, and bing, I’ve got the patches in a form I
      can look at, review, and maybe merge.
Also, if I make review comments and you want to update the
      patches, it saves space
again
if you don’t have to send
      a full set of updated patch files, but instead, push a modified
      version of your branch and just send another email saying
OK, I’ve addressed those review comments. New patches are in
        the same place as before.
An incremental git bundle
Git bundles don’t seem to be very widely known. I think that’s
      a shame, because they’re awesome.
The simplest kind of git bundle – a
full
bundle – is a
      whole git repository, wrapped up into a single file. It contains
      a collection of git objects, plus a collection of references
      (typically branch heads). You can access it by any of the same
      methods you’d use to access an actual git remote, by passing its
      filename to
git fetch
or
git pull
, or
      maybe start with
git ls-remote
to see what branches
      are in the bundle file and decide which one to fetch. The only
      thing you can’t usefully do is modify it. If you want a git
      bundle to contain something different, you just make a fresh one
      from scratch.
But a bundle can also be
incremental
, which means that
      some objects are missing, because it expects the bundle
      recipient to have those objects already. This is just what you
      want when you’re sending patches against an existing repository:
      you know the recipient has all the objects you got from the
      original repo, and you only have to send the new objects.
So, suppose you’ve prepared a series of commits (or just one
      commit) against the
main
branch of one of my
      repositories. Then you can do something like this:
git bundle create fix-weasel-rotator.bundle origin/main..HEAD
That will create a file called
      ‘
fix-weasel-rotator.bundle
’ (example name only!)
      which contains all the extra commits you’ve made on top
      of
origin/main
(my upstream branch). Now you can
      send that file as an attachment.
Why I like it
: If I’m going to receive patches as
      email attachments at all, this is my favourite way to do it, for
      lots of reasons.
Firstly, it’s
one
file, no matter how many patches you
      put in it. That means I can download it in one go to my
      development machine and not have to herd a whole collection of
      smaller files.
Secondly, git bundles are
small
: significantly smaller
      than the corresponding textual patch files. (They use the same
      compression as git’s packed object format.)
Thirdly, git bundles are
binary
: the compression turns
      them into completely impenetrable binary nonsense. That
      doesn’t
sound
like a good thing, but it does give email
      clients the best chance of transferring them completely
      unchanged, without trying to be clever (character set
      conversion, ‘helpfully’ rewrapping long lines).
Perhaps most importantly, the commits in a git bundle are
      described in full detail: I can see what base commit you
      prepared them against, because they come with their parent
      links. So if I need to reapply the patches against a different
      parent, I know what parent I’m starting from, and what’s changed
      since then. This helps me to rebase the patches correctly. So
      does the fact that with the patches already in the form of git
      commits, I can use
git rebase
in the first place,
      and get its really nice conflict handling (better than
git
      am
).
A set of patch files from
git
        format-patch
This is the most popular option people actually seem to choose:
      run ‘
git format-patch
’ to produce a sequence of
      textual patch files, one per commit, with names starting with
      0001, 0002, 0003, … so that the recipient can see what order
      they go in. Then send that lot as a pile of separate email
      attachments, or (rarely) in some single container like a zip
      file.
I don’t think this is quite as nice as a git bundle, for a
      couple of reasons:
Multiple files to herd
. When I get an email with five
      patch attachments, I have five files to copy around instead of
      one, with long awkward names.
Text is vulnerable
. Because the patches are text
      files, there’s at least
some
chance that an MUA did
      something ‘helpful’ (not actually helpful) to them in transit.
Harder to handle conflicts
. The
git am
command, which applies patches in this format, doesn’t handle
      conflicts in the way I most prefer, by applying the parts of the
      patch that worked and leaving in-file conflict markers at the
      places where something went wrong. Also, because
git
      format-patch
doesn’t mention what commit the
      patches
do
apply against, I’m more likely to encounter
      a conflict in the first place when trying to apply them.
So, for all those reasons, I prefer a single binary git bundle
      citing its parent commit to a handful of text patch files. But
      these disadvantages don’t
normally
cause problems:
      the
format-patch
approach normally works well
      enough, and if it’s what a sender is happy with, I won’t spend
      any time trying to persuade them to do things differently.
A bare diff file generated by
git diff
Plain
git diff
has all the same disadvantages
      of
git format-patch
, plus one extra downside: it
      doesn’t include the commit metadata: authorship and commit
      message.
If you send me a plain
git diff
, I have to write
      the commit message myself. That either means understanding your
      patch well enough to know what your
intentions
were (maybe not the same as what you
      actually did!), or copying text out of the email you sent along
      with the patch.
My
general advice
when
      submitting patches by email is that if you have an explanation
      of why the patch is desirable, or safe, or both, it’s better to
      put it in the commit message, so that it’s preserved for later
      people reading the git history. So you might as well put it
      there in the first place, and then I don’t have to move it!
WORST: A series of separate emails generated
        by
git send-email
Ugh, please, no. I really dislike receiving
git
      send-email
output. If you can
possibly
do it
      any other way, please do.
Why I don’t like it
: because the patch series is split
      into multiple emails, they arrive in my inbox in a random order,
      and then I have to save them one by one to files, and manually
      sort those files back into the right order by their subject
      lines.
With
git format-patch
, the files arrive as
      attachments to the same email, so I can save them all in one go,
      and then their names make it easy to sort them.
git
      send-email
has neither advantage.
Why don’t I use a git forge?
I promised I’d also talk about why I make this choice. Most
      people these days like git forges: why don’t I?
Trust
For me, the first question in deciding where to host my code is
      not what facilities it provides, but who runs it. I want my code
      not to be at the mercy of people I don’t trust.
I don’t mean that I have any especial
dis
trust of the
      organisations in charge of major Git forge websites. But I don’t
      know them personally, and I prefer to put my trust in people I
      do. So my git hosting arrangements live on a server run by a
      friend, instead of a server run by a company.
Is that excessive paranoia on my part? I don’t think so.
Perhaps it would be, if all my projects were low-stakes – not
      handling important secrets, and with very few users, so that
      they weren’t an attractive target for anyone to attack. But I
      maintain a security project, and also some of my stuff has
      become pretty popular. Even something completely frivolous like
      a videogame can be an attractive target if it’s installed on a
      lot of machines.
Admittedly, this was a more serious concern before Git: the
      nature of Git’s commit hashing system is that it’s very
      difficult to quietly change the content of a repository to
      something malicious, without everyone who already had a clone of
      it noticing. In the Subversion days it was much easier to
      quietly hack a repository’s contents if you had admin access.
But ‘difficult’ isn’t
impossible
, so it still seems
      worth taking some care.
Trusting a company is also dangerous because management
      changes: even if you trust the people in charge
now
,
      they may not be in charge next year, and the people who are may
      be completely different. The same facilities that attract users
      to Github now would have attracted people to Sourceforge a
      couple of decades ago – and Sourceforge now has a pretty bad
      reputation.
Heavyweight
Of course, using a well-known forge
website
and using
      forge
software
aren’t the same thing. If I don’t want
      to host my code on
gitlab.com
, I could still
      arrange to run my own instance of the Gitlab
software
somewhere under my own control, and use that.
From everything I’ve heard, that’s a lot more effort than
      hosting a plain git repository. I don’t think the overall
      convenience gain is worth the large amount of effort it would
      cost me to run a thing like that. It would take away from time
      I’d rather be spending on the actual code.
Account management
A particular thing I don’t like about git forge websites is the
      way they make you create an account.
Even to
report a bug
against someone else’s project –
      let alone send a patch – if it’s hosted in some Gitlab instance
      I haven’t used before, I have to make an account on that
      instance, because until I do that, I can’t interact with the
      system at all. And it’s not
just
instances I haven’t
      used before: at least some Gitlab instances will delete old
      accounts, so that even if I
have
interacted with a
      project before, when I find another bug in the same software
      years later I might still have to make a fresh account.
Making accounts is a
bad thing
. Every one of them is
      an extra thing to track in your password manager; some kind of
      2FA setup if the site insists on it; periodic need to spend
      effort on it (like if the site notifies you that they’ve had a
      compromise and you need to reconfirm something); an outright
      risk (like if a
scammer
pretending to be the site sends
      you a fraudulent notification of that kind); an extra facet of
      your online identity to keep track of. Each one is individually
      small, but they add up, and managing a ton of accounts is
      annoying. I don’t enjoy having to do that myself, and I don’t
      want to inflict it on other people!
You get a workflow imposed on you
Git forge websites come with a bunch of stuff beyond the plain
      git repository. That’s their whole point.
In particular, your project automatically gets a bug tracker –
      and you don’t get a choice about what bug tracker to use, or
      what it looks like. If you use Gitlab, you’re using the Gitlab
      bug tracker. The same goes for the pull request / merge request
      system.
When I started using Git, PuTTY already
had
a bug
      tracker. A pretty simple one – not much more than a set of text
      files and a script that turns them into a set of web pages – but
      it’s there, and it integrates with our source control and
      releases and website in ways we’re familiar with. Throw it away
      in favour of a thing tied to the hosting system which doesn’t
      behave the way we carefully chose? No thanks.
More generally, I don’t want that kind of decision about my
      development workflows to be a consequence of some unrelated
      thing like what version control I’m using. I want to
      decide
first
how to handle patches and bug reports, and
      then decide what software will best serve those needs – not the
      other way round.
Update, 2025-03-06
: Colin Watson
      kindly
informs me that I’m more or less completely wrong
      about this when it comes to Gitlab: you can turn off the issue
      tracker on a repository, and merge requests too if you want
      to.
Plain old inertia
I wouldn’t want anyone to think I was
concealing
this
      reason, or deluding myself that it wasn’t part of my
      motivations, so I should make sure to say it out loud.
One reason I don’t use a forge is simply because I
      didn’t
start out
using a forge, and moving all my stuff
      into one would be effort. I’ve been providing public source
      repositories since before Git was a thing, and before forges
      themselves were a thing. (OK, not
quite
before the
      pre-Git Sourceforge was actually founded, but before it was well
      known.) Before Git, my stuff was hosted in SVN on a particular
      Linux box; when I moved my stuff from SVN to Git, the path of
      changing as little as possible was to host it in Git on the same
      Linux box.
Of course, that’s not a good reason by itself. And that’s all
      right – it’s not my
only
reason. But I can’t deny that
      it’s
one
of my reasons. Change is effort, and ought to
      give enough benefit to be worth the effort.
Special mention: especially not Github
For all these reasons, I don’t really want to use
any
git forge. But I
particularly
don’t want to use
      Github.
The biggest reason is that it’s not itself free software. If
      you want to take back control of your project by moving it to
      another instance of the same system (perhaps even setting up
      your own), you can do that with Gitlab – migrating all your bug
      records along with the git repository – but not with Github.
      You’re locked in.
Also, I might as well come out and say this: one reason I don’t
      want to use Github is
because
it’s the most popular
      place to host your code. It’s almost never healthy to have a
      monoculture of
anything
, and a monoculture controlled
      by a single company is particularly dangerous. I’d rather
      contribute to the Internet being distributed than contribute to
      it being centralised.
(I get particularly annoyed when people demand I move to Github
      for this reason. “Everyone is on Github, get with the programme!
      Conform!” I’m actually less likely to do it
because
you
      said that. Ugh.)
Of course, these days Github is owned by Microsoft, and there
      are plenty of people who don’t 100% trust Microsoft. I can’t
      claim to be completely immune to that, but I
already
didn’t want to use Github before it was bought, so that’s not my
      only reason. Not even my main reason.
Should I start using a git forge instead?
Sometimes I get email from people who would prefer me to start
      doing things the ‘normal’ way. It’s not
always
just
      because my way isn’t what they’re already used to. Some of them
      have more interesting and thoughtful reasons.
The most interesting comment I’ve had along these lines is that
      a forge puts all your interactions with contributors out in the
      open. If someone is considering contributing to your code base,
      they can look at past MRs / PRs and see what happened: whether
      there seems to be an active community at all, whether the
      developer(s) respond to contributions in good time, whether the
      reviews seem constructive, whether there’s any obnoxious or
      toxic behaviour going on. And then maybe decide not to waste
      their time on that project at all, if it doesn’t look
      welcoming or helpful.
With my approach, where each discussion of a contribution
      happens in private email, it is true that the process of making
      a contribution is a lot less public. I could be amazingly rude
      to one contributor, and none of the others would necessarily
      find out about it (unless the hypothetical victim ranted about
      it on their blog, or something). I could take ages to get round
      to doing anything (for any reason – laziness or overloading or
      anything in between). I could lie to each contributor about what
      other contributors were doing (although I can’t think of any
      reason it would even be in my own interest to!)
So I accept that there are downsides of doing it my way, as
      well as upsides. Forges aren’t a complete waste of time. I just
      haven’t yet been convinced that the advantages of a forge
      outweigh the disadvantages.
But I’d be more interested in thoughts about how to get the
      best of both worlds. If there were a system for allowing
      contributions and their review and discussion to happen in
      public, using software much more lightweight and easier to run
      than Gitlab, which allowed contribution without requiring anyone
      to create and manage yet another account, with an extremely
      configurable form of workflow management (if any), and having a
      hard separation between the discussion-forum layer and the
      actual git repository so that a compromise wouldn’t allow
      injecting malware into the target project, I’d be interested in
      giving it a look!
(Of course, just occasionally a contribution
does
have
      to happen via private communication, e.g. because it’s a fix for
      a not-yet-public security issue. I certainly wouldn’t want
      to
stop
people from contributing privately, if it was
      necessary, or just if that was what they preferred.)
