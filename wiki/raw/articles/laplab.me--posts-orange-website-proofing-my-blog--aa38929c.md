---
title: "Orange-Website-Proofing My Blog"
url: "https://laplab.me/posts/orange-website-proofing-my-blog/"
fetched_at: 2026-05-05T07:01:24.403799+00:00
source: "Nikita Lapkov (laplab)"
tags: [blog, raw]
---

# Orange-Website-Proofing My Blog

Source: https://laplab.me/posts/orange-website-proofing-my-blog/

Discussion on
HackerNews
and
Lobsters
.
Over the course of one year this website is deployed, I did not pay a penny for hosting it. Sure, I pay for renting the domain itself, but everything else is free and quite honestly I like it this way. So when I woke up to a 10$ bill from DigitalOcean, I immediately knew something was amiss.
Orange Website
Last month I wrote
an article
that reached the front page of HackerNews. This happened before, but this specific article included a couple of high-res photos and I made a mistake of not checking their size before uploading. There were 4 images in total, each roughly 2MB in size. With all the page visits from the Orange Website, this resulted in
82.76GB
of bandwidth spent. Lazy loading would have reduced this number by a factor, but it was still much more than I expected.
Note that this shows only visits from users without adblocker.
Previously, this website was hosted on DigitalOcean as a Hugo App. It provides you with a nice Github integration, which automatically builds and publishes content on commits to the main branch. On top of that, you have 1GB of free bandwidth, which was just enough until the article with these 4 blasted images was published. Any extra bandwidth goes with a price tag of 0.10$/GB, causing my bills to be an annoyingly non-zero number. With 81GB it was kind of okay, but I am uncomfortable with the idea that it can get out of hand this quickly.
Update from May 2025:
I disabled Github integration and just upload website bundle directly using
wrangler
tool. Using a reproducible CI for deploying a static website seems like an absolute overkill and needless spending of resources. It’s also way faster to just build everything locally thanks to caches from Hugo.
Time to rewrite everything
No!
Phew, that was a close one. I am fighting the urge to write a custom server for my blog for almost 6 months now. Going strong! We will not waste time on writing anything and then spend hours maintaining it if the problem can be solved using some service.
Update from May 2025:
Turns out Hugo can automatically convert all images to WebP format if you override
render-image.html
. I did that and the final bundle of my website went from 44MB to 7.6MB, which is almost a 6x reduction in size. I also added lazy loading for images.
Switching gears
Since the pricing model of DigitalOcean did not really suite me, I decided to change my hosting provider. I opted to go with CloudFlare, since their Pages product provided unlimited bandwidth on the Free plan. I am sure there are many other options to choose from and I am not saying that CloudFlare Pages is necessarily the best one. It is just the one I decided to go with.
This is actually quite funny, because I noticed that when my blog was hosted on DigitalOcean, it automatically applied CloudFlare Scraping Protection to hide my email on the main page. Since this indicates that DigitalOcean is using CloudFlare at least to some extent, I wonder if anything actually changed from the technical standpoint. Did I just change the way my content is delivered to CloudFlare edge servers? Who knows.
Double-layered CloudFlare
I think that I have accidentially created two levels of CDN for my website. And it seems that there is no way around it.
The first layer is the CloudFlare Pages. The website gets deployed to a geographically distributed set of edge servers called CloudFlare CDN/Cache. Pages is actually a very confusingly documented product, since the docs mainly focus on their serverless solution. Still, that is at least what is said on their marketing page.
The second layer is CloudFlare DNS. In order to add a custom domain to the Pages, you need to bring it under the umbrella of CloudFlare DNS. This was desirable for me, since I wanted to get Scraping Protection and similar features anyway. However, at least judging from the admin UI, CloudFlare does not seem to differentiate between a server from Pages product and any other origin server. So it does at least some amount of caching of content at this layer as well (there is even a button to purge this cache) - which seems redundant because I think that the CloudFlare CDN already does it under the hood.
In any case, this is a speculation, maybe they handle it somehow on their side and just do not communicate it properly to the user. Worst case scenario, caches for my website will take a bit longer time to propagate through all the layers - that is fine by me.
The only thing that I was concerned with when changing the nameservers to the CloudFlare ones was the email redirect feature I used when I had nameservers from Namecheap. Turns out CloudFlare has it as well, so it was a smooth migration.
Analytics
Since I am changing the whole infrastructure behind the website, I thought that I might as well rethink my analytics. Previously, I used
Nullitics
, which is a privacy-respecting open-source analytics system. I was lucky to be one of the first 100 people to get the lifetime license for the price of just 10$, which is a good value. While Nullitics is a great service to do some basic tracking, it seems to have stopped in development and was not very customizable. I was passively looking to switch to some other provider.
During migration to CloudFlare, it suggested to use their Web Analytics product. I did not really like the level of detail it was providing, so I decided it was not worth it. Roughly at the same time, I noticed that
fasterthanli.me
uses
GoatCounter
- again, open-source, privacy-focused, all the good stuff, but at the same time it was much more customizable (UI layout, what data to collect, etc). I tried it out, decided that it was my kind of jam and switched to it.
Update from Apr 2025:
I removed tracking/analytics from my website because I don’t need it.
Conclusion
And that’s about it! I hope this setup will work reliably and will not produce any more surprise bills. Time will show :)
