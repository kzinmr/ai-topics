---
title: "I Finally Fixed My Locales In Arch Linux (Yes I Am Smart)"
url: "https://jayd.ml/2025/10/29/finally-figured-out-locales.html"
fetched_at: 2026-04-29T07:02:13.461414+00:00
source: "jayd.ml"
tags: [blog, raw]
---

# I Finally Fixed My Locales In Arch Linux (Yes I Am Smart)

Source: https://jayd.ml/2025/10/29/finally-figured-out-locales.html

For the past 8 months or so I’ve been using Arch my locales have been kind of
half broken and I couldn’t figure out why. I would see output like this:
$
locale
-a
locale: Cannot
set
LC_CTYPE to default locale: No such file or directory
locale: Cannot
set
LC_MESSAGES to default locale: No such file or directory
C
C.utf8
POSIX
en_US.utf8
$
locale
locale: Cannot
set
LC_CTYPE to default locale: No such file or directory
locale: Cannot
set
LC_MESSAGES to default locale: No such file or directory
locale: Cannot
set
LC_ALL to default locale: No such file or directory
LANG
=
en_us.UTF-8
LC_CTYPE
=
"en_us.UTF-8"
LC_NUMERIC
=
"en_us.UTF-8"
LC_TIME
=
"en_us.UTF-8"
LC_COLLATE
=
C.UTF-8
LC_MONETARY
=
"en_us.UTF-8"
LC_MESSAGES
=
"en_us.UTF-8"
LC_PAPER
=
"en_us.UTF-8"
LC_NAME
=
"en_us.UTF-8"
LC_ADDRESS
=
"en_us.UTF-8"
LC_TELEPHONE
=
"en_us.UTF-8"
LC_MEASUREMENT
=
"en_us.UTF-8"
LC_IDENTIFICATION
=
"en_us.UTF-8"
LC_ALL
=
All the time, even when I ssh-ed into something. I read
the Arch wiki
over and over, checked
/etc/locale.conf
:
LANG=en_US.UTF-8
LANGUAGE=en_US:en:C
LC_COLLATE=C.UTF-8
NOTE:
Eagle eyed viewers will notice that
en_us.UTF-8
from
locale
does 
not match
en_US.UTF-8
from
/etc/locale.conf
. Congratulations, you are more
observant than I am
Triple checked I’d uncommented the right things in
/etc/locale.gen
, and
locale-gen
over and over, to no avail.
The Big Clue
Finally after going over every forum and stackoverflow post I could find,
I found
this one
,
where someone suggests you
unset LANG
and
source /etc/profile.d/locale.sh
to
see if it works.
And it did after I changed that!
$
unset
LANG
$
source
/etc/profile.d/locale.sh
$
locale
-a
C
C.utf8
POSIX
en_US.utf8
So I had been barking up the wrong tree the whole time: my
/etc/locale.conf
apparently wasn’t the problem.
So what else could it be?
Well, it turns out KDE overrides your locale somehow, and it was stuck with some
misconfigured value (
en_us.UTF-8
vs
en_US.UTF-8
).
I went to Settings -> Region and Language -> Language -> Modify and “American
English” was listed twice, and there was some kind of error about “American English”
not being supported.
Artists Rendering of What The List Looked Like:
American English
American English
C
I deleted both American English entries because I figured one was bugged and 
re-added them. KDE told me to run
local-gen
again, so I did, and rebooted.
$
locale
-a
C
C.utf8
POSIX
en_US.utf8
$
locale
LANG
=
en_US.UTF-8
LC_CTYPE
=
"en_US.UTF-8"
LC_NUMERIC
=
en_US.UTF-8
LC_TIME
=
en_US.UTF-8
LC_COLLATE
=
C.UTF-8
LC_MONETARY
=
en_US.UTF-8
LC_MESSAGES
=
"en_US.UTF-8"
LC_PAPER
=
en_US.UTF-8
LC_NAME
=
en_US.UTF-8
LC_ADDRESS
=
en_US.UTF-8
LC_TELEPHONE
=
en_US.UTF-8
LC_MEASUREMENT
=
en_US.UTF-8
LC_IDENTIFICATION
=
"en_US.UTF-8"
LC_ALL
=
Huzzah, this basic thing finally works.
My theory is that I fat fingered
en_us
vs
en_US
(on two different computers!) 
in
/etc/locale.conf
when installing and fixed it later. KDE however must have
its own locale mechanism, and kept the bugged entry stored somewhere until I 
went and cleared it out. Oof.
