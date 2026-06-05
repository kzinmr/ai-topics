---
title: "Aggressive caching for a Mastodon reverse proxy: what to cache, what to never cache, and why content negotiation will eventually betray you"
url: "https://it-notes.dragas.net/2026/06/05/aggressive_caching_for_a_mastodon_reverse_proxy/"
fetched_at: 2026-06-05T07:01:41.358443+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# Aggressive caching for a Mastodon reverse proxy: what to cache, what to never cache, and why content negotiation will eventually betray you

Source: https://it-notes.dragas.net/2026/06/05/aggressive_caching_for_a_mastodon_reverse_proxy/

I have written before about putting a cache in front of
snac
, and more recently about
the HAProxy layer in front of FediMeteo
. The general idea is always the same: the reverse proxy should absorb the repetitive, public work that has no business reaching the application server.
This post is the same idea applied to a much louder neighbour: a Mastodon instance. The instance is
mastodon.bsd.cafe
, the proxy is nginx on FreeBSD, and the configuration below is what I am currently running in production.
Mastodon is heavier than snac in every direction. It has Puma and Sidekiq behind it, more endpoints, more streaming, more federation patterns, and one specific characteristic that complicates everything: it serves multiple representations on the same URLs. The same path returns HTML to a browser, ActivityPub JSON to a remote instance, and sometimes plain JSON to an API client. If the proxy treats the URL as one thing, sooner or later it will return the wrong thing to the wrong client.
Most of the work below comes from that single observation.
If I had to summarize this whole post in a single sentence, it would be this:
Mastodon is not a website. It is a website, an API, and an ActivityPub server, all sharing the same URLs.
Everything else in this configuration - cache keys, variants, bypass rules, the diagnostic headers - is decoration around that one fact.
A popular toot from a friend gets boosted. Twenty federated instances ask for the same ActivityPub object within the same second. Browsers fetch the HTML version of the same URL. If the proxy sees only "a URL", it will eventually betray you: a remote instance will receive HTML, a browser will receive ActivityPub JSON, and you will spend an afternoon wondering why your timeline looks broken on three different servers. I have spent that afternoon. I do not recommend it.
Assumptions before anything else
Before any directive, this configuration assumes a few things about the instance. If any of these does not match your setup, the directives still make sense, but you must read the caveats at the end before adapting them.
The first assumption is that
AUTHORIZED_FETCH
(secure mode) is disabled. With secure mode off, all ActivityPub GET responses cached at the proxy layer are public and identical regardless of the requesting actor. With secure mode on, Mastodon can legitimately return different bodies depending on which remote actor is asking, and caching them blindly at the proxy becomes at best wasteful, at worst a cache-poisoning surface.
This is not a hypothetical.
CVE-2026-25540
, fixed in Mastodon 4.3.19, 4.4.13, and 4.5.6, is exactly this kind of mistake, but inside Mastodon's own
Rails.cache
: the pinned posts and featured hashtags endpoints had actor-dependent ActivityPub responses but were keyed without the actor. The CVE does not directly apply to nginx caches, but the underlying lesson does. Do not cache what depends on the caller unless the caller is part of the cache key. Keep this rule in mind every time you are tempted to cache a federation endpoint "just in case".
The second assumption is that no signed-URL storage backend sits behind
/system/
or
/media_proxy/
. If those paths ever redirect to short-lived presigned S3 or SeaweedFS URLs, my TTLs below are too long: nginx will happily cache a redirect to a URL that has already expired.
The third assumption is that federation traffic uses HTTP Signatures, not the HTTP
Authorization
header. Mastodon signs federated GETs with the
Signature
header. The
Authorization
-based skip-cache rule further down catches API tokens, not signed federation traffic. If you enable
AUTHORIZED_FETCH
, you must add an explicit skip rule for
$http_signature
.
I am being deliberate about these assumptions because the configuration that follows is internally consistent only as long as they hold.
The proxy in front of
mastodon.bsd.cafe
has three jobs:
TLS termination, microcaching of expensive endpoints (especially federation-heavy collections and default public routes), and long-lived caching of immutable assets and user media.
The point is not to replace Mastodon's internal Rails cache. The point is to absorb spiky federation traffic and repetitive asset fetches that would otherwise hit Puma and Rails for every single request.
The strategy is deliberately layered: very long TTL on fingerprinted assets, medium TTL on user-uploaded media, very short microcache on dynamic pages and federation endpoints that get hammered, and explicit bypass rules for anything private, authenticated, actor-dependent, or otherwise unsafe.
Every cacheable layer is keyed correctly for content negotiation. That is the part that matters most.
The cache zone
A single cache zone is shared across all Mastodon locations:
proxy_cache_path /var/cache/nginx/mastodon
                 levels=1:2
                 keys_zone=mastodon_cache:200m
                 max_size=20g
                 inactive=24h
                 use_temp_path=off;
