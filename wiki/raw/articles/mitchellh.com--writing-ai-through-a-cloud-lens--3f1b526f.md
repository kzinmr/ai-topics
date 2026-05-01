---
title: "Growth of AI Through a Cloud Lens"
url: "https://mitchellh.com/writing/ai-through-a-cloud-lens"
fetched_at: 2026-05-01T07:02:03.604412+00:00
source: "mitchellh.com"
tags: [blog, raw]
---

# Growth of AI Through a Cloud Lens

Source: https://mitchellh.com/writing/ai-through-a-cloud-lens

Every 10 or so years, a platform shift begins. 17 years ago, Amazon kicked
off a platform shift with the release of S3 and EC2 under the Amazon Web
Services (AWS) umbrella. This resulted in a shift best summarized as
"cloud-native," fundamentally changing the way we build and deliver software
worldwide from small individuals to the largest global companies.
Today, AI -- in particular the advancements in
large language models (LLMs)
--
is starting to feel like the beginning of another platform shift. This isn't
a shift
from cloud
, this is a platform shift within a different category,
but it has the same potential to fundamentally change the way we build and
deliver software.
I will look at the rise of AI through the historical lens of the rise of cloud.
Rather than recount a full history of cloud (boring!), I will highlight a few
categories of thought and use those categories to make comparisons from
cloud to AI and predictions about the future.
The early success of cloud was marked by providing
immediate value
to
early adopters. For small projects (initially, more on this later), EC2
was the fastest and cheapest way to get a server and S3 was the easiest and most
reliable way to store and serve static assets and binary blobs. And everything
had an easy to use HTTP API, encouraging a new age of automation and approachability
for engineers.
Recent AI developments have the same
immediate value
feeling.
Previously hard problems to quickly integrate like sentiment analysis
("is this bio offensive?") are now trivial. Code generation through tools
like
Copilot
are not only not terrible,
they're... kind of decent? And oh yeah, everything is starting to have an
easy to use HTTP API, encouraging a new age of automation and approachability
for engineers.
Immediate value is a
really good sign
and builds an early tribe of enthuastic
users that make a lot of noise. At the same time, immediate value is often
mistaken for durable value
.
The initial value of AI is undeniable, what remains to be seen is how big
of an impact this value makes.
"Crypto" (as in cryptocurrencies, not cryptography) failed this test for me.
It had no immediate practical value. Enthusiasts claimed it had all sorts of
long-term future value. Maybe, maybe not. 🤷 All I know is someone sent me a
bitcoin in 2010 and I thought "okay, now what?" And I personally never really
got past that stage even to now, 13 years later, regardless of any long-term
potential.
Impractical Beginnings
Early cloud computing was raw and impractical for a large tract of problems.
Long-lived IP addresses didn't become available until 2008,
two years
after the launch of EC2. Persistent storage so you can reliably save data also
didn't become available until
two years
after the launch of EC2. Every
EC2 instance was on a shared public network until the launch of VPC in
2009,
three years
later. The examples continue.
The impracticality of something can't be judged in isolation. A thing is
only impractical in the context of something else. So while the lack of
private networks was impractical in the context of business software, it
didn't make a difference for small projects and early stage startups. This
led to excitement and growth in the context where cloud computing was practical.
As AWS continued to launch new services, the set of contexts in which it was
impractical continued to shrink.
As cloud gained some popularity and hype, a common dismissal during this era
of cloud was "
real
businesses won't ever be able to use it." And as
cloud continued to become more capable, the goal post just moved, such
as "fortune 500s will never use cloud" then "regulated companies will never use
cloud" then "governments will never able to use it" and so on. Today, for
better or worse, important aspects
of the US national defense
rely on cloud.
AI is in a similar position today. Despite its immediate value, the lack of
additional functionality and tooling make it impractical in many contexts.
Getting the
right answer reliably
for certain questions is very hard or maybe
impossible. Integrating LLMs with outside, up-to-date knowledge is in its
infancy. A lot of tooling lacks corporate support or is currently one of
a thousand seed-stage startups with no clear winner. It's early.
And just like cloud, I hear similar dismissals of the technology: "it'll
never generate
large
amounts of code" or "it'll always require a human
in the loop" and so on. Maybe, maybe not. The dismissal itself can't be
immediately dismissed, but it also isn't enough on its own to ignore a trend.
Given the previously stated
immediate value
that AI has
today
, I believe
this issue will sort itself out in the same way it did for cloud. The
impractical parts of AI aren't that it isn't useful, its that its hard to
integrate or trust the usefulness of it at scale. This is a tractable problem,
not some fundamental impossibility.
There are some questions of fundamental impossibility when considering
future (undemonstrated) value
. As one extreme example, the excitement around
artificial general intelligence (AGI)
is
very unproven and models that exist today are impractical for AGI. This type
of impractical problem however is based on completely undemonstrated value
and a different sort of definition of "impractical" than I am describing.
Evolution in Software Properties
The hallmark trait of a platform shift is forcing an evolution in software
properties. Software that has these properties is usually coined with some term,
such as "cloud-native" or "mobile-first." Back in 2016, I gave a talk where
I outlined the properties of "cloud-native" as a shift from a static
to dynamic way of thinking:
(This is not the same slide I used in 2016. This is a more modern
version that we integrated into various
HashiCorp
decks in later years.)
My argument was that software in the left column is "traditional"
software. Traditional software
can
run in cloud environments, but
it is inferior to software with equivalent functionality that embraces
the dynamic, cloud-native approach. For software vendors in the left column,
their product was also more likely to be eaten by new startups that build the
same software but with properties in the right column. As an example,
I often argue that
Vault
would not exist
if the incumbents had just adapted to a cloud-native world.
An older example of the impact of shifting software properties are mobile apps.
I had the opportunity
in the 2010s to meet with the CEO of a large US bank. He rhetorically
asked me: "what do you think is the #1 reason people switch banks?" After some
wrong guesses, he told me: "more functionality in the mobile app." He was
describing why the bank was investing so much money into cloud services and
software engineering, and it was all going towards mobile functionality. Banks
that took longer to adapt to the rise of mobile devices lost more customers.
An even older example is web apps. I think this one is obvious: you're more
likely to use a service if they're present on the web. And you're more likely
to use a service that has the
better
presence on the web.
I predict that a similar situation will arise with AI. Some sort of properties
will present themselves that differentiate between "old" and "new", and the
products and businesses that embrace the "new" will become more attractive
to a shifting generation of users. "Old" software will not be immediately rendered
obsolete, it'll just be a less attractive option compared to the "new" and
as time goes on that gap will only widen.
It's too early to say what the properties will be, it takes years of maturity
for these to shake out in a confident way. Given the commoditization of natural
language interfaces that LLMs represent, one prediction is that all software
will need some form of natural language interface at a minimum. For example,
a calendar application with event generation, a command-line tool with
language-guided configuration, a SaaS with an actually helpful assistant,
etc. These are now all relatively easy problems to solve that provide good
value to users, so it may just become a base expectation for software.
So long as incumbents in different industry categories recognize, react, and adapt
to this shift, most will be fine. The core functionality of most applications
is still an important necessary base prior to augmenting with AI. However,
this shift will also represent a huge opportunity for new upstart ventures
to capitalize on slow-moving incumbents.
Bringing Along Old Friends
I believe a really important property of early cloud computing that helped
enable its success is that it had a migration story. You could
"lift and shift"
your way to victory -- to a limited, but sizable extent. Other big
platform shifts like containerization
had a similar property
.
Future evolutions on top of cloud, such as Heroku or more generally
platform as a service (PaaS)
,
didn't have this property. Early PaaS was still very popular, but it didn't represent
the same
platform shift
impact as it was often difficult or impossible
to integrate with "legacy" applications.
To put it another way, new technologies that require throwing away old
technologies are harder to scale to industry-wide impact than new technologies
that somehow bring along old technologies.
Recent AI developments
make existing software better
. Yes, they enable
some revolutionary new takes for certain categories of software too, but they
continue to make "legacy" software better
.
Ignoring various other complaints I have about it, this is another major
reason I was never impressed with the web3 ecosystem. You were either
a
dApp
or you
were not. There wasn't really an in-between. I know in theory some features
could be built "on chain" while others were not, but this is not how that
ecosystem marketed itself as a whole.
In Conclusion
AI may be reaching its "platform shift" moment. It shares a lot of the
same positive qualities and challenges I recognized in early cloud.
If this is true, we're in the extremely early innings of a very long
game. If you take AWS launching S3 and EC2 as "time 0" of the cloud
platform shift, then it took another decade or so for the ecosystem to mature
and for long-time "legacy" incumbents to begin to be significantly disrupted.
Admittedly, I feel the hype around AI has a significantly broader social reach
than cloud, so I think the time horizons on market maturity (if one develops)
are shorter. But still, I predict at least many years of "open window" early-mover
opportunity.
At the very least, I would caution against fully ignoring this one.
