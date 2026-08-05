---
title: "OpenAI Responds to Apple’s Lawsuit and Motion for Preliminary Injunction: ‘Apple Is Getting This Wrong’"
url: "https://daringfireball.net/2026/08/openai_apple_is_getting_this_wrong"
fetched_at: 2026-08-05T10:12:32.578368+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# OpenAI Responds to Apple’s Lawsuit and Motion for Preliminary Injunction: ‘Apple Is Getting This Wrong’

Source: https://daringfireball.net/2026/08/openai_apple_is_getting_this_wrong

OpenAI Responds to Apple’s Lawsuit and Motion for Preliminary Injunction: ‘Apple Is Getting This Wrong’
Tuesday, 4 August 2026
OpenAI published an unbylined blog post
overnight, responding in public — but not yet in court — to Apple’s new motion for a preliminary injunction. It’s an unusual move to respond to a high-stakes legal filing with a blog post, but OpenAI is an unusual company. A few snippets from their post, and some commentary:
Apple had claimed that they contacted OpenAI in February and that
we didn’t respond. They now admit that their outside lawyers
emailed the wrong person after confusing two Asian last names — only after we brought this to their attention.
OpenAI is
hanging on
to the fact that Apple’s outside counsel, Gabriel Gross, sent one email to the wrong address, and quickly emailed an apology. In OpenAI’s phrasing, it sounds like Apple’s attorney sent the entire initial letter of concern to the wrong person, and that’s why OpenAI never responded — because it wasn’t sent to the correct person (OpenAI general counsel Che Chang). That’s not what happened. The initial blockbuster “hey we think you guys are stealing our trade secrets and we want to talk to you about it” letter
was
sent to Che Chang. And Che Chang never did respond to Apple’s lawyers. That a mistaken email thanking Che Chang for a phone call that never happened (because that email was intended for another OpenAI employee) was also sent is irrelevant. I don’t understand why OpenAI is continuing to focus on this inconsequential mistake. (
Apple’s motion
for a preliminary injunction includes the full text of the mistaken email and subsequent apology.)
Apple accuses Chang Liu of accessing Apple confidential
information after leaving the company, but only now admits that
Apple employees reached out to him and asked for his help to
locate this information (you can read the messages
here
).
Apple now tries to shift the blame to “residual access”, but they
also don’t disclose that this is a common issue with Apple which
is caused by them failing to properly manage system access when
people leave. What that means in practice is that former employees
who are trying to do the right thing when they leave still have
access to Apple files — despite not wanting them or even being
aware of them.
OpenAI is seemingly alluding to Apple’s unusual use of iCloud Drive, tied to employees’ personal Apple Account IDs,
that I (coincidentally?) wrote about yesterday
. Apple’s motion for injunction, however, addresses this very point. From page 3 of the motion:
Mr. Liu resigned on Thursday, January 22, 2026, and provided
notice that he would start at OpenAI the following Tuesday. On his
last day, he failed to respond to Apple’s attempt to schedule his
exit interview or sign his confidentiality reminder.
In the days following his departure, Mr. Liu seemed initially
cooperative and aware of his obligations to Apple. He worked with
others on his former Apple team to return certain Apple
information remaining on his personal iCloud account to
Apple.
1
He also continued to converse with former
co-workers, for example, to answer questions about his earlier
work and where certain information was stored. But these
interactions and exchanges cannot explain the repeated,
unauthorized downloading of voluminous technical files from
Apple’s cloud-based storage discussed below, which Mr. Liu
performed on multiple occasions from February to April 2026 while
employed by OpenAI.
That footnote reads:
1
While Apple seeks discovery into what Apple
confidential information Mr. Liu accessed from his personal
storage accounts (including iCloud) and devices after his
departure, the specific unauthorized downloads referenced in the
complaint and at the heart of this motion are not based on iCloud
activity, but instead relate to Apple’s third-party cloud storage.
Nowhere in any of Apple’s filings (
here’s the Court Listener index page
for all the documents filed in the cast) does it say who the third-party cloud storage provider is, but I’m almost certain it’s Box, which I know is widely used throughout Apple.
The iMessage transcripts that OpenAI provides at the bottom of their post do not contradict Apple’s claims at all. Apple’s motion states that Liu helped former colleagues find certain documents that were in iCloud; that’s what OpenAI’s transcript shows. But that’s not in dispute. Apple also claims that Liu accessed confidential information, presumably in Box and definitely not in iCloud Drive, on five different occasions, up until 27 April 2026, over three months after he left Apple. These chat transcripts offer no explanation for that. The chat transcripts explain iCloud Drive access that Apple itself says is not in dispute, and do not explain the 37 documents Liu downloaded from the third-party cloud provider (Box?) that Apple says are at the heart of naming him in the lawsuit.
Here is Apple’s declaration from digital forensic specialist Daniel Roffman
, documenting Liu’s access to confidential files post-employment (albeit with significant redactions).
I do not understand why OpenAI is treating this is a PR problem instead of as a legal problem. Dan Moren,
linking to it from Six Colors
, is of similar mind, writing:
What kept running through my head while reading this was the old
legal chestnut: “If you have the facts on your side, pound the
facts. If you have the law on your side, pound the law. If you
have neither on your side, pound the table.”
Thus far this feels like table-pounding from OpenAI to me. Their blog post does, however, move the ball from “
we have no interest
” in Apple’s trade secrets to “we don’t have them”, (emphasis added):
Apple also accuses Tang Tan of trying to get and use their trade
secrets. However, Tang has always been clear with the team that
we do not want, and must not use, any confidential information
from other companies. Tang served Apple for more than 24 years
and was widely known as one of the most innovative leaders at the
company. [...]
Apple’s request for a preliminary injunction is both based on
false information and completely unnecessary
because we do not
have, nor want, any of their trade secrets
. We’re much more
interested in building innovative products and technologies that
push the frontier.
To me, the most interesting response from OpenAI wasn’t their blog post, and was in fact released by Apple, as “
Exhibit F
” to one of their expert declarations submitted to the court last night. OpenAI has retained the Chicago law firm Quinn Emanuel as outside counsel, and this exhibit is a long email from Quinn Emanuel attorney Patrick Curran to Apple’s attorneys. From that email, dated Monday July 20, Curran writes:
You also ask that we “revisit” the specific points proposed in
your July 15 letter. It appears that you want to move backwards.
As noted, we already discussed these during our meet and confer
but Apple was unable to respond to basic questions my colleagues
raised about these requests. For example, your letter proposes
that OpenAI “[p]roduce witnesses to testify at deposition” but
Apple was unable to identify who those witnesses would be.
Similarly, Apple was unsure when we asked if it was actually
proposing that hundreds of OpenAI employees fill out
“questionnaires” even if Apple has no basis to allege (and is
indeed not alleging) that such employees have any connection to
this litigation. The seven sections in your letter are broadly
worded and remain vague and general. This is not what a forensic
protocol looks like and we’re sure you understand that you will
not get this as relief from the court. You first need to
(preliminarily) identify the TS you are suing for, and your email
states that you “appreciate the need” to do so. Any protocol will
be informed by such identification. A forensic protocol cannot be
based on general terms like “Apple confidential information”; you
need to tell us what you’re looking for, and it sounds like you
understand that and are prepared to do so. The efficient way
forward is therefore to tackle these issues as part of the
negotiation of a proper, detailed forensic protocol. If you
instead prefer to move for a PI because OpenAI did not agree off
the bat to subject hundreds of employees to “questionnaires” about
“Apple confidential information” generally, that is unfortunate — and inconsistent with what I understand both our clients have
requested. If you choose this path instead of working with us, we
look forward to filing an opposition that sets the record
straight.
Apple, obviously, did choose this path (“PI” = preliminary injunction), and I too look forward to OpenAI’s setting the record straight, especially if they do so in plainspoken language like Curran’s in this email. Curran continues:
Finally, although I know OpenAI would like to resolve this
amicably, as their counsel I have to tell you what I think you
already know — this case lacks merit. You have not articulated
any basis to support a preliminary injunction. Your complaint is
predicated on a misrepresentation of facts and allegations that
are speculative at best. It fails to even remotely identify any
trade secrets. You are attacking ordinary business practices (used
widely across the industry). You are complaining about situations
that you have caused, including through your own procedures and
decisions. We stand ready to oppose any preliminary injunction
motion and tell the world what really happened here to set the
record straight. We made clear we would prefer to quickly and
collaboratively address any legitimate concerns that your client
has, but that is not well-served by repeated threats.
This email is a far better response than what OpenAI published on their blog.