200m
of keys zone holds metadata for roughly 1.6 million entries in RAM. The body can grow up to
20g
on disk. The two numbers are independent: keys live in shared memory, bodies live on the filesystem, and the cache key is what links them.
inactive=24h
evicts anything not requested for a day, even if there is free space. This is intentional. I do not want a long, cold tail of stale entries to squat in the cache forever. I want the working set to remain hot, and I want the rest to fade.
use_temp_path=off
is small but important. By default nginx writes a cached response to a temporary file and then renames it into place. If the temp path and cache path are on different filesystems, that cheap rename becomes a real copy. Setting
use_temp_path=off
puts temporary files directly under the cache directory and avoids that trap. It is the kind of detail nobody mentions until something is suspiciously slow.
Of all the maps in this configuration, only one really earns its place. This one:
map $http_accept $mastodon_cache_variant {
    default                          "default";
    "~*application/activity\+json"   "activitypub";
    "~*application/ld\+json"         "activitypub";
    "~*application/json"             "json";
    "~*text/html"                    "html";
}
Mastodon serves the same URL with different bodies depending on the
Accept
header. A status URL like
/@user/123456789
returns rendered HTML to a browser and an ActivityPub object to another federated instance. If you cache by URL alone, the first request that comes in wins and the next request receives the wrong content type. Instances start federating HTML, browsers start downloading JSON, and the failure is subtle enough to waste hours.
The map normalizes
Accept
into four buckets -
activitypub
,
json
,
html
, and
default
- and the result is folded into the cache key in every location that does content negotiation:
proxy_cache_key "$scheme$host$request_uri|accept=$mastodon_cache_variant";
Coalescing equivalent MIME types is intentional.
application/activity+json
and
application/ld+json
both map to
activitypub
, because splitting them across two cache buckets would fragment the cache for no useful operational gain.
A subtle point I want to be explicit about: I do not include
$request_method
in the cache key. nginx already converts
HEAD
into
GET
for caching purposes by default, which is what I want here. A
HEAD
request on
/@user/123
should hit the same cache entry as a
GET
request on the same URL. Adding the method would only separate them for no benefit.
During rollout I also expose the selected variant as a response header:
add_header X-Cache-Variant $mastodon_cache_variant always;
The header is there to verify the behaviour in production. It can come off once the configuration has proved itself, but I tend to leave it on. A cache that works should be visible. A cache that is invisible can be correct, but it can also be silently wrong, and I would rather know.
This is the first real gotcha, and I want to spend a moment on it because it caught me out the first time I configured a similar setup.
nginx honors the upstream
Vary
response header in addition to
proxy_cache_key
. If Mastodon emits
Vary: Accept
, or worse,
Vary: Accept, Cookie, ...
, my carefully normalized variant key gets paired with nginx's native Vary handling. The result is that the cache may still fragment on the full, un-normalized
Accept
header - which defeats the entire point of the variant map.
There is another, very specific failure mode on older or unpatched nginx builds. nginx stores the
Vary
value in a fixed-size cache metadata field. Historically that field was 42 bytes, which is famously short and almost charmingly suspicious of being a Douglas Adams reference. Modern nginx raised the limit to 128 bytes, which is enough for the common cases but still surprisingly small. If your upstream emits a long
Vary
header, anything beyond the limit is treated as
Vary: *
, which means the response is not cached at all. The only signal you get is a critical line in the error log, and unless you are looking for it, you will not see it.
The operational lesson is the same in both cases: if you rely on your own normalized variant key, do not assume upstream
Vary
is harmless. Check your nginx version, check your error log, and verify cache behaviour via
X-Cache-Status
and
X-Cache-Variant
.
On the locations where the variant map is the cache dimension I care about, I take responsibility explicitly:
proxy_ignore_headers Vary;
This tells nginx to stop using upstream
Vary
to protect me. That is fine only if my own cache key and request normalization cover every response dimension that matters. In particular, I make sure the backend is not also varying on
Accept-Encoding
in a way that would create compressed and uncompressed variants behind my back. The cleanest way to avoid that is not to forward
Accept-Encoding
to the backend at all, and let frontend nginx handle compression itself:
proxy_set_header Accept-Encoding "";
This is the kind of decision I prefer to be explicit about. Ignoring
Vary
is not magic. It is a responsibility, and it should be paired with the rules that take its place.
Rather than build one giant boolean to decide what bypasses cache, I prefer to decompose the logic into small orthogonal maps. Each map is
1
when caching must be skipped, and the final decision is an OR of all of them.
map $request_method $skip_cache_method {
    default 1;
    GET     0;
    HEAD    0;
}

