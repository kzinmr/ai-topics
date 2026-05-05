---
title: "How to identify software licenses using Python, Vector Space Search and Ngram Keywords"
url: "https://boyter.org/2017/05/identify-software-licenses-python-vector-space-search-ngram-keywords/"
fetched_at: 2026-05-05T07:02:00.243238+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# How to identify software licenses using Python, Vector Space Search and Ngram Keywords

Source: https://boyter.org/2017/05/identify-software-licenses-python-vector-space-search-ngram-keywords/

EDIT
– I have since taken the ideas below improved them and released a command line application you can use to build software license reports
https://github.com/boyter/lc/
The below is mostly a log of my thought process while building out some functionality that I wanted to add into
searchcode server
. I kept a record of progress and thoughts while doing this in the hopes that I get some sort of useful blog post out of it. It has been edited somewhat for clarity.
One of the tickets raised for searchcode server is the ability to to filter by licence
https://github.com/boyter/searchcode-server/issues/96
yes, I am the one who raised the ticket, but it is based on requests from customers. It will also put searchcode server closer to feature parity with Krugle so it seems like a good thing to add.
This means that ideally all I want is a script that given a projects directory and a filename can tell me what licenses it is likely to be under. I can then port that over to searchcode-server and its Java codebase at my leisure.
My first thought was that adding it for say the top 20 most popular licenses shouldn’t be too difficult, and its something that I could always expand on later if things are working well.
As such the first thing I needed was to determine the top software licenses in use which thankfully Blackduck Software has already done
https://www.blackducksoftware.com/top-open-source-licenses
Then I needed to get a copy of them and in a nice format such as JSON to allow for processing. I decided to source them from SPDX.org since generally they should be considered the source of truth for license information.
https://spdx.org/licenses/
I then wrote a simple script
download.py
to pull all the licenses down (yes using regex to pull information out of HTML which is BAD but I am not trying to parse it so I am
pretty sure he won’t come
) locally and allow for further processing. Sorry SPDX people about crawling your site in a non robots compliant way. I did try to get what I needed and cache it locally so I suspect I impacted the site less than Googlebot would have.
I also added a simple filter to pull back the top 20+ licences that we previously identified so we can test things out.
The next step was to turn the HTML into JSON. Again an ugly script
parse.py
which calls the beast by using regex to pull information out of HTML. One thing I did notice is that the Fair Source licence was missing. Since I was planning on using searchcode server as a test bed I needed that and added it myself.
Once again sorry to the SPDX people. If you come to Sydney and ill buy you a beer and apologize for,
For creating my own short-name for the Fair Source License without permission
For the crappy internet you will experience (Seriously search for Turnbull NBN if you want to see how backwards a country can become, copper for life yo)
The result is now we have a database of about 20 licences that we can use to try and determine what licence a software project is.
Attempt 1
To start with I made the following assumptions.
A file with a name such as LICENSE or COPYING is likely to exist in the root folder of any project and contain license information. If not have a look inside the readme (if it exists). This file if found and it has a license that we can identify then it becomes the base license for all files inside the project. However files inside the project itself may have a header which must also be considered.
One thing that I didn’t consider at first is that there may be another license/copying file somewhere deeper inside the file tree. Something to consider for later.
First thought was to just use the vector space search algorithm. It really is my hammer for every problem. It works reasonably well for a lot of them, is fast enough in most cases and generally gets the job done. Thankfully I had already written
one for Python
a while ago. Don’t hate please, I wrote this 10 years ago when I was first learning it and yes its not Pythonic but works. One thing to note is that licenses tend to be of different length. This means that licenses that are closer to each other in length will be matched more closely using the vector space which is a cool side effect of how it works.
So the algorithm is,
Find likely candidates for license files.
Compare them to the list of known licenses using the vector space model.
Keep the most likely match.
Then walk through every file in the repository, checking for the special header and when there are no matches try the full header because things like the entire MIT license tends to get included at the top of the file. The resulting ugly script
attempt1.py
produced the following.
The result for
searchcode-server
Project License
0.929696395964 Fair Source License v0.9
0.802095284986 Mozilla Public License 2.0 (no copyleft exception)
0.802095284986 Mozilla Public License 2.0

