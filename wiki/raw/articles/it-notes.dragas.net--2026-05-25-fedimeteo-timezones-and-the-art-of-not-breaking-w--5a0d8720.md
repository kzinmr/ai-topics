---
title: "FediMeteo, timezones, and the art of not breaking what already works"
url: "https://it-notes.dragas.net/2026/05/25/fedimeteo-timezones-and-the-art-of-not-breaking-what-already-works/"
fetched_at: 2026-05-26T07:14:42.685396+00:00
source: "it-notes.dragas.net"
tags: [blog, raw]
---

# FediMeteo, timezones, and the art of not breaking what already works

Source: https://it-notes.dragas.net/2026/05/25/fedimeteo-timezones-and-the-art-of-not-breaking-what-already-works/

I have already written about
how FediMeteo was born
, and about how
HAProxy helps reduce the number of requests that reach snac
.
Seen from the outside, FediMeteo almost seems still. There is a static homepage, regenerated every hour. There are the city pages, with their forecasts. There are RSS feeds waiting to be fetched, JSON objects waiting to be requested, Fediverse instances refreshing data, subscribing, unsubscribing, retrieving profiles, and reading notes.
That is the visible part.
Behind it, however,
FediMeteo
is much more than a homepage, a few ActivityPub accounts, and a well-behaved reverse proxy. It is a chain of small pieces, in proper Unix style, each trying to do one thing and do it as well as possible.
That chain, although almost invisible from the outside, was not born already tidy. It changed, was rewritten, adapted to new countries, timezones, ambiguous city names, external service limits, and also to my own mistakes.
Some mistakes were small. Others were much less so.
Because FediMeteo is a human project and, as such, imperfect. Imperfect in the way humans are imperfect, which today almost seems unfashionable. I like that.
The first version of the bot was almost embarrassingly simple, and I was proud of that.
It took a city name as input, asked
Nominatim
for the coordinates through
geopy
, called the
Open-Meteo
API for the current weather and the next several days, and printed a markdown block with current conditions, the forecast for today, the next twelve hours, and the coming days. The text was in Italian. The cities were Italian. The timezone was
Europe/Rome
. There was nothing to calculate.
Around the script, a small
sh
wrapper read a list of cities and, for each one, ran the Python program and piped its output into
snac note_unlisted
. A cron job ran the wrapper every six hours. The output was loose markdown, which snac happily renders, and the integration was: standard output goes into standard input. Nothing fancier than that.
I like this kind of design. It is the part of the Unix philosophy that survives even when fashions change.
When I started adding other European countries, I did not need to change much. I separated the operational logic from the localized strings, moved the strings into one JSON file per country, and spread the cron entries so that not every country posted in the same minute. Each country had its own snac instance, in its own FreeBSD jail, with its own dataset. The bot, internally, was almost the same script as before.
This worked because Europe is, in essence, two or three timezones across most of the countries I cared about.
Then I added Germany, and Germany taught me my first lesson about names.
There are several places called Neustadt in Germany. There is a Frankfurt am Main, and a Frankfurt an der Oder, and they are not the same city. There is a Halle in Saxony-Anhalt and a Halle in North Rhine-Westphalia. Asking Nominatim for "Frankfurt, Germany" produced one of the two, consistently, but not always the one I wanted. Some German users wrote to me, politely, to point out that the forecast for "their" Frankfurt was, in fact, for the other one.
I started thinking about disambiguation, but only enough to fix the immediate cases. The bot still took a single city name. The ambiguous ones I worked around by editing the cities file and hoping for the best.
In hindsight, this was the seed of what would happen later.
The United States broke every assumption the bot had grown up with
.
The first problem was the number of cities. I wanted reasonable coverage at state level, which meant identifying the main cities for each of the fifty states. The list ended up at more than 1200 entries. That alone is more cities than every other country in the project combined.
The second problem was timezones. The contiguous United States covers four of them, and Alaska and Hawaii bring the total to six. A "current weather at 12:00" line generated at the same instant for New York and for Los Angeles is technically the same instant, but the two cities are living different parts of the day, and the forecast for "today" is not even quite the same window. A bot that pretended every city was on the same clock would be wrong, sometimes embarrassingly so, every single day.
The third problem was the name thing again, only larger. There are dozens of Springfields. There is a Portland in Oregon and a Portland in Maine. The Germany workaround - editing the cities file by hand and hoping Nominatim picked the right city - was clearly not going to scale to a country where the same name is also a state.
I sat with this for a couple of days before admitting what I already knew.
The bot needed to be rewritten
.
What made this hard was not the rewriting itself. It was the requirement to do it without breaking everything else.
By the time I decided to add the United States, the infrastructure around the bot had grown into something I trusted. Jails, snapshots, backup jobs, cron schedules, snac instances on production paths, the HAProxy layer, the homepage cron that aggregated follower counts, and a long list of cities being processed in series every six hours. None of that knew or cared about the bot's internal shape. All of it cared, very much, about the bot's external behavior: a city name and a country code go in, valid markdown comes out, and that markdown ends up in a timeline.
So the contract was clear, even if I had never written it down anywhere. The command-line interface, the output format, the exit codes, the way the wrapper script invoked it, the structure of the JSON country configs - all of it had to keep working. Italian had to keep working. German had to keep working. The cron job that ran every six hours had to keep producing the same shape of output, just with new countries added.
What I changed was almost everything below the surface.
The city argument grew an optional
__state
suffix, with a double underscore as separator:
python3 main.py springfield__illinois us
python3 main.py springfield__massachusetts us
python3 main.py new_york__new_york us
A city without the suffix continued to work exactly as before, which is what every European country needed. The country config gained a
timezone
field that could be a fixed string or the literal
"auto"
; when it was
"auto"
, the bot used
timezonefinder
against the resolved coordinates to determine the right zone for that specific city. Internally I separated the weather provider behind an interface, so Open-Meteo could remain the primary while MET Norway and
wttr.in
sat behind as alternatives, with automatic fallback when the primary failed. Units became configurable per country: temperature, wind speed, precipitation. The United States needed Fahrenheit, miles per hour, and inches. Most of Europe wanted Celsius, kilometers per hour, and millimeters. The bot now does either, on a per-country basis, without caring which is which.
I am skipping a lot of small detail here, but the principle was always the same: every new degree of freedom had to be expressible as an optional field in the config or as an optional CLI flag. If a country did not set the new field, the old behavior continued, identical to before.
I tested this by running the new bot against the old country configs and comparing the output line by line. Where it differed, it was a bug in the new bot. Not in the test.
The first cycle after deploying the rewrite was, for every country except the United States, indistinguishable from the cycle before. That was the point.
This is the part of the story I dislike telling, which is precisely why I should tell it.
At some point during the development, while debugging an Open-Meteo response that did not look right, I added a
print
statement to the error path that dumped the full request URL whenever something went wrong. The full URL of the Open-Meteo customer endpoint includes the
apikey
query parameter. The print was meant for development. I forgot to remove it.
I deployed
.
The next time Open-Meteo had an outage - and small ones happen, sometimes for several minutes at a time - the bot dutifully printed the failing request URL into the post body. For every city. For every cycle that ran during the outage. The wrapper script piped the output into
snac note_unlisted
without complaint. The posts went out, federated across the Fediverse, with my API key sitting in the text for anyone who cared to read.
Some users were kind enough to write me and tell me. Others were less kind, and made fun of me. Both groups were correct. This should not have happened.
I reported the incident to the Open-Meteo team, who were extremely understanding. They rotated the key immediately and gave me a fresh one. I removed the debug print, and then I did the slightly more useful thing, which was to add redaction at multiple layers - in the bot's output, in the daemon's logging, and in the debug helpers themselves. URL query parameters that look like API keys are masked. Environment variables and config keys named
apikey
or
OPEN_METEO_APIKEY
are redacted before any string reaches stdout or a log file. Even JSON-like fields that include
open_meteo_apikey
are scrubbed if they ever appear in something the program prints.
The lesson is not "be more careful." The lesson is that debug paths leak, sooner or later, so the secrets have to be unreachable from the debug paths in the first place. Now they are.
That afternoon, when I realised what was happening, I closed everything for a minute and looked out of the window. Then I started fixing.
Nominatim is a public service, and it is generous, but it is not infinite. Every city in the project needs coordinates, and at the start of the project every cycle would re-ask Nominatim for every city. Most of the time this worked. Sometimes it did not.
There was one cycle, before I added caching, when Nominatim simply did not respond for one of my queries. The geopy call timed out. The bot raised an exception. The wrapper script gave up on that city and moved on to the next one. A few users noticed that a particular city had not received its forecast that day, and asked what had happened.
I added a coordinate cache, and I am still grateful that I did.
The cache is intentionally boring. The first time the bot resolves a city, it writes the latitude and longitude into a small file under
/tmp
, named after the city, and the state when present. Every subsequent run reads the file. If the file exists, no Nominatim call is made. If the file is missing, the bot calls Nominatim and writes the file. After the first successful lookup, the cache becomes the source of truth for the coordinates of that city.
This is lighter on Nominatim, faster for every cycle, and much more resilient against transient failures. It is also nice for a reason I did not anticipate.
Nominatim is a geocoder, and like every geocoder it has opinions.
I live in Ferrara, so when I added Italy I made sure Ferrara was in the list, and I checked the first cycle to make sure everything looked right. The forecast came out fine. The temperature was reasonable. The icon matched the sky outside my window. I closed the laptop and forgot about it.
Then, one evening months later, I looked more carefully at the coordinates Nominatim had returned for "Ferrara, Italy", and I realised they did not point to the city. They pointed to a location closer to the centroid of the
province
, which is a much larger area and mostly countryside. The forecast had been, on average, for a field somewhere outside town, not for the city center.
I am not entirely sure why I had not noticed earlier. Probably because the weather in Ferrara and the weather in the fields outside Ferrara is, on most days, indistinguishable to anyone who is not paying attention. But this is the kind of detail I do not want to leave wrong, especially for my own city.
There are other places where geocoding lands slightly off. Sometimes it is a few kilometers, sometimes a different neighborhood, sometimes genuinely the wrong place.
Because the cache is just a file per city, the fix is also just a file per city. I open the cache file, replace the latitude and longitude with the correct values, save. The next cycle uses the corrected coordinates. No code change, no redeploy, no special tooling. I keep a small list of patched cities in a separate text file, so that if I ever rebuild the cache, I do not lose the manual corrections.
This is the kind of operational simplicity I like. A cache made of plain files costs almost nothing and quietly pays back every time a small problem appears.
For every report it generates, the bot also writes a simplified English text snapshot to
/tmp/<city>.txt
, or
/tmp/<city>__<state>.txt
when there is a state.
This is intentional, and it is not a debug artifact. I am not ready to say what I am doing with it yet, but it is part of a future direction for the project. Text is a useful intermediate format, and having a clean, language-neutral representation of every forecast sitting on disk costs almost nothing and might be worth a great deal later.
I prefer to let ideas mature in private before I commit to them in public. So I will leave it at this for the moment.
A full cycle for the United States takes hours.
It is not because the work is heavy. It is because I deliberately inserted a small
sleep
between cities, to give snac time to dispatch the previous post before the next one is generated. With more than 1200 cities in series, even a short pause adds up. I am not in a hurry. Forecasts that arrive a few minutes apart from each other are not a problem, and the bot was already a polite citizen elsewhere. A polite cycle is fine.
The problem with a slow cycle is not the duration. The problem is what happens to it.
In the original design, the cycle was launched by cron. Every six hours, cron called the wrapper script, the wrapper iterated through the cities file, and for each city it ran the bot and piped the output into snac. There was no scheduler in the project at all. Cron was the scheduler. The wrapper was just a loop.
Restarting snac was harmless. The wrapper would call
snac note_unlisted
per city, and if snac happened to be unavailable for a moment, that single call might fail, but the loop kept moving and snac was usually back within seconds. Snac itself was not what held the cycle together.
What held the cycle together was the wrapper process. And the wrapper process lived inside the jail.
If the FreeBSD jail was restarted while the wrapper was running, the loop stopped wherever it happened to be. The cron schedule did not care. Six hours later, the next cron tick started a new cycle from the first city, and the cities that had been about to be processed at the moment of the restart were simply skipped for that window. For the United States, this could mean several hundred cities going without an update.
There was a worse case, and it took me longer than it should have to recognise it. If the host was rebooting
exactly
in the minute when cron should have fired, cron simply did not fire. There was no daemon waiting to pick up the missed tick. The cycle never even started. Six hours of forecasts would be lost, in silence, with nothing in any log to suggest anything had gone wrong.
I lived with this for a long time. Reboots were rare, the impact was limited, and adding state was the kind of thing I always meant to do "next week."
What finally changed it was not a dramatic incident. It was the slow accumulation of small ones. A scheduled VPS reboot. A jail restart after an upgrade. Each one on its own was nothing. Together, they were a steady drip of missed cycles.
So I wrote a daemon
.
The crontab entries for the bot went away. There is now a long-running process inside the jail, started at boot, and it does the scheduling itself. The schedule is a list of hours and a minute, read from a JSON config. The daemon wakes up once a minute, checks whether it is time to start a cycle, and either starts one or waits.
The interesting part is the state file.
As the daemon walks through the cities file, it writes its position to a small JSON file: which cities file it is processing, and the index of the next city to handle. The write happens at the boundary between one city and the next, because that is the only place where resuming makes sense. If the daemon is interrupted mid-city, that city is retried on resume; no half-finished post escapes.
When the daemon starts, it reads the state file. If it finds one matching the current cities file, it resumes from the saved index. If the cities file has changed since the state was written, the daemon starts fresh. The check is deliberately conservative: a renamed or modified cities file is treated as a different cycle, because the indices would otherwise be meaningless.
The result is the behavior I should have had from the start. If the host reboots while the United States cycle is running, the daemon comes back up with the jail, reads the state, and continues from where it left off. Every city still gets its update, just with a small gap corresponding to the reboot itself. The cycle finishes. The state file is reset. Life goes on.
And the worst case from the cron days is gone. The daemon does not need anyone to fire it. As long as the jail is running, the daemon is running, and the next scheduled cycle will happen when its hour comes, regardless of what was happening at any specific minute.
Of all the changes I have made to the project, this is the one I like most. It is not exciting work. It is the kind of thing that earns no applause because, when it works, it produces no visible event. But it removes a whole class of small daily annoyances, and it makes a slow process robust against the boring kind of failure: the kind nobody plans for, but that always eventually happens.
The current bot does considerably more than the original Italian script. It handles per-city timezones, three weather providers with automatic fallback, unit conversion for temperature, wind, and precipitation, optional air quality, pressure trend indicators when the provider supplies pressure data, a simplified English text snapshot for future use, a coordinate cache that can be patched by hand, secret redaction at multiple layers, a heartbeat that adapts to whichever HTTP client is installed on the host, and a scheduler-and-resume daemon that survives reboots.
But from the outside, almost nothing has changed.
The European country configs work the same way they always did. The wrapper scripts are unchanged. The snac integration is the same one-line pipe. The HAProxy layer in front does not know or care that the bot was rewritten. The homepage cron that counts followers and regenerates the static page works exactly as before.
The original Italian script does not exist as a file anymore, but it survives as a default. A country config with
timezone
set to
Europe/Rome
and no special options behaves, today, exactly as the first version of the bot would have. Everything else is opt-in.
I like this kind of work.
