---
title: "Blunt Banhammer Blocks Basic Bots Ballistically"
url: "https://shkspr.mobi/blog/2026/11/blunt-banhammer-blocks-basic-bots-ballistically/"
fetched_at: 2026-11-10T10:01:16.872447+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Blunt Banhammer Blocks Basic Bots Ballistically

Source: https://shkspr.mobi/blog/2026/11/blunt-banhammer-blocks-basic-bots-ballistically/

I cut bot traffic to my site by over 80% with a simple trap.
Last month, my hobby website
OpenBenches.org
transferred more than 2.5TB of data to visitors. As much as I'd like to think the site is enormously popular, it looks like it is just AI bots endlessly crawling the data and slurping up the images.
So I've built B
6
to be an indiscriminate tool to eradicate these unwanted parasites.
It is
very
loosely inspired by
Jeff Starr's Blackhole
, but works even on sites with heavy caching.
Here's the high level description of how it works.
Create a directory like
/honeypot/
on your site
Put some code in
index.php
within the directory
Add the honeypot as an explicit "Disallow" in
robots.txt
Include a hidden link to to the honeypot on every page of your site
If something accesses that page, write its IP address to your
.htaccess
The
.htaccess
bans the IP address from ever accessing your site again.
This blog post shows you how you can build this yourself and discusses some of the problems it might cause.
The file
robots.txt
lives at the root of your website. It contains a list of instructions to automated web crawlers. Respectful bots will read it and refuse to look at specific parts of your site.
Add these two lines to it:
Copied  to 📋
⧉
User-agent: *
Disallow: /honeypot/
That says bots shouldn't visit any page in the honeypot directory.
Bots generally check for updates every 24 hours, so either wait a day or manually submit it to major crawlers.
The
.htaccess file
contains a list of instructions for how your server should process requests.
Find the bit of your
.htaccess
file which looks like this:
Copied  to 📋
⧉
<IfModule mod_rewrite.c>
        RewriteEngine On
        RewriteBase /
Edit it to look like this:
Copied  to 📋
⧉
<IfModule mod_rewrite.c>
        RewriteEngine On
        RewriteBase /

### BLOCKED IPs
    #   TEST-NET-1
    RewriteCond %{REMOTE_ADDR} "=192.0.2.1"
    RewriteRule ^ - [R=402,L]
### /BLOCKED IPs
It is important that these rules come before any other rewrite rules.
Change the end of this
IfModule
to look like:
Copied  to 📋
⧉
</IfModule>

