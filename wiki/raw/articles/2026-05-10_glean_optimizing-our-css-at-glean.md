---
title: "Optimizing our CSS at Glean"
source: "Glean Blog"
url: "https://www.glean.com/blog/optimizing-our-css-at-glean"
scraped: "2026-05-10T01:27:51.781696+00:00"
lastmod: "None"
type: "sitemap"
---

# Optimizing our CSS at Glean

**Source**: [https://www.glean.com/blog/optimizing-our-css-at-glean](https://www.glean.com/blog/optimizing-our-css-at-glean)

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
Optimizing our CSS at Glean
0
minutes read
Raymond Carino
Engineering
Vardhman Singh
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
Glean transitioned from inline styles to vanilla-extract, a zero-runtime CSS-in-JS solution, to optimize performance and developer experience, despite a steeper learning curve.
The migration involved converting over 300 files and 10,000 lines of code, facilitated by a custom codemod to automate the transformation process.
The adoption of vanilla-extract improved debugging with classNames, reduced initial migration bugs, and enhanced overall productivity and web performance.
Back when
Glean
first started, we chose to use inline styles. This did not scale well as we grew, so we decided to survey CSS-in-JS options.
vanilla-extract
, our chosen solution, optimizes performance (zero-runtime overhead) and developer experience at the cost of a slightly steeper learning curve.
Read this if you:
Want to learn about performance and developer experience tradeoffs between common, modern CSS frameworks
Are interested in trying out zero-runtime CSS-in-JS solutions
{{richtext-banner-component}}
Our survey of CSS framework options
We started our search for a CSS solution by checking trends and surveys such as
State of CSS
(2021). From usage below, we saw that Styled Components and CSS Modules were a close-ish #1 and #2. Note that vanilla-extract’s usage was near the bottom, at 1%. This made sense given its first stable release was in
May 2021
.
‍
However, from developer satisfaction, we saw that vanilla-extract was leading, and CSS Modules was a very close second.
‍
To tiebreak our 3 leading options of Styled Components, CSS Modules, and vanilla-extract, we read developer blogs to dig into the pros/cons.
Why we ruled out Styled Components
Styled Components
are an opinionated mechanism of packing style properties (unclassed) into a React Component. Our main concern with Styled Components was its runtime overhead. We didn’t run a Styled Components prototype, but
other developers’ notes
were convincing. In short, Styled Components incurs a runtime bundlesize overhead from its loader. Its render, like inline styles, is also blocked until JS execution.
CSS Modules were promising
CSS Modules
are a mechanism of obfuscating CSS classes to hack local scoping into CSS. We liked its philosophical separation of concerns between CSS files and React Component files. Furthermore, CSS Modules transpile down to plain CSS assets, which are:
More
parallelizable
: CSS only blocks render (not parse) whereas JS blocks HTML parsing.
Faster for the browser to apply: See the JS styling overhead in this
benchmark
.
However, CSS Modules are not a CSS-in-JS solution, and would require migrating from TS to CSS or a preprocessor.
Why we chose vanilla-extract
vanilla-extract
’s pitch as a best of both worlds (CSS-in-JS and CSS Modules) solution was promising enough to prototype. Recall vanilla-extract is a build time TS to CSS modules preprocessor. It’s also worth noting that vanilla-extract’s author is the co-creator of CSS Modules, which is second to Styled Components in current
usage
.
We suspect that Styled Components has high usage but
relatively lower satisfaction
because it’s easy for smaller-to-medium sized projects to start up (no CSS preprocessor). Whereas CSS Modules and vanilla-extract are a better fit for larger projects due to their performance, file layout, and debuggability benefits.
vanilla-extract vs. CSS Modules
CSS Modules and vanilla-extract both support zero-runtime overhead. That is, transpiled native CSS lets the browser do what it does best in native code rather than running in JS "user space" which parses much more slowly and gets blocked during load.
However, we believe vanilla-extract’s CSS-in-JS approach is better than CSS Module transpilation because TS integration offers
IDE intellisense
,
Webpack bundle splitting
,
tree shaking (dead code pruning)
, etc. In short: easier refactoring, and better web performance due to minimal asset size.
That said, our reservations about adopting vanilla-extract still hold true. We’ve adopted the project fairly early. For example, Facebook’s CSS-in-JS solution,
Stylex
, might open source and become more popular. This concern is somewhat mitigated by Stylex’s similarity. Both transpile TS down to CSS Modules. If push comes to shove, swapping similar solutions might not be terrible. Lastly, from the
linked article
, Stylex should have been released in late 2021, but is still not available as of Sep 2022. This may be a signal that Stylex is conceding to vanilla-extract’s open source traction. We measure traction by: increasing adoption measured by
npm downloads
, and
Github commits
.
Migrating from inline styles to vanilla-extract
While we had switched to vanilla-extract for new features, we still had to migrate the existing inline styles in the codebase. This also turned out to be a fairly large refactor, as we had over ~300 files (10K lines of code) to convert to vanilla-extract.
Manually migrating some of the stylesheets we noticed that the effort is fairly mechanical as we’re converting one style of code to another; So we decided to write a codemod to do some heavy lifting.
Refactoring using codemods
A codemod is a set of transformations to automate changes that would essentially comprise a refactor. The idea is to treat the code as data for another program that would be able to understand its structure and apply specific transforms. Given the right setup, codemods can reduce a ton of time and effort that goes into large scale refactors.
Looking into the implementation, our codemod scripts would do the following for each stylesheet:
Step 1. Convert inline style rules to vanilla-extract styles
For each file we had to convert style rules into corresponding vanilla-extract style() declarations. We do use a custom Stylesheet() declaration for our existing inline styles, which is a good starting point for the codemod script. At a high level we’re looking at four separate transformations:
Find all
Stylesheet()
declarations in the file.
For each
Stylesheet()
, extract each property and expression to create a new variable declaration.
For eg: `container: { …styleRules }` → `export const container = style({ ...styleRules })`
Add an import for `style` from vanilla-extract.
Remove the Stylesheet() declaration and import.
‍
‍
Step 2. Finally, update ‘style’ props to ‘className’ in the JSX components
With the styles transformed, we also had to convert the components that were using these inline styles.
Locating them was straightforward as most of our components share a naming convention with their styles.
Once the files are located, we’re looking at a few more transformations:
Convert
style
JSXAttributes to
className
and reference the transformed styles.
Update the default styles import to named imports since we have moved away from a default Stylesheet export above.
Step 3. Add .css.ts to the filename
At this point, both the stylesheet and the component has been transformed, so the only thing left is to rename the file and add .css.ts to the filename.
Tools
We used
ASTExplorer
to explore and visualize the Abstract syntax tree (AST) for the code and figure out where to apply transformations. We also used
JSCodeshift
which provides a neat API to apply transformations to the code.
Vanilla extract in practice
After prototyping, and widely adopting, we realized
classNames for debugging
was our greatest productivity improvement. The React Component tree and DOM tree often differ greatly. A className=$fileName_$elementClass_$moduleHash (ex: ProfilePage_mainPersonCard__1bmv6no1) is far more debuggable than hacking around inline styles’ lack of
sourcemaps
. For example, we previously
hotloaded
tracer textNodes each time we needed to map rendered styles to TS source:
<div style={{...inlineStylesToDebug}}> {/* no sourcemaps */}
Test: is this the div I’m debugging? {/* tracer textNode */}
<SomeComponent />
</div>
The costs of adopting vanilla-extract were one-time:
There’s a learning curve to adopting classNames. Ex:
arbitrary className specificity resolution
. Developers needed to learn new practices such as preferring a max of 1 className per DOM element:
// Near-equivalent of
SCSS mixins
const deepMergedClassName =
style
([baseStyle, otherBase, componentOverrides])
Initial migration bugs. Migrating from inline styles to classNames breaks when selectors tie, and when previously common !important properties are present. Manually detecting bugs was tedious, but the bugs motivated more automated
Storybook screenshot diff tests
, which prevent future regressions
Takeaways
Some of the benefits of working at a fast-growing startup are:
There’s no lack of impactful work when there’s a lot of low-hanging fruit.
If you spot an improvement, you can often fully own solutions.
If
building
or
using
a best-in-class search product sounds interesting to you, reach out!
Back to all stories
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
What is Retrieval Augmented Generation (RAG)?
Retrieval Augmented Generation is a pipeline framework that retrieves information via an external discovery system, enhancing the knowledge retrieval process for large language models. Generative AI and large language models (LLMs) are emerging as some of today’s most transformative workplace technologies – however, many solutions struggle with knowledge retrieval. Retrieval Augmented Generation addresses this issue by separating the knowledge retrieval from the generation process. Learn more about what it takes to make RAG work and how it unlocks the full potential of generative AI in this free 2-pager.
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
