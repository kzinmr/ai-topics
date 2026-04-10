---
title: "Simon Willison on code-interpreter"
url: "https://substack.com/redirect/744882fb-8b32-4033-b787-001ccbfd6884?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-10T14:11:19.973780+00:00
source_date: 2026-04-10
tags: [newsletter, auto-ingested]
---

# Simon Willison on code-interpreter

Source: https://substack.com/redirect/744882fb-8b32-4033-b787-001ccbfd6884?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

Atom feed for code-interpreter
Random
30 posts tagged “code-interpreter”
ChatGPT Code Interpreter is a mode of
ChatGPT
(and now
Claude
) that allows it to write and then execute Python code in a sandboxed environment. OpenAI sometimes call this feature
data analysis
.
2026
Meta
announced Muse Spark
today, their first model release since Llama 4
almost exactly a year ago
. It’s hosted, not open weights, and the API is currently “a private API preview to select users”, but you can try it out today on
meta.ai
(Facebook or Instagram login required).
[...
2,607 words
]
One of my favourite features of ChatGPT is its ability to write and execute code in a container. This feature launched as ChatGPT Code Interpreter
nearly three years ago
, was half-heartedly rebranded to “Advanced Data Analysis” at some point and is generally really difficult to find detailed documentation about. Case in point: it appears to have had a
massive
upgrade at some point in the past few months, and I can’t find documentation about the new capabilities anywhere!
[...
3,019 words
]
2025
Anthropic this morning
introduced Claude Skills
, a new pattern for making new abilities available to their models:
[...
1,864 words
]
simonw/claude-skills
.
    One of the tips I picked up from
