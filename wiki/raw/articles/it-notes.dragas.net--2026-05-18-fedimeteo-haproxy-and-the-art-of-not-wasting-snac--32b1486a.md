---
title: "FediMeteo, HAProxy, and the art of not wasting snac threads"
url: "https://it-notes.dragas.net/2026/05/18/fedimeteo-haproxy-and-the-art-of-not-wasting-snac-threads/"
fetched_at: 2026-05-19T07:01:16.200297+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# FediMeteo, HAProxy, and the art of not wasting snac threads

Source: https://it-notes.dragas.net/2026/05/18/fedimeteo-haproxy-and-the-art-of-not-wasting-snac-threads/

When I wrote about
FediMeteo
for the first time, I told the story from the beginning: the idea born almost by chance while checking the weather for a holiday, the memory of my grandfather, who for years had been my personal meteorologist, the decision to build something small and useful, and then the surprise of seeing people actually use it. What began as a personal experiment quickly became a small global service, still running with the same philosophy: FreeBSD, jails, simple scripts, snac, text, emoji, and a lot of small pieces doing their work quietly.
That article was mostly about the birth and growth of the project. This one is about one of the less romantic parts of the same story, although I have to admit that I find a certain beauty in it too: keeping the service light as it grows.
FediMeteo
is still intentionally simple from the outside. A homepage, some numbers, a list of countries, and many ActivityPub accounts publishing weather forecasts. The posts are text and emoji. There is no JavaScript requirement to read the pages, no heavy frontend, no unnecessary media attached to every forecast, and no dynamic homepage recalculated at every visit just to show the same numbers. This is not accidental. It is the way I wanted the service to behave from the beginning.
But the more the service is used, the more the small details matter. A request that looks harmless when there are ten followers may become a repeated request when there are thousands of followers, remote instances, crawlers, previews, and other servers fetching the same public objects. In the Fediverse, the same small thing can be asked many times by many different places, each one with a perfectly legitimate reason. The backend doesn't care: it just needs to deal with the requests.
And in FediMeteo, the backend is
snac
.
I like snac very much precisely because it is small, clear, and efficient. It is not a giant application that tries to be everything. It does a focused job and does it well. But this also means that I want to respect its shape. I do not want to waste its threads on work that the reverse proxy can safely do. A snac thread serving the same public avatar again and again is not a tragedy, but it is still a waste. A snac thread answering the same public ActivityPub object several times in the same minute is doing real work, but often not necessary work.
This is the reason behind the
HAProxy
tuning I am currently using in front of FediMeteo.
It is not about making the configuration look clever. It is about keeping snac quiet.
A continuation of the same idea
I had already explored the same problem with snac and nginx in two previous posts:
Improving snac Performance with Nginx Proxy Cache
and
Caching snac Proxied Media with Nginx
. In both cases, the idea was that the reverse proxy should absorb repeated public requests instead of letting them consume snac resources.
This is especially important because snac uses a limited number of threads. I like that. Limits are healthy. They force us to understand what the service is doing, and they prevent a small program from pretending to be an infinite resource. But limits also make waste visible. If a few threads are busy serving files that could have been served from cache, those threads are not available for something more useful.
With FediMeteo the implementation is different because the reverse proxy is HAProxy, but the reasoning is the same. I have many small snac instances, each one in its own FreeBSD (
Bastille
) jail, and one public entry point that has to route, terminate TLS, compress, cache, and generally remove as much repetitive work as possible from the backends.
This is, in a way, the natural continuation of the original FediMeteo design. In the first article I wrote that I wanted to manage everything according to the Unix philosophy: small pieces working together. This is another piece of that same puzzle. HAProxy does the edge work. snac does the ActivityPub work. Scripts generate forecasts. cron launches updates. ZFS gives me snapshots. FreeBSD jails keep countries separated. Nothing is particularly heroic by itself, but the whole system becomes pleasant because each part has a clear responsibility.
Why there is almost no media
Before talking about HAProxy, it is worth mentioning one of the most important optimizations, which is not in the proxy configuration at all.
FediMeteo does not use media in its forecasts.
No images attached to the posts, no generated weather cards, no maps for each city, no decorative banners. The forecasts are text and emoji. This was a deliberate decision. Weather information does not become more useful just because it is put inside an image, and every media file used by the service would become something to store, serve, cache, federate, expire, back up, and occasionally debug.
Text and emoji are enough. They are accessible, light, readable in text browsers, friendly to timelines, and understandable even when someone does not know the local language perfectly. This was one of the original design principles of FediMeteo, and it also helps the infrastructure. Less media means less work, fewer cache entries, fewer repeated fetches, fewer surprises.
There is one exception: the avatar.
All FediMeteo accounts use the same avatar, and this is also intentional. I could have used a different avatar for each country, or for each city, or created something visually richer. It would have been nicer in some screenshots, perhaps. It would also have been operationally worse.
With one shared avatar, the reverse proxy has one very useful object to cache. It is public, identical for everyone, small, requested often, and therefore almost always hot in cache. HAProxy can serve it directly instead of asking each snac instance to return the same file. Since avatars are requested by remote instances, browsers, profile previews, and all sorts of federation-related fetches, this single decision removes a surprising amount of pointless backend traffic.
So the avatar is not only a visual identity. It is part of the architecture.
This is the kind of optimization I like most, because it starts before the software. It starts with deciding not to create a problem.
The homepage is static because it can be static
The main homepage follows the same logic.
It is a static HTML page generated from a template. Once per hour, a cron script updates the numbers and statistics. It counts the data I want to show, regenerates the page, and then the page remains static until the next run.
This is not because I cannot make a dynamic page. It is because I do not need one. Boring is good.
The homepage does not need to query all the country instances on every visit. It does not need a database request for each user who opens it. It does not need to ask snac anything in real time. The numbers are useful, but they do not need to be updated every second. Once per hour is enough, and it also fits the spirit of the whole project: do the work when it is needed, then serve the result cheaply.
I have seen too many small services become heavy because the first implementation was convenient rather than appropriate. A cron job and a template are not fashionable, but they are often exactly what a page like this needs.
Many countries, one entry point
FediMeteo is made of many country instances. Each one runs in its own jail and listens on its own internal address and port. From the outside, however, they all live under the same domain structure:
fedimeteo.com
www.fedimeteo.com
it.fedimeteo.com
uk.fedimeteo.com
jp.fedimeteo.com
us.fedimeteo.com
usa.fedimeteo.com
can.fedimeteo.com
canada.fedimeteo.com
And many more.
At the beginning, it is always tempting to write one ACL after another in the HAProxy frontend. It is quick, it is explicit, and for five hostnames it is perfectly fine. But FediMeteo did not remain at five hostnames. As countries and aliases grew, a long chain of ACLs would have turned the frontend into a list of names instead of a description of how the proxy behaves.
So I moved the hostname to backend mapping into a map file:
fedimeteo.com        backend_fedimeteo
www.fedimeteo.com    backend_fedimeteo
it.fedimeteo.com     backend_it
uk.fedimeteo.com     backend_uk
jp.fedimeteo.com     backend_jp
us.fedimeteo.com     backend_us
usa.fedimeteo.com    backend_us
can.fedimeteo.com    backend_ca
canada.fedimeteo.com backend_ca
The frontend then needs only one rule:
use_backend %[req.hdr(host),field(1,:),lower,map(/usr/local/etc/fedimeteo.map,backend_fedimeteo)]
This reads the
Host
header, removes the port if present, lowercases the result, and looks it up in
/usr/local/etc/fedimeteo.map
. If nothing matches, it falls back to the main FediMeteo backend.
I like this because it keeps the configuration honest. The frontend contains the policy. The map contains the data. Adding a country means adding an entry to the map and defining a backend. I do not need to make the frontend more complicated every time the service grows.
Backends as small compartments
The country backends are deliberately plain:
backend backend_it
    mode http
    http-reuse safe
    server srv1 10.0.0.2:8001 maxconn 30

