---
title: "Connecting to and querying Snowflake from Python | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/connecting-snowflake-python/"
scraped: "2026-05-10T01:30:00.209503+00:00"
lastmod: "2022-08-22"
type: "sitemap"
---

# Connecting to and querying Snowflake from Python | Hex 

**Source**: [https://hex.tech/blog/connecting-snowflake-python/](https://hex.tech/blog/connecting-snowflake-python/)

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
Connecting to and querying Snowflake from Python
Four steps to read data from your warehouse directly into Python
Izzy Miller
Further reading
August 22, 2022
Share:
twitter
linkedin
In this article
🐍 Installing the Snowflake Connector for Python
❄️ Authenticating and connecting to Snowflake
🔎 Running a query
🐼 Reading data into a pandas DataFrame
Other methods
Get started for free
Your local Python environment and a massive Snowflake cluster up in the cloud live in very different worlds. Learning to connect them and query data from Snowflake directly into your Python environment or Jupyter notebook means you can get whatever data you need right into the tool where you need it.
There are a few different ways to connect to and query Snowflake from Python. We’ll cover the most common approach in depth, and briefly mention some alternative methods. We'll walk through:
1. Installing the Snowflake Connector for Python (
snowflake-connector-python
)
2. Authenticating and connecting to your Snowflake data warehouse
3. Running a query!
At this point, you’ve successfully connected to and queried Snowflake from Python, and you can write any query you want. Job done? Not quite. We’ll also cover:
4. Reading data from a Snowflake query into a
pandas DataFrame
If you’re running through this live, it should only take you around 10 minutes to go from zero to successful query. Let's get into it!
🐍 Installing the Snowflake Connector for Python
There’s nothing particularly special about the environment needed for this, so if you already know you have a working Python 3.6+ installation, you can skip to the next section,
Installing the snowflake-connector-python package
.
Prepping your Python environment
There are two likely scenarios here for how you're accessing Python:
a. You’re using a
Jupyter
notebook or a
Jupyter notebook alternative
:
You should be pretty much good to go in this case. If you want to make sure, you can run this Python command in a cell and look for a response that's >= 3.6:
Copy
from platform import python_version
print(python_version())
Checking the Python version of a notebook
b. You’re using the terminal / command line / some other Python IDE directly:
Open up your terminal (Terminal app on Mac, command prompt or Powershell on windows, etc.)
Run
python --version
to check what Python version is installed. Mine prints out
Python 3.9.12
, but as long as yours is 3.6 or greater, you’re perfect.
If you get a
command not found: python
error, or your output is
Python 2.x
, try running
python3 --version
. If that works, then you have separate installations of Python 3 and Python 2, and for the rest of this tutorial you’ll need to substitue
python3
for
python
and
pip3
for
pip
in the example commands.
If
python3 --version
also does not work, then you don’t have Python installed. The easiest way to get this working is to
download the official installer
for your machine.
PS: We won’t go deep into the setup of virtual environments here, but if you’re doing a lot of Python work directly at the command line, you’ll want to read up on them.
Virtualenv
works well, and lots of people also like
conda
.
Installing the snowflake-connector-python package
This step is very easy! It only takes one command to install the official Snowflake Python connector. We’ll also install pandas at the same time, since we’ll use it later.
Copy
pip install "snowflake-connector-python[pandas]"
Remember, if you had to run
python3 -- version
earlier to get a working output, you need to run
pip3
instead of
pip
to install the package. And if you’re writing this in a Jupyter notebook, add a
!
before pip to let this command run as a system call.
Copy
!pip install "snowflake-connector-python[pandas]"
This
pip install
command will spin through a bunch of messages and progress bars, and maybe a few warnings about your “pip version” or various package deprecations. This is OK, and unless anything actually says “ERROR” in red, you can probably ignore it.
pip installing the snowflake connector
Now we’re ready to connect to the Snowflake data warehouse.
❄️ Authenticating and connecting to Snowflake
In this next part, we’ll be working with sensitive information: your Snowflake authentication credentials.
You shouldn’t ever store these directly in code.
You never know what you might unthinkingly do with that code— send it to a coworker to help, post it on Stack Overflow with a question, check it into a public git repo...
Storing Snowflake credentials
Instead of directly entering your user and password credentials, we’ll use environment variables. This lets us reference the values from Python without directly storing them in the Python code, entrusting their safekeeping to our computer’s environment.
In a terminal (not a Python session) run the following command, replacing the placeholders with your actual username and password:
Copy
export snowflakeuser=<your_snowflake_username>
export snowflakepass=<your_snowflake_password>
In a Jupyter notebook, you can also choose to set environment variables right from the notebook using the
%env
'magic' command. Make sure to delete the cell after it's run, though, or else the credentials will still be sitting right there! Some online hosted Jupyter notebooks have their own secret variable managers, and you can use those instead.
Copy
%env snowflakeuser=<your_snowflake_username>
%env snowflakepass=<your_snowflake_password>
These commands won't print any kind of output or status response, but they will have saved these sensitive values to your current environment. We’ll learn how to reference them in a little bit.
Opening a connection to Snowflake
Now let’s start working in Python. Open a new Python session, either in the terminal by running
python
/
python3
, or by opening your choice of notebook tool.
We’ll import the packages that we need to work with:
Copy
import pandas as pd
import os
import snowflake.connector
Now we can create a connection to Snowflake. You’ll need a few other pieces of information about your Snowflake instance for this (shown as placeholders below), but these are not sensitive and don’t need to be stored as environment variables.
Copy
ctx = snowflake.connector.connect(
user=os.environ['snowflakeuser'],
password=os.environ['snowflakepass'],
account='your-snowflake-account-identifier-here',
warehouse='your-warehouse-name',
role='your-role-name',
database='your-database-name',
schema ='your-default-schema-name'
)
cs = ctx.cursor()
Not sure where to find this information?
Your account identifier is everything between
https://
and
.snowflakecomputing.com
in your Snowflake web URL. If your URL is
https://ab12345.us-east-2.aws.snowflakecomputing.com
, then your account identifier is
ab12345.us-east-2.aws
.
You can find data warehouse, role, database, and schema information from the
Context
menu in a new Snowflake
worksheet
.
Setting environment variables and opening a connection
These commands establish a connection and open a “cursor” to your Snowflake data warehouse. Quick dictionary interlude:
ctx
stands for “context”, a common term used when accessing databases in Python. It refers to an object that holds “state” (aka context) about the current status of the database connection: if it’s still authenticated, elapsed time since it was created, etc.
cs
stands for "cursor", the standard terminology for an object used to actually access records in a database. Kind of like how you can ‘point’ at things on the screen with your mouse cursor, this virtual cursor acts as a pointer to rows in your database and lets you point at and select them.
Also, notice how we’re using the
os.environ['snowflakepass']
syntax to reference the environment variable containing our password. This means if a bad actor gets their hands on this code, they still won’t have anything sensitive.
🔎 Running a query
If those commands ran successfully, we’re all authenticated and ready to query!
First, we’ll run a simple test query just to establish that our connection worked properly.
Copy
sql = "select 1"
cs.execute(sql)
first_row = cs.fetchone()
print(first_row[0])
Running a simple query in Snowflake with Python
If that returned
1
, then congratulations—
you’ve just run a query against your Snowflake data warehouse!
You can replace
"select 1"
with any SQL query you want to run, and the
cs
object will contain the results.
Now that you're running a real query, you probably want to fetch more than one row from the results. In addition to
fetchone()
, the cursor object has a
fetchall()
method that helps iterate over the entire result set:
Copy
results = cs.fetchall()
for row in results:
print('%s, %s' % (row[0], row[1]))
But this isn’t the best way to work with lots of data— you don’t just want to look at the results, you want to do things with them! You could manually replace that
print()
line with something that dumps all the rows into a data structure you can use… or, as we'll explain now, you can use the
fetch_pandas_all()
method to do all that automatically!
For more information and other ways to fetch results from a cursor,
dive into the official Snowflake docs
.
🐼 Reading data into a pandas DataFrame
Since most data analytics and data science projects use
pandas
to crunch data, what we really want is to get results from a Snowflake query into a pandas DataFrame. Luckily, the library we’re using makes that really easy to do.
Let’s use a real query instead of that
SELECT 1
, so we have some more data to work with. I’ve got a demo dataset with a table called
DIM_CUSTOMERS
, in a DB called
ANALYTICS
. You won't be able to run this query if you copy/paste it, so you'll want to replace it with a query against your own data.
If you get an error like
Database 'your-db-name' does not exist or not authorized
when running a query, double-check your
ctx
config from earlier and make sure it includes a role that is authorized to access the database and schema you’re querying. Remember, if you create a new context, you then need to re-run the command to establish a new cursor.
Copy
sql = 'SELECT * FROM "ANALYTICS"."PROD"."DIM_CUSTOMERS"'
cs.execute(sql)
df = cs.fetch_pandas_all()
This will assign the results of your query to a pandas DataFrame called
df
. You can print a sample of the results to make sure it worked:
Copy
df.head()
Reading results to a pandas dataframe
And you’re off to the races! You can use this method to execute any Snowflake query and read the results directly into a pandas DataFrame.
Once you've got data in this format, you can use any pandas functions or libraries from the greater Python ecosystem on your data, jumping into a complex statistical analysis, machine learning, geospatial analysis, or even modifying and
writing data back
to your data warehouse.
Other methods
Part of the joy (or chaos) of Python is that there’s always more than one way to do something. There’s lots of other options for connecting to Snowflake, but here are the most relevant alternatives:
SQLAlchemy
: SQLAlchemy is a generic database toolkit for connecting to any database from Python. It’s not specifically tailored to Snowflake, but works with it just fine. Check out
their docs
for detailed instructions on connecting SQLAlchemy to Python.
pandas.read_sql
: This isn’t a replacement for the entire process, since you still have to create a Snowflake connection, but instead of running your SQL with a cursor and then using
fetch_pandas_all
, you could do it all from pandas directly. In my anecdotal experience, this is less performant than the other methods, though it still works fine.
Copy
df = pd.read_sql('SELECT * FROM "ANALYTICS"."PROD"."DIM_CUSTOMERS"', ctx)
Using pd.read_sql
And if you use
Hex
(hint: you’re on our website right now!) you don’t have to deal with any of these contexts and cursors, and can just write SQL in a
SQL cell
and get the results as a DataFrame.
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.

If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨ Get started for free
👩‍💻 Open roles
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
