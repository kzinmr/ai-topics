---
title: "PHP - simple way to send HTTP headers before a script ends"
url: "https://shkspr.mobi/blog/2026/05/php-simple-way-to-send-http-headers-before-a-script-ends/"
fetched_at: 2026-05-26T07:14:43.263381+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# PHP - simple way to send HTTP headers before a script ends

Source: https://shkspr.mobi/blog/2026/05/php-simple-way-to-send-http-headers-before-a-script-ends/

Suppose you want PHP to keep processing
after
it has sent back an HTTP response. Normally, this doesn't work:
⧉
PHP
<?php
header
(
"Location: https://example.com/"
);
//   Long operation.
sleep
(10);
die
();
Try it yourself. You'll have to wait 10 seconds before you get back
⧉
< HTTP/2 302 
< location: https://example.com/
There are some complex ways to fix this - they usually involve spawning sub-processes or having a cron job run something. But there's a simpler way!
Most servers do some form of output buffering. They wait for the buffer to fill (or be explicitly terminated) before they send any content. My server was set to a buffer of 4,096 bytes. So I forced some dummy output to fill it up, then told PHP to flush the buffer:
⧉
PHP
<?php
header
(
"Location: https://example.com/"
);
echo
str_repeat
(
"😆"
, 4097);
flush
();
sleep
(10);
die
();
Some clients, like Python's Requests,
wait until they've explicitly seen the end of the response before processing it
.
But, for something like curl, the above is sufficient.