backend backend_uk
    mode http
    http-reuse safe
    server srv1 10.0.0.7:8001 maxconn 30

backend backend_jp
    mode http
    http-reuse safe
    server srv1 10.0.0.32:8001 maxconn 30
One backend, one jail, one snac instance. This is exactly the same organizational principle as the rest of the project. If I need to reason about Italy, I look at the Italian jail. If I need to reason about the United Kingdom, I look at the UK jail. If one day I need to move a country elsewhere, the separation is already there.
The
maxconn 30
value is not a magic number. It is a ceiling. I want each small backend to have a visible limit in front of it. If something starts hammering a country instance, I prefer the pressure to appear at the HAProxy layer instead of becoming unlimited concurrent work inside snac.
http-reuse safe
lets HAProxy reuse backend connections where appropriate. This is another small reduction in unnecessary work. Opening connections repeatedly is not the biggest problem in the world, but avoiding it is still better, especially when many small services sit behind the same proxy.
The front door
The HTTPS frontend listens on IPv4 and IPv6 and offers both HTTP/2 and HTTP/1.1:
frontend https_in
    bind :::443 v4v6 ssl crt /usr/local/etc/certs/ alpn h2,http/1.1
    mode http
    option http-keep-alive
TLS defaults are set globally:
ssl-default-bind-ciphersuites TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256
ssl-default-bind-options no-sslv3 no-tlsv10 no-tlsv11 no-tls-tickets
Port 80 only redirects to HTTPS, except for Let's Encrypt challenges:
acl letsencrypt-acl path_beg /.well-known/acme-challenge/
http-request redirect scheme https code 301 unless letsencrypt-acl
use_backend letsencrypt-backend if letsencrypt-acl
In the HTTPS frontend I also set the usual forwarding headers:
http-request set-header X-Real-IP %[src]
http-request set-header X-Forwarded-Proto https
And I add HSTS:
http-response set-header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
None of this is unusual, and that is fine. The interesting parts of an infrastructure are not always the parts that should be unusual.
Two caches, because the requests are different
The HAProxy configuration defines two caches:
cache mediacache
  total-max-size 128
  max-object-size 10000000
  max-age 3600
  process-vary on
  max-secondary-entries 12

