---
title: "Oodle 2.8.9 with Oodle Texture speed fix and UE4 integration"
url: "http://cbloomrants.blogspot.com/2020/07/oodle-289-with-oodle-texture-speed-fix.html"
fetched_at: 2026-05-05T07:01:48.821928+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Oodle 2.8.9 with Oodle Texture speed fix and UE4 integration

Source: http://cbloomrants.blogspot.com/2020/07/oodle-289-with-oodle-texture-speed-fix.html

Oodle 2.8.9 is now shipping, with the aforementioned speed fix for large textures.
Oodle Texture RDO is always going to be slower than non-RDO encoding, it simply has to do a lot more work.
It has to search many possible encodings of the block to BCN, and then it has to evaluate those possible
encodings for both R & D, and it has to use more sophisicated D functions, and it has to search for possible
good encodings in a non-convex search space.  It simply has to be something like 5X slower than non-RDO
encoding.  But previously we just had a perf bug where working set got larger than cache sized that caused
a performance cliff, and that shouldn't happen.  If you do find any performance anomalies, such as encoding
on a specific texture or with specific options causes much slower performance, please contact RAD.
timerun 287 vs 289

hero_xxx_n.png ; 4096 x 4096
timerun textest bcn bc7 r:\hero_xxx_n.png r:\out.dds -r40 --w32
got opt: rdo_lagrange_parameter=40

Oodle 2.8.7 :

encode time: ~ 8.9 s
per-pixel rmse (bc7): 0.8238
---------------------------------------------
timerun: 10.881 seconds

Oodle 2.8.9 :

encode time: 4.948s
per-pixel rmse (bc7): 0.8229
---------------------------------------------
timerun: 6.818 seconds
the "timerun" time includes all loading and saving and startup, which appears to be about 1.9s ; the RDO encode
time has gone from about 8.9s to 4.95 s
(Oodle 2.8.7 textest bcn didn't log encode time so that's estimated; the default number of worker threads has changed,
so use --w32 to make it equal for both runs)
We are now shipping a UE4 integration for Oodle Texture!
The Oodle Texture integration is currently only for Oodle Texture RDO/non-RDO BCN encoders (not BC7Prep).
It should be pretty simple, once you integrate it your Editor will just do Oodle Texture encodes.  The
texture previews in the Editor let you see how the encodings look, and that's what you pack in the game.
It uses the Unreal Derived Data Cache to avoid regenerating the encodings.
We expose our "lambda" parameter via the "LossyCompressionAmount" field which is already in the Editor GUI
per texture.  Our engine patches further make it so that LossyCompressionAmount inherits from LODGroup,
and if not set there, it inherits from a global default.  So you can set lambda at :
per texture LossyCompressionAmount

if Default then look at :

LODGroup LossyCompressionAmount

if Default then look at :

global lambda
We believe that best practice is to avoid having artists tweaking lambda a lot per-texture.  We recommend
leaving that at "Default" (inherit) as much as possible.  The tech leads should set up the global lambda to
what's right for your game, and possibly set up the LODGroups to override that for specific texture classes.
Only rarely should you need to override on specific textures.
LIMITATIONS :
Currently our Oodle Texture for UE4 integration only works for non-console builds. (eg. Windows,Linux,Mac,
host PC builds).  It cannot export content for PS4/5/Xbox/Switch console builds.  We will hopefully be
working with Epic to fix this ASAP.
If you are a console dev, you can still try Oodle Texture for UE4, and it will work in your Editor and if
you package a build for Windows, but if you do "package for PS4" it won't be used.
Sample package sizes for "InfiltratorDemo" :
InfiltratorDemo-WindowsNoEditor.pak 

No compression :                            2,536,094,378

No Oodle Data (Zlib), no Oodle Texture :    1,175,375,893

Yes Oodle Data,  no Oodle Texture :           969,205,688

No Oodle Data (Zlib), yes Oodle Texture :     948,127,728

Oodle Data + Oodle Texture lambda=40 :        759,825,164
Oodle Texture provides great size benefit even with the default Zlib compression in Unreal, but it
works even better when combined with Oodle Data.
