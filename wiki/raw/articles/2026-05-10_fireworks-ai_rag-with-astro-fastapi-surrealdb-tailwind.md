---
title: "Building a RAG with Astro, FastAPI, SurrealDB and Llama 3.1"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/rag-with-astro-fastapi-surrealdb-tailwind"
scraped: "2026-05-10T01:20:56.500320+00:00"
lastmod: "2026-02-12T18:52:51.000Z"
type: "sitemap"
---

# Building a RAG with Astro, FastAPI, SurrealDB and Llama 3.1

**Source**: [https://fireworks.ai/blog/rag-with-astro-fastapi-surrealdb-tailwind](https://fireworks.ai/blog/rag-with-astro-fastapi-surrealdb-tailwind)

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
Rag With Astro Fastapi Surrealdb Tailwind
Building a RAG with Astro, FastAPI, SurrealDB and Llama 3.1
PUBLISHED
8/14/2024
Table of Contents
Prerequisites
Tech Stack
High-Level Data Flow and Operations
Step 1: Setup SurrealDB Server
Step 2: Generate
Step 3: Create a new FastAPI application
Install Dependencies
Define Data Models using Pydantic
Use Fireworks API Key
Use Fireworks Nomic AI Embeddings Model
Define SurrealDB Vector Store
Initialize FastAPI App
Create a Knowledge Update API endpoint
Create a Chat API endpoint
Run FastAPI App Locally
Create a new Astro application
Add Tailwind CSS to the application
Integrate React in your Astro project
Install an AI SDK and Axios
Build Conversation User Interface
Build User Interface to Update Application’s Knowledge
Run Astro Application Locally
Conclusion
Table of Contents
Table of Contents
Prerequisites
Tech Stack
High-Level Data Flow and Operations
Step 1: Setup SurrealDB Server
Step 2: Generate
Step 3: Create a new FastAPI application
Install Dependencies
Define Data Models using Pydantic
Use Fireworks API Key
Use Fireworks Nomic AI Embeddings Model
Define SurrealDB Vector Store
Initialize FastAPI App
Create a Knowledge Update API endpoint
Create a Chat API endpoint
Run FastAPI App Locally
Create a new Astro application
Add Tailwind CSS to the application
Integrate React in your Astro project
Install an AI SDK and Axios
Build Conversation User Interface
Build User Interface to Update Application’s Knowledge
Run Astro Application Locally
Conclusion
Table of Contents
Large Language Models have revolutionized how we retrieve information or build search systems. Retrieval-augmented generation (RAG) methodology has become a common way to access or extract information.
This guide teaches you how to build a Retrieval-Augmented Generation application using SurrealDB, Fireworks, FastAPI, and Astro. By the end of this guide, you will be able to update the chatbot’s knowledge visually and obtain the latest and personalized responses to your queries.
Prerequisites
You'll need the following:
•
Node.js 18
or later
•
A
Fireworks
account
Tech Stack
The following technologies are used in creating our RAG application:
Technology
Type
Description
FastAPI
Framework
A high performance framework to build APIs with Python 3.8+.
Astro
Framework
Framework for building fast, modern websites with serverless backend support.
TailwindCSS
Framework
CSS framework for building custom designs.
SurrealDB
Platform
A multi-model database platform.
Fireworks
Platform
Lightning-fast Inference platform to run generative AI models.
High-Level Data Flow and Operations
This is a high-level architecture of how data is flowing and operations that take place 👇🏻
•
When a user asks a question, relevant vectors to the latest user question are queried from SurrealDB. Further, they are combined with the user messages to create a system context. The response is then streamed to the user from Fireworks hosted
Llama 3.1 405B Instruct
Model.
•
When a user updates the existing knowledge other system, vector embeddings with metadata are created for the particular information, and then pushed to SurrealDB
Step 1: Setup SurrealDB Server
You can find various methods to install and run the SurrealDB server in the
documentation
. Let's opt for installing SurrealDB using its dedicated
install script
for our scenario. In your terminal window, execute the following command:
1
2
curl
--
proto
'=https'
--
tlsv1
.
2
-
sSf https
:
/
/
install
.
surrealdb
.
com
|
sh
The above command attempts to install the latest version of SurrealDB (per your platform and CPU type) into the
/usr/local/bin
folder in your system.
Once that is done, execute the following command in your terminal window:
1
2
surreal start
--
log trace
--
user root
--
pass root
--
bind
0.0
.0
.0
:
4304
file
:
mydatabase
.
db
The above command does the following:
•
Starts the SurrealDB server at
0.0.0.0:4304
network address.
•
Enables trace level logging producing verbose logs in your terminal window.
•
Sets the user and password of the default database as
root
.
•
Creates the file
mydatabase.db
to persist data on your filesystem.
Step 2: Generate
Fireworks AI API Key
Model inference requests to the Fireworks API require an API Key. To generate this API key, log in to your Fireworks account and navigate to
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
"<YOUR_FIREWORKS_API_KEY>"
Step 3: Create a new FastAPI application
First, let's start by creating a new project. You can create a new directory by executing the following command in your terminal window:
1
2
3
4
# Create and move to the new directory
mkdir chat-streaming
cd chat-streaming
Install Dependencies
Next, you can install the required dependencies by executing the following command in your terminal window:
1
2
3
4
5
pip install surrealdb
pip install fireworks-ai
pip install langchain langchain-community langchain_fireworks
pip install fastapi "uvicorn[standard]"
The above command installs the required libraries to run ASGI Server, FastAPI, Fireworks AI, SurrealDB and LangChain in your Python project.
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
19
20
21
22
import uuid, os
from typing import List
# FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
## Streaming Response utility
from fastapi.responses import StreamingResponse
## Enable CORS utility
from fastapi.middleware.cors import CORSMiddleware
# Fireworks SDK
import fireworks.client
# SurrealDB Vector Store SDK for LangChain
from langchain_community.vectorstores import SurrealDBStore
# Fireworks Embeddings Integration via LangChain
from langchain_fireworks import FireworksEmbeddings
The above code imports the following:
•
os
module to use the environment variable you’ve set earlier.
•
List
to denote a list of elements of specific type.
•
BaseModel
class to define models of the request body FastAPI endpoints.
•
StreamingResponse
class to generate streaming responses from FastAPI endpoints.
•
CORSMiddleware
FastAPI middleware to enable Cross Origin Resource Sharing of FastAPI endpoints.
•
fireworks.client
SDK for conveniently accessing Fireworks supported LLMs.
•
SurrealDBStore
class by LangChain to use SurrealDB as vector store.
•
FireworksEmbeddings
class via LangChain Fireworks integration to use Nomic AI Embeddings Model.
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
10
11
12
13
# Class representing the string of messages to be searched and embedded as system context.
class LearningMessages(BaseModel):
messages: str
# Class representing a single message of the conversation between RAG application and user.
class Message(BaseModel):
role: str
content: str
# Class representing collection of messages above.
class Messages(BaseModel):
messages: List[Message]
The above code defines three
Pydantic
models:
•
LearningMessages
: a model that will store the input string with a single field called
messages
.
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
Use Fireworks API Key
To set the Fireworks API key used by Fireworks AI module internally, append the following code in
main.py
file:
1
2
3
# Set the Fireworks API Key
fireworks.client.api_key = os.environ["FIREWORKS_API_KEY"]
The above code uses the
os
module to load the environment variable
FIREWORKS_API_KEY
as Firework’s API Key.
Use Fireworks Nomic AI Embeddings Model
To use
FireworksEmbeddings
class to create an embeddings generator using the
nomic-ai/nomic-embed-text-v1.5
, append the following code in
main.py
file:
1
2
3
# Load the nomic-embed-text-v1.5 embedding models via Langchain Fireworks Integration
embeddings = FireworksEmbeddings(model="nomic-ai/nomic-embed-text-v1.5",fireworks_api_key=os.getenv("FIREWORKS_API_KEY"))
Define SurrealDB Vector Store
To define the SurrealDB vector store configuration, append the following code in
main.py
file:
1
2
3
4
5
6
dburl = "ws://localhost:4304/rpc"
db_user = "root"
db_pass = "root"
vector_collection = "vectors"
vector_db = SurrealDBStore(dburl=dburl, db_user=db_user, db_pass=db_pass, collection=vector_collection, embedding_function=embeddings)
The above code uses the following values to establish a SurrealDB Vector Store with LangChain:
•
ws://localhost:4304/rpc
as the database URL to establish a WebSocket connection with SurrealDB. Using a WebSocket connection allows to send and receive messages from SurrealDB using the WebSocket API.
•
root
as both the username and password of the SurrealDB instance.
•
vectors
as the collection name of the vector store to and from which the relevant vectors will be inserted and queried from.
•
Uses
embeddings
generator as the embedding function.
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
app = FastAPI()
# Add CORS middleware
app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)
The code above creates a FastAPI instance and uses the
CORSMIddleware
middleware to enable Cross Origin requests. This allows your frontend to successfully POST to the RAG application endpoints to fetch responses to the user query, regardless of the port it is running on.
Create a Knowledge Update API endpoint
To update application’s knowledge in realtime by generating vector embeddings and inserting them into SurrealDB, you’ll create an
/update
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
@app.post('/update')
async def update(messages: LearningMessages):
messages_json = messages.model_dump()["messages"].split(',')
# Initialize SurrealDB
await vector_db.initialize()
# Create texts to be inserted into the Vector Store (Embeddings are generated automatically)
metadatas = [{"len": len(t)} for t in messages_json]
ids = [str(uuid.uuid4()) for _ in messages_json]
await vector_db.aadd_texts(messages_json, metadatas=metadatas, ids=ids)
update(messages: LearningMessages)
method -
•
Accepts a single string as
messages
containing comma (,) separated messages to be inserted in your SurrealDB vector store.
•
Awaits connection set up with SurrealDB.
•
Creates
metadata
list, each item being length of each message received as input.
•
Creates
ids
list, each item being a randomly generated id for each message received as input.
•
Using the
embeddings
generator passed as the embeddings function, it generates the vector embedding of each message. Alongwith each message’s metadata, it inserts the vector embedding into the SurrealDB vector store.
Create a Chat API endpoint
To generate personalized responses that uses the application’s existing knowledge, you’ll create an
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
21
@app.post("/chat")
async def chat(messages: Messages):
messages_json = (messages.model_dump())['messages']
# Initialize SurrealDB
await vector_db.initialize()
# Create System Context
knowledge = "Only answer what you know. If do not know, say it's an unknown. Following are the things you know of:\n"
relevant_content = await vector_db.asimilarity_search(messages_json[-1]['content'])
if relevant_content:
for each_content in relevant_content:
knowledge += each_content.page_content
messages_json.insert(0, { "role": "system", "content": knowledge })
# Create LLAMA Completion Responses
response = fireworks.client.ChatCompletion.create(
stream=True,
prompt_or_messages=messages_json,
model="accounts/fireworks/models/llama-v3p1-70b-instruct",
)
# Stream the response from requests.post
return StreamingResponse(yield_content(response))
chat(messages: Messages)
method -
•
Accepts a list of
Message
model as
messages
.
•
Awaits connection set up with SurrealDB.
•
Defines a system prompt to restrict it to answer what it already knows.
•
Performs a similarity search on the latest
Message
, which represents a user query.
•
Loops over all similar vector embeddings and appends them into the system prompt defined earlier.
•
Prepends a
Message
model, representing role of the system and it’s content as the system prompt created.
•
Uses fireworks Chat Completion API to stream LLAMA 3.1 70B Chat model context aware responses.
•
Returns a StreamingResponse using the
yield_content
function.
The
yield_content
function loops over each
Document
(received as the similar vector with it’s metadata), and streams the
content
value of it as part of the API response.
1
2
3
4
5
6
# Function to yield content from each choice
def yield_content(response):
for chunk in response:
if chunk.choices[0].delta.content:
yield chunk.choices[0].delta.content
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
import uuid, os
from typing import List
# FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
## Streaming Response utility
from fastapi.responses import StreamingResponse
## Enable CORS utility
from fastapi.middleware.cors import CORSMiddleware
# Fireworks SDK
import fireworks.client
# SurrealDB Vector Store SDK for LangChain
from langchain_community.vectorstores import SurrealDBStore
# Fireworks Embeddings Integration via LangChain
from langchain_fireworks import FireworksEmbeddings
# Class representing the string of messages to be searched and embedded as system context.
class LearningMessages(BaseModel):
messages: str
# Class representing a single message of the conversation between RAG application and user.
class Message(BaseModel):
role: str
content: str
# Class representing collection of messages above.
class Messages(BaseModel):
messages: List[Message]
# Set the Fireworks API Key
fireworks.client.api_key = os.getenv("FIREWORKS_API_KEY")
# Load the nomic-embed-text-v1.5 embedding models via Langchain Fireworks Integration
embeddings = FireworksEmbeddings(model="nomic-ai/nomic-embed-text-v1.5",fireworks_api_key=os.getenv("FIREWORKS_API_KEY"))
dburl = "ws://localhost:4304/rpc"
db_user = "root"
db_pass = "root"
vector_collection = "vectors"
vector_db = SurrealDBStore(dburl=dburl, db_user=db_user, db_pass=db_pass, collection=vector_collection, embedding_function=embeddings)
app = FastAPI()
# Add CORS middleware
app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)
# Function to yield content from each choice
def yield_content(response):
for chunk in response:
if chunk.choices[0].delta.content:
yield chunk.choices[0].delta.content
@app.post('/update')
async def update(messages: LearningMessages):
messages_json = messages.model_dump()["messages"].split(',')
# Initialize SurrealDB
await vector_db.initialize()
# Create texts to be inserted into the Vector Store (Embeddings are generated automatically)
metadatas = [{"len": len(t)} for t in messages_json]
ids = [str(uuid.uuid4()) for _ in messages_json]
await vector_db.aadd_texts(messages_json, metadatas=metadatas, ids=ids)
@app.post("/chat")
async def chat(messages: Messages):
messages_json = (messages.model_dump())['messages']
# Initialize SurrealDB
await vector_db.initialize()
# Create System Context
knowledge = "Only answer what you know. If do not know, say it's an unknown. Following are the things you know of:\n"
relevant_content = await vector_db.asimilarity_search(messages_json[-1]['content'])
if relevant_content:
for each_content in relevant_content:
knowledge += each_content.page_content
messages_json.insert(0, { "role": "system", "content": knowledge })
# Create LLAMA Completion Responses
response = fireworks.client.ChatCompletion.create(
stream=True,
prompt_or_messages=messages_json,
model="accounts/fireworks/models/llama-v3p1-405b-instruct",
)
# Stream the response from requests.post
return StreamingResponse(yield_content(response))
Run FastAPI App Locally
Execute the following command in another terminal window:
1
2
uvicorn main:app --reload
The app should be running on
localhost:8000
. Let’s keep it running while we create an user interface to invoke the endpoints to create responses to user queries.
Create a new Astro application
Let’s get started by creating a new Astro project. Open your terminal and run the following command:
1
2
npm create astro@latest chat-ui
npm create astro
is the recommended way to scaffold an Astro project quickly.
When prompted, choose the following:
•
Empty
when prompted on how to start the new project.
•
Yes
when prompted whether to write Typescript.
•
Strict
when prompted how strict Typescript should be.
•
Yes
when prompted to whether install dependencies.
•
Yes
when prompted to whether initialize a git repository.
Once that’s done, you can move into the project directory and start the app:
1
2
3
cd chat-ui
npm run dev
The app should be running on
localhost:4321
. Let's close the development server as we move on to integrate TailwindCSS into the application.
Add Tailwind CSS to the application
For styling the app, you will be using Tailwind CSS. Install and set up Tailwind CSS at the root of our project's directory by running:
1
2
npx astro add tailwind
When prompted, choose:
•
Yes
when prompted to install the Tailwind dependencies.
•
Yes
when prompted to generate a minimal
tailwind.config.mjs
file.
•
Yes
when prompted to make changes to Astro configuration file.
With choices as above, the command finishes integrating TailwindCSS into your Astro project. It installed the following dependency:
•
tailwindcss
: TailwindCSS as a package to scan your project files to generate corresponding styles.
•
@astrojs/tailwind
: The adapter that brings Tailwind's utility CSS classes to every
.astro
file and framework component in your project.
To create reactive interfaces quickly, let’s move onto integrating React in your application.
Integrate React in your Astro project
To prototype the reactive user interface quickly, you are gonna use React as the library with Astro. In your terminal window, execute the following command:
1
2
npx astro add react
npx
allows us to execute npm packages binaries without having to first install it globally.
When prompted, choose the following:
•
Yes
when prompted whether to install the React dependencies.
•
Yes
when prompted whether to make changes to Astro configuration file.
•
Yes
when prompted whether to make changes to
tsconfig.json
file.
To create conversation user interface easily, let’s move onto installing an AI SDK in your application.
Install an AI SDK and Axios
In your terminal window, run the command below to install the necessary library for building the conversation user interface:
1
2
npm install ai axios
The above command installs the following:
•
ai
library to build AI-powered streaming text and chat UIs.
•
axios
library to make HTTP requests.
Build Conversation User Interface
Inside
src
directory, create a
Chat.jsx
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
//
File
:
src
/
Chat
.
jsx
import
{
useChat
}
from
'ai/react'
export default function
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
'http://localhost:8000/chat'
,
}
)
return
(
<
form className
=
"mt-12 flex w-full max-w-[300px] flex-col"
onSubmit
=
{
handleSubmit
}
>
<
input
id
=
"input"
name
=
"prompt"
value
=
{
input
}
onChange
=
{
handleInputChange
}
placeholder
=
"What's your next question?"
className
=
"mt-3 rounded border px-2 py-1 outline-none focus:border-black"
/
>
<
button className
=
"mt-3 max-w-max rounded border px-3 py-1 outline-none hover:bg-black hover:text-white"
type
=
"submit"
>
Ask
&
rarr
;
<
/
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
=
>
(
<
div className
=
"mt-3 border-t pt-3"
key
=
{
i
}
>
{
message
.
content
}
<
/
div
>
)
)
}
<
/
form
>
)
}
chat.jsx
does the following:
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
Now, let’s create a component that will allow the user to supply some strings to the application to take into consideration before it answers any of the user query.
Build User Interface to Update Application’s Knowledge
Inside
src
directory, create a
Update.jsx
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
//
File
:
src
/
Update
.
jsx
import
axios
from
'axios'
import
{
useState
}
from
'react'
export default function
(
)
{
const
[
messages
,
setMessages
]
=
useState
(
''
)
return
(
<
form
className
=
"mt-12 flex w-full max-w-[300px] flex-col"
onSubmit
=
{
(
e
)
=
>
{
e
.
preventDefault
(
)
axios
.
post
(
'http://localhost:8000/update'
,
{
messages
,
}
)
}
}
>
<
textarea
value
=
{
messages
}
id
=
"learn_messages"
name
=
"learn_messages"
onChange
=
{
(
e
)
=
>
setMessages
(
e
.
target
.
value
)
}
placeholder
=
"Things to learn [seperated by comma (,)]"
className
=
"mt-3 rounded border px-2 py-1 outline-none focus:border-black"
/
>
<
button className
=
"mt-3 max-w-max rounded border px-3 py-1 outline-none hover:bg-black hover:text-white"
type
=
"submit"
>
Learn
&
rarr
;
<
/
button
>
<
/
form
>
)
}
Update.jsx
-
•
Imports
axios
library and
useState
hook by React.
•
Exports a React component that returns a form containing an
<textarea>
element to allow users to enter multiple strings, wherein each string is represented between comma(s).
•
Upon form submission, it POSTs the messages as JSON to the
http://localhost:8000/update
endpoint.
•
To use the React components on the home page of your Astro application, make the following changes in
src/pages/index.astro
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
-
-
-
+
import
Chat
from
'../Chat'
+
import
Update
from
'../Update'
-
-
-
<
html lang
=
"en"
>
<
head
>
<
meta charset
=
"utf-8"
/
>
<
link rel
=
"icon"
type
=
"image/svg+xml"
href
=
"/favicon.svg"
/
>
<
meta name
=
"viewport"
content
=
"width=device-width"
/
>
<
meta name
=
"generator"
content
=
{
Astro
.
generator
}
/
>
<
title
>
Astro
<
/
title
>
<
/
head
>
<
body
class
=
"flex w-screen flex-col items-center"
>
-
<
h1
>
Astro
<
/
h1
>
+
<
Update client
:
load
/
>
+
<
Chat client
:
load
/
>
<
/
body
>
<
/
html
>
The changes above being with importing both the Chat and Update React components. Then, it uses Astro's
client:load
directive
to make sure that both the components are loaded and hydrated immediately on the page.
Run Astro Application Locally
Run your Astro application by executing the following command in another terminal window:
1
2
npm run build
&
&
npm run preview
The app should be running on
localhost:4321
.
Conclusion
Congratulations, you created a Retrieval-Augmented Generation application using
SurrealDB
and
Fireworks AI
. With SurrealDB’s vector store, you are able to insert and update vector embeddings on the fly over WebSockets, and perform similarity search to user queries using vector embeddings generated internally for you.
Further, using Fireworks AI, you are able to invoke Llama 3.1 70B Chat model with system context and generate personalized responses to user queries.
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
