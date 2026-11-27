---
title: "Obvious Affordances Are Due for a Comeback"
url: "https://daringfireball.net/2026/11/obvious_affordances_are_due_for_a_comeback"
fetched_at: 2026-11-27T10:00:54.888966+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Obvious Affordances Are Due for a Comeback

Source: https://daringfireball.net/2026/11/obvious_affordances_are_due_for_a_comeback

Obvious Affordances Are Due for a Comeback
Thursday, 26 November 2026
Speaking of
Marcin Wichary, like me, he’s a big user of Apple Notes. Unlike me, he’s such a big user of Notes that he (somehow)
uses Notes as the CMS
for the whole Unsung blog.
In a post this week
, he wrote about how Notes — like file systems and most other notes apps — keeps two dates for each note: created and modified. You can sort your list of notes in Notes by either date; the default is by modification date, which Notes calls “edited”. Conveniently, Notes will remember your sorting preference on a per-folder basis. So if you have a folder of notes that you use as a journal, you can sort that folder by date created, without affecting the sort order for your other folders. (Notes only remembers each folder’s sort-by order per device, so if you use multiple devices, you’ll need to change the sort-by setting for a given folder on each device.)
In the editing view for a single note, however, Notes only shows one date, the modified/edited date, like so:
November 26, 2026 at 1:00 pm
Wichary writes
:
This can feel frustrating. You know the data is there, you see it
in the left pane, part of the software recognizes and supports it,
but there seems to be no way to summon it in a place you want. I
looked through the context (right click) menus, and through the
main menu. I couldn’t find anything, and I assumed that
possibility just wasn’t there.
Then recently, years on, I accidentally clicked on the timestamp,
and this happened:
[
Screen capture movie omitted.
]
That click was what I needed all along. Clicking alternates
between “created” and “edited” timestamps. It even puts a little
prefix not just before the other date, but before both.
Yet… there is really no way to know this functionality is there.
Clicking the timestamp to toggle between the edited and created dates is a cool hidden feature. But as Wichary notes, why is it hidden?
I don’t necessarily mean that Notes had to do something like what
Finder or Bear do, and expose that data all the time — that kind
of stuff can feel heavy. But I think it’s important to make sure
all actions have their entry points
somewhere
where you can
discover them. Maybe it’s the main menu, maybe it’s the
right-click menu. I’m a fan of
command palettes
in part
because that’s where more esoteric options can go without
overloading other surfaces.
On the Mac, there probably ought to be an item in the View menu for this. But that wouldn’t help on iOS, which has no menu bar. The basic problem is that the timestamp at the top of every note is clickable, but it doesn’t look clickable. If clicking on something does something, that thing should look clickable. Just what “looking clickable” means is open for debate, but ought to be part of the standard visual language for the platform. It could look like a raised button. It could look like a recessed well. You could keep it flat and just draw a faint button shape behind the text. You could design something exuberantly fun, like making it look and animate like a train station
split-flap display
. You could be lazy and just underline the text — underlining, although gross, would at least be
something
. Things that are inert should look inert; things that are clickable should look clickable.
1
This gets to the heart of the problem with Apple’s too-minimal UI language — and the rest of the industry mindlessly following Apple’s lead. There’s a wonderful rule of thumb
oft attributed to Albert Einstein
:
Everything should be made as simple as possible, but not simpler.
When clickable UI elements do not look clickable, they’ve been made too simple.
One More Thing
I long ago noticed, somehow, that the timestamps atop notes in Notes
2
are clickable, to toggle between edited and created dates. But Wichary’s post brought to my attention a detail that I consider a violation of good design. When you first display a note, the timestamp at the top looks like this:
November 26, 2026 at 1:00 pm
That’s the edited date (which I really want to call “modified”) — but it doesn’t say so. It just shows the date. When you click it, it changes to:
Created: October 31, 2026 at 4:30 pm
Click again and you get:
Edited: November 26, 2026 at 1:00 pm
If you continue clicking, it keeps toggling between the timestamps with the “Created:” and “Edited:” prefix labels. The design violation I’m flagging is that the initial state doesn’t have a label,
and there’s no way to get back to the initial unlabeled timestamp
. If repeatedly clicking something cycles through multiple states, you should wind up exactly where you started. With these timestamps in Notes, the only way to get back to where you started — a timestamp with no label — is to close the note and reopen it. That’s clearly wrong.
This is a foul, not a bug. It’s a deliberate design decision. And I think we can presume how Apple arrived at this design. The solution I’d like to see is for the date to always be labeled — “Edited:” or “Created:”. Then clicking would just toggle between the two states. With two clicks, you’d be right back where you started. I think always showing these labels would also offer a gentle hint that you can click to change which date is shown. That’s not enough to fully suggest clickability, but it’d be better than nothing, which is what we have now. I’m guessing that the “simpler than possible” minimalist cohort at Apple complained that showing the “Edited:” label from the start is ugly clutter. So, we wound up with this unsatisfying compromise: no label at the start, but toggling between “Created:” and “Edited:”
after
you click on the timestamp.
Needless clutter ought to be omitted. Some elements are reasonably made optional. But when an item in an app has two timestamps associated with it, labeling which date is which isn’t clutter. Clarity is good. Eliminating ambiguity is good. Liking the way something looks should never come at the expense of conveying an understanding of how it works, or making it harder to use. If you’re not excited by the challenge of designing a presentation for the Notes timestamp that both looks good
and
suggests that it’s a clickable toggle, you are not a UI designer. You’re a graphic designer.
Dan Wineman wrote a good post on visual affordances
back in 2013, just days after Apple unveiled iOS 7’s great flattening, which I’ll
quote from again
:
That’s what affordances do. They operate on the boundary between
sight and touch. You see a thing, often from a distance, and its
affordances give you enough information to simulate, in your mind,
the sensation of manipulating it. Unconsciously, you configure
your fine motor system in advance, so that by the time you get to
the door handle, your hand is already forming the right shape to
grasp it and pull the door open. [...]
Affordances are the baby to skeuomorphism’s bathwater. When they
engage our instincts just right, they create an emotional bond,
and the unfamiliar becomes inviting. Without them, it’s just
pictures under glass. It makes no difference how flat, how deep,
how minimal, or how ornate the look-and-feel is if it can’t show
us, when we look, how to feel.
This is the way back to the future. We don’t need to invent these designs. We just need to embrace again what we already know.
