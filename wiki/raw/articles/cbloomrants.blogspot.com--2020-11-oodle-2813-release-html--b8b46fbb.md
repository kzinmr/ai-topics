---
title: "Oodle 2.8.13 Release"
url: "http://cbloomrants.blogspot.com/2020/11/oodle-2813-release.html"
fetched_at: 2026-05-05T07:01:48.618938+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Oodle 2.8.13 Release

Source: http://cbloomrants.blogspot.com/2020/11/oodle-2813-release.html

Oodle 2.8.13 fixes an issue in Oodle Texture with consistency of encodings across machine architectures.
We try to ensure that Oodle Texture creates the same encodings regardless of the machine you run on.  So
for example if you run on machines that have AVX2 or not, our optional AVX2 routines won't change the
results, so you get binary identical encodings.
We had a mistake that was causing some BC1 RDO encodings to be different on AMD and Intel chips.  This is
now fixed.
The fixed encoding (for BC1 RDO) made by 2.8.13 can be different than either of the previous (AMD or Intel)
encodings.
I want to use this announcement as an opportunity to repeat I point I am trying to push :
Do not use the binary output of encodings to decide what content needs to be patched!
This is widespread practice in games and it is really a bad idea.  The problem is that any changes to the encoders
you use (either Oodle Texture, your compressor, or other), can cause you to patch all your content unnecessarily.
We do NOT gaurantee that different versions of Oodle Texture produce the same output, and in fact we can specifically
promise they won't (always produce the same encodings)
because we will continue to improve the encoder and find better encodings over time.  Aside from version
changes causing binary diffs, you might want to change settings, quality or speed levels, etc. and that
shouldn't force a full patch down to customers.
The alternative to using binary output to make patches is to check if the pre-encoding content has changed, and don't
patch if that is the same.  I know there are difficult issues with that, often for textures you do something like load a
bitmap, apply various transforms, then do the BCN encoding, and there's not a snapshot taken of the fully processed
texture right before the BCN encoding.
If you are shipping a game with a short lifespan, your intention is to only ship it and only patch for bugs, then
patching based on binary compiled content diffs is probably fine.  But if you are shipping a game that you intend to have
a long lifetime, with various generations of DLC, or a long term online player base, then you seriously need to consider
patching based on pre-compression content diffs.  It is very likely you will at some point in the life time of the game
have to face OS version changes, compiler changes, or perhaps bugs in the encoder which force you to get on a newer version
of the compression tools.  You don't want to be in a situation where that's impossible because it would generate big patches.
One elegant way to solve this, and also speed up your content cooking, is to implement a cooked content cache.
Take the source bitmap, and all the texture cooking & encoding options, and use those as a key to look up pre-cooked content
from a network share or similar.  If found, don't re-encode.
Every time you export a level, you don't want to have to re-encode all the textures with Oodle Texture.  With huge
art teams, when someone edits a texture, everyone else on the team can just fetch from the cook cache rather than
encode it locally.
The same kind of system can be used to avoid unnecessary patches.
If you then populate your cook-cache with the content from the last shipped version, you won't make new encodings unless the
source art or options change, even if the encoder algorithm changes.
For the lossless package compressor, ideally the patch generator would be able to decode the compression and wouldn't generate
patches if only the compressed version changed.
To be clear, I'm assuming here that you are compressing assets individually, or even in smaller sub-asset chunks, or some kind of
paging unit.  I'm assuming you are NOT compressing whole packages as single compression units; if you did that any a single byte changing
in any asset could change the entire compressed unit, that's a bad idea for patching.
(note that encryption also has the same property of taking a single byte change and spreading it around the chunk, so encryption
should usually be done on the same or smaller chunk than the compression)
With most existing patchers that are not compression-aware, if you change the compressor (for example by changing the encode level
option, or updating to a newer version), the compressed bytes will change and generate large patches.  What they should ideally
do is see that while the compressed bytes changed, the decompressed bytes are the same, so no patch is needed, and the old version
of the compressed bytes can be retained.  This would allow you to deploy new compressors and have them used for all new content
and gradually roll out, without generating unnecessary large patches.
