---
title: 'Google SRE - SRE for Developers: Insights and Innovations'
source_url: https://sre.google/workbook/conclusion/
license: CC-BY-NC-ND-4.0
license_url: https://creativecommons.org/licenses/by-nc-nd/4.0/
attribution: Google, Inc.; editors Betsy Beyer, Niall Richard Murphy, David K. Rensin,
  Kent Kawahara, Stephen Thorne; O’Reilly, 2018
reuse_scope: Unmodified originals; noncommercial archive. Text is a technical format
  conversion; no translation or content edits.
publication_year: 2018
original_html: original-source.zip!/conclusion.html
original_sha256: ce0f2ec6a3c4464099c4405e11168906a1424417a4531a7b01d535237e60e547
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://sre.google/workbook/conclusion/
ingested: '2026-10-14'
sha256: af97805c4c1506b9a63f34ef7923dff3131331b65b1fe94afa0e2c4f571f044f
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
Conclusion
By Dave Rensin, Betsy Beyer, Niall Richard Murphy,
Stephen Thorne, and Kent Kawahara
Onward…
The American economist Edgar Fiedler used to say that “[h]e who lives by the crystal ball soon learns to eat ground glass.” Predicting the future is dangerous.
Nonetheless, we’re going to risk the broken glass and try to say a few useful words about what we think comes after this book.
The Future Belongs to the Past
Our experiences since the publication of the first
SRE book
and the process of assembling this volume have clearly demonstrated a huge pent-up demand for SRE from enterprises both large and small. From this, some interesting observations emerge.
First, large enterprises tend to have correspondingly large appetites to adopt SRE practices in a robust way. The familiar meme that large enterprises are slow to change is decidedly not true in this case. We expect to see a lot of interesting innovation in the SRE space from these firms over the next year, and that’s really exciting.
Next, smaller firms are finding ways to adopt SRE practices regardless of whether or not they can staff a full-blown, globally distributed SRE team. We’ve long speculated that although the substance and sequence of the dishes are vitally important, people don’t have to eat the whole SRE meal at once. We are now seeing that notion put into good practice, and that’s also really exciting because it allows everyone to participate.
Finally, if you are reading this book and wondering if there’s a market opportunity for you to offer services or build products that help firms adopt SRE, then the answer is a resounding yes. In fact, if that’s something you decide to do, please let us know through O'Reilly at
bookquestions@oreilly.com
. We’d like to keep up with your progress.
SRE + <Insert Other Discipline>
We heard from many thoughtful people that SRE principles and practices seem like they should also apply to other disciplines—particularly security. We didn’t cover the SRE/security overlap in the first book (or this book), but this is clearly a quickly burgeoning area of focus. If you’re wondering why we didn’t cover it in any depth in this volume, it’s because we’re not sure what we want to say about it (yet).
At the time of this writing (early spring 2018) we’re already seeing the emergence of the term
DevSecOps
—a recognition that development, security, and operations are all interdependent—in the marketplace. If you’re an SRE looking for a useful and unexplored space in which to spend some time, that’s a really good candidate!
In general, we think this is the start of a trend toward asking, “How would SRE be applied to <insert other discipline>?” It certainly stands to reason that some SRE principles and practices could have value in other domains.
We’re pretty excited to see where that leads…
Trickles, Streams, and Floods
The number of people offering to contribute content to this volume was much larger than the previous volume. That seems easy enough to explain—the first book was pretty popular, so people were keen to contribute to the second one. However, the
variety
of people offering to pitch in has been interesting. The types and range of the content proposals we evaluated surprised us. For example, a team of lawyers approached us about how they might incorporate error budgets into nontechnical legal agreements. How SRE applies to the legal profession is a topic clearly out of scope for this book, but is probably really interesting to a whole other professional population.
Because of this variety, we decided that this volume will not just be an implementation companion to the previous book. It will also be a launching point for whole new streams of SRE-related content. That means more books, articles, podcasts, videos, and who knows what else. This volume is a beginning, not an end.
SRE Belongs to All of Us
When we started work on the first book, our primary motivation was to explain SRE—this interesting thing we do to make Google work well for our users. It seemed useful to spread that knowledge around.
In our enthusiasm to explain our view of the world, we anchored on our direct experiences. As a result, we unintentionally alienated some in the larger DevOps community and beyond, who felt we ignored other organizations’ contributions to the field. This volume aims to correct that mistake by devoting considerable space to discussing DevOps and SRE and why they are not at odds.
To our great joy, SRE is a growing community of practitioners that now extends very far outside of Google. In fact, it’s likely that the number of non-Google SREs will significantly outnumber Google SREs by the time you read this.
Whatever its history, SRE is now a global community of which Google is one member. It belongs to all of us, and that’s a good thing. It’s already abundantly clear, via conferences like SREcon, meetups, and other publications, that we all have a lot to share with and learn from each other. To that end, we hope this book further expands that ongoing conversation.
On Gratitude
This volume has been a labor of love for us, and we are deeply grateful that you decided to read it. This process has taught each of us some surprising lessons about what SRE has become and made us all very excited to see what comes next.
(And since we are SREs, we’ll be starting a lengthy postmortem on this process. Who knows, maybe you’ll even see it in a blog post one of these days…)
May your queries flow and your pagers stay silent.
—Dave, Betsy, Niall, Stephen, and Kent
