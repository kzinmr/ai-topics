---
title: "A Cautionary Tale About Data Breach Claims, Verification and Carhartt"
url: "https://www.troyhunt.com/a-cautionary-tale-about-data-breach-claims-verification-and-carhartt/"
fetched_at: 2026-08-26T10:00:59.626279+00:00
source: "troyhunt.com"
tags: [blog, raw]
---

# A Cautionary Tale About Data Breach Claims, Verification and Carhartt

Source: https://www.troyhunt.com/a-cautionary-tale-about-data-breach-claims-verification-and-carhartt/

You're not going to believe this, but turns out you can't always take criminals at their word. Actually, I'll walk that back a bit as it may not even be the cybercrime guys who got this wrong, but it all starts here:
My usual Have I Been Pwned (HIBP) workflow after a breach emerges is to run
our open source Email Address Extractor tool
over the corpus of data, get a count of the unique addresses then drop it into the processing pipeline. Having a count helps prioritise: it's roughly the same effort to process a breach with 10M addresses in it as it is 100k addresses, but we obviously reach 100x more people with the larger corpus so that goes first. So, following the release of the Carhartt data above, I ran the tool and got 24,876,077 addresses. That's a biggy, let's dive in.
One of the first things I do when analysing a breach is look for news and industry commentary. Once you get through all the results for class actions (
ugh
), you usually find various other services and news sites reporting on the incident. One such example (which I won't name, because they're wrong) cited a very similar number to my initial pass, which at face value, reinforced my thinking. But here's where it all takes a turn because, inevitably, this is where the other analysts stopped...
I've been using OpenClaw pretty extensively this year to help with a number of tasks, including breach analysis. Here's how I normally begin (timestamps are AEST and yes, I called it "PwnedClaw"):
[24/08/2026 17:30] Troy Hunt: Let's look at the ShinyHunters Carhartt breach. I'm seeing nearly 25M unique email addresses so it's very large, tell me about what they do.
  
[24/08/2026 17:30] PwnedClaw: Carhartt is an American workwear brand founded in 1889, headquartered in Dearborn, Michigan. They make rugged, durable clothing primarily for tradespeople and outdoor workers: heavy-duty jackets, bibs, coveralls, work pants, boots, and accessories. Think construction workers, farmers, hunters.

They've also crossed over into streetwear/fashion in recent years (particularly through Carhartt WIP, their Work In Progress line), which massively expanded their demographic beyond blue-collar workers into urban fashion, skateboarding, and hip-hop culture. That crossover likely explains a 25M email count — they're not just selling to contractors anymore, they're a mainstream lifestyle brand.

Strong US base but significant global presence, especially in Europe where WIP is huge.

For HIBP context: broad demographic mix (blue-collar workers + fashion/streetwear), real names, physical addresses, and purchase history are likely present given it's a retail breach. Want me to pull the tracker entry for current status?
Ok, cool, nothing too revolutionary there. Let's start analysing the data, and the first thing I do is begin with the report of our open source
Email Address Extractor
tool, which lists every file an address was found in, and then how many unique ones are in there:
[24/08/2026 17:32] Troy Hunt: Let's start looking at data, and we'll begin with the email extractor report at "\scratch\Carhartt\Carhartt.txt.report.txt"
  
[24/08/2026 17:32] PwnedClaw: Interesting. The data is from Databricks (their analytics/data lakehouse platform) and follows the TPC-DS benchmark schema (tpcds_sf1000) — that's a standard retail analytics benchmark format. The "sf1000" means scale factor 1000, which is massive.

Key observations:

• All emails are in customer_chunk_XXXX.csv files, numbered 0000-0599+, so ~600 chunks
• Each chunk has ~19,300 unique emails, remarkably uniform distribution
• ~600 chunks × ~19,300 = ~11.6M from this directory alone — but you said ~25M total, so there are likely more directories

