---
title: "Introducing the Safari MCP server for web developers"
url: "https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/"
fetched_at: 2026-07-03T07:00:57.958532+00:00
source: "daringfireball.net"
tags: [blog, raw]
---

# Introducing the Safari MCP server for web developers

Source: https://webkit.org/blog/18136/introducing-the-safari-mcp-server-for-web-developers/

In
Safari Technology Preview 247
, we’re introducing the Safari MCP server — a Model Context Protocol server for web developers that makes your web development and debugging workflow faster and more powerful. We know agents are increasingly integral to the coding process and the Safari MCP server gives your agent the ability to know how your code actually renders in the browser by connecting it to a Safari browser window.
Any MCP-compatible client can connect to the Safari MCP server. By connecting your agent to a Safari browser window, your agent can emulate what your users experience, giving it the information it needs to debug more autonomously, like access to the DOM, network requests, screenshots, and console output.
It speeds up your debugging process and lets you stay in the comfort of your terminal, which means fewer rounds of hopping windows and typing prompts to debug your code.
The use cases
If you build for the web, then you know about the debugging dance. It usually goes something like this:
You see something wrong with your site in the browser. You open the console to hunt it down. You click into the styles tab. You see what’s broken. You go back to your code to fix it. Or maybe you take a screenshot, detail the problem to your agent, and let it do the fixing for you. Hopefully it gets it right, the bug is fixed, and you can move on.
But when it isn’t fixed, you go through the workflow again — Browser. Prompt. Agent.
And again and again, until you finally squash the bug.
Regardless of the browser or tools you use, the debugging workflow is a lot of clicks, tools, and window hopping to make a single fix, but it doesn’t have to be that way. If you’re already using agents in your development workflow, the Safari MCP server makes your debugging faster and more efficient.
The Safari MCP server enables your agent to do more debugging and troubleshooting on its own. Here are just a few examples of what it can help with:
Web development in Safari
. The next time you develop in Safari, you’ll benefit from an upgraded workflow. Your agent already helps you with your code, now it can do even more by checking out how your code actually renders in Safari.
Improve compatibility with Safari.
Testing in just one browser means missing potential bugs in another, giving those users a subpar experience. With the Safari MCP server, your agent can open your site in Safari, inspect computed styles, check layout, and compare it against what you expect without switching windows.
Analyze performance.
See what parts of your site are slowing things down. The Safari MCP server lets your agent evaluate JavaScript on the page to surface performance metrics, like navigation timing and resource load times, so it can pinpoint what’s slowing your site down and work on the right fix.
Check for accessibility.
The Safari MCP server lets your agent check for common accessibility issues like missing labels, improper ARIA attributes, and poor contrast, so you can catch problems that impact your users.
Verify any user state.
Know that the page is working and looking as it should. Your agent can check the state of the form, query an element using a selector, confirm specific interactions, show different states of a checkout flow, and more. Spend less time on these manual checks and empower the agent to do it for you.
These are just a few of the use cases. However you decide to implement it, the Safari MCP server helps your agent do more for you and reduce all the back and forth that web development often requires. An easier workflow means more bugs squashed, happier users, and a better product.
The tools
Here are the available tools and what they do:
Tool
Description
browser_console_messages
Return buffered console logs for the current or specified tab
browser_dialogs
List and respond to browser dialogs (accept, dismiss, or input text for JS prompts)
close_tab
Close a browser tab by its handle
create_tab
Create a new browser tab, optionally loading a URL
evaluate_javascript
Execute JavaScript code within the page and return the result
get_network_request
Get full detail for a single recorded network request (headers, body, timing)
get_page_content
Extract text content of a page in various formats (markdown, HTML, JSON, etc.)
list_network_requests
List network request summaries (URL, method, status, timing) for the current tab
list_tabs
List all open browser tabs with their handles and URLs
navigate_to_url
Navigate to a URL and return the loaded page’s content
page_info
Get info about the current page: URL, title, and loading state
page_interactions
Perform DOM interactions in sequence: click, type, scroll, hover, keyPress, etc.
screenshot
Capture a screenshot of the current page as a PNG
set_emulated_media
Emulate a CSS media type (e.g. “print”) for responsive-design testing
set_viewport_size
Set the browser viewport size in CSS pixels
switch_tab
Switch to a different browser tab by its handle
wait_for_navigation
Wait for the current page to finish loading; returns final URL and title
With the Safari MCP server, you no longer have to write the perfect prompt, carefully describing to your agent what you’re experiencing in the browser. You can give your agent the ability to find out for itself.
How to get started
First you’ll need to install
Safari Technology Preview
. Once installed, make sure you enable Safari Settings > Advanced > Show features for web developers. Then go to Safari Settings > Developer > Enable remote automation and external agents.
If you’re using Claude, you can use the following command in your terminal:
claude mcp add safari-mcp-stp -- "/Applications/Safari Technology Preview.app/Contents/MacOS/safaridriver" --mcp
If you’re using Codex, you can use the following command in your terminal:
codex mcp add safari-mcp-stp -- "/Applications/Safari Technology Preview.app/Contents/MacOS/safaridriver" --mcp
For other agents, you can put the following in your
mcp.json
or
config.json
:
"safari-mcp-stp"
:
{
"command"
:
"/Applications/Safari Technology Preview.app/Contents/MacOS/safaridriver"
,
"args"
:
[
"--mcp"
] 
}
Note that while the above code names the server
safari-mcp-stp
, you can name it whatever you like, even just
safari
. Once you have the Safari MCP server installed, try one of the following prompts:
Find bugs on my site in Safari
How accessible is my site in Safari?
See how my website performs in Safari
While each agent works a little differently, it shouldn’t need to be told to use the Safari MCP server explicitly — it’ll figure it out on its own. Simple prompts like the ones above are enough to kickstart the MCP.
Here’s how a conversation with an agent using the Safari MCP server might go:
You:
Got a bug report — something’s broken in Safari on the flight page. Can you figure out what’s going on?
Agent:
Sure, let me take a look.
Agent:
I found two distinct bugs on the flight page in Safari. Want me to fix them both?
You:
Yes. Anything else here that might be causing problems for Safari users?
Agent:
Yes, two more things worth flagging. The results reveal animation is silently broken and the API server startup log is wrong. Should I tackle both as well?
All you need is an initial request to get started, and with the help of the Safari MCP server, your agent can take it from there.
The Safari MCP server runs entirely on your local machine and makes no network calls of its own. It also does not have access to your personal information in Safari (e.g. AutoFill or other browser activity). When it captures page content, screenshots, or console logs, that data goes directly to the agent you’re running — not to Apple. What happens to that data from there depends on the agent and model you’re using. As with any agent you give access to your browser, only use ones you trust.
Why we built this
There are many ways to build for the web, both with and without AI. If AI is a part of your workflow, we think this tool will help make it even more productive. And if it isn’t, that’s OK too.
By creating this resource, we hope to make it easier than ever to test and debug in Safari by helping your agent understand how things look and work in the browser.
If you end up giving it a try or if this is your first time using an MCP server, let us know what you think.
Find us online: Saron Yitbarek on
BlueSky
, Jen Simmons on
Bluesky
/
Mastodon
, and Jon Davis on
Bluesky
/
Mastodon
. If you run into any issues, file a
WebKit bug report
. Filing issues really does make a difference.
