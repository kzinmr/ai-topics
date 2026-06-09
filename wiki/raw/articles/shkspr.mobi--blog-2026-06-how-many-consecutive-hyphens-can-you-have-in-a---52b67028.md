---
title: "How many consecutive hyphens can you have in a domain name?"
url: "https://shkspr.mobi/blog/2026/06/how-many-consecutive-hyphens-can-you-have-in-a-domain-name/"
fetched_at: 2026-06-09T07:01:22.846799+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# How many consecutive hyphens can you have in a domain name?

Source: https://shkspr.mobi/blog/2026/06/how-many-consecutive-hyphens-can-you-have-in-a-domain-name/

A seemingly simple question which sent me down into the murky depths of standards. How many consecutive hyphens can you have in a domain name? It probably isn't
sensible
to name your online presence
a----------hyphen.com
- but is there anything technically stopping you?
History
TLD Restrictions
Anomalies
So What?
Let's do some history!
This is 1978's "HOST NAMES ON-LINE". Early Internet standards described the
-
character as "minus" rather than hyphen.
RFC 608
up to 48 characters drawn from the alphabet (A-Z),
digits (0-9), and the minus sign (-) ... specifically, no blank or space characters allowed;
no distinction between upper and lower case letters;
the first character is a letter;
the last character is NOT a minus sign;
no other restrictions on content or syntax.
So, originally, you could have as many hyphens as you wanted after the first symbol - which had to be a letter. The last symbol had to be a letter or number
.
That was later formalised in 1981's "DoD INTERNET HOST TABLE SPECIFICATION"
RFC 810
GRAMMATICAL HOST TABLE SPECIFICATION
<name>  ::= <let>[*[<let-or-digit-or-hyphen>]<let-or-digit>]
That's carried in the the slightly more modern
RFC 952
.
By the time we hit 1987, the word "minus" has gone. Note, there are no restrictions on the number of hyphens - just as long as your domain name doesn't start or end with one
.
RFC 1035
2.3.1. Preferred name syntax
The labels must follow the rules for ARPANET host names.  They must start with a letter, end with a letter or digit, and have as interior characters only letters, digits, and hyphen.
By 1989, the "DOMAIN NAMES - IMPLEMENTATION AND SPECIFICATION" was tweaked again:
RFC 1123
2. GENERAL ISSUES
The syntax of a legal Internet host name was specified in RFC-952.  One aspect of host name syntax is hereby changed: the restriction on the first character is relaxed to allow either a letter or a digit.  Host software MUST support this more liberal syntax.
And, from then on, things stayed pretty stable until the futuristic year 2010. That was when Internationalised Domain Names (IDN) became available. They use the
xn--
string at the start of the name so, the spec now says:
RFC 5891
4.2.3.1.  Hyphen Restrictions
The Unicode string MUST NOT contain "--" (two consecutive hyphens) in the third and fourth character positions and MUST NOT start or end with a "-" (hyphen).
What they
really
mean is that "--" is banned in position 3 & 4
unless
the first two characters are "xn"
.
So, in theory, you can have up to 59 consecutive hyphens by ensuring that they start in position 4 and end at position 62.
Something like
abc---[…]---z.com
should be fine.
OR IS IT?!?!?
There's what the RFC's say, and what a Top Level Domain (TLD) will allow. The Registry (the organisation which administers the TLD) may set their own, more restrictive, policies. Some will ban naughty words, or refuse IDN registrations, or prevent impersonation of Public Suffix domain, etc.
For example, South Sudan's
.ss policies refuse to allow
any
hyphens
.
Nominet, who run the .uk Registry,
don't have any restrictions on the use of hyphens
other than refusing to register
xn--
domains.
But, in general, you can register multi-hyphened domain names with most Registries.
Of course, the mighty Internet mostly runs on spit and hope
. Naturally there are going to be mistakes, glitches, exceptions, and anomalies.
My delightful friend
Q Misell
had a rummage through her archives and helped track down some of the domain names which violate the modern rules. It's somewhat difficult to query
every
domain name, nevertheless, there are hundreds of multi-hyphened domains lurking within DNS.
Some, like
ok--computer.com
are long dead, but some are still active
!
Possibly the most consecutive hyphens belongs to
http://a-------------------------------------------------------------a.com/
Sixty-one hyphens! The maximum possible, and it still works! The website looks like it hasn't been updated since it was first registered in 2000.
But what about more modern domains? The spookily named
http://zz--icann-monitoring.uk/
was registered in 2024 - long after the rules were updated. But as Nominet doesn't allow
xn--
domains, I guess it is fine?
There are some domains like
bq--3bhauz7frjrgbka.com
which look like they were pseudo-randomly generated. Perhaps as command-and-control servers?
Here's a quick table showing some of the ones Q found:
Domain
Creation Date
Status
0-------------------------------------------------------------0.com
1999
Down
0-------------------------------------------------------------5.com
2001
Live
0---------------------0.com
2000
Live
0----------------0.com
2000
Live
0---------0.com
2000
Live
pr--newswire.org.uk
2005
Down
0o--o0.com
2000
Down
a-----a.net
2000
Down
pr--newswire.uk
2019
Down
uk--domain--names.uk
2019
Live
zz--icann-monitoring.uk
2024
Live
cd--storage-shelves.co.uk
2012
Live
mb--uk.co.uk
2015
Live
o---t.co.uk
2016
Live
om--tat-sat.co.uk
1999
Live
pr--newswire.co.uk
2005
Down
uk--domain--names.co.uk
2000
Down
we--buy--any--car.co.uk
2009
Down
i---i.net
2001
Down
a-------------------------------------------------------------a.com
2000
Live
a---b.com
2000
Down
v---v.net
2000
Down
we--care.net
1999
Down
b---h.com
2001
Down
bq--3bhauz7frjrgbka.com
2000
Down
bq--3bhauz7frjrgbkdcia.com
2000
Down
bq--3cbpcty2rjyq.com
2000
Down
bq--744a.com
2000
Down
bq--abs7czi.com
2000
Down
bq--abxgt4lb.com
2000
Down
bq--azbukkckjavdc.com
2000
Down
bq--azdecny.com
2000
Live
bq--eh7xj73b75xp62x7mh7xgah7ad7xj73b75xa.com
2000
Down
bq--gbbpy2enmnhq.com
2000
Down
bq--gbtfs2a.com
2000
Down
bq--s7z76.com
2000
Down
bq--zzzz.com
2000
Down
c-------7.com
2001
Live
f---you.com
1998
Down
id--design.com
1999
Down
ok--computer.com
2001
Down
t---28.com
2000
Live
t---taz---t.com
2001
Down
Note, "Live" just means an HTTP request returned
something
. There may, of course, be other services running on that domain, or on subdomains.
Without a full list of every domain name, it's rather hard to draw firm conclusions. But, in the absence of anything better to do, here are some thoughts.
Most people don't want multiple consecutive hyphens in their domain names. They're unwieldy but mostly not prohibited.
If the authors of RFC 5891 had access to a full list of domains, might they have chosen a different syntax for Punycode?
Why is it so hard to look through every single registered domain name anyway? Even Certificate Logs no longer seem to be easily searchable.
Are there any other weird restrictions which are violated by older domain names?
When will DNS finally go all-in with Unicode rather than this kludge? (Probably around the same time as IPv6 adoption!)
If you know of any weird multi-hyphenated domains, please stick a comment in the box 😊
Update!
A kind anonymous benefactor has shared a list of eighty-four
thousand
domains with multiple hyphen
s. There are some very odd entries in there.
