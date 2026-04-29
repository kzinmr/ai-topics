---
title: "Untitled"
url: "https://matduggan.com/fyi-broadcom-is-ruining-bitnami-containers/"
fetched_at: 2026-04-29T07:01:55.034019+00:00
source: "matduggan.com"
tags: [blog, raw]
---

# Untitled

Source: https://matduggan.com/fyi-broadcom-is-ruining-bitnami-containers/

For a long time Bitnami containers and Helm charts have been widely considered the easiest and fastest way to get reliable, latest versions of popular applications built following container best practices. They also have some of the better docs on the internet for figuring out how to configure all this stuff.
However Broadcom, in their infinite capacity for short term gain over long term relationships, has decided to bring that to a close. On July 16th they informed their users that the platform was changing. Originally they were going to break a ton of workflows with only 43 days warning, but have expanded that out to a generous 75 days.
It's impossible to read these timelines as anything other than Broadcom knows that enterprise customers won't be able to switch off in 43 or 75 days and is using this to extort people into paying them the rumored $50,000 a year to keep using the images.
You can read the entire announcement here:
https://github.com/bitnami/containers/issues/83267
Here is my summary though:
TL;DR:
Bitnami is significantly reducing their free container image offerings and moving most existing images to a legacy repository with no future updates.
What's Changing:
Free Community Tier (Severely Limited):
Only a small subset of hardened images will remain free
Available only with "latest" tags (no version pinning)
Intended for development use only
Find the limited selection at:
https://hub.docker.com/u/bitnamisecure
Your Existing Images:
All current Bitnami images (including versioned tags) move to
docker.io/bitnamilegacy
No updates, patches, or support
for legacy images
Use legacy repo only as temporary migration solution
Production Users:
Need to subscribe to "Bitnami Secure Images" for continued support
Includes security patches, LTS branches, and full version catalog
Action Items for DevOps Teams:
Before September 29th:
Audit your deployments
- Check which Bitnami images you're using
Update CI/CD pipelines
- Remove dependencies on deprecated images
Choose your path:
Development only:
Migrate to the limited free tier (latest tags only)
Production:
Subscribe to Bitnami Secure Images or find alternatives
Temporary fix:
Update image references to
bitnamilegacy/
(not recommended long-term)
Helm Charts:
Source code remains open source on GitHub
Existing OCI charts at
docker.io/bitnamicharts
won't receive updates
Charts will fail unless you override image repositories
Bottom Line:
If you're using Bitnami for anything beyond basic development with latest tags, you'll need to either pay for Bitnami Secure Images or migrate to alternative container images before September 29th.
