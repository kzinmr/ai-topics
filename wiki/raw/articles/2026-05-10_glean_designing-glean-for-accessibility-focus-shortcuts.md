---
title: "Designing Glean for accessibility – focus & shortcuts"
source: "Glean Blog"
url: "https://www.glean.com/blog/designing-glean-for-accessibility-focus-shortcuts"
scraped: "2026-05-10T01:27:19.354534+00:00"
lastmod: "None"
type: "sitemap"
---

# Designing Glean for accessibility – focus & shortcuts

**Source**: [https://www.glean.com/blog/designing-glean-for-accessibility-focus-shortcuts](https://www.glean.com/blog/designing-glean-for-accessibility-focus-shortcuts)

Product
WORK AI PLATFORM
Platform Overview
Glean Assistant
Your personal AI assistant
Data Analysis
Canvas
Deep Research
Glean Agents
Build and manage AI agents
Agent Builder
Agent Governance
Agent Orchestration
Agent Library
Glean Search
The foundation of enterprise AI
Enterprise Graph
Personal Graph
System of context
Hybrid Search
Connectors & Actions
Connect to all your apps
Model Hub
Get access to the latest models
APIs
Build generative AI experiences
Security
Safely scale AI at work
Agentic Engine
Plan & adapt over company context
GLEAN WHERE YOU WORK
Glean in Slack
Glean in Microsoft Teams
Glean in Zoom
Glean in Service Cloud
Glean in ServiceNow
Glean in Zendesk
Glean in GitHub
Glean in Miro
Browser Extension
Sign in
Customers
Solutions
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
Marketing
B2B Marketing
B2C Marketing
People
IT
INDUSTRIES
Retail
Financial Services
Banking
PE/VC
Asset management
Insurance
Higher Education
Healthcare
Government
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Sign in
Joel McKelvey
Head of Solutions, Glean
Abdullah Haydar
Director of Engineering, LinkedIn
Webinar
AI Powered Engineering
Expert insights and actionable strategies for accelerating developer productivity.
Watch now
Resources
EXPLORE
Resource Center
Blog
Prompt Library
Guides
Product Videos
ENGAGE
Webinars
Newsroom
Glean:GO 2026
Events
Gleaniverse Community
SUPPORT & SERVICES
Help Center
Developers
Partners
Work AI Institute
Sign in
The AI Transformation 100
Explore 100 real-world moves organizations are making to transform themselves with AI.
Download the report
About
Thank you! Your submission has been received!
Oops! Something went wrong while submitting the form.
Sign in
Get a demo
Get a demo
Sign in
Get a demo
Get a demo
Product
Customers
Solutions
Resources
About
Sign in
Back
WORK AI PLATFORM
Platform Overview
Glean Assistant
Your personal AI assistant
Data Analysis
Canvas
Deep Research
Glean Agents
Build and manage AI agents
Agent Builder
Agent Governance
Agent Orchestration
Agent Library
Glean Search
The foundation of enterprise AI
Enterprise Graph
Personal Graph
System of context
Hybrid Search
Connectors & Actions
Connect to all your apps
Model Hub
Get access to the latest models
APIs
Build generative AI experiences
Security
Safely scale AI at work
Agentic Engine
Plan & adapt over company context
GLEAN WHERE YOU WORK
Glean in Slack
Glean in Microsoft Teams
Glean in Zoom
Glean in Service Cloud
Glean in ServiceNow
Glean in Zendesk
Glean in GitHub
Glean in Miro
Browser Extension
Sign in
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
Marketing
B2B Marketing
B2C Marketing
People
IT
INDUSTRIES
Retail
Financial Services
Banking
PE/VC
Asset management
Insurance
Higher Education
Healthcare
Government
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Sign in
Joel McKelvey
Head of Solutions, Glean
Abdullah Haydar
Director of Engineering, LinkedIn
Webinar
AI Powered Engineering
Expert insights and actionable strategies for accelerating developer productivity.
Watch now
EXPLORE
Resource Center
Blog
Prompt Library
Guides
Product Videos
ENGAGE
Webinars
Newsroom
Glean:GO 2026
Events
Gleaniverse Community
SUPPORT & SERVICES
Help Center
Developers
Partners
Work AI Institute
Sign in
The AI Transformation 100
Explore 100 real-world moves organizations are making to transform themselves with AI.
Download the report
Last updated Jan 27, 2026.
Designing Glean for accessibility – focus & shortcuts
0
minutes read
Tommy Vo
Engineering
Keya Mann
Engineering
Listen to article
0:00
0.5x
1x
1.5x
2x
Table of contents
Heading 2
Heading 3
Heading 4
Heading 5
Heading 6
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
Share this article:
Listen to article
0:00
0.5x
1x
1.5x
2x
AI Summary by Glean
Glean emphasizes the importance of considering accessibility from the start, incorporating a common design system, and securing early buy-in from stakeholders to ensure long-term commitment and resource allocation.
The blog discusses the significance of enabling keyboard-only navigation with clear focus indicators, using CSS properties like :focus-visible, and maintaining intuitive focus order to enhance usability for keyboard and screen reader users.
Keyboard Shortcuts and Navigation: Glean has integrated various keyboard shortcuts to improve navigation efficiency, such as using the [Tab] key, arrow keys, and global shortcuts like F6. They also highlight the importance of documenting these shortcuts for user accessibility.
‍
Although Glean is just about five years old, our team makes considerable efforts to get things right from the very beginning. It’s helped lend Glean layers of maturity you may not often see in newer products.
One of those layers is accessibility. In line with our mission to democratize knowledge discovery, we’ve made great strides during our journey to make Glean more friendly and usable for everyone. In this blog, we’ll share how we built Glean to be more accessible, along with a few learnings from both a technical and practical perspective.
Guiding principles
Accessibility is a must-have for every product to reach its widest audience. We often receive feedback from customers who want to use Glean effortlessly without a mouse, or understand Glean better when using a
screen reader
. Accessibility compliance is also a business consideration – it’s a common legal requirement for enterprise customers, and sometimes a last-minute hurdle to closing deals.
Taking these into account, we committed to developing with accessibility in mind and settled on a few guiding principles to set us on our way:
Consider accessibility at the start of the process – the earlier, the better
Incorporate a common design system across the product to scale accessibility efficiently
Get buy-in early from stakeholders, such as product teams and leadership, to align on long-term commitment and resource allocation
With these principles outlined, we moved on to developing our first key improvements for Glean’s keyboard and shortcut experience.
Implementing focus indicators for keyboard-only use
Not everyone can use a mouse – and navigating a product via keyboard closely resembles how a screen reader user accesses the product. Thus, it’s beneficial to make your product work well with a keyboard.
One of the most important functionalities is enabling users to stay in focus. While navigating the website via keyboard, there
should always be a focus indicator
telling users where their interaction is.
When an interactive element (i.e link) is focused, there should be a clear indicator around it
There are a few common ways to implement such focus indicator (also known as a "focus ring"):
<ul type='disc'>
<li> Using popular libraries such as
Discord
or
React-Aria
FocusRing, both React-friendly </li>
<li> Or, implementing it yourself. Luckily the web standard has caught up quickly the past few years, making this easier:
<ul type='disc'>
<li> Previously, developers relied on the <span class="text-rich-text-code" style="font-family: monospace;">:focus</span> CSS property </li>
<li> There’s now a widely supported <span class="text-rich-text-code" style="font-family: monospace;">:focus-visible</span> property to detect when an interactive element receives focus and the user agent/browser allows the focus indicator to be visible <ul type='disc'>
<li> For most browsers, this is the equivalent to the interactive element receiving focus via keyboard </li>
<li> Alternatively, you can use a
polyfill
to mirror this behavior, for more flexibility </li>
</ul>
</li>
<li> To style the indicator itself, you can use common CSS properties such as <span class="text-rich-text-code" style="font-family: monospace;">outline</span> (default behavior), <span class="text-rich-text-code" style="font-family: monospace;">border</span>, or <span class="text-rich-text-code" style="font-family: monospace;">box-shadow</span> <ul type='disc'>
<li> You can also use pseudo-selectors like <span class="text-rich-text-code" style="font-family: monospace;">::before</span> and <span class="text-rich-text-code" style="font-family: monospace;">::after</span> to avoid any potential layout conflict (i.e with <span class="text-rich-text-code" style="font-family: monospace;">padding</span> or <span class="text-rich-text-code" style="font-family: monospace;">margin</span>), which could happen with the aforementioned properties </li>
</ul>
</li>
</ul>
</li>
</ul>
Aside from having a focus indicator that works with keyboard shortcuts (more in the latter section), there are other common focus best-practices that we’ve implemented:
<ul type='disc'>
<li> Having a
skip link
to immediately bring focus to the main content is very helpful, especially if your site has a verbose header & navigation system </li>
<li> Keep focus order intuitively, meaning:
<ul type='disc'>
<li> Keep your <span class="text-rich-text-code" style="font-family: monospace;">tabIndex</span> usage simple. It should either be <span class="text-rich-text-code" style="font-family: monospace;">-1</span> or <span class="text-rich-text-code" style="font-family: monospace;">0</span>. A positive value means the element’s focus order might mismatch its visual order (i.e a button might be focused before its prior sibling) </li>
</ul>
</li>
<li> Make sure focus is intuitively tracked when traversing across different UI layers:
<ul type='disc'>
<li> For example, when selecting a button that opens up a dialog, focus should be placed to the first interactive element within the dialog. Closing the dialog later would restore focus to its trigger – the previous button </li>
</ul>
</li>
<li> Keep <span class="text-rich-text-code" style="font-family: monospace;">autofocus</span> to a minimum:
<ul type='disc'>
<li> <span class="text-rich-text-code" style="font-family: monospace;">autofocus</span> is a useful tool to place user to where they should be </li>
<li> However, it also causes user to skip over many potentially important information prior </li>
<li> Potential conflict with other autofocus elements can arise </li>
<li> Instead of allowing a primitive/simple element (such as an <span class="text-rich-text-code" style="font-family: monospace;">input</span>) to autofocus, keep that logic as high-level as possible, i.e the page where the <span class="text-rich-text-code" style="font-family: monospace;">input</span> is displayed </li>
</ul>
</li>
</ul>
Life is easier with shortcuts
As mentioned earlier, keyboard shortcuts simulate how a screen reader user navigates the site. Power users also rely on shortcuts to make themselves more productive. It’s an excellent way to help all sorts of users access the product in the way they want.
In every website, you can use the
[Tab]
key to move focus around (which should work in tandem with the focus indicator). Focus order should resemble the interactive elements order within the DOM tree (and depends on <span class="text-rich-text-code" style="font-family: monospace;">tabIndex</span>)
Since using
[Tab]
is the comprehensive but exhaustive method to navigate through the site, there are a few common patterns to make navigation faster and more intuitive. One of these is via the arrow keys. This method is the most common way to navigate every website, i.e for menu navigation, or adjacent items within a list
Arrow keys can also be used to cycle between search results or tables
Navigating via tab and arrow keys
There’s a few other shortcut recommendations to consider:
If your website comprises of multiple important sections (such as sidebar, header, main content, footer, etc...), it’s worthwhile to add a global shortcut to cycle through these regions & allow accessing relevant content much faster. We pick F6 (and Shift + F6 for the other direction) for this purpose
Users should be able to use any arrow keys for two-dimension navigation across complex structures, such as tables.
Navigating via F6 and table navigation with arrow keys
Last but not least, documenting these keyboard shortcuts within the site makes it much more friendly for new users to learn. Within Glean, users can use Command + ‘/’ anywhere to retrieve a list of our supported shortcuts
Documenting shortcuts helps users learn them easier
Accessibility is a journey
Building a product from scratch always has its challenges, but it’s incredibly rewarding to try do it right the first time around. Optimizing the keyboard experience and integrating shortcuts is only part of our accessibility suite and pipeline – as we continue to build Glean, we’re
committed
to being compliant with WCAG 2.1 AA standards. If you’re interested to learn more, stay tuned for part two of our accessibility blog series!
Have any inquiries or requests when it comes to accessibility? Please reach out to
a11y@glean.com
– and check out our
public accessibility roadmap
to know what we’re actively working on to bring
better search and knowledge discovery
into the hands of more users.
Back to all stories
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
Get The Resource
Get The Resource
Work AI for all.
Get a Demo
Work AI that works.
Get a demo
Ask AI for a summary about Glean
634 2nd Street
San Francisco, CA 94107
United States
Language
English (United States)
Japanese (Japan)
PRODUCT
Work AI Platform
Workplace Search
Assistant
Data Analysis
Deep Research
Canvas
Prompt Library
Agents
Agent Builder
Agent Orchestration
Agent Library
Agentic Engine
Connectors
Model Hub
Security
System of Context
SOLUTIONS
All Teams
Engineering
Sales
Marketing
Support
People
Retail
Financial Services
USE CASES
Enterprise AI
Enterprise Search Software
AI Agent Orchestration
COMPARISONS
Glean vs other alternatives
Glean vs ChatGPT Enterprise
Glean vs Microsoft 365 Copilot
Glean vs Claude Enterprise
RESOURCES
Resources Center
Product Videos
Guides
Customer Stories
Blog
Events
Webinars
Developers
Help Center
Download Glean
Product Drops
AI Glossary
Gleaniverse Community
COMPANY
About
Careers
Newsroom
Referrals
Partners
Trust center
260 Sheridan Ave, Suite 300
Palo Alto, CA 94306, United States
Gartner®, Peer Insights™, Voice of the Customer for Insight Engines, Peer Contributors, 28 June 2024.
Gartner Peer Insights content consists of the opinions of individual end users based on their own experiences, and should not be construed as statements of fact, nor do they represent the views of Gartner or its affiliates.
Gartner does not endorse any vendor, product or service depicted in this content nor makes any warranties, expressed or implied, with respect to this content, about its accuracy or completeness, including any warranties of merchantability or fitness for a particular purpose.
GARTNER is a registered trademark and service mark of Gartner, Inc. and/or its affiliates in the U.S. and internationally, and PEER INSIGHTS and GARTNER PEER INSIGHTS CUSTOMERS’ CHOICE BADGE is a registered trademark of Gartner, Inc. and/or its affiliates and are used herein with permission. All rights reserved.
©
2026
, Glean Technologies, Inc.
Website Terms
Privacy
