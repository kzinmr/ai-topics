---
title: "How we beat browser bottlenecks  | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/ui-virtualization/"
scraped: "2026-05-10T01:29:59.156412+00:00"
lastmod: "2025-03-06"
type: "sitemap"
---

# How we beat browser bottlenecks  | Hex 

**Source**: [https://hex.tech/blog/ui-virtualization/](https://hex.tech/blog/ui-virtualization/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
Platform
chevron-down
Products
Agentic notebooks
Powerful, deep-dive analysis without the silos
Conversational self-serve
The best BI tool isn't just a BI tool
semantic-models
Context Studio
Build trust in data with semantic models and AI governance
cli
Hex CLI
Control your analytics from the terminal
Capabilities
Exploratory analysis
Go from quick question to deep analysis to data app in one place
Embedded analytics
Ship secure, customer-facing data experiences
app-builder
Data apps
Build and share interactive dashboards and reporting
Integrations
Out-of-the-box connections and flexible APIs
magic
AI & agents
Agentic workflows to empower your entire team
Solutions
chevron-down
lightbulb
Explore all solutions
One connected system - infinite data answers
By team
solutions-data-leader
Data leader
Focus your team and scale answers
solutions-product
Product
Build your product with data, not gut feels
solutions-marketing
Marketing
Turn scattered data into clear growth opportunities
solutions-sales
Sales
Clear pipeline. Confident forecasts
solutions-customer-success
Customer success
Create a complete view of customer health
Enterprise
Resources
chevron-down
Get started
integrations
Switching to Hex
A guide to getting started on agentic analytics
Templates
Jumpstart with pre-built projects
Hex Foundations
Video series
help
Docs
Resources and product guides
Changelog
Product updates
Inspiration
Blog
From data teams to data teams
Guides
Learn how to do more with data, together
Events
Learn and connect with peers
Customer stories
Empowering the best data teams
Partners
Learn more about our partnerships
save
Download
The Data Leader's Guide to AI Analytics
A practical roadmap for understanding and implementing AI to accelerate your data team and enable true self-service.
Pricing
Log In
Get started
Blog
Beating browser bottlenecks with virtualization
Inside our new approach to virtualization
Reno Bowen & Sam Crank
Engineering
March 6, 2025
Share:
twitter
linkedin
In this article
Performance optimization in browsers
Scrolling by a problem
Reading the tea leaves: building our own virtualized element
Raking in the benefits
Conclusion
Get started for free
Hex is built to be an extremely powerful, flexible tool to build almost anything with data. We’ve architected around the “cell” paradigm first popularized in notebooks, but taken it to an extreme: we have dozens of cells that handle everything from querying data and writing code to building visualizations and configuring UI inputs.
People use these to build some incredible analyses and
data apps
. But it also means that Hex projects can have a
lot
going on, with hundreds of cells with rich UI and interactive visualization all working together. This adds up, and as the Hex product and our user base kept growing, we saw progressively more challenges in having a performant, delightful user experience.
Hex is built to be an extremely powerful, flexible tool where you can build almost anything with data — it also means Hex projects have a lot going on!
Performance optimization in browsers
Of course one solution here is virtualization, trying to only render things visible in the
viewport
, and freeing the client resources to do other stuff.
Virtualization visualized — cells in the viewport are mounted (pictured left; actively rendered), while those outside are virtualized (pictured middle; tracked while out of a user’s sight). Typically this means they are completely omitted from page content until they are in view (pictured right).
Early on, we turned to
React Virtuoso
for virtualization. It’s fantastic for efficiently rendering large lists — why not leverage it for cells? By rendering only visible elements, Virtuoso reduced rendering loads for our biggest notebooks and improved performance.
It worked well in some ways, but with some caveats: scrolling was jittery and and reliably remedying it was a challenge. We used it for only our largest notebooks, where the benefits outweighed the quirks. Smaller notebooks performed fine without Virtuoso, but that was short-lived. We were forced to confront the problem.
Scrolling by a problem
We don’t blame Virtuoso for our scrolling woes. The many ways in which Hex cells were resized — by users, their collaborators, or kernel operations — probably wasn’t doing us any favors. Virtuoso
does
support mixed-size content and resizing, so it was likely solvable. Unfortunately this wasn’t our only problem!
Virtuoso was designed for
lists
.
Huge
lists.
Infinite
lists. Modern Hex notebooks more closely resemble
trees
— hierarchical rather than linear — on the order of hundreds of cells at most and increasingly deeply nested.
Old notebooks (pictured left) didn’t have nesting. Every node was effectively a “leaf” in these flat lists. Newer Hex notebooks (pictured right) contain deeply nested cell types that pose challenges for list virtualization.
Virtuoso supports
some
nesting — at the time of writing, one level deep. This wasn’t going to cut it. Users nested cells within sections inside components, sometimes within more sections. If the viewport happened to scoop up a container with deeply nested content, we might be forced to render all of it at once.
Deeply nested cells were unnecessarily mounted (pictured left). We needed a way to virtualize the leaves of our tree (pictured right).
Virtuoso orchestrates virtualization from a specialized list container that controls the mounting behavior of its contents. Could we place control over mounting behavior in the hands of the cells themselves? Regardless of how deeply nested they were in the tree?
Given 10,000 elements, it would be expensive to delegate that decision. We could take advantage of our domain — notebooks with (at most) hundreds of cells — and reap the benefits.
Reading the tea leaves: building our own virtualized element
Rather than wield a virtualized container to mount and unmount elements from a list, we built a self-contained virtualized element. Any React component — but most importantly cells — should be virtualized or rendered depending on their proximity to the viewport alone. Each cell making this decision independently ensured that nesting wasn’t an issue.
Virtualized cells are replaced with correctly-sized placeholders to retain a skeleton for the notebook to hydrate. If there are 100 cells, there should be 100 virtualized elements — each deciding whether it’s time to mount its contents. By making the size of the notebook more stable, we could offer a better scrolling experience. No magic to fake the height of the page — the elements are there!
We never fully remove any cell from the DOM — we just replace it with a placeholder. As a result, we don’t need to perform any specific magic to guarantee the scroll bar looks correct.
react-intersection-observer
was already in use elsewhere in the codebase and became a building block for the implementation. Mounts needed to be conservative as they’re expensive. Once mounted, we could be liberal with our retention to minimize how often we have to re-mount as users go about their work. To accomplish this, we used two separate observers: mount and unmount.
A visualization of mount and unmount behavior for a notebook of cells.
Distinct observers allow us to independently control the schedule of mounting and unmounting. We trigger mounts for cells that are within 500 pixels of the viewport, and trigger unmounts (and placeholders) for cells that are more than 5,000 pixels of the viewport. The result is a 4,500 pixel window of cells with visible content, through which users can scroll without triggering any mounts or unmounts.
Before hiding content, the intersection observer provides us the actual height which we can then use for placeholders. A simplified version of our implementation expresses all of the above fairly concisely:
Copy
import { useInView } from "react-intersection-observer";

export const VirtualizedElement = ({ children }) => {
  const [contentVisible, setContentVisible] = useState(false);
  const [elementHeight, setElementHeight] = useState();
  const { scrollRoot } = useContext(VirtualizationContext);

  const handleEnter = (inView, intersection) => {
    if(inView) {
      setContentVisible(true);
      setElementHeight(intersection.boundingClientRect.height);
    }
  };
  const { enterRef } = useInView({ scrollRoot, handleEnter, margin: "500px 0" });

  const handleExit = (inView, intersection) => {
    if(!inView) {
      setContentVisible(false);
      setElementHeight(intersection.boundingClientRect.height);
    }
  };
  const { exitRef } = useInView({ scrollRoot, handleExit, margin: "5000px 0" });

  return (
    <div ref={(el) => { enterRef(el); exitRef(el); }}>
      {contentVisible ?
        children :
        <Placeholder height={elementHeight ?? 200} />
      }
    </div>
  );
}
A simplified implementation of
VirtualizedElement.
Raking in the benefits
Our custom-built
VirtualizedElement
offered a tidy, generalized solution designed for our domain — how much did it pay off? Front-end performance improved measurably across the board!
90%
reduction in initial render time for the notebook
33%
reduction in interaction lag (latency of user interactions)
25%
reduction in page load (until network requests and DOM changes are complete)
14%
reduction in render lag (long animation frames observed during scrolling or animations)
10%
reduction in memory usage
Conclusion
Although not appropriate for every use case,
VirtualizedElement
is a great fit for Hex notebooks. Building it offered us direct performance wins as well as an opportunity for our team to deep-dive on our product needs. We’re much better prepared for the road ahead!
If this kind of problem solving interests you,
let us know
!
We’re hiring
.
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.
If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨
Get started for free
👩‍💻
Open roles
Made with
🍩
☕
🥟
🍺
🍰
🔮
🔒
🥖
🍷
🛌
💜
🥨
🛹
🍤
🧄
🍞
🥥
⛳
🤞
🔊
🎧
on
🌎
.
Company
Careers
Customers
Solutions
Media kit
Newsroom
Platform
AI and agents
Agentic notebooks
Conversational self-serve
Context Studio
Hex CLI
Exploratory analysis
Embedded analytics
Data apps
Integrations
Changelog
Resources
Pricing
Switching to Hex
Enterprise
Docs
Blog
Events
Templates
Compare
Trust Center
Status
Connect
Contact sales
Request a demo
Technical support
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
