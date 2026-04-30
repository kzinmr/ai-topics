---
title: "TeleMessage customers include DC Police, Andreessen Horowitz, JP Morgan, and hundreds more"
url: "https://micahflee.com/telemessage-customers-include-dc-police-andreesen-horowitz-jp-morgan-and-hundreds-more/"
fetched_at: 2026-04-30T07:01:56.987914+00:00
source: "micahflee.com"
tags: [blog, raw]
---

# TeleMessage customers include DC Police, Andreessen Horowitz, JP Morgan, and hundreds more

Source: https://micahflee.com/telemessage-customers-include-dc-police-andreesen-horowitz-jp-morgan-and-hundreds-more/

I've been digging through the
410 GB of Java heap dumps
from TeleMessage's archive server,
provided
by DDoSecrets. Here's a description of the dataset, some of my initial findings, details about an upcoming open source research tool I'm going to release, and a huge list of potential TeleMessage customers.
First, some background. This "clean OPSEC" saga is
unbelievable
.
Mike Waltz
invited
a journalist into a Signal group full of high-level Trumpers where they discussed and executed
bombing
an apartment building full of innocent people. This led to Congressional
hearings
(about using a Signal group for war, not the war crimes themselves... Congress doesn't really care about those).
Later, Waltz was photographed using TeleMessage SGNL, an Israeli-made knockoff of Signal that archives messages for its customers, and that
lied
about supporting end-to-end encryption. Then TeleMessage was
hacked
,
twice
. The
trivial vulnerability
let anyone on the internet download Java heap dumps from the server. Then, DDoSecrets
released
410 GB of these heap dumps, all from May 4, 2025, and is distributing them to journalists and researchers.
"The trove included material from disaster responders, customs officials, several U.S. diplomatic staffers, at least one White House staffer and members of the Secret Service,"
according
to a Reuters report.
I'm crunching data and writing these newsletters in my free time. If you want to support my work, considering becoming a paid supporter.
Become a paid supporter
What even is this data?
On May 4, a hacker loaded the URL
archive.telemessage.com/management/heapdump
over and over again, each time downloading a different Java heap dump from TeleMessage's server. Yes, the vulnerability was that simple, which is why it took
about 20 minutes
to find and exploit.
Each file is between 130 MB and 291 MB, and is in Java
HPROF format
. The easiest way to see what's inside is using the command line tool
strings
, which extracts all the printable strings from a binary file. If you run
strings
on one of these heap dump files, thousands of lines will scroll by, and some of them will be juicy-looking JSON objects containing plaintext chat messages, along with other interesting data.
This dataset is
not
a copy of all of the data that was stored on the TeleMessage archive server. It only includes fragments of data that happened to be in memory at a single moment on May 4. For example, I might find an interesting-looking message that's part of a group chat, but without any other messages from the same group.
The earliest message I found was from November 15, 2022, and there are messages all the way up until the hack. But about 80% of them are from May 2025. The dataset is mostly a snapshot in time from a specific Sunday earlier this month.
How juicy are we talking?
So far, I haven't found anything from Trump cabinet officials.
While I've found plenty of things that seem interesting and warrant further investigation, so far I haven't uncovered anything that is obviously sensitive or revelatory.
I found a WhatsApp group called "MPD Command Staff" with 46 users in it. There are many messages in this group, but they're all encrypted. (As I described in my
earlier analysis
, some of the individual messages are encrypted.) I looked up some of the phone numbers from this group on
OSINT Industries
and quickly discovered that these people all work for the Metropolitan Police Department in Washington, DC.
I also found a message sent to a Signal group called "US / China AI Race." The Signal group had 100 people in it. I looked some of them up: many of the group members hold prominent positions at major universities, the defense industry, and the military, and all seem to do AI-related work. The message says, "The biggest crime was USG ignored these fabs for two years." That's it. The dataset doesn't include any other messages from this Signal group.
If you're a journalist looking for a tip: Most of the members of the group only listed names, but a few listed phone numbers. If you have access to this data and are looking for a story, why not send the phone-number people Signal messages and ask what this group is about?
As you can see, this dataset probably holds a million different leads. It's too early to tell if any of them will pan out and become something bigger.
How much data are we talking?
The main file in the dataset that contains the compressed heap dumps is
telemessage.7z
, and it's 54 GB. After decompressing it, I end up with a folder with 2,729 heap dump files, taking a total of 384 GB of space. After running
strings
on each of these files, I end up with 83 GB of just text data.
Most of the text data is hundreds of thousands of useless lines like this:
P<E_IN:Ljava/lang/Object;E_OUT:Ljava/lang/Object;>Ljava/util/stream/ReferencePipeline<TE_IN;TE_OUT;>;
(Ljava/util/function/BinaryOperator;Ljava/util/Map;Ljava/util/Map;)Ljava/util/Map;
PMethod java/util/concurrent/ConcurrentNavigableMap.floorEntry(Ljava/lang/Object;)Ljava/util/Map$Entry; is abstract
However, some of the lines are more interesting, like this mildly redacted one:
{"typ":"RawMessage","gatewayReceivedDate":1746332951616,"partner":"NONE","securityContent":null,"sourceService":null,"internalSecurityData":{"version":"0.0.2","internalDecryptionData":{"typ":"nothing","encryptionType":"DO_NOTHING","params":{}}},"networkType":"WHATSAPP_CLOUD_ARCHIVER","sourceType":"WHATSAPP_CLOUD_ARCHIVER","ownerExtClassId":null,"body":{"owner":{"value":"==redacted==","type":"PHONE"},"messageId":"09cfd8142e20170be8a3","messageType":"APP_MESSAGE","messageTime":1746332951000,"sender":{"value":"==redacted==","type":"PHONE"},"recipients":[{"value":"==redacted==","type":"PHONE"}],"direction":"IN","subject":"WhatsApp message from ==redacted== to ==redacted==","textField":{"extractor":{"typ":"WrapperExt","data":"Sure\nI
Notice that this line ends abruptly, with
"data":"Sure\nI
, and that's it. This is a fragment of a JSON object, not the whole thing. These are all over the place. While there's potentially interesting details in broken JSON fragments, I decided to ignore them.
I've been writing software (which I plan to release as open source soon, and I talk about more below) that extracts every single intact JSON object from every single heap dump and stores anything that looks interesting in a PostgreSQL database, ignoring duplicates.
I might be missing stuff. For example, I'm only looking for JSON objects now, but I had previously found
private keys
in the heap dumps. But with just storing interesting-looking JSON, the database ends up taking up 2.7 GB of space.
Statistics
Here are some numbers I've pulled from my database. Please take them all with a grain of salt for the following reasons:
The dataset is not a representative sample of the messages passing through TeleMessage's archive server. Rather, it's what happened to be saved in heap dumps on one specific Sunday.
While I removed millions of duplicate JSON objects while building the database, there are still a lot of duplicates. Sometimes the same message is repeated multiple times, but the JSON objects are slightly different, like because two different people in the same group archived the same message.
I've made some value judgements that appear in the data. For example, some messages include metadata making it clear they're encrypted. Others look encrypted (because the text field is Base64 encoded), but are missing metadata saying one way or the other. I just mark those as encrypted, because they probably are, but I could be wrong.
That said, here's what I've found:
60,012 messages.
36,388 of the messages are plaintext, and 23,624 are encrypted.
1,079 of the message include full attachments (like images, videos, PDFs, contact files, etc.) that are actually part of the dataset. But of those, only 50 of messages are in plaintext. I can, however, actually open and view those plaintext attachments.
Most messages have a
subject
field that's something like, "WhatsApp message from X to Y." Based on these subjects:
37,753 are WhatsApp messages.
2,549 are Telegram messages.
455 are SMS messages.
141 are Signal messages.
95 are something called "App Messages."
26 are MMS messages.
26 are WeChat messages.
16 are voice calls logs.
11,254 are missing
subject
fields.
3,501 group chats, the vast majority of which are WhatsApp.
At least 2,034 are WhatsApp groups.
At least 578 are SMS groups.
At least 256 are Telegram groups.
At least 26 are Signal groups.
At least 10 are WeChat groups.
I'm not sure about the other ~600 groups, though it's possible to determine by manually looking at the messages associated with them.
There are also plenty of individual messages that are clearly part of a group chat, but that didn't include JSON metadata related to it, so they're not categorized as groups, even though they are.
44,503 users. These are either senders or recipients of messages.
At least 25,792 of them use phone numbers as the identifier.
At least 31 of them use email addresses, and at least 391 look like they use usernames.
I'm not sure about another 18,289 of them, but I think most of them are also phone numbers.
17,377 of them include first and/or last names, too.
TeleMessage Explorer
As I mentioned, I've been programming a tool to make researching this dataset easier. It's called TeleMessage Explore, and I'm going to release it as open source soon.
Subscribe to my newsletter
if you're interested in updates.
Since DDoSecrets is only distributing the TeleMessage dataset to journalists and researchers, this tool will only be useful to a small number of people, but I hope that it will make it
so much easier
for everyone who does have access to find good stories.
Hundreds of TeleMessage customers
While sifting through thousands of different JSON objects, I came across what appears to be an OAuth2 validation object. This is data related to someone signing into TeleMessage using a Single Sign-On service.
Here's a validation object with info from someone at JP Morgan. I've redacted his email address and phone number, but I have them.
{
    "validationData": {
        "reason": "OK",
        "validated": true
    },
    "enhancementData": {
        "data": ["==redacted=="],
        "email": "==redacted==@jpmorgan.com",
        "userName": "==redacted==",
        "shortCodes": [],
        "subUserIds": [],
        "activeIdentityProviderWithParams": {
            "activeIdentityProvider": "MICROSOFT",
            "identityProviderParams": {
                "NONCE": {"value": "", "predefined": true},
                "SCOPE": {"value": "JPMC:URI:RS-108400-153785-TMAdminConsoleSSOProd-PROD/openid", "predefined": false},
                "AUDIENCE": {"value": "JPMC:URI:RS-108400-153785-TMAdminConsoleSSOProd-PROD", "predefined": false},
                "CLIENT_ID": {"value": "PC-108400-SID-340413-PROD", "predefined": false},
                "TOKEN_ENDPOINT": {"value": "https://idag2.jpmorganchase.com/adfs/oauth2/token", "predefined": false},
                "TTL_IN_MINUTES": {"value": "30", "predefined": false},
                "VALIDATION_URL": {"value": "https://auth-service-charlie.kapi.telemessage.com/oidc/validate", "predefined": true},
                "EXPIRATION_DAYS": {"value": "0", "predefined": false},
                "METADATA_DOCUMENT": {"value": "https://idag2.jpmorganchase.com/adfs/.well-known/openid-configuration", "predefined": false},
                "TOKEN_EXCHANGE_URL": {"value": "https://auth-service-charlie.kapi.telemessage.com/oidc/exchangeAndValidateToken", "predefined": true},
                "OAUTH2_RESPONSE_TYPES": {"value": "code", "predefined": false},
                "AUTHORIZATION_ENDPOINT": {"value": "https://idag2.jpmorganchase.com/adfs/oauth2/authorize", "predefined": false}
            }
        }
    }
}
When looking for more of these objects, I found that some don't include an
activeIdentityProvider
, like this one. This person works for Scotiabank:
{
    "validationData": {
        "reason": "OK",
        "validated": true
    },
    "enhancementData": {
        "data": [
            "==redacted=="
        ],
        "email": "==redacted==@scotiabank.com",
        "userName": "==redacted==",
        "shortCodes": [],
        "subUserIds": [],
        "activeIdentityProviderWithParams": {
            "activeIdentityProvider": "NONE",
            "identityProviderParams": {}
        }
    }
}
In all, I found 2,545 similar validation objects. I think it's likely that every email address in a validation object belongs to someone working for a TeleMessage customer.
Following is a list of domain names, along with the number of email addresses associated with those domains, in alphabetic order.
(It starts with a16z.com, which is the site for tech venture capitalist firm Andreessen Horowitz. This firm is owned by Silicon Valley billionaire and prominent reactionary Trump supporter Marc Andreessen.)
a16z.com (3 emails)
abgadvisory.com (2 emails)
aipgp.com (4 emails)
alphawaveglobal.com (4 emails)
alternasecurities.com (1 email)
amcgroup.com (1 email)
amerexenergy.com (1 email)
aminagroup.com (3 emails)
amius.com (6 emails)
apg-am.com (1 email)
apg-am.hk (9 emails)
apg-am.sg (1 email)
aramcotrading.us (12 emails)
ardian.com (1 email)
aresmgmt.com (2 emails)
arringtoncapital.com (1 email)
aviorcapital.co.uk (1 email)
aviorcapital.us (1 email)
awincubation.com (2 emails)
axiuminfra.com (1 email)
b2c2.com (2 emails)
bainbridgefs.com (1 email)
ballestasgroup.com (1 email)
bbva.com (3 emails)
bgcg.com (2 emails)
biremecapital.com (1 email)
bisoncapital.com (1 email)
bitbuy.ca (1 email)
bitkraft.vc (2 emails)
blockchaincapital.com (1 email)
boltonglobal.com (5 emails)
borealcm.com (4 emails)
bradescobank.com (8 emails)
brevanhoward.com (2 emails)
br.scotiabank.com (1 email)
bulltick.com (1 email)
burlinv.com (1 email)
cantor.com (6 emails)
cantor.co.uk (1 email)
cbam.coinbase.com (1 email)
cbp.dhs.gov (26 emails)
cercano.asia (4 emails)
cibc.com (6 emails)
clarksons.com (4 emails)
cmcmarkets.com (1 email)
coinbase.com (20 emails)
consultant.kkr.com (1 email)
conti.com (1 email)
contractor101.co.uk (1 email)
contrariancapital.com (1 email)
crownagentsbank.com (5 emails)
dbank.co.il (3 emails)
dc.gov (30 emails)
dfc.gov (10 emails)
digitalbridge.com (1 email)
directhedge.com (1 email)
eastdilsecured.com (1 email)
ecor1cap.com (4 emails)
efhutton.com (1 email)
eni.com (13 emails)
exalogi.com (1 email)
falconcommoditymarkets.com (2 emails)
fibi.co.il (2 emails)
franklintempleton.com (1 email)
freightinvestor.ae (1 email)
freightinvestor.com (5 emails)
galaxydigital.io (7 emails)
gentrustwm.com (2 emails)
gfigroup.com.sg (1 email)
gmail.com (6 emails)
godspeedcm.com (1 email)
golubcapital.com (1 email)
govcapsecurities.com (1 email)
gtbankuk.com (1 email)
gunvorgroup.com (1 email)
hack-vc.com (4 emails)
hbluk.com (4 emails)
hedgepointglobal.com (1 email)
hiddenroad.com (8 emails)
hnwag.com (1 email)
hudson-trading.com (1 email)
hummerfas.com (1 email)
icap.com (3 emails)
icap.com.sg (1 email)
interactivebrokers.com (3 emails)
intercamus.com (1 email)
intercourtage.com (1 email)
investamericap.com (1 email)
itaubba.eu (1 email)
itau.ch (1 email)
jefferies.com (62 emails)
jpmchase.com (1 email)
jpmorgan.com (21 emails)
kkr.com (31 emails)
larrainvial.com (2 emails)
lasallegroupllc.com (3 emails)
lcatterton.com (8 emails)
marathonpetroleum.com (1 email)
marexfp.com (1 email)
maximcapitalgroup.com (1 email)
mbcfrance.com (1 email)
mbcl.com (2 emails)
mcquilling-energy.com (4 emails)
miraeasset.co.id (3 emails)
mitsui.com (1 email)
mlp.com (7 emails)
morganstanley.com (17 emails)
muzinich.com (1 email)
mvfp.net (1 email)
nebari.com (1 email)
nice.com (1 email)
nirbhaucorp.com (3 emails)
northisland.ventures (2 emails)
nuveen.com (1 email)
nuveenglobal.com (4 emails)
nycapmarkets.com (1 email)
opco.co.il (1 email)
p66.com (7 emails)
panteracapital.com (1 email)
paradigm.xyz (4 emails)
pa.scotiabank.com (48 emails)
petrobras.com (5 emails)
petrobras.com.br (1 email)
pimco.com (1 email)
principal.com (1 email)
privatewealthadvisorsinc.com (1 email)
psc.com (1 email)
pvm.co.uk (10 emails)
pwafamilyoffice.com (1 email)
reynoldschannel.com (1 email)
rhbgroup.com (5 emails)
ribbitcap.com (1 email)
rjobrien.com (1 email)
rmb.co.uk (2 emails)
rmbsecurities.com (1 email)
rohrpwm.com (1 email)
rsgcorp.com (1 email)
safra.com (13 emails)
scotiabank.cl (34 emails)
scotiabankcolpatria.com (71 emails)
scotiabank.com (126 emails)
scotiabank.com.mx (164 emails)
scotiabank.com.pe (45 emails)
scotiacb.com.mx (1 email)
scotiawealth.com (6 emails)
scotiawealth.com.mx (5 emails)
scsotc.com (2 emails)
seaportglobal.com (1 email)
searleco.com (1 email)
seba.swiss (1 email)
senatorlp.com (1 email)
sequencefinancialspecialists.com (1 email)
sg.pimco.com (1 email)
smarsh.com (4 emails)
smbcgroup.com (2 emails)
soteriasolutions.us (15 emails)
sperrycapital.com (1 email)
standardbank.co.za (6 emails)
statetrust.com (1 email)
steadview.com (1 email)
sunglobal.co.uk (1 email)
sunmountaincapital.com (1 email)
tcv.com (2 emails)
telemessage2020.onmicrosoft.com (9 emails)
telemessage.com (13 emails)
thestrategicfinancial.com (1 email)
tigerglobal.com (2 emails)
tm.com (4 emails)
totalenergies.com (92 emails)
tower-research.com (1 email)
tpicap.com (6 emails)
traditionasia.com (1 email)
tradition.com (4 emails)
tridentotc.com (1 email)
tullettprebon.co.jp (1 email)
tullettprebon.com (10 emails)
tyruscap.mc (1 email)
ubauk.com (3 emails)
uk.pimco.com (1 email)
united-icap.com (6 emails)
us.icap.com (1 email)
usss.dhs.gov (2 emails)
uyanapartners.com (1 email)
valley.com (8 emails)
vistaequitypartners.com (4 emails)
vitol.com (8 emails)
vlmsofts.com (1 email)
who.eop.gov (1 email)
williamblair.com (5 emails)
wonder.fi (1 email)
worldquant.com (1 email)
If you found this interesting,
subscribe
to get these posts emailed directly to your inbox. If you want to support my work, consider becoming a paid supporter.
