---
title: "Finalizing a compression format"
url: "http://fastcompression.blogspot.com/2016/05/finalizing-compression-format.html"
fetched_at: 2026-05-05T07:00:59.989811+00:00
source: "Yann Collet (LZ4/Zstd)"
tags: [blog, raw]
---

# Finalizing a compression format

Source: http://fastcompression.blogspot.com/2016/05/finalizing-compression-format.html

With Zstandard v1.0 looming ahead, the last major item for zstd to settle is an extended set of features for its frame encapsulation layer.
Quick overview of the design : data compressed by zstd is cut into blocks. A compressed block has a maximum content size (128 KB), so obviously if input data is larger than this, it will have to occupy multiple blocks.
The frame layer organize these blocks into a single content. It also provides to the decoder a set of properties that the encoder pledges to respect. These properties allow a decoder to prepare required resources, such as allocating enough memory.
The current frame layer only stores 1 identifier and 2 parameters  :
frame Id :
It simply tells what are the expected frame and compression formats for follow. This is currently use to automatically detect legacy formats (v0.5.x, v0.4.x, etc.) and select the right decoder for them. It occupies the first 4 bytes of a frame.
windowLog
: This is the maximum search distance that will be used by the encoder. It is also the maximum block size, when
(1<<windowLog) < MaxBlockSize (== 128 KB)
. This is enough for a decoder to guarantee successful decoding operation using a limited buffer budget, whatever the real content size is (endless streaming included).
contentSize
: This is the amount of data to decode within this frame. This information is optional. It can be used to allocate the exact amount of memory for the object to decode.
These information may seem redundant.
Indeed, for a few situations, they are : when
contentSize  < (1<<windowLog)
. In which case, it's enough to allocated
contentSize
bytes for decoding, and
windowLog
is just redundant.
But for all other situations,
windowLog
is useful : either
contentSize
is unknown (it wasn't known at the beginning of the frame and was only discovered on frame termination), or
windowLog
defines a smaller memory budget than
contentSize
, in which case, it can be used to limit memory budget.
That's all there is for v0.6.x. Arguably, that's a pretty small list.
The intention is to create a more feature complete frame format for v1.0.
Here is a list of features considered, in priority order :
Content Checksum
: objective is to validate that decoded content is correct.
Dictionary ID
: objective is to confirm or detect dictionary mismatch, for files which require a dictionary for correct decompression. Without it, a wrong dictionary could be picked, resulting in silent corruption (or an error).
Custom content
, aka skippable frames : the objective is to allow users to embed custom elements (comments, indexes, etc.) within a file consisting of multiple concatenated frames.
Custom window sizes
, including non power of 2 : extend current windowLog scheme, to allow more precise choices.
Header checksum
: validate that checksum informations are not accidentally distorted.
Each of these bullet points introduce its own set of questions, that is detailed below :
Content checksum
The goal of this field is obvious : validate that decoded content is correct. But there are many little details to select.
Content checksum only protects against accidental errors (transmission, storage, bugs, etc). It's not an electronic "signature".
1) Should it be enabled or disabled by default (field == 0) ?
Suggestion : disabled by default
Reasoning : There are already a lot of checksum around, in storage, in transmission, etc. Consequently, errors are now pretty rare, and when they happen, they tend to be "large" rather than sparse. Also, zstd is likely to detect errors just by parsing the compressed input anyway.
2)
Which algorithm ? Should it be selectable ?
Suggestion : xxh64, additional header bit reserved in case of additional checksum, but just a single one defined in v1.
Reasoning : we have transitioned to a 64-bits world. 64-bits checksum are faster to generate than 32-bits ones on such systems. So let's use the faster ones.
xxh64 also has excellent distribution properties, and is highly portable (no dependency on hardware capability). It can be run in 32-bits mode if need be.
3)
How many bits for the checksum ?
Current format defines the "frame end mark" as a 3-bytes field, the same size as a block header, which is no accident : it makes parsing easier. This field has a 2-bits header, hence 22 bits free, which can be used for a content checksum. This wouldn't increase the frame size.
22-bits means there is a 1 in 4 millions chances of collision in case of error. Or said differently, there are 4194303 chances out of 4194304 to detect a decoding error (on top of all the syntax verification which are inherent to the format itself). That's more than > 99.9999 %. Good enough in my view.
Dictionary ID
Data compressed using a dictionary needs the exact same one to be regenerated. But no control is done on the dictionary itself. In case of wrong dictionary selection, it can result in a data corruption scenario.
The corruption is likely to be detected by parsing the compressed format (or thanks to the previously described optional content checksum field).
But an even better outcome would be detect such mismatch immediately, before starting decompression, and with a clearer error message/id than "corruption", which is too generic.
For that, it would be enough to embed a "Dictionary ID" into the frame.
The Dictionary ID would simply be a random value stored inside the dictionary (or an assigned one, provided the user as a way to control that he doesn't re-use the same value multiple times). A comparison between the ID in the frame and the ID in the dictionary will be enough to detect the mismatch.
A simple question is : how long should be this ID ? 1, 2, 4 bytes ?
In my view, 4 bytes is enough for a random-based ID, since it makes the probability of collision very low. But that's still 4 more bytes to fit into the frame header. In some ways it can be considered an efficiency issue.
Maybe some people will prefer 2 bytes ? or maybe even 1 byte (notably for manually assigned ID values) ? or maybe even 0 bytes ?
It's unclear, and I guess multiple scenarios will have different answers.
So maybe a good solution would be to support all 4 possibilities in the format, and default to 4-bytes ID when using dictionary compression.
Note that if saving headers is important for your scenario, it's also possible to use frame-less block format (
ZSTD_compressBlock()
,
ZSTD_decompressBlock()
), which will remove any frame header, saving 12+ bytes in the process. It looks like a small saving, but when the corpus consists of lot of small messages of ~50 bytes each, it makes quite a difference. The application will have to save metadata on its own (what's the correct dictionary, compression size, decompressed size, etc.).
Custom content
Embedding custom content can be useful for a lot of unforeseen applications.
For example, it could contain a custom index into compressed content, or a file descriptor, or just some user comment.
The only thing that a standard decoder can do is skip this section. Dealing with its content is within application-specific realm.
The
lz4 frame format
already defines such container, as skippable frames. It looks good enough, so let's re-use the same definition.
Custom window sizes
The current frame format allows defining window sizes from 4 KB to 128 MB, all intermediate sizes being strict power of 2 (8 KB, 16 KB, etc.). It works fine, but maybe some user would find its granularity or limits insufficient.
There are 2 parts to consider :
- Allowing larger sizes : the current implementation will have troubles handling window sizes > 256 MB. That being said, it's an implementation issue, not a format issue. An improved version could likely work with larger sizes (at the cost of some complexity).
From a frame format perspective, allowing larger sizes can be as easy as keeping a reserved bit for later.
- Non-power of 2 sizes : Good news is, the internals within zstd are not tied to a specific power of 2, so the problem is limited to sending more precise window sizes. This requires more header bits.
Maybe an unsigned 32-bits value would be good enough for such use.
Note that it doesn't make sense to specify a larger window size than content size. Such case should be automatically avoided by the encoder. As to the decoder, it's unclear how it should react : stop and issue an error ? proceed with allocating the larger window size ? or use the smaller content size, and issue an error if the content ends up larger than that ?
Anyway, in many cases, what the user is likely to want is simply enough size for the frame content. In which case, a simple "refer to frame content size" is probably the better solution, with no additional field needed.
Header Checksum
The intention is to catch errors in the frame header before they translate into larger problems for the decoder. Note that only errors can be caught this way : intentional data tampering can simply rebuild the checksum, hence remain undetected.
Suggestion : this is not necessary.
While transmission errors used to be more common a few decades ago, they are much less of threat today, or they tend to garbage some large sections (not just a few bits).
An erroneous header can nonetheless be detected just by parsing it, considering the number of reserved bits and forbidden value. They must all be validated.
The nail in the coffin is that we do no longer trust headers, as they can be abused by remote attackers to deliver an exploit. And that's an area where the header checksum is simply useless. Every field must be validated, and all accepted values must have controllable effects (for example, if the attacker intentionally requests a lot of memory, the decoder shall put a high limit to the accepted amount, and check the allocation result).
So we already are highly protected against errors, by design, because we must be protected against intentional attacks.
Future features : forward and bakward compatibility
It's also important to design from day 1 a header format able to safely accommodate future features, with regards to version discrepancy.
The basic idea is to keep a number of reserved bits for these features, set to
0
while waiting for some future definition.
It seems also interesting to split these reserved bits into 2 categories :
- Optional and skippable features : these are features which a decoder can safely ignore, without jeopardizing decompression result. For example, a purely informational signal with no impact on decompression.
- Future features, disabled by default (
0
): these features can have unpredictable impact on compression format, such as : adding a new field costing a few more bytes. A non-compatible decoder cannot take the risk to proceed with decompression. It will stop on detecting such a reserved bit to
1
and gives an error message.
While it's great to keep room for the future, it should not take a too much toll in the present. So only a few bits will be reserved. If more are needed, it simply means another frame format is necessary. It's enough in such case to use a different frame identifier (First 4 bytes of a frame).
