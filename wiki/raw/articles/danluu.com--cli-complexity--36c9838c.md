---
title: "The growth of command line options, 1979-Present"
url: "https://danluu.com/cli-complexity/"
fetched_at: 2026-05-05T07:01:31.115299+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# The growth of command line options, 1979-Present

Source: https://danluu.com/cli-complexity/

My hobby
: opening up
McIlroy’s UNIX philosophy
on one monitor while reading manpages on the other.
The first of McIlroy's dicta is often paraphrased as "do one thing and do it well", which is
shortened from
"Make each program do one thing well. To do a new job, build afresh rather than complicate old programs by adding new 'features.'"
McIlroy's example of this dictum is:
Surprising to outsiders is the fact that UNIX compilers produce no listings: printing can be done better and more flexibly by a separate program.
If you open up a manpage for
ls
on mac, you’ll see that it starts with
ls [-ABCFGHLOPRSTUW@abcdefghiklmnopqrstuwx1] [file ...]
That is, the one-letter flags to
ls
include every lowercase letter except for
{jvyz}
, 14 uppercase letters, plus
@
and
1
. That’s 22 + 14 + 2 = 38 single-character options alone.
On ubuntu 17, if you read the manpage for coreutils
ls
, you don’t get a nice summary of options, but you’ll see that
ls
has 58 options (including
--help
and
--version
).
To see if
ls
is an aberration or if it's normal to have commands that do this much stuff, we can look at some common commands, sorted by frequency of use.
command
1979
1996
2015
2017
ls
11
42
58
58
rm
3
7
11
12
mkdir
0
4
6
7
mv
0
9
13
14
cp
0
18
30
32
cat
1
12
12
12
pwd
0
2
4
4
chmod
0
6
9
9
echo
1
4
5
5
man
5
16
39
40
which
0
1
1
sudo
0
23
25
tar
12
53
134
139
touch
1
9
11
11
clear
0
0
0
find
14
57
82
82
ln
0
11
15
16
ps
4
22
85
85
ping
12
12
29
kill
1
3
3
3
ifconfig
16
25
25
chown
0
6
15
15
grep
11
22
45
45
tail
1
7
12
13
df
0
10
17
18
top
6
12
14
This table has the number of command line options for various commands for v7 Unix (1979), slackware 3.1 (1996), ubuntu 12 (2015), and ubuntu 17 (2017). Cells are darker and blue-er when they have more options (log scale) and are greyed out if no command was found.
We can see that the number of command line options has dramatically increased over time; entries tend to get darker going to the right (more options) and there are no cases where entries get lighter (fewer options).
McIlroy has long decried the increase in the number of options, size, and general functionality of commands
:
Everything was small and my heart sinks for Linux when I see the size [inaudible]. The same utilities that used to fit in eight k[ilobytes] are a meg now. And the manual page, which used to really fit on, which used to really be a manual
page
, is now a small volume with a thousand options... We used to sit around in the UNIX room saying "what can we throw out? Why is there this option?" It's usually, it's often because there's some deficiency in the basic design — you didn't really hit the right design point. Instead of putting in an option, figure out why, what was forcing you to add that option. This viewpoint, which was imposed partly because there was very small hardware ... has been lost and we're not better off for it.
Ironically, one of the reasons for the rise in the number of command line options is another McIlroy dictum, "Write programs to handle text streams, because that is a universal interface" (see
ls
for one example of this).
If structured data or objects were passed around, formatting could be left to a final formatting pass. But, with plain text, the formatting and the content are intermingled; because formatting can only be done by parsing the content out, it's common for commands to add formatting options for convenience. Alternately, formatting can be done when the user leverages their knowledge of the structure of the data and encodes that knowledge into arguments to
cut
,
awk
,
sed
, etc. (also using their knowledge of how those programs handle formatting; it's different for different programs and the user is expected to, for example,
know how
cut -f4
is different from
awk '{ print $4 }'
). That's a lot more hassle than passing in one or two arguments to the last command in a sequence and it pushes the complexity from the tool to the user.
People sometimes say that they don't want to support structured data because they'd have to support multiple formats to make a universal tool, but they already have to support multiple formats to make a universal tool. Some standard commands can't read output from other commands because they use different formats,
wc -w
doesn't handle Unicode correctly, etc. Saying that "text" is a universal format is like saying that "binary" is a universal format.
I've heard people say that there isn't really any alternative to this kind of complexity for command line tools, but people who say that have never really tried the alternative, something like PowerShell. I have plenty of complaints about PowerShell, but passing structured data around and easily being able to operate on structured data without having to hold metadata information in my head so that I can pass the appropriate metadata to the right command line tools at that right places the pipeline isn't among my complaints.
The sleight of hand that's happening when someone says that we can keep software simple and compatible by making everything handle text is the pretense that text data doesn't have a structure that needs to be parsed. In some cases, we can just think of everything as a single space separated line, or maybe a table with some row and column separators that we specify (
with some behavior that isn't consistent across tools, of course
). That adds some hassle when it works, and then there are the cases where serializing data to a flat text format adds considerable complexity since the structure of data means that simple flattening requires significant parsing work to re-ingest the data in a meaningful way.
Another reason commands now have more options is that people have added convenience flags for functionality that could have been done by cobbling together a series of commands. These go all the way back to v7 unix, where
ls
has an option to reverse the sort order (which could have been done by passing the output to something like
tac
had they written
tac
instead of adding a special-case reverse option).
Over time, more convenience options have been added. For example, to pick a command that originally has zero options,
mv
can move
and
create a backup (three options; two are different ways to specify a backup, one of which takes an argument and the other of which takes zero explicit arguments and reads an implicit argument from the
VERSION_CONTROL
environment variable; one option allows overriding the default backup suffix).
mv
now also has options to never overwrite and to only overwrite if the file is newer.
mkdir
is another program that used to have no options where, excluding security things for SELinux or SMACK as well as help and version options, the added options are convenience flags: setting the permissions of the new directory and making parent directories if they don't exist.
If we look at
tail
, which originally had one option (
-number
, telling
tail
where to start), it's added both formatting and convenience options For formatting, it has
-z
, which makes the line delimiter
null
instead of a newline. Some examples of convenience options are
-f
to print when there are new changes,
-s
to set the sleep interval between checking for
-f
changes,
--retry
to retry if the file isn't accessible.
McIlroy says "we're not better off" for having added all of these options but I'm better off. I've never used some of the options we've discussed and only rarely use others, but that's the beauty of command line options — unlike with a GUI, adding these options doesn't clutter up the interface. The manpage can get cluttered, but in the age of google and stackoverflow, I suspect many people just search for a solution to what they're trying to do without reading the manpage anyway.
This isn't to say there's no cost to adding options — more options means more maintenance burden, but that's a cost that maintainers pay to benefit users, which isn't obviously unreasonable considering the ratio of maintainers to users. This is analogous to Gary Bernhardt's comment that it's reasonable to practice a talk fifty times since, if there's a three hundred person audience, the ratio of time spent watching to the talk to time spent practicing will still only be 1:6. In general, this ratio will be even more extreme with commonly used command line tools.
Someone might argue that all these extra options create a burden for users. That's not exactly wrong, but that complexity burden was always going to be there, it's just a question of where the burden was going to lie. If you think of the set of command line tools along with a shell as forming a language, a language where anyone can write a new method and it effectively gets added to the standard library if it becomes popular, where standards are defined by dicta like "write programs to handle text streams, because that is a universal interface", the language was always going to turn into a write-only incoherent mess when taken as a whole. At least with tools that bundle up more functionality and options than is UNIX-y users can replace a gigantic set of wildly inconsistent tools with a merely large set of tools that, while inconsistent with each other, may have some internal consistency.
McIlroy implies that the problem is that people didn't think hard enough, the old school UNIX mavens would have sat down in the same room and thought longer and harder until they came up with a set of consistent tools that has "unusual simplicity". But that was never going to scale, the philosophy made the mess we're in inevitable. It's not a matter of not thinking longer or harder; it's a matter of having a philosophy that cannot scale unless you have a relatively small team with a shared cultural understanding, able to to sit down in the same room.
Many of the main long-term UNIX anti-features and anti-patterns that we're still stuck with today, fifty years later, come from the "we should all act like we're in the same room" design philosophy, which is the opposite of the approach you want if you want to create nice, usable, general, interfaces that can adapt to problems that the original designers didn't think of. For example, it's a common complain that modern shells and terminals lack a bunch of obvious features that anyone designing a modern interface would want. When you talk to people who've written a new shell and a new terminal with modern principles in mind, like Jesse Luehrs, they'll note that a major problem is that the UNIX model doesn't have a good seperation of interface and implementation, which works ok if you're going to write a terminal that acts in the same way that a terminal that was created fifty years ago acts, but is immediately and obviously problematic if you want to build a modern terminal. That design philosophy works fine if everyone's in the same room and the system doesn't need to scale up the number of contributors or over time, but that's simply not the world we live in today.
If anyone can write a tool and the main instruction comes from "the unix philosophy", people will have different opinions about what "
simplicity
" or "doing one thing" means, what the right way to do things is, and inconsistency will bloom, resulting in the kind of complexity you get when dealing with a wildly inconsistent language, like PHP. People make fun of PHP and javascript for having all sorts of warts and weird inconsistencies, but as a language and a standard library, any commonly used shell plus the collection of widely used *nix tools taken together is much worse and contains much more accidental complexity due to inconsistency even within a single Linux distro and there's no other way it could have turned out. If you compare across Linux distros, BSDs, Solaris, AIX, etc.,  the amount of accidental complexity that users have to hold in their heads when switching systems dwarfs PHP or javascript's incoherence. The most widely mocked programming languages are paragons of great design by comparison.
To be clear, I'm not saying that I or anyone else could have done better with the knowledge available in the 70s in terms of making a system that was practically useful at the time that would be elegant today. It's easy to look back and find issues with the benefit of hindsight. What I disagree with are comments from Unix mavens speaking today; comments like McIlroy's, which imply that we just forgot or don't understand the value of simplicity, or
Ken Thompson saying that C is as safe a language as any and if we don't want bugs we should just write bug-free code
. These kinds of comments imply that there's not much to learn from hindsight; in the 70s, we were building systems as effectively as anyone can today; five decades of collective experience, tens of millions of person-years, have taught us nothing; if we just go back to building systems like the original Unix mavens did, all will be well. I respectfully disagree.
Appendix: memory
Although addressing McIlroy's complaints about binary size bloat is a bit out of scope for this, I will note that, in 2017, I bought a Chromebook that had 16GB of RAM for $300. A 1 meg binary might have been a serious problem in 1979, when a standard Apple II had 4KB. An Apple II cost $1298 in 1979 dollars, or $4612 in 2020 dollars. You can get a low end Chromebook that costs less than 1/15th as much which has four million times more memory. Complaining that memory usage grew by a factor of one thousand when a (portable!) machine that's more than an order of magnitude cheaper has four million times more memory seems a bit ridiculous.
I prefer slimmer software, which is why I optimized my home page down to two packets (it would be a single packet if my CDN served high-level brotli), but that's purely an aesthetic preference, something I do for fun. The bottleneck for command line tools isn't memory usage and spending time optimizing the memory footprint of a tool that takes one meg is like getting a homepage down to a single packet. Perhaps a fun hobby, but not something that anyone should prescribe.
Methodology for table
Command frequencies were sourced from public command history files on github, not necessarily representative of your personal usage. Only "simple" commands were kept, which ruled out things like curl, git, gcc (which has > 1000 options), and wget. What's considered simple is arbitrary.
Shell builtins
, like
cd
weren't included.
Repeated options aren't counted as separate options. For example,
git blame -C
,
git blame -C -C
, and
git blame -C -C -C
have different behavior, but these would all be counted as a single argument even though
-C -C
is effectively a different argument from
-C
.
The table counts sub-options as a single option. For example,
ls
has the following:
--format=WORD
across -x, commas -m,  horizontal  -x,  long  -l,  single-column  -1,  verbose  -l, vertical -C
Even though there are seven format options, this is considered to be only one option.
Options that are explicitly listed as not doing anything are still counted as options, e.g.,
ls -g
, which reads
Ignored; for Unix compatibility.
is counted as an option.
Multiple versions of the same option are also considered to be one option. For example, with
ls
,
-A
and
--almost-all
are counted as a single option.
In cases where the manpage says an option is supposed to exist, but doesn't, the option isn't counted. For example, the v7
mv
manpage says
BUGS
If file1 and file2 lie on different file systems, mv must copy the file and delete the original.  In this case the owner name becomes that of the copying process and any linking relationship with other files is lost.
Mv should take
-f
flag, like rm, to suppress the question if the target exists and is not writable.
-f
isn't counted as a flag in the table because the option doesn't actually exist.
The latest year in the table is 2017 because I wrote the first draft for this post in 2017 and didn't get around to cleaning it up until 2020.
mjd on the Unix philosophy, with an aside into the mess of /usr/bin/time vs. built-in time
.
mjd making a joke about the proliferation of command line options in 1991
.
On HN:
p1mrx:
It's strange that ls has grown to 58 options, but still can't output \0-terminated filenames
As an exercise, try to sort a directory by size or date, and pass the result to xargs, while supporting any valid filename. I eventually just gave up and made my script ignore any filenames containing \n.
whelming_wave:
Here you go: sort all files in the current directory by modification time, whitespace-in-filenames-safe.
The
printf (od -> sed)' construction converts back out of null-separated characters into newline-separated, though feel free to replace that with anything accepting null-separated input. Granted,
sort --zero-terminated' is a GNU extension and kinda cheating, but it's even available on macOS so it's probably fine.
printf '%b' $(
        find . -maxdepth 1 -exec sh -c '
          printf '\''%s %s\0'\'' "$(stat -f '\''%m'\'' "$1")" "$1"
        ' sh {} \; | \
        sort --zero-terminated | \
        od -v -b | \
        sed 's/^[^ ]*//
      s/ *$//
      s/  */ \\/g
      s/\\000/\\012/g')
If you're running this under zsh, you'll need to prefix it with `command' to use the system executable: zsh's builtin printf doesn't support printing octal escape codes for normally printable characters, and you may have to assign the output to a variable and explicitly word-split it.
This is all POSIX as far as I know, except for the sort.
The Unix haters handbook
.
Why create a new shell
?
Thanks to Leah Hanson, Jesse Luehrs, Hillel Wayne, Wesley Aptekar-Cassels, Mark Jason Dominus, Travis Downs, and Yuri Vishnevsky for comments/corrections/discussion.
