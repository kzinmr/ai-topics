---
title: "Refactoring English"
url: "https://refactoringenglish.com/services/blog-editing/sample-future-of-git/"
fetched_at: 2026-04-29T07:01:23.314940+00:00
source: "refactoringenglish.com"
tags: [blog, raw]
---

# Refactoring English

Source: https://refactoringenglish.com/services/blog-editing/sample-future-of-git/

Sample Blog Editing Notes
The notes below are my
blog editing notes
for the first draft of Tyler Cipriani’s article,
“The future of large files in Git is Git.”
I worked with Tyler to:
Reach a clearer understanding of his target audience
Focus the post on practical lessons the reader can apply
Find a structure that feels clear and intuitive
Tyler’s finished article enjoyed a strongly positive reception:
What’s working well
Broadly relevant topic
I love the topic because it’s relevant to a large number of developers, especially on places like Hacker News.
Many developers have encountered the problem of storing large files on git. Maybe they’ve used git LFS, or maybe they’ve never tried it because it seems too complicated. I think all of these people would be excited to hear that there’s a better alternative.
Clear, intuitive structure
The article presents the information well. It makes it clear what the reader will gain from the article, it breaks the ideas into sections with clear headings, and the order of information is logical and easy to follow.
Opportunities for improvement
Deliver on the promise
The biggest issue I have with the current draft is that it feels like it overpromises and underdelivers. The intro gets me excited that I can manage large files using git’s native utilities, but the examples feel pretty difficult.
With git LFS, everyone working on a repo can happily go about their work without thinking about git LFS unless they need to work with large files. But with the git-native alternatives, the default experience is slow clones and bloated storage. All the contributors need to make repo-specific changes to their standard git workflows to avoid issues, whereas with git LFS, the default experience is fine for anyone who doesn’t need the large files locally.
I think the article needs to either provide paths where native git can be as convenient for collaborators as git LFS or scale back the initial claim to something more modest like, “For
solo projects
, here’s how you can manage large files without git LFS.”
Capture what’s exciting in the title
Assuming the article can deliver on its promise (above), the current title “Vanilla Git for Large Files” doesn’t capture what I think is compelling, which is that git has changed, and the conventional wisdom about large files in git is no longer correct.
Consider alternatives that make the exciting news more obvious:
You Can Now Use Vanilla Git for Large Files
Vanilla Git Now Handles Large Files Well
Use Vanilla Git for Large Files
Make the value more obvious in the introduction
My rule of thumb is that within the first three sentences, the reader should be able to answer these two questions:
Did the author write this article for someone like me?
How will I benefit from reading it?
Here are the first three sentences in the current draft:
Today, git LFS is the standard for storing large files in git. But new git commands may mean you no longer need it.
Large files create pain for git users.
I think the intro successfully answers those two questions, but we can do it even faster.
I’d start with the pain point people recognize: storing large files in git sucks. The number of people who know that is a subset of the people who are familiar with git LFS, so I’d lead with the pain point. Here’s a suggested rewrite that focuses on the pain:
For most of its history, git has handled large files poorly. Adding large files to a git repository bloats its storage, which slows down clone operations and continuous integration jobs. Most developers turn to third-party git extensions like git LFS to manage large files, but recent improvements allow git to manage large files without any third-party extensions.
Give a simple answer to people who want it simple
I see two audiences for this post:
People who are interested in the different options for managing large files in git and their tradeoffs.
People who don’t care about a complicated decision and want a simple rule of thumb for “how should I deal with large files in git?”
Right now, the article feels aimed at audience (1), but you can serve audience (2) without alientating the detail lovers. Group (2) is the much larger group, and they’ll share and upvote the article on social media, which will make it more visible to people in group (1).
Consider adding a section right after the intro that gives a simple answer for common scenarios like:
Scenario
Recommended strategy
You have a few large files that change infrequently
git partial clone
You have many or frequenly changing large files
git Large Object Promisers
…
…
I think Scott Chacon did this well in a recent
post about git’s configuration options
.
Show your work
I noticed a pattern in the article where it makes a provable claim but omits the evidence. In most cases, the evidence is just showing a single command.
For example:
The script above creates a git repo with
a 280MB
database.db
in our working directory.
In that case, I think it would be helpful to show the command to make the reader feel like they’re riding along in the terminal with you:
$ du -h database.db
280M  database.db
This happens in a few other places:
But the repo’s total size
is 578MB.
Git’s object database
stores two compressed copies
of
database.db
plus the space needed by the working directory
.
After running
git lfs migrate import --include="*.db"
, our database file
looks like this
inside git:
Clones MediaWiki
88% faster
vs. a straight
git clone
without a filter.
Keep the reader in your article
If a reader is part of your target audience, they should be able to read the article from start to finish and understand everything without having to go outside the article to look things up. It’s fine to leave breadcrumbs for them to explore topics more deeply, but the reader shouldn’t feel like they have to go do extra research to understand what the article says at a basic level.
The article uses a few terms that I don’t think the average git user would recognize:
“All git large-file storage solutions are hacks of
git’s smudge and clean filters
.”
“You can fight this using
an LFS transfer agent
, but that makes your set up even more fiddly.”
The more the article uses terms the reader doesn’t recognize, the more they think, “Oh, maybe this article is actually not for people like me, so I should stop reading here.”
It’s fine to use terms the reader might not recognize, but the article should gently introduce those terms rather than take it for granted that the reader will recognize them.
There’s also a section that pushes the reader out of the article with the link to the
rev-list
documentation:
Other options are available on git’s rev-list man page.
The article doesn’t have to duplicate the entire man page, but I think it would be helpful to list two or three of the most useful/common options and what they do.
What happens in CI?
I noticed a bit of a gap in that the current draft doesn’t address continuous integration (CI). With git LFS, if I have a bunch of CI jobs that don’t depend on the LFS-managed files, everything works fine. With the LFS alternatives in the article, my CI jobs would default to downloading all of the large files, which would slow down CI significantly in some cases.
Slow down the sparse checkouts explanation
I had trouble following the explanation of sparse checkouts.
It shows a sequence of commands without much explanation. This would be easier to follow if the article explained the commands more beforehand so the reader understands what they’re seeing.
I also didn’t understand the
--cone
flag. I like that there’s a diagram, but I didn’t understand it because the files and folders in the diagram don’t match the output of the previous
tree
command.
Tweaks to the git LFS section
I thought “What’s wrong with Git LFS?” was strong, but I had a few thoughts about possible improvements:
“Centralized” is the current bullet, but to me “High vendor lock-in” would feel a bit more clear.
And “hard to undo” could merge into “high vendor lock-in.”
Under the “Costly” bullet, I think it would be helpful to show hypothetical costs on a 50 GB repo, especially if you have automated jobs that run daily/weekly. And then highlight how if these prices go up, you’re stuck.
I expected the bullet ordering to go from most severe to least severe, but that’s not how I’d rank these items (though I know this is subjective). Vendor lock-in is the worst to me, followed by the cost.
“Hacky” feels a bit too hand-wavey. Are there concrete examples the article could link to where git LFS has caused problems?
“Fragile” feels not compelling to me. It doesn’t seem meaningfully different from how you might accidentally commit a file in native git because you forgot to add it to
.gitignore
.
Minor notes
Git LFS tried to solve these problems
This feels like the start of a new section. It doesn’t quite fit under, “What’s the problem with large files in git?”
Now, after I force push to GitHub to rewrite project history, folks working with me get a different experience.
I found the wording confusing because there’s ambiguity between “different from your experience as committer” and “different from the non-LFS experience.”
Git LFS keeps large files outside git’s guts while keeping those files’ histories integrated with git.
This line tripped me up. I think it’s because saying “those files’ histories” aloud is a bit of a tongue-twister. Even though I’m reading it in my head, I think there’s a natural stumbling on sequences that would be difficult to say louad.
After running
git lfs migrate import --include="\*.db"
, our database file looks like this inside git:
This part confused me because I wasn’t sure if the implication is that we’re running this command after the previous commands or if we’re running it after just the
database.db
commands but before the
git commit
command.
The option I use most often is
--filter='blob:none'
, which avoids downloading any files not needed for the current checkout.
I didn’t understand this. How would git know at repo clone time which files you plan to use?
git commit -m 'Add junk data'
In general, I recommend
using verbose command-line flags
(e.g.,
git commit --message
) for better readability.
The Linus Torvalds quote feels not relevant enough to include.
I know it’s not central to the argument, but when I saw that the quote was from 2009, my first thought was, “Is that still true 16 years and however many git versions later?”
To me, it’s a bit like saying Apple knows it’s behind on streaming TV shows, as evidenced by this thing Tim Cook said in 2009.
If you do include it, I recommend linking directly to the quote.
“Setup” is a noun, and “set up” is a verb, but the article gets this backwards in a couple of places:
“Makes your
set up
even more…” should be “makes your
setup
…”
“…your collaborators must install and
setup
git…” should be “…your collaborators must install and
set up
git…”
The draft uses inconsistent capitalization on “git” vs. “Git”.
