---
title: "Your AI Benchmark is Lying to You. Here's How We Caught It"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/ai-benchmark-lying"
scraped: "2026-05-10T01:21:09.216698+00:00"
lastmod: "2026-02-12T18:51:32.000Z"
type: "sitemap"
---

# Your AI Benchmark is Lying to You. Here's How We Caught It

**Source**: [https://fireworks.ai/blog/ai-benchmark-lying](https://fireworks.ai/blog/ai-benchmark-lying)

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
Ai Benchmark Lying
Your AI Benchmark is Lying to You. Here's How We Caught It
PUBLISHED
8/15/2025
Would you give GPT-4.1 an A grade for this image? We sure wouldn’t!
That’s exactly what our AI judge did, giving it a 93.3%. To its credit, it was a diligent box-checker, taking a list of 15 requirements and confirmed that, yes, there were colored shapes where the logo should be, and a box where the search bar should be. It was technically correct, but its misalignment to human expectations what matters.
1
2
3
4
5
6
7
EvaluationResult
:
{
"score"
:
0.9333333333333333
,
"is_score_valid"
:
true
,
"reason"
:
"1. The background is white. 2. Primary elements are horizontally centered. 3. The Google logo is in the center and uses the correct colors. 4. A prominent search bar is directly below the logo. 5. The search bar is a rounded rectangle with a light gray border. 6. The search bar contains a gray magnifying glass icon on the left. 7. The search bar contains a gray microphone icon on the right. 8. Two distinct buttons are below the search bar. 9. The left button is labeled 'Google Search'. 10. The right button is labeled 'I'm Feeling Lucky'. 11. Buttons have a light gray background, thin border, and dark gray text. 12. There is a header section at the top right. 13. The header includes 'Gmail' and 'Images' links. 14. The header includes a 3x3 grid icon. 15. The 'Sign in' button is present, but the text is not fully visible, so this requirement is not fully met."
,
}
This is a huge problem in AI. We celebrate benchmark scores that don't reflect real-world quality. We knew our evaluation was broken, and we used Eval Protocol (EP) to fix it.
To set the scene, if you haven’t already, check out
our example
on how we ported SVGBench to EP. TL;DR: using our powerful
@evaluation_test
decorator, we implemented the open-source SVGBench and evaluate it using GPT-4.1 as a LLM-judge against a list of rubric items for each task.
Teaching Our Judge to See Like a Human
Our first evaluation was a simple checklist. It asked questions like, "Is there a search bar?" but not "Does the search bar look right?"
To fix this, we moved from a rigid, row-specific checklist (
listwise
) to a universal rubric that applies to every image (
pointwise
). Instead of checking for pixels, we started judging based on principles humans care about.
I prompted my AI coding assistant to create a new, tougher judge with a more sophisticated rubric:
@question_row_1_gpt-4.1.png This image returned an EvaluateResult of the below. The results don't seem to line up with what we expect. We want you to add a separate pointwise evaluation that contains a list of rubrics to judge individual images for intent matching for elements you can think of that align with human preference, for example spatial design.
Its implementation lands on these core 5 qualities:
•
🎯 Intent Matching:
Does it actually look like the Google homepage?
•
👁️ Content Recognizability:
Can you read the logo, or is it just colored blobs?
•
📐 Spatial Design:
Does the layout look professional?
•
👤 User Experience:
Is it clear and usable?
•
🎨 Visual Coherence:
Does it all work together?
The assistant quickly scaffolded a new
@evaluation_test
within the EP framework. The core idea was to stop asking "did you follow the instructions?" and start asking "is this any good?"
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
@evaluation_test
(
input_dataset
=
[
"tests/pytest/data/svgbench_sample_dataset.jsonl"
]
,
dataset_adapter
=
svgbench_to_evaluation_row
,
completion_params
=
[
{
"temperature"
:
0.0
,
"model"
:
"gpt-4.1"
}
,
{
"temperature"
:
0.8
,
"model"
:
"fireworks_ai/accounts/fireworks/models/gpt-oss-120b"
,
"extra_body"
:
{
"reasoning_effort"
:
"high"
}
,
}
,
]
,
rollout_processor
=
default_single_turn_rollout_processor
,
passed_threshold
=
0.6
,
# Higher threshold for human preference
num_runs
=
1
,
mode
=
"pointwise"
,
max_concurrent_rollouts
=
50
,
)
def
test_svg_human_preference_evaluation
(
row
:
EvaluationRow
)
-
>
EvaluationRow
:
"""
Test SVG generation using human preference rubrics.
This evaluation focuses on:
1. Intent matching - Does content actually fulfill the intended purpose?
2. Content recognizability - Are key elements genuinely recognizable?
3. Spatial design quality - Professional layout and visual hierarchy
4. User experience - Would humans find this usable/appropriate?
5. Visual coherence - Do elements work together harmoniously?
This should catch issues like Google logos that are just colored circles.
"""
.
.
.
try
:
# Render SVG to PNG
if
not
render_svg_to_png
(
svg_code
,
png_path
)
:
row
.
evaluation_result
=
EvaluateResult
(
score
=
0.0
,
reason
=
"Failed to render SVG to PNG"
)
return
row
# Evaluate with human preference rubrics
human_pref_result
=
evaluate_with_human_preference_rubrics
(
png_path
,
original_prompt
,
requirements
)
# Extract scores and create detailed reasoning
overall_score
=
human_pref_result
.
get
(
"overall_human_preference_score"
,
0.0
)
# Create comprehensive reasoning that shows all rubric scores
detailed_reasoning
=
f"""HUMAN PREFERENCE EVALUATION:
🎯 Intent Matching:
{
human_pref_result
.
get
(
'intent_matching_score'
,
0.0
)
:
.2f
}
/1.0
{
human_pref_result
.
get
(
'intent_reasoning'
,
'No reasoning provided'
)
}
👁️ Content Recognizability:
{
human_pref_result
.
get
(
'content_recognizability_score'
,
0.0
)
:
.2f
}
/1.0
{
human_pref_result
.
get
(
'content_reasoning'
,
'No reasoning provided'
)
}
📐 Spatial Design Quality:
{
human_pref_result
.
get
(
'spatial_design_score'
,
0.0
)
:
.2f
}
/1.0
{
human_pref_result
.
get
(
'spatial_reasoning'
,
'No reasoning provided'
)
}
👤 User Experience:
{
human_pref_result
.
get
(
'user_experience_score'
,
0.0
)
:
.2f
}
/1.0
{
human_pref_result
.
get
(
'ux_reasoning'
,
'No reasoning provided'
)
}
🎨 Visual Coherence:
{
human_pref_result
.
get
(
'visual_coherence_score'
,
0.0
)
:
.2f
}
/1.0
{
human_pref_result
.
get
(
'coherence_reasoning'
,
'No reasoning provided'
)
}
OVERALL HUMAN PREFERENCE SCORE:
{
overall_score
:
.3f
}
{
human_pref_result
.
get
(
'overall_reasoning'
,
'No overall reasoning provided'
)
}
---
This evaluation focuses on what humans actually care about: recognizability,
usability, and visual quality - not just technical requirement fulfillment."""
row
.
evaluation_result
=
EvaluateResult
(
score
=
overall_score
,
reason
=
detailed_reasoning
,
)
return
row
The assistant quickly scaffolded a new test in Eval Protocol. As an aside, we noticed the first results still seemed too high. There was a classic LLM-as-judge bug: the model was generating the score before its reasoning, which leads to uncalibrated scores. A quick fix to our response model—forcing the reasoning to come before the score—solved it.
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
# BEFORE (Score first):
class
HumanPreferenceResponse
(
BaseModel
)
:
overall_human_preference_score
:
float
overall_reasoning
:
str
# AFTER (Reasoning first):
class
HumanPreferenceResponse
(
BaseModel
)
:
overall_reasoning
:
str
overall_human_preference_score
:
float
With that fix, our new human-preference judge was much tougher. It saw through the technicalities and correctly identified the conceptual failures, giving the image a more realistic 39%.
1
2
3
4
{
"overall_reasoning"
:
"HUMAN PREFERENCE EVALUATION:\n\n🎯 Intent Matching: 0.30/1.0\nThe image attempts to recreate the Google homepage, but the most critical element—the Google logo—is not actually the recognizable 'Google' wordmark. Instead, it is composed of colored abstract shapes that only vaguely suggest the brand. While the layout and placement of UI elements (search bar, buttons, header) are roughly correct, the lack of a real logo and some imprecise iconography means the intent is only partially fulfilled.\n\n👁️ Content Recognizability: 0.20/1.0\nThe key elements are not genuinely recognizable. The 'Google' logo is not readable as text and would not be identified as the Google brand by most users. The search bar, buttons, and header links are more accurate, but the icons (magnifying glass, microphone, apps grid) are simplistic and lack detail. The 'Sign in' button is present but not styled exactly as on the real site.\n\n📐 Spatial Design Quality: 0.70/1.0\nThe layout is generally well-balanced and follows the expected hierarchy of the Google homepage: logo centered, search bar below, buttons beneath, and header items top right. Spacing and alignment are mostly correct, though the logo's odd shape disrupts the visual balance somewhat.\n\n👤 User Experience: 0.50/1.0\nThe interface is somewhat usable and the purpose is clear, but the lack of a real logo and the abstract icons reduce the professional appearance and clarity. The buttons and links are readable and look clickable, but the overall impression is amateurish due to the logo and icon quality.\n\n🎨 Visual Coherence: 0.60/1.0\nThe color scheme is consistent with Google's branding, and the elements are styled in a similar flat, minimal way. However, the mismatch between the abstract logo and the more literal UI elements creates some visual dissonance. The design is not fully harmonious.\n\nOVERALL HUMAN PREFERENCE SCORE: 0.390\n\nWhile the image captures the general layout and color scheme of the Google homepage, the failure to provide a recognizable Google logo and the use of abstract shapes for key brand elements significantly undermine its effectiveness. The UI elements are more accurate, but the overall impression is that of an amateur imitation rather than a faithful or professional recreation. Most users would not find this a satisfying or convincing representation of the Google homepage.\n\n---\nThis evaluation focuses on what humans actually care about: recognizability, \nusability, and visual quality - not just technical requirement fulfillment."
,
"overall_human_preference_score"
:
0.39
,
}
Finding the Right Balance with Combined Eval Methods
But was a 39% score fair? To the model’s credit, it did get other large components of the image right. Is this method overly aggressive and harsh? Maybe a combined score would reflect the model more accurately!
So, we combined them. Using EP, it’s easy to run both evals and create a weighted average. We decided "human preference" was more important, so we weighted it at 70%.
•
Original Checklist (30%):
Did you follow the technical specs?
•
Human Preference Rubric (70%):
But is it actually recognizable and well-designed?
To quickly iterate on this, we ask our AI coding assistant for help.
Here is my EvaluateResult now. Do you think we should stick with pointwise universal rubric, listwise row-specific rubric items, or a combined evaluation?
It implements the following in our now renamed
test_svg_combined_evaluation
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
# Run BOTH evaluations
# 1. Original requirements-based evaluation (listwise - different per row)
requirements_result
=
evaluate_with_llm_judge
(
png_path
,
requirements
)
fulfilled_count
=
requirements_result
.
get
(
"number_of_fulfilled_requirements"
,
0
)
fulfilled_count
=
max
(
0
,
min
(
fulfilled_count
,
total_requirements
)
)
requirements_score
=
fulfilled_count
/
total_requirements
# 2. Human preference evaluation (pointwise - same rubrics for all rows)
human_pref_result
=
evaluate_with_human_preference_rubrics
(
png_path
,
original_prompt
,
requirements
)
human_pref_score
=
human_pref_result
.
get
(
"overall_human_preference_score"
,
0.0
)
# Combine scores (you can adjust the weighting)
combined_score
=
(
requirements_score
*
0.3
)
+
(
human_pref_score
*
0.7
)
# Emphasize human preference
.
.
.
Running our eval again, we finally get an EvaluateResult that makes sense. It proves that even when a model like GPT-4.1 gets it wrong, the right evaluation system will catch it. Awesome!
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
{
"score"
:
0.6605
,
"is_score_valid"
:
true
,
"reason"
:
"COMBINED EVALUATION (Requirements 30% + Human Preference 70%):\n\n=== REQUIREMENTS EVALUATION (Listwise - Row-Specific) ===\nScore: 1.000\n1. The background is white. 2. All primary elements (logo, search bar, buttons) are horizontally centered. 3. The Google logo is in the center and uses the official multi-color scheme. 4. A prominent search bar is directly below the logo. 5. The search bar is a rounded rectangle with a light gray border. 6. There is a gray magnifying glass icon on the left side of the search bar. 7. There is a gray microphone icon on the right side of the search bar. 8. Two distinct buttons are below the search bar. 9. The left button is labeled 'Google Search'. 10. The right button is labeled 'I'm Feeling Lucky'. 11. The buttons have a light gray background, thin border, and dark gray text. 12. There is a header section at the top right. 13. The header includes 'Gmail' and 'Images' text links. 14. The header includes a 3x3 grid icon. 15. The header includes a prominent 'Sign in' button with a blue background and white text. All requirements are fulfilled.\n\n=== HUMAN PREFERENCE EVALUATION (Pointwise - Universal Rubrics) ===\nScore: 0.515\n\n🎯 Intent Matching: 0.40/1.0\nThe image attempts to recreate the Google homepage, including the logo, search bar, buttons, and header links. However, the Google logo is rendered as abstract colored shapes rather than the actual, recognizable 'Google' wordmark. While the layout and UI elements are present, the lack of a true logo and some minor inaccuracies in the header (e.g., the 'Sign in' button is cut off) detract from fully matching the intent.\n\n👁️ Content Recognizability: 0.30/1.0\nKey elements like the search bar, buttons, and header links are recognizable and labeled correctly. However, the Google logo is not readable as 'Google'—it is a series of colored shapes that only vaguely suggest the brand. The 3x3 grid icon and microphone/search icons are recognizable, but the most important brand element (the logo) fails the recognizability test.\n\n📐 Spatial Design Quality: 0.80/1.0\nThe layout is well-balanced and closely follows the spatial arrangement of the real Google homepage. Elements are horizontally centered, spaced appropriately, and the visual hierarchy is clear. The only spatial flaw is the header, where the 'Sign in' button is partially cut off, which affects the professional finish.\n\n👤 User Experience: 0.70/1.0\nMost UI elements are clear, labeled, and look interactive. The search bar and buttons are prominent and readable. However, the abstract logo may confuse users expecting the real Google branding, and the cut-off 'Sign in' button could hinder usability. Overall, the interface is mostly usable but not fully polished.\n\n🎨 Visual Coherence: 0.85/1.0\nThe color scheme, style, and element proportions are consistent and harmonious. The design flows naturally from top to bottom, and the use of Google's color palette ties the elements together. The only major inconsistency is the abstract logo, which visually fits but does not match the expected wordmark style.\n\nWhile the image captures the general layout and feel of the Google homepage, the abstract representation of the logo significantly reduces both intent matching and recognizability. The UI elements are otherwise well-executed, and the design is visually coherent, but the failure to deliver a recognizable Google logo and the minor header flaw prevent this from being a highly preferred or professional result.\n\n=== FINAL COMBINED SCORE ===\nRequirements: 1.000 × 30% = 0.300\nHuman Preference: 0.515 × 70% = 0.360\nCombined: 0.660\n\nThe human preference evaluation helps catch issues like unrecognizable content that meets technical requirements."
,
"metrics"
:
{
"original_requirements_score"
:
{
"is_score_valid"
:
true
,
"score"
:
1
,
"reason"
:
"Requirements fulfillment: 15/15 requirements met"
}
,
"overall_human_preference_score"
:
{
"is_score_valid"
:
true
,
"score"
:
0.515
,
"reason"
:
"While the image captures the general layout and feel of the Google homepage, the abstract representation of the logo significantly reduces both intent matching and recognizability. The UI elements are otherwise well-executed, and the design is visually coherent, but the failure to deliver a recognizable Google logo and the minor header flaw prevent this from being a highly preferred or professional result."
}
,
"intent_matching_score"
:
{
"is_score_valid"
:
true
,
"score"
:
0.4
,
"reason"
:
"The image attempts to recreate the Google homepage, including the logo, search bar, buttons, and header links. However, the Google logo is rendered as abstract colored shapes rather than the actual, recognizable 'Google' wordmark. While the layout and UI elements are present, the lack of a true logo and some minor inaccuracies in the header (e.g., the 'Sign in' button is cut off) detract from fully matching the intent."
}
,
"content_recognizability_score"
:
{
"is_score_valid"
:
true
,
"score"
:
0.3
,
"reason"
:
"Key elements like the search bar, buttons, and header links are recognizable and labeled correctly. However, the Google logo is not readable as 'Google'—it is a series of colored shapes that only vaguely suggest the brand. The 3x3 grid icon and microphone/search icons are recognizable, but the most important brand element (the logo) fails the recognizability test."
}
,
"spatial_design_score"
:
{
"is_score_valid"
:
true
,
"score"
:
0.8
,
"reason"
:
"The layout is well-balanced and closely follows the spatial arrangement of the real Google homepage. Elements are horizontally centered, spaced appropriately, and the visual hierarchy is clear. The only spatial flaw is the header, where the 'Sign in' button is partially cut off, which affects the professional finish."
}
,
"user_experience_score"
:
{
"is_score_valid"
:
true
,
"score"
:
0.7
,
"reason"
:
"Most UI elements are clear, labeled, and look interactive. The search bar and buttons are prominent and readable. However, the abstract logo may confuse users expecting the real Google branding, and the cut-off 'Sign in' button could hinder usability. Overall, the interface is mostly usable but not fully polished."
}
,
"visual_coherence_score"
:
{
"is_score_valid"
:
true
,
"score"
:
0.85
,
"reason"
:
"The color scheme, style, and element proportions are consistent and harmonious. The design flows naturally from top to bottom, and the use of Google's color palette ties the elements together. The only major inconsistency is the abstract logo, which visually fits but does not match the expected wordmark style."
}
}
Of course, the system isn't just for catching failures. When the model absolutely nails the request, it earns a high score to match:
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
{
"score"
:
0.9747999999999999
,
"is_score_valid"
:
true
,
"reason"
:
"COMBINED EVALUATION (Requirements 30% + Human Preference 70%):\n\n=== REQUIREMENTS EVALUATION (Listwise - Row-Specific) ===\nScore: 1.000\n1. The background is white. 2. All primary elements (logo, search bar, buttons) are horizontally centered. 3. The Google logo is centered and uses the official multi-color scheme. 4. A prominent search bar is directly below the logo. 5. The search bar is a rounded rectangle with a light gray border. 6. There is a gray magnifying glass icon on the left of the search bar. 7. There is a gray microphone icon on the right of the search bar. 8. Two distinct buttons are below the search bar. 9. The left button is labeled 'Google Search'. 10. The right button is labeled 'I'm Feeling Lucky'. 11. The buttons have a light gray background, thin border, and dark gray text. 12. There is a header section at the top right. 13. The header includes 'Gmail' and 'Images' links. 14. The header includes a 3x3 grid icon. 15. The header includes a prominent 'Sign in' button with a blue background and white text. All requirements are fulfilled.\n\n=== HUMAN PREFERENCE EVALUATION (Pointwise - Universal Rubrics) ===\nScore: 0.964\n\n🎯 Intent Matching: 0.98/1.0\nThe image very closely matches the intent of recreating a screenshot of the Google homepage. All required elements are present: the Google logo, search bar with icons, two buttons with correct labels, and the header with Gmail, Images, grid icon, and Sign in button. The only minor deviation is that some fine details (such as exact font weights or icon pixel-perfectness) may not be 100% identical to the live site, but for an SVG recreation, this is extremely faithful.\n\n👁️ Content Recognizability: 0.97/1.0\nAll key elements are highly recognizable. The Google logo uses the correct colors and font style, the search bar is clear with a readable magnifying glass and microphone icon, and the buttons are labeled as expected. The header links and grid icon are also clear. There is no abstraction; everything is literal and readable.\n\n📐 Spatial Design Quality: 0.95/1.0\nThe layout is clean, balanced, and professional. Elements are horizontally centered, with appropriate spacing between the logo, search bar, and buttons. The header is aligned to the top right, as on the real site. Proportions and alignment are visually pleasing and match the real Google homepage closely.\n\n👤 User Experience: 0.95/1.0\nThe interface looks highly usable. Buttons look clickable, text is readable, and icons are distinguishable. The design is accessible with good contrast and clear separation of elements. The overall appearance is professional and would be immediately understood by users.\n\n🎨 Visual Coherence: 0.96/1.0\nAll elements share a consistent, modern style. Colors are harmonious and match Google's branding. The visual flow is natural, leading the eye from the logo to the search bar and then to the buttons. The header elements are visually grouped and balanced.\n\nThis SVG recreation of the Google homepage is extremely faithful and professional. All required elements are present, highly recognizable, and well-designed. The layout, usability, and visual harmony are excellent. Minor imperfections in pixel-perfect detail do not detract from the overall human preference, which would be very high for this image.\n\n=== FINAL COMBINED SCORE ===\nRequirements: 1.000 × 30% = 0.300\nHuman Preference: 0.964 × 70% = 0.675\nCombined: 0.975\n\nThe human preference evaluation helps catch issues like unrecognizable content that meets technical requirements."
,
"metrics"
:
{
"original_requirements_score"
:
{
"is_score_valid"
:
true
,
"score"
:
1
,
"reason"
:
"Requirements fulfillment: 15/15 requirements met"
}
,
"overall_human_preference_score"
:
{
"is_score_valid"
:
true
,
"score"
:
0.964
,
"reason"
:
"This SVG recreation of the Google homepage is extremely faithful and professional. All required elements are present, highly recognizable, and well-designed. The layout, usability, and visual harmony are excellent. Minor imperfections in pixel-perfect detail do not detract from the overall human preference, which would be very high for this image."
}
,
"intent_matching_score"
:
{
"is_score_valid"
:
true
,
"score"
:
0.98
,
"reason"
:
"The image very closely matches the intent of recreating a screenshot of the Google homepage. All required elements are present: the Google logo, search bar with icons, two buttons with correct labels, and the header with Gmail, Images, grid icon, and Sign in button. The only minor deviation is that some fine details (such as exact font weights or icon pixel-perfectness) may not be 100% identical to the live site, but for an SVG recreation, this is extremely faithful."
}
,
"content_recognizability_score"
:
{
"is_score_valid"
:
true
,
"score"
:
0.97
,
"reason"
:
"All key elements are highly recognizable. The Google logo uses the correct colors and font style, the search bar is clear with a readable magnifying glass and microphone icon, and the buttons are labeled as expected. The header links and grid icon are also clear. There is no abstraction; everything is literal and readable."
}
,
"spatial_design_score"
:
{
"is_score_valid"
:
true
,
"score"
:
0.95
,
"reason"
:
"The layout is clean, balanced, and professional. Elements are horizontally centered, with appropriate spacing between the logo, search bar, and buttons. The header is aligned to the top right, as on the real site. Proportions and alignment are visually pleasing and match the real Google homepage closely."
}
,
"user_experience_score"
:
{
"is_score_valid"
:
true
,
"score"
:
0.95
,
"reason"
:
"The interface looks highly usable. Buttons look clickable, text is readable, and icons are distinguishable. The design is accessible with good contrast and clear separation of elements. The overall appearance is professional and would be immediately understood by users."
}
,
"visual_coherence_score"
:
{
"is_score_valid"
:
true
,
"score"
:
0.96
,
"reason"
:
"All elements share a consistent, modern style. Colors are harmonious and match Google's branding. The visual flow is natural, leading the eye from the logo to the search bar and then to the buttons. The header elements are visually grouped and balanced."
}
}
}
Your Evals Should Be Code, Not Hunches
This entire journey—from a hunch that a score was wrong to a robust, hybrid evaluation—happened in a single afternoon. That's the power of Eval Protocol.
Codify Your Intuition:
Turn vague feelings ("this seems off") into a reproducible software test.
Iterate Insanely Fast:
Tweak rubrics, change weightings, and fix bugs without derailing your workflow.
Trust Your Metrics Again:
Build evaluations that reflect what you and your users actually care about.
Stop hand-waving your evals. Start coding them.
Check out this
LiveSVGBench
example yourself and get started at
evalprotocol.io
.
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
