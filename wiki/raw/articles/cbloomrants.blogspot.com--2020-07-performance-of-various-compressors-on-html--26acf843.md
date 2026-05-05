---
title: "Performance of various compressors on Oodle Texture RDO data"
url: "http://cbloomrants.blogspot.com/2020/07/performance-of-various-compressors-on.html"
fetched_at: 2026-05-05T07:01:48.364796+00:00
source: "Charles Bloom"
tags: [blog, raw]
---

# Performance of various compressors on Oodle Texture RDO data

Source: http://cbloomrants.blogspot.com/2020/07/performance-of-various-compressors-on.html

Oodle Texture RDO can be used with any lossless back-end compressor.  RDO does not itself make data
smaller, it makes the data more compressible for the following lossless compressor, which you use for
package compression.  For example it works great with the hardware compressors in the PS5 and the
Xbox Series X.
I thought I'd have a look at how various options for the back end lossless compressor do on BCN
texture data after Oodle Texture RDO.  (Oodle 2.8.9)
127,822,976 bytes of BC1-7 sample data from a game.  BC1,3,4,5, and 7.  Mix of diffuse, normals, etc.
The compressors here are run on the data cut into 256 KB chunks to simulate more typical game usage.
"baseline" is the non-RDO encoding to BCN by Oodle Texture.  "rdo lambda 40" is a medium quality RDO run;
at that level visual degradation is just starting to become easier to spot (lambda 30 and below is high
quality).
baseline:
by ratio:
ooLeviathan8    :  1.79:1 ,    1.4 enc MB/s , 1069.7 dec MB/s
lzma_def9       :  1.79:1 ,    8.7 enc MB/s ,   34.4 dec MB/s
ooKraken8       :  1.76:1 ,    2.2 enc MB/s , 1743.5 dec MB/s
ooMermaid8      :  1.71:1 ,    4.9 enc MB/s , 3268.7 dec MB/s
zstd22          :  1.70:1 ,    4.5 enc MB/s ,  648.7 dec MB/s
zlib9           :  1.64:1 ,   15.1 enc MB/s ,  316.3 dec MB/s
lz4hc1          :  1.55:1 ,   72.9 enc MB/s , 4657.8 dec MB/s
ooSelkie8       :  1.53:1 ,    7.4 enc MB/s , 7028.2 dec MB/s
rdo lambda=40:
by ratio:
lzma_def9       :  3.19:1 ,    7.7 enc MB/s ,   60.7 dec MB/s
ooLeviathan8    :  3.18:1 ,    1.1 enc MB/s , 1139.3 dec MB/s
ooKraken8       :  3.13:1 ,    1.7 enc MB/s , 1902.9 dec MB/s
ooMermaid8      :  3.01:1 ,    4.2 enc MB/s , 3050.6 dec MB/s
zstd22          :  2.88:1 ,    3.3 enc MB/s ,  733.9 dec MB/s
zlib9           :  2.69:1 ,   16.5 enc MB/s ,  415.3 dec MB/s
ooSelkie8       :  2.41:1 ,    6.6 enc MB/s , 6010.1 dec MB/s
lz4hc1          :  2.41:1 ,  106.6 enc MB/s , 4244.5 dec MB/s
If you compare the log-log charts before & after RDO, it's easy to see that the relative position of all
the compressors is basically unchanged, they just all get more compression.
The output size from baseline divided by the output size from post-RDO is the compression improvement
factor.  For each compressor it is :
ooLeviathan8    : 1.7765
ooKraken8       : 1.7784
ooMermaid8      : 1.7602
ooSelkie8       : 1.5548

