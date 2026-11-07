---
source_url: https://mcp-explained.com/
fetched: 2026-11-07
capture: active-crawl
---

# SOURCE: https://mcp-explained.com/

MCP Explained · how the Model Context Protocol works 

 Model Context Protocol 
 What is MCP? 
 An open standard for connecting AI apps to the tools and data they use. A server says what it can do, the app shows that to the model, and when the model wants something the app calls the server and hands the result back. 

 Host the AI app you use: Claude, Cursor, ChatGPT, an agent 
 Server a small program exposing tools, data or prompts 
 Model decides what to use; never talks to a server directly 
 Not REST JSON-RPC over stdin/stdout or one HTTP endpoint, and servers can talk back 
 Not just JSON-RPC JSON-RPC is the envelope. MCP defines what goes in it: the methods, capability negotiation, transports and auth 

 Start the lessons → 
 or jump to Tools · the spec time machine · Break it 

 Model Context Protocol Lessons Spec 
 Spec 

 Network Sequence 

 Message flow 

 Step 
 Reset 

 # From To Method Info 

 Not in the MCP spec A harness implementation detail, not part of MCP. Nothing new on the wire: the client and servers still speak plain tools/list and tools/call . 

 Message 

 MCP spec 2025-11-25. Token counts are illustrative. Made by Runlayer , the operating layer for AI. Source .
