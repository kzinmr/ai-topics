---
title: "New in Fireworks: Image-to-Image and ControlNet support for SSD-1B and SDXL!"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/new-in-fireworks-image-to-image-and-controlnet-support-for-ssd-1b-and-sdxl"
scraped: "2026-05-10T01:27:12.903859+00:00"
lastmod: "2026-02-12T18:53:23.000Z"
type: "sitemap"
---

# New in Fireworks: Image-to-Image and ControlNet support for SSD-1B and SDXL!

**Source**: [https://fireworks.ai/blog/new-in-fireworks-image-to-image-and-controlnet-support-for-ssd-1b-and-sdxl](https://fireworks.ai/blog/new-in-fireworks-image-to-image-and-controlnet-support-for-ssd-1b-and-sdxl)

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
New In Fireworks Image To Image And Controlnet Support For Ssd 1b And Sdxl
New in Fireworks: Image-to-Image and ControlNet support for SSD-1B and SDXL!
PUBLISHED
11/2/2023
Table of Contents
Blazing-Fast Image Generation
Image-to-Image
ControlNet
Native Resolutions
Safety Checker
Billing
Closing Words
Table of Contents
Table of Contents
Blazing-Fast Image Generation
Image-to-Image
ControlNet
Native Resolutions
Safety Checker
Billing
Closing Words
Table of Contents
The Fireworks.ai blazing-fast inference platform enables developers to build with generative AI to accelerate product innovation.
We are thrilled to announce a set of comprehensive features available through our image generation APIs. These new features will empower generative AI developers to take their image-generation apps to the next level:
•
Blazing-Fast Image Generation
•
Image-to-Image Generation
•
ControlNet Support
•
Native Resolutions
•
Safety Checker
•
Cost-Effective Pricing
Try out the new features in the
Fireworks console
!
Try our
API
!
Blazing-Fast Image Generation
We are excited to introduce Segmind Stable Diffusion 1B (SSD-1B) to the Fireworks.ai inference platform. SSD-1B, released by Segmind, is one of the fastest diffusion-based text-to-image models available today. We are making it accessible to all our users via our fast inference platform with unprecedented image generation performance.
It's now possible to generate 1024x1024 images in 30 steps in just 1 second!
Try out the SSD-1B model in the
Fireworks console
!
Image-to-Image
The Image-to-Image functionality can be used to transform photos with text prompts. To use it, provide an image description, a negative prompt (optional), and an initial image.
Here is a step-by-step example of how to use
SDXL on the console
:
Step 1:
Use the following text prompt: “
Fennec Fox Van Gogh, cartoon, purple, vibrant painting, fantasy concept
”.
Step 2:
Leave “Negative Prompt” empty for now and don't set any LoRA Adapter.
Step 3:
Click on the image-to-image option under “Additional Conditioning” and upload the following image:
Step 4:
Click on the “Generate Image” option. Here are a few generations obtained using the default parameters.
This is a lot of fun! Feel free to play with the console by creating an account, and learn more about image-to-image generation from our
API reference
.
ControlNet
The SSD-1B and SDXL models also now support using ControlNet to generate images using a provided image as guidance.
Let's use the same original image above to guide the generation of the SDXL example above. You can follow the same steps as before but now you set “Additional Conditioning” as “ControlNet” and upload the image. Here are a few of our own generations:
There is still more room for experimenting but you can see that the generated image is now much closer to the original image, all possible with the ControlNet support.
Learn more about ControlNet support for SDXL via our
API reference
.
Native Resolutions
The text-to-image feature now supports nine different resolutions of various aspect ratios: (1024, 1024), (1152, 896), (896, 1152), (1216, 832), (832, 1216), (1344, 768), (768, 1344), (1536, 640), and (640, 1536). In addition, you can also specify the return type to be either
PNG
or
JPEG
.
Safety Checker
It's fun to develop with these image generation models but it's important to also think about safety when developing with generative AI. To address this, we also now support enabling a safety check in the API for content filtering.
Enable
safety_check: true
in the API to run an unsafe content detection network on generated images. Unsafe images are blacked out and a CONTENT_FILTERED finish reason is returned.
To demonstrate how the safety check works, below is a sample code snippet that demonstrates how to use the
Fireworks.ai Python client
to generate images with the safety check enabled. Make sure to include your own
FIREWORKS_API_KEY
and set
safety_check=True
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
# pip install 'fireworks-ai>=0.6.0'
import
fireworks
.
client
from
fireworks
.
client
.
image
import
ImageInference
,
Answer
# Initialize the ImageInference client
fireworks
.
client
.
api_key
=
"<FIREWORKS_API_KEY>"
inference_client
=
ImageInference
(
model
=
"stable-diffusion-xl-1024-v1-0"
)
# Generate an image using the text_to_image method
answer
:
Answer
=
inference_client
.
text_to_image
(
prompt
=
"Fennec Fox Van Gogh, cartoon, purple, vibrant painting, fantasy concept"
,
cfg_scale
=
7
,
height
=
1024
,
width
=
1024
,
sampler
=
None
,
steps
=
25
,
seed
=
0
,
safety_check
=
True
,
# Add additional parameters here as necessary
)
if
answer
.
image
is
None
:
raise
RuntimeError
(
f"No return image,
{
answer
.
finish_reason
}
"
)
else
:
answer
.
image
.
save
(
"output.png"
)
Try out the features in the
Fireworks console
!
Try our
API
!
Billing
We've also introduced our
competitive cost-effective pricing
for using the image-generation models. Check it out and hit us up with any questions.
Closing Words
We're amped to see how developers use these new features to accelerate product innovation and creative applications with the advanced image-generation capabilities of SSD-1B and SDXL on the Fireworks inference platform.
🗣 Join our community on
Discord
.
🎆 Learn more about the
Fireworks Generative AI platform
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