The TPC-DS schema is telling — it means this was Carhartt's customer analytics warehouse in Databricks, not their production transactional database. TPC-DS models: customer demographics, store sales, web sales, catalog sales, dates, etc. So the data likely includes purchase history and behavioral analytics on top of PII.

Want me to look at an actual chunk file to see what columns are present?
Think of it as using the AI to distil large volumes of information down into something much more workable. In this case, I gave it four of the files in question and let the analysis run:
[24/08/2026 17:33] PwnedClaw: The columns from the TPC-DS customer table:

• c_customer_sk / c_customer_id — internal IDs
• c_current_cdemo_sk — customer demographic key (links to demo table with age/gender/education/marital status/income band)
• c_current_hdemo_sk — household demographic key
• c_current_addr_sk — current address key (links to full address table)
• c_first_shipto_date_sk / c_first_sales_date_sk — date of first purchase/shipment
• c_salutation — Mr/Mrs/Miss/Sir etc.
• c_first_name / c_last_name
• c_preferred_cust_flag — loyalty/preferred customer flag
• c_birth_day / c_birth_month / c_birth_year — full DOB
• c_birth_country
• c_login — empty in the samples
• c_email_address
• c_last_review_date_sk / c_last_review_date

So: full name, email, DOB, salutation, birth country, preferred customer status, first purchase date. Address is a foreign key here (in a separate address table that's presumably also in the dump).

Notable: c_login appears empty — so no passwords in this table. DOB is split across three columns which is a bit unusual but all three are there. Birth year goes back to 1949 in the sample, so this spans a wide age range.

Want me to check how many rows have DOB fully populated, and whether there are other tables in the dump (address, demographics) in what you have locally?
I'll save you from all the to-and-fro of my questions and PwnedClaw's responses, here's where it gets interesting and where AI plays a genuinely valuable role:
[24/08/2026 17:41] PwnedClaw: TLD anomaly worth flagging:

• 4M .edu and 3.9M .org is extremely high for a retail brand. That's likely noise from the TPC-DS synthetic data generation mixed with real records, or it could indicate Carhartt ran promotions targeting institutions. Worth sanity checking a sample of those.

Want me to pull 20 random .edu and .org samples to see if they look real or synthetic?
Huh, yeah, that feels odd. Let's drill down further, and just a quick caveat: I'm
highly
confident that all the data I'm about to show is fabricated and that I'm not inadvertently putting someone else's PII on display here.
[24/08/2026 17:47] Troy Hunt: Give me some examples of what you consider synthetic addresses
  
[24/08/2026 17:48] PwnedClaw: From the earlier sample:

Clearly synthetic (TPC-DS generated):

• roy.griffin@mbfhz82d0vkpes4x.edu — random hex-like domain
• violet.day@ob7.edu — 3-char alphanumeric
• michael.ware@c.edu — single character domain
• manuel.baugh@p.edu — single character domain
• april.garza@r3zc1yf6i2lxfg.edu — random alphanumeric
• craig.hodge@nrvnrtanujylkigl.edu — random consonant string
• ted.walker@9q3ulo9h987zp.edu — starts with digit, mixed
• michelle.larue@lkvb06fkzsjv.org — random alphanumeric
• joel.maldonado@y8rlxnc.org — short random alphanumeric

The pattern is consistent: real-looking Firstname.Lastname local part (from TPC-DS customer name generation) grafted onto a completely random/gibberish domain. The local parts look plausible but the domains have no vowel patterns, random digit insertion, or are implausibly short (single characters).

The tell: TPC-DS generates customer emails by concatenating real name fields with random domain strings. So you get sally.smith@uea8muo3gx9udizg.edu — Sally Smith is plausible, but no .edu institution has that domain.

Want me to build a filter that identifies synthetic domains specifically (gibberish detection) and get a precise real vs synthetic split?
Oh yeah, that's definitely junk. It was enough for me to start trawling through the data myself, old-school, like I used to, well, before earlier this year! And that's where I found data like this:
c_customer_sk,c_customer_id,c_current_cdemo_sk,c_current_hdemo_sk,c_current_addr_sk,c_first_shipto_date_sk,c_first_sales_date_sk,c_salutation,c_first_name,c_last_name,c_preferred_cust_flag,c_birth_day,c_birth_month,c_birth_year,c_birth_country,c_login,c_email_address,c_last_review_date_sk,c_last_review_date
11270429,AAAAAAAANBJPLKAA,1423814,7001,19788,2451033,2451003,Miss,Marina,Tucker,Y,13,3,1968,BENIN,,Marina.Tucker@xgpgHqAu.com,2452499,2452499
It's the same sort of .edu pattern but not on a .edu TLD. First name, last name, random domain name. And "Benin"?! I'll save you Googling it like I had to, it's a small country in West Africa and if I'm guessing, not a major Carhartt market.
[24/08/2026 17:51] Troy Hunt: Yeah, something smells here, there are screwy domains in addresses like this too: Marina.Tucker@xgpgHqAu.com
  
[24/08/2026 17:52] PwnedClaw: That's a much bigger problem than I initially thought. The frequency analysis confirms it:

• 54.8% of addresses (13.6M) are at domains appearing 100+ times — these are real
• 45.2% (11.25M) are at domains appearing fewer than 100 times — and 8.4M of those contain digits

So the synthetic pattern isn't confined to .edu/.org at all — it's throughout .com and everything else too. Marina.Tucker@xgpgHqAu.com is the same TPC-DS generation, just with .com slapped on.

The 32% figure I gave you earlier was a significant undercount. The real split looks closer to:

• ~13.6M real addresses (domains with 100+ occurrences)
• ~11.25M synthetic (single-use gibberish domains across all TLDs)

That's roughly 45% junk across the whole corpus, not 32%.

For HIBP the headline number would be around 13-14M rather than 24.8M. Want me to produce a clean filtered list of just the real addresses for an accurate count?
And the more I probed, the more it all unravelled:
[24/08/2026 17:53] Troy Hunt: I want you to get a distinct list of all domains with a count next to each one showing how many addresses are on it. This is starting to smell bad.
  
[24/08/2026 17:54] PwnedClaw: Done. 10.35M unique domains written to:

scratch/Carhartt/domain-counts.txt

Format is countdomain, sorted by count descending. So the top of the file is gmail.com (http://gmail.com/) at 7M+, and the long tail is all the single-occurrence gibberish. Your HIBP domain dataset should make it very obvious where the cliff edge is between known-real and never-seen-before.
  
[24/08/2026 17:58] Troy Hunt: There's an extraordinary long tail of domains with only 1 address. Also look at the country of birth next to the add addresses; places like Myanmar, Latvia and PNG are just really odd in terms of likelihood.
  
[24/08/2026 17:58] PwnedClaw: That country distribution is damning. Here's what's wrong with it:

97.6% of domains appear exactly once — that's not a long tail, that's a signature. Real breach data from a retail company would have thousands of addresses on corporate domains, hundreds on ISP domains, a natural power law. Instead you have 10.1M singleton domains. That's pure TPC-DS generation.

The birth country data is the other nail in the coffin. Look at what's in those 4 chunk files:

• Venezuela, Nicaragua, Qatar, Montenegro, Lesotho, Gambia, Norfolks Island, Réunion, Comoros, Western Sahara, Palau...
• United States appears only 407 times — tied with Canada, both dwarfed by places like Antigua and Barbuda and Lesotho
• The distribution across 211 countries is essentially uniform — ~380-420 per country

That's textbook TPC-DS. It generates customer records with birth countries sampled uniformly from the full ISO country list. No real Carhartt customer database would have more customers born in Montenegro than the United States.

Bottom line: What you have here looks like real Carhartt customer records (the carharttdonotship.com, carhartt.com domains, the 70% HIBP hit rate on freemail addresses) that were stored in Databricks alongside TPC-DS benchmark data that was run against the same schema. ShinyHunters grabbed the whole Databricks dump without distinguishing real customer data from the benchmark test data sitting in the same tables.

The real customer data is in there, but it's heavily contaminated with synthetic TPC-DS records. Your domain frequency analysis from HIBP will be the cleanest way to separate them.
Annoying AI sentence structure aside ("that's not [one thing], that's [this other thing]"), this is just gold. And PwnedClaw gives ShinyHunters a bit of a free pass too: these guys just grabbed and published everything without realising there was a bunch of synthetic data in there. But there's one more smoking gun:
[24/08/2026 18:02] Troy Hunt: Also look at the distribution of birth year - there are way too many people with early 1900's entries, got any stats on that?
  
[24/08/2026 18:03] PwnedClaw: Birth year stats are conclusive. The distribution runs 1924-1992 and is perfectly flat — roughly 1,050-1,194 per year, every single year without exception. That's not population data, that's a random number generator with a fixed range.

A real Carhartt customer base would be heavily weighted 1965-1995, almost nothing pre-1950, and the pre-1924/post-1992 cutoffs wouldn't exist at all. Instead you get mathematically uniform coverage of 69 years. TPC-DS again.

Here's the full picture of what we now have as synthetic indicators — every single one points the same direction:

| Signal                        | Finding                                                          |
| ----------------------------- | ---------------------------------------------------------------- |
| Domain singletons             | 97.6% of domains appear exactly once                             |
| Synthetic TLDs                | 32% of addresses on .edu/.org with gibberish domains             |
| Gibberish .com domains        | e.g. Marina.Tucker@xgpgHqAu.com                                  |
| Firstname.Lastname pattern    | 50.4% — should be ~10-15% in real retail data                    |
| Birth country distribution    | Perfectly uniform across all 211 ISO countries, US = 407 records |
| Birth year distribution       | Perfectly flat 1924-1992, ~1,100/year                            |
| carharttdonotship.com         | Proves real Carhartt data IS present                             |
| 70% HIBP hit rate on freemail | Proves real records are mixed in                                 |

The conclusion is pretty solid: this is a real Carhartt Databricks breach, but the TPC-DS benchmark data was co-located in the same schema and ShinyHunters (and every aggregator after them) grabbed it all without knowing what they were looking at.
It would have been so easy just to dump this all into HIBP, put out social posts with a big headline number and be done with it, but it'd also be completely wrong. And here's what's really worrying about watching other people do exactly this: headline numbers get misrepresented, victim organisations are unfairly reported on (news headlines with the HIBP number often follow quickly), I run the risk of attracting the ire of the company for inaccurate reporting, and the whole thing just becomes a mess.
So, was Carhartt actually breached, and did ShinyHunters fabricate the data?
Almost certainly "yes" and then, almost certainly "no", and both positions are supported by previous ShinyHunters form. These guys are approaching 100 breaches sitting on their Tor site (all of which I've reviewed), and I'm yet to see a single one with data they've fabricated. These guys have a track record of successfully gaining access to large orgs and dumping data that genuinely came from the claimed origin. Not to trivialise their criminal extortion campaigns, but misrepresenting the scope of their activities would be bad for business in the same way that not following through on threats and dumping data when they don't get payment would be. This presents an alternate theory PwnedClaw has already touched on: Carhartt simply had a bunch of test data sitting in their Databricks instance.
Going back to the output of our tool, here are the largest files which we now know have junk data in them:
Unique addresses per file:
\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\tables\samples\tpcds_sf1000\customer_chunk_0309.csv: 19,402
\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\tables\samples\tpcds_sf1000\customer_chunk_0589.csv: 19,372
\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\tables\samples\tpcds_sf1000\customer_chunk_0568.csv: 19,362
\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\tables\samples\tpcds_sf1000\customer_chunk_0460.csv: 19,360
\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\tables\samples\tpcds_sf1000\customer_chunk_0263.csv: 19,358
\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\tables\samples\tpcds_sf1000\customer_chunk_0584.csv: 19,358
\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\tables\samples\tpcds_sf1000\customer_chunk_0350.csv: 19,357
\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\tables\samples\tpcds_sf1000\customer_chunk_0264.csv: 19,356
\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\tables\samples\tpcds_sf1000\customer_chunk_0278.csv: 19,356
There were 600 of these files, then another
1,200
files with similar data in this common path:
C:\ShinyHunters\shouldve_paid_the_ransom_carhartt_shinyhunters\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\20260801_033207\samples\tpcds_sf1000\customer\chunk_0116.csv: 9,689
C:\ShinyHunters\shouldve_paid_the_ransom_carhartt_shinyhunters\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\20260801_033207\samples\tpcds_sf1000\customer\chunk_0921.csv: 9,689
C:\ShinyHunters\shouldve_paid_the_ransom_carhartt_shinyhunters\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\20260801_033207\samples\tpcds_sf1000\customer\chunk_1172.csv: 9,689
C:\ShinyHunters\shouldve_paid_the_ransom_carhartt_shinyhunters\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\20260801_033207\samples\tpcds_sf1000\customer\chunk_0529.csv: 9,688
C:\ShinyHunters\shouldve_paid_the_ransom_carhartt_shinyhunters\shouldve_paid_the_ransom_carhartt_shinyhunters\databricks\databricks_dump\20260801_033207\samples\tpcds_sf1000\customer\chunk_0054.csv
Once excluded, the unique address count plummeted to just 13,306,258 results. That's a 47% drop from the 24M+ number we started at... and it's still too high.
I
always
eyeball the distinct list of email addresses after they're exported by our tooling. Call me old-fashioned, but I still reckon there are things I'll see with my experienced human eyes that the AI will miss (at least, for now). And it missed these:
[25/08/2026 08:47] Troy Hunt: Back on Carhartt, we have a lot of instances like these where the same alias appears across 3 different versions of the domain. I'm writing this up in a blog post, help me explain to the readers what's going on here and why it's inflating the numbers:

[unique alias]@carhartt.com
[unique alias]@carhartt.mail.onmicrosoft.com
[unique alias]@carhartt.onmicrosoft.com

  [25/08/2026 08:47] PwnedClaw: When someone creates an email account at a company like Carhartt, Microsoft 365 (which Carhartt uses for email) automatically creates the mailbox under multiple domain identities simultaneously:

• carhartt.com (http://carhartt.com/) — the primary, human-facing domain (the one you'd put on a business card)
• carhartt.onmicrosoft.com (http://carhartt.onmicrosoft.com/) — Microsoft's default domain, automatically assigned to every Microsoft 365 tenant, exists whether you want it or not
• carhartt.mail.onmicrosoft.com (http://carhartt.mail.onmicrosoft.com/) — a routing domain Microsoft uses internally for mail flow

All three resolve to the exact same person, the same inbox, the same [unique alias]. It's not three people — it's one person with three email addresses that all deliver to the same place.

The inflation problem: when a breach dataset is exported or scraped, all three variants can appear as distinct rows because technically they are distinct email addresses, even though they represent a single individual. A naive deduplication (or none at all) counts [unique alias] three times instead of once.

The fix HIBP applies is normalising to the primary domain and deduplicating on that — but it requires knowing which domains are Microsoft routing aliases, which isn't always obvious, and the breach data doesn't label them as such.
I've previously removed these manually by regex'ing them out myself, but let's not repeat laborious tasks that can be automated away:
[25/08/2026 15:39] Troy Hunt: Cool, delete all those from the file at "\scratch\Carhartt\Carhartt.txt" and we'll keep refining that until it's better sanitised. Tell me how many rows you remove as well.
  
[25/08/2026 15:39] PwnedClaw: Done. Removed 5,736 rows, down from 13,306,258 to 13,300,522.
Continuing the eyeballing work, another pattern emerges:
[25/08/2026 15:41] Troy Hunt: I'm seeing a lot of addresses that begin with "deactivate-". How many are there and what can you tell me about this pattern?
  
[25/08/2026 15:41] PwnedClaw: 288,982 of them. The pattern is clear: these are accounts that were deactivated in Carhartt's system (likely an e-commerce platform or loyalty/membership system), where instead of deleting the record, they prefixed the email address with deactivate- to mark it as inactive while preserving the row. It's a common soft-delete pattern — keeps the data for audit/history purposes but flags the account as no longer active.

The implications for HIBP:

• These are real email addresses that no longer exist in that form — deactivate-[unique alias]@carhartt.com is not a deliverable address
• The real person's address is just [unique alias]@carhartt.com, which may already appear separately in the breach data
• Notifying deactivate-* addresses would bounce or go nowhere

Worth removing them, but worth checking first how many have a corresponding non-deactivated version in the file — if most do, they're pure duplicates and safe to drop. Want me to check that?
  
[25/08/2026 15:42] Troy Hunt: How many already appear without that prefix?
  
[25/08/2026 15:42] PwnedClaw: 285,808 of the 288,982 already have a non-prefixed version in the file — that's 99% pure duplicates. Only ~3,174 appear exclusively as deactivate- with no corresponding active address.
[25/08/2026 15:43] Troy Hunt: Delete all the "deactivate-" prefixed addresses with corresponding active addresses, remove the prefix from the other ones and give me a new total count.
[25/08/2026 15:43] PwnedClaw: Done. Removed 285,808 rows, renamed 3,174 rows, new total: 13,014,714.
That's enough of human eyes, what else have we got?
[25/08/2026 15:50] Troy Hunt: Review the remaining addresses - are there any remaining unusual patterns that frequently occurs? Small issues here and there don't matter, anything in the thousands or more?

[25/08/2026 15:50] PwnedClaw: Two stand out:

wctest.com — 48,787 rows
Looks like a test domain used during development or QA. Not real customers.

carharttdonotship.com — 32,514 rows
The domain name says it all — this appears to be Carhartt's internal domain for flagging accounts they won't ship to (fraud, chargebacks, banned customers). Real people possibly, but deliberately excluded from Carhartt's operations and almost certainly not expecting breach notifications from their banned account email.

Everything else looks like normal consumer email providers. Want to remove either or both of those?

[25/08/2026 15:53] Troy Hunt: They also all seem to have "perftest" in the alias. Delete all these addresses.

[25/08/2026 15:53] PwnedClaw: Done. Removed 48,787 rows, new total: 12,965,927.

[25/08/2026 15:54] Troy Hunt: And the carharttdonotship.com  addresses also have "perftest" in the aliases so let's drop all those too and give me a total remaining count.

[25/08/2026 15:54] PwnedClaw: Done. Removed 32,514 rows, new total: 12,933,413.
Not quite the 24M+ headline any more, that's almost half the addresses in the original corpus discarded because they don't represent actual people. Whilst nothing
empirically
bad would have happened if I'd loaded them all, the incident would have looked twice as bad as what it actually is (based on the raw numbers, at least), and when I later put out a tweet like this, the percentage of pre-existing addresses would have read way too low:
But let's do one more AI-assisted sanity check, and I'm tending to ask this on each and every breach I process now:
[25/08/2026 16:01] Troy Hunt: Based on the remaining email addresses alone, what can you see that gives you confidence this came from Carhartt? Explain with examples and equally, explain if there's any data that *disproves* Carhartt as the origin.
  
[25/08/2026 16:01] PwnedClaw: Here's what the email addresses alone tell us:

Evidence FOR Carhartt as the origin:

• 15,057 @carhartt.com employee addresses — internal staff addresses don't end up in a dataset unless it came from Carhartt's own systems. You don't scrape these from the outside.
• Hash-prefixed internal aliases like 004cab9722d948ae956d10ce31e7ed74[unique alias]@carhartt.com — that 32-character hex prefix before the surname is clearly a system-generated internal identifier, the kind of thing a CRM or e-commerce platform creates internally. Completely invisible externally.
• carharttdonotship.com (now removed) — a domain that only makes sense if you're inside Carhartt's order management system. No external actor would know this domain exists, let alone have thousands of records under it.
• wctest.com perftest data (now removed) — performance test data from what appears to be Carhartt's own WooCommerce implementation. Again, only accessible internally.
• Demographically consistent — overwhelmingly US consumer email providers (Gmail, Yahoo, Hotmail, AOL, Comcast, sbcglobal, att.net (http://att.net/), verizon.net (http://verizon.net/)). Carhartt is a US workwear brand with a predominantly American customer base. The mix matches perfectly.

Evidence AGAINST Carhartt as the sole/direct origin:

• [unique alias]@state.mn.us — a government employee address. Plausible as a real Carhartt customer, but worth noting government addresses appearing in retail breach data is slightly unusual.
• The sheer volume (12.9M) is large for a workwear retailer — possible the data aggregates multiple systems or years of records, or includes data from third-party partners like Ticketmaster-style fulfilment services.

Overall the internal markers (employee addresses, hash aliases, internal test domains) are the smoking guns — those simply cannot come from anywhere other than Carhartt's own systems.
  
[25/08/2026 16:14] Troy Hunt: Acknowledging the cases "for" and agreeing, I want to challenge both cases "against":

Gov email addresses are *always* in data breaches. Even Ashley Madison (and similar).

My wife tells me that Carhartt is not solely considered a "workwear retailer" and produces products that are worn well beyond just the building site. Review their website and see if your analysis needs revision: https://www.carhartt.com/
  
[25/08/2026 16:14] PwnedClaw: Withdrawn. 12.9M records is entirely plausible for Carhartt — they're a 130-year-old brand with massive mainstream appeal well beyond workwear. Streetwear culture adopted Carhartt heavily in the 90s and it's remained a genuine lifestyle brand since. The volume is consistent with a large, broad consumer base accumulated over many years of e-commerce. That objection doesn't hold up.
Of course, anything AI says needs to be validated and in the cases above, that had already been done. I've included that transcript here anyway just to illustrate the due diligence involved in
properly
validating data, not just picking it up and chucking it in with a massive headline figure. But it does massively accelerate activities that were previously very manual:
[26/08/2026 05:40] Troy Hunt: Looking at the final list of email addresses, what do the sub-addresses tell us about the origin?
  
[26/08/2026 05:40] PwnedClaw: The sub-addresses are a goldmine for provenance. The dominant signal is clear:

1,072 +carhartt — people who tagged their address specifically when signing up at Carhartt. This is the single biggest tag and is an unambiguous origin marker. Combined with the typo variants (+carhart ×35, +carharrt ×14, +carhatt ×6, +carthartt ×4, +carh ×12) you've got ~1,150+ people who fingerprinted their Carhartt signup specifically.

+paypal ×112, +pp ×10, +applepay ×8` — people who used PayPal/Apple Pay to check out at Carhartt, and tagged the email to that payment method. Strongly confirms this is a shopping/ecommerce dataset.

+shopping ×28, +shop ×15, +orders ×9, +receipts ×4, +retail ×3` — generic purchase-tracking tags, consistent with an online store.

+www.carhartt.com ×8, +carhartt.com ×8` — people who tagged the full domain. Explicit.

+apple ×13` — likely Sign in with Apple or Apple Pay checkout.

The picture is unambiguous: this is a legitimate Carhartt customer/order database, not a compiled list or credential stuffing corpus. People sub-addressed their emails at the point of purchase. That's about as strong a provenance signal as you can get.
And so on and so forth. I don't need to labour the point with more examples, but let me come back around to the premise of this post: take headline numbers with a grain of salt unless you're confident in the processes of those making the claims. I'm fond of saying that whenever there are misleading statements made about breaches, "the truth is in the data", but you have to be willing to go and seek that truth out, even if it requires a significant investment in time.
