---
title: "From text to task: Constrained generation for structured extraction in R1"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/constrained-generation-with-reasoning"
scraped: "2026-05-10T01:27:39.741480+00:00"
lastmod: "2026-02-12T18:52:26.000Z"
type: "sitemap"
---

# From text to task: Constrained generation for structured extraction in R1

**Source**: [https://fireworks.ai/blog/constrained-generation-with-reasoning](https://fireworks.ai/blog/constrained-generation-with-reasoning)

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
Constrained Generation With Reasoning
From text to task: Constrained generation for structured extraction in R1
PUBLISHED
2/1/2025
Table of Contents
What we’ll cover
How it works
Output
The response from R1
The reasoning
The parsed JSON data
Output
The response from R1
The reasoning
The parsed JSON data
Additional resources
Table of Contents
Table of Contents
What we’ll cover
How it works
Output
The response from R1
The reasoning
The parsed JSON data
Output
The response from R1
The reasoning
The parsed JSON data
Additional resources
Table of Contents
What is constrained generation and why is it useful
Constrained generation
is a technique in natural language processing (NLP) where language models are guided to produce text that adheres to specific predefined rules or structures. This approach is particularly useful in applications requiring structured outputs, such as generating code, creating formatted documents, or producing data in formats like JSON. By enforcing constraints during the text generation process, models can ensure outputs that are not only coherent but also conform to the desired structure, enhancing both the utility and reliability of the generated content.
What we’ll cover
•
How constrained generation works
•
Guiding model token selection
•
Constrained decoding for structured outputs
•
Reasoning models and structured extraction
•
The role of constrained generation in reasoning models
•
Fireworks' JSON mode for reasoning models
•
Examples of constrained generation in action
•
Structured Q&A with reasoning
•
Healthcare records with AI-driven summaries
•
Computer system specifications with structured recommendations
•
Conclusion
•
Why structured generation improves AI reliability
•
Future applications and best practices
How does it work
The process of constrained generation involves manipulating a model's token generation to restrict its next-token predictions to only those that do not violate the required output structure. This can be achieved through various methods, such as constrained decoding, where the model's output is directed to follow specific patterns or formats. For instance, in structured generation tasks, constrained decoding can simplify the next-token prediction space, accelerating generation by allowing some token generation steps to be skipped. Additionally, by focusing only on generating the necessary parts of the output and bypassing boilerplate sections, the overall efficiency of the generation process is improved.
Implementing constrained generation not only enhances the quality of the output by ensuring adherence to desired formats but may also improve performance. By reducing the complexity of the generation task and narrowing down the prediction space, the model can generate outputs more quickly and with greater accuracy. This efficiency gain is particularly beneficial in applications where rapid and reliable generation of structured text is crucial.
Constrained generation in reasoning models
In the context of reasoning models, such as the recently released
DeepSeek R1
, constrained generation plays a pivotal role in ensuring that outputs adhere to specific formats and structures. The DeepSeek R1 model exemplifies this by incorporating a unique mechanism: it generates a reasoning process enclosed within
<think>
and
</think>
tokens, followed by a JSON-formatted output. This structured approach allows the model to transparently display its thought process before presenting the final result. Notably, the JSON schema applies exclusively to the JSON section that follows the
<think>
tags, ensuring that the reasoning process and the final output are clearly delineated and properly formatted. The caller can employ simple output parsing to separate the reasoning section from the structured output.
Example 1: Simple Q&A
In this section, we'll demonstrate how to utilize the
DeepSeek R1
reasoning model in JSON mode
using the Fireworks API
.
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
# Import necessary libraries
import
json
import
re
from
pydantic
import
BaseModel
from
openai
import
OpenAI
import
os
# Initialize the Fireworks client
client
=
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
getenv
(
"FIREWORKS_API_KEY"
)
,
)
# Define the output schema using Pydantic
class
QAResult
(
BaseModel
)
:
question
:
str
answer
:
str
# Prepare the user input
user_input
=
"Who wrote 'Pride and Prejudice'?"
# Construct the messages payload
messages
=
[
{
"role"
:
"user"
,
"content"
:
user_input
}
]
# Make the API call to DeepSeek R1
response
=
client
.
chat
.
completions
.
create
(
model
=
"accounts/fireworks/models/deepseek-r1"
,
messages
=
messages
,
response_format
=
{
"type"
:
"json_object"
,
"schema"
:
QAResult
.
model_json_schema
(
)
}
,
max_tokens
=
1000
,
# Adjust as needed to prevent truncation
)
# Extract the content of the response
response_content
=
response
.
choices
[
0
]
.
message
.
content
print
(
f"Response content:
{
response_content
}
"
)
# Use regular expressions to extract the reasoning and JSON parts.
# The reasoning is enclosed within <think>...</think> tags,
# and the JSON part follows the </think> tag.
reasoning_match
=
re
.
search
(
r"<think>(.*?)</think>"
,
response_content
,
re
.
DOTALL
)
json_match
=
re
.
search
(
r"</think>\s*(\{.*\})"
,
response_content
,
re
.
DOTALL
)
# Extract reasoning
reasoning
=
reasoning_match
.
group
(
1
)
.
strip
(
)
# Extract JSON string
json_str
=
json_match
.
group
(
1
)
.
strip
(
)
# Directly parse the JSON string into a Pydantic model
qa_result
=
QAResult
.
model_validate_json
(
json_str
)
# Output the extracted reasoning and the parsed Pydantic model
print
(
f"\nReasoning:
{
reasoning
}
"
)
print
(
f"\nQAResult:
{
qa_result
}
"
)
How it works
User Input:
A question is submitted to the model (e.g., "Who wrote Pride and Prejudice?").
Constrained Generation:
The model first produces its reasoning, enclosed in
<think>...</think>
, ensuring a structured explanation before providing the answer.
Schema Enforcement:
The JSON-formatted response follows a
Pydantic-defined schema
, ensuring structured data.
Parsing and Validation:
The reasoning section and JSON output are extracted separately, maintaining
cleanly structured and machine-readable responses
.
Let’s show another example, this time for a health care use case.
Example 2: Structured healthcare data generation with reasoning JSON mode
This example showcases how to generate structured healthcare records using Fireworks AI’s DeepSeek R1 model in Reasoning JSON Mode. By combining structured output with an explanation of the model’s thought process, this approach enhances transparency and reliability in AI-generated medical documentation.
The workflow consists of the following steps:
•
Defining a Pydantic Schema
– Ensures consistency in patient records by specifying required fields.
•
Making an API Request
– Generates structured healthcare data tailored to a given medical scenario.
•
Extracting Model Reasoning
– Captures the model’s thought process within
<think>...</think>
tags to provide insights into diagnoses and treatments.
•
Validating and Parsing JSON Output
– Uses Pydantic to ensure compliance with the predefined schema.
This structured approach enables seamless integration of AI-generated healthcare data into medical systems, making it valuable for clinical documentation, decision support, and automated reporting.
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
# Import necessary libraries
import
json
import
re
from
pydantic
import
BaseModel
from
openai
import
OpenAI
import
os
# Load environment variables
from
dotenv
import
load_dotenv
load_dotenv
(
)
# Initialize the Fireworks client with API Key from environment variables
client
=
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
getenv
(
"FIREWORKS_API_KEY"
)
,
)
# Define the structured output schema for a healthcare patient record
class
PatientRecord
(
BaseModel
)
:
name
:
str
age
:
int
gender
:
str
diagnosis
:
str
treatment
:
str
medications
:
str
notes
:
str
# Prepare the user input for generating a structured healthcare record
user_input
=
"Generate a structured healthcare record with reasoning for a patient diagnosed with hypertension."
# Construct the messages payload
messages
=
[
{
"role"
:
"user"
,
"content"
:
user_input
}
]
# Make the API call to DeepSeek R1 using Reasoning JSON Mode
response
=
client
.
chat
.
completions
.
create
(
model
=
"accounts/fireworks/models/deepseek-r1"
,
messages
=
messages
,
response_format
=
{
"type"
:
"json_object"
,
"schema"
:
PatientRecord
.
model_json_schema
(
)
}
,
max_tokens
=
3000
,
# Adjust max tokens to prevent truncation
)
# Extract the content of the response
response_content
=
response
.
choices
[
0
]
.
message
.
content
print
(
f"Response content:
{
response_content
}
"
)
# Use regular expressions to extract the reasoning and JSON parts.
# The reasoning is enclosed within <think>...</think> tags,
# and the JSON part follows the </think> tag.
reasoning_match
=
re
.
search
(
r"<think>(.*?)</think>"
,
response_content
,
re
.
DOTALL
)
json_match
=
re
.
search
(
r"</think>\s*(\{.*\})"
,
response_content
,
re
.
DOTALL
)
# Extract reasoning if present
reasoning
=
reasoning_match
.
group
(
1
)
.
strip
(
)
if
reasoning_match
else
"No reasoning provided."
# Extract JSON string if present
json_str
=
json_match
.
group
(
1
)
.
strip
(
)
if
json_match
else
"{}"
# Parse the JSON string into a Pydantic model
patient_record
=
PatientRecord
.
model_validate_json
(
json_str
)
# Output the extracted reasoning and the parsed patient record
print
(
"\n🧠 Model Reasoning:"
)
print
(
reasoning
)
print
(
"\n📋 Structured Patient Record (JSON Data):"
)
print
(
patient_record
.
model_dump_json
(
indent
=
4
)
)
Output
When the script is run, the outputs would be similar to the following:
The response from R1
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
<
think
>
Okay
,
the user wants a structured healthcare record
for
a patient
with
hypertension
,
including reasoning
.
Let me start by recalling what a standard healthcare record includes
.
Typically
,
there's patient demographics
,
medical history
,
presenting complaints
,
physical exam findings
,
lab results
,
diagnosis
,
management plan
,
and
follow
-
up
.
Plus
,
they want reasoning
,
so I should explain why each part
is
included
.
First
,
demographics
.
John Doe
,
58
,
male
,
African American
.
Wait
,
African Americans have higher hypertension risk
,
so that
's relevant. Also, 10-year history of hypertension, non-compliant with meds—that'
s important
for
management
.
Family history matters because his father had hypertension
and
died of stroke
.
Lifestyle factors
:
sedentary
,
high
-
salt diet
,
smoking
.
Those are modifiable risk factors
.
Okay
,
so addressing those
in
the plan makes sense
.
Presenting complaints
:
headache
,
fatigue
,
chest discomfort
.
Headaches
and
fatigue are common
in
hypertension
.
Chest pain could indicate something more serious like cardiac issues
,
so I need to note that
as
a possible differential diagnosis
,
maybe order an ECG
.
Shortness of breath too—could be heart failure
or
other complications
.
Vitals
:
BP
168
/
100
mmHg
,
which
is
stage
2
hypertension
.
Elevated heart rate—maybe due to anxiety
or
compensation
.
BMI
30
is
obese
,
which
is
a risk factor
.
Waist circumference
and
waist
-
hip ratio also indicate central obesity
,
adding to cardiovascular risk
.
Physical exam
:
JVP normal
,
so maybe no fluid overload
.
Lungs clear
,
no edema—so no signs of heart failure yet
.
Fundoscopy
with
AV nicking
and
arteriolar narrowing—those are hypertensive retinopathy signs
.
Good to include that
as
it shows end
-
organ damage
.
Labs
:
Basic metabolic panel
,
lipid profile
,
urinalysis
.
Elevated creatinine suggests possible kidney impairment—hypertension can cause that
.
LDL high
,
HDL low
,
which are cardiovascular risks
.
Urinalysis shows proteinuria
,
indicating kidney damage
.
Microalbuminuria
is
an early sign
.
So
,
these labs support the diagnosis
and
show complications
.
Diagnosis
:
Essential hypertension
,
stage
2.
Obesity
and
hyperlipidemia
as
comorbidities
.
Hypertensive retinopathy
and
CKD stage 3a
as
complications
.
Differential diagnoses like secondary hypertension? Maybe check
for
that
with
aldosterone
,
renin levels
.
Pheochromocytoma less likely but mentioned
.
Management plan
:
Pharmacological—ACE inhibitor
(
lisinopril
)
because it's good
in
African Americans
and
for
kidney protection
.
Thiazide diuretic
(
HCTZ
)
for
added effect
.
Statin
for
cholesterol
.
Non
-
pharmacological
:
Lifestyle changes—diet
(
DASH
)
,
exercise
,
smoking cessation
.
Education on med compliance
.
Follow
-
up
in
4
weeks
.
Referral to nephrology
for
CKD
and
nutritionist
for
diet
.
Reasoning
:
Why ACEi? Because
in
African Americans
,
they respond better to ACEi
or
CCBs
.
Also
,
renal protection
.
Thiazide
for
synergy
.
Statin
for
ASCVD risk
.
Lifestyle changes crucial
.
Early CKD needs specialist
input
.
Follow
-
up to adjust meds
and
monitor
.
Follow
-
up plan
:
Adjust meds
if
BP
not
controlled
.
Check labs again
.
24
-
hour BP monitoring
if
needed
.
Patient engagement important to ensure compliance
.
Wait
,
should I mention differential diagnoses reasoning more? Like why secondary hypertension
is
considered? Maybe check
for
resistant hypertension causes
.
Labs like thyroid
,
cortisol? Maybe add those to the lab tests
for
secondary causes
.
But the user might
not
want too much detail
.
They asked
for
structured record
with
reasoning
,
so maybe keep it concise but cover key points
.
Also
,
avoid mentioning lab tests
for
secondary causes
in
the management unless necessary
.
But since differentials include secondary HTN
,
maybe just the aldosterone
/
renin ratio
and
catecholamines
.
TSH
for
thyroid issues
.
That's covered
in
the lab tests
.
Okay
,
making sure the structure
is
clear
and
each section has reasoning
.
Combine
all
into sections
as
per the example
.
Does it flow well? Maybe check
if
all
essential parts are included
.
Yes
,
seems comprehensive
.
Need to make sure the reasoning
is
integrated to show clinical decision
-
making
.
That should cover the user's request
.
<
/
think
>
The reasoning
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
Reasoning
:
Okay
,
the user wants a structured healthcare record
for
a patient
with
hypertension
,
including reasoning
.
Let me start by recalling what a standard healthcare record includes
.
Typically
,
there's patient demographics
,
medical history
,
presenting complaints
,
physical exam findings
,
lab results
,
diagnosis
,
management plan
,
and
follow
-
up
.
Plus
,
they want reasoning
,
so I should explain why each part
is
included
.
First
,
demographics
.
John Doe
,
58
,
male
,
African American
.
Wait
,
African Americans have higher hypertension risk
,
so that
's relevant. Also, 10-year history of hypertension, non-compliant with meds—that'
s important
for
management
.
Family history matters because his father had hypertension
and
died of stroke
.
Lifestyle factors
:
sedentary
,
high
-
salt diet
,
smoking
.
Those are modifiable risk factors
.
Okay
,
so addressing those
in
the plan makes sense
.
Presenting complaints
:
headache
,
fatigue
,
chest discomfort
.
Headaches
and
fatigue are common
in
hypertension
.
Chest pain could indicate something more serious like cardiac issues
,
so I need to note that
as
a possible differential diagnosis
,
maybe order an ECG
.
Shortness of breath too—could be heart failure
or
other complications
.
Vitals
:
BP
168
/
100
mmHg
,
which
is
stage
2
hypertension
.
Elevated heart rate—maybe due to anxiety
or
compensation
.
BMI
30
is
obese
,
which
is
a risk factor
.
Waist circumference
and
waist
-
hip ratio also indicate central obesity
,
adding to cardiovascular risk
.
Physical exam
:
JVP normal
,
so maybe no fluid overload
.
Lungs clear
,
no edema—so no signs of heart failure yet
.
Fundoscopy
with
AV nicking
and
arteriolar narrowing—those are hypertensive retinopathy signs
.
Good to include that
as
it shows end
-
organ damage
.
Labs
:
Basic metabolic panel
,
lipid profile
,
urinalysis
.
Elevated creatinine suggests possible kidney impairment—hypertension can cause that
.
LDL high
,
HDL low
,
which are cardiovascular risks
.
Urinalysis shows proteinuria
,
indicating kidney damage
.
Microalbuminuria
is
an early sign
.
So
,
these labs support the diagnosis
and
show complications
.
Diagnosis
:
Essential hypertension
,
stage
2.
Obesity
and
hyperlipidemia
as
comorbidities
.
Hypertensive retinopathy
and
CKD stage 3a
as
complications
.
Differential diagnoses like secondary hypertension? Maybe check
for
that
with
aldosterone
,
renin levels
.
Pheochromocytoma less likely but mentioned
.
Management plan
:
Pharmacological—ACE inhibitor
(
lisinopril
)
because it's good
in
African Americans
and
for
kidney protection
.
Thiazide diuretic
(
HCTZ
)
for
added effect
.
Statin
for
cholesterol
.
Non
-
pharmacological
:
Lifestyle changes—diet
(
DASH
)
,
exercise
,
smoking cessation
.
Education on med compliance
.
Follow
-
up
in
4
weeks
.
Referral to nephrology
for
CKD
and
nutritionist
for
diet
.
Reasoning
:
Why ACEi? Because
in
African Americans
,
they respond better to ACEi
or
CCBs
.
Also
,
renal protection
.
Thiazide
for
synergy
.
Statin
for
ASCVD risk
.
Lifestyle changes crucial
.
Early CKD needs specialist
input
.
Follow
-
up to adjust meds
and
monitor
.
Follow
-
up plan
:
Adjust meds
if
BP
not
controlled
.
Check labs again
.
24
-
hour BP monitoring
if
needed
.
Patient engagement important to ensure compliance
.
Wait
,
should I mention differential diagnoses reasoning more? Like why secondary hypertension
is
considered? Maybe check
for
resistant hypertension causes
.
Labs like thyroid
,
cortisol? Maybe add those to the lab tests
for
secondary causes
.
But the user might
not
want too much detail
.
They asked
for
structured record
with
reasoning
,
so maybe keep it concise but cover key points
.
Also
,
avoid mentioning lab tests
for
secondary causes
in
the management unless necessary
.
But since differentials include secondary HTN
,
maybe just the aldosterone
/
renin ratio
and
catecholamines
.
TSH
for
thyroid issues
.
That's covered
in
the lab tests
.
Okay
,
making sure the structure
is
clear
and
each section has reasoning
.
Combine
all
into sections
as
per the example
.
Does it flow well? Maybe check
if
all
essential parts are included
.
Yes
,
seems comprehensive
.
Need to make sure the reasoning
is
integrated to show clinical decision
-
making
.
That should cover the user's request
.
The parsed JSON data
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
Patient Record
(
JSON Data
)
:
{
"name"
:
"John Doe"
,
"age"
:
58
,
"gender"
:
"Male"
,
"diagnosis"
:
"Hypertension (Stage 2)"
,
"treatment"
:
"Lisinopril (10 mg daily), Hydrochlorothiazide (12.5 mg daily)"
,
"medications"
:
""
,
"notes"
:
" "
}
Example 3: Generating structured computer system specifications with reasoning JSON mode
In this last example, we show how to generate structured computer system specifications using DeepSeek R1 in Reasoning JSON Mode. By leveraging structured output and model reasoning, this method ensures clear and consistent AI-generated hardware recommendations.
The process involves:
•
Defining a Pydantic Schema
– Enforces structured specifications for computer components.
•
Making an API Request
– Generates PC configurations based on user requirements.
•
Extracting Model Reasoning
– Explains why specific components were selected within
<think>...</think>
tags.
•
Validating and Parsing JSON Output
– Ensures the structured response adheres to expected hardware constraints.
This approach is particularly useful for system builders, procurement tools, and recommendation engines that require AI-driven hardware configurations with explainable decision-making.
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
# Import necessary libraries
import
json
import
re
import
os
from
pydantic
import
BaseModel
,
Field
from
dotenv
import
load_dotenv
from
openai
import
OpenAI
# Load environment variables from .env file
load_dotenv
(
)
# Initialize the Fireworks client
client
=
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
getenv
(
"FIREWORKS_API_KEY"
)
,
)
# Define the output schema using Pydantic
class
Processor
(
BaseModel
)
:
brand
:
str
=
Field
(
pattern
=
"^(Intel|AMD)$"
)
model
:
str
cores
:
int
=
Field
(
ge
=
2
,
le
=
32
)
clock_speed_ghz
:
float
=
Field
(
ge
=
1.0
,
le
=
6.0
)
class
Memory
(
BaseModel
)
:
size_gb
:
int
=
Field
(
ge
=
4
,
le
=
256
)
type
:
str
=
Field
(
pattern
=
"^(DDR4|DDR5)$"
)
class
Storage
(
BaseModel
)
:
type
:
str
=
Field
(
pattern
=
"^(SSD|HDD|NVMe SSD)$"
)
capacity_tb
:
float
=
Field
(
ge
=
0.5
,
le
=
10
)
class
GPU
(
BaseModel
)
:
brand
:
str
=
Field
(
pattern
=
"^(NVIDIA|AMD)$"
)
model
:
str
class
ComputerSpec
(
BaseModel
)
:
processor
:
Processor
memory
:
Memory
storage
:
Storage
gpu
:
GPU
motherboard
:
str
=
Field
(
pattern
=
"^(ATX|Micro-ATX|Mini-ITX)$"
)
cooling
:
str
=
Field
(
pattern
=
"^(Air-cooled|Liquid-cooled)$"
)
networking
:
str
=
Field
(
pattern
=
"^(WiFi 6|WiFi 6E|Gigabit Ethernet|2.5G Ethernet)$"
)
ports
:
list
[
str
]
=
Field
(
min_items
=
1
,
max_items
=
5
)
os
:
str
=
Field
(
pattern
=
"^(Windows 11|macOS Sonoma|Ubuntu 22.04|Fedora 38)$"
)
# Prepare user input
user_input
=
"Generate a structured gaming PC specification with an Intel Core i9, 64GB DDR5 RAM, and an NVIDIA RTX 4090."
# Construct messages payload
messages
=
[
{
"role"
:
"user"
,
"content"
:
user_input
}
]
# Make the API call to DeepSeek R1
response
=
client
.
chat
.
completions
.
create
(
model
=
"accounts/fireworks/models/deepseek-r1"
,
messages
=
messages
,
response_format
=
{
"type"
:
"json_object"
,
"schema"
:
ComputerSpec
.
model_json_schema
(
)
}
,
max_tokens
=
2000
,
# Adjust token limit
)
# Extract the response content
response_content
=
response
.
choices
[
0
]
.
message
.
content
print
(
"Raw Response Content:\n"
,
response_content
)
# Extract the reasoning part enclosed in <think>...</think> tags
reasoning_match
=
re
.
search
(
r"<think>(.*?)</think>"
,
response_content
,
re
.
DOTALL
)
reasoning
=
reasoning_match
.
group
(
1
)
.
strip
(
)
if
reasoning_match
else
"No reasoning provided."
# Extract the JSON part that follows after the reasoning
json_match
=
re
.
search
(
r"</think>\s*(\{.*\})"
,
response_content
,
re
.
DOTALL
)
json_str
=
json_match
.
group
(
1
)
.
strip
(
)
if
json_match
else
"{}"
# Parse the JSON response into the Pydantic model
computer_spec
=
ComputerSpec
.
model_validate_json
(
json_str
)
# Output the extracted reasoning and structured data
print
(
"\nReasoning:\n"
,
reasoning
)
print
(
"\nComputer Specification (JSON Data):"
)
print
(
computer_spec
.
model_dump_json
(
indent
=
4
)
)
Output
When the example above is run, you should see output similar to:
The response from R1
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
<
think
>
Okay
,
the user wants a high
-
performance gaming PC
with
an AMD Ryzen
9
,
64GB DDR5 RAM
,
and
an NVIDIA RTX
3090
GPU
.
Let me start by breaking down each component
.
First
,
the CPU
.
AMD Ryzen
9
series has several options
.
The latest would be the
7000
series
,
like the Ryzen
9
7950X
.
That's
16
cores
,
which
is
overkill
for
gaming but great
for
multitasking
and
future
-
proofing
.
Some users might prefer the 7900X
if
they want a balance
,
but since the user specified Ryzen
9
,
the top
-
tier model seems suitable
.
Next
,
the GPU
:
RTX
3090.
Wait
,
NVIDIA has newer models like the
40
series
.
The
3090
is
still powerful
,
but I should check
if
the user specifically wants the
3090.
Maybe they have a reason
,
like availability
or
specific use cases
.
So stick
with
the
3090
,
but note that a
4080
or
4090
might offer better performance
.
Also
,
the
3090
has 24GB VRAM
,
which
is
great
for
gaming at high resolutions
or
content creation
.
RAM
:
64GB DDR5
.
That
's a lot for gaming. Most games don'
t need more than 32GB
,
but maybe the user
is
into streaming
,
video editing
,
or
heavy multitasking
.
So need to pick a high
-
speed DDR5
,
like 6000MHz
.
CL latency matters
;
lower CL
is
better
.
Maybe a 6000MHz CL30
or
CL32 kit
.
Also
,
ensure it's AMD EXPO certified
for
Ryzen compatibility
.
Motherboard
:
X670E chipset to support the Ryzen
7000
series
.
Need PCIe
5.0
for
future GPUs
and
NVMe
.
Look
for
good VRM cooling
,
multiple M
.
2
slots
,
and
built
-
in
Wi
-
Fi 6E
if
possible
.
Brands like ASUS
,
MSI
,
or
Gigabyte
.
Storage
:
For gaming
,
NVMe SSD
is
a must
.
A 2TB PCIe
4.0
drive like Samsung
980
Pro
or
WD Black SN850X
.
Maybe a 4TB
if
budget allows
.
Also
,
secondary storage could be a larger SATA SSD
or
HDD
,
but the user might prefer
all
NVMe
for
speed
.
Power Supply
:
RTX
3090
is
power
-
hungry
.
A 850W PSU minimum
,
but 1000W to be safe
,
especially
with
a high
-
end CPU
and
room
for
overclocking
.
80
+
Platinum efficiency
.
Modular
for
cable management
.
Brands like Corsair
,
EVGA
,
or
Seasonic
.
Cooling
:
Ryzen
9
can run hot
.
An AIO liquid cooler
with
360mm radiator would be best
.
Arctic Liquid Freezer II
or
Corsair iCUE H150i
.
Good thermal paste also important
.
Case
:
Needs good airflow
.
Lian Li PC
-
O11 Dynamic
or
Corsair 5000D
.
Make sure it fits the 360mm radiator
and
the GPU length
.
Plenty of fan mounts
for
airflow
.
Extras
:
Maybe RGB
for
aesthetics
,
Windows
11
Pro
,
and
a monitor recommendation
.
If the user
is
using a
3090
,
a 4K 144Hz monitor would pair well
.
Peripherals like mechanical keyboard
and
gaming mouse
.
Wait
,
the user didn't mention a budget
,
but high
-
performance implies top
-
tier parts
.
Check
for
possible bottlenecks
.
64GB RAM might be overkill
,
but the user specified it
.
Maybe note that 32GB
is
enough
for
gaming
,
but 64GB
is
for
other tasks
.
Also
,
ensure DDR5
is
dual
-
channel
and
dual
-
rank
for
optimal performance
.
Double
-
check compatibility
:
CPU socket AM5
for
Ryzen
7000
,
motherboard chipset X670E
,
and
ensure the PSU has enough PCIe connectors
for
the GPU
.
Case dimensions
for
all
components
.
Alternative components
if
certain parts are unavailable
.
Mention possible upgrades like adding more storage later
.
Also
,
highlight the reasoning behind each choice to
help
the user understand the build's balance
.
Make sure the total wattage
is
covered by the PSU
.
RTX
3090
can peak around 450W
,
Ryzen
9
7950X up to 230W
,
other components adding maybe 100W
.
Total around 800W at peak
,
so 1000W PSU gives headroom
for
overclocking
and
efficiency
.
Final check
:
No incompatible parts
,
all
components fit
in
the
case
,
adequate cooling
for
both CPU
and
GPU
,
and
high
-
speed storage
for
quick load times
.
<
/
think
>
{
"processor"
:
"AMD Ryzen 9 7950X"
,
"memory"
:
"64GB Corsair Dominator Platinum RGB DDR5 6000MHz (CL30)"
,
"storage"
:
"Primary: 2TB Samsung 990 Pro NVMe SSD (PCIe 4.0) | Secondary: 4TB Seagate BarraCuda HDD"
,
"gpu"
:
"NVIDIA GeForce RTX 3090 Founders Edition (24GB GDDR6X)"
,
"motherboard"
:
"ASUS ROG Crosshair X670E Extreme (Wi-Fi 6E, PCIe 5.0)"
,
"cooling"
:
"NZXT Kraken Z73 360mm AIO Liquid Cooler"
,
"networking"
:
"Onboard 10G LAN + Wi-Fi 6E"
,
"ports"
:
"USB4, Thunderbolt 4, 12x USB 3.2 Gen 2"
,
"os"
:
"Windows 11 Pro 64-bit"
}
The reasoning
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
Reasoning
:
Okay
,
the user wants a high
-
performance gaming PC
with
an AMD Ryzen
9
,
64GB DDR5 RAM
,
and
an NVIDIA RTX
3090
GPU
.
Let me start by breaking down each component
.
First
,
the CPU
.
AMD Ryzen
9
series has several options
.
The latest would be the
7000
series
,
like the Ryzen
9
7950X
.
That's
16
cores
,
which
is
overkill
for
gaming but great
for
multitasking
and
future
-
proofing
.
Some users might prefer the 7900X
if
they want a balance
,
but since the user specified Ryzen
9
,
the top
-
tier model seems suitable
.
Next
,
the GPU
:
RTX
3090.
Wait
,
NVIDIA has newer models like the
40
series
.
The
3090
is
still powerful
,
but I should check
if
the user specifically wants the
3090.
Maybe they have a reason
,
like availability
or
specific use cases
.
So stick
with
the
3090
,
but note that a
4080
or
4090
might offer better performance
.
Also
,
the
3090
has 24GB VRAM
,
which
is
great
for
gaming at high resolutions
or
content creation
.
RAM
:
64GB DDR5
.
That
's a lot for gaming. Most games don'
t need more than 32GB
,
but maybe the user
is
into streaming
,
video editing
,
or
heavy multitasking
.
So need to pick a high
-
speed DDR5
,
like 6000MHz
.
CL latency matters
;
lower CL
is
better
.
Maybe a 6000MHz CL30
or
CL32 kit
.
Also
,
ensure it's AMD EXPO certified
for
Ryzen compatibility
.
Motherboard
:
X670E chipset to support the Ryzen
7000
series
.
Need PCIe
5.0
for
future GPUs
and
NVMe
.
Look
for
good VRM cooling
,
multiple M
.
2
slots
,
and
built
-
in
Wi
-
Fi 6E
if
possible
.
Brands like ASUS
,
MSI
,
or
Gigabyte
.
Storage
:
For gaming
,
NVMe SSD
is
a must
.
A 2TB PCIe
4.0
drive like Samsung
980
Pro
or
WD Black SN850X
.
Maybe a 4TB
if
budget allows
.
Also
,
secondary storage could be a larger SATA SSD
or
HDD
,
but the user might prefer
all
NVMe
for
speed
.
Power Supply
:
RTX
3090
is
power
-
hungry
.
A 850W PSU minimum
,
but 1000W to be safe
,
especially
with
a high
-
end CPU
and
room
for
overclocking
.
80
+
Platinum efficiency
.
Modular
for
cable management
.
Brands like Corsair
,
EVGA
,
or
Seasonic
.
Cooling
:
Ryzen
9
can run hot
.
An AIO liquid cooler
with
360mm radiator would be best
.
Arctic Liquid Freezer II
or
Corsair iCUE H150i
.
Good thermal paste also important
.
Case
:
Needs good airflow
.
Lian Li PC
-
O11 Dynamic
or
Corsair 5000D
.
Make sure it fits the 360mm radiator
and
the GPU length
.
Plenty of fan mounts
for
airflow
.
Extras
:
Maybe RGB
for
aesthetics
,
Windows
11
Pro
,
and
a monitor recommendation
.
If the user
is
using a
3090
,
a 4K 144Hz monitor would pair well
.
Peripherals like mechanical keyboard
and
gaming mouse
.
Wait
,
the user didn't mention a budget
,
but high
-
performance implies top
-
tier parts
.
Check
for
possible bottlenecks
.
64GB RAM might be overkill
,
but the user specified it
.
Maybe note that 32GB
is
enough
for
gaming
,
but 64GB
is
for
other tasks
.
Also
,
ensure DDR5
is
dual
-
channel
and
dual
-
rank
for
optimal performance
.
Double
-
check compatibility
:
CPU socket AM5
for
Ryzen
7000
,
motherboard chipset X670E
,
and
ensure the PSU has enough PCIe connectors
for
the GPU
.
Case dimensions
for
all
components
.
Alternative components
if
certain parts are unavailable
.
Mention possible upgrades like adding more storage later
.
Also
,
highlight the reasoning behind each choice to
help
the user understand the build's balance
.
Make sure the total wattage
is
covered by the PSU
.
RTX
3090
can peak around 450W
,
Ryzen
9
7950X up to 230W
,
other components adding maybe 100W
.
Total around 800W at peak
,
so 1000W PSU gives headroom
for
overclocking
and
efficiency
.
Final check
:
No incompatible parts
,
all
components fit
in
the
case
,
adequate cooling
for
both CPU
and
GPU
,
and
high
-
speed storage
for
quick load times
.
The parsed JSON data
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
Computer Specification
(
JSON Data
)
:
{
"processor"
:
"AMD Ryzen 9 7950X"
,
"memory"
:
"64GB Corsair Dominator Platinum RGB DDR5 6000MHz (CL30)"
,
"storage"
:
"Primary: 2TB Samsung 990 Pro NVMe SSD (PCIe 4.0) | Secondary: 4TB Seagate BarraCuda HDD"
,
"gpu"
:
"NVIDIA GeForce RTX 3090 Founders Edition (24GB GDDR6X)"
,
"motherboard"
:
"ASUS ROG Crosshair X670E Extreme (Wi-Fi 6E, PCIe 5.0)"
,
"cooling"
:
"NZXT Kraken Z73 360mm AIO Liquid Cooler"
,
"networking"
:
"Onboard 10G LAN + Wi-Fi 6E"
,
"ports"
:
"USB4, Thunderbolt 4, 12x USB 3.2 Gen 2"
,
"os"
:
"Windows 11 Pro 64-bit"
}
Additional resources
For more details on using constrained reasoning in Fireworks, check out our documentation on
structured response modes
, where we hope to publish additional examples soon.
Conclusion
To conclude, constrained generation in reasoning models like DeepSeek R1 enables AI to produce structured, interpretable, and machine-readable outputs across a wide range of applications. By enforcing predefined formats through JSON mode, grammar-based constraints, and reasoning-enhanced responses, we can ensure reliability, transparency, and consistency in AI-generated content. Whether it’s structured Q&A, healthcare documentation, or computer system recommendations, this approach not only improves the accuracy of outputs but also enhances their usability in real-world systems. As AI continues to evolve, structured generation techniques will play a crucial role in making model outputs more actionable, verifiable, and seamlessly integrable into existing workflows.
Why Fireworks AI
Fireworks AI
is an enterprise scale LLM inference engine. Today, several AI-enabled developer experiences built on the Fireworks Inference platform are serving millions of developers.
Fireworks lightning fast serving stack enables enterprises to build mission critical Generative AI Applications that are super low latency. With methods like prompt caching, speculative API, we guarantee high throughput performance with low total cost of offering (TCO) in addition to bringing best of the open-source LLMs on the same day of the launch.
If you have more questions,
join our community
and tag a Fireworks AI team member or
drop a note
to discuss building with LLMs from prototype to production.
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
