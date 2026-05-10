---
title: "Designing Glean for accessibility – design system and compliance"
source: "Glean Blog"
url: "https://www.glean.com/blog/designing-glean-for-accessibility-design-compliance"
scraped: "2026-05-10T01:27:18.008373+00:00"
lastmod: "None"
type: "sitemap"
---

# Designing Glean for accessibility – design system and compliance

**Source**: [https://www.glean.com/blog/designing-glean-for-accessibility-design-compliance](https://www.glean.com/blog/designing-glean-for-accessibility-design-compliance)

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
Designing Glean for accessibility – design system and compliance
0
minutes read
Sashank Gogula
Software Engineer
Sarah Ross
Software Engineer
Anojen Jeyapalan
Product Designer
Tommy Vo
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
Glean has fundamentally integrated accessibility into its design system by standardizing components and design tokens, ensuring that every new feature is accessible by default and reducing inconsistencies and regressions across the product.
The migration to a more accessible foundation, powered by Base UI, has improved out-of-the-box support for screen readers, keyboard navigation, and focus management, making the user interface more reliable and inclusive for all users.
Glean has achieved formal accessibility compliance through an up-to-date Accessibility Conformance Report (VPAT), enabling customers to evaluate its alignment with accessibility standards and reinforcing accessibility as a core design principle moving forward.
Over the last couple of years, we’ve shared how Glean approaches
focus management and keyboard shortcuts
, as well as
screen readers, color, and responsive design
. Those posts covered the philosophy and the technical underpinnings behind our accessibility work from an engineering perspective.
We wanted to now follow up with a
design perspective
—showing how these changes mark a shift in how we build products. Instead of treating accessibility as a set of one‑off fixes, we’re baking it directly into our tokens, components, and patterns. That way, accessibility becomes the default for every new feature.
With that, we’re excited to share two big milestones in our journey:
We’ve
revamped our design system
into a more accessible foundation powered by
Base UI
, which brings better screen reader and keyboard accessibility out of the box. Many thanks to the Base UI team and congrats on the 1.0 launch! 🎉
We’ve completed our
VPAT
(Voluntary Product Accessibility Template), improving transparency during evaluations. Customers can formally review how Glean aligns with their accessibility standards.
A more accessible and standardized design system
In our previous posts, we talked about layering accessibility into product design, including getting keyboard focus right, using semantic HTML, supporting screen readers, and standardizing colors and typography. Underneath all of that is a crucial piece of infrastructure:
our design system
.
Since then, we’ve done a significant upgrade to that foundation. The goal was simple: make the most common building blocks of Glean, like controls, buttons and inputs,
accessible by default,
so every new feature inherits better behavior without requiring extra work.
Standardizing components, not just pages
As part of the migration, we audited every component in our library, including
buttons, inputs, selects, tooltips, popovers, and more
. Over time, we’d been a bit too lenient with component customization. It was easy to override styles or behaviors at the callsite, which led to lots of one‑off variations.
We used the migration as a chance to
reset the baseline
:
Each component now has a
small, opinionated API
: a focused set of props that capture the meaningful, semantic differences (for example, variant, size, or whether something is destructive), rather than every possible styling knob.
Callers can still pass a style, but it’s limited to
layout‑centric tweaks
(like margin) rather than visual styling like colors or typography. This keeps individual screens flexible without letting them drift away from the system.
In Figma, these same components are represented with a matching set of variants and states, so designers and engineers are truly working from the
same component, not just similar ones
.
In practice, that means a component like Input behaves the same way everywhere—same label pattern, same error state, same focus treatment—no matter which team uses it. That consistency reduces cognitive load for users, prevents subtle accessibility regressions, and keeps teams from re‑implementing slightly different patterns that drift out of alignment over time.
Standardizing tokens, not ad‑hoc CSS
We also standardized the
design tokens
that sit underneath those components.
Historically, it was easy to drop in ad‑hoc CSS like margin: {number}px or a hex color directly into a component. Over hundreds of components, those small one‑offs add up. Layouts are harder to change, visual consistency drifts, and checking for contrast or spacing issues becomes more manual.
Today, spacing, color, and typography all go through a
tokenized system
. Since we already use
vanilla‑extract
, we layered
sprinkles
on top to semi‑enforce those tokens in code—similar in spirit to how Tailwind encourages utility‑first, token‑driven styling.
Need spacing? You use a spacing token, not a raw pixel value.
Need a text or background color? You choose from the semantic color tokens that are already vetted for contrast.
Need to adjust layout? You reach for predictable utilities instead of inventing a new pattern.
This alignment between
components + tokens
does two things for accessibility:
It makes it much harder to accidentally ship something with poor contrast or tiny hit‑areas, because the defaults are already
compliant and consistent
.
It makes it easier to
change things centrally
—for example, improving a focus ring or text contrast in one place and having that propagate across the product.
For examples, we used to have multiple ad-hoc versions of the Input component:
// style can accept any properties
<Input id=”A” style={{
height
: 40px, border-color: black,
marginLeft
: 8px}}>
// Input B has very non-standardized height and margin
<Input id=”B” style={{height: 37px, border-color: black, marginLeft: 7px}}>
<Input id=”C” style={{height: 36px, border-color: red, marginRight: 8px}}>
‍
After the migration, this became:
// style now only accepts layout-centric properties like margin,
//position, etc…
// height is converted to a semantic size prop, with standardized
//36/40px or equivalent rem under the hood
// border-color is converted to a semantic borderVariant prop
//that maps to respective color value under the hood
<Input id=”A” size=
"sm"
borderVariant=
"default"
style={{
marginLeft
: 8px}}>
// Update input B to use the nearest standardized height and margin
<Input id=”B” size="sm borderVariant=”default”
style={{marginLeft: 8px}}> <Input id=”C” size="lg" borderVariant="error"
style={{marginRight: 8px}}>
Better screen reader support built in
Previously, getting a component “just right” for screen readers could require a lot of custom work: picking the right HTML elements, wiring up ARIA attributes, and testing in multiple assistive technologies.
Migrating to Base UI gave us a more solid foundation here, and it also unlocked a bunch of screen‑reader wins that now come “for free” with our components:
Lower‑level interactive components expose the right state and roles.
Controls like switches, checkboxes, and radios now automatically surface the appropriate role along with state attributes like aria-label and aria-checked, so assistive technologies can correctly announce what the control is and whether it’s on or off. On the design side, we’ve standardized these controls with clear label, helper text, and error patterns, so teams don’t have to invent new visual treatments or wording for each use case.
Popup‑based components advertise their relationship correctly.
Components that open a popup—like select menus, and autocomplete—now manage attributes such as aria-haspopup and aria-expanded on the trigger, and connect aria-controls so screen readers can tell which popup is being opened.
Listbox‑style widgets keep screen readers in sync with keyboard navigation.
For list‑based components (like menus and selects), keyboard focus and selection are reflected via the correct roles and selection attributes, so screen readers can announce which option is currently highlighted or selected as you move through the list.
Overlays describe themselves as dialogs.
Modals, popovers, and drawers expose the appropriate role="dialog" (or related roles where appropriate) and carry a label that describes their purpose, making it clearer when a new “layer” has appeared and what it’s for.
Important messages are announced via toasts, not hand‑rolled hacks.
We now route important status updates through a toast system that uses aria-live under the hood, rather than ad‑hoc patterns. This makes it much more reliable for screen reader users to hear confirmations, errors, and other key events.
Fewer nested interactive elements.
Our components now render a single, correctly typed interactive element (for example, a button or link), instead of nesting an anchor inside a button (or vice versa) just to get the right styling. This is both cleaner for screen readers and less confusing to navigate.
Tooltips behave better with assistive tech.
Tooltips are notoriously tricky for accessibility due to because they often rely on hover-only behavior, are difficult to expose reliably to screen readers, and require careful keyboard focus management. In Glean, they now show up not just on mouse hover, but also when an element receives keyboard focus—so keyboard and screen reader users get the same hints as mouse users. We also make sure the text inside each tooltip is concise and helpful for screen readers, and avoid repeating information that’s already announced (for example, when an element already has its own accessible label).
In practice, this means that when you use Glean with a screen reader, more of the UI “just works” out of the box: the right roles are exposed, the right relationships are wired up, and important state changes are announced without every feature team having to reinvent the same patterns.
[Example: Tooltip and Menu with screenreader support out of the box]
Better keyboard support and focus management
In part one of this series, we highlighted how important
keyboard navigation and focus
are—not just for screen reader users, but for anyone who prefers or relies on the keyboard.
Our new design system extends that work and make those behaviors even more reliable:
Every interactive element is keyboard‑friendly by default.
Buttons, links, inputs, menus, tabs, and other widgets are all reachable via
Tab/Shift+Tab
and operable via the keyboard. This dramatically reduces the chance that a feature ships with an element you can see, but can’t reach without a mouse.
Dialogs manage focus for you.
Base UI dialogs, drawers, and similar overlays trap focus while they’re open, so Tab stays inside the active surface instead of wandering into the page behind it. We can also configure an initialFocus (where focus lands when the dialog opens) and rely on finalFocus behavior to restore focus back to the original trigger when the dialog closes. That makes multi‑step flows much easier to follow from a keyboard‑only perspective.
Fewer “invisible traps.”
Because all of this behavior is centralized in our components, teams don’t have to remember to set up keyboard and focus handling every time. That reduces the risk of stray elements you can tab into but not out of, or surfaces that open without a clear way to dismiss them via keyboard.
Put simply? Navigating Glean with a keyboard should now feel even more natural and reliable, because
keyboard support and focus management are built into the underlying components
, not bolted on feature by feature.
Compliance
Many customers, especially large enterprises, need confidence that the tools they rely on meet accessibility expectations. For software, that often requires providing a
VPAT
—a standardized document describing how a product supports specific accessibility criteria (like WCAG 2.2 A and AA).
We’re happy to share that Glean now has an
up‑to‑date Accessibility Conformance Report (ACR)
, based on the latest
VPAT® 2.5
format, covering
WCAG 2.0, 2.1, and 2.2
at
Levels A and AA.
If your team needs to review Glean’s accessibility in depth as part of your evaluation, due diligence, you can find it on
our resource page
.
Why this matters going forward
Accessibility is never “done,” but our design system overhaul give us a much stronger foundation:
Every new feature we ship is
more likely to be accessible from day one
, because it’s built on components that already handle a lot of the heavy lifting.
Our design system gives teams a
shared, opinionated starting point
—from colors and typography to complex components—so accessible choices are the default, not a separate checklist.
As we continue to evolve Glean’s look and feel, we’re treating accessibility as a
core design principle
, on the same level as clarity, consistency, and brand.
Customers can
formally evaluate
how Glean meets their accessibility requirements.
We’ll keep iterating on this work, adding new improvements and refining the ones we already have. If you rely on assistive technologies, keyboard navigation, or specific accessibility features and have feedback, we’d love to hear from you
. Feel free to reach out to us at a11y@glean.com
, or connect with your Glean representative to start the conversation.
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
