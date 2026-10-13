---
title: Google SRE Handbook - Enacting the Principles of SRE
source_url: https://sre.google/workbook/preface/
license: CC-BY-NC-ND-4.0
license_url: https://creativecommons.org/licenses/by-nc-nd/4.0/
attribution: Google, Inc.; editors Betsy Beyer, Niall Richard Murphy, David K. Rensin,
  Kent Kawahara, Stephen Thorne; O’Reilly, 2018
reuse_scope: Unmodified originals; noncommercial archive. Text is a technical format
  conversion; no translation or content edits.
publication_year: 2018
original_html: original-source.zip!/preface.html
original_sha256: e66400665990654f5d596042b342d66801225cf10abe49f500eee56693aa54a8
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://sre.google/workbook/preface/
ingested: '2026-10-14'
sha256: 46b1859c29a1f115ce8d104c932c2246c62ccbb3d3af767556ee4562ba72f449
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
Preface
When we wrote the original
Site Reliability Engineering
book
, we had a goal: explain the philosophy and the principles of production engineering and operations at Google. The book was our attempt to share our teams’ best practices and lessons with the rest of the computing world. We assumed that the SRE book might appeal to a modest number of engineers working in large, reliability-conscious endeavors, and that both the quantity and the focus of the content would tend to limit the book’s appeal.
As it turned out, we were happily mistaken on both counts.
To our surprise and delight, the SRE book was a best-seller in computing for an exhilarating period after its release, and it was not just being sold or downloaded; it was being
read
. We received questions from around the world about the book, the team, the practices, and the outcomes. We were asked to speak about chapters, approaches, and incidents. We found ourselves in the unexpected position of having to turn down outside requests because we were out of cycles.
Like most success disasters, the SRE book created an opportunity to respond with human effort (“Hire more people! Do more speaking engagements!”) or with something more scalable. And being SREs, it will surprise few readers that we gravitated toward the latter approach. We decided to write a second SRE book—one that expanded on the content we were most frequently being asked to speak about, and that addressed the most common questions readers had about the first book.
Out of the many different questions, requests, and comments we received about the first SRE book, two themes were particularly interesting to us; if left unaddressed, they were barriers to putting SRE’s lessons to productive use. These themes are colloquially summarized as:
Principles are interesting, but how do I turn them into practice in
my
project/team/company?
SRE’s approach would not work for me; it is feasible only in Google’s culture, and makes sense only at Google’s scale.
The purpose of this second SRE book is (a) to add more implementation detail to the principles outlined in the first volume, and (b) to dispel the idea that SRE is implementable only at “Google scale” or in “Google culture.”
This volume is a
companion
to the previous work—not a new version. The two books should be taken together as a pair. You will get the most from this book if you’re already familiar with its predecessor. The first SRE book is available
online for free
.
By design, the structure of this book roughly follows the structure of the first volume. We want you to be able to read the chapters in tandem. Each chapter in this volume assumes you’re familiar with its counterpart from the previous work; our goal is to allow you to jump back and forth between principle and practice as you go. That way, you can use both volumes as ongoing references.
Next, a word about ethos: We heard from some readers that while describing Google’s journey toward better operations we concentrated too much on
just us
. Some readers suggested that we were too removed from the practicalities of the world outside Google, and failed to address
the interaction of our ideas
with the principles of DevOps. That’s an entirely fair criticism that we’ve tried to take to heart in this volume.
However, we do think that the highly opinionated nature of SRE contributes to its usefulness as a discipline. To us that’s a feature, not a bug. We do not advocate that SRE is the only way (or even universally the best way) to build and operate highly reliable systems. It’s just the way that has been most successful for us.
We’ll also spend a few words talking about how SRE and DevOps relate to each other. The important point to keep in mind is that they are not in conflict.
We’d like to acknowledge up front that this volume is necessarily incomplete. The SRE discipline is a broad field even inside the confines of Google, and it is evolving even faster now that it’s practiced widely outside of Google. Rather than go broad and superficial, we focused this volume to answer the most requested implementation details from the first volume.
Finally, this volume and its predecessor are not intended to be gospel. Please don’t treat them that way. Even after all these years, we’re still finding conditions and cases that cause us to tweak (or in some cases, replace) previously firmly held beliefs. SRE is a journey as much as it is a discipline.
We hope that you enjoy what you read in these pages and find the book useful. Assembling it has been a labor of love. We’re delighted that there’s a growing and skilled community of SRE professionals with whom we can learn and improve.
As always, your direct feedback is much appreciated. It teaches us something valuable every time you contribute it.
How to Read This Book
This book is the companion volume to Google’s first book,
Site Reliability Engineering
. To get the most out of this volume, we recommend that you have read, or can refer to, the first SRE book (available to read online for free at
https://sre.google
).The two works complement each other in the following ways:
The previous work was an introduction to principles and philosophy. This volume concentrates on how those principles are applied. (In a few areas—particularly configuration management and canarying—we also cover some new ground to provide background for the practical treatment of other subjects.)
The earlier volume concentrated exclusively on how SRE is practiced at Google. This work includes perspectives from a number of other firms—from traditional enterprises (including The Home Depot and the
New York Times
) to digital natives (Evernote, Spotify, and others).
The first book didn’t directly refer to the larger operations community—especially DevOps—whereas this book speaks directly to how SRE and DevOps relate to each other.
This volume assumes that you will bounce between this volume and its predecessor. You might, for example, read
Chapter 4, “Service Level Objectives”
in the first book and then read its implementation complement (
Implementing SLOs
) in this volume.
This book assumes that every chapter is just the starting point for a longer discussion and journey. Accordingly, this book is intended to be a conversation starter rather than the last word.
—The Editors
Conventions Used in This Book
The following typographical conventions are used in this book:
Italic
Indicates new terms, URLs, email addresses, filenames, and file extensions.
Constant width
Used for program listings, as well as within paragraphs to refer to program elements such as variable or function names, databases, data types, environment variables, statements, and keywords.
Constant width bold
Shows commands or other text that should be typed literally by the user.
Constant width italic
Shows text that should be replaced with user-supplied values or by values determined by context.
Tip
This element signifies a tip or suggestion.
Note
This element signifies a general note.
Warning
This element indicates a warning or caution.
Using Code Examples
Supplemental material (code examples, exercises, etc.) is available for download at
https://g.co/SiteReliabilityWorkbookMaterials
.
This book is here to help you get your job done. In general, if example code is offered with this book, you may use it in your programs and documentation. You do not need to contact us for permission unless you’re reproducing a significant portion of the code. For example, writing a program that uses several chunks of code from this book does not require permission. Selling or distributing a CD-ROM of examples from O’Reilly books does require permission. Answering a question by citing this book and quoting example code does not require permission. Incorporating a significant amount of example code from this book into your product’s documentation does require permission.
We appreciate, but do not require, attribution. An attribution usually includes the title, author, publisher, and ISBN. For example: “
The Site Reliability Workbook
, edited by Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, and Stephen Thorne (O’Reilly). Copyright 2018 Google LLC, 978-1-492-02950-2.”
If you feel your use of code examples falls outside fair use or the permission given above, feel free to contact us at
permissions@oreilly.com
.
O'Reilly Safari
Note
Safari
(formerly Safari Books Online) is a membership-based training and reference platform for enterprise, government, educators, and individuals.
Members have access to thousands of books, training videos, Learning Paths, interactive tutorials, and curated playlists from over 250 publishers, including O’Reilly Media, Harvard Business Review, Prentice Hall Professional, Addison-Wesley Professional, Microsoft Press, Sams, Que, Peachpit Press, Adobe, Focal Press, Cisco Press, John Wiley & Sons, Syngress, Morgan Kaufmann, IBM Redbooks, Packt, Adobe Press, FT Press, Apress, Manning, New Riders, McGraw-Hill, Jones & Bartlett, and Course Technology, among others.
For more information, please visit
https://oreilly.com/safari
.
How to Contact Us
Please address comments and questions concerning this book to the publisher:
O’Reilly Media, Inc.
1005 Gravenstein Highway North
Sebastopol, CA 95472
800-998-9938 (in the United States or Canada)
707-829-0515 (international or local)
707-829-0104 (fax)
We have a web page for this book, where we list errata, examples, and any additional information. You can access this page at
https://bit.ly/siteReliabilityWkbk
.
To comment or ask technical questions about this book, send email to
bookquestions@oreilly.com
For more information about our books, courses, conferences, and news, see our website at
https://www.oreilly.com
.
Find us on Facebook:
https://facebook.com/oreilly
Follow us on Twitter:
https://twitter.com/oreillymedia
Watch us on YouTube:
https://www.youtube.com/oreillymedia
Acknowledgments
This book is the product of the enthusiastic and generous contributions of more than 100 people, including authors, tech writers, and reviewers. Each chapter has a byline for the individual authors and tech writers. We’d also like to take a moment to thank everyone not listed there.
We would like to thank the following reviewers for providing valuable (and sometimes pointed) feedback: Abe Hassan, Alex Perry, Cara Donnelly, Chris Jones, Cody Smith, Dermot Duffy, Jarrod Todd, Jay Judkowitz, John T. Reese, Liz Fong-Jones, Mike Danese, Murali Suriar, Narayan Desai, Niccolò Cascarano, Ralph Pearson, Salim Virji, Todd Underwood, Vivek Rau, and Zoltan Egyed.
We would like to express our deepest appreciation to the following people for serving as our overall quality bar for this volume. They made substantial contributions throughout the entire volume: Alex Matey, Max Luebbe, Matt Brown, and JC van Winkel.
As the leaders of Google SRE, Benjamin Treynor Sloss and Ben Lutch were this book’s primary executive sponsors within Google; their strong and unwavering belief in a follow-up project that was a worthy companion of the first SRE book was essential to making this book happen.
While the authors and technical writers are specifically acknowledged in each chapter, we’d like to recognize those that contributed to each chapter by providing thoughtful input, discussion, and review. In chapter order, they are:
Implementing SLOs:
Javier Kohen, Patrick Eaton, Richard Bondi, Yaniv Aknin
Monitoring:
Alex Matey, Clint Pauline, Cody Smith, JC van Winkel, Ola Kłapcińska, Štěpán Davidovič
Alerting on SLOs:
Alex Matey, Clint Pauline, Cody Smith, Iain Cooke, JC van Winkel, Štěpán Davidovič
Eliminating Toil:
Dermot Duffy, James O'Keeffe, Stephen Thorne
Simplicity:
Mark Brody
On-Call:
Alex Perry, Alex Hidalgo, David Huska, Sebastian Kirsch, Sabrina Farmer, Steven Carstensen, Liz Fong-Jones,
  Nandu Shah (Evernote), Robert Holley (Evernote)