cache jsoncache
  total-max-size 16
  max-object-size 1000000
  max-age 60
  process-vary on
  max-secondary-entries 12
I keep media and ActivityPub JSON separate because they are not the same kind of traffic.
The media cache is larger and has a longer maximum age. In FediMeteo, this mostly means the shared avatar and a few static-looking objects. Since there is intentionally almost no media, the important cached object is requested very often and remains warm.
The JSON cache is smaller and short-lived. It is there for public ActivityPub GET requests, not to store federation state forever. A 60 second cache is enough to collapse many repeated requests that arrive close together in time, without pretending that ActivityPub responses should be treated like immutable files.
This distinction is important. Caching is not one decision. It is a set of small decisions about what a response means, who can see it, how often it changes, and what happens if it is served again.
Recognizing media
For media, the ACL is based on file extensions:
acl is_media path_end -i .jpg .jpeg .png .gif .webp .svg .ico .mp4 .webm .mp3 .ogg .wav .flac .mov .avi .mkv .m4v
Then I store the result in a transaction variable:
http-request set-var(txn.is_media) bool(true) if is_media
The cache lookup is straightforward:
http-request cache-use mediacache if { var(txn.is_media) -m bool true }
And on the response side:
http-response set-header Cache-Control "max-age=3600, public" if { var(txn.is_media) -m bool true }
http-response del-header Set-Cookie if { var(txn.is_media) -m bool true }
http-response del-header Vary if { var(txn.is_media) -m bool true }
http-response cache-store mediacache if { var(txn.is_media) -m bool true }
The
Cache-Control
header makes the intent explicit.
Set-Cookie
is removed because a public media object should not carry session information.
Vary
is removed because I do not want the same avatar to fragment into many cache entries because of harmless header differences.
This is aggressive only if removed from its context. In this service, with this media policy, it is a reasonable choice. FediMeteo is not serving private media under these paths. It is mostly serving the same public avatar over and over.
For the same reason, I clean the request before it reaches the backend:
http-request del-header Authorization if { var(txn.is_media) -m bool true }
http-request del-header Cookie        if { var(txn.is_media) -m bool true }
I would not do this globally. I do it after deciding that the request is media. Scope is what makes these rules safe.
The result is exactly what I want: the shared avatar becomes an almost perfect cache object. Small, public, repeatedly requested, and served by HAProxy instead of snac.
ActivityPub JSON microcaching
The ActivityPub side starts from the
Accept
header:
acl is_ap_json   req.hdr(Accept),lower -m sub application/activity+json
acl is_ap_ldjson req.hdr(Accept),lower -m sub application/ld+json
acl is_outbox    path_end /outbox
acl is_get       method GET
acl has_auth     req.hdr(Authorization) -m found
acl has_cookie   req.hdr(Cookie) -m found
This part matters because ActivityPub uses content negotiation. The same path may return HTML to a browser and JSON to a remote instance. If the proxy pretends that a URL is always one thing, it will eventually cache the wrong representation.
So I only mark public ActivityPub GET requests as cacheable:
http-request set-var(txn.is_activitypub) bool(true) if is_get !is_outbox is_ap_json !has_auth !has_cookie
http-request set-var(txn.is_activitypub) bool(true) if is_get !is_outbox is_ap_ldjson !has_auth !has_cookie
There are several decisions here, all important.
It must be a
GET
, because I am not caching deliveries or anything that changes state. It must not be
/outbox
, because outbox collections are not the traffic I want to cache here. It must not have
Authorization
, and it must not have cookies, because authenticated or user-specific requests do not belong in a shared public cache.
Then the cache can be used and populated:
http-request cache-use jsoncache if { var(txn.is_activitypub) -m bool true }