Jesse Vincent's Claude Code Superpowers post
(
previously
) was this:
Skills are what give your agents Superpowers.
The first time they really popped up on my radar was a few weeks ago when Anthropic rolled out improved Office document creation. When the feature rolled out, I went poking around a bit -- I asked Claude to tell me all about its new skills. And it was
only too happy to dish
.
In that transcript Jesse asks how the skill system works and Claude replies:
Looking at the skills system, here's how it works:
Current Skills
(in
/mnt/skills/public/
):
docx
- Word document handling
pdf
- PDF processing and form filling
pptx
- PowerPoint presentations
xlsx
- Excel spreadsheets
This looks like it's part of Claude's brand new Code Interpreter feature! I
wrote about that extensively
last month, but I missed that there was a
/mnt/skills/public/
folder full of fascinating implementation details.
So I fired up a fresh Claude instance (fun fact: Code Interpreter also works in the Claude iOS app now, which it didn't when they first launched) and prompted:
Create a zip file of everything in your /mnt/skills folder
This worked, and gave me a
.zip
to download. You can
run the prompt yourself here
, though you'll need to
enable the new feature first
.
I've pushed the contents of that zip to my
new simonw/claude-skills GitHub repo
.
So now you can see the prompts Anthropic wrote to enable the creation and manipulation of the following files in their Claude consumer applications:
pdf
- PDF files
docx
- Microsoft Word
pptx
- Microsoft PowerPoint decks
xlsx
- Microsoft Excel
In each case the prompts spell out detailed instructions for manipulating those file types using Python, using libraries that come pre-installed on Claude's containers.
Skills are more than just prompts though: the repository also includes dozens of pre-written Python scripts for performing common operations.
pdf/scripts/fill_fillable_fields.py
for example is a custom CLI tool that uses
pypdf
to find and then fill in a bunch of PDF form fields, specified as JSON, then render out the resulting combined PDF.
This is a really sophisticated set of tools for document manipulation, and I love that Anthropic have made those visible - presumably deliberately - to users of Claude who know how to ask for them.
#
10th October 2025
,
11:57 pm
/
pdf
,
python
,
ai
,
prompt-engineering
,
generative-ai
,
llms
,
anthropic
,
claude
,
code-interpreter
,
jesse-vincent
,
skills
Anthropic
released Claude Sonnet 4.5 today
, with a
very
bold set of claims:
[...
1,205 words
]
Apollo Global Management’s “Chief Economist” Dr. Torsten Sløk released
this interesting chart
which appears to show a slowdown in AI adoption rates among large (>250 employees) companies:
[...
2,673 words
]
Demo of ChatGPT Code Interpreter running in o3-mini-high
.
    OpenAI made GPT-4.5 available to Plus ($20/month) users today. I was
a little disappointed
with GPT-4.5 when I tried it through the API, but having access in the ChatGPT interface meant I could use it with existing tools such as Code Interpreter which made its strengths
a whole lot more evident
- that’s a transcript where I had it design and test its own version of the JSON Schema succinct DSL I published
last week
.
Riley Goodside
then spotted
that Code Interpreter has been quietly enabled for other models too, including the excellent o3-mini reasoning model. This means you can have o3-mini reason about code, write that code, test it, iterate on it and keep going until it gets something that works.
Code Interpreter remains my favorite implementation of the "coding agent" pattern, despite recieving very few upgrades in the two years after its initial release. Plugging much stronger models into it than the previous GPT-4o default makes it even more useful.
Nothing about this in the
ChatGPT release notes
yet, but I've tested it in the ChatGPT iOS app and mobile web app and it definitely works there.
#
5th March 2025
,
11:07 pm
/
python
,
ai
,
openai
,
generative-ai
,
chatgpt
,
riley-goodside
,
llms
,
ai-assisted-programming
,
code-interpreter
,
ai-agents
,
llm-reasoning
,
coding-agents
A surprisingly common complaint I see from developers who have tried using LLMs for code is that they encountered a hallucination—usually the LLM inventing a method or even a full software library that doesn’t exist—and it crashed their confidence in LLMs as a tool for writing code. How could anyone productively use these things if they invent methods that don’t exist?
[...
1,052 words
]
The
Oxide and Friends
podcast has an annual tradition of asking guests to share their predictions for the next 1, 3 and 6 years. Here’s
2022
,
2023
and
2024
. This year they invited me to participate. I’ve never been brave enough to share
any
public predictions before, so this was a great opportunity to get outside my comfort zone!
[...
2,675 words
]
2024
open-interpreter
(
via
)
    This "natural language interface for computers" open source ChatGPT Code Interpreter alternative has been around for a while, but today I finally got around to trying it out.
Here's how I ran it (without first installing anything) using
uv
:
uvx --from open-interpreter interpreter
The default mode asks you for an OpenAI API key so it can use
gpt-4o
- there are a multitude of other options, including the ability to use local models with
interpreter --local
.
It runs in your terminal and works by generating Python code to help answer your questions, asking your permission to run it and then executing it directly on your computer.
I pasted in an API key and then prompted it with this:
find largest files on my desktop
Here's
the full transcript
.
Since code is run directly on your machine there are all sorts of ways things could go wrong if you don't carefully review the generated code before hitting "y". The team have an experimental
safe mode
in development which works by scanning generated code with
semgrep
. I'm not convinced by that approach, I think executing code in a sandbox would be a much more robust solution here - but sandboxing Python is still a very difficult problem.
They do at least have an experimental
Docker integration
.
#
24th November 2024
,
6:29 pm
/
python
,
sandboxing
,
ai
,
docker
,
openai
,
generative-ai
,
llms
,
ai-assisted-programming
,
code-interpreter
,
uv
,
coding-agents
Foursquare Open Source Places: A new foundational dataset for the geospatial community
(
via
)
    I did not expect this!
[...] we are announcing today the general availability of a foundational open data set, Foursquare Open Source Places ("FSQ OS Places"). This base layer of 100mm+ global places of interest ("POI") includes 22 core attributes (see schema
here
) that will be updated monthly and available for commercial use under the Apache 2.0 license framework.
The data is available
as Parquet files
hosted on Amazon S3.
Here's how to list the available files:
aws s3 ls s3://fsq-os-places-us-east-1/release/dt=2024-11-19/places/parquet/
I got back
places-00000.snappy.parquet
through
places-00024.snappy.parquet
, each file around 455MB for a total of 10.6GB of data.
I ran
duckdb
and then used DuckDB's ability to remotely query Parquet on S3 to explore the data a bit more without downloading it to my laptop first:
select count(*) from 's3://fsq-os-places-us-east-1/release/dt=2024-11-19/places/parquet/places-00000.snappy.parquet';
This got back 4,180,424 - that number is similar for each file, suggesting around 104,000,000 records total.
Update:
DuckDB can use wildcards in S3 paths (thanks,
Paul
) so this query provides an exact count:
select count(*) from 's3://fsq-os-places-us-east-1/release/dt=2024-11-19/places/parquet/places-*.snappy.parquet';
That returned 104,511,073 - and Activity Monitor on my Mac confirmed that DuckDB only needed to fetch 1.2MB of data to answer that query.
I ran this query to retrieve 1,000 places from that first file as newline-delimited JSON:
copy (
    select * from 's3://fsq-os-places-us-east-1/release/dt=2024-11-19/places/parquet/places-00000.snappy.parquet'
    limit 1000
) to '/tmp/places.json';
Here's
that places.json file
, and here it is
imported into Datasette Lite
.
Finally, I got ChatGPT Code Interpreter to
convert that file to GeoJSON
and pasted the result
into this Gist
, giving me a map of those thousand places (because Gists automatically render GeoJSON):
#
20th November 2024
,
5:52 am
/
geospatial
,
open-source
,
foursquare
,
geojson
,
parquet
,
duckdb
,
datasette-lite
,
ai-assisted-programming
,
code-interpreter
,
coding-agents
OpenAI Public Bug Bounty
.
    Reading
this investigation
of the security boundaries of OpenAI's Code Interpreter environment helped me realize that the rules for OpenAI's public bug bounty inadvertently double as the missing details for a whole bunch of different aspects of their platform.
This description of Code Interpreter is significantly more useful than their official documentation!
Code execution from within our sandboxed Python code interpreter is out of scope. (This is an intended product feature.) When the model executes Python code it does so within a sandbox. If you think you've gotten RCE
outside
the sandbox, you
must
include the output of
uname -a
. A result like the following indicates that you are inside the sandbox -- specifically note the 2016 kernel version:
Linux 9d23de67-3784-48f6-b935-4d224ed8f555 4.4.0 #1 SMP Sun Jan 10 15:06:54 PST 2016 x86_64 x86_64 x86_64 GNU/Linux
Inside the sandbox you would also see
sandbox
as the output of
whoami
, and as the only user in the output of
ps
.
#
14th November 2024
,
11:44 pm
/
security
,
ai
,
openai
,
generative-ai
,
llms
,
code-interpreter
,
coding-agents
Anthropic
released a new feature
for their
Claude.ai
consumer-facing chat bot interface today which they’re calling “the analysis tool”.
[...
918 words
]
pip install GPT
(
via
)
    I've been uploading wheel files to ChatGPT in order to install them into Code Interpreter
for a while now
. Nico Ritschel built a better way: this GPT can download wheels directly from PyPI and then install them.
I didn't think this was possible, since Code Interpreter is blocked from making outbound network requests.
Nico's trick uses a new-to-me feature of GPT Actions: you can
return up to ten files
from an action call and ChatGPT will download those files to the same disk volume that Code Interpreter can access.
Nico wired up a Val Town endpoint that can divide a PyPI wheel into multiple 9.5MB files (if necessary) to fit the file size limit for files returned to a GPT, then uses prompts to tell ChatGPT to combine the resulting files and treat them as installable wheels.
#
21st July 2024
,
5:54 am
/
pypi
,
python
,
ai
,
generative-ai
,
chatgpt
,
llms
,
code-interpreter
,
coding-agents
An example running DuckDB in ChatGPT Code Interpreter
(
via
)
    I confirmed today that DuckDB can indeed be run inside ChatGPT Code Interpreter (aka "data analysis"), provided you upload the correct wheel file for it to install. The wheel file it needs is currently
duckdb-1.0.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
from the
PyPI releases page
- I asked ChatGPT to identify its platform, and it said that it needs
manylinux2014_x86_64.whl
wheels.
Once the wheel in installed ChatGPT already knows enough of the DuckDB API to start performing useful operations with it - and any brand new features in 1.0 will work if you tell it how to use them.
#
17th July 2024
,
9:04 pm
/
ai
,
duckdb
,
generative-ai
,
chatgpt
,
llms
,
code-interpreter
,
coding-agents
If you have a project, an idea, a product feature, or anything else that you want other people to understand and have conversations about... give them something to link to!
[...
685 words
]
I gave a talk last month at the
Story Discovery at Scale
data journalism conference hosted at Stanford by Big Local News. My brief was to go deep into the things we can use Large Language Models for right now, illustrated by a flurry of demos to help provide starting points for further conversations at the conference.
[...
6,081 words
]
I wrote yesterday about how I used
Claude and ChatGPT Code Interpreter for simple ad-hoc side quests
—in that case, for converting a shapefile to GeoJSON and merging it into a single polygon.
[...
4,612 words
]
Here is a short, illustrative example of one of the ways in which I use Claude and ChatGPT on a daily basis.
[...
1,754 words
]
2023
The biggest announcement from
last week’s OpenAI DevDay
(and there were a LOT of announcements) was
GPTs
. Users of ChatGPT Plus can now create their own, custom GPT chat bots that other Plus subscribers can then talk to.
[...
5,699 words
]
Last week I gave the closing keynote at the
AI Engineer Summit
in San Francisco. I was asked by the organizers to both summarize the conference, summarize the last year of activity in the space and give the audience something to think about by posing some open questions for them to take home.
[...
6,928 words
]
I’m on
the latest episode
of the Rooftop Ruby podcast with Collin Donnell and Joel Drapper, talking all things LLM.
[...
15,489 words
]
I gave
an invited keynote
at
WordCamp 2023
in National Harbor, Maryland on Friday.
[...
14,189 words
]
I gave a talk on Sunday at
North Bay Python
where I attempted to summarize the last few years of development in the space of LLMs—Large Language Models, the technology behind tools like ChatGPT, Google Bard and Llama 2.
[...
10,489 words
]
What AI can do with a toolbox... Getting started with Code Interpreter
.
    Ethan Mollick has been doing some very creative explorations of ChatGPT Code Interpreter over the past few months, and has tied a lot of them together into this useful introductory tutorial.
#
12th July 2023
,
8:57 pm
/
ai
,
openai
,
generative-ai
,
chatgpt
,
llms
,
ethan-mollick
,
code-interpreter
,
coding-agents
Latent Space: Code Interpreter == GPT 4.5
(
via
)
    I presented as part of this Latent Space episode over the weekend, talking about the newly released ChatGPT Code Interpreter mode with swyx, Alex Volkov, Daniel Wilson and more. swyx did a great job editing our Twitter Spaces conversation into a podcast and writing up a detailed executive summary, posted here along with the transcript. If you’re curious you can listen to the first 15 minutes to get a great high-level explanation of Code Interpreter, or stick around for the full two hours for all of the details.
Apparently our live conversation had 17,000+ listeners!
#
10th July 2023
,
10:06 pm
/
podcasts
,
speaking
,
ai
,
swyx
,
generative-ai
,
chatgpt
,
llms
,
code-interpreter
,
podcast-appearances
,
coding-agents
ChatGPT Plugins Don’t Have PMF
.
    Sam Altman was recently quoted (in a since unpublished blog post) noting that ChatGPT plugins have not yet demonstrated product market fit.
This matches my own usage patterns: I use the “browse” and “code interpreter” modes on a daily basis, but I’ve not found any of the third party developer plugins to stick for me yet.
I like Matt Rickard’s observation here: “Chat is not the right UX for plugins. If you know what you want to do, it’s often easier to just do a few clicks on the website. If you don’t, just a chat interface makes it hard to steer the model toward your goal.”
#
8th June 2023
,
4:59 am
/
ai
,
openai
,
generative-ai
,
chatgpt
,
llms
,
code-interpreter
,
sam-altman
,
coding-agents
,
chatgpt-plugins
I gave myself some time off stressing about my core responsibilities this week after PyCon, which meant allowing myself to be distracted by some miscellaneous research projects.
[...
891 words
]
Today I wanted to understand the performance difference between two Python implementations of a mechanism to detect changes to a SQLite database schema. I rendered the difference between the two as this chart:
[...
2,939 words
]
