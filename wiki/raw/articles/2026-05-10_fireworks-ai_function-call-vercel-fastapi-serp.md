---
title: "Build Your Own Flight Recommendation System using FastAPI, SerpAPI, and Firefunction"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/function-call-vercel-fastapi-serp"
scraped: "2026-05-10T01:20:46.499954+00:00"
lastmod: "2026-02-12T18:52:50.000Z"
type: "sitemap"
---

# Build Your Own Flight Recommendation System using FastAPI, SerpAPI, and Firefunction

**Source**: [https://fireworks.ai/blog/function-call-vercel-fastapi-serp](https://fireworks.ai/blog/function-call-vercel-fastapi-serp)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Function Call Vercel Fastapi Serp
Build Your Own Flight Recommendation System using FastAPI, SerpAPI, and Firefunction
PUBLISHED
8/29/2024
Table of Contents
Prerequisites
Tech Stack
High-Level Data Flow and Operations
Steps
Generate the
Generate the SerpApi API Key
Create a new FastAPI application
Install Dependencies
Define Data Models using Pydantic
Initialize FastAPI App
Integration with Firefunction V2
Create a Chat API endpoint
Use SerpApi to generate recommendations from Google Flights in real-time
Run FastAPI App Locally
Create a new Next.js application
Install AI SDK
Build Conversation User Interface
Run Next.js Application Locally
Conclusion
Table of Contents
Table of Contents
Prerequisites
Tech Stack
High-Level Data Flow and Operations
Steps
Generate the
Generate the SerpApi API Key
Create a new FastAPI application
Install Dependencies
Define Data Models using Pydantic
Initialize FastAPI App
Integration with Firefunction V2
Create a Chat API endpoint
Use SerpApi to generate recommendations from Google Flights in real-time
Run FastAPI App Locally
Create a new Next.js application
Install AI SDK
Build Conversation User Interface
Run Next.js Application Locally
Conclusion
Table of Contents
Imagine you're planning a last-minute getaway. You've got a few days off, but you're not sure where to go, or how to get there. Instead of spending hours scouring the internet for travel options, wouldn't it be great if you could simply type in your preferences and instantly receive tailored suggestions?
That's exactly what we'll be creating in this guide: a personalized recommendation system for flights using
Fireworks
,
SerpApi
,
FastAPI
, and
Next.js
.
In this tutorial, we're going to create a
Flight Recommendation System
utilizing Firefunction-v2 to streamline the extraction of Departure and Arrival Airport Code (IATA Code) and the date or time of travel recommendations, as well as flight details, from dynamically received user inputs.
Prerequisites
You'll need the following:
•
Node.js 18
or later
•
A
Fireworks
account
•
A
SerpApi
account
Tech Stack
Following technologies are used in creating our RAG application:
Technology
Type
Description
FastAPI
Framework
A high performance framework to build APIs with Python 3.8+.
Next.js
Framework
The React Framework for the Web.
TailwindCSS
Framework
CSS framework for building custom designs.
Fireworks
Platform
Blazing fast LLM Inference platform.
SerpApi
Platform
A real-time API to access Google search results.
High-Level Data Flow and Operations
This is a high-level diagram of how data is flowing and operations that take place 👇🏻
When a user types in a query like “Flights from San Francisco to Dulles”, a tool call is generated as per the registered function spec in Firefunction v2. Further, they are used to query
SerpApi
for real-time results. The response is then returned to the user.
Steps
•
•
•
•
Generate the
Fireworks AI API Key
HTTP requests to the Fireworks API require an API Key. To generate this API key, log in to your Fireworks account and navigate to
API Keys
. Enter a name for your API key and click the
Create Key
button to generate a new API key. Copy and securely store this token for later use as
FIREWORKS_API_KEY
environment variable.
Locally, set and export the
FIREWORKS_API_KEY
environment variable by executing the following command:
1
2
export
FIREWORKS_API_KEY
=
"YOUR_FIREWORKS_API_KEY"
Generate the SerpApi API Key
HTTP requests to the SerpApi require an authorization token. To generate this token, while logged into your SerpApi account, navigate to the
dashboard
, scroll down to
Your Private API Key
section, and click the
Clipboard
icon. Copy and securely store this token for later use as
SERPAPI_API_KEY
environment variable.
Locally, set and export the
SERPAPI_API_KEY
environment variable by executing the following command:
1
2
export
SERPAPI_API_KEY
=
"YOUR_SERPAPI_API_KEY"
Create a new FastAPI application
First, let's start by creating a new project. You can create a new directory by executing the following command in your terminal window:
1
2
3
4
#
Create
and move to the
new
directory
mkdir genai
-
functions
cd genai
-
functions
Install Dependencies
Next, you can install the required dependencies by executing the following command in your terminal window:
1
2
3
4
5
pip install fastapi
"uvicorn[standard]"
pip install openai
pip install fireworks
-
ai
pip install google
-
search
-
results
The above command installs the required libraries to run ASGI Server, FastAPI, OpenAI, Fireworks AI, and SerpAPI in your Python project.
Next, create a file
main.py
with the following code:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
import
os
import
json
from
typing
import
List
from
datetime
import
datetime
#
OpenAI
import
openai
#
SerpApi
from
serpapi
import
GoogleSearch
#
FastAPI
from
fastapi
import
FastAPI
from
pydantic
import
BaseModel
#
Enable
CORS
utility
from
fastapi
.
middleware
.
cors
import
CORSMiddleware
The above code imports the following:
•
os
module to use the environment variables you’ve set earlier.
•
List
to denote a list of elements of specific type.
•
json
to parse string model outputs as JSON.
•
datetime
module to get today’s date.
•
openai
module to conveniently call OpenAI API.
•
serpapi
module to scrape and parse search results from Google Search.
•
BaseModel
class to define models of the request body FastAPI endpoints.
•
CORSMiddleware
FastAPI middleware to enable Cross Origin Resource Sharing of FastAPI endpoints.
Define Data Models using Pydantic
To create the data types of request body in your FastAPI endpoints, append the following code in
main.py
file:
1
2
3
4
5
6
7
8
9
# Class representing a single message of the conversation between RAG application and user.
class
Message
(
BaseModel
)
:
role
:
str
content
:
str
# Class representing collection of messages above.
class
Messages
(
BaseModel
)
:
messages
:
List
[
Message
]
The above code defines two
Pydantic
models:
•
Message
: a model that will store each message containing two fields,
role
and
content
.
•
Messages
: a model that will store the input as a list of
Message
model.
Initialize FastAPI App
To initialize a FastAPI application, append the following code in
main.py
file:
1
2
3
4
5
6
7
8
9
10
11
12
# Initialize FastAPI App
app
=
FastAPI
(
)
# Add CORS middleware
app
.
add_middleware
(
CORSMiddleware
,
allow_origins
=
[
"*"
]
,
allow_credentials
=
True
,
allow_methods
=
[
"*"
]
,
allow_headers
=
[
"*"
]
,
)
The code above creates a FastAPI instance and uses the
CORSMiddleware
middleware to enable Cross Origin requests. This allows your frontend to successfully POST to the GenAI application endpoints to fetch responses to the user query, regardless of the port it is running on.
Integration with Firefunction V2
Firefunction-v2 is a function calling LLM that can help you with build agentic use cases like chat assistants that involve function calling capabilities, alongside general chat capabilities.
In the code below, we're defining a set of tools utilizing Firefunction-v2 to streamline the extraction of Departure and Arrival Airport Code (IATA Code) and the date or time of travel recommendations, as well as flight details, from dynamically received user inputs. This approach not only improves the user experience by automating the workflow but also demonstrates the practical application of Firefunction-v2 in real-world scenarios.
In each function, you’ll define a structure like below:
•
name
: A personalized name for your function.
•
description
: Few characters to illustrate the use case of the function.
•
parameters
: The values the function is supposed to extract from the user prompt.
•
properties
: A structured object containing the name, description and type of the values with instructions that need to be extracted. Make sure to have a detailed description that allows AI to produce accurate results to your intended use case.
•
required
: The name of the values that are necessary to be generated from this tool, if invoked by AI.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
#
Get
today's date
today_date
=
datetime
.
today
(
)
.
strftime
(
"%Y-%m-%d"
)
#
Define
the
set
of
tools
tools
=
[
{
#
Create
a flight detail generator
function
"type"
:
"function"
,
"function"
:
{
"name"
:
"flight_generator"
,
"description"
:
"Extract flight details from the user prompt."
,
"parameters"
:
{
"type"
:
"object"
,
"properties"
:
{
"departure_id"
:
{
"type"
:
"string"
,
"description"
:
"This represents the departure airport code in 3 letters. If you find a name of the country from user prompt, locate the most busiest airport and use it's IATA based 3-letter code, else if find an airport in the prompt, use it's IATA based airport code."
,
}
,
"departure_date"
:
{
"type"
:
"string"
,
"description"
:
f
"This represents the departure date in YYYY-MM-DD format. If you can not find a date in user prompt, just use {today_date} as the fallback."
,
}
,
"arrival_id"
:
{
"type"
:
"string"
,
"description"
:
"This represents the arrival airport code in 3 letters. If you find a name of the country from user prompt, locate the most busiest airport and use it's IATA based 3-letter code, else if find an airport in the prompt, use it's IATA based airport code."
,
}
,
"arrival_date"
:
{
"type"
:
"string"
,
"description"
:
f
"This represents the arrival date in YYYY-MM-DD format. If you can not find a date in user prompt, just use {today_date} as the fallback."
,
}
,
}
,
"required"
:
[
"departure_id"
,
"departure_date"
,
"arrival_id"
,
"arrival_date"
]
,
}
,
}
,
}
,
]
The code above does the following:
•
Creates a date in YYYY-MM-DD format using the
datetime
module.
•
flight_generator
: A function that outputs (if found), four arguments pertaining to the departure and arrival of the flights based on the
IATA
codes of the airports by which the user could fly between the timings as gathered from their prompt.
Create a Chat API endpoint
To generate personalized responses by using Fireworks Firefunction-v2, you’ll create an
/chat
endpoint in your FastAPI application. Append the following code in
main.py
file:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
client
=
openai
.
OpenAI
(
base_url
=
"https://api.fireworks.ai/inference/v1"
,
api_key
=
os
.
environ
[
"FIREWORKS_API_KEY"
]
)
@app
.
post
(
"/chat"
)
async
def
chat
(
messages
:
Messages
)
:
messages_json
=
(
messages
.
model_dump
(
)
)
[
'messages'
]
# Create System Context
knowledge
=
"You are a helpful assistant with access to functions. Use them if required."
messages_json
.
insert
(
0
,
{
"role"
:
"system"
,
"content"
:
knowledge
}
)
# Call Fireworks Function to determine the flights user asked for
chat_completion
=
client
.
chat
.
completions
.
create
(
tools
=
tools
,
temperature
=
0.1
,
messages
=
messages_json
,
model
=
"accounts/fireworks/models/firefunction-v2"
,
)
# Parse the generated function call to obtain the Airport codes and date of travel
generated_tool_call
=
json
.
loads
(
chat_completion
.
choices
[
0
]
.
message
.
model_dump_json
(
include
=
{
"tool_calls"
}
)
)
generated_args
=
generated_tool_call
[
"tool_calls"
]
[
0
]
[
"function"
]
[
"arguments"
]
final_args
=
json
.
loads
(
generated_args
)
The above code does the following:
•
Accepts a list of
messages
that could be specified natural language format “Flights from San Francisco to New York this Sunday”.
•
Defines a system prompt to let the assistant be able to call the fireworks functions you’ve defined earlier using tools array. Prepends a
Message
model, representing role of the system and it’s content as the system prompt created.
•
Uses Fireworks Chat Completion API to invoke Firefunction-v2 to generate params for booking flights.
•
Serializes the output obtained from the chat completion API to a JSON and extracts the arguments obtained, containing the value of flight details.
Use SerpApi to generate recommendations from Google Flights in real-time
SerpApi helps you access real-time data from many internet sources namely YouTube or Google Flights, facilitating dynamic content generation and flight searches.
To retrieve relevant results from Google Flights, you need to set the SerpApi engine to
google_flights
and pass the date and airport codes of arrival and departure, the currency and the language SerpApi should return results in. SerpApi then returns details of relevant flights matching the user's query, enabling personalized flight recommendations.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
@app
.
post
(
"/chat"
)
async
def
chat
(
messages
:
Messages
)
:
# ...
final_args
=
json
.
loads
(
generated_args
)
params
=
{
"api_key"
:
os
.
environ
[
"SERPAPI_API_KEY"
]
,
}
if
final_args
[
"arrival_date"
]
is
not
None
:
# Create params for the SerpApi for finding flights matching the user query
params
.
update
(
{
"hl"
:
"en"
,
"currency"
:
"USD"
,
"engine"
:
"google_flights"
,
"arrival_id"
:
final_args
[
"arrival_id"
]
,
"return_date"
:
final_args
[
"arrival_date"
]
,
"departure_id"
:
final_args
[
"departure_id"
]
,
"outbound_date"
:
final_args
[
"departure_date"
]
,
}
)
# Obtain the relevant content on YouTube
search
=
GoogleSearch
(
params
)
# Return it as the response to the API endpoint
resp
=
search
.
get_dict
(
)
The code above does the following:
•
Creates a params dict with
api_key
parameter to SerpApi key obtained earlier.
•
Checks if the arguments obtained earlier had
arrival_date
in it. It updates the
params
dict to contain the expected arrival and departure date and related airport codes. It also sets the currency and language SerpApi should respond real time flight details with.
Once you’ve obtained the response, you’re going to selectively create an array of flights that contain JSON objects representing details of each recommendation by SerpApi and return it as the response.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
@app
.
post
(
"/chat"
)
async
def
chat
(
messages
:
Messages
)
:
# ...
resp
=
search
.
get_dict
(
)
if
final_args
[
"arrival_date"
]
is
not
None
:
return
{
"flights"
:
[
{
"price"
:
flight
[
"price"
]
,
"airline_logo"
:
single_flight
[
"airline_logo"
]
,
"arrival_airport_name"
:
single_flight
[
"arrival_airport"
]
[
"name"
]
,
"arrival_airport_time"
:
single_flight
[
"arrival_airport"
]
[
"time"
]
,
"departure_airport_name"
:
single_flight
[
"departure_airport"
]
[
"name"
]
,
"departure_airport_time"
:
single_flight
[
"departure_airport"
]
[
"time"
]
,
}
for
flight
in
resp
[
"best_flights"
]
for
single_flight
in
flight
[
"flights"
]
[
:
3
]
]
}
The code above does the following:
•
It creates a
flights
array to be returned as response. Each item in the
flights
array represents the price and airline logo of the flight, with it’s arrival and departure dates and airport names.
With all that done, here’s how our
main.py
will finally look like containing both the endpoints:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
import
os
import
json
from
typing
import
List
from
datetime
import
datetime
# OpenAI
import
openai
# SerpApi
from
serpapi
import
GoogleSearch
# FastAPI
from
fastapi
import
FastAPI
from
pydantic
import
BaseModel
# Enable CORS utility
from
fastapi
.
middleware
.
cors
import
CORSMiddleware
# Class representing a single message of the conversation between RAG application and user.
class
Message
(
BaseModel
)
:
role
:
str
content
:
str
# Class representing collection of messages above.
class
Messages
(
BaseModel
)
:
messages
:
List
[
Message
]
# Create a FastAPI App instance
app
=
FastAPI
(
)
# Add CORS middleware
app
.
add_middleware
(
CORSMiddleware
,
allow_origins
=
[
"*"
]
,
allow_credentials
=
True
,
allow_methods
=
[
"*"
]
,
allow_headers
=
[
"*"
]
,
)
# Get today's date
today_date
=
datetime
.
today
(
)
.
strftime
(
"%Y-%m-%d"
)
tools
=
[
{
"type"
:
"function"
,
"function"
:
{
"name"
:
"flight_generator"
,
"description"
:
"Extract flight details from the user prompt."
,
"parameters"
:
{
"type"
:
"object"
,
"properties"
:
{
"departure_id"
:
{
"type"
:
"string"
,
"description"
:
"This represents the departure airport code in 3 letters. If you find a name of the country from user prompt, locate the most busiest airport and use it's IATA based 3-letter code, else if find an airport in the prompt, use it's IATA based airport code."
,
}
,
"departure_date"
:
{
"type"
:
"string"
,
"description"
:
f"This represents the departure date in YYYY-MM-DD format. If you can not find a date in user prompt, just use
{
today_date
}
as the fallback."
,
}
,
"arrival_id"
:
{
"type"
:
"string"
,
"description"
:
"This represents the arrival airport code in 3 letters. If you find a name of the country from user prompt, locate the most busiest airport and use it's IATA based 3-letter code, else if find an airport in the prompt, use it's IATA based airport code."
,
}
,
"arrival_date"
:
{
"type"
:
"string"
,
"description"
:
f"This represents the arrival date in YYYY-MM-DD format. If you can not find a date in user prompt, just use
{
today_date
}
as the fallback."
,
}
,
}
,
"required"
:
[
"departure_id"
,
"departure_date"
,
"arrival_id"
,
"arrival_date"
]
,
}
,
}
,
}
,
]
client
=
openai
.
OpenAI
(
base_url
=
"https://api.fireworks.ai/inference/v1"
,
api_key
=
os
.
environ
[
"FIREWORKS_API_KEY"
]
)
@app
.
post
(
"/chat"
)
def
chat
(
messages
:
Messages
)
:
messages_json
=
(
messages
.
model_dump
(
)
)
[
"messages"
]
# Create System Context
knowledge
=
"You are a helpful assistant with access to functions. Use them if required."
messages_json
.
insert
(
0
,
{
"role"
:
"system"
,
"content"
:
knowledge
}
)
# Call Fireworks Function to determine the flights user asked for
chat_completion
=
client
.
chat
.
completions
.
create
(
tools
=
tools
,
temperature
=
0.1
,
messages
=
[
messages_json
[
0
]
,
messages_json
[
-
1
]
]
,
model
=
"accounts/fireworks/models/firefunction-v2"
,
)
# Parse the generated function call to obtain the Airport codes and date of travel
generated_tool_call
=
json
.
loads
(
chat_completion
.
choices
[
0
]
.
message
.
model_dump_json
(
include
=
{
"tool_calls"
}
)
)
generated_args
=
generated_tool_call
[
"tool_calls"
]
[
0
]
[
"function"
]
[
"arguments"
]
final_args
=
json
.
loads
(
generated_args
)
params
=
{
"api_key"
:
os
.
environ
[
"SERPAPI_API_KEY"
]
,
}
if
final_args
[
"arrival_date"
]
is
not
None
:
# Create params for the SerpApi for finding flights matching the user query
params
.
update
(
{
"hl"
:
"en"
,
"currency"
:
"USD"
,
"engine"
:
"google_flights"
,
"arrival_id"
:
final_args
[
"arrival_id"
]
,
"return_date"
:
final_args
[
"arrival_date"
]
,
"departure_id"
:
final_args
[
"departure_id"
]
,
"outbound_date"
:
final_args
[
"departure_date"
]
,
}
)
# Obtain the relevant content on YouTube
search
=
GoogleSearch
(
params
)
# Return it as the response to the API endpoint
resp
=
search
.
get_dict
(
)
if
final_args
[
"arrival_date"
]
is
not
None
:
return
{
"flights"
:
[
{
"price"
:
flight
[
"price"
]
,
"airline_logo"
:
single_flight
[
"airline_logo"
]
,
"arrival_airport_name"
:
single_flight
[
"arrival_airport"
]
[
"name"
]
,
"arrival_airport_time"
:
single_flight
[
"arrival_airport"
]
[
"time"
]
,
"departure_airport_name"
:
single_flight
[
"departure_airport"
]
[
"name"
]
,
"departure_airport_time"
:
single_flight
[
"departure_airport"
]
[
"time"
]
,
}
for
flight
in
resp
[
"best_flights"
]
for
single_flight
in
flight
[
"flights"
]
[
:
3
]
]
}
Run FastAPI App Locally
Run your FastAPI application by executing the following command in another terminal window:
1
2
uvicorn main
:
app
-
-
reload
The app should be running on
localhost:8000
. Let’s keep it running while we create an user interface to invoke the chat endpoint to create responses to user queries.
Create a new Next.js application
Let’s get started by creating a new Next.js project. Open your terminal and run the following command:
1
2
npx create-next-app@latest genai-ui
When prompted, choose:
•
Yes
when prompted to use TypeScript.
•
No
when prompted to use ESLint.
•
Yes
when prompted to use Tailwind CSS.
•
No
when prompted to use
src/
directory.
•
Yes
when prompted to use App Router.
•
No
when prompted to customize the default import alias (
@/*
).
Once that is done, move into the project directory and start the app in development mode by executing the following command:
1
2
3
cd genai-ui
npm run dev
The app should be running on
localhost:3000
.
Install AI SDK
In your terminal window, run the command below to install the necessary library for building the conversation user interface:
1
2
npm install
[email protected]
The above command installs the following:
•
ai
library to build AI-powered streaming text and chat UIs.
Build Conversation User Interface
Inside the
app
directory, replace the code inside
page.tsx
file with the following code:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
// File: app/page.tsx
"use client"
;
import
{
useChat
}
from
"ai/react"
;
interface
FlightObj
{
airline_logo
:
string
;
price
:
string
|
number
;
departure_airport_name
:
string
;
departure_airport_time
:
string
;
arrival_airport_name
:
string
;
arrival_airport_time
:
string
;
}
export
default
function
(
)
{
const
{
messages
,
handleSubmit
,
input
,
handleInputChange
}
=
useChat
(
{
api
:
"http://localhost:8000/chat"
,
}
)
;
return
(
<
div
className
=
"
flex flex-col bg-white items-center w-screen min-h-screen
"
>
<
form
onSubmit
=
{
handleSubmit
}
className
=
"
mt-12 flex w-full max-w-[300px] flex-col
"
>
<
input
id
=
"
input
"
name
=
"
prompt
"
value
=
{
input
}
autoComplete
=
"
off
"
onChange
=
{
handleInputChange
}
placeholder
=
"
What kind of movies you want to watch?
"
className
=
"
mt-3 min-w-[300px] rounded border px-2 py-1 outline-none focus:border-black text-black
"
/>
<
button
type
=
"
submit
"
className
=
"
mt-3 max-w-max rounded border px-3 py-1 outline-none text-black hover:bg-black hover:text-white
"
>
Ask &rarr;
</
button
>
{
messages
.
map
(
(
message
,
i
)
=>
message
.
role
===
"assistant"
?
(
<
div
key
=
{
`
response_
${
i
}
`
}
className
=
"
mt-3 pt-3 flex flex-col
"
>
{
JSON
.
parse
(
message
.
content
)
[
"videos"
]
?
(
JSON
.
parse
(
message
.
content
)
.
flights
.
map
(
(
flight
:
FlightObj
,
_
:
number
)
=>
(
<
div
key
=
{
`
flight_
${
_
}
_
${
i
}
`
}
className
=
"
mt-3 flex flex-col
"
>
<
div
className
=
"
flex flex-row items-center gap-x-3
"
>
<
img
loading
=
"
lazy
"
className
=
"
size-10
"
src
=
{
flight
.
airline_logo
}
/>
<
span
>
USD
{
flight
.
price
}
</
span
>
</
div
>
<
div
className
=
"
flex flex-row items-center gap-x-3
"
>
<
span
>
{
flight
.
departure_airport_name
}
</
span
>
<
span
>
{
flight
.
departure_airport_time
}
</
span
>
</
div
>
<
div
className
=
"
flex flex-row items-center gap-x-3
"
>
<
span
>
{
flight
.
arrival_airport_name
}
</
span
>
<
span
>
{
flight
.
arrival_airport_time
}
</
span
>
</
div
>
</
div
>
)
)
)
}
</
div
>
)
:
(
<
div
className
=
"
mt-3 border-t text-black pt-3
"
key
=
{
message
.
content
+
i
}
>
{
message
.
content
}
</
div
>
)
)
}
</
form
>
</
div
>
)
;
}
The code above does the following:
•
Imports the
useChat
hook by
ai
SDK to manage the conversation between user and the application. It takes care of saving the entire conversation (on the client-side) and using them as the request body when it calls the user defined
api
endpoint to fetch the response from chatbot.
•
Exports a React component that returns a form containing an
<input>
element to allow users to enter their query. It then loops over all the messages in the entire conversation, including the latest response to the user query.
•
Finally, loops over the list of flights and creates their preview using flight’s arrival and departure details, the airline it’s for and it’s cost.
Run Next.js Application Locally
Run your Next.js application by executing the following command in another terminal window:
1
2
npm run build && npm run start
The app should be running on
localhost:3000
.
Conclusion
In this tutorial, you learned how to create a real-time recommendation system using SerpApi and Fireworks AI. With Fireworks
Firefunction-v2
, you’re able to identify exactly the set parameters from a dynamically received user prompt, and defining a set of pre-knowledge to help the AI predict the user needs even better.
Now, just imagine the convenience of planning your next adventure, thanks to the intelligence of AI.
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
