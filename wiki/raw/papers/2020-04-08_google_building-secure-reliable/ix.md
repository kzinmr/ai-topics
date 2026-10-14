---
title: 'Index: Building Secure and Reliable Systems'
source_url: https://raw.githubusercontent.com/google/building-secure-and-reliable-systems/2a2ae3e0d4dbd288f9862ed47194f5b1b1ed7c3c/raw/ix.html
license: CC-BY-4.0
license_url: https://creativecommons.org/licenses/by/4.0/
attribution: Heather Adkins, Betsy Beyer, Paul Blankinship, Piotr Lewandowski, Ana
  Oprea, Adam Stubblefield; Google; O’Reilly, 2020
source_revision: 2a2ae3e0d4dbd288f9862ed47194f5b1b1ed7c3c
original_html: original-source.zip!/raw/ix.html
original_sha256: 6b850e5bd6237daf6e9c990432c86f2a49b7058b0de53fac7c3c56d76e6829cd
created: '2026-10-14'
updated: '2026-10-14'
type: summary
tags:
- reliability
- security
- documentation
sources:
- https://raw.githubusercontent.com/google/building-secure-and-reliable-systems/2a2ae3e0d4dbd288f9862ed47194f5b1b1ed7c3c/raw/ix.html
ingested: '2026-10-14'
sha256: 5350f3e3fa988a0e3f300ed05f8bb870159c214afb340de51da5a6d8e05248ad
content_kind: mechanical_text_extraction
transformation: HTML to plain text in Markdown container; source order retained; no
  translation or abridgment
