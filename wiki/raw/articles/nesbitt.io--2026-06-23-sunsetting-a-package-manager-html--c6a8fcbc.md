---
title: "Sunsetting a Package Manager"
url: "https://nesbitt.io/2026/06/23/sunsetting-a-package-manager.html"
fetched_at: 2026-06-24T07:01:00.489505+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# Sunsetting a Package Manager

Source: https://nesbitt.io/2026/06/23/sunsetting-a-package-manager.html

On December 2nd 2026, CocoaPods trunk
goes read-only
. Orta Therox set the plan out in 2024: the server stops accepting new pods and new versions, while the
more than 100,000
libraries already published keep resolving through the Specs repo on GitHub and the CDN on jsDelivr, so every existing Podfile resolves exactly as it did the day before. The maintainers had run out of people, Apple’s Swift Package Manager had become the first-class tool, and a
2024 round of critical vulnerabilities
had turned running the trunk server into a liability.
Plenty of users remain: React Native still resolves its iOS dependencies through CocoaPods, the move to SPM is an
active RFC
rather than a finished path, and a long tail of apps will keep running
pod install
well after the freeze. A registry that stops accepting uploads still serves installs to everyone who already depends on it, and the CocoaPods maintainers are not the first team to manage that. Four registries have frozen or shut down before them:
Bower
, web and JavaScript, 2017
Bintray
, JFrog’s binary host, May 2021
JCenter
, Java and Android, read-only May 2021, redirected August 2024
Atom apm
, Atom editor packages, December 2022
Degrees of read-only
Read-only covers a range of states, from a server that rejects new uploads to a dataset that outlives the organisation that ran it, and CocoaPods is choosing the far end by design. The Specs index already lives in a
GitHub repository
and the packages are served from jsDelivr, so the freeze retires the trunk server the team ran, leaving the index and packages on infrastructure CocoaPods does not operate, on the bet that GitHub and jsDelivr outlast the need for it.
Atom’s
apm
went the other way: when GitHub archived the editor in December 2022 the package backend was retired with it, and
apm install
stopped working. Keeping installs alive after a freeze takes deliberate arrangement.
JFrog made the opposite arrangement for
JCenter
, the Java and Android registry it inherited from Bintray. When Bintray was deprecated on May 1st 2021, JFrog kept JCenter as “a read-only repository to ease the burden on the community”, and ran it that way on its own infrastructure for three years. Apache’s
Attic
is the same terminal state given a process: a project whose community has dissolved is moved there, its code stays readable, and nothing new ships. In both cases the organisation that ran the registry holds the data itself.
Bower sits at the other extreme: its registry only ever stored a
package name and a git URL
, with versions read live from the repository’s git tags rather than kept centrally. When it
stopped accepting new registrations
, existing packages went on resolving untouched. A Bower package installs straight from its repository, where the code and tags live, so the freeze took away new names and nothing else, as long as each repo keeps its
bower.json
.
Since 2000 Perl has kept
BackPAN
for exactly this question of who holds the files, a mirror that replicates uploads and ignores deletions, so every release an author ever pushed stays fetchable even after they remove it. A frozen registry needs the same answer: if jsDelivr ever drops the CocoaPods mirror, who holds a complete copy of 100,000 podspecs becomes an urgent question, best answered while the data is still live.
Redirect or rewrite
A registry that keeps serving sets no deadline, so users keep putting the migration off, and JFrog applied some pressure with
brown-outs
: scheduled windows where requests were redirected to Maven Central instead of served, starting with two one-hour windows on July 30th 2024, then two four-hour windows, then a full day, before the permanent redirect on August 15th. The escalation gave every remaining build a recoverable failure to react to ahead of the permanent one. CocoaPods has a gentler version already scheduled, a
test run of read-only mode
from November 1st to 7th 2026, a month before the real switch.
A redirect only works when there is somewhere equivalent to send the traffic, and JFrog could point JCenter at Maven Central because the two registries serve the same artifacts under the same coordinates, so the redirect was close to a drop-in. Bower had no equivalent: it
told users to move to npm
and Webpack, a different tool with a different manifest, so the move was a rewrite. CocoaPods is closer to Bower, because SPM is not a drop-in for a Podfile and moving off it means rewriting each manifest by hand.
The escape hatch is built into CocoaPods’ original design: a podspec’s
source
can name a git tag, and a Podfile can
point a dependency straight at a repository
, bypassing trunk entirely. Therox’s announcement notes that the freeze “shouldn’t affect people who use CocoaPods with their own specs repos, or have all of their dependencies vendored”. Private specs repos and git-backed pods keep the client useful long after the central index stops moving.
Git-backed pods inherit the forge’s mutability: a published registry coordinate cannot change, but a git tag can be moved, and a repository deleted and recreated at the same path takes its old URL with it, the same
redirect surface
that lets a transferred GitHub repo keep resolving. Swapping a frozen immutable index for a live mutable forge is a real trade, easy to make without noticing.
Patching after the freeze
The freeze removes the only place a pod can ever be fixed, even though the
2024 vulnerabilities
that helped justify it were in CocoaPods’ own infrastructure and not in any published pod: an
orphaned-pod takeover
at CVSS 9.3, a
session hijack
at 9.6, and an
RCE on the trunk server itself
at 10.0, all of them closed by shutting the server down.
The pods are where the cost lands: after December 2nd, a popular library with a newly discovered critical CVE has no canonical version to carry the fix, and every consumer is left pinning a git fork by hand. SDWebImage is the kind of pod this strands: actively maintained, resolving from trunk into
more than 25,000 repositories
, with image decoders a routine source of memory-safety CVEs. Once trunk is read-only, a fix its maintainers ship has no way onto the coordinate those repositories already point at.
The team has already used a write restriction as a security tool,
blocking new pods that use
prepare_command
in May 2025 because the field runs arbitrary shell at install time, and a full freeze is the same lever pulled all the way: it closes trunk’s attack surface and the ability to ship any fix along with it.
Linux distributions have lived with this for decades and built a narrow exception for it: a Debian stable release is frozen for everything except security, where a
small team backports fixes
into an otherwise static tree, and the
LTS effort
extends that window past the point where the rest of the project has moved on.
One shape that maps onto a sunset registry is a security-only publishing channel: trunk stays closed to feature releases, but a named set of admins retains the ability to cut a patch version when a vulnerability in a widely-depended-on pod would otherwise have nowhere to land. It keeps publishing narrow, a minimal team and an audit trail, and accepts that the alternative is a known-exploitable package frozen as the newest version.
None of this is free: someone has to staff the channel, decide which CVEs clear the bar, and hold publishing keys to a system that was shut down partly because holding those keys had become dangerous. The 2024 vulnerabilities were in the trunk server’s web stack rather than in cutting a release, so a narrow publishing path need not stand the dangerous server back up. A maintainer might reasonably decide the long tail can fork and pin, and that keeping a loaded server alive costs more than the patches it would ship. The freeze date forecloses the option, so the security-only channel is worth pricing before the switch rather than after the first post-freeze CVE.
