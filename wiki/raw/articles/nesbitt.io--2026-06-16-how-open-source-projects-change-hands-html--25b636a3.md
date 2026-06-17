---
title: "How Open Source Projects Change Hands"
url: "https://nesbitt.io/2026/06/16/how-open-source-projects-change-hands.html"
fetched_at: 2026-06-17T07:01:19.928319+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# How Open Source Projects Change Hands

Source: https://nesbitt.io/2026/06/16/how-open-source-projects-change-hands.html

Dumb Ways for an Open Source Project to Die
listed the ways projects end up dead, and most of the entries describe a moment where maintainership should have moved to someone else and didn’t. This is the other, shorter inventory: the mechanisms that exist for a project to change hands, and who can trigger each one.
The maintainer decides
Chosen successor.
The maintainer picks a person and hands over the keys. This is the model everyone imagines when they say succession, and it has almost no supporting infrastructure: it’s a private conversation followed by some permission changes. The vetting is whatever the departing maintainer feels like doing, which is how
event-stream
happened: “he emailed me and said he wanted to maintain the module, so I gave it to him.” The
xz takeover
was the same mechanism worked patiently, with sock-puppet users manufacturing the pressure on an overworked maintainer to hand over.
CPAN is the one registry that gives this stage a name: a module whose permissions list the pseudo-user
HANDOFF
has a maintainer looking for someone to take over, recorded in the same machine-readable
permissions file
as every real owner.
The successor setting.
GitHub has had
account successors
since 2020: you name a person in your account settings, and after presenting
a death certificate and waiting seven days, or an obituary and waiting twenty-one
, they can archive your public repositories or transfer them to an account they control. It is the only entry on this list built for the case where the maintainer dies. It covers the repos but not the registry accounts that publish from them, and no registry has an equivalent.
Open adoption.
Instead of picking someone, the maintainer flags the project as available and waits. CPAN again has the oldest version: the
ADOPTME
pseudo-user as owner means the module is up for adoption, and NEEDHELP means the owner wants co-maintainers without leaving. RubyGems
proposed
an equivalent in October 2014, designed so that “the happiest of happy paths is to enable communication dev-to-dev, requiring no external involvement”, and
shipped it
as ownership calls and requests at the end of 2021. Debian’s RFA, Request For Adoption, does the same job for packages: the maintainer keeps working until a successor appears. Outside the registries the equivalent is a
repostatus badge
or a “looking for maintainers” line in the README, and no tooling reads either one.
Deliberate ending.
The maintainer can also decline to be succeeded, and the registries support that decision better than any of the handovers above. Packagist’s
abandoned
field takes a replacement package name, and composer prints “Package X is abandoned, you should avoid using it. Use Y instead.” on every install.
NuGet deprecation
carries an alternate package, and a fully deprecated legacy package can apply to transfer its search ranking to a successor that shares its owners. Maven has the
relocation
element for coordinates that moved.
PyPI added
project archival
in 2025 and now serves
status markers
through its APIs. GitHub archiving makes the repo read-only with a banner. Pointing at a successor package moves the users to different code rather than moving the code to a different maintainer.
Someone else decides
Registry adjudication.
A third party hears a claim on an unmaintained name and rules on it. PyPI runs the most formal version:
PEP 541
defines abandonment by three conjunctive criteria (unreachable owner, no release in twelve months, no owner activity). The claimant has to show failed contact attempts and improvements on their own fork, and explain why a renamed fork won’t do. It handled
over 500 requests in 2025
and cleared what had been a nine-month backlog. PAUSE admins will grant co-maintainership on a CPAN module when the owner “has entirely disappeared”, with the condition that the adopter is “
required to respect the work and design of the author
”. Hackage admins
add you to a package’s maintainer group
after you’ve tried the maintainer and stated your intent publicly.
npm ran a four-week mediation process and
suspended it in February 2021
after a mis-transfer; the
current policy
is “we do not transfer package, organization, or username ownership simply because another user wants the name”. crates.io
removed its transfer mediation policy
in 2024, on the grounds that requests grow with the registry and “aren’t even usually successful”, citing a PyPI team “not able to keep up with the requests”.
The orphan pool.
The Linux distributions treat an unmaintained package as a vacancy to fill, and built state machines for filling it. Debian encodes the whole lifecycle as
WNPP bugs
: O for orphaned, RFA for adoption requested, RFH for help wanted, ITA for intent to adopt, and
ITS for intent to salvage
a package whose maintainer is present but inactive. Orphaning sets the package’s Maintainer field to the
Debian QA Group
, and an
MIA team
chases unresponsive maintainers through a staged escalation that ends in orphaning everything they hold.
Fedora reassigns orphaned packages to a literal
orphan user
that any packager can take over from with a button. After six weeks unclaimed the package is retired by
committing a file named dead.package
to its repo. The AUR grants
orphan requests
after two weeks of maintainer silence, automatically if the package has been flagged out-of-date for 180 days. CRAN marks the maintainer field itself
ORPHANED
and lets anyone take over without the previous maintainer’s consent. None of the language registries has anything like this: a distro package is communal property with a caretaker of record, while a registry name belongs to whoever published first.
In June 2026 an attacker adopted
over four hundred orphaned AUR packages
and added an
npm install
line to every PKGBUILD. The fetched npm package’s preinstall hook installed a
credential stealer and eBPF rootkit
. The
first report
was a user noticing
npm install
in a VR streaming tool’s PKGBUILD. Each time the payload package was taken down and the install line grepped for, the next batch of adoptions switched:
npm install
became
bun add
on a fresh package, then
'b''u''n' 'a'"d""d"
. Arch
restricted account creation and package adoption
while the incident ran.
The monorepo.
Homebrew, nixpkgs, and conda-forge keep every package definition in one shared repository, so there are no keys to hand over and a succession is a pull request, which is as close as this list gets to anyone deciding with a reviewer in the loop. homebrew/core records no per-formula maintainer at all; maintainership amounts to whoever the tap accepts changes from. nixpkgs lists package maintainers as entries in
one file
, and adopting an orphaned package means adding your name to it, which is the distro’s caretaker-of-record model without the orphaning process.
Foundation custody.
Projects can move into an organisation built to outlive any individual maintainer. Apache projects are run by
PMCs
rather than people, so succession is a membership change inside a structure that persists, and when a community dissolves the project moves to the
Attic
, a read-only terminal state with its own documented process. The OpenJS Foundation runs a
progression and emeritus lifecycle
for hosted projects. The foundation takes on the bus factor in exchange for governance overhead, and most packages on any registry are far too small to ever make that trade.
Corporate custody.
When a company holds the project, succession is an org chart event: from inside it’s the chosen-successor mechanism with an employer attached, and from outside it isn’t visible at all. When
antirez stepped down from Redis in 2020
he chose two successors and refused to design the governance that followed. He and both successors were Redis Labs employees, and the company held the trademark. The community’s succession came in 2024, when the
relicense
pushed Madelyn Olson and most of the external core team into forking Valkey under the Linux Foundation. That arrangement holds until the team is cut and the project becomes the corporate orphan from the previous post.
Anyone decides
The fork.
Every mechanism above falls back to this one: PEP 541 requires a working fork before PyPI will consider a transfer, and crates.io’s advice for an unreachable owner is to pick a new name. A fork copies the code, and the original keeps the registry name, which means it also keeps the install count and every manifest and lockfile that references it. The fork limbo and licence rug-pull cases from the death list both happened this way, with development moving to a new repo and the installs still resolving to the old one.
The forwarding-address problem has one solution, at the forge layer: GitHub
repository transfers
redirect the old URL to the new one indefinitely, although creating a new repository at the old name deletes the redirect permanently, an attack surface of its own. Go modules inherit both properties because a
module path contains the repo that hosts it
: there are no registry accounts to transfer, and a fork lives at a new path with a Deprecated comment in go.mod as the forwarding address. A transferred repo keeps resolving through the redirect, and Swift packages, declared as
Git URLs in the manifest
, behave the same way without an equivalent of the Deprecated comment to forward a fork.
The stranger.
Avelino et al.
studied 1,932 popular GitHub projects
and found 16% had been abandoned by all of their core developers; 41% of those survived, and 86% of the survivors were rescued by a single new core developer. The most common motivation was “because I was using the project”, and the barriers the rescuers reported were not technical: lack of time, and not being able to get push access because the people who could grant it were gone.
The rescue the study describes is informal: someone who needs the package asks whoever still has access, and the handover is an email and some permission changes that nothing flags or records. That is also how event-stream changed hands, and the maintainer granting access has no way to tell the rescuer from the attacker. Where the orphan pool has already removed that maintainer, as with the four hundred AUR packages above, there is nobody in a position to tell.