---
Index
A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z
A
AbsInt,
start
absolute time, limiting dependence on,
start
-
end
abstract interpretation,
start
access control lists (ACLs)
advanced authorization controls,
start
data isolation and,
start
graceful degradation and,
start
key isolation and,
start
safe proxies and,
start
access controls
designing for recovery,
start
Google's corporate network and,
start
understandability and,
start
access denials,
start
accidental errors, recovery from,
start
accountability, risk taking and,
start
ACLs,
start
active entities, defined,
start
activists, as attackers,
start
AddressSanitizer (ASan),
start
administrative APIs,
start
,
start
advanced authorization controls,
start
business justifications,
start
multi-party authorization,
start
three-factor authorization (3FA),
start
-
end
advanced authorization controls,
start
-
end
advanced mitigation strategies,
start
-
end
binary provenance,
start
-
end
code signing,
start
deployment choke points,
start
post-deployment verification,
start
provenance-based deployment policies,
start
-
end
verifiable builds,
start
-
end
advanced mitigation strategies,
start
adversarial testing,
start
adversaries, understanding,
start
-
end
attacker methods,
start
-
end
attacker motivations,
start
attacker profiles,
start
hobbyists,
start
risk assessment considerations,
start
-
end
vulnerability researchers,
start
AFL (American Fuzzy Lop),
start
Agile development,
start
alternative components
pitfalls,
start
types,
start
-
end
ALTS (Application Layer Transport Security),
start
American Fuzzy Lop (AFL),
start
amplification attacks,
start
Android Keystore,
start
Android security team,
start
Android,
start
anonymization,
start
Anonymous (hacktivist group),
start
antivirus software,
start
anycast,
start
APIs (application programming interfaces)
defined,
start
least-privilege-based design,
start
-
end
secure cryptographic APIs and Tink crypto framework,
start
-
end
third-party insider threats,
start
usability and understandability,
start
-
end
App Engine,
start
App Security Improvement (ASI),
start
application frameworks
defined,
start
for service-wide requirements,
start
-
end
Application Layer Transport Security (ALTS),
start
application logs,
start
application-level data recovery,
start
artifact, defined,
start
artificial intelligence
cyber attacks and,
start
protecting systems from automated attacks,
start
ASan (AddressSanitizer),
start
ASI (App Security Improvement),
start
AST pattern matching,
start
-
end
ATT&CK framework,
start
attack surface
binary provenance and,
start
redundancy and,
start
attacker methods,
start
-
end
categorizing of tactics, techniques, and procedures,
start
Cyber Kill Chain framework for studying,
start
DoS attacks,
start
threat intelligence framework for studying,
start
attacker profiles,
start
activists/hacktivists,
start
criminal actors,
start
-
end
governments,
start
-
end
hobbyists,
start
insiders,
start
-
end
vulnerability researchers,
start
attackers,
start
auditing
automated systems,
start
choosing an auditor,
start
collecting good audit logs,
start
least privilege and,
start
-
end
authentication protocol, defined,
start
authentication
credential/secret rotation,
start
-
end
least-privilege policy framework for,
start
-
end
second-factor authentication using FIDO security keys,
start
-
end
understandability and,
start
authorization
advanced controls,
start
auditing to detect incorrect usage,
start
-
end
avoiding potential pitfalls,
start
business justifications,
start
investing in a widely used authorization framework,
start
least-privilege policy framework for,
start
-
end
multi-party,
start
temporary access,
start
three-factor authorization (3FA),
start
-
end
authorized_keys file,
start
automated attacks,
start
automated code inspection tools,
start
-
end
automated response mechanisms,
start
-
end
failing safe versus failing secure,
start
human involvement in,
start
automated testing,
start
automation
code deployment,
start
cyber attacks and,
start
response mechanism deployment,
start
awareness campaigns,
start
awareness, culture of,
start
-
end
AWS Key Management Service,
start
B
batteries-included frameworks,
start
BeyondCorp architecture,
start
Device Inventory Service tools,
start
location-based trust and,
start
zero trust networking model,
start
Bigtable,
start
binary provenance,
start
-
end
,
start
BIOS,
start
blameless postmortems,
start
,
start
blast radius, controlling,
start
-
end
failure domains,
start
-
end
location separation,
start
-
end
role separation,
start
time separation,
start
Blue Teams,
start
-
end
,
start
breakglass mechanism
as safety net,
start
code deployment and,
start
graceful failure and,
start
least-privilege-based design,
start
,
start
budget, for logging,
start
bug bounties (Vulnerability Reward Programs),
start
,
start
,
start
-
end
bugs, compromises versus,
start
builds
defined,
start
verifiable,
start
C
C++,
start
for publicly trusted CA,
start
sanitizing code,
start
CA/Browser Forum Baseline Requirements,
start
California Department of Forestry and Fire Protection,
start
,
start
canaries,
start
Cantrill, Bryan,
start
CAPTCHA (Completely Automated Public Turing test) systems,
start
,
start
CAs,
start
CASBs (cloud access security brokers),
start
casting, implicit,
start
Cellcom,
start
certificate authorities (CAs)
at Google,
start
-
end
background on publicly trusted CAs,
start
build or buy decision,
start
complexity versus understandability,
start
data validation,
start
design, implementation, maintenance considerations,
start
-
end
Google's business need for,
start
hardening with fixits,
start
programming language choice,
start
resiliency for CA key material,
start
securing third-party/open source components,
start
testing,
start
certificate revocation,
start
Certificate Signing Requests (CSRs),
start
certification (security specialists),
start
certification validity database,
start
CFG (control-flow graph),
start
champions, IR team,
start
change budget,
start
change, designing for,
start
-
end
architecture decisions to make changes easier,
start
-
end
best practices for designing your change,
start
complications: when plans change,
start
containers,
start
factors influencing speed of change,
start
-
end
Heartbleed security bug example,
start
keeping dependencies up to date,
start
long-term change: external demand,
start
-
end
medium-term change: improvement to security posture,
start
-
end
microservices,
start
-
end
rebuilding,
start
releasing frequently using automated testing,
start
second-factor authentication using FIDO security keys,
start
-
end
short-term change: zero-day vulnerability,
start
-
end
types of security changes,
start
change
building a case for,
start
picking your battles,
start
reducing fear with risk-reduction mechanisms,
start
-
end
resistance to,
start
slowing down a change,
start
chaos engineering,
start
charter, IR team,
start
checksums,
start
China,
start
choke points,
start
Chrome security team,
start
-
end
background,
start
designing for defense in depth,
start
helping users safely navigate the web,
start
security as team responsibility,
start
speed of detecting and fixing security flaws,
start
stages of evolution,
start
-
end
transparency and community engagement,
start
Chrome security team,
start
CI/CD,
start
CIA (confidentiality, integrity, availability) triad,
start
Cisco,
start
CL (communications lead),
start
,
start
Clang-Tidy,
start
-
end
CLI (command-line interface),
start
-
end
client software,
start
cloud access security brokers (CASBs),
start
cloud assets
compromised cloud instances,
start
identifying/inventorying,
start
Cloud Key Management Service (KMS),
start
ClusterFuzz,
start
code inspection tools, automated,
start
-
end
code reviews,
start
code signing,
start
Code Spaces,
start
code
deploying,
start
testing,
start
writing,
start
Codenomicon,
start
collaborative debugging,
start
Colombia,
start
Columbia Disaster Investigation Board,
start
command-line interface (CLI),
start
-
end
common object model,
start
communication
crisis management and,
start
-
end
emergency access and,
start
foundation for trust,
start
hedging,
start
hypothetical crisis management example,
start
keeping the right people informed with the right levels of detail,
start
meetings in crisis management situations,
start
misunderstandings,
start
overcommunication and transparency when advocating for change,
start
preparing,
start
when email or instant messaging system is compromised,
start
when taking a break from debugging,
start
communications lead (CL),
start
,
start
community engagement,
start
compartmentalization,
start
-
end
location separation,
start
-
end
role separation,
start
complexity
breaking down,
start
evolution and,
start
in evolving systems,
start
least privilege and,
start
managing,
start
understandability versus,
start
concolic testing,
start
confidentiality
isolation of,
start
reliability/security intersection,
start
configuration distribution
custom HTTP receiver (in-process),
start
custom HTTP receiver (sidecar),
start
custom OpenSSH ForceCommand,
start
in least-privilege environment,
start
-
end
POSIX API via OpenSSH,
start
software update API,
start
tradeoffs,
start
configuration-as-code,
start
conformance checks,
start
containers,
start
continuous integration/continuous deployment (CI/CD),
start
implementing verifiable builds,
start
-
end
provenance-based deployment policies,
start
unit tests,
start
continuous validation
designing for recovery,
start
exercising emergency components as part of normal workflows,
start
Google's CA,
start
injecting anticipated changes in behavior,
start
key rotation cycle measurement,
start
oversubscribing but preventing complacency,
start
resilient design and,
start
-
end
scenarios for,
start
-
end
splitting when you cannot mirror traffic,
start
validation focus areas,
start
control plane,
start
control-flow graph (CFG),
start
coordinated vulnerability disclosure (CVD),
start
costs
adding reliability/security to existing systems,
start
computing resources consumed by failure,
start
differentiating costs of failures,
start
-
end
logging,
start
recovery speed's effect on,
start
reliability/security failures,
start
resilience solutions,
start
third-party service providers,
start
credentials
defined,
start
revocation system,
start
-
end
rotation of,
start
-
end
criminal actors
as attackers,
start
-
end
protecting your systems from,
start
crises, incidents versus,
start
-
end
crisis management,
start
-
end
avoiding panic,
start
beginning of response,
start
closure,
start
communications,
start
-
end
compromises versus bugs,
start
coordinated vulnerability disclosure,
start
crises versus incidents,
start
-
end
email attack example,
start
establishing your incident team,
start
handovers,
start
-
end
hypothetical example,
start
-
end
intersection of security and reliability,
start
investigative process,
start
-
end
keeping control of the incident,
start
-
end
keeping the right people informed with the right levels of detail,
start
operational security,
start
-
end
parallelizing the incident,
start
preparing communications and remediation,
start
reliability/security tradeoffs,
start
taking command of your incident,
start
-
end
trading good OpSec for the greater good,
start
triage,
start
-
end
when tools try to be helpful,
start
communications,
start
handovers,
start
operational security,
start
communications,
start
handovers,
start
cross-site scripting (XSS),
start
cryptographic code,
start
-
end
cryptographic keys,
start
cryptography,
start
CSRs (Certificate Signing Requests),
start
culture of no,
start
culture of yes,
start
culture,
start
aligning goals and participant incentives,
start
balancing accountability and risk taking,
start
building a case for change,
start
building a culture of security and reliability,
start
-
end
building empathy,
start
changing through good practice,
start
-
end
culture of awareness,
start
-
end
culture of inevitability,
start
culture of review,
start
-
end
culture of sustainability,
start
-
end
culture of yes,
start
defining a healthy security/reliability culture,
start
-
end
escalations and problem resolution,
start
increasing productivity and usability,
start
-
end
leadership buy-in for security/reliability changes,
start
-
end
least privilege's impact on,
start
overcommunication and transparency,
start
picking your battles,
start
reducing fear with risk-reduction mechanisms,
start
-
end
safety nets as norm,
start
security and reliability as default condition,
start
culture,
start
-
end
CVD (coordinated vulnerability disclosure),
start
Cyber Grand Challenge,
start
Cyber Kill Chain,
start
cyber warfare,
start
D
Dapper,
start
DARPA (Defense Advanced Research Projects Agency),
start
data corruption,
start
data integrity,
start
data isolation,
start
data plane,
start
data sanitization,
start
data summarization,
start
DDoS attacks,
start
debugging,
start
-
end
cleaning up code,
start
collaborative debugging,
start
correlation-versus-causation problem,
start
data corruption and checksums,
start
deleting legacy systems,
start
distinguishing common from uncommon bugs,
start
filtering out normal events from bugs,
start
hypothesis testing with actual data,
start
importance of regular practice,
start
improving access/authorization controls,
start
improving observability,
start
isolating the problem,
start
recording observations,
start
reliability of logging,
start
reproducing the bug,
start
rereading documentation,
start
robust, secure access to systems,
start
security investigations versus,
start
security issues,
start
setting aside time for debugging and investigations,
start
stopping when things start to go wrong,
start
taking a break,
start
techniques,
start
-
end
what to do when you're stuck,
start
-
end
declaring an incident,
start
,
start
decompilers,
start
defacing of websites,
start
Defense Advanced Research Projects Agency (DARPA),
start
defense in depth,
start
-
end
Chrome security team (case study),
start
controlling blast radius,
start
-
end
Google App Engine analysis,
start
-
end
resilience and,
start
Trojan Horse attack,
start
-
end
degradation
controlling,
start
-
end
differentiating costs of failures,
start
-
end
DoS attacks and,
start
failing safe versus failing secure,
start
logs and,
start
resilience and,
start
-
end
response mechanism automation,
start
-
end
Delta Airlines,
start
denial-of-service (DoS) attacks,
start
-
end
amplification attacks,
start
attacker's strategy,
start
CAPTCHA implementation,
start
client retry behavior in self-inflicted attacks,
start
DDoS attacks versus,
start
defendable architecture,
start
-
end
defendable services,
start
defender's strategy,
start
designing for defense against,
start
-
end
graceful degradation,
start
mitigating,
start
-
end
mitigation system,
start
monitoring/alerting,
start
problems with failing open,
start
reliability/security intersection,
start
self-inflicted attacks,
start
-
end
strategic response,
start
user behavior in self-inflicted attacks,
start
deny lists,
start
dependencies, keeping up to date,
start
deploying code,
start
-
end
actionable error messages,
start
advanced mitigation strategies,
start
-
end
automation for,
start
best practices,
start
-
end
binary provenance,
start
-
end
breakglass with,
start
code reviews,
start
code signing,
start
concepts and terminology,
start
-
end
creating unambiguous policies,
start
deployment choke points,
start
ensuring unambiguous provenance,
start
errors manifested during deployment,
start
maintaining confidentiality of secrets,
start
post-deployment verification,
start
practical advice,
start
-
end
provenance-based deployment policies,
start
-
end
securing against threat model,
start
-
end
supply chain issues,
start
threat model,
start
treating configuration as code,
start
trusting third-party code,
start
verifiable builds,
start
-
end
verifying artifacts,
start
advanced mitigation strategies,
start
deployment (generally)
definition,
start
response mechanism,
start
-
end
system,
start
Trojan Horse attack,
start
DER (Distinguished Encoding Rules),
start
design document template (Google),
start
design tradeoffs,
start
-
end
balancing requirements,
start
-
end
cost of adding reliability and security to existing systems,
start
feature requirements,
start
features versus emergent properties,
start
-
end
Google design document template,
start
initial versus sustained velocity,
start
-
end
managing tensions/aligning goals,
start
-
end
microservices and Google web application framework,
start
nonfunctional requirements,
start
objectives/requirements,
start
-
end
payment processing example,
start
-
end
developers, least privilege and,
start
Device Inventory Service tools,
start
DevOps,
start
DevSecOps,
start
,
start
dictionaries, fuzz engines and,
start
digital forensics,
start
-
end
disassemblers,
start
disaster planning,
start
-
end
configuring systems,
start
defining "disaster",
start
dynamic response strategies,
start
prestaging systems and people before an incident,
start
-
end
processes and procedures,
start
real-world examples from Google,
start
-
end
risk analysis,
start
setting up an incident response team,
start
-
end
testing systems and response plans,
start
-
end
training,
start
Disaster Recovery Testing (DiRT) program,
start
,
start
disaster risk analysis,
start
,
start
distinct failure domains,
start
-
end
alternate component pitfalls,
start
alternate component types,
start
-
end
benefits of splitting system into,
start
data isolation,
start
functional isolation,
start
high-availability components,
start
high-capacity components,
start
low-dependency components,
start
-
end
resilience and,
start
distributed denial-of-service (DDoS) attacks,
start
Anonymous's attack on Israeli websites,
start
DoS attacks versus,
start
reliability/security intersection,
start
DNS (Domain Name System) queries,
start
documentation
culture of awareness and,
start
maintaining access to,
start
rereading,
start
dogfooding,
start
DoS extortion,
start
dumb fuzzing,
start
dynamic program analysis,
start
-
end
dynamic type checking,
start
E
elections, hacking of,
start
Elliptic Curve Cryptography (ECC),
start
email
communicating when system is compromised,
start
crisis management email attack example,
start
embargoed vulnerabilities,
start
emergency access
access controls,
start
communication channels,
start
designing for recovery,
start
-
end
responder habits,
start
emergent properties
aligning security/reliability goals,
start
feature requirements versus,
start
-
end
reliability and security as,
start
empathy,
start
encryption keys,
start
encryption
defense in depth and,
start
log data,
start
Envoy HTTP proxy,
start
epoch,
start
error messages,
start
Error Prone,
start
,
start
,
start
errors, threat modeling and,
start
escalations, problem resolution and,
start
espionage,
start
EternalBlue,
start
evolution of systems,
start
exception handling,
start
explicit revocation mechanism,
start
-
end
avoiding risky exceptions,
start
centralized service to revoke certificates,
start
failing open,
start
handling emergencies directly,
start
removing dependency on accurate notions of time,
start
revoking credentials at scale,
start
exponential backoff,
start
,
start
external researchers,
start
-
end
F
Facetime privacy bug,
start
failing closed (secure)
failing safe versus,
start
security/reliability tradeoffs,
start
failing open (safe)
failing secure versus,
start
revocation system,
start
security/reliability tradeoffs,
start
failing static,
start
failover strategies,
start
,
start
failure domains,
start
failures, cost of
computing resources consumed by,
start
differentiating costs of,
start
-
end
effect on user experience,
start
speed of mitigation,
start
failures, system-wide,
start
false positives/negatives,
start
fault injection,
start
fear
reducing with risk-reduction mechanisms,
start
-
end
resistance to change and,
start
feature requirements,
start
FIDO security keys,
start
-
end
firmware
capturing state for updates,
start
rollbacks,
start
first-party insiders,
start
fixits,
start
ForceCommand,
start
forensic timeline,
start
forensics, digital,
start
-
end
forward-only MASVN,
start
Fourth Industrial Revolution,
start
Frama-C,
start
frameworks, software development,
start
access control policies,
start
benefits of,
start
lessons for evaluation/construction,
start
-
end
reliability/security benefits of,
start
reliability/security enforcement,
start
-
end
rollout strategy,
start
RPC backends,
start
-
end
simple, safe, reliable libraries for common tasks,
start
understandability and,
start
-
end
full-stack frameworks,
start
functional isolation,
start
functional requirements,
start
fuzz engines,
start
-
end
fuzz testing (fuzzing),
start
"known safe" functions,
start
Chrome security team and,
start
ClusterFuzz,
start
continuous fuzzing,
start
example fuzzer,
start
-
end
fixits and,
start
how fuzz engines work,
start
-
end
OSS-Fuzz,
start
security/reliability benefits,
start
writing effective fuzz drivers,
start
fuzz testing (fuzzing),
start
-
end
G
games, for developing culture of awareness,
start
General Electric (GE),
start
GFE (Google Front End),
start
global network failure,
start
Gmail,
start
Go Race Detector,
start
Go,
start
goals, aligning,
start
-
end
emergent-property requirements,
start
microservices and Google web application framework,
start
participant incentives and,
start
Google App Engine
culture of yes and,
start
defense in depth and,
start
-
end
runtime layers,
start
threat modeling,
start
Google design document template,
start
Google Front End (GFE),
start
Google Sanitizers,
start
,
start
Google Search,
start
Google
DiRT exercise testing emergency access,
start
disaster planning at,
start
-
end
earthquake response test,
start
embedding security at,
start
-
end
industry-wide vulnerabilities in Linux kernel,
start
password manager incident,
start
reliability- and security-related sections of design doc template,
start
safe proxies case study,
start
-
end
security/reliability education,
start
smart system for intake,
start
sustainable reliability and security culture at,
start
Tool Proxy,
start
-
end
governments
as attackers,
start
-
end
cyber attacks as domestic activity monitoring,
start
intelligence gathering,
start
military purposes of attacks,
start
protecting systems from nation-state actors,
start
graceful degradation
DoS attacks and,
start
logs and,
start
resilience and,
start
-
end
graceful failure,
start
Gregg, Brendan,
start
H
Hacker Camp,
start
hacking (origin of term),
start
hacktivists
as attackers,
start
protecting systems from,
start
handovers,
start
-
end
,
start
,
start
hardware security module (HSM),
start
health, of team members,
start
Heartbleed security bug,
start
,
start
hedging,
start
hermetic builds,
start
hero mode,
start
HIDS (host intrusion detection system),
start
high-availability components,
start
high-capacity service,
start
hobbyists, as attackers,
start
Honggfuzz,
start
host intrusion detection system (HIDS),
start
host management,
start
-
end
HSM (hardware security module),
start
HTTPS,
start
,
start
-
end
human resource testing,
start
I
IC (incident commander),
start
,
start
idempotent operations,
start
identifiers,
start
identities
Google production system model,
start
understandable,
start
-
end
IMAG,
start
imminent risk,
start
immutability, logging design for,
start
implicit casting,
start
implicit type conversions,
start
in-memory state,
start
incentives, aligning goals with,
start
Incident Command System,
start
,
start
incident commander (IC),
start
,
start
Incident Management at Google (IMAG)
crisis management,
start
crisis response,
start
IR team training,
start
crisis management,
start
incident management,
start
incident response (IR) team,
start
-
end
avoiding single points of failure,
start
communicating when email or instant messaging system is compromised,
start
communications,
start
-
end
creating/staffing,
start
-
end
developing response plans,
start
-
end
establishing team charter,
start
handovers,
start
-
end
identifying team members and roles,
start
-
end
keeping control of the incident,
start
-
end
maintaining access to documentation and update information,
start
morale issues,
start
operating parameters,
start
playbooks for,
start
processes and procedures,
start
severity/priority models,
start
training,
start
handovers,
start
morale issues,
start
incident, crisis versus,
start
-
end
incremental development and design,
start
indicators of compromise (IOCs),
start
inevitability, culture of,
start
Infer,
start
information warfare,
start
initial velocity, sustained velocity versus,
start
-
end
injection sinks,
start
insider risk
defined,
start
designing for,
start
MPA protection against,
start
resilience and,
start
threat modeling,
start
insider threat,
start
insiders
attacks by,
start
-
end
designing for insider risk,
start
determining intent of,
start
first-party,
start
related,
start
third-party,
start
threat modeling insider risk,
start
instant messaging, communicating when system is compromised,
start
intake,
start
integration testing,
start
intelligence gathering,
start
interactive sessions,
start
interactive talks,
start
interfaces
common object model and,
start
idempotent operations and,
start
narrow,
start
understandable,
start
-
end
Internet Relay Chat (IRC),
start
intersection of security and reliability,
start
-
end
assessment,
start
budgeting for long-term log storage,
start
commonalities between reliability and security,
start
-
end
communicating when email or instant messaging system is compromised,
start
confidentiality, integrity, availability,
start
-
end
crisis response,
start
deployment of design,
start
design considerations,
start
effects of insiders,
start
emergency access,
start
evolution,
start
Google password manager incident,
start
invisibility,
start
logging,
start
permissions,
start
recognizing a compromise,
start
recovery,
start
relationship between security and reliability,
start
resilience,
start
simplicity,
start
intrusion prevention systems (IPSs),
start
invariants,
start
common security invariants,
start
defined,
start
system invariants,
start
-
end
investigating systems,
start
-
end
debugging techniques,
start
-
end
debugging versus,
start
from debugging to investigation,
start
-
end
intersection of security and reliability,
start
logs, appropriate/useful,
start
-
end
robust, secure debugging access,
start
temporary files,
start
-
end
invisibility, of reliability and security,
start
IP addresses, microservices and,
start
IPsec,
start
IR team,
start
Iran,
start
isolation of assets,
start
-
end
isolation of trust,
start
Israel,
start
J
Java Cryptography Architecture (JCA),
start
JavaScript,
start
jitter,
start
just-in-time notifications,
start
K
key isolation,
start
Key Management Service (KMS),
start
Key Revocation List (KRL),
start
,
start
key rotation
cycle measurement,
start
Heartbleed bug and,
start
preventing rollback with,
start
SSL keys,
start
time separation and,
start
KMS (Key Management Service),
start
known safe functions,
start
known_hosts file,
start
Knusperli,
start
-
end
Kralevich, Nick,
start
KRL (Key Revocation List),
start
,
start
ksplice,
start
Kubernetes,
start
L
lame-duck mode,
start
law enforcement agencies
as attackers,
start
-
end
cyber attacks as domestic activity monitoring,
start
law of diminishing returns,
start
leadership
building a case for change,
start
buy-in for security/reliability changes,
start
-
end
escalations and problem resolution,
start
picking your battles,
start
understanding the decision-making process,
start
least privilege,
start
-
end
advanced authorization controls,
start
auditing,
start
-
end
best practices,
start
-
end
breakglass,
start
business justifications,
start
classifying access based on risk,
start
complexity of security posture,
start
concepts and terminology,
start
configuration distribution,
start
-
end
defined,
start
designing for,
start
-
end
developer complexity and,
start
diagnosing access denials,
start
graceful failure and breakglass mechanisms,
start
impact on collaboration and company culture,
start
investing in a widely used authorization framework,
start
multi-party authorization,
start
policy framework for authentication/authorization decisions,
start
-
end
proxies,
start
quality of security-impacting data,
start
reliability/security tradeoffs,
start
small functional APIs,
start
-
end
temporary access and,
start
testing and,
start
-
end
three-factor authorization (3FA),
start
-
end
tradeoffs/tensions,
start
user productivity and,
start
zero touch,
start
zero trust networking,
start
advanced authorization controls,
start
-
end
breakglass,
start
legacy systems,
start
Liberia,
start
libFuzzer,
start
linters,
start
LLVM Clang,
start
load balancing,
start
load shedding,
start
location separation,
start
-
end
aligning physical and logical architecture,
start
isolation of confidentiality,
start
isolation of trust,
start
location-based trust,
start
Lockheed Martin,
start
logging
attackers' bypassing of,
start
budget for,
start
collecting appropriate/useful logs,
start
-
end
designing for immutability,
start
determining which security logs to retain,
start
-
end
intersection of security and reliability,
start
logs as attack target,
start
privacy issues,
start
reliability issues,
start
Lonestar,
start
lost causes, value of,
start
low-dependency service,
start
-
end
M
malicious actions, recovery from,
start
malware reports,
start
MASVN (minimum acceptable security version numbers),
start
-
end
mean time to detection (MTTD),
start
mean time to repair (MTTR),
start
meetings, in crisis management situations,
start
Mehta, Neel,
start
memory corruption, checksums and,
start
memory-safe languages,
start
mental models
idempotency and,
start
understandability and,
start
microservices
designing for change with,
start
-
end
Google's frontend design,
start
Google-internal framework,
start
rate-limiting mechanism as,
start
role separation,
start
military, cyber warfare and,
start
Miller, Matt,
start
minimum acceptable security version numbers (MASVN),
start
-
end
Mission Control program,
start
mission, of IR team,
start
mistakes, threat modeling and,
start
MIT (Massachusetts Institute of Technology),
start
mitigation doc,
start
mitigation strategies, advanced,
start
MITRE,
start
morale issues
IC's responsibility for,
start
on incident response teams,
start
motivations, of attacker,
start
MTTD (mean time to detection),
start
MTTR (mean time to repair),
start
multi-party authorization (MPA),
start
code review as,
start
reliability and,
start
resilience and,
start
unilateral insider risk protection,
start
multicomponent failure testing,
start
multilevel nesting,
start
mutation testing,
start
N
NASA,
start
nation-state actors, protecting systems from,
start
Netflix,
start
network intrusion detection systems (NIDSs),
start
nonfunctional requirements,
start
nontechnical risks,
start
North Korea,
start
notes, keeping during recovery,
start
,
start
NotPetya ransomware,
start
NSA,
start
NSO Group,
start
O
observability, improving,
start
OIDC (OpenID Connect),
start
,
start
OL (operations lead),
start
one-time passwords (OTPs),
start
-
end
one-time programmable (OTP) devices,
start
OODA (observe, orient, decide, act) loop,
start
open source components
for Google custom CA,
start
third-party insider threats,
start
OpenID Connect (OIDC),
start
,
start
OpenSSH
configuration distribution via,
start
custom OpenSSH ForceCommand,
start
OpenSSL library,
start
,
start
operating parameters, IR team,
start
operating system logs,
start
Operation Aurora,
start
,
start
operational overload,
start
,
start
operational security (OpSec)
crisis management,
start
-
end
hypothetical crisis management example,
start
trading good OpSec for the greater good,
start
operations lead (OL),
start
OSS-Fuzz,
start
OTP (one-time programmable) devices,
start
OTPs (one-time passwords),
start
-
end
overcommunication,
start
,
start
,
start
overprovisioning,
start
P
panic rooms,
start
parallelizing an incident,
start
Park Jin Hyok,
start
partial restores,
start
passwords,
start
patch, defined,
start
payment processing system design (case study),
start
-
end
security/reliability considerations,
start
third-party service provider for sensitive data,
start
-
end
Peach Fuzzer,
start
penetration testers,
start
,
start
permissions,
start
persistent data,
start
personally identifiable information (PII),
start
Petya ransomware,
start
phishing attack
credential rotation and,
start
recovery from,
start
-
end
two-factor authentication to address risk of,
start
phone bridges,
start
physical location,
start
-
end
PII (personally identifiable information),
start
pivot points,
start
playbooks, IR team,
start
poisoned regions,
start
police,
start
policies
avoiding automated unsupervised changes,
start
creating unambiguous,
start
POSIX API,
start
,
start
post_install command,
start
postmortems,
start
-
end
,
start
,
start
pre_rm command,
start
prestaging (disaster planning),
start
-
end
configuring systems,
start
processes and procedures,
start
training,
start
priority models, IR teams and,
start
privacy, logging and,
start
production
intersection of security and reliability,
start
safe proxies in production environments,
start
-
end
single system testing/fault injection,
start
testing response in production environments,
start
productivity
increasing,
start
-
end
least privilege and,
start
profile, attacker,
start
program analysis
dynamic,
start
-
end
static,
start
-
end
Project Shield,
start
provenance-based deployment policies,
start
-
end
provenance
binary,
start
-
end
data sanitization and,
start
ensuring unambiguous provenance,
start
binary,
start
proxies,
start
benefits of,
start
downsides of,
start
safe,
start
pseudonymization,
start
publicly trusted certificate authority (CA),
start
-
end
Purple Team,
start
,
start
Pwn2Own,
start
Pwnium,
start
Q
quality-of-service (QoS) controls,
start
quarantine (isolation)
assets,
start
-
end
compartments and,
start
R
random errors, recovery from,
start
ransomware attacks,
start
Petya,
start
responses based on culture,
start
Rapid (software release tool at Google),
start
rate-limiting mechanism,
start
readability,
start
recovery checklists,
start
,
start
,
start
,
start
recovery data,
start
recovery speed,
start
recovery, designing for,
start
-
end
accidental errors,
start
design for reasonable speed,
start
-
end
design for testing/continuous validation,
start
design principles,
start
-
end
emergency access,
start
-
end
explicit revocation mechanism,
start
-
end
isolating the rate-limiting mechanism,
start
knowing intended state,
start
-
end
limiting dependencies on external notions of time,
start
-
end
malicious actions,
start
random errors,
start
rollbacks as tradeoff between security and reliability,
start
-
end
scenarios requiring recovery,
start
-
end
software errors,
start
unexpected benefits,
start
recovery,
start
-
end
aftermath of,
start
-
end
attacker's response to,
start
checklists,
start
compromised cloud instances,
start
compromised infrastructure/tooling,
start
credential/secret rotation,
start
-
end
data sanitization,
start
examples,
start
-
end
initiating,
start
-
end
intersection of security and reliability,
start
isolation of assets,
start
-
end
large-scale phishing attack,
start
-
end
logistics,
start
-
end
mitigation option questions,
start
-
end
open-ended questions/considerations,
start
-
end
planning,
start
-
end
postmortems,
start
-
end
recovery data,
start
reintroduction of attack vectors,
start
repeating risks,
start
roles and responsibilities in,
start
scoping,
start
speed of mitigation,
start
system rebuilds and software upgrades,
start
targeted attack requiring complex recovery,
start
timeline,
start
variants of attack,
start
recovery,
start
-
end
Red Teams,
start
defined,
start
location-based trust and,
start
Red Teams,
start
,
start
-
end
redundancy
controlling,
start
-
end
failover strategies,
start
payment processing system example,
start
reliability/security tradeoffs,
start
refactoring,
start
,
start
reference documentation,
start
related insiders,
start
reliability risks,
start
,
start
reliability
as emergent property of system design,
start
security and,
start
remediation lead (RL),
start
,
start
,
start
remote procedure calls (RPCs)
framework for backends,
start
-
end
safe proxies and,
start
three-factor authorization and,
start
tool proxies and,
start
reproducible builds,
start
researchers,
start
-
end
resilience, designing for,
start
-
end
continuous validation,
start
-
end
controlling blast radius,
start
-
end
controlling degradation,
start
-
end
controlling redundancies,
start
-
end
defense in depth,
start
-
end
design principles,
start
failure domains,
start
-
end
intersection of security and reliability,
start
overcoming resistance to,
start
response mechanism deployment,
start
-
end
solutions in order of costs,
start
starting points for,
start
-
end
resistance to change,
start
response mechanism deployment,
start
-
end
automated response,
start
load shedding,
start
reliability/security tradeoffs,
start
throttling,
start
response plans
auditing automated systems,
start
communicating when email/instant messaging system is compromised,
start
conducting nonintrusive tabletops,
start
-
end
developing,
start
-
end
DiRT exercise testing emergency access,
start
earthquake response test,
start
evaluating responses,
start
human resource testing,
start
in production environments,
start
industry-wide vulnerabilities in Linux kernel,
start
multicomponent testing,
start
real-world examples from Google,
start
-
end
Red Team exercises,
start
single system testing/fault injection,
start
system-wide failures/failovers,
start
testing,
start
-
end
reverse engineering,
start
,
start
review, culture of,
start
-
end
revocation list,
start
revocation mechanism,
start
risk analysis,
start
,
start
risk assessment
disaster risk assessment matrix,
start
understanding adversaries,
start
-
end
risk ratings,
start
risk reduction, reducing fear with,
start
-
end
risk taking, balancing accountability with,
start
risk
classifying access based on,
start
reliability versus security design considerations,
start
RL (remediation lead),
start
,
start
,
start
role separation,
start
roles and responsibilities,
start
-
end
Blue and Red Teams,
start
-
end
embedding security at Google,
start
-
end
embedding security specialists and security teams,
start
external researchers,
start
-
end
integrating security into the organization,
start
-
end
recovery and,
start
security/reliability as everyone's responsibility,
start
-
end
security/reliability risk evaluation,
start
specialists' roles,
start
understanding security expertise,
start
rollbacks
deny lists,
start
firmware/hardware-centric constraints,
start
minimum acceptable security version numbers,
start
-
end
rotating signing keys,
start
security/reliability tradeoffs,
start
-
end
rollouts
incremental,
start
legacy conversions,
start
staged,
start
strategy for,
start
rotation of keys,
start
RPCs,
start
RSA,
start
,
start
S
safe proxies (case study),
start
-
end
Google Tool Proxy,
start
-
end
in production environments,
start
-
end
SafeHtml,
start
,
start
SafeSql,
start
safety nets,
start
same-origin policy,
start
sandboxing,
start
,
start
,
start
sanitizing code,
start
sanitizing data,
start
scalable revocation,
start
scope, of IR team charter,
start
secrets
dangers of including in code,
start
rotation of,
start
-
end
security (generally)
as emergent property of system design,
start
integrating into the organization,
start
-
end
reliability and,
start
security boundaries
defined,
start
small TCBs and strong security boundaries,
start
threat models and,
start
understandability and,
start
-
end
security by design,
start
security champions,
start
security changes,
start
security experts,
start
security investigations,
start
security logs
application logs,
start
cloud logs,
start
determining which security logs to retain,
start
-
end
host agents,
start
network-based logging and detection,
start
operating system logs,
start
security posture, changes to,
start
-
end
security risks,
start
,
start
security specialists
certifications and academia,
start
embedding into the organization,
start
hiring,
start
role of,
start
security teams,
start
seed corpus,
start
self-inflicted DoS attacks,
start
-
end
client retry behavior,
start
user behavior,
start
self-registration,
start
self-resolution,
start
severity model,
start
Shellshock,
start
Shipshape,
start
sidecar daemon,
start
signing keys,
start
Simian Army,
start
simplicity,
start
single sign-on (SSO) services,
start
single system testing, fault injection and,
start
Site Isolation project,
start
Site Reliability Engineer/Engineering (SRE)
crisis management,
start
problem space's similarities to security problems,
start
risk evaluation by,
start
Security Engineering's similarities to,
start
SRE Security Exchange Program,
start
software development,
start
software errors, recovery from,
start
software supply chain,
start
-
end
software upgrades, recovery and,
start
Sony Pictures,
start
Space Shuttle Columbia incident,
start
Spanner,
start
,
start
-
end
SQL injection (SQLI),
start
,
start
-
end
SRE Security Exchange Program,
start
SRE,
start
SSL key rotation,
start
SSO (single sign-on) services,
start
staged rollouts,
start
stalkerware,
start
state exhaustion attack,
start
state
defined,
start
device firmware,
start
global services,
start
host management,
start
-
end
knowing intended state,
start
-
end
persistent data and,
start
static analysis,
start
-
end
abstract interpretation,
start
automated code inspection tools,
start
-
end
formal methods,
start
integration into developer workflow,
start
-
end
reverse engineering and test input generation,
start
static type checking,
start
Stoll, Clifford,
start
stored XSS bugs,
start
Strava,
start
strongly typed language,
start
,
start
-
end
structured justification,
start
supply chain,
start
code deployment issues,
start
security benefits of designing for recovery,
start
sustainability, culture of,
start
-
end
sustained velocity, initial velocity versus,
start
-
end
Syrian Electronic Army,
start
system invariants,
start
-
end
,
start
system logs, as attack target,
start
system rebuilds,
start
systems (generally)
in context of systems engineering,
start
investigating,
start
T
tabletop exercises,
start
-
end
tactics, techniques, and procedures (TTPs),
start
,
start
talks, interactive,
start
TCB,
start
technical debt
compromised assets as,
start
during recovery,
start
repaying when writing code,
start
technical program managers (TPMs),
start
temporary access, least privilege and,
start
test, defined,
start
testing (automated),
start
testing (code),
start
-
end
correctness validation,
start
dynamic program analysis,
start
-
end
fuzz testing,
start
-
end
integration testing,
start
static program analysis,
start
-
end
unit testing,
start
-
end
testing (general)
designing for recovery,
start
Google's certificate authority,
start
least privilege and,
start
-
end
test environment security/reliability tradeoffs,
start
testing (response plans)
auditing automated systems,
start
conducting nonintrusive tabletops,
start
-
end
DiRT exercise testing emergency access,
start
earthquake response test,
start
evaluating responses,
start
human resource testing,
start
in production environments,
start
industry-wide vulnerabilities in Linux kernel,
start
multicomponent testing,
start
real-world examples from Google,
start
-
end
Red Team exercises,
start
single system testing/fault injection,
start
system-wide failures/failovers,
start
third-party code,
start
third-party components,
start
third-party insiders,
start
third-party service providers
benefits of,
start
costs and nontechnical risks,
start
reliability risks,
start
security risks,
start
sensitive data and,
start
-
end
threat intelligence,
start
threat mitigation,
start
threat modeling
deploying code,
start
insider risk,
start
mistakes and,
start
securing code against threat model,
start
-
end
security boundaries and,
start
Trojan Horse attack,
start
securing code against threat model,
start
three-factor authorization (3FA),
start
-
end
ticket queue,
start
time dependence, limiting,
start
-
end
Tink library,
start
-
end
Tool Proxy (Google binary),
start
-
end
TPMs (technical program managers),
start
tradeoffs, design,
start
tradeoffs, reliability/security
controlling degradation,
start
deny lists,
start
imminent risk,
start
incident management,
start
redundancy,
start
response mechanisms,
start
rollbacks,
start
-
end
system usability in least-privilege environment,
start
test environments,
start
transparency
Chrome security team case study,
start
when advocating for change,
start
transport security,
start
triage,
start
-
end
,
start
Tricorder,
start
Trojan Horse attack,
start
-
end
compromise,
start
deployment,
start
execution,
start
threat modeling and vulnerability discovery,
start
trust, isolation of,
start
trusted computing base (TCB),
start
-
end
small TCBs and strong security boundaries,
start
understandability and,
start
TrustedSqlString,
start
-
end
TTPs (tactics, techniques, and procedures),
start
,
start
two-factor authentication (2FA)
3FA vs.,
start
benefits during recovery,
start
using FIDO security keys,
start
-
end
type checking,
start
type conversions, implicit,
start
U
UCLA Medical Center,
start
Ukraine,
start
understandability,
start
-
end
access control and,
start
analyzing invariants,
start
API usability and,
start
-
end
application frameworks for service-wide requirements,
start
-
end
authentication and transport security,
start
benefits of,
start
-
end
breaking down complexity,
start
centralized responsibility for security/reliability requirements,
start
complex data flows,
start
-
end
complexity versus,
start
designing understandable systems,
start
-
end
Google CA implementation,
start
identities,
start
-
end
interface specifications,
start
-
end
mental models and,
start
security boundaries,
start
-
end
software design,
start
-
end
system architecture,
start
-
end
system invariants and,
start
-
end
unit testing,
start
-
end
effect on code,
start
-
end
when to write unit tests,
start
writing effective unit tests,
start
universal two-factor (U2F) hardware security tokens,
start
Unix, small functional APIs and,
start
-
end
unmanaged complexity, understandability versus,
start
unzipping,
start
Upvote,
start
URLs,
start
usability
focus on,
start
increasing,
start
-
end
user experience, failures' effect on,
start
user productivity, least privilege and,
start
V
Valgrind,
start
,
start
validation, continuous,
start
velocity, initial versus sustained,
start
-
end
verifiable builds,
start
-
end
architectures,
start
implementation,
start
-
end
unauthenticated inputs,
start
untrusted inputs,
start
Verizon,
start
version advancement,
start
virtual LANs (VLANs),
start
vulnerability researchers, as attackers,
start
Vulnerability Reward Programs (bug bounties),
start
,
start
,
start
-
end
vulnerability scanning teams,
start
W
wall-clock time, limiting dependencies on,
start
-
end
WannaCry Ransomware,
start
,
start
web application firewall (WAF),
start
web applications, Google-internal framework,
start
web origin, defined,
start
WebKit,
start
Wheel of Misfortune,
start
Wilkes, Maurice,
start
writing code,
start
-
end
avoiding multilevel nesting,
start
choice of tools for,
start
-
end
common security vulnerabilities,
start
-
end
eliminating YAGNI smells,
start
frameworks to enforce security and reliability,
start
-
end
lessons for framework evaluation/construction,
start
-
end
memory-safe languages for,
start
refactoring,
start
repaying technical debt,
start
rollout strategy,
start
sanitizing code,
start
security and reliability by default,
start
-
end
simple, safe, reliable libraries for common tasks,
start
simplicity's importance to,
start
-
end
static type checking for,
start
strong typing for,
start
understandability,
start
-
end
strong typing for,
start
-
end
Wycheproof,
start
X
XSS (cross-site scripting),
start
Y
YAGNI ("You Aren't Gonna Need It"),
start
Yahoo!,
start
yes, culture of,
start
YouTube,
start
Z
Zero Touch interfaces,
start
Zero Touch Prod (ZTP),
start
,
start
zero trust networking,
start
access control and,
start
Google's corporate network,
start
location-based trust and,
start
zero-day vulnerability
responding to,
start
-
end
Shellshock example,
start
Zipkin,
start
ZTP (Zero Touch Prod),
start
,
start