http-response set-header Cache-Control "max-age=60, public" if { var(txn.is_activitypub) -m bool true }
http-response cache-store jsoncache if { var(txn.is_activitypub) -m bool true }
Sixty seconds is short, but useful. Federation often creates small clusters of identical requests. A remote server fetches an actor, another fetches the same actor, something asks for the same object, something retries. I do not need to cache these responses for hours. I only need HAProxy to answer the second and third identical request during the same small burst.
This is microcaching in the most practical sense. It reduces repeated work without changing the nature of the service.
Static media paths
There is also a rule for static paths:
acl is_short_path path_reg ^/[^/]+/s/
http-request cache-use mediacache if is_short_path
This comes from the same observation that led me to cache snac media with nginx. snac uses static media paths, and those paths often represent the kind of public, repeatable traffic that should not consume backend threads if the proxy can serve it. I call them "short", not because they are, but because the first time I saw them, I thought the 's' stood for "short", not "static". The name just stuck.
In FediMeteo this is less central than on a normal social instance, because I deliberately do not use media except for the avatar and basic static objects. Still, the rule fits the general policy: let HAProxy handle repeatable edge work, and let snac spend its threads where they are actually needed.
Vary
, but not without limits
Both caches have:
process-vary on
max-secondary-entries 12
I want HAProxy to process
Vary
, because content negotiation is real, especially when ActivityPub is involved. But I also want variation to be bounded. If every slightly different header creates another cache entry, the cache becomes a complicated way to miss.
For media, I remove
Vary
before storing the response. A shared avatar does not need to vary by
Accept
. For ActivityPub JSON, I am more careful because the representation matters.
Again, the important thing is not the number itself. It is the decision to make variation explicit and limited.
Seeing whether it works
During rollout, I like to expose a very small diagnostic header:
http-response set-header X-Cache-Status HIT if !{ srv_id -m found }
http-response set-header X-Cache-Status MISS if { srv_id -m found }
This is intentionally simple. If HAProxy selected a backend server, I call it a miss. If no backend server was selected, the response came from cache, so I call it a hit. It is not a complete observability system, but it is enough to answer the first question I usually have after changing a cache rule.
Did this request reach snac?
A test can be as simple as:
curl -I https://it.fedimeteo.com/path/to/avatar.png
curl -I https://it.fedimeteo.com/path/to/avatar.png
The second request should be a hit.
For ActivityPub JSON, the test must use the right
Accept
header:
curl -I \
  -H 'Accept: application/activity+json' \
  https://it.fedimeteo.com/some/activitypub/object