0.925341443302 MIT License /searchcode-server/src/main/resources/public/js/cache.js
Wow. That is a very cool result. It actually worked. It not only picked up that we are using the Fair Source Licence it also picked up that that one file is using the MIT license. Lets try it out on some other projects.
Against
wordpress
,
Project License
0.623430083878 GNU General Public License v2.0 only
0.614318516008 GNU General Public License v1.0 only
0.601642491832 GNU Library General Public License v2 only
While it did pick up that its probably using GNU GPL v2.0 but it wasn’t as confident as it was with the previous. Lets try another one.
Against
minitwit
(a Spark Java example project)
Project License
0.954897366777 MIT License
0.784597744861 Fair Source License v0.9
0.777231345803 Apache License 2.0
Not bad. Its pretty confident that it us under the MIT license.
Against
Armory React
Project License
0.945769202843 BSD 3-clause Clear License
0.937649791859 BSD with attribution
0.927894236317 BSD 2-clause "Simplified" License
Again pretty good.
Ok. So it looks like we could just pop the top license off and call it a day. This works pretty well with the most common licenses, but why limit ourselves. Lets just do every license that SPDX has listed? It should work just as well in theory. All we need to do is remove the filter in download.py and rebuild the database and try again.
Trying out on searchcode-server again
Project License
0.929696395964 Fair Source License v0.9
0.813818153434 OCLC Research Public License 2.0
0.804549095187 OSET Public License version 2.1

