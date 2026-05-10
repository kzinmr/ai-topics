---
title: "Building ML Models In Minutes With Hex and Snowflake ML Functions | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/snowflake-ml-functions-hex-tutorial/"
scraped: "2026-05-10T01:28:57.007428+00:00"
lastmod: "2024-05-28"
type: "sitemap"
---

# Building ML Models In Minutes With Hex and Snowflake ML Functions | Hex 

**Source**: [https://hex.tech/blog/snowflake-ml-functions-hex-tutorial/](https://hex.tech/blog/snowflake-ml-functions-hex-tutorial/)

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
Building ML Models In Minutes With Hex and Snowflake ML Functions
Build machine learning models with SQL
Armin Efendic
Product
May 28, 2024
Share:
twitter
linkedin
Machine learning has drastically changed in the past year with the rise of LLMs. Generative AI has changed the landscape, but traditional machine learning has been and still is very prevalent. However, a common problem still persists — the steep learning curve is too high for large adoption of ML models within enterprises. Snowflake’s answer to this problem are their
Snowflake ML functions
. I will walk through how to implement ML models using only SQL!
Snowflake ML Functions
Snowflake ML functions
are a new way to train and call ML models in Snowflake. They are easy of use, provide security, and are accessible to anyone that can write basic SQL! Problems that required advanced knowledge of Python, machine learning libraries and best practices can now be solved with a few lines of SnowSQL. To date, there are four ML functions available:
Anomaly Detection
Classification
Contribution Explorer
Forecasting
We will review how to use the forecasting function.
Hex + Snowflake ML Functions
Taking advantage of Snowflake ML functions is made easy in Hex. All that is required is a
Snowflake connection
and a SQL cell. In Hex, the ML functions will return results as a
Pandas dataframe
. As a SQL user, understanding this is not important but it provides the flexibility to quickly work with Python. Every Hex project also comes with pre-installed libraries so you can expand on your analysis with ease.
Model Training With Snowflake ML Functions:
The ML Functions allow us to train models using only SQL. In the images below, I am using a dataset that contains US population information such as birth rates, growth rates, migration rates, and more. I want to forecast population growth over time by using these columns. I simply call the
SNOWFLAKE.ML.FORECAST()
against my dataset called
usa_population
and my model is trained!
In the code I do not need to specify columns like birth rates and migration rates to the model. I only need to specify the
TIMESTAMP_COLNAME
and
TARGET_COLNAME
. The Forecast function automatically will use the columns for training The Forecast function will even exclude
NULL
values. You can learn more about the
forecast function
in Snowflake’s documentation.
For my
INPUT_DATA
I am using a system function called
SYSTEM$QUERY_REFERENCE()
. This is a simple trick that runs the query specified when I run the code above. This avoids me from having to create a separate table or view just to ensure that my timestamp column is of
TIMESTAMP_NTZ
.
Finally, I am ensuring that my timestamp column is of
TIMESTAMP_NTZ
(no time zone) as this is a requirement for the forecast model with the code
YEAR::TIMESTAMP_NTZ AS YEAR_NTZ
.
Model Inference With Snowflake ML Functions:
Now that our model is trained, let’s try it out! We can forecast population growth by simply calling the model we created.
All I need to do is specify the timestamp column,
TIMESTAMP_COLNAME = ‘YEAR_NTZ’
and the model will predict future values. Notice that I am using the
SYSTEM$QUERY_REFERENCE()
again to avoid having to create a view or table.
Partitioned Model Training
Only the forecasted data above is for the US. In real world applications, it is very likely that you have to perform partitioned model training. Meaning, you have data that can not be trained with one model. For example, imagine that our dataset had many different countries instead of just the US.
Traditionally, we would need to partition our data or rather create new datasets for each country and then train individual models. Each country has specific birth rates, immigration rates, etc. and that must be accounted for. The more performant way to handle this, is to partition the model training so that the models run in parallel. But, this is an advanced technique. With Snowflake ML functions partitioning is only one additional line of SQL code:
The
SERIES_COLNAME
is used to specify the column I want to partition on. In our dataset, the
NAME
column contains the names of the various countries; I can simply add
SERIES_COLNAME => ‘NAME’
and the model will partition on each unique country in the dataset.
I am able to forecast on numerous country names with only one additional line of SQL. The final result is individually forecasted values for all the countries in my table:
Conclusion
To review all the code, how I got this dataset, prepared the data, and made the predictions check out
Building ML Models In Minutes With Snowflake ML Functions and Hex
and get a copy to run the code in your own Hex environment. These models have been trained using only SQL for quick and easy model development. Whether you are an ML engineer looking for quick base models that you optimize or a SQL analyst looking to upskill, you can leverage Snowflake ML models and the integration with Hex make it effortless.
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