map $http_authorization $skip_cache_auth {
    default 1;
    ""      0;
}

map $http_cookie $skip_cache_cookie {
    default 1;
    ""      0;
}

map $uri $skip_cache_uri {
    default                  0;
    ~^/auth                  1;
    ~^/oauth                 1;
    ~^/settings              1;
    ~^/admin                 1;
    ~^/api/v1/custom_emojis$ 0;
    ~^/api/v1/instance$      0;
    ~^/api/v2/instance$      0;
    ~^/api/v1/trends/tags$   0;
    ~^/api/oembed$           0;
    ~^/api/                  1;
}
The reasoning is straightforward. Only
GET
and
HEAD
are cacheable; everything else, including
POST
,
DELETE
,
PUT
, and ActivityPub deliveries, must pass through. Any request carrying an
Authorization
header is an API call with a token, and those are never public. Any request with a cookie is potentially logged-in traffic, and caching logged-in pages would leak personal timelines across users. Auth flows, settings, admin, and most of the API bypass the cache by URI, while a small, carefully chosen set of slow-changing public API endpoints is allowed through.
The important caveat I want to underline: the
Authorization
map does
not
catch signed federated GETs. Mastodon federation uses HTTP Signatures, which means the relevant request header is
Signature
. If
AUTHORIZED_FETCH
is enabled, you must add a parallel map:
map $http_signature $skip_cache_signature {
    default 1;
    ""      0;
}
and then include it in both
proxy_cache_bypass
and
proxy_no_cache
. Do this before enabling secure mode, not after.
The maps are used together in each cacheable location:
proxy_cache_bypass $skip_cache_method $skip_cache_auth $skip_cache_cookie $skip_cache_uri;
proxy_no_cache     $skip_cache_method $skip_cache_auth $skip_cache_cookie $skip_cache_uri;
Both directives are necessary.
proxy_cache_bypass
means "do not read from cache for this request".
proxy_no_cache
means "do not write this response to cache". Without
proxy_no_cache
, a logged-in user's response could still poison the anonymous cache. Without
proxy_cache_bypass
, a request that should have gone straight to the backend might still receive a cached anonymous response. I keep both, every time.
Most locations share a common proxy baseline. There is nothing clever here, but if any of these lines is missing the rest of the configuration quietly does less than expected.
proxy_http_version 1.1;
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
proxy_set_header X-Forwarded-Proto $scheme;
proxy_set_header Connection "";
proxy_set_header Accept-Encoding "";
proxy_http_version 1.1
and
proxy_set_header Connection ""
matter for upstream keepalive. Without them, nginx may use HTTP/1.0 semantics upstream and send
Connection: close
on every request, which makes the
keepalive
directive on the upstream block far less useful than it looks.
proxy_set_header Accept-Encoding ""
keeps backend responses uncompressed so nginx can cache a single representation and handle client-facing compression itself. It also prevents accidental cache fragmentation through
Vary: Accept-Encoding
, which would otherwise creep in despite the variant map.
These settings are not exciting, and they should not be. The interesting parts of an infrastructure are not always the parts that should be unusual.
The Mastodon
server
block in my configuration ends up with seven distinct request profiles. Six of them cache; one explicitly does not, because streaming is not a cacheable workload.
I do not group them under one
location /
with a giant
if
block. I prefer to keep each profile in its own location, even if some of them look similar. When something goes wrong in production, I want to be able to point at one location and reason about it without holding the rest of the configuration in my head.
location ~ ^/(assets|packs|emoji)/ {
    proxy_cache mastodon_cache;
    proxy_cache_key "$scheme$host$request_uri";
    proxy_ignore_headers Vary;

    proxy_cache_valid 200 301 302 7d;
    proxy_cache_valid 404 10m;

    proxy_cache_lock on;
    proxy_cache_use_stale error timeout updating http_500 http_502 http_503 http_504;
    proxy_cache_background_update on;

    proxy_cache_bypass $skip_cache_method $skip_cache_auth $skip_cache_cookie $skip_cache_uri;
    proxy_no_cache     $skip_cache_method $skip_cache_auth $skip_cache_cookie $skip_cache_uri;

    proxy_pass http://$custom_upstream;
}
These paths are content-addressed. Webpack fingerprints filenames with hashes, so a new deploy publishes new URLs while the old URLs remain valid. A 7-day TTL is safe because
/packs/js/common-abc123.js
will never become different content under the same URL. If it does, it has a new URL.
404s get a short 10-minute TTL so a temporarily missing asset can recover quickly.
proxy_cache_lock on
is the thundering-herd guard. When a popular asset is not cached and ten clients ask for it at once, nine wait for the first request to populate the cache instead of all ten hammering the backend. I like this directive a lot. It is the kind of small switch that quietly removes a class of problems.
proxy_cache_use_stale
together with
proxy_cache_background_update
is the stale-while-revalidate pattern. If an entry has expired but Mastodon is slow or briefly down, nginx can serve the stale copy and refresh it asynchronously. For static assets this is almost always the right trade-off. The asset has not actually changed under the same URL, and a few extra hours of stale data hurt nobody.
location ~ ^/system/(accounts/avatars|media_attachments/files|custom_emojis/images)/ {
    proxy_cache mastodon_cache;
    proxy_cache_key "$scheme$host$request_uri";
    proxy_ignore_headers Vary;

    proxy_cache_valid 200 302 6h;
    proxy_cache_valid 404 5m;

    proxy_cache_lock on;
    proxy_cache_use_stale error timeout updating http_500 http_502 http_503 http_504;
    proxy_cache_background_update on;

    proxy_cache_bypass $skip_cache_method $skip_cache_auth $skip_cache_cookie $skip_cache_uri;
    proxy_no_cache     $skip_cache_method $skip_cache_auth $skip_cache_cookie $skip_cache_uri;

    proxy_pass http://$custom_upstream;
}
Avatars, attachment thumbnails, and custom emoji are also effectively content-addressed, because the file path contains an ID. They can still be replaced or deleted, so the TTL is more conservative than for assets: six hours instead of seven days.
The 302 status is also cached, because Mastodon may redirect to another storage location, and the redirect is usually stable enough to cache for hours.
This is also where the caveat about signed URLs really matters. If you ever put a signed-URL backend behind
/system/
, this TTL must be shorter than the signed URL lifetime, or nginx will eventually serve a redirect to a URL that no longer works. On
mastodon.bsd.cafe
I do not use signed URLs, so six hours is fine.
location ~ ^/(users|ap/users)/[^/]+/statuses/[0-9]+/replies {
    proxy_cache mastodon_cache;
    proxy_cache_key "$scheme$host$request_uri|accept=$mastodon_cache_variant";
    proxy_ignore_headers Vary;

    proxy_cache_valid 200 30s;
    proxy_cache_valid 404 10s;

    proxy_cache_lock on;
    proxy_cache_lock_timeout 1s;
    proxy_cache_lock_age 5s;

    proxy_cache_bypass $skip_cache_method $skip_cache_auth $skip_cache_cookie $skip_cache_uri;
    proxy_no_cache     $skip_cache_method $skip_cache_auth $skip_cache_cookie $skip_cache_uri;

    proxy_pass http://$custom_upstream;
}
This is the location I tuned most carefully. When a status starts going viral, dozens of federated instances poll
/replies
to build their thread view, often within the same second. The same URL must serve an HTML thread view to browsers and an ActivityPub
OrderedCollection
to remote instances, so the variant key is essential here.
A 30-second microcache absorbs the spike without serving meaningfully stale data. A reply that appears 30 seconds late in a federated thread is usually invisible to humans, while the backend relief is very visible.
The lock settings keep backend load and latency bounded.
proxy_cache_lock_timeout 1s
bounds how long queued requests wait behind the lock. If the timeout expires, they go to the upstream directly, but their responses are not stored in the cache, which prevents a runaway thundering herd from clogging the cache fill path.
proxy_cache_lock_age 5s
prevents one slow cache-populating request from monopolizing the fill path forever; if the request holding the lock has not completed after 5 seconds, nginx may let another request reach the upstream to retry.
I have currently left
proxy_cache_use_stale
off on this location while I am still validating the deployment. This is a deliberate debugging stance, not a permanent choice. Stale-while-revalidate is useful in production, but during rollout it can hide upstream issues while I am trying to understand the system. Once the behaviour is stable, the production version will be:
proxy_cache_use_stale error timeout updating http_500 http_502 http_503 http_504;
proxy_cache_background_update on;
location ^~ /media_proxy/ {
    proxy_cache mastodon_cache;
    proxy_cache_key "$scheme$host$request_uri";

    proxy_cache_valid 200 10m;
    proxy_cache_valid 301 302 10m;
    proxy_cache_valid 404 1m;

    proxy_ignore_headers Cache-Control Expires Vary;

    proxy_cache_lock on;
    proxy_cache_use_stale error timeout updating http_500 http_502 http_503 http_504;
    proxy_cache_background_update on;

    proxy_cache_bypass $skip_cache_method $skip_cache_auth $skip_cache_cookie $skip_cache_uri;
    proxy_no_cache     $skip_cache_method $skip_cache_auth $skip_cache_cookie $skip_cache_uri;

    proxy_pass http://$custom_upstream;
}
Mastodon's
/media_proxy/
fetches remote media so clients do not leak their IP address to remote servers. The response is the same regardless of
Accept
, so the cache key intentionally omits the variant. Splitting media proxy responses across
html
,
json
,
activitypub
, and
default
buckets would only waste storage.
proxy_ignore_headers Cache-Control Expires Vary
is deliberate here. Mastodon may emit conservative cache headers, or none at all, and I want the proxy to enforce a short local 10-minute policy regardless of what the backend says.
Set-Cookie
is not in the ignore list. nginx's default refusal to cache responses carrying
Set-Cookie
still applies, and I want it to. It is a safety net I do not want to disable just to win a few cache hits.
The
^~
prefix is a small useful detail. Once this location matches, nginx stops evaluating regex locations. Media proxy traffic can be heavy, and skipping further regex matching is a tiny but free win.
location ~ ^/(users|ap/users)/[^/]+/(followers|following) {
    proxy_pass http://$custom_upstream;
}
This one is a pure proxy, no cache. I want to be explicit that this is a decision, not an omission.
/users/<name>/followers
and
/users/<name>/following
are pagination-heavy, change frequently as people follow and unfollow, and are queried by federation crawlers in ways that would make the cache key proliferate through pages and cursors. The likely hit ratio is poor, the risk of serving stale social graph data is non-trivial, and the cost of caching them - in storage and in mental overhead - is not worth it.
If a remote instance starts hammering these endpoints, the right answer is rate limiting with
limit_req_zone
, not retrofitting cache as a rate limiter.
Default location: the microcache and streaming without cache
location / {
    proxy_cache mastodon_cache;
    proxy_cache_key "$scheme$host$request_uri|accept=$mastodon_cache_variant";
    proxy_ignore_headers Vary;

    proxy_cache_valid 200 10s;
    proxy_cache_valid 301 302 1m;
    proxy_cache_valid 404 10s;

    proxy_cache_lock on;
    proxy_cache_lock_timeout 5s;

    proxy_cache_bypass $skip_cache_method $skip_cache_auth $skip_cache_cookie $skip_cache_uri;
    proxy_no_cache     $skip_cache_method $skip_cache_auth $skip_cache_cookie $skip_cache_uri;

    proxy_next_upstream error timeout http_502 http_503 http_504;
    proxy_next_upstream_tries 2;

    proxy_pass http://$custom_upstream;
}
Everything not matched by a more specific location falls here: profiles, individual statuses, the about page, the public timeline, and many ActivityPub object fetches.
The TTL is only 10 seconds for 200 responses. That is enough to deduplicate the wave of requests when a popular toot gets boosted or linked from elsewhere, without making the page feel stale to a human visitor.
It is worth being honest that short TTLs still cost CPU. A 10-second microcache on a sustained-traffic URL means the backend regenerates the entry six times per minute. That is vastly better than serving every request from Rails, but it is not free. If your backend cannot comfortably handle that, raise the TTL, or enable stale-while-revalidate on these dynamic paths.
proxy_next_upstream
with
proxy_next_upstream_tries 2
is the failover trigger. If the primary returns 502, 503, 504, or times out, nginx retries on the backup. The chain is capped at two attempts so a sick upstream cannot hold the request indefinitely.
At the
http
level:
map $http_upgrade $connection_upgrade {
    default upgrade;
    ""      close;
}
In the server block:
location /api/v1/streaming {
    proxy_buffering off;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection $connection_upgrade;
    proxy_read_timeout 3600s;
    proxy_send_timeout 3600s;
    proxy_pass http://$custom_upstream;
}
Streaming is a WebSocket and SSE-style endpoint. Buffering must be off, otherwise the proxy may hold messages while waiting for buffers to fill. The
Upgrade
and
Connection
headers are driven by
$connection_upgrade
, which is
upgrade
only when the client actually sent an
Upgrade
header. That way a non-WebSocket request to the same path does not get its
Connection
header mangled.
The hour-long read and send timeouts allow long-lived streams to stay open through quiet periods.
There is no cache here. Streaming is not a cacheable workload, and trying to make it one is one of those ideas that sounds clever for about thirty seconds.
Upstream and failover
upstream mastodonbsdcafe {
    server 192.168.123.33  max_fails=3 fail_timeout=30s;
    server 192.168.122.133 backup;
    keepalive 64;
}
The primary backend is on another VPS; the backup is in a jail next to the reverse proxy. After three consecutive failures, the primary is marked down for 30 seconds. Traffic flips to the backup, then nginx retries the primary after the window.
keepalive 64
holds up to 64 idle TCP connections to the upstream per worker. On a busy instance, this saves real handshake overhead, but only if the proxied connection can actually stay open. That is why the shared proxy settings include
proxy_http_version 1.1
and
proxy_set_header Connection ""
. Without those, upstream keepalive does much less than it looks like it should.
I also use an indirection layer:
map $remote_addr $custom_upstream {
    default mastodonbsdcafe;
}
Today everything defaults to the main upstream group. The map exists so that specific client IPs can be pinned to a specific upstream when I am debugging, or so an admin connection can be routed to the backup while the primary is being tested. It costs nothing to have it sitting there, and it has saved me time more than once.
What I log and why
log_format detailed '$remote_addr - $remote_user [$time_local] '
                    '"$request" $status $body_bytes_sent '
                    '"$http_referer" "$http_user_agent" '
                    'rt=$request_time '
                    'uct=$upstream_connect_time '
                    'uht=$upstream_header_time '
                    'urt=$upstream_response_time '
                    'us=$upstream_status '
                    'ua=$upstream_addr '
                    'cache=$upstream_cache_status '
                    'variant=$mastodon_cache_variant';

