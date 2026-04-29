---
title: "You can parse an .env file as an .ini with PHP"
url: "https://shkspr.mobi/blog/2026/04/you-can-parse-an-env-file-as-an-ini-with-php-but-theres-a-catch/"
fetched_at: 2026-04-29T07:01:07.708823+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# You can parse an .env file as an .ini with PHP

Source: https://shkspr.mobi/blog/2026/04/you-can-parse-an-env-file-as-an-ini-with-php-but-theres-a-catch/

The humble
.env
file is a useful and low-tech way of storing persistent environment variables. Drop the file on your server and let your PHP scripts consume it with glee.
But consume it
how
? There are lots of excellent parsing libraries for PHP. But isn't there a simpler way? Yes! You can use
PHP's
parse_ini_file()
function
and it works.
But…
.env
and
.ini
have subtly different behaviour which might cause you to swear at your computer.
Let's take this example:
⧉
ENV
# This is a comment
USERNAME
="edent"
Run
$env = parse_ini_file( ".env" );
and you'll get back an array setting the USERNAME to be "edent". Hurrah! Works perfectly. Ship it!
But consider this:
⧉
ENV
# This is a comment
USERNAME
="edent"
# Don't use an @ symbol here.
It will happily tell you that the username is
"edent# Don"
WTAF?
Here's the thing. The comment character for
.ini
is
not
#
- it's the semicolon
;
Let me give you some other examples of things which will fuck up your parsing:
⧉
ENV
# Documentation at https:/example.com/?doc=123
DOCUMENTATION
=123
# Set the password
PASSWORD
=qwerty;789
That gets us back this PHP array:
⧉
PHP
[
'# Documentation at https:/example.com/?doc'
=>
'123'
,
'DOCUMENTATION'
=>
'123'
,
'PASSWORD'
=>
'qwerty'
,
];
When the
.ini
is parsed, it ignores every line which
doesn't have an
=
sign
. It also treats literal semicolons as the start of a new comment until they're wrapped in quotes.
My code highlighter should show you how it is parsed:
⧉
INI
#
Documentation at https:/example.com/?doc
=123
DOCUMENTATION
=123
# Set the password
PASSWORD
=qwerty
;789
It gets worse. Consider this:
⧉
ENV
# Set the "official" name
REALNAME
="Arthur, King of the Britons"
That immediately fails with
PHP Warning:  syntax error, unexpected '"' in envtest on line 1
You can use single quotes in pseudo-comments just fine, but if the ini parser sees a double quote without an equals then it throws a wobbly.
I'm sure there are several other gotchas as well. For example, there are
certain reserved words and symbols you can't used as a key
.
This will fail:
⧉
ENV
# Can we fix it? Yes we can!
FIX
=true
It chokes on the exclamation point.
The comments on an
.env
file start with a hash.
The comments on an
.ini
file start with a semicolon.
So, it is perfectly valid for a hybrid file to have its comments start with
#;
Look, if it's stupid but it works…
There's a right way and a wrong way to do
.env
parsing.
The wrong way works, up until the point it doesn't.
You should probably use a proper parser rather than hoping your
.env
looks enough like an
.ini
to pass muster.
On next week's show - why you shouldn't store your passwords inside a JPEG!
