---
title: "A rant about phishing: It's not the user's fault (and not DNS either)"
url: "https://maurycyz.com/misc/domains/"
fetched_at: 2026-09-10T10:01:26.398833+00:00
source: "maurycyz.com"
tags: [blog, raw]
---

# A rant about phishing: It's not the user's fault (and not DNS either)

Source: https://maurycyz.com/misc/domains/

A rant about phishing: It's not the user's fault (and not DNS either)
2026-09-09
"For safety, don't click suspicious links"
Meanwhile, most organization's login flow redirects through:
# This is a real example, but I've changed the names to avoid pointing fingers
https://www.
[name of company].com
/squawk/
https://login.
[name of company].com
/
https://
login.smallcrow.com
/324aa78a-03a6-66fc-23e1-4124fdsa213
https://
experience.crow-cloud.com
/
[name of company]
/auth
https://
flock.auth.bird-security.com
/authorization
https://
api-deadbeef.bird-security.com
/oauth/v1/authorize?token=DeAdBeEf
https://
api2.bird-security.com
/2fa
https://www.
[name of company].com
/cool/bird/
https://
experience.crow-cloud.com
/
[name of company]
/
https://www.
[name of company].com
/squawk/
Neither the username, password nor 2FA code prompts are hosted on the company's own domain.
Combine that with constant login expiration triggering random authetication pop-ups, and it's nearly impossible not to be phished
... because the real thing looks indistinguishable from a scam:
All an attacker needs to do is write a website with a password box and the company logo.
The URL doesn't matter at all because users are trained to ignore it.
I'll admit that URLs aren't the most intuitive things
, because the reading direction alternates.
Hostname and scheme start specific and become more general, while the path is the other way around:
https
://
funnies
.
maurycyz.com
/
memes
/crow_hobbies.jpg
  |        |        |     |    |     |     
  |        |        |     |    |     |
(most significant)
|        |        |     +------------ 1. Top level domain
  |        |        +------------------ 2. Operator
  |        +--------------------------- 3. Server name
  +------------------------------------ 4. Protocol
                               |     |
                               +-----|- 5. Directory 
                                     +- 6. Filename
(least significant)
This URL is for crow_hobbies.jpg, located in the
memes
folder
of the HTTP daemon on the
funnies
server run by
maurycyz.com
As a result of this syntax, the important bit (the second level domain) is in the middle of the URL.
This fact is something non-technical users must be taught: simply telling them to "avoid suspicious links" isn't enough.
However, the whole excersise is useless
if hostname isn't a reliable indicator.
For users to have any chance of spotting a scam...
An organization
MUST
use a single, well recognized, root domain.
Internal services
MUST
be on subdomains of the root and
MUST NOT
use URLs like:
# All these look like scams. Don't normalize scammyness!
https://[name of company]-auth.com/
https://[name of company].someone-else.com/
https://someone-else.com/[name of company]
https://auth.someone-else.com/[big UUID]
This is obviously important for login pages (since impersonating them would allow stealing credentials),
but it
SHOULD
be applied everywhere to build good habits and prevent social engineering.
Links sent by email or SMS
MUST
be under the recognizable domain.
If it's absolutely necessary to point users somewhere else, create a local redirect or a page with a link:
https://
[name of company].com
/survey
->
https://
crow-survey.com
/[name of company].
This does not mean everything has to be hosted by the organization:
many services allow bringing your own domain.
Links and redirects are free.
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL
    NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED",  "MAY", and
    "OPTIONAL" in this document are to be interpreted as described in
    RFC 2119...
The hostname situation
has gotten so bad that I've seen people arguing that it's a problem that subdomains exist,
because it allows criminals to impersonate anyone they want with no oversight.
DNS a hierarchical system who's structure hasn't changed in 40+ years:
There should absolutely no confusion over who runs any given website...
except that it seems to have become standard practice to put great effort into making legitimate sites indistinguishable from scams.
(not even governments consistently use their assigned TLDs)
