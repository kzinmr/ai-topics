---
title: "Snowpark + Hex Ask Me Anything | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/snowpark-ama/"
scraped: "2026-05-10T01:29:05.489871+00:00"
lastmod: "2023-09-29"
type: "sitemap"
---

# Snowpark + Hex Ask Me Anything | Hex 

**Source**: [https://hex.tech/blog/snowpark-ama/](https://hex.tech/blog/snowpark-ama/)

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
Snowpark + Hex Ask Me Anything
Highlighted questions and answers from a live joint Snowflake and Hex session
Armin Efendic
Product
September 29, 2023
Share:
twitter
linkedin
Hex recently joined Snowflake for an Ask Me Anything (AMA) session about Snowpark for Python, with a particular focus on Feature Engineering and Model Training for AI and ML.
Like any great AMA session, we got great questions!  To hear all of the questions that were asked and answered, register and
watch Snowflake’s recording of the event
. Here’s a short selection of questions from the live event, along with links to further information, documentation, and resources.
Q: I would like to better understand how to initiate a Snowpark instance in Hex
Answer: Use our easy button to quickly start a Snowpark session:
For more information, please refer to our
documentation
.
Q: To import a package, do I have to have that package available in Snowpark? Or can I have a separate set of packages or custom packages that are installed in Hex's runtime?
Answer: Hex comes pre-installed with many different packages, including all the packages required for Snowpark and Snowpark ML. If you are registering a User Defined (Table) Function (UDxF) or a Stored Procedure (Sproc) in Snowflake, you can view the packages available
inside
of said UDxF or Sproc
here
. A lot of those packages are already installed in Hex, but it is best practice to ensure you have matching versions. This means that if you are using a package when registering a UDxF or Sproc, it is best to have the same version of that package in Hex. You can simply check this from a python cell using pip:
Copy
!pip show snowflake-snowpark-python
When it comes to custom packages or packages that are not available in the Snowflake Anaconda channel, check out
Introducing: Simple workflow for using Python Packages in Snowpark
. To add packages into Hex you can simply run:
Copy
!pip install <my_package_name>
Q: What is it that Hex offers that is not in Jupyter?
Answer: We have so many benefits over Jupyter. Check them all out in this blog post that explains why
Hex + Snowflake is a powerful alternative to Jupyter
.  Our Snowpark integration is unique to Hex– there is no comparable offering in Jupyter.  Being able to switch between different cells is a Hex creation, that’s only available in Hex. Other notable benefits of Hex include:
Easy of setup, no more management of environments and packaged dependencies
Direct integration with Snowflake (push down all of your compute!)
Collaboration, version control, and easy share interactive data apps
Hex cells are reactive meaning there are no more state issues to deal with
Hex Magic provides code generations, explanation, and debugging to accelerate your workflows.
Q: Hi, Is Hex a 3rd party tool or Snowflake’s own tool?
Answer: Hex, an independent software company, is Snowflake’s notebook of choice.  We’re an Elite Technology Partner of Snowflake, which means we’ve been validated by their team and have been recognized for great product collaboration. Read more about
our partnership with Snowflake
.
Q: Is there a native way to integrate Hex/Snowpark into CI/CD workflows?
Answer: Yes, Hex provides a
git integration
which can then be used in a CI/CD workflow. We also provide
native versioning
, similar to google docs, if that is more your speed!
If you are looking for orchestration and scheduling of notebooks you can utilize Hex’s built in
scheduler
, our
integration with orchestration tools
such as Airflow and Dagster, and leverage the
Hex API
for more flexibility.
Q: What's the best way to get started with these great features? Does this run faster than running a local Jupyter notebook? What would be your recommendations for converting an existing Jupyter notebook that's run locally to using this functionality?
Great questions! The easiest way to get started with Snowpark is within a Hex notebook, thanks to our
easy button
. If you are currently working with a Jupyter notebook, you can easily
import a Juypter notebook into Hex
. Best of all, Hex comes pre-installed with all the packages you need for working with Snowpark and Snowpark ML.
One thing to remember is when using Snowpark, all of the queries are being run inside of Snowflake. This means you don't need to bring any data into your kernel's memory. You’ll appreciate this when working with large datasets! Think about all those times that a query has exceeded the memory limits of your notebook… let’s not even get into leaving a query to run overnight only for the memory to be taken up.
Give Hex a try
and see how easy it is to use SQL, Python, and Visual cells all while leveraging Snowpark!
Q: When is compute pushed down to Snowflake and when is it run within Hex? Is it always best to try to push as much compute demand as possible down to Snowflake using Snowpark? How does this compare to a notebook using Pyspark for similar purposes?
Answer: When you are using Snowpark in Hex all the compute is pushed down into Snowflake. The beauty of our integration is we allow users to work in a SQL, Python, or visual cell and have all the compute still be pushed down to Snowflake. This is very advantageous when it comes to those large data workloads as you can easily scale your computing power via Snowflake warehouses. When working with smaller datasets that data can be brought into Hex memory and computed by the Hex kernel. When it is best to use Snowpark vs in-memory computation in Hex will be on a case by case basis. Predominantly, this will be determined by the size of your data and the need for scalability.
When it comes to using PySpark there are some similarities and differences. It is similar in the sense that you are leveraging distributed compute via your Spark cluster. With Snowpark you leverage Snowflake’s distributed compute architecture. The idea for both is that PySpark and Snowpark are an abstraction to the user so they do not need to worry about how to best utilize the distributed compute. This abstraction takes shape in the form of a Spark Dataframe and Snowpark Dataframe respectively. Infact, the syntax of PySpark and Snowpark is nearly identical. If you are comfortable with one you will be comfortable with the other.
With that said, if you use Snowpark in Hex you get the added benefits the easy button (mentioned above) and push down while using a native SQL, Python, or Chart cell all while working with a Snowpark dataframe. This is not something that is not available to you with a Spark dataframe.
Q: I presume you have your own Virtual Warehouse for ML purposes to do heavy lifting. Right?
Answer: You can leverage any warehouse while utilizing Snowpark and it's very simple to scale up or down with a simple snowpark command session.use_warehouse('XLarge')  When it comes to memory intensive operations, like some ML training, you can leverage a Snowpark Optimized Warehouse. Switching to that warehouse is the same as the command above!
Q: What feature engineering does Snowpark offer for us?
Answer: Snowpark ML is effectively a wrapper for scikit-learn. You can find the currently available preprocessing methods in
snowflake.ml.modeling.preprocessing
. When it comes to performing feature engineering tasks that are not provided in Snowpark ML you can leverage a stored procedure with Snowpark.
Q: What is the difference between Hex magic and Snowpark?
Answer: Hex Magic is Hex's AI assistant. It can generate, debug, and explain code for you. Snowpark is Snowflake’s creation that allows users to leverage Snowflake compute while working in languages like Python, Java, and Scala. You will hear
Snowpark for Python
which is the python implementation of Snowpark
Q: How do we think about model versioning, testing, and experiment / hyperparameter tuning testing/tracking in snowflake ml?
Answer: Great question! Snowflake has a Model Registry that is currently in Private Preview (PrPr) at the time of writing, which addresses some of the questions you’ve asked. In terms of hyperparameter tuning you can
leverage a UDTF
to cross train models in parallel. This is certainly an advanced topic and I would first recommend getting comfortable with Snowpark ML.
Share:
twitter
linkedin
Love Snowflake? Us too! Try Snowpark for Python in Hex and let us know what you think.
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
