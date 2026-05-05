---
title: "Not so unique GUID"
url: "https://boyter.org/2014/05/unique-guid/"
fetched_at: 2026-05-05T07:02:03.469146+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Not so unique GUID

Source: https://boyter.org/2014/05/unique-guid/

I have been doing a lot of work with the Sitecore CMS recently. Once of the things you quickly learn is how it relies on GUID’s for pretty much everything. This means of course when you start testing and need to supply GUID’s into your tests that you end up with lots of GUIDs that look like the following sprinkled through your code {11111111-1111-1111-1111-111111111111}
Today I remarked that we should be using things like “deadbeef” for the first part of the GUID with a colleague. He suggested that we should try and actually write something. With a little bit of 1337 speak this is actually possible. Naturally we got back to work, but with a little free time I quickly coded up a simple Python application to generate “phrased” GUID’s. Some examples follow,
silicles-oafs-blob-tael-declassified -> {5111c1e5-0af5-b10b-7ae1-dec1a551f1ed}
deedless-gait-soft-goes-eisteddfodic -> {deed1e55-9a17-50f7-90e5-e157eddf0d1c}
libelist-diel-alls-flit-disaffiliate -> {11be1157-d1e1-a115-f117-d15aff111a7e}
offstage-diel-labs-scat-classifiable -> {0ff57a9e-d1e1-1ab5-5ca7-c1a551f1ab1e}
None of the above are make much sense, but by looking at the outputs you can attempt to write something such as,
cassette soft gold dice collectibles
{ca55e77e-50f7-901d-d1ce-c011ec71b1e5}
Very zen. Some rough back of napkin calculations gives my program something like 10,000,000,000,000 combinations of GUID’s based on the word list I supplied. I may just turn it into a online GUID generator like this one
http://www.guidgenerator.com/
or you can get it via this gist
https://gist.github.com/boyter/6f5b7c1b375e79449d01916f5828e1db
