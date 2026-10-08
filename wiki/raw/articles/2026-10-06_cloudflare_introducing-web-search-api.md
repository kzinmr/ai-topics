---
source_url: https://developers.cloudflare.com/changelog/post/2026-10-02/web-search-api/
ingested: 2026-10-06
sha256: 797735ace60602728f9c9987ff42c2e1aeabea7399091324abfb1677c6314e5b
---

Skip to content Docs Search Ctrl K Log in Dashboard Changelog New updates and improvements at Cloudflare. 
 View RSS feeds
 
 Subscribe to RSS
 Back to all posts October 2, 2026 Introducing Web Search API AI Gateway Web Search API Copy as Markdown | View as Markdown | Agent setup Web Search API is now available in beta. Web Search API lets your AI agents and applications search the Internet and ground their responses in live information, instead of guessing URLs or relying on a model's training cutoff. 
 At launch, you can choose between three search providers: Ceramic.ai, Exa, and Linkup . All three support Zero Data Retention for requests made through Cloudflare, and all have committed to Cloudflare's verified bot crawling standards. 
 Web Search API runs through AI Gateway , so search requests appear in your gateway logs and are billed to your AI Gateway credits at each provider's list API price, with no additional markup. You can also bring your own provider API key. 
 Call Web Search API with the REST API: 
 curl https://api.cloudflare.com/client/v4/accounts/ $CLOUDFLARE_ACCOUNT_ID /ai/websearch/ \ 
 --request POST \ 
 --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN " \ 
 --header "Content-Type: application/json" \ 
 --data '{ 
 "query": "What are some fun things to do in Salt Lake City as fall approaches?", 
 "provider": "ceramic", 
 "limit": 5, 
 "options": { "gateway": { "id": "default" } } 
 }' 
 Or from a Worker with the AI binding: 
 const response = await env. AI . websearch ({ 
 gatewayId: "default" , 
 query: "What are some fun things to do in Salt Lake City as fall approaches?" , 
 provider: "exa" , 
 limit: 5 , 
 }); 
 
 const results = await response. json (); 
 To get started, refer to How to use Web Search API .