access_log /var/log/nginx/access.mastodon.bsd.cafe.log detailed;

add_header X-Cache-Status  $upstream_cache_status always;
add_header X-Cache-Variant $mastodon_cache_variant always;
This log format is purpose-built for the cache layer. For each request it records total request time, upstream connect time, upstream header time, upstream response time, upstream status, which backend served the request, cache status, and which content-negotiation variant was selected.
The cache status is one of the values nginx exposes through
$upstream_cache_status
:
HIT
,
MISS
,
BYPASS
,
EXPIRED
,
STALE
,
UPDATING
, or
REVALIDATED
. The response headers expose the same information to the client, which makes it trivial to verify behaviour with
curl -I
or browser dev tools.
The
always
qualifier matters. Without it, nginx only adds these headers to a subset of responses, so a 502 from the backend might arrive without the diagnostic headers you need most. I want them on every response, no exceptions.
There is also a small operational detail I find pleasant: a custom 502 page.
error_page 502 /502.html;
location = /502.html {
    root /usr/local/www/mastodon_errors;
    internal;
}
It is not part of the cache strategy, but it makes backend hiccups less ugly. And I block some abusive user agents with
444
, which closes the connection without sending any response at all:
if ($http_user_agent ~* "bytespider") {
    return 444;
}
This is not a general bot strategy. It is just a cheap refusal path for traffic I know I do not want.
How I check it actually works
A configuration that I cannot verify is a configuration I do not trust. Here is the short set of commands I keep in a paste buffer for this proxy.
The first verification is variant separation. Three requests to the same URL with different
Accept
headers should produce three independent cache entries:
for v in 'text/html' \
         'application/activity+json' \
         'application/ld+json; profile="https://www.w3.org/ns/activitystreams"'; do
  printf '%-75s -> ' "$v"
  curl -s -o /dev/null -D - -H "Accept: $v" \
    https://mastodon.bsd.cafe/@someuser/123456789 \
    | awk '/^[Xx]-[Cc]ache/ { printf "%s ", $0 } END { print "" }'