0.977617793941 BSD Zero Clause License /searchcode-server/include/license/database.json
0.939606278132 Attribution Assurance License /searchcode-server/include/license/database.json
0.908192569643 Open CASCADE Technology Public License /searchcode-server/include/license/database.json
0.902275136399 Adaptive Public License 1.0 /searchcode-server/include/license/database.json
0.93217139424 JSON License /searchcode-server/src/main/resources/public/js/cache.js
0.925341443302 MIT License /searchcode-server/src/main/resources/public/js/cache.js
0.914039614281 feh License /searchcode-server/src/main/resources/public/js/cache.js
Ok so it still picked up fair source as the main project license which is a good result. However our very cool result of MIT being found in cache.js has gone away. Apparently the JSON license looks like the MIT license to the vector space. Indeed a diff between them shows that they are almost the same. The differences being right at the start,
MIT License Copyright (c)
JSON License Copyright (c) 2002 JSON.org
and buried in the middle of the JSON license
The Software shall be used for Good, not Evil.
Hah! I remember reading about that a while ago. Something about Google not being able to use it because apparently their motto “Don’t be evil” is more a guideline then a rule. In all seriousness though its actually due to the license being classified as a non-free license because it imposes conditions which restrict the usage see
https://www.cnet.com/news/dont-be-evil-google-spurns-no-evil-software/
for more details.
So what we would normally do about now is add keyword weighting to the terms so that in this case MIT makes it rank higher for MIT and JSON for JSON. In fact I started doing just that with keyword it then realised with 328 licenses this is going to be a painful process. Perhaps there is a better way.
Thinking about it what we really want is to find keywords or a collection of multiple keywords that we know to be unique for each license. Then all we need to is check the text for the presence of those keywords. The catch being we need to ensure that they are unique for each license. To do so what I think will work is break the license up into collections of works of length 1-10 and check for unique-ness against the other licenses. The technical term for these terms is ngram.
An example would be,
Lorem ipsum dolor sit amet consetetur sadipscing elitr
bi-grams
[('lorem', 'ipsum'), ('ipsum', 'dolor'), ('dolor', 'sit'), ('sit', 'amet'), ('amet', 'consetetur'), ('consetetur', 'sadipscing'), ('sadipscing', 'elitr')]
tri-grams
[('lorem', 'ipsum', 'dolor'), ('ipsum', 'dolor', 'sit'), ('dolor', 'sit', 'amet'), ('sit', 'amet', 'consetetur'), ('amet', 'consetetur', 'sadipscing'), ('consetetur', 'sadipscing', 'elitr')]
Thankfully this is pretty easy to do in Python so I borrowed an existing bit of code to do it for me,
http://locallyoptimal.com/blog/2013/01/20/elegant-n-gram-generation-in-python/
input_list
=
[
'all'
,
'this'
,
'happened'
,
'more'
,
'or'
,
'less'
]
def
find_ngrams
(input_list, n):
return
zip(
*
[input_list[i:]
for
i
in
range(n)])
For the record I am totally aware that NTLK can also do this but since I don’t currently have that installed lets go pure Python. It will be a little slower but considering this should rarely run this calculation I am not too worried about performance yet. Of course thats a good idea to live by anyway. Only worry about performance when it becomes an issue.
We can then generate ngrams for each license, then check for its uniqueness in every other one. If no matches found then woohoo we have a gram that uniquely matches the license.
Some simple but stupid code was written
parse2.py
which does exactly this. Turns out that language is a lot more distinctive for licenses then I first thought,
0BSD 188
AAL 1985
Abstyles 437
Adobe-2006 1234
Adobe-Glyph 1620
ADSL 608
AFL-1.1 555
AFL-1.2 251
AFL-2.0 69
AFL-2.1 67
AFL-3.0 452
Afmparse 959
AGPL-1.0 2212
...truncated..
For the BSD Zero Clause License there are apparently 188 unique ngrams between a length of 2-10 words in it. For the Affero General Public License v1.0 there are a whopping 2212! The numbers were so high that I changed the ngrams to start at 5 to 10. This dropped the numbers found by about 25% which seems about right as you would expect the most unique combinations of words to exist at the upper range of ngrams.
One problem I noticed with this is that a lot of the ngrams are based on names that exist within the sample licenses that SPDX has. For example BSD Zero Clause has the name “Rob Landley” which produces a lot of ngrams with this name in it as is indeed unique, but is useless unless we happen to be checking code that Rob has written.
However the performance issue that I was worried about before popped up. it was taking a long time to process. Not surprising considering the actual implementation consists of multiple nested loops. With the encouraging result that there is a lot of uniqueness for most licenses I tried just searching for ngrams of 4-5 words long to speed things up. Assuming we didn’t find 0 matches then happy days we can try implementing using what we have and everything should be fine. A few small tweaks later and I ran it again.
Doh! As it turns out some are not unique enough. The culprits,
Artistic-1.0
BSD-3-Clause
MIT-CMU
MPL-1.1
MPL-2.0-no-copyleft-exception
MPL-2.0
I modified the code to just loop those ones with a more exhaustive search to find what worked. With ngrams of length 2-10 still there was not enough uniqueness. So I went all out, ngrams from length 2-35.
Artistic-1.0 120
BSD-3-Clause 21
This resolved the issue for Artistic-1.0 and BSD-3-Clause but we still have nothing for the following licenses,
MIT-CMU
MPL-1.1
MPL-2.0-no-copyleft-exception
MPL-2.0
Something is wrong here.
Turns out some of these are particularly troubling. The Mozilla Public License 1.1 (MPL-1.1 in the above) for example seems to be embedded  in the Netscape Public License v1.1 which of course means nothing about it is unique compared to the other. The others have a similar story. I tried searching just between both those licences with ngrams of length 2-100 to see if anything would turn up, which of course took a crazy amount of time to process. The result was that there was nothing that could be used keyword wise to seperate these licenses.
How about a hybrid approach?
If we cannot definitively say using keywords what license the file is, then we can fall back to the vector space to rank based on those without keywords. To do so I flushed the results of the last run into the database file using 7-8 ngrams for everything except Artistic-1.0 and BSD-3-Clause which checked for ngrams with a range of 2-35. The results of this produced the following licenses with their number of unique ngrams,
0BSD 25
AAL 246
Abstyles 54
Adobe-2006 163
Adobe-Glyph 210
ADSL 78
...truncated...
Fair-Source-0.9 267
Most seem to have over 100 or so unique ngrams which means they will probably work pretty well, and as expected the only exceptions are the MPL licenses which has nothing unique about it compared to every other license.
I ended up cleaning up the code at this point and improving on the loops so thankfully it took only a few minutes to run. Some of the original runs were taking tens of minutes due to inefficient code so this was a big win. The resulting file was on the heavy side though at 20 megabytes and crashed most editors when I tried to read it. To resolve this I truncated down to at most 50 unique ngrams per license to see how this worked in the real world. This file weighed in a much more realistic 3 megabytes.
I then created
attempt2.py
which used the new database using keywords to guess which license the applications had applicable. Firstly I tried it against searchcode-server itself. With the result that the LICENCE file found was indeed the Fair Source License. I then tried it against GCC. Its interesting to note that this resulted in its COPYING file being marked as containing both the GPL-2.0 and LGPL-2.1. At first I thought this might have been a bug in my logic but it seems it was actually correct. The offending ngram used to match was
"street, fifth floor, boston, ma 02110-1301 usa"
Which is supposed to be unique to LGPL-2.1 but included in this case. Since we actually have 813 (but truncated to 50) ngrams for each I figured we might as well when checking see if MOST (70%) of the keywords are there, and if so mark it as a match otherwise ignore. This resutled in the following for GCC
COPYING GPL-2.0
COPYING.LIB GPL-2.0
COPYING.RUNTIME GPL-2.0
COPYING3 GPL-3.0
COPYING3.LIB GPL-3.0
Which is correct. In fact further tests on various other repositories worked until I hit the react-armory which is under the BSD Clear License. Turns out most of the ngrams generated for it actually involve the project name meaning they are useless. Annoyingly the ngram of length 3 “BSD Clear License” which is unique was missed because the parser was set to look from 7-8 ngrams. Urgh.
Thinking about this for a bit, it totally makes sense to look for ngrams from 2-8 even when we are truncating to the top 50. The smaller ones are going to be high value ones usually and there shouldn’t be too many of them. The only problem is the increased processing time to walk all of the combinations of things like [‘the’, ‘license’] and the like. At the very least we should include trigrams (3 length ngrams) since it solves this specific issue and should work to be unique for a lot of licenses. Modifying the parse2.py script to take in a range of numbers defined was easy enough then just let it run and produce the new database to work with and try everything again. It took longer than before but not so much that it was annoying.
Due to how painful this was getting to test manually I started to build a small test harness (
test_attempt2.py
) which I could eyeball to see if I was getting closer to a result I wanted without regressions. Thankfully it was working perfectly for the tests I was trying.
At this point I tried the same technique across all the files in repositories. Using the previous example of searchcode-server I would have expected that the cache.js file would be marked as MIT license as before. This however was not the case. Because I had the keyword match script as a sliding scale where it needed a few matches to be considered positive it was missing out on this one as there were only a few matches.
I decided at this time to integrate the Vector Space back in. If a file was marked with any license, we would then confirm using the Vector Space and if it was able to have a high degree of confidence over the license that matched then it would be marked as the license. After adding this logic I managed to get the following output,
Bens-MBP:license boyter$ python attempt2.py
0.988840442861 Fair-Source-0.9 /searchcode-server/LICENSE.txt
0.442713859889 MIT /searchcode-server/src/main/resources/public/js/cache.js
Exactly what I was looking for. All of the tests I had previously written also passed with this logic. With a simple change to only check the top of the file where the header would be by cutting the string down to the length of the license I was able to improve the result considerably,
Bens-MBP:license boyter$ python attempt2.py
0.988840442861 Fair-Source-0.9 /searchcode-server/LICENSE.txt
0.985719098155 MIT /searchcode-server/src/main/resources/public/js/cache.js
That is a seriously cool result. Not only was the code able to identify the licences, it did so with a very high percentage of confidence to boot.
I tried running it over a collection of projects I had checked out including GCC, Linux and WordPress
0.993261478239 BSD-3-Clause-Clear /armory-react/LICENSE
0.999679612780 GPL-3.0 /decodingcaptchas/LICENSE
0.980796066053 OFL-1.1 /decodingcaptchas/lib/font/source-sans-pro/LICENSE
0.999692799354 GPL-3.0 /freemoz/LICENSE
0.999792347852 GPL-2.0 /gcc/COPYING
0.999922926136 LGPL-2.1 /gcc/COPYING.LIB
0.999679612780 GPL-3.0 /gcc/COPYING3
0.999902746595 LGPL-3.0 /gcc/COPYING3.LIB
0.999792347852 GPL-2.0 /gcc/gcc/COPYING
0.999932589474 LGPL-2.1 /gcc/gcc/COPYING.LIB
0.999679612780 GPL-3.0 /gcc/gcc/COPYING3
0.999902746595 LGPL-3.0 /gcc/gcc/COPYING3.LIB
0.858896713823 GPL-2.0 /gcc/gcc/df-core.c
0.999532020106 GFDL-1.3 /gcc/gcc/ada/doc/share/gnu_free_documentation_license.rst
0.948529328513 bzip2-1.0.6 /gcc/gcc/testsuite/gcc.c-torture/execute/pr20527-1.c
0.994200247145 bzip2-1.0.6 /gcc/gcc/testsuite/gcc.dg/params/LICENSE
0.999792347852 GPL-2.0 /gcc/include/COPYING
0.999679612780 GPL-3.0 /gcc/include/COPYING3
0.889767272339 bzip2-1.0.6 /gcc/libbacktrace/alloc.c
0.899838703127 bzip2-1.0.6 /gcc/libbacktrace/atomic.c
0.883378984629 bzip2-1.0.6 /gcc/libbacktrace/backtrace.c
0.885232659466 bzip2-1.0.6 /gcc/libbacktrace/btest.c
0.866517942966 bzip2-1.0.6 /gcc/libbacktrace/dwarf.c
0.881126480326 bzip2-1.0.6 /gcc/libbacktrace/elf.c
0.876148037216 bzip2-1.0.6 /gcc/libbacktrace/fileline.c
0.862314849462 bzip2-1.0.6 /gcc/libbacktrace/mmap.c
0.876559695369 bzip2-1.0.6 /gcc/libbacktrace/mmapio.c
0.903997364404 bzip2-1.0.6 /gcc/libbacktrace/nounwind.c
0.880387358104 bzip2-1.0.6 /gcc/libbacktrace/pecoff.c
0.872402129061 bzip2-1.0.6 /gcc/libbacktrace/posix.c
0.881550515104 bzip2-1.0.6 /gcc/libbacktrace/print.c
0.878971997218 bzip2-1.0.6 /gcc/libbacktrace/read.c
0.880857671076 bzip2-1.0.6 /gcc/libbacktrace/simple.c
0.897738871764 bzip2-1.0.6 /gcc/libbacktrace/sort.c
0.890041393843 bzip2-1.0.6 /gcc/libbacktrace/state.c
0.874782494001 bzip2-1.0.6 /gcc/libbacktrace/stest.c
0.897023027383 bzip2-1.0.6 /gcc/libbacktrace/unknown.c
0.879821572348 MITNFA /gcc/libffi/src/mips/ffi.c
0.997055163924 LGPL-2.1 /gcc/libiberty/copying-lib.texi
0.999932589474 LGPL-2.1 /gcc/libiberty/COPYING.LIB
0.899167675944 Intel /gcc/liboffloadmic/runtime/liboffload_error.c
0.889543866358 Intel /gcc/liboffloadmic/runtime/liboffload_msg.c
0.887357763796 Intel /gcc/liboffloadmic/runtime/orsl-lite/lib/orsl-lite.c
0.999932589474 LGPL-2.1 /gcc/libquadmath/COPYING.LIB
0.857337014417 NCSA /gcc/libsanitizer/LICENSE.TXT
1.000000000000 BSL-1.0 /gcc/zlib/contrib/dotzlib/LICENSE_1_0.txt
0.998470560414 GPL-2.0 /linux/COPYING
0.999831352903 LGPL-2.0 /linux/arch/sparc/lib/COPYING.LIB
0.997101938433 GPL-2.0 /linux/Documentation/networking/LICENSE.qlcnic
0.997101938433 GPL-2.0 /linux/Documentation/networking/LICENSE.qlge
0.997004626197 GPL-2.0 /linux/Documentation/scsi/LICENSE.qla2xxx
0.997004626197 GPL-2.0 /linux/Documentation/scsi/LICENSE.qla4xxx
0.900564102581 Intel /linux/drivers/crypto/qat/qat_c3xxx/adf_c3xxx_hw_data.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_c3xxx/adf_drv.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_c3xxxvf/adf_c3xxxvf_hw_data.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_c3xxxvf/adf_drv.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_c62x/adf_c62x_hw_data.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_c62x/adf_drv.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_c62xvf/adf_c62xvf_hw_data.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_c62xvf/adf_drv.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_accel_engine.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_admin.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_aer.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_cfg.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_ctl_drv.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_dev_mgr.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_hw_arbiter.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_init.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_isr.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_pf2vf_msg.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_sriov.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_transport.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_transport_debug.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_vf2pf_msg.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/adf_vf_isr.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/qat_algs.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/qat_asym_algs.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/qat_crypto.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/qat_hal.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_common/qat_uclo.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_dh895xcc/adf_dh895xcc_hw_data.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_dh895xcc/adf_drv.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_dh895xccvf/adf_dh895xccvf_hw_data.c
0.900564102581 Intel /linux/drivers/crypto/qat/qat_dh895xccvf/adf_drv.c
0.998958351972 GPL-2.0 /linux/drivers/staging/rtl8192e/license
0.999594583136 GPL-2.0 /linux/drivers/staging/rtl8192u/copying
0.999792347852 GPL-2.0 /linux/tools/usb/usbip/COPYING
0.952930843666 Sleepycat /pathos/dill-0.2.1/LICENSE
0.952930843666 Sleepycat /pathos/pathos-master/LICENSE
0.952930843666 Sleepycat /pathos/pox-0.2/LICENSE
0.987991559152 MIT /phonecat/LICENSE
1.000000000000 Apache-2.0 /python-goose/LICENSE.txt
1.000000000000 Apache-2.0 /searchcode/searchcode/searchcode/static/admin/fonts/LICENSE.txt
0.987991559152 MIT /searchcode/searchcode/searchcode/static/admin/js/vendor/xregexp/LICENSE-XREGEXP.txt
0.988840442861 Fair-Source-0.9 /searchcode-server/LICENSE.txt
0.985719098155 MIT /searchcode-server/src/main/resources/public/js/cache.js
0.985719098155 MIT /searchcode-server/target/classes/public/js/cache.js
0.999268167835 LGPL-2.1 /seo/vendor/videlalvaro/php-amqplib/LICENSE
0.999692799354 GPL-3.0 /SingleBugs/LICENSE
0.999692799354 GPL-3.0 /testing/LICENSE
0.997865652460 GPL-2.0 /wordpress/license.txt
0.999792346238 GPL-2.0 /wordpress/wp-content/themes/twentyfourteen/genericons/LICENSE.txt
0.999792346238 GPL-2.0 /wordpress/wp-content/themes/twentythirteen/fonts/LICENSE.txt
0.999792346238 GPL-2.0 /wordpress/wp-includes/js/plupload/license.txt
0.999932589474 LGPL-2.1 /wordpress/wp-includes/js/tinymce/license.txt
Rather cool. Lots of licenses identified with quite a lot of confidence.
There is however one issue I am overlooking. Take for example a project which includes another project in a sub directory. What license should be displayed for the files that are in the latter? In this case I would expect that they are marked with both. It would be very nice to see this information.
One final issue is what to do when there are multiple license files in the root directory. GCC is an example of this and it has 4 licenses defined in the root. The idea being you take which one is most applicable to your project.
0.999792347852 GPL-2.0 /gcc/COPYING
0.999922926136 LGPL-2.1 /gcc/COPYING.LIB
0.99967961278 GPL-3.0 /gcc/COPYING3
0.999902746595 LGPL-3.0 /gcc/COPYING3.LIB
Looking at the SPDX specification the rule is to define them as being under all. This is the exact text regarding this,
Representing Multiple Licenses
Multiple licenses can be represented using a SPDX license expression as defined in Appendix IV. A set of licenses must be enclosed in parentheses (this is a convention for SPDX expressions). As further described there:
When there is a choice between licenses (“disjunctive license”), they should be separated with “OR”. If presented with a choice between two or more licenses, use the disjunctive binary “OR” operator to construct a new license expression.
Similarly when multiple licenses need to be simultaneously applied (“conjunctive license”), they should be separated with “AND”. If required to simultaneously comply with two or more licenses, use the conjunctive binary “AND” operator to construct a new license expression.
In some cases, a set of license terms apply except under special circumstances, in this case, use the “WITH” operator followed by one of the recognized exception identifiers.
Sometimes a set of license terms apply except under special circumstances. In this case, use the binary “WITH” operator to construct a new license expression to represent the special exception situation.
Examples:
SPDX-License-Identifier: (GPL-2.0 OR MIT)
SPDX-License-Identifier: (LGPL-2.1 AND BSD-2-CLAUSE)
SPDX-License-Identifier: (GPL-2.0+ WITH Bison-exception-2.2)
This was taken from
https://spdx.org/spdx-specification-21-web-version
Appendix V: Using SPDX short identifiers in Source Files
Fair enough. We then need to write one last version of our license guesser which will use everything done above BUT support multiple licenses and look for license files inside root directories and make anything below it as belonging to that one, unless of course there is another license file or it is over-ridden by the header. We are not trying to keep track of the above WITH or AND logic described above as I just want to mark each file with the potential license. As such just marking it so is good enough.
For this I simply copied the existing attempt2.py and created
attempt3.py
which should hopefully be the last version for this. What we now need to do is walk the tree, and every time we encounter a license file, keep track of the license that the file should be under, and for any file that is a child of that license mark as such. When we leave the directory then we pop the license off.
Thankfully this was a very easy change to implement. I used a project which I knew to already have some mixed licenses and ran over it.
>>>>>>>> /decodingcaptchas/LICENSE GPL-3.0
>>>>>>>> /decodingcaptchas/LICENSE GPL-3.0
>>>>>>>> /decodingcaptchas/LICENSE GPL-2.0
>>>>>>>> /decodingcaptchas/LICENSE GPL-2.0
/decodingcaptchas/Gruntfile.js GPL-2.0 GPL-3.0
/decodingcaptchas/code/crack.py GPL-2.0 GPL-3.0
/decodingcaptchas/code/crack_test.py GPL-2.0 GPL-3.0
/decodingcaptchas/code/geticons.py GPL-2.0 GPL-3.0
/decodingcaptchas/code/step1.py GPL-2.0 GPL-3.0
/decodingcaptchas/code/step2.py GPL-2.0 GPL-3.0
/decodingcaptchas/code/step3.py GPL-2.0 GPL-3.0
/decodingcaptchas/code/step4.py GPL-2.0 GPL-3.0
/decodingcaptchas/code/style.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/reveal.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/print/paper.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/print/pdf.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/theme/beige.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/theme/black.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/theme/blood.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/theme/league.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/theme/moon.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/theme/night.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/theme/serif.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/theme/simple.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/theme/sky.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/theme/solarized.css GPL-2.0 GPL-3.0
/decodingcaptchas/css/theme/white.css GPL-2.0 GPL-3.0
/decodingcaptchas/js/reveal.js GPL-2.0 GPL-3.0
>>>>>>>> /decodingcaptchas/lib/LICENSE Fair-Source-0.9
/decodingcaptchas/lib/css/zenburn.css Fair-Source-0.9 GPL-2.0 GPL-3.0
/decodingcaptchas/lib/font/league-gothic/league-gothic.css Fair-Source-0.9 GPL-2.0 GPL-3.0
>>>>>>>> /decodingcaptchas/lib/font/source-sans-pro/LICENSE OFL-1.1
>>>>>>>> /decodingcaptchas/lib/font/source-sans-pro/LICENSE OFL-1.1
/decodingcaptchas/lib/font/source-sans-pro/source-sans-pro.css Fair-Source-0.9 GPL-2.0 GPL-3.0 OFL-1.1
/decodingcaptchas/lib/js/classList.js Fair-Source-0.9 GPL-2.0 GPL-3.0
/decodingcaptchas/lib/js/head.min.js Fair-Source-0.9 GPL-2.0 GPL-3.0
/decodingcaptchas/lib/js/html5shiv.js Fair-Source-0.9 GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/highlight/highlight.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/leap/leap.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/markdown/markdown.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/markdown/marked.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/math/math.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/multiplex/client.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/multiplex/index.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/multiplex/master.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/notes/notes.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/notes-server/client.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/notes-server/index.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/print-pdf/print-pdf.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/remotes/remotes.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/search/search.js GPL-2.0 GPL-3.0
/decodingcaptchas/plugin/zoom-js/zoom.js GPL-2.0 GPL-3.0
/decodingcaptchas/test/qunit-1.12.0.css GPL-2.0 GPL-3.0
/decodingcaptchas/test/qunit-1.12.0.js GPL-2.0 GPL-3.0
/decodingcaptchas/test/test-markdown-element-attributes.js GPL-2.0 GPL-3.0
/decodingcaptchas/test/test-markdown-slide-attributes.js GPL-2.0 GPL-3.0
/decodingcaptchas/test/test-markdown.js GPL-2.0 GPL-3.0
/decodingcaptchas/test/test-pdf.js GPL-2.0 GPL-3.0
/decodingcaptchas/test/test.js GPL-2.0 GPL-3.0
What this shows is each file along with each license that the program believes it to belong to. Files prefixed with »»»> indicate a license file which changes the licenses of the files below it.
The root of the project is dual licensed under GPL-2.0 and GPL-3.0 which makes everything have at least those two licenses. There are however also some fonts under the SIL Open Font License 1.1 which were also picked up. To make things a little harder I added the Fair Source license under the lib directory (just as a test) to see if this would be reflected correctly.
I am pretty happy with the result. So I took the code and ran it against GCC and the Linux Kernel. The output for both are too large to post on this blog but you can view the GCC one as a gist
https://gist.github.com/boyter/ee534011cf512ba7e2992ecdef87523c
The last part was to add back the file check so that we can identify license headers for each file in the subfolders. Thankfully this was just a short tweak. Of course the generation is now much slower due to add the additional processing but it seemed to work pretty well.
Well that about covers that. Everything seems to work as I would expect and it would be reasonably easy at this point to take the code and produce a full blown SPDX parser. I will leave that as an exercise for the reader (unless it turns out I need one at a later date).
The next step for me is to integrate this into searchcode server, which is just porting the above into Java and then adding this information as a facet for searching. This is something I may write about later. If you are interested in a
code search application though please check it out
!
I have uploaded all the code into the following
github repository
released under the MIT License. Note that the database will also be released under Creative Commons inside the
searchcode-server
project itself and it is also something I will be keeping up to date so it might be a better source if you want to do any license matching.
