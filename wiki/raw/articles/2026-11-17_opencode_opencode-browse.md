---
title: "OpenCode Browse product page"
type: article
source: https://opencode.ai/product/browse
published: 2026-11-16
fetched: 2026-11-17T12:05:41Z
sha256: e999536e2becd3483b73cb10b96ec1197961b01fd6a42e89d5c7a9d8ffe5df63
---

OpenCode | Browse, your real browser for coding agents 

 Skip to content [ 0 ] Docs [ 0 ] Product [ 0 ] Data [ 0 ] Console [ 0 ] Models [ 0 ] Subscriptions [ 0 ] Enterprise [ ] Changelog [ ] GitHub (opens in a new tab) English 简体中文 Chinese, Simplified 繁體中文 Chinese, Traditional 한국어 Korean Deutsch German Español Spanish Français French Italiano Italian Dansk Danish 日本語 Japanese Polski Polish Русский Russian Українська Ukrainian العربية Arabic Norsk Norwegian Português (Brasil) Portuguese, Brazil ไทย Thai Türkçe Turkish [ 0 ] Docs [ 0 ] Product [ 0 ] Data [ 0 ] Console [ 0 ] Models [ 0 ] Subscriptions [ 0 ] Enterprise [ ] Changelog [ ] GitHub (opens in a new tab) Product | Browse Browse An MCP server and a Chromium extension that let your agents use your real browser, with your tabs, your logins and your extensions. They open tabs in the background, grouped out of your way, and read pages, click, type, take screenshots and record tabs. When it's your turn, for a login, a 2FA prompt or a payment, they hand the tab back to you and continue once you click Continue. Add to Chrome (opens in a new tab) View source (opens in a new tab) Your real browser Chrome, Edge, Brave, Arc, Helium, Vivaldi, Opera and Chromium. Out of your way Agent tabs open in the background, in collapsed groups. Handoffs Do the login or 2FA step yourself, then click Continue. Lend a tab Click the toolbar button to hand an agent a tab you have open. Record and capture Screenshots, tab recordings and network traffic. Any MCP client OpenCode, Claude Code, Cursor, Codex, Zed and many more. All your logins Agents use the sites you're already signed into. No keys, no setup. Allowed sites Keep an agent's tab on the sites you name. Install Install the Chrome extension first. It walks you through the rest of the steps. To install the CLI directly (you should not need to do this), use any of these. curl curl -fsSL https://opencode.ai/browse/install | bash Copy curl command pwsh irm https://opencode.ai/browse/install.ps1 | iex Copy pwsh command npm npm install -g @opencode/browse && browse install Copy npm command bun bun add -g @opencode/browse && browse install Copy bun command More from Anomaly Hex On-device voice dictation for any app. Learn more (opens in a new tab) OpenTunnel Public HTTPS URLs for local apps. Learn more (opens in a new tab) OpenTUI A library for terminal user interfaces. Learn more (opens in a new tab) [ ] Community (opens in a new tab) [ ] Changelog [ ] Press [ ] Brand [ ] Legal [ ] English English 简体中文 繁體中文 한국어 Deutsch Español Français Italiano Dansk 日本語 Polski Русский Українська العربية Norsk Português (Brasil) ไทย Türkçe Status: Normal (opens in a new tab) ©2026 Anomaly Drag a letter to move it. With the keyboard, press Space to pick up a letter, the arrow keys to move it and Space to drop it, or Alt and an arrow key to move it at once. Like letters? Check out the OpenCode font

## HN discussion highlights (item 50523459, 281pts)

### opencode-browse  (281pts, story=OpenCode Browse)
[orsenthil] OpenCode comes with the cost too. The cost of the hosted version is on par with cloud hosted proprietary models. And we cannot simply run the LLMs on every laptop. Given this, how do we us the browse efficiently?
---
[sixtyj] > Your real browser: 
Chrome, Edge, Brave, Arc, Helium, Vivaldi, Opera and Chromium. Firefox not?
---
[jeremyjacob] The functionality seems to overlap with the Playwright MCP server [0]. I've been using this instead of the built in browsers in Claude Code and Codex since it lets you grant access to pages and sessions that are already open. Of course one should be weary of the lethal trifecta when using these tools and use separate profiles for them. [0]  https://playwright.dev/docs/getting-started-mcp
---
[esafak] It's all right when it works, but it has a habit of disconnecting; you have to rerun 'browse pair'. This MCP should hopefully become unnecessary once OpenCode's integrated browser tool gains persistent sessions.  https://github.com/anomalyco/opencode/pull/63002
---
[testtestmetest] Opencode vibe codes and releases like 3 projects a week at this points. Cool, just know its throwaway software to them. They seem really reckless when it comes to security. Opencode V2 basically threw security out the window. Theyve completely lost the plot as an org. Their CEO spends all day on twitter talking about how much better he is than everyone. And how nobody can use agents like he can. Its quite obnoxious Also just use CDP, way too many
---
[vibebingo] Oh this is a problem? I just ask my agent to do stuff with a browser and it figures it out.
---
[latchkey] codex's extension connection will often randomly fail on me and i (and ai) can't figure out how to get it working again. i've switched to using omp's extension and that seems to work better.  https://github.com/can1357/oh-my-pi/blob/main/packages/brows...
---
[_pdp_] Cool.. but I think it is just simply better to give your AI agents their own browsers for your own sanity.
---
[skeledrew] I found agent browsing to be an issue when I started using them months ago. Built a Firefox extension back then that uses the browser instance that I use, the way I use it, so there's really no difference to a site.
---
[breakwaterlabs] At least they don't even pretend that it's sandboxed or approval gated. To anyone trying this, good luck and keep a fire extinguisher handy.
---
