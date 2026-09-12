---
source_url: https://www.autom.dev/blog/google-search-goto-links
ingested: 2026-09-12
sha256: 5f867b57e2eb4d1ec786aa9368cf0efbb77a6ae3177cda67edbb31c3a702b5fc
---

google.com/goto: Google's anti-scraping update Features Pricing Documentation Blog Login Sign up Home Blog google.com/goto: Google's anti-scraping update Published August 27, 2026 Category Google Authors Autom Team Share X.com Ready to scrape? Start scraping with Autom today and discover the power of our API. Start for free Google August 27, 2026 | by Autom Team google.com/goto: Google's anti-scraping update What's happening 
 Google Search is rewriting organic result links to google.com/goto?url=... instead of exposing the destination URL directly in the HTML. 
 When you click a result, Google redirects you to the real page. The url parameter uses a custom, Google-specific encoding. It is not a plain base64 of the target URL. In practice, it looks like an opaque reference to Google's index record for that page. 
 As of late August 2026, this is showing up consistently across searches when you are logged out or browsing in private mode. It may still be an experiment, but it is no longer limited to a small slice of SERPs. 
 Not the same as google.com/url 
 Google has used redirect wrappers before. The older format is google.com/url?q=[URL-encoded destination] , where the target link is readable in the query string. 
 The new goto format is different: 

 The result href is /goto , not the destination 
 You cannot decode the url= blob offline 
 The real URL is in the Location header on /goto . Request that URL. Do not follow the redirect. 

 Google still needs the destination to draw the SERP (domain, favicon, attribution), so copies of the URL remain on the page. That is a separate story from reading Location . The walkthrough is here: google.com/goto: read Location with HEAD . 
 That shift matters for anyone building a search index from SERP data at scale. 
 Why Google is doing this 
 This fits Google's broader push against automated SERP harvesting, especially from AI crawlers and SEO scrapers that bulk-extract result URLs to build their own indexes. 
 With plaintext links, a scraper could parse thousands of URLs from HTML without touching Google again. With goto , each result needs a request back to Google just to learn the destination. You read Location ; you do not follow through to the page. That is slower, noisier, and gives Google a clear signal when the same client resolves hundreds of links in sequence. 
 Combined with earlier moves like removing &num=100 and tightening BotGuard/SearchGuard, Google is steadily raising the cost of naive SERP scraping. 
 What we saw at Autom 
 We first spotted goto links on a small percentage of SERPs. At that level, it was hard to ship a reliable fix without breaking responses for everyone else. 
 As of late August 2026, the pattern is much more consistent for logged-out and private sessions. Result URLs on Google Search are effectively all goto in those conditions. 
 We have been monitoring the rollout and testing against it. 
 Update at Autom.dev 
 We have updated our Google Search pipeline to resolve google.com/goto links (read Location , no follow) and return the final destination URL in API responses, in the same structured fields customers already use. 
 If you call Autom's Google Search endpoints, you should keep getting usable destination URLs without changing your integration. We will keep watching Google's rollout and adjust if the redirect format shifts again. 
 Related reading 

 google.com/goto: read Location with HEAD 
 Google killed num=100 
 Google sues SerpAPI: What SearchGuard reveals 
 Scraping SERP with Google, Bing, and Brave 

 Need live SERP data while Google keeps moving the goalposts? Try 1,000 free requests on Autom pricing , or get an API key at app.autom.dev/register . Read also Google Building an Automation To Build Title & Description for Your Keyword Autom Team | Jan 15, 2026 Google Scrape Google Images using Python Autom Team | Feb 5, 2026 Sales 7 Best Google Sheets Extensions for Data & Contact Enrichment in 2026 Autom Team | Feb 26, 2026 Google Best Serper.dev Alternative in 2026 Autom Team | Jul 30, 2026 SERP API Discover why Autom is the preferred API provider for developers. Deploy your SERP scraper View pricing Fastest SERP API 8 Secure payments Discord Resources Pricing Documentation Blog Library Toolbox Service Status All resources Compare Oxylabs Scrapingbee Bright Data ScraperAPI SerpAPI See all Account Login Register Contact us Company WebAPI Group Privacy Policy Terms of Service Affiliate Bug Bounty Startup Program Preferences 🇺🇸 English Autom has been servicing since 0 years 0 months 0 days 0 hours 0 min 0 secs 🇺🇸 English
