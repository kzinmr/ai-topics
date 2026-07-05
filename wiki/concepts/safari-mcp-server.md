---
title: "Safari MCP Server"
type: concept
created: 2026-07-05
updated: 2026-07-05
tags:
  - mcp
  - apple
  - browser
  - web-development
  - coding-agents
related:
  - concepts/mcp.md
  - concepts/coding-agents.md
  - entities/apple.md
sources:
  - raw/articles/webkit.org--blog-18136-introducing-the-safari-mcp-server-for-web-develop--01cdb46f.md
---

# Safari MCP Server

## Overview

**Safari MCP Server** is Apple's first official implementation of the Model Context Protocol ([[concepts/mcp.md]]), released as part of **Safari Technology Preview 247**. It enables [[concepts/coding-agents.md]] and other MCP-compatible clients — such as Claude Desktop, Claude Code, or custom agent harnesses — to connect to a running Safari browser window and programmatically inspect, debug, and interact with web pages.

The server acts as a bridge between an AI agent and the Safari browser, exposing the full WebKit developer tooling surface through MCP tools. This means an AI coding agent can open a web application in Safari, examine its DOM structure, read console logs, intercept network requests, evaluate JavaScript expressions, take screenshots, and even navigate through multiple tabs — all through natural language prompts.

Apple's decision to ship a first-party MCP server signals a significant shift: after years of third-party browser automation efforts (Puppeteer, Playwright), the browser vendor itself is now providing an official MCP interface, reducing reliance on fragile DOM-scripting approaches and giving AI tooling direct access to the browser's internal debugging APIs.

## Available Tools

The Safari MCP server exposes the following tools for MCP clients:

| Tool | Description |
|------|-------------|
| `browser_console_messages` | Retrieve console output (logs, warnings, errors) from the current page |
| `browser_dialogs` | Intercept and handle browser dialogs (alert, confirm, prompt) |
| `close_tab` | Close a specific browser tab by ID |
| `create_tab` | Open a new blank tab in the browser |
| `evaluate_javascript` | Execute arbitrary JavaScript in the page context and return results |
| `get_network_request` | Retrieve details of a specific network request by ID |
| `get_page_content` | Get the full HTML content of the current page |
| `list_network_requests` | List all network requests made by the current page |
| `list_tabs` | Enumerate all open tabs with their titles and URLs |
| `navigate_to_url` | Navigate the current tab to a specified URL |
| `page_info` | Get metadata about the current page (URL, title, load status) |
| `page_interactions` | List or trigger page interaction events |
| `screenshot` | Capture a screenshot of the current viewport |
| `set_emulated_media` | Simulate media features (prefers-color-scheme, prefers-reduced-motion) |
| `set_viewport_size` | Resize the browser viewport to specified dimensions |
| `switch_tab` | Switch focus to a different tab by ID |
| `wait_for_navigation` | Wait for the page to finish navigating to a URL |

These tools collectively provide a complete web debugging and automation surface, comparable to what a developer would access manually through Safari's Web Inspector panel.

## Use Cases

### Debugging

An AI agent can open a web application, navigate to a failing page, inspect console errors, examine network requests for failed API calls, and evaluate JavaScript expressions to probe application state — all without the developer leaving their chat interface. For example:

1. `navigate_to_url` → load the failing page
2. `browser_console_messages` → read errors
3. `list_network_requests` → find failed API calls
4. `get_network_request` → inspect request/response details
5. `evaluate_javascript` → probe component state

### Performance Analysis

By combining `list_network_requests` with `get_network_request`, an agent can analyze load times, resource sizes, and waterfall patterns. The `screenshot` tool captures visual rendering state for comparison. Combined with viewport emulation, agents can test performance across device profiles.

### Accessibility Testing

The `set_emulated_media` tool allows agents to test page behavior under accessibility preferences such as `prefers-reduced-motion` and `prefers-color-scheme: dark`. By scripting navigation through a page's structure via `evaluate_javascript`, agents can audit heading hierarchies, ARIA attributes, and focus management.

### Cross-Browser Compatibility

While Safari MCP only controls Safari, its standardized MCP interface means that agents can orchestrate testing across multiple browsers by connecting to separate MCP servers (e.g., a Playwright MCP server for Chrome/Firefox alongside Safari MCP), running the same test scenarios in each.

## Relationship to MCP

The Safari MCP server is a concrete implementation of the **Model Context Protocol** ([[concepts/mcp.md]]) — it acts as an MCP **server** that exposes browser capabilities as MCP **tools**. Any MCP-compatible **client** (Claude Desktop, Claude Code, custom agents, VS Code via Copilot) can connect to it.

This follows the standard MCP architecture:

- **Client** (e.g., Claude) sends tool requests via MCP
- **Server** (Safari MCP) translates those requests into WebKit remote debugging protocol commands
- **Host** (Safari Technology Preview) executes the browser operations and returns results

Apple's adoption of MCP is notable because it represents a major platform vendor natively supporting the protocol, adding significant legitimacy to MCP's role as the "USB-C for AI tools." Prior to this, browser MCP servers were third-party projects (e.g., Playwright MCP, Puppeteer MCP) that ran standalone browser instances. Safari MCP is the first to integrate directly with the vendor's own browser.

## Related Browser Automation Tools

Safari MCP occupies a unique position in the ecosystem of browser automation tools:

| Tool | Type | Browser | Vendor |
|------|------|---------|--------|
| **Safari MCP** | MCP server (first-party) | Safari | Apple |
| **Playwright MCP** | MCP server (third-party) | Chromium/Firefox/WebKit | Microsoft |
| **Puppeteer MCP** | MCP server (third-party) | Chromium | Google (community) |
| **Browserbase MCP** | MCP server (cloud) | Chromium | Browserbase |
| **WebDriver (Selenium)** | W3C standard protocol | All | W3C |
| **Playwright** | Automation library | All | Microsoft |
| **Puppeteer** | Automation library | Chromium | Google |

The key differentiator of Safari MCP is that it connects to **an already-running Safari window** that the developer can see and interact with — it does not launch a headless browser. This makes it ideal for debugging sessions where a developer wants an AI assistant to help inspect a page they are already viewing.

It also runs on **macOS only** (as Safari is macOS-exclusive) and requires **Safari Technology Preview 247** or later. This is a deliberate choice by Apple to target professional web developers working on Apple hardware.

For Apple ecosystem developers using [[concepts/coding-agents.md]], the Safari MCP server provides native integration that avoids the reliability issues of scripting Safari via WebDriver or Playwright WebKit mode — it speaks the browser's native debugging protocol directly through an MCP interface, making it the most reliable way for AI agents to interact with Safari.
