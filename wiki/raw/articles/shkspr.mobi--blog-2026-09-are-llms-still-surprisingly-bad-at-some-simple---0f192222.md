---
title: "Are LLMs still surprisingly bad at some simple tasks?"
url: "https://shkspr.mobi/blog/2026/09/are-llms-still-surprisingly-bad-at-some-simple-tasks/"
fetched_at: 2026-09-23T10:01:08.784953+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Are LLMs still surprisingly bad at some simple tasks?

Source: https://shkspr.mobi/blog/2026/09/are-llms-still-surprisingly-bad-at-some-simple-tasks/

Last year I ran
an experiment to test the ability of modern LLMs
to correctly answer a relatively straightforward question. Every single one of them got it wrong. Some missed information, some made up false statements, none were right.
Of course the fanbois variously claimed that I was holding it wrong, my prompts were shit, I should have chosen better defaults, and - my favourite - that it would be better next year.
Well, next year is now. 365 days after the original experiment, let's see if these self-reinforcing-learning machines have achieved anything close to intern-levels of competence.
I asked:
Which TLDs have the same name as valid HTML5 elements?
This is the sort of question that I would expect a moderately bright teenager to answer. There exists a list which comprehensively includes all TLDs. There is a separate list which contains every HTML element.
One could either manually go through the TLD list comparing it to the HTML list, or write a tiny scrap of code to do the same.
This isn't "solve Navier-Stokes" levels of superintelligence. It's a simple but boring task which people are bound to offload onto their digital sycophants.
How many LLM generated answers have become load-bearing without scrutiny?
People are lazy, slapdash, and some third thing to make the rule-of-three. If an answer looks answer-shaped, they'll accept it. On a simple but boring task, no reasonable human is going to suspect that a superintelligent computer has made a mistake. All the marketing says that these machines are brainier than you - so why bother?
So how did the current crop do? First up
Google Gemini
.
The default "Flash" model came up with this:
Valid top-level domains (TLDs) registered in the IANA Root Zone Database share exact names with standard HTML elements:
.a —
<a>
(Anchor/Hyperlink)
.app —
<app>
(Deprecated HTML tag for WebAPKs/WebApps)
.art —
<art>
(Historical/non-standard HTML element)
.audio —
<audio>
.bar —
<bar>
(Historical SVG/HTML draft tag)
Then it listed a dozen more. You don't need to be a DNS expert to know that the minimum length of a TLD is two characters -
.a
simply isn't valid. HTML nerds will know that art, app, and bar have never been elements. Pathetic.
So I tried Gemini's extended thinking model. Thankfully, it didn't make up any imaginary TLDs or elements. It did, however, miss the
<data>
element which has a valid
.data
TLD. It also missed
map
,
select
, and
search
.
So, points for not making shit up. But demerits for not being able to compare two text lists.
A friend
asked Claude
. That missed
search
and
select
. It didn't report
any
ccTLDs. You
could
argue that a country code like
li
isn't part of the original question - but I'd say that was weak justification; the set of TLDs contains ccTLDs.
A different friend (I have many!) used
a different model
and, while the answers looked accurate, it included this at the end:
Near misses that don't count: .codes, .forum, .pictures, .market, .navy, .press, .dell, .baseball.
I get that there's a
<code>
and
.codes
, similarly
<picture>
and
.picture
- but what are forum, baseball, and the others doing there? This is just unnecessary verbiage designed to trick the user into thinking the task has been well-researched.
If you want a laugh,
take a look at Perplexity
which found 54 matches - most of which were wrong.
Finally, someone asked "GPT Astra 6 Extra High" (which is a bonkers bad name for any product). It seemed to get all the elements - and made a note that
two were actually obsolete
.
So that's a range of modern models which are either very wrong, slightly wrong, included spurious and incoherent information, or were right.
How do you know which one to choose? How confident are you that the non-determinist computer will always produce the correct answer?
Another AI which got all the correct answers, didn't make anything up, didn't add extraneous information, and didn't use weasel words was…
Siri!
FUCKING SIRI?!?!
How did a glorified Speak 'n' Spell beat all the other AIs?
Oh. It just copied the answers off
a random idiot's website
.
Note carefully the question.
Which TLDs have the same name as valid HTML5 elements?
There's a —secret— and —some would say— unintuitive type of element. Behold the mighty power of
The Custom Element
.
Website authors can create their own elements like
<my-custom-element>
in order to extend the functionality of their site. But you can't go and create any old custom element. You can't have
<mobi>
or
<uk>
. No, there are
rules for validity
.
The rules
say that custom elements must start with a lower-case letter, it must not contain any upper-case letters, and it must contain a dash.
And that's the whole game.
There are over
one hundred and fifty
Top Level Domains which match that criteria!
The Hindi top level domain of
.कॉम
is represented in Punycode as
xn--11b4c3d
. It has been present in the list of TLDs
for over a decade
.
Paste this in to your console:
Copied JavaScript to 📋
⧉
JavaScript
class
Example
extends
HTMLElement {
constructor
() {
super
();
  }
}

customElements.
define
(
'xn--vermgensberatung-pwb'
, Example);
Try it again with a custom element like
holiday
(which is also a valid TLD) and it will fail with the error "'holiday' is not a valid custom element name". Thus it is demonstrated, Punycode TLDs
are
valid HTML5 elements.
Perhaps you think that including custom HTML elements is a cheat. A trick question set by a bitter old man to tarnish the holy name of our new machine gods?
Verily, I submit to you one final heresy.
HTML specifically allows
MathML elements
in its documents.
That means we can include the following valid elements which are
also
TLDs:
mn
,
mo
,
ms
, and
mtr
!
Amusingly, if you go back and
look at the Perplexity answer
, after it barfed up a bunch of misinformation, it said:
The HTML specification also includes names from embedded vocabularies—
<math>
from MathML and
<svg>
from SVG—but
.math
and
.svg
are not currently delegated TLDs in the public DNS root.
So close and yet so far!
If you think the original question was unfair, try asking "
Which TLDs have the same name as elements which are valid in an HTML document?
" and see if you get better results.
What precise wording would you use to ensure that a model would get the right answers? What assumptions are you making about how well you understand the problem? At what point do end up writing a thousand-word formal specification?
Let's delve in to the problems.
Most people don't change defaults. Telling people "you have to fiddle with the settings" just means the normal experience is rubbish.
Humans are lazy and won't check outputs. But, crucially, they shouldn't have to! If something markets itself as a genius, why should a human have to hold its hand?
Sycophantic models make themselves seem less fallible by giving extraneous detail in order to misdirect overworked readers. That is despicable.
The fast models are no better than they were a year ago. There's no evidence of "trickle-down intelligence".
Some models
are
better than others! But unless you constantly validate their output, you'll have no real way of knowing which ones are capable of working at a suitable level.
Look, I don't claim this question is as useful or entertaining as
Simon Wilson's "generate an SVG of a pelican riding a bicycle"
. But I do think it is an example of the sort of real-world use-case where LLMs regularly fail.
If I give a list of one thousand different numbers to Excel, I can be sure it'll add them up correctly. If I tell Photoshop to select all red pixels, I can be sure it won't imagine some of the blues are really red.
That's people's mental model of computers - they do boring tasks quickly and accurately.
In my opinion, LLMs are
still
surprisingly bad - but only if you know what you're looking for and if you can be bothered to check their outputs.
(And, yes, I am
still
just so bored of AI
!)
