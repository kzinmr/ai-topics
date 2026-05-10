---
title: "Writing Your First dbt Package | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/writing-first-dbt-package/"
scraped: "2026-05-10T01:29:26.897636+00:00"
lastmod: "2022-11-11"
type: "sitemap"
---

# Writing Your First dbt Package | Hex 

**Source**: [https://hex.tech/blog/writing-first-dbt-package/](https://hex.tech/blog/writing-first-dbt-package/)

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
Writing Your First dbt Package
A comprehensive guide on how to create dbt packages with working code examples, and an open-source repo that you can build from.
Pedram Navid
Data
November 11, 2022
Share:
twitter
linkedin
In this article
Types of dbt packages
When should you write a dbt package, and why?
Basic dbt package concepts
Writing a package
Creating a dbt Package Project
Defining the Raw Data
Consider compatibility issues
Using variables in your models
Local testing
Publishing your package
Wrapping up
Get started for free
If you've spent enough time working with dbt or in the dbt community, you've likely come across dbt packages. Your first interaction with one of these packages might have been the
dbt utils
package or one of the many packages
Fivetran
provides for their data models. But if you're like me, your curiosity is never satisfied, and you soon find yourself wondering how to create your own dbt package. That's what we'll be exploring today.
We'll cover everything from the different types of packages and what you need to build one to more subtle details like how a package works under the hood and the best development workflow.
Types of dbt packages
Two types of dbt packages are generally available:
Internal packages built for use cases within your organization
External packages that are more generalized for broader users across companies.
Internal packages can be beneficial for helping spread the adoption of best practices and for making the lives of your peers better.
For example, some ideas for internal packages might be bespoke tests or custom macros for repetitive tasks such as parsing and cleaning website URLs and emails. Internal packages can take advantage of your business domain context without the overhead of making a solution overly generalized and customizable.
External packages take what you've learned internally and go one step further. They can take many forms, and all you need to do is browse
dbt's package hub
to get a sense of what's possible; from code generation to artifact creation to modeling, there are many ways to build valuable packages for the community. One caveat is that building an external package often means building in a more generalized and abstract way, which can be tricky at times, but hopefully, this guide will help you get started.
When should you write a dbt package, and why?
Not every idea needs a dbt package, and abstractions can be costly. For example, if you're a small team working out of one dbt repo, you might not need a dbt package since you can add macros and tests directly to your project repository.
However, a package might be a good idea if you have multiple projects within your company or you are building something unique that you think is broadly helpful and doesn't involve business-specific logic. When creating a package, you open up your work to the broader community, which can help others facing a similar problem and even encourage contributions from the
dbt community
!
Basic dbt package concepts
At its core, a dbt package is a dbt project that can be installed as a module within another dbt project and referenced. To install a package, you define it in your
packages.yml
file. You can install packages from dbt hub, git, or a local folder on your computer (great for local development).
Copy
# packages.yml
packages:
- package: dbt-labs/snowplow
version: 0.7.0
- git: "https://github.com/dbt-labs/dbt-utils.git"
revision: 0.1.21
- local: /opt/dbt/redshift
Once you run
dbt deps
, dbt will install the packages specified in your
packages.yml
file to your
dbt_packages
directory.
Packages are namespaced, similar to your main dbt project. In your
dbt_project.yml
file, you declare a
name
for your package. You also use that package name to configure your models. The same principle applies to packages you install.
Copy
# dbt_project.yml
name: jaffle_shop
models:
jaffle_shop:
sales:
+schema: sales
my_installed_package:
+schema: my_package
You can extend this logic to variables as well. Variables can be defined globally or tied to a particular package. We'll touch on variables and how they can enhance your packages shortly.
Copy
vars:
my_global_var: 'i_love_cookies'
jaffle_shop:
start_date: '2022-01-01'
my_installed_package:
platforms: ['web', 'mobile']
Writing a package
When learning to write packages, there are a couple of approaches. First, it's helpful to learn from other packages. Fortunately, there are many open-source dbt packages that you can use as a starting point to understand how they're built— take a spin through the
dbt hub
and crack open the hood on a few interesting looking packages!
The second approach is to just dive right in and write a package, which we'll do now. In this example, we'll pretend that we are a software company called Penta that writes data in a standard format to a data warehouse. We want to build a dbt package for our customers so they can take advantage of modeled views based on the raw data our application feeds in.
Creating a dbt Package Project
We'll start by creating a new dbt project.
Copy
dbt init dbt-penta
This command will create a project skeleton. First, we'll update the
dbt_project.yml
file with a barebones schema. Next, we'll also define the schema where we want to write our models by default.
Copy
# dbt_project.yml
name: "dbt_penta"
version: "0.1.0"
config-version: 2
require-dbt-version: [">=1.0.0", "<2.0.0"]
models:
dbt_penta:
+schema: Penta
Defining the Raw Data
Like any good project, we first need to define where our raw data is. Since users may have custom locations for data ingestion, it's best to use a variable to allow users to set their schema and table names. We will be good data citizens and also add some documentation to our tables.
Copy
version: 2
sources:
- name: penta_raw
schema: "{{ var('penta_raw_schema', 'Penta') }}"
database: "{{ var('penta_raw_database', target.database) }}"
tables:
- name: changelog
description: |
This table contains a row for every operation performed by Penta
It includes the result of the operation, as well as any error messages.
columns:
- name: id
description: The id of the change
- name: event
description: The event that caused the change
- name: meta
description: Additional metadata about the change
- name: op_type
description: |
Whether the row was added, changed, or removed relative to the last run.
You can imagine repeating this process for every raw table and dataset's columns.
From here, you would continue to build your package as if it was a typical dbt project. Use the same dbt best practices, such as creating staging tables that reference source tables and making sure to only reference staging tables in your downstream models.
Copy
# stg_penta__changelog.yml
with base as (
select * from {{ source('penta_raw', 'changelog') }}
),
Consider compatibility issues
Recall that your users may use different warehouses, so using the
built-in dbt macros
for cross-database compatible functions is essential. For example, datediff has different arguments depending on the underlying warehouse, so a more compatible approach might look like this:
These macros are native to dbt Core as of v1.2. If you are running dbt Core < v1.2, you'll need to use the
dbt_utils
package to import them. Usage is the same, just use
dbt_utils.datediff
rather than
dbt.datediff
.
Copy
select
{{ dbt.datediff('started_at', 'finished_at', 'second') }} as sync_elapsed_seconds
...
Using variables in your models
You can also use variables to control the behavior of your models. For example, you may wish to allow your users to disable specific models:
In your model, set a model as enabled based on the presence of a variable like this:
Copy
{{ config(
enabled = not var('penta_complex_models_disabled', False)
)
}}
...
Local testing
Once you've built and documented your models, you can test them locally. The easiest way is to use your existing dbt project as a test bed. First, add a local definition in your dbt project (not in your new package).
Copy
# packages.yml
packages:
- local: /Users/pedram/my_cool_packages/packages/penta
Then run
dbt deps
to ensure the local version installs and works as expected. Next, test out your variables to make sure they function too. Finally, if everything looks okay, you're ready for the scariest part, deploying it in the wild! (You'll do great, I promise.)
Publishing your package
The final step is to make your package available to the public. You'll want to create a helpful README that describes what your package does. Here's a
great example of what a README
looks like by the folks at Fivetran.
If you really want to go the extra mile, you can create a Hex project that showcases your dbt package in action for bonus points! Here's an
example of just that
, from the Hightouch team. Get inspired!
Next, create a GitHub repo and add the contents of your package directory. Once you've pushed your repo to GitHub, people can now install it directly from git, similar to how you specified a local folder above:
Copy
packages:
- git: "https://github.com/penta-labs/dbt-penta.git" # git URL
revision: main # tag or branch name
Once pushed, you'll want to test this again to ensure your package still installs. Then, if everything looks good, you're ready to
cut a release
. GitHub makes it straightforward to create a named release, and I'd encourage you to read up on
Semantic Versioning
to help your users understand what changes might break compatibility with previous versions.
If everything looks good, the last step is to release your package on
dbt hub by creating a Pull Request
. Take a look at
this PR
if you need some inspiration; only a few lines of code are needed.
Wrapping up
Once you’ve published your package, it’s time to celebrate. If your package helped solve a problem you face, odds are it’ll help someone else too, so let the community know on
dbt Slack
to encourage adoption and feedback. If you get stuck anywhere, the community is very helpful as well. I hope this was a useful tour of the dbt package ecosystem. You’re well on your way to being a dbt expert.
Share:
twitter
linkedin
See how data teams are using Hex to help their cross-functional teams meet their goals.
Get inspired by more data apps
Request a demo
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
