---
title: "Revisiting Leander v Sweden and Big Brother Watch"
url: "https://berthub.eu/articles/posts/revisiting-leander-and-big-brother/"
fetched_at: 2026-11-11T10:01:31.673331+00:00
source: "berthub.eu"
tags: [blog, raw]
---

# Revisiting Leander v Sweden and Big Brother Watch

Source: https://berthub.eu/articles/posts/revisiting-leander-and-big-brother/

Governments in Europe are
gearing up
to
increase their bulk surveillance capabilities
. One check on their ambitions is the
European Convention on Human Rights
. In this piece, I want to highlight recent jurisprudence from the European Court of Human Rights (ECtHR), and interpret the case law in light of current cybersecurity and AI developments. This interpretation may have relevance for future evaluations of SIGINT and other bulk data collection programs. Because what seemed reasonable a few years ago may no longer be so.
The short version: Many European government agencies collect and store vast amounts of data relating to people’s private and family lives. Most of this data will never be useful or used, but a tiny part may be
selected
for further processing and intelligence work. The ECtHR has long argued that the mere storage and gathering of such data already infringes on Article 8 rights, and in 2021 argued that this infringement is real but manageable, since no one is yet looking at that data. In the present piece I argue that in 2026 there is a hugely and provably increased risk when merely gathering and storing data. The idea of
an agency getting hacked and leaking classified data
is no longer far-fetched, and legislators and courts would do well to recalibrate their appreciation of the risks of agencies hosting piles of data that might well get leaked, or shared on cloud platforms. Similarly, data collection facilities operated on behalf of the US government
have provably been compromised by China-related actors
, underscoring the risk involved in merely collecting data. Courts and legislators should take this changing landscape into account, and demand strong and technical oversight. Finally, specific State’s attempts to extend the ‘mere storage’ regime to ‘
mere hacking and installing surveillance software
’ should be given a harsh look.
Article 8 of the
European Convention on Human Rights
:
1 Everyone has the right to respect for his private and family life, his home and his correspondence.
2 There shall be no interference by a public authority with the exercise of this right except such as is in accordance with the law and is
necessary in a democratic society
in the interests of national security, public safety or the economic well-being of the country, for the prevention of disorder or crime, for the protection of health or morals, or for the protection of the rights and freedoms of others.
These two sentences have led to hundreds or even thousands of pages of relevant discussion, for example in the useful publication
Guide on Article 8 of the European Convention on Human Rights
(specifically paragraphs around 680).
For the purposes of the present publication, the concept of ’necessary in a democratic society’ is of prime importance.  The court explained this in
Gillow v. The United Kingdom
:
The notion of necessity implies a pressing social need; in particular, the measure employed must be proportionate to the legitimate aim pursued.
In
Leander v. Sweden
the court noted:
However, the Court recognises that the national authorities enjoy a margin of appreciation, the scope of which will depend not only on the nature of the legitimate aim pursued but also on the particular nature of the interference involved. In the instant case, the interest of the respondent State in protecting its national security
must be balanced against the seriousness of the interference with the applicant’s right to respect for his private life
So, the right to respect of private life and correspondence can be interfered with if necessary, and the level of interference that is acceptable increases with the gravity of the State’s (national security) interests.
Targeted and bulk infringement
When performing the Article 8 balancing act, it is clear that a country can perform full surveillance on a murder suspect. There is a pressing social need to convict this person (if guilty!) and get them off the streets. This is typically codified in national law by stating that (say) phone surveillance is warranted for crimes carrying a penalty of more than x years.
In addition to such targeted surveillance, many states have intelligence, police, military and security agencies that also perform
bulk
surveillance and data gathering, where almost all data captured and/or stored is in no way related to any ongoing crimes or worrying activities. Agencies are authorized to perform analysis on that data and
selecting
specific bits of it for further scrutiny, all to enhance (national) security.
It is not easy to square such bulk processing of data with Article 8. How do you justify collecting and storing large amounts of data about people not suspected of any (future) crime? In ECtHR jurisprudence, the theory has grown that the infringement caused by processing data depends on the level of scrutiny performed on that data, and might initially be so limited that collecting and/or storing data in bulk is acceptable
It could be argued that this theory was formed retroactively to somehow legalise historical and existing bulk interception regimes
.
In Paragraph 325 of
Big Brother Watch and Others v. The United Kingdom
the Grand Chamber proposed separating the processing in four stages:
(a)  the interception and initial retention of communications and related communications data (that is, the traffic data belonging to the intercepted communications);
(b)  the application of specific selectors to the retained communications/ related communications data;
(c)  the examination of selected communications/related communications data by analysts; and
(d)  the subsequent retention of data and use of the “final product”, including the sharing of data with third parties.
The Grand Chamber also stated that “Article 8 applies at each of the above stages. While the initial interception followed by the immediate discarding of parts of the communications does not constitute a particularly significant interference, the degree of interference with individuals’ Article 8 rights will increase as the bulk interception process progresses”.
As we progress from (a) to (d), both the scrutiny of communications and the infringement of the Article 8 rights increase. In graph form:
In Big Brother Watch, the Grand Chamber also reiterated a key insight from the
Leander
ruling:
In this regard,
the Court has clearly stated that even the mere storing of data relating to the private life of an individual amounts to an interference within the meaning of Article 8
This puts a useful floor under the balancing that States need to perform: even if data is only stored, there is already an interference with the rights protected by Article 8. This means that merely storing data relating to someone’s private life always needs justification, and requires at least some ‘pressing social need’ for it to be warranted.
In graph form this looks like this:
So how does data that is “merely stored” infringe on rights? There are a number of reasons:
Potential for internal abuse: data that is available might be used for unauthorized purposes (political interference, for example), either by rogue employees or by an agency that has lost its way. Data that is not there can’t be used for that.
External abuse: an agency might get hacked, or the data might leak in another way
Chilling effects
“The Chilling Effects of Surveillance and Human Rights: Insights from Qualitative Research in Uganda and Zimbabwe”, Journal of Human Rights Practice, Volume 16, Issue 1, February 2024, Pages 397–412
: if people know their data is being recorded and stored, this will cause them to mind their words and self-limit their freedom of expression
Regime change: we do not know who will be in charge in the future, and if these are non-democratically minded powers, having all this data on citizens around might help them in undesirable ways
A police officer recently related to me that he was not worried about mere data leaks, since he had nothing to hide. To which I add that it is quite selfish to say such things, since many people in fact do have something important to hide. The recent
T-Mobile/Odido data leak here in The Netherlands
for example might be extremely harmful to you if you were trying to hide your new address from your abusive ex.
As an aside, building on the prevailing theory that merely capturing and storing data is itself only a slight interference, a proposed new Dutch intelligence law includes very lightly regulated powers to hack into phones and computers, and even to install surveillance software on them. The regulatory regime is so light that individual team leads can authorize such “pre-hacking”. The Dutch agencies would only need regular oversight approved permission once the hack delivers data meant to enter the analysis stage.
What has changed since 1987
The 1987 Leander case was about physical (paper) files that were locked down and stored in national security facilities in Sweden, data that was unlikely to ever get stolen or leaked or sold online. And even then the court decided that this data formed an infringement that needed justification.
Although intelligence agencies have previously suffered from penetration, and leaked data, such occurrences were rare. And leaks were typically of specific high-value data, relating to targets of investigation, and not to the bulk of the population. Of note however, in 2015 the files of the US agency coordinating security clearances got hacked wholesale, leaking the most private details (and fingerprints) of millions of Americans, apparently to China
2015 Office of Personnel Management data breach
, Wikipedia
.
As of 2026, almost all data is stored in computers. And, such data is ever more stored online or in clouds, even within military, police and
astoundingly also intelligence agencies
“Deutsche Nachrichtendienste setzen auf Google”, Tagesschau, 26 October 2026
.
The advent of AI-powered hacking has led to a massive increase in the discovery of security weaknesses
“AI is accelerating and amplifying threats: immediate action is necessary”
, Dutch National Cyber Security Centre
. Such weaknesses are being addressed, but this is not keeping up with the rate of discovery of new weaknesses
“Attackers are exploiting AI faster than defenders can keep up, new report warns”
, Booz Allen Hamilton via Cyberscoop
. Especially older systems are at risk of compromise therefore. Governments themselves are sounding the alarm as they find that they can’t keep up with the latest threats
“Government websites go dark after AI-discovered flaw sparks security scramble”
, Reuters
.
As such, the risk of leaking data that is ‘merely stored’ has increased vastly. This is no longer about paper stored in vaults. It is about storing data on platforms that are getting hacked left and right.
An additional risk: collection
Before even the ‘mere storage’ of data can begin, it has to be collected. Collecting such data necessarily involves communicating with the outside world, particularly outside networks that are by now infested with (state) actors. This means that the ‘mere collecting’ of data is already a risk. Quoting Wikipedia:
On August 27, 2024, The Washington Post reported that at least two major internet service providers in the United States had been compromised by Chinese hackers. It was later reported that the hackers affected at least nine telecommunications firms in the U.S., including AT&T, Verizon, Lumen Technologies, and T-Mobile, and had also affected dozens of other countries. […] The hackers
were also able to access wiretapping systems
used to conduct court-authorized wiretapping. The attack was later attributed to the Salt Typhoon advanced persistent threat actor linked to China’s Ministry of State Security (MSS). [..] The hackers
obtained an almost complete list of phone numbers being wiretapped
.
The threat was so enormous that the US government
recommended people use “encrypted messaging apps” instead of phone calls
.
Source:
New York Times
Later,
together with most western intelligence agencies, the US government released guidance
“Countering Chinese State-Sponsored Actors Compromise of Networks Worldwide to Feed Global Espionage System”, by a huge collection of intelligence and security agencies
on the many ways in which the “Salt Typhoon” Chinese actor had compromised telecommunication companies, including the wiretapping interfaces.
As a further example, all three major Dutch telecommunication companies were found to have serious security breaches in the wiretapping facilities they maintain for government use (
Vodafone Ziggo
,
KPN
,
Odido/T-Mobile
Reports from the Dutch Authority for Digital Infrastructure
RDI
).
The upshot of this is that third parties have provably gained access to our protected private and family lives through the act we might call “mere collection capability”.
So respectfully, in 2026 we can disagree with the Court when it stated in 2021 that “initial interception followed by the immediate discarding of parts of the communications does not constitute a particularly significant interference”. These days, in practice, such interception (capability) does constitute a significant risk.
What the court has said on implementation
In
Podchasov v. Russia
(specifically paragraph 80), the Court has made it clear that technical details matter greatly in determining if the infringement of an individual’s private communication is proportional to the aims.
For the ‘mere storing of data’, this may mean that States should in their procedures protect data in ways that are proportional to the 2026 information security landscape, which is dire. This means agencies can not simply state they are being very careful with the data, they should provably implement the very best practices in an attempt to keep their data from leaking or being stolen. If they do not provably do so, it may no longer be proportional to even store any potentially infringing data for any period of time.
Similarly, given the examples above of lax security during the act of
merely collecting
data, agencies must provably have done their utmost to not make the interception process itself a risk factor.
Both for collecting and storing data, determining if security levels are adequate involves capable oversight that has the time, budget, access and specifically also the expertise to independently verify if agencies are performing well enough on these fronts. It should be noted that “compliance on paper”, possibly through lengthy written procedures, does not deliver provably secure practices, which in turn could lead to tangible harm to Article 8 rights.
What this means for Article 8
Whereas it was already clear that merely storing data relating to the private life of an individual amounted to an interference of Article 8, today this interference is far greater than in 1987. There is a significant chance that merely stored data will leak, and it might subsequently even get sold, or held for ransom.
In addition, building the very infrastructure to collect such data to be merely stored is a proven and significant risk factor. These two factors lead to the following “infringement graph”:
Note well that infringement starts at collection and storage already
Any courts, national or the ECtHR itself, are well advised to take these two factors into account when performing the balancing between a State’s need to protect its (national security) interests, against the right for respect for private and family life and correspondence.
Conversely, States revamping their bulk intercept/national security frameworks
The new Dutch intelligence law goes too far
, Bits of Freedom
Unconstitutional? German intelligence to receive more powers
, Deutsche Welle
would do well to not skimp on both technical and legal oversight. It seems likely courts will include ’technical quality of oversight’ as a factor, especially if they want to stick to the model where bulk selection & data storage are regarded as ’not particularly infringing’.
Courts will in all likelihood take note of external developments and come to new conclusions about the proportionality of mere bulk data collection & storage. I sure hope they will in any case!
Some notes on (really) technical oversight
When I was
a member of the regulatory powers commission for the Dutch intelligence and security services
, I was tasked with connecting technical and legal realities. I remember that time fondly, and I hope that this post, similar to my former job, contributes to a better understanding of (bulk) interception jurisprudence and law.
Of note,
this commission in the Netherlands
(so far) is staffed with (former) judges, but also has a full technical member (like I was) to make sure decisions on complex hacking or interception operations are taken by a well informed commission, one that fully understands what is going on. This technical member operates as part of the “non-judicial body” (in the words of the ECtHR), but does not need to have a formal legal background.
I can recommend this setup for all courts or non-judicial equivalents that have to perform oversight on intelligence and security agencies. It is not enough to have technical support. The technical knowledge must be a 100% mandatory and integral part of the court or commission.
In 2026, it would be really odd to argue that such a court or commission should be headed exclusively by legal professionals.
Further reading
Big Brother’s Little, More Dangerous Brother
(Mark Klamberg), an analysis of Centrum för Rättvisa v. Sweden - key quote: “The lack of proper scrutiny [by the court] may be explained in several ways, including the potential absence of technological knowledge and perception that national security is ultimately a matter for the executive and not the courts. This begs the question whether courts – domestic and international – will ever be in a position to exercise effective control when states are conducting surveillance for national security reasons”