done
On the first pass, every variant should be a
MISS
. On the second pass, every variant should be a
HIT
, with
X-Cache-Variant
showing the expected bucket.
The second verification is that cookies and
Authorization
always trigger
BYPASS
:
curl -I -H 'Cookie: _mastodon_session=test' \
  https://mastodon.bsd.cafe/@someuser

curl -I -H 'Authorization: Bearer fake' \
  https://mastodon.bsd.cafe/api/v1/timelines/home
Both should return
X-Cache-Status: BYPASS
. If they do not, the skip-cache rules are wrong, and the entire setup is unsafe.
If you intend to enable
AUTHORIZED_FETCH
, the third verification is for signed GETs. A quick synthetic check that the nginx map fires correctly:
curl -I -H 'Signature: fake' \
       -H 'Accept: application/activity+json' \
       https://mastodon.bsd.cafe/users/someuser
If you added
$skip_cache_signature
, the result should be
X-Cache-Status: BYPASS
.
Finally, the logs themselves tell me how the cache is performing in production. Cache status distribution:
awk '{
  for (i = 1; i <= NF; i++)
    if ($i ~ /^cache=/) c[$i]++
}
END {
  for (k in c) print k, c[k]
}' /var/log/nginx/access.mastodon.bsd.cafe.log
A healthy instance shows
cache=HIT
and
cache=BYPASS
doing most of the work, with
cache=MISS
accounting for cold paths and short-TTL refreshes. The same trick works for the variant distribution:
awk '{
  for (i = 1; i <= NF; i++)
    if ($i ~ /^variant=/) v[$i]++
}
END {
  for (k in v) print k, v[k]
}' /var/log/nginx/access.mastodon.bsd.cafe.log
This tells me what my traffic actually looks like. A federation-heavy instance shows a lot of
activitypub
. An instance with many human visitors shows more
html
. On
mastodon.bsd.cafe
the balance shifts depending on what is happening in the wider Fediverse on any given day.
Caveats worth being honest about
I do not like presenting configurations as magic, so I want to be explicit about the conditions under which this one is appropriate.
Short TTLs cost CPU. A 10-second microcache on a sustained-traffic URL means six backend regenerations per minute. That is much better than no cache, but it is not free. If the backend cannot comfortably handle that, raise the TTL or enable stale-while-revalidate on the dynamic paths.
Dynamic stale-while-revalidate is powerful but it hides problems. I currently keep
proxy_cache_use_stale
off on the dynamic locations because I am still validating behaviour. In steady-state production, stale-while-revalidate is usually the right choice. During rollout, it can quietly hide upstream errors and make debugging harder. Be honest with yourself about which mode you are in.
AUTHORIZED_FETCH
changes the threat model. With secure mode disabled, public ActivityPub GET responses are safe to cache as public content, provided your cache key handles content negotiation correctly. With secure mode enabled, ActivityPub responses can become actor-dependent. At that point you must either bypass cache for signed GETs or include the signing actor in the key. The latter usually destroys the hit ratio, so bypassing is the practical answer.
The variant map is a compromise. It covers
application/activity+json
,
application/ld+json
,
application/json
, and
text/html
. Everything else falls into the
default
bucket. That is intentional, but the default bucket is still a bucket. If you discover a real client type that matters on your instance, add it explicitly.
Ignoring
Vary
is a responsibility.
proxy_ignore_headers Vary
is not magic; it tells nginx to stop protecting you based on upstream
Vary
. That is fine only if your own cache key and request normalization cover every dimension
Vary
was protecting. For this configuration that means normalizing
Accept
into a variant, avoiding backend
Accept-Encoding
variation, never caching cookies or authorization, and never caching signed GETs if secure mode is enabled.
Followers and following are uncached on purpose. They are pagination-heavy and change frequently. Caching them would create many low-value entries with questionable freshness. If a remote instance hammers these endpoints, use
limit_req_zone
. Do not retrofit cache as a rate limiter.
Signed-URL redirects require shorter TTLs. Caching 302s is useful when redirects are stable. It is dangerous when redirects point to short-lived signed URLs. If your media storage returns presigned URLs, your nginx redirect TTL must be shorter than the URL lifetime.
Set-Cookie
must remain special. Do not add
Set-Cookie
to
proxy_ignore_headers
unless you are absolutely sure the location cannot produce user-specific responses. nginx's default refusal to cache
Set-Cookie
responses is a safety net. Keep it.
A good configuration is a written form of the assumptions behind a service. When the assumptions change, the configuration must change too.
There is no single brilliant directive in this configuration. The trick is combining long TTLs for immutable assets, medium TTLs for media, tiny TTLs for dynamic public pages, cache locking for thundering-herd protection, strict bypass rules for private or actor-dependent traffic, a normalized content-negotiation key, and enough logging to prove the system is doing what I think it is.
What this layer buys me, in one sentence: fewer requests reach Puma and Rails.
That is the metric I care about. Mastodon is not slow, but it is heavy, and the bigger the instance grows the more it benefits from a layer in front that quietly absorbs the work that does not need to be done by the application. A reverse proxy that caches Mastodon safely has to remember, with every request, that the same URL might mean three different things to three different clients. Once it does, even a very short microcache can remove a surprising amount of load without changing the user-visible behaviour of the instance.