Incident Response:
Alex Hidalgo, Alex Matey, Alex Perry, Dave Rensin, Matt Brown, Tor Gunnar Houeland, Trevor
  Strohman
Postmortem Culture:
Learning from Failure: John T. Reese
Managing Load:
Daniel E. Eisenbud, Dave Rensin, Dmitry Nefedkin, Dževad Trumić, Edward Wu (Niantic), JC van Winkel, Lucas Pereira, Luke Stone, Matt Brown, Natalia Sakowska, Niall Richard Murphy, Phil Keslin (Niantic), Rita Sodt, Scott Devoid, Simon Donovan, Tomasz Kulczyński
Introducing Non-Abstract Large System Design:
Ivo Krka, Matt Brown, Nicky Nicolosi, Tanya Reilly
Data Processing Pipelines:
Bartosz Janota (Spotify), Cara Donnelly, Chris Farrar, Johannes Rußek (Spotify), Max Charas, Max Luebbe, Michelle Duffy, Nelson Arapé (Spotify), Riccardo Petrocco (Spotify), Rickard Zwahlen (Spotify), Robert Stephenson (Spotify), Steven Thurgood
Configuration Design and Best Practices:
Charlene Perez, Dave Cunningham, Dave Rensin, JC van Winkel, John Reese, Stephen Thorne
Configuration Specifics:
Alex Matey, Bo Shi, Charlene Perez, Dave Rensin, Eric Johnson, Juliette Benton, Lars Wander, Mike Danese, Narayan Desai, Niall Richard Murphy, Štěpán Davidovič, Stephen Thorne
Canarying Releases:
Alex Matey, Liz Fong-Jones, Max Luebbe
Identifying and Recovering from Overload:
Andrew Harvey, Aleksander Szymanek, Brad Kratochvil, Ed Wehrwein, Duncan Sargeant, Jessika Reissland, Matt Brown, Piotr Sieklucki and Thomas Adamcik
SRE Engagement Model:
Brian Balser (
New York Times
), Deep Kapadia (
New York Times
), Michelle Duffy, Xavier Llorà
SRE: Reaching Beyond Your Walls:
Matt Brown
SRE Team Lifecycles:
Brian Balser (
New York Times
), Christophe Kalt, Daniel Rogers, Max Luebbe, Niall Richard Murphy, Ramón Medrano Llamas, Richard Bondi, Steven Carstensen, Stephen Thorne, Steven Thurgood, Thomas Wright
Organizational Change Management in SRE:
Dave Rensin, JC Van Winkel, Max Luebbe, Ronen Louvton, Stephen Thorne, Tom Feiner, Tsiki Rosenman
We are also grateful to the following contributors, who supplied significant expertise or resources, or had some otherwise excellent effect on this work: Caleb Donaldson, Charlene Perez, Evan Leonard, Jennifer Petoff, Juliette Benton, and Lea Miller.
We very much appreciate the thoughtful and in-depth feedback that we received from industry reviewers: Mark Burgess, David Blank-Edelman, John Looney, Jennifer Davis, Björn Rabenstein, Susan Fowler, Thomas A. Limoncelli, James Meickle, Theo Schlossangle, Jez Humble, Alice Goldfuss, Arup Chakrabarti, John Allspaw, Angus Lees, Eric Liang, Brendan Gregg, and Bryan Liles.
We would like to extend a special thanks to Shylaja Nukala, who generously committed the time and skills of the SRE Technical Writing Team. She enthusiastically supported their necessary and valued efforts.
Thanks also to the O’Reilly Media team—Virginia Wilson, Kristen Brown, Rachel Monaghan, Nikki McDonald, Melanie Yarbrough, and Gloria Lukos—for their help and support making the book a reality in our ambitious timeline.
And an
extra
special thanks to Niall Richard Murphy: despite the fact that he moved on from Google before this book hit the shelves, his continual insights and dedication were crucial for getting a goodly portion of meaningful content over the finish line. His leadership, thoughtfulness, tenacity, and wit are nothing short of inspirational!
Finally, the editors would also like to personally thank the following people:
Betsy Beyer:
To Grandmother, my go-to source for encouragement, inspiration, popcorn, pep, and puzzling. You made both this book and my everyday life better! To Duzzie, Hammer, Joan, Kiki, and Mini (note the alphabetical order—ha!) who helped shape me into the obsessive writer slash person I am today. And of course, Riba, for providing the DMD and other provisions necessary to fuel this effort.
Niall Richard Murphy:
To Léan, Oisín, Fiachra, and Kay, north stars. To someone whose protestations of self-interest are entirely out of odds with how he acts. To Sharon, more influential than she knows. To Alex, in a light-filled sitting room, with a cup of tea, a book, a box of dice, and thou.
Stephen Thorne:
To my mum and dad, who have always encouraged me to push myself. To my wife, Elspeth. To my colleagues who have given me more respect and encouragement than I think I deserve: Ola, Štěpán, Perry, and David.
Dave Rensin:
After I wrote my first book, I swore I’d never write another. That was six books ago and I say exactly the same thing each time. To my wife, Lia, who gives me the space to do it and never says “I told you so.” (Even though she tells me so.) To my colleagues at Google—and particularly to the family of SRE—who have taught me more these last few years about production engineering at scale than I had learned in the previous 20. Finally, to Benjamin Treynor Sloss, who interviewed me and convinced me to come to Google in the first place.
Kent Kawahara:
To my parents, Denby and Setsuko, and my Aunt Asako for helping me get to where I am. To my siblings, Randy and Patti, for their support over the years. To my wife, Angela, and my sons, Ryan, Ethan, and Brady, for their love and support. Finally, to the core team of Dave, Betsy, Niall, Juliette, and Stephen, I feel honored to have worked with you on this project.
