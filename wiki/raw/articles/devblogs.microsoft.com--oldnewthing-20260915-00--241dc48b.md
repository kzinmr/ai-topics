---
title: "Why do Microsoft job levels start in the high 50's instead of starting at a sane number like 1?"
url: "https://devblogs.microsoft.com/oldnewthing/20260915-00/?p=112700"
fetched_at: 2026-09-17T10:01:20.321266+00:00
source: "devblogs.microsoft.com/oldnewthing"
tags: [blog, raw]
---

# Why do Microsoft job levels start in the high 50's instead of starting at a sane number like 1?

Source: https://devblogs.microsoft.com/oldnewthing/20260915-00/?p=112700

Those unfamiliar with the Microsoft job level nomenclature are probably very confused that the entry-level full-time software engineering position is described as level 59, with increasing numbers as you get promoted. Why does it start at 59? Why not start with 1 like a sane person?
The level numbers used to start with 1.
In the old days, recent college graduates typically started at levels 10 or 11, with a senior position at level 12, an advanced position at level 13, and a small number of elites at levels 14 and higher.
The problem with that system is that there was very poor granularity. Notice that if you come in as an advanced college graduate at 11, it’s just two promotions before you’re pretty much hit the practical limit. As a result, each level contained a large number of developers, covering a broad range of skills within the level. It was difficult to move up a level because the skill set required to be, say, a 13, was much higher than that required to be a 12. You first had to work your way to the top of your (very large) level, and only then could you work on developing the skills necessary to make the leap the next level. These slow promotion rates created widespread frustration.
To address these problems, each of the old career levels was divided into two or three new career levels, so that moving from one level to the next was a smaller step (and therefore easier to achieve), and so that the employees within a level were closer in talent.
Great. We made the levels narrower and consequently made it easier for employees to receive promotions, creating more easily achieved career milestones and improving morale. But how should we number the new levels?
If the new levels also started counting at 1, then you would have a period of confusion when people talked about being at “level 11” and you had to check whether they were talking about “old level 11” or “new level 11”. And if you ran across a document that said something like “We would probably need two level 11 developers for this project,” you’d have to check the date on the document to figure out whether they are talking about old level 11 or new level 11. And checking the date might not be good enough, because the document may have been written under the old level system, and then somebody made some modifications to an unrelated part of the document, so the last-modified date now comes after the levels changed, but the text in the document is still talking about the old levels.
The solution was to give numbers to the new levels that did not overlap with the numbers for the old levels. (
Sound familiar
?) Even more than that, the new levels had numbers that didn’t even remotely overlap with the old level numbers. Because if the new levels started at 20, people would see a 20 and not be sure if that means “a new level 20” or “some super-genius old level 20, I didn’t know the levels even went that high.”
The new levels therefore started at a lofty 40, and the old level 10 corresponded roughly to a new level 59.
You could say that the numbering system avoids backward compatibility issues.
The old broad levels still show through in the new system in two ways. One is in the job titles. Rather than making up new titles for each of the new narrow levels, the new levels inherited the title from the old level they were split off from. So the old level 10 split up into new levels 59 and 60, but both 59 and 60 have the same title. The other way that the old levels show through is in the rate of promotion: Comparatively speaking, getting promoted to a level that has a new job title requires a greater demonstration of distinction than getting promoted to a higher level within a job title. Internally, we call levels that share a job title a
band
. A promotion to a higher level with the same job title is an
in-band promotion
, whereas one to a new job title is a
cross-band promotion
.
Bonus chatter
: If new college hires come in at old level 10, or new level 59, what were the lower levels 1-9 (new levels 40-58) used for? The level system was designed to cover all possible Microsoft employees, so the lower levels are used for things like summer interns and temporary employees, as well as non-engineering positions like receptionist or mail delivery.
