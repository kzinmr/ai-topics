---
title: "Package Manager CWEs"
url: "https://nesbitt.io/2026/05/04/package-manager-cwes.html"
fetched_at: 2026-05-05T07:00:56.078347+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# Package Manager CWEs

Source: https://nesbitt.io/2026/05/04/package-manager-cwes.html

I went through every public CVE and security advisory I could find that was filed against a package manager itself. Clients and registries both: language package managers, system package managers, self-hosted registry servers, the lot.
The same dozen or so failure modes appear independently in tool after tool, often years apart, because the people building package manager number nineteen don’t always know what bit package managers one through eighteen. If you’re building or maintaining one of these things, this is the list of places to look. I’ve deliberately not organised it by tool. Most of these were fixed quickly, several were found by the projects themselves, and which project hit which bug matters much less than the pattern.
One caveat. CVE counts measure what got reported and assigned an ID, which is a different thing from risk. Some projects run bug bounties and file a CVE for every ANSI escape. Others fix things in a point release with a changelog line. And the design-level weaknesses where most real-world compromise actually happens (install scripts running as the user, trust carrying across maintainer changes, first-come namespaces) are out of scope here precisely because they never get CVEs. That’s a separate post.
Client
CWE-22 (path traversal), with CWE-59 (link following) for the symlink variants. The single most common entry in the dataset by raw count, and it has been recurring for twenty years. A package archive contains a path with
../
in it, or a symlink pointing outside the extraction root, or a Windows-style backslash separator that the path-sanitising code doesn’t recognise, and the installer writes a file wherever the archive author wanted.
The 2018
Zip Slip
research found this across most ecosystems at once, but it had been hitting them individually long before (
CVE-2007-0469
is the earliest I found in a language package manager) and has kept hitting them since (
CVE-2026-34591
,
CVE-2026-35206
). Fixing the
..
case doesn’t fix the symlink case, fixing the symlink case for tar doesn’t fix it for zip, and fixing it for forward slashes doesn’t fix it for backslashes on Windows. Several tools have three or four CVEs in this category because each fix was partial.
The pattern extends beyond the archive itself. A
bin
field in a manifest that points at
../../../usr/local/bin/something
(
CVE-2019-16775
), a
Content-Disposition
header on a download with
../
in the filename (
CVE-2019-20916
,
CVE-2019-9686
), a chart name or version string with path segments in it (
CVE-2023-35946
). Anywhere a string from a package ends up in a filesystem path.
If you’re building one: extract into a directory and refuse to create anything whose resolved path isn’t under it. Resolve symlinks before checking. Treat every separator the target OS treats as a separator. Apply the same check to every field that becomes a path, not just archive entries.
Argument injection into git, hg, svn, and friends
CWE-88 (argument injection). Nearly every package manager can install from a VCS URL, and nearly every one of them has at some point passed a user-controlled string into
git clone
or
hg clone
in a way that let it be interpreted as an option rather than an argument. A ref of
--upload-pack=payload
, a URL starting with a dash, a branch name with shell metacharacters in it.
Examples:
CVE-2021-29472
,
CVE-2022-36069
,
CVE-2021-43809
,
CVE-2023-5752
,
CVE-2022-24440
. One tool has six separate CVEs in this category across git, hg, and Perforce drivers.
The fix is the
--
separator and an allowlist of which options you actually pass, but the bug keeps reappearing because each VCS backend is written separately and the lesson from the git driver doesn’t transfer to the p4 driver three years later.
A related but distinct cluster is compiler flag injection: a package smuggling
-fplugin=
or arbitrary
LDFLAGS
through to the C compiler at build time. This is mostly a Go pattern (
CVE-2018-6574
,
CVE-2023-29404
,
CVE-2023-39323
) because of how cgo works, but the shape is the same: untrusted strings reaching a subprocess that treats some strings as instructions.
Integrity checks that fail open
CWE-345 (insufficient verification of data authenticity) and CWE-347 (improper verification of cryptographic signature). A missing signature file causes verification to be skipped, or an error from the checker gets treated as success. In other cases the hash is checked on the way into the cache but not on the way out, or dependency verification is on and one code path bypasses it.
CVE-2016-1252
is the canonical example: a clearsigned file parser that under specific conditions let unsigned content through as if it had been signed.
CVE-2022-31156
silently skipped verification when the signature check couldn’t run.
CVE-2012-6088
treated an unparseable signature as a valid one.
CVE-2026-35205
passed plugin verification when the provenance file simply wasn’t there.
The early-2010s version of this was simpler: no TLS, or TLS without certificate checks, or following an HTTPS-to-HTTP redirect (
CVE-2012-2125
,
CVE-2013-1629
,
CVE-2013-0253
). That’s mostly fixed now, though
CVE-2022-46176
(no SSH host key verification on git index clones) shows the equivalent gap can survive on less-examined transports.
If you have a verification step, write the test where the signature is absent, malformed, and valid-but-for-different-content, and make sure all three refuse to install.
Credentials sent to the wrong place
CWE-522 (insufficiently protected credentials). An auth token scoped to one registry gets sent to another, usually via a redirect, a mirror, or a dependency hosted somewhere else.
CVE-2016-3956
sent the bearer token with every request regardless of host.
CVE-2019-15052
followed a redirect and re-sent credentials to the new host.
CVE-2021-32690
sent repository credentials to whatever domain a chart’s dependencies pointed at.
CVE-2021-22568
sent the official-registry OAuth token to any third-party server you published to.
The other half of this category is credentials ending up in logs or published artifacts: passwords embedded in URLs written to the build log (
CVE-2020-15095
), signing passphrases at debug level (
CVE-2020-13165
), workspace ignore files not honoured so secrets get packed into the published tarball (
CVE-2022-29244
).
Credentials should be bound to an origin and stripped on cross-origin redirect, same as a browser would. And anything that builds a publishable artifact needs a test that
.env
doesn’t end up inside it.
Picking the wrong source
CWE-427 (uncontrolled search path element) at the resolver level, also filed as CWE-829 (inclusion of functionality from untrusted control sphere). The dependency confusion family. A private package name also exists on the public registry, the resolver consults both, and “highest version wins” means the public one gets installed. Or a secondary source in the manifest is allowed to satisfy any dependency, not just the ones it was added for.
This was reported against individual tools years before it had a name:
CVE-2013-0334
and
CVE-2016-7954
are the same bug Alex Birsan made famous in 2021.
CVE-2020-36327
and
CVE-2018-20225
are the post-2021 filings, the second disputed by maintainers as documented behaviour.
CVE-2022-21668
is the nastier variant where an
--index-url
hidden in a requirements file comment redirects every subsequent install to an attacker’s index.
There’s a less obvious version where the resolver falls through to the next configured source when one errors or can’t be reached (
CVE-2026-22865
), and a version where something that isn’t a release gets treated as one (
CVE-2022-23773
, branch names that look like version tags).
Every dependency should resolve from exactly one source, and that source should be pinned in the lockfile. If a source is unreachable, fail rather than try the next one.
Local files and directories trusted as config
CWE-426 (untrusted search path) and CWE-427 again. Running the package manager inside an untrusted directory (a fresh clone, a downloaded tarball, a mounted volume) and having it pick up an executable, a config file, or a search path from that directory.
CVE-2021-4435
and
CVE-2021-3115
ran binaries found in the current directory.
CVE-2023-39320
let a
toolchain
directive in the module file point at a binary inside the module.
CVE-2024-24821
loaded a PHP file from the project’s
vendor/
directory into the package manager’s own process.
This overlaps with the “code runs earlier than you expect” problem. The user’s mental model is often that
install
runs code but
status
or
lock
or
audit
doesn’t, and the CVEs land where that model is wrong.
Shared filesystem locations other users can write to
CWE-377 (insecure temporary file) and CWE-276 (incorrect default permissions). Predictable paths under
/tmp
, world-writable cache or install directories, files extracted with the archive’s mode bits instead of the user’s umask. Another local user plants a file before you get there, or modifies one after you’ve put it down.
CVE-2019-3881
,
CVE-2021-29428
, and
CVE-2023-38497
are examples from language package managers. The system package managers have a much longer history here because they run as root: a symlink or hardlink swap between “installer creates the file” and “installer sets its permissions” gives privilege escalation, and the same tool can accumulate several of these over a decade as each fix turns out to be incomplete (
CVE-2017-7500
,
CVE-2021-35937
,
CVE-2021-35939
).
Use per-process temp directories from
mkdtemp
, set permissions at creation time not after, and on the system-package-manager side use fd-relative operations rather than path-based ones so the thing you checked is the thing you modify.
Unsafe deserialisation of manifests
CWE-502 (deserialisation of untrusted data). Package metadata parsed with a YAML or marshalling library that can instantiate arbitrary objects.
CVE-2017-0903
is the well-known one: a gemspec is YAML, the YAML loader was the unsafe variant, and a crafted gem got code execution at parse time before any signature check could run.
CVE-2025-32798
is the same shape with recipe selectors evaluated as Python.
The XML twin is CWE-611 (XML external entity reference). Java-ecosystem manifests are XML, the platform’s default parser resolves external entities, and a
<!DOCTYPE>
in a POM or ivy.xml reads local files off the machine doing the resolve.
CVE-2022-46751
and
CVE-2023-42445
are the same parser-left-on-default bug a year apart in two tools that read the same file format.
Both halves of this category are small in count but high in severity, because they mean code execution or file disclosure from metadata alone, before the user has agreed to install anything. Use the safe-load variant of whatever parser you have, and turn off DTDs and external entities if it’s XML.
Resource exhaustion from crafted packages
CWE-400 (uncontrolled resource consumption) and CWE-1333 (inefficient regular expression complexity). A compressed archive that expands to fill the disk (
CVE-2022-36114
), or a version string or git URL that hits exponential backtracking in a regex (
CVE-2013-4287
,
CVE-2025-8262
).
CVE-2025-55199
is a JSON Schema whose
$ref
chain is deep enough to exhaust memory, and
CVE-2018-1000075
is a tar header with a negative size that loops forever.
Mostly a nuisance on a developer machine, more interesting on a shared CI runner or anything that processes packages automatically. Worth capping extracted size and recursion depth, and linting the regexes that touch package metadata.
CWE-150 (improper neutralisation of escape sequences). Package name, description, or error text from the registry is printed straight to the terminal, ANSI escapes and all. Lets a malicious package rewrite earlier output, hide what was actually installed, or in some terminal emulators do worse. There are at least nine CVEs for this across four ecosystems (
CVE-2017-0899
,
CVE-2021-21303
,
CVE-2025-67746
), plus an HTML-output variant where build-timing reports rendered attacker-controlled feature names without escaping (
CVE-2023-40030
).
Strip control characters from anything that came from a package before it goes to stdout.
Lockfiles and caches that don’t actually pin
No clean CWE; usually filed under CWE-345. The lockfile exists, the user believes installs are reproducible, and some code path ignores it.
CVE-2021-43616
installed even when the lockfile didn’t match the manifest.
CVE-2025-69263
allowed remote dynamic dependencies through a frozen lockfile.
CVE-2019-15608
checked a hash on the way into the cache but not on the way out.
A more recent variant is the parser differential: two tools, or a tool and an auditor, disagree on what’s inside the same archive.
CVE-2023-37478
is a tarball that one installer reads differently from others while matching the same lockfile hash.
CVE-2026-3219
is a file that’s both a tar and a zip depending on which end you read from. The package the security scanner saw isn’t the package that got installed.
Build sandbox escape
CWE-693 (protection mechanism failure). For the minority of tools that try to isolate package builds from the host, the bugs are in the isolation. Passing file descriptors between builds over Unix sockets (
CVE-2024-27297
), privilege dropping that didn’t actually drop on one platform (
CVE-2025-53819
), built-in fetchers that run outside the sandbox the build runs in. The
Homebrew audit
found several in that sandbox too.
This category is small only because most package managers don’t sandbox builds at all. That moves the risk out of the CVE record and into the design, where it’s larger but unnumbered.
Memory corruption in archive parsers
CWE-787 (out-of-bounds write) and friends. Specific to tools written in C with their own ar, tar, cpio, or header parsers. Integer overflows on length fields, off-by-one on magic strings, format string bugs in error paths (
CVE-2020-27350
,
CVE-2014-8118
,
CVE-2015-0860
). About a dozen of these across the system package managers.
Not much to say beyond the obvious: if you can use a memory-safe language or a well-fuzzed library for the archive layer, do.
Registry
The disclosure record on the registry side is lopsided. Self-hosted registry servers (Nexus, Artifactory, Harbor, Verdaccio, NuGet Gallery) are shipped software, so their bugs get CVE IDs. The big hosted registries are services, so their bugs mostly get a blog post if anything. I’ve leaned on incident writeups, audit reports, and HackerOne disclosures alongside the CVE record here.
Publishing or replacing someone else’s package
CWE-285 (improper authorisation) and CWE-863 (incorrect authorisation). The registry-side bug that matters most, because it turns directly into a supply-chain compromise without anyone’s account being touched.
CVE-2022-29176
was a name-parsing edge case that let you yank and replace any package whose name contained a dash, and
CVE-2022-29218
let you overwrite the platform-specific variant of someone else’s release in the CDN by exploiting upload ordering. In
CVE-2024-38368
a migration had left an orphaned-ownership API in place for a decade and anyone could claim 1,800 packages. One registry had a microservice authorisation gap that let anyone publish a new version of any package,
reported
and fixed without a CVE.
The self-hosted registries have a parallel set where the role check tests the wrong object: a maintainer can edit project metadata reserved for admins (
CVE-2024-22278
), self-registration accepts an
admin: true
field from the request body (
CVE-2019-16097
), a low-privilege user can reach an endpoint that confers admin (
CVE-2024-4142
).
The publish, yank, and transfer-ownership endpoints are the ones to threat-model hardest. Every input to “which package is this acting on” is attacker-controlled.
Account takeover via the recovery path
CWE-287 (improper authentication), but the practical version is rarely a bug in the login form. It’s that the maintainer’s email domain expired, someone registered it, requested a password reset, and published. This has happened on at least three major registries (
the
ctx
incident
is the documented one) and is listed as an open threat in
npm’s own model
. The credential-stuffing variant has also worked: a
2017 sweep
found reused passwords gave publish access to about 14% of one registry by download weight, and a
2023 incident
hijacked fourteen packages the same way.
The actual code bugs in this category are about token hygiene. One registry was generating tokens with a non-cryptographic RNG and storing them unhashed (
2020 crates.io advisory
).
CVE-2019-9733
let an
X-Forwarded-For: 127.0.0.1
header bypass a localhost-only admin account check.
CVE-2024-38367
was a session-validation link that an attacker could get clicked zero-touch by the victim’s mail scanner, and
CVE-2024-22244
a loose OAuth
redirect_uri
check that sent the authorisation code to whatever host the attacker put in the link.
Registries are in a position to detect the domain-expiry case before an attacker does, and several now do. Mandatory 2FA on publish closes most of the rest, as long as the API tokens that bypass 2FA are actually scoped.
Stored XSS in rendered package pages
CWE-79 (cross-site scripting). The registry renders a README, a description, a homepage link, or a profile field that came from a package upload, and the sanitiser misses something.
javascript:
URIs in markdown autolinks (
CVE-2024-37304
), HTML attribute handling in rendered descriptions (
CVE-2024-47604
), README content not sanitised before rendering (
GHSA-78j5-gcmf-vqc8
). The self-hosted registries have a long tail of these.
On a registry this is higher stakes than the average web XSS, because the victim is logged in as someone with publish rights and the page they’re viewing was put there by someone who wants those rights. Render package-supplied content with a real sanitiser and a CSP that assumes the sanitiser will eventually miss one.
CWE-94 (code injection), and often literally the same bug as the client. Registries parse manifests and clone repositories using the same code the client uses, so a YAML deserialisation bug in the gem library is
RCE on the registry
as well as on developer machines, and an argument injection in the Composer hg driver is
command execution on packagist.org
as well as locally.
CVE-2024-38366
is a registry shelling out during email validation. The 2021
CocoaPods trunk RCE
is
git ls-remote
argument injection again, server-side.
If you maintain both a client and a registry, every client-side parsing or VCS bug above is worth checking on the server too. The registry is the higher-value target and it processes the same untrusted input.
SSRF via repository URLs and webhooks
CWE-918 (server-side request forgery). The registry fetches a URL the user provided, and that URL points at the metadata service, an internal admin port, or another tenant’s endpoint. A “test webhook” button that lets a project admin port-scan the internal network (
CVE-2020-13788
), a remote-repository configuration that the server fetches on the user’s behalf (
CVE-2022-27907
), an XXE in an uploaded XML config that reaches internal hosts (
CVE-2020-29436
). The self-hosted registries cluster here because they’re the ones running inside corporate networks where SSRF reaches something interesting.
Outbound fetches from user-supplied URLs need an allowlist, a DNS-rebinding check, and a block on private address ranges.
IDOR on admin and settings endpoints
CWE-639 (insecure direct object reference). The request says which project, package, webhook, or robot account to act on, and the server checks that you’re allowed to perform the action but not that you own the object. One self-hosted registry had five of these reported in a single batch covering webhook policies, robot accounts, tag-immutability rules, retention policies, and job logs (
CVE-2022-31666
through CVE-2022-31671). Others have leaked the full repository list to any authenticated user (
CVE-2021-46270
) or the system proxy config (
CVE-2024-3505
).
These concentrate in the multi-tenant self-hosted registries where one server holds many organisations’ packages. Every handler that takes an object ID needs to check ownership, including the read-only ones.
Tokens that grant more than they say
CWE-863 again. An “upload-only” API token that turns out to be session-equivalent if sent as a header (
PyPI 2020 disclosure
). A read-only key that can be exchanged for a full-scope OAuth token (
CVE-2026-21621
). Automation tokens that bypass 2FA by design and can’t be narrowed to a single package.
Publish tokens are what attackers exfiltrate from CI, so the scope printed on the token needs to be the scope the server enforces, and there should be no exchange path from a narrow token to a wide one.
The registry and the client disagree
No clean CWE. The registry stores and displays one set of metadata, the client installs based on another, and an attacker arranges for them to differ. The 2023
npm manifest confusion
report is the named example: the publish API accepted a manifest independently of the
package.json
inside the tarball, so the website, audit tools, and
npm install
could each see a different dependency list. The Go proxy variant is temporal rather than spatial: the proxy
caches the first version of a module path it sees
and keeps serving it after the source repository has been cleaned up.
This one is about having a single source of truth for what a package contains and making sure every consumer reads from it.
Across roughly two hundred advisories that’s more or less the full set of shapes. Twelve patterns on the client, eight on the registry, and almost every tool in the survey has entries under at least half of them. The cheapest thing a package manager project can do for its own security is subscribe to the advisory feeds of five or six others, because the bug filed against someone else’s tar extractor this month is a decent description of the bug in yours.
