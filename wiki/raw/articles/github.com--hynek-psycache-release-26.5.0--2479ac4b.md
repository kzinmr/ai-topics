---
title: "Release 26.5.0 · hynek/psycache"
source_url: "https://github.com/hynek/psycache/releases/tag/26.5.0"
fetched: 2026-11-24
type: raw-article
---

Highlights
This release upgrades Sentry instrumentation to
sentry-sdk
3.0
. Don't upgrade if you're stuck with 2.x. The download numbers currently do not justify adding support for both version.
Full changelog below!
Special thanks
This release would not be possible without my generous sponsors! Thank you to all of you making sustainable maintenance possible! If
you
would like to join them, go to
https://github.com/sponsors/hynek
and check out the sweet perks!
Above and beyond
Variomedia AG
(@
variomedia
),
Tidelift
(@
tidelift
),
Kraken Tech
(@
kraken-tech
),
Klaviyo
(@
klaviyo
),
Privacy Solutions GmbH
(@
privacy-solutions
),
FilePreviews
(@
filepreviews
),
TestMu AI Open Source Office (Formerly LambdaTest)
(@
LambdaTest-Inc
),
Todoist Inc
(@
todoist
), Daniel Fortunov (@
asqui
), and Kevin P. Fleming (@
kpfleming
).
Maintenance sustainers
Buttondown
(@
buttondown
),
Christopher Dignam
(@
chdsbd
), Magnus Watn (@
magnuswatn
),
David Cramer
(@
dcramer
),
Rivo Laks
(@
rivol
),
Mike Fiedler
(@
miketheman
), Duncan Hill (@
cricalix
), Colin Marquardt (@
cmarqu
),
August Trapper Bigelow
(@
atbigelow
), Nick Libertini (@
libertininick
),
Brian M. Dennis
(@
crossjam
),
Al Sweigart
(@
asweigart
), Celebrity News AG (@
celebritynewsag
),
Sławomir Ehlert
(@
slafs
), Mostafa Khalil (@
khadrawy
),
Filip Mularczyk
(@
mukiblejlok
), Thomas Klinger (@
thmsklngr
),
Andreas Poehlmann
(@
ap--
),
Carlton Gibson
(@
carltongibson
), and
Roboflow
(@
roboflow
).
Full changelog
Changed
psycache.instrumentation.sentry.SentryInstrumentation
now requires
sentry-sdk
3.0 or later. The span data are now span attributes, and the operation is the
sentry.op
attribute.
#12
This release contains contributions from
@hynek
.