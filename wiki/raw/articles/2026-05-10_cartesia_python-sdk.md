---
title: "Cartesia Python SDK v2.0.0 - Cartesia"
source: "Cartesia Blog"
url: "https://cartesia.ai/blog/python-sdk"
scraped: "2026-05-10T01:19:25.078707+00:00"
lastmod: "None"
type: "sitemap"
---

# Cartesia Python SDK v2.0.0 - Cartesia

**Source**: [https://cartesia.ai/blog/python-sdk](https://cartesia.ai/blog/python-sdk)

Meet Sonic-3: the best text-to-speech for voice agents
|
Learn more
Meet Sonic-3: the best text-to-speech for voice agents
|
Learn more
Sonic-3: the best text-to-speech for voice agents
Models
new
Agents
Solutions
Resources
Pricing
Contact sales
Sign in
Start for Free
Start for Free
Mar 28, 2025
·
Engineering
Cartesia Python SDK v2.0.0
Cartesia Python SDK v2.0.0
Arjun Desai
We are excited to announce the release of v2.0.0 of our Python SDK, polishing the developer experience when using Cartesia's AI voice capabilities with Python.
Getting started with Cartesia using Python
Install the Cartesia Python SDK in your project with:
pip
install
cartesia
pip
install
cartesia
pip
install
cartesia
pip
install
cartesia
Initialize the SDK and authenticate:
from
cartesia
import
Cartesia
import
os
client
=
Cartesia
(
api_key
=
os
.
getenv
(
"CARTESIA_API_KEY"
)
)
from
cartesia
import
Cartesia
import
os
client
=
Cartesia
(
api_key
=
os
.
getenv
(
"CARTESIA_API_KEY"
)
)
from
cartesia
import
Cartesia
import
os
client
=
Cartesia
(
api_key
=
os
.
getenv
(
"CARTESIA_API_KEY"
)
)
from
cartesia
import
Cartesia
import
os
client
=
Cartesia
(
api_key
=
os
.
getenv
(
"CARTESIA_API_KEY"
)
)
Now, you can start making requests. For example, to generate audio with Cartesia's text-to-speech model:
client
.
tts
.
bytes
(
model_id
=
"sonic-2"
,
transcript
=
"Hello, world!"
,
voice
=
{
"mode"
:
"id"
,
"id"
:
"694f9389-aac1-45b6-b726-9d9369183238"
,
}
,
language
=
"en"
,
output_format
=
{
"container"
:
"wav"
,
"sample_rate"
:
44100
,
"encoding"
:
"pcm_f32le"
,
}
,
)
client
.
tts
.
bytes
(
model_id
=
"sonic-2"
,
transcript
=
"Hello, world!"
,
voice
=
{
"mode"
:
"id"
,
"id"
:
"694f9389-aac1-45b6-b726-9d9369183238"
,
}
,
language
=
"en"
,
output_format
=
{
"container"
:
"wav"
,
"sample_rate"
:
44100
,
"encoding"
:
"pcm_f32le"
,
}
,
)
client
.
tts
.
bytes
(
model_id
=
"sonic-2"
,
transcript
=
"Hello, world!"
,
voice
=
{
"mode"
:
"id"
,
"id"
:
"694f9389-aac1-45b6-b726-9d9369183238"
,
}
,
language
=
"en"
,
output_format
=
{
"container"
:
"wav"
,
"sample_rate"
:
44100
,
"encoding"
:
"pcm_f32le"
,
}
,
)
client
.
tts
.
bytes
(
model_id
=
"sonic-2"
,
transcript
=
"Hello, world!"
,
voice
=
{
"mode"
:
"id"
,
"id"
:
"694f9389-aac1-45b6-b726-9d9369183238"
,
}
,
language
=
"en"
,
output_format
=
{
"container"
:
"wav"
,
"sample_rate"
:
44100
,
"encoding"
:
"pcm_f32le"
,
}
,
)
For more examples, check out our
API Explorer
to generate Python code snippets for any of
our APIs
.
The Python SDK at a glance
Building upon industry established SDK patterns, v2 of our Python SDK delivers a great development experience structured around a primary Cartesia client, which is the entry point for accessing the various API endpoints.
Even more features
Basic Client
- Instantiate and use the client with just 24 lines of code.
Async Client
- The SDK exports an
async
client alongside standard real-time calls, allowing you to make non-blocking API requests.
Streaming
- The SDK supports streaming responses and outputs a generator that you can iterate over.
WebSocket
- Integrate using WebSockets to build realtime, low-latency voice applications.
Exception Handling
- The API gracefully handles non-success status codes (4xx and 5xx responses).
Retries
- The SDK is instrumented with automatic retries with exponential backoff.
Timeouts
- The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.
Custom Client
—
You can override the
httpx
client to customize it for your use-case. Some common use-cases include support for proxies and transports.
What’s next?
We can’t wait to see what you build with the
Cartesia Python SDK
! Your feedback helps us improve—let us know your thoughts on our
Discord
or by submitting issues on
GitHub
.
Try our Python SDK today
Learn more about the implementation details
Learn more about the implementation details
Integrate now
Related articles
Related articles
Sep 24, 2025
·
News
Cartesia achieves GDPR compliance
Aug 19, 2025
·
News
Introducing Line: The Modern Voice Agent Development Platform
Jul 11, 2025
·
Research
Hierarchical modeling
Sep 24, 2025
·
News
Cartesia achieves GDPR compliance
Aug 19, 2025
·
News
Introducing Line: The Modern Voice Agent Development Platform
Real-time, multimodal intelligence for every device.
Models
Sonic
Ink
Agents
Solutions
Customer service
Localization
Recruiting
Sales
Finance
Healthcare
Gaming
Hospitality
Regions
Asia pacific
Brazil
China
India
Japan
Korea
Latin America
Middle East
North America
Western Europe
Eastern Europe
Resources
Blog
Customers
Docs
Events
Pricing
Research
Support
Company
About
Careers
Legal
Terms of Service
Privacy
Acceptable Use
Cookie Settings
Real-time, multimodal intelligence for every device.
Models
Sonic
Ink
Agents
Solutions
Customer service
Localization
Recruiting
Sales
Finance
Healthcare
Gaming
Hospitality
Regions
Asia pacific
Brazil
China
India
Japan
Korea
Latin America
Middle East
North America
Western Europe
Eastern Europe
Resources
Blog
Customers
Docs
Events
Pricing
Research
Support
Company
About
Careers
Legal
Terms of Service
Privacy
Acceptable Use
Cookie Settings
Real-time, multimodal intelligence for every device.
Models
Sonic
Ink
Agents
Solutions
Customer service
Localization
Recruiting
Sales
Finance
Healthcare
Gaming
Hospitality
Regions
Asia pacific
Brazil
China
India
Japan
Korea
Latin America
Middle East
North America
Western Europe
Eastern Europe
Resources
Blog
Customers
Docs
Events
Pricing
Research
Support
Company
About
Careers
Cookie Settings
Legal
Terms of Use
Privacy
Acceptable Use