And I also want to verify that cookies and authorization prevent public caching:
curl -I \
  -H 'Cookie: test=value' \
  -H 'Accept: application/activity+json' \
  https://it.fedimeteo.com/some/activitypub/object

curl -I \
  -H 'Authorization: Bearer fake' \
  -H 'Accept: application/activity+json' \
  https://it.fedimeteo.com/some/activitypub/object
A cache that works should be visible. A cache that is invisible can be correct, but it can also be silently wrong. I prefer to know.
Compression and operational paths
HAProxy also handles gzip compression:
filter compression
compression algo gzip
compression type text/css text/html text/javascript application/javascript text/plain text/xml application/json application/activity+json
This keeps another common responsibility at the edge. The country instances can stay focused on snac and the forecast data, while HAProxy deals with client-facing compression for HTML, JSON, and ActivityPub responses.
There is also a local Prometheus exporter:
frontend prometheus
  bind 127.0.0.1:8405
  mode http
  http-request use-service prometheus-exporter
  no log
And I keep internal operational paths, such as statistics and Grafana, handled before the hostname map. These are small details, but ordering matters. Special paths should be explicit and early. The hostname map is for FediMeteo routing, not for every internal tool I happen to expose behind the same proxy.
What this changes in practice
The nice thing about this configuration is that none of its parts is particularly surprising.
The map keeps hostname routing manageable. The backend definitions keep each country isolated and limited. The static homepage avoids dynamic work for something that changes once per hour. The shared avatar gives HAProxy one very hot media object to serve directly. The media cache keeps public files away from snac. The JSON microcache absorbs short ActivityPub bursts. Header cleanup prevents useless variation. Connection reuse avoids unnecessary backend connection churn.
But all of this is only a longer way of saying one thing:
fewer requests reach snac
.
That is the metric I care about here.
Not because snac is slow. If anything, FediMeteo exists in its current form because snac is efficient enough to make this kind of project possible on a very small VPS. But precisely because the whole architecture is small and pleasant, I do not want to waste resources where there is no need.
This is also consistent with the rest of the project. Forecasts are serialized by scripts. Updates happen every six hours. The homepage is regenerated hourly. Countries live in separate jails. Snapshots and backups are handled outside the application. No single component tries to be the entire system.
HAProxy is just another small piece, but it sits in the right place to remove a lot of repeated work.
Caveats
This configuration is not a universal HAProxy recipe for ActivityPub services.
It matches FediMeteo as it is now: almost no media, one shared avatar, static homepage, public forecasts, many small snac instances, and ActivityPub traffic that can benefit from a short public cache when there are no cookies or authorization headers.
If I decide one day to use media in forecasts, the media cache rules will need to be reviewed. If I use different avatars for each city or country, the cache will still work, but I will lose the very nice property of one shared, always-hot avatar. If ActivityPub responses become actor-dependent, public JSON caching must be reconsidered. If one country grows a very different traffic pattern from the others, it may deserve a different limit or policy.
This is why I do not like presenting configurations as magic. A good configuration is a written form of the assumptions behind a service. When the assumptions change, the configuration must change too.
Conclusion
FediMeteo started as a small idea and became larger than I expected, but I still want it to feel small in the right ways. Small does not mean fragile. Small means understandable. It means that each part has a reason to exist, and that unnecessary work is removed before it becomes a problem.
The HAProxy layer follows this idea. It terminates TLS, routes hostnames through a map, reuses backend connections, serves the shared avatar from cache, microcaches public ActivityPub JSON, avoids authenticated and cookie-based traffic, and gives me a small diagnostic header to see what is happening.
There is no single brilliant directive here. There is only the usual work of matching infrastructure to reality.
FediMeteo publishes weather forecasts as text and emoji. The homepage is static HTML updated every hour. The accounts share the same avatar because it is enough, and because it is better for the cache. Each country has its own snac instance in its own FreeBSD jail. HAProxy stands in front of them and tries, quietly, not to bother them unless it has to.
I like this kind of infrastructure.
Not because it is invisible, but because when it works well, it leaves very little to say.
