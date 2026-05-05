---
title: "Can anyone explain how this regex [ -~] matches ASCII characters?"
url: "https://boyter.org/2014/02/explain-regex-matches-ascii-characters/"
fetched_at: 2026-05-05T07:02:04.281386+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Can anyone explain how this regex [ -~] matches ASCII characters?

Source: https://boyter.org/2014/02/explain-regex-matches-ascii-characters/

Since I am pulling most of my content from other sites such as Mahalo and Quora I thought I would pull back some of my more interesting HN comments.
Can anyone explain how this regex [- ~] matches ASCII characters?
It’s pretty simple. Assuming you know regex. Im going to assume you don’t since you are asking.
The bracket expression [ ] defines single characters to match, however you can have more then 1 character inside which all will match.
[a] matches a
[ab] matches either a or b
[abc] matches either a or b or c
[a-c] matches either a or b or c
The – allows us to define the range. You can just as easily use [abc] but for long sequences such as [a-z] consider it short hand.
In this case [ -~] it means every character between  and , which just happens to be all the ASCII printable characters (see chart in the article). The only bit you need to keep in mind is that  is a character as well, and hence you can match on it.
You could rewrite the regex like so (note I haven’t escaped or anything in this so its probably not valid)
[ !"#$%&'()*+,-./0123456789:;&lt;=&gt;?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~]
but that’s not quite as clever or neat.