ErrorDocument 402 "Payment Required - Access Denied."
If an IP address is in the blocked IP list, the server will send an error code and a readable message. You can add whatever plain text you like here.
Inside the honeypot directory, create a file called
index.php
(or whatever you like). When this page is visited, it grabs the visitor's IP address and the name of its User Agent. It then places them in the BLOCKED IPs section.
Copied PHP to 📋
⧉
PHP
//  What's their IP?
$IP
=
get_client_ip
();
//  User Agent
$UA
=
isset
(
$_SERVER
[
"HTTP_USER_AGENT"
] )
?
$_SERVER
[
"HTTP_USER_AGENT"
] :
""
;
//  Get the existing .htaccess file.
$htaccess_file
=
"../.htaccess"
;
$htaccess
=
file_get_contents
(
$htaccess_file
);
//  Split by newline.
$htaccess_lines
=
explode
(
separator
:
"\n"
,
string
:
$htaccess
);
//  Where's our start block?
$start
=
"###   BLOCKED IPs"
;
$end
=
"###   /BLOCKED IPs"
;
//  Exit if the .htaccess doesn't have the block.
if
( !
in_array
(
needle
:
$start
,
haystack
:
$htaccess_lines
) ) {
die
(); }
//  This is where to start from.
$start_block
=
array_search
(
needle
:
$start
,
haystack
:
$htaccess_lines
);
//  Add the line after the start block.
//  Include a date.
$htaccess_lines
[
$start_block
] =
$start
.
"\n"
.
"\t#\t"
.
date
(
"c"
) .
"\t{$UA}\n"
.
"\tRewriteCond %{REMOTE_ADDR} \"={$IP}\" [OR]"
;
//  Turn the array back to a string.
$newHtaccess
=
implode
(
separator
:
"\n"
,
array
:
$htaccess_lines
);
//  Save the new .htaccess file.
file_put_contents
(
filename
:
$htaccess_file
,
data
:
$newHtaccess
);
function
get_client_ip
():
string
{
//  Adapted from https://github.com/ibericode/koko-analytics/blob/main/src/Resources/functions/collect.php
//  X-Forwarded-For sometimes contains a comma-separated list of IP addresses
//  @see https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Forwarded-For
$ips
=
empty
(
$_SERVER
[
"HTTP_X_FORWARDED_FOR"
] )
?
[] :
        \
array_map
(
"trim"
, \
explode
(
","
,
$_SERVER
[
"HTTP_X_FORWARDED_FOR"
] ) );
//  Always add REMOTE_ADDR and HTTP_CLIENT_IP to list of ip addresses, if set
foreach
( [
"REMOTE_ADDR"
,
"HTTP_CLIENT_IP"
]
as
$key
) {
if
( !
empty
(
$_SERVER
[
$key
] ) ) {
$ips
[] =
$_SERVER
[
$key
];
        }
    }
//  Return first valid IP address from list
foreach
(
$ips
as
$ip
) {
if
( \
filter_var
(
$ip
,
FILTER_VALIDATE_IP
,
FILTER_FLAG_NO_PRIV_RANGE
|
FILTER_FLAG_NO_RES_RANGE
) ) {
return
$ip
;
        }
    }
return
""
;
}
Web crawlers look at a page, find every link on it, then visit those links. So we need to put a link to the honeypot on every page - but in such a way that normal users will not find it or click it.
This adds a link, removes it from the accessibility tree, and gives it impossible to click text (a zero width joiner).
Copied HTML to 📋
⧉
HTML
<
a
id
="honey"
aria-hidden
="true"
href
="/honeypot/index.php">‍</
a
>
This CSS hides it from normal viewers and removes the mouse cursor from view.
Copied CSS to 📋
⧉
CSS
#honey
{
display
: none !important;
cursor
:  none !important;
}
It's unlikely that a human will find the link, click on it, and be banned. But if they do, consider put a message in the blocking text telling them how they can get unblocked.
Some useful bots ignore robots.txt. If they identify themselves via a User-Agent string (and they should) you can manually remove them from .htaccess. You could also code in an allow list exemption for them. But, of course, many bad bots lie about who they really are.
Conversely, not all bots crawl every link. This won't catch bots which respect robots.txt but are nevertheless problematic.
If you have thousands of different bots blocked, the performance of your server
might
slow down while .htaccess is parsed. There's weak anecdotal evidence that it adds a slight overhead. But, personally, I don't think that's worth worrying about.
Bots often use hijacked IP addresses. After the bot has moved, an innocent party might be blocked from your site. Each block has a timestamp associated with it. You could periodically unblock older entries.
Bots rotate through hundreds of different IP addresses. So the same bot might get blocked multiple times.
Bots might see the CSS marks the link as hidden and refuse to follow it. Instead of CSS, you could use invisible spaces or other characters which would be hard for a human to see but appear visible to a bot.
Similarly, a smart bot might refuse to visit a path called /honeypot/ so choose a better name for it. A smarter bot would see that touching the honeypot leads to a ban - so perhaps a selection of traps are needed?
As is implied in the name, this is a
blunt
banhammer. It doesn't give a warning, nor does it look at User-Agent, Country, or any other signal. You touch the honeypot and you receive an instaban. No warning and no automated way to appeal.
There are alternative ways to do this. Some bots don't send language headers, some use older versions of HTTP, they often have severely outdated User Agent strings. Those are all reasonable ways to block something which is
probably
a bot. There are likely to be a few false positives though.
But B
6
has no false positives. A normal user
can't
follow the link to the trap and a well-behaved bot
won't
follow the link.
Things like Anubis require a lot of work to set up and annoy normal users. B
6
doesn't require a specific hosting environment and is never shown to normal users.
Since running B
6
a week ago, I've blocked over 400 IP addresses and seen a significant fall in traffic. I've not had any complaints yet. Sadly, none of the bots have paid to remove the paywall!
At peak, my site was seeing 216GB of data transfer per day. That's now dropped to around 25GB.
I don't claim this is the most sophisticated bot blocker in existence - but I enjoyed building it myself. I'll probably add something to records the geolocation of the IP and maybe remove any block older than a certain age.
If you'd like to use it or improve this code, I'd be grateful if you treated it as
AGPL v3 licensed
.