lzma_def9       : 1.7821
zstd22          : 1.6941
zlib9           : 1.6402
lz4hc1          : 1.5751
Leviathan, Kraken, Mermaid and LZMA all improve around 1.77 X ; ZStd and Zlib a little bit less (1.65-1.70X),
LZ4 and Selkie by less (1.55X - 1.57X).
Basically the stronger compressors (on this type of data) get more help from RDO and their advantage grows.
ZStd is stronger than Mermaid on many types of data, but Mermaid is particularly good on BCN.
* : Caveat on ZStd & LZ4 speed here : this is a run of all compressors built with MSVC 2017 on my AMD reference
machine.  ZStd & LZ4 have very poor speed in their MSVC build, they do much better in a clang build.  Their clang
build can be around 1.5X faster; ZStd-clang is usually slightly faster to decode than Leviathan, not slower.
LZ4-clang is probably similar in decode speed to Selkie.  The speed numbers fo ZStd & LZ4 here should not be taken
literally.
It is common that the more powerful compressors speed up (decompression) slightly on RDO data
because they speed up with higher compression ratios, while the weaker compressors (LZ4 and Selkie) slow down slightly
on RDO data (because they are often in the incompressible path on baseline BCN, which is a fast path).
Looking at the log-log plots some things stand out to me as different than generic data :
Leviathan, Kraken & Mermaid have a smaller gap than usual.  Their compression ratio on this data is quite
similar, usually there's a bigger step, but here the line connecting them in log-log space is more horizontal.
This makes Mermaid more attractive because you're not losing much compression ratio for the speed gains.
(for example, Mermaid + BC7Prep is much better for space & speed than Kraken alone).
ZStd is relatively poor on this type of data.  Usually it has more compression than Mermaid and is closer to
Kraken, here it's lagging quite far behind, and Mermaid is significantly better.
Selkie is relatively poor on this type of data.  Usually Selkie beats LZ4 for compression ratio (sometimes it
even beats zlib), but here it's just slightly worse than LZ4.  Part of that is the 256 KB chunking is not
allowing Selkie to do long-distance matches, but that's not the main issue.  Mermaid looks like a much better 
choice than Selkie here.
Another BCN data set :
358,883,720 of BCN data.  Mostly BC7 with a bit of BC6.  Mix of diffuse, normals, etc.
The compressors here are run on the data cut into 256 KB chunks to simulate more typical game usage.
baseline :
by ratio:
ooLeviathan8    :  1.89:1 ,    1.1 enc MB/s ,  937.0 dec MB/s
lzma_def9       :  1.88:1 ,    7.6 enc MB/s ,   35.9 dec MB/s
ooKraken8       :  1.85:1 ,    1.7 enc MB/s , 1567.5 dec MB/s
ooMermaid8      :  1.77:1 ,    4.3 enc MB/s , 3295.8 dec MB/s
zstd22          :  1.76:1 ,    3.9 enc MB/s ,  645.6 dec MB/s
zlib9           :  1.69:1 ,   11.1 enc MB/s ,  312.2 dec MB/s
lz4hc1          :  1.60:1 ,   73.3 enc MB/s , 4659.9 dec MB/s
ooSelkie8       :  1.60:1 ,    7.0 enc MB/s , 8084.8 dec MB/s
rdo lambda=40 :
by ratio:
lzma_def9       :  4.06:1 ,    7.2 enc MB/s ,   75.2 dec MB/s
ooLeviathan8    :  4.05:1 ,    0.8 enc MB/s , 1167.3 dec MB/s
ooKraken8       :  3.99:1 ,    1.3 enc MB/s , 1919.3 dec MB/s
ooMermaid8      :  3.69:1 ,    3.9 enc MB/s , 2917.8 dec MB/s
zstd22          :  3.65:1 ,    2.9 enc MB/s ,  760.0 dec MB/s
zlib9           :  3.36:1 ,   19.1 enc MB/s ,  438.9 dec MB/s
ooSelkie8       :  2.93:1 ,    6.2 enc MB/s , 4987.6 dec MB/s
lz4hc1          :  2.80:1 ,  114.8 enc MB/s , 4529.0 dec MB/s
On this data set, Mermaid lags between the stronger compressors more, and it's almost equal to ZStd.  On BCN data, the strong compressors
(LZMA, Leviathan, & Kraken) have less difference in compression ratio than they do on some other types of data.  On this data set, Selkie
pulls ahead of LZ4 after RDO, as the increased compressibility of post-RDO data helps it find some gains.  Zlib, LZ4, and Selkie are almost
identical compression ratios on the baseline pre-RDO data but zlib pulls ahead post-RDO.
The improvement factors are :
ooLeviathan8   :    2.154
ooKraken8      :    2.157
ooMermaid8     :    2.085
ooSelkie8      :    1.831

lzma_def9      :    2.148
zstd22         :    2.074
zlib9          :    1.988
lz4hc1         :    1.750
Similar pattern, around 2.15X for the stronger compressors, around 2.08X for the medium ones, and under 2.0 for the weaker ones.
Conclusion:
Oodle Texture works great with all the lossless LZ coders tested here.  We expect it to work well with all
packaging systems.
The compression improvement factor from Oodle Texture is similar and good for all the compressors, but
stronger compressors like Oodle Kraken are able to get even more benefit from the entropy reduction of
Oodle Texture.  Not only do they start out with more compression on baseline non-RDO data, they also
improve by a larger multiplier on RDO data.
The Oodle Data lossless compressors are particularly good on BCN data, even relatively stronger than
alternatives like zlib and ZStd than they are on some other data types.  For example Oodle Mermaid is
often slightly lower compression than ZStd on other data types, but is slightly higher compression than
ZStd on BCN.
Mermaid has a substantial compression advantage over zlib on post-RDO BCN data, and decompresses 5-10X faster,
making Mermaid a huge win over software zlib (zip/deflate/inflate).
