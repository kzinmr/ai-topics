---
title: "Using SQL for Data Analysis | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/sql-for-data-analysis/"
scraped: "2026-05-10T01:29:52.753751+00:00"
lastmod: "2023-07-12"
type: "sitemap"
---

# Using SQL for Data Analysis | Hex 

**Source**: [https://hex.tech/blog/sql-for-data-analysis/](https://hex.tech/blog/sql-for-data-analysis/)

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
Using SQL for data analysis
SQL is for more than just reading and writing to your database. Understanding the core components of this language lets you be much more efficient with your data analysis.
Andrew Tate
Further reading
July 12, 2023
Share:
twitter
linkedin
In this article
The foundations of data analysis with SQL
More complex SQL for data analysis
Stored Procedures
Better performance from your data analysis using SQL
Get started for free
If you’re asked to do any data analysis, you immediately power up a Jupyter notebook and start flexing your .ipynb muscles, right? Data analysis means Python and it means R. The only SQL you need is for
reading the data
out of the database. Then you turn to a proper analysis language.
But SQL is insanely powerful. It’s much, much more than SELECT *. In fact, that’s the worst part of it! The power of SQL means you can do a ton of data analysis basically within your database. SQL is designed to manage, manipulate, and query data efficiently. It's particularly adept at handling large datasets quickly and can perform complex aggregations, joins, and calculations on the fly.
It is designed to do these tasks on the database server itself, reducing the amount of data that needs to be pulled over the network and into memory, as you’d see with Python and R.
So let’s go through how you might use SQL for data analysis. We’ll get through:
The basic manipulations and queries that you use as the building blocks of analysis in SQL
The more sophisticated techniques you can use to aggregate and calculate data
How to build stored procedures to quickly implement data analyses within databases
How to optimize and tune your queries and performance to reduce overhead and costs.
Let’s get to it.
The foundations of data analysis with SQL
Let’s say we’re a data analyst working for a SaaS company doing some data modeling. We want to use SQL with our datasets to perform some data aggregation and data mining.
SQL is a great option for this task because:
One of the advantages of SQL is its simplicity and the ease with which you can chain together its functions to create more complex queries. SQL has a relatively small set of core commands: SELECT, FROM, WHERE, GROUP BY, HAVING, ORDER BY, and JOIN, among others. These commands can be combined and nested in various ways to extract, filter, sort, and analyze data.
But SQL also includes a wide range of additional functions and capabilities, including mathematical and statistical functions, string manipulation functions, date and time functions, and advanced features like subqueries, window functions, and stored procedures.
So, the simplicity and consistency of SQL's core commands make it easy to get started and to understand what a query is doing. At the same time, its powerful set of functions and features enables complex and sophisticated data analysis and data modeling.
Sequel or ess-que-ell? Almost everyone is going to go with pronouncing it sequel, just for ease, but it should be ess-que-ell. When the language was first introduced in the 1970s it was called SEQUEL, but a British engineering company had the trademark on that name, so the query language became SQL. So whether you are doing ess-que-ell data analysis, or SQL data analysis, or sequel data analysis is up to you!
Before we can get started, we’ll need some data. Because of the way databases and SQL work, we’ll create two tables for these examples,
subscriptions
and
users
:
The
subscriptions
table looks like this:
And the
users
table looks like this:
You can generate data like this with
Mockaroo
, a great option for generating large amounts of test data for database or API testing.
Let’s go through those simple commands first.
SELECT
Pretty much the most basic SQL command. This command is used to select data from a database. You can select one or multiple columns.
Copy
SELECT user_id, sign_up_date
FROM users;
Output:
WHERE
The WHERE clause is used to filter records based on specific conditions. Here we want to just get a single user from our users table, the user with user_id = 1:
Copy
SELECT *
FROM users
WHERE user_id = 1;
Output:
GROUP BY
The above two commands just let you select the raw data from the tables. However, the GROUP BY statement groups rows that have the same values in specified columns into aggregated data. Here we’re counting the number of subscriptions we have for each of our two plans:
Copy
SELECT plan_id, COUNT(*) as count
FROM subscriptions
GROUP BY plan_id;
Output:
HAVING
The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions. So we can aggregate with GROUP BY then select with HAVING (in this case finding the plan with more than 2 members):
Copy
SELECT plan_id, COUNT(*) as count
FROM subscriptions
GROUP BY plan_id
HAVING COUNT(*) > 2;
Output:
ORDER BY
The ORDER BY keyword is used to sort the result-set in ascending or descending order. Let’s see who signed up most recently:
Copy
SELECT *
FROM users
ORDER BY sign_up_date DESC;
Output:
JOIN
A JOIN clause is used to combine rows from two or more tables, based on a related column between them. JOINs are one of the most common needs in SQL and where the benefits of SQL come into play as you don’t have to pull all the data from different tables as you would with Python and R. Here we’ll JOIN our two tables on the user_id field:
Copy
SELECT *
FROM users
JOIN subscriptions ON users.user_id = subscriptions.user_id;
Output:
Subquery
A Subquery or Inner query or Nested query is a query within another SQL query and embedded within the WHERE clause. Subqueries are used to return data that will be used in the main query as a condition to further restrict the data to be retrieved. This one it's shows the subscriptions that have a price higher than the average subscription price.
Copy
SELECT *
FROM subscriptions
WHERE price > (SELECT AVG(price) FROM subscriptions);
Output:
CASE
The CASE statement goes through conditions and returns a value when the first condition is met. It works kinda like an if/else statement in other languages. Once a condition is true, it will stop reading and return the result. If no conditions are true, it returns the value in the ELSE clause. We can use it to categorize our subscriptions:
Copy
SELECT user_id,
price,
CASE
WHEN price >= 150 THEN 'High'
WHEN price >= 100 THEN 'Medium'
ELSE 'Low'
END as price_category
FROM subscriptions;
Output:
And with that, you genuinely have almost everything you need to start generating extremely powerful queries for data analysis with SQL.
More complex SQL for data analysis
With the above tools, you can do a huge amount, especially when it comes to just data wrangling and data mining. But most of them aren’t doing real calculations.
You can use those functions get SQL to do the heavy lifting for data manipulation before going into more detailed analysis in Python or R. But SQL can also do more complex analysis. Let’s go through some of the more sophisticated techniques data analysts can use with SQL
Window functions
Window functions perform a calculation across a set of table rows that are somehow related to the current row.
This is comparable to the type of calculation that can be done with an aggregate function. But unlike regular aggregate functions, the use of a window function does not cause rows to become grouped into a single output row — the rows retain their separate identities.
Copy
SELECT user_id,
start_date,
price,
SUM(price) OVER (PARTITION BY user_id ORDER BY start_date) as running_total
FROM subscriptions;
Output:
PARTITION_BY
The PARTITION BY clause is used in conjunction with window functions in SQL. This clause divides the result set produced by the FROM clause into partitions to which the window function is applied.
Let's say we want to calculate the cumulative sum of the subscription prices for each user over time. This could help us see how much each user has spent in total at any given point in time. Let's calculate the cumulative sum of the subscription prices for each user:
Copy
SELECT user_id,
start_date,
price,
SUM(price) OVER (PARTITION BY user_id ORDER BY start_date) as cumulative_price
FROM subscriptions;
Output:
Here, the cumulative_price column represents the cumulative sum of the subscription prices for each user over time.
The SUM(price) OVER (PARTITION BY user_id ORDER BY start_date) part of the query calculates this cumulative sum by summing the price for each partition of user_id, ordered by start_date. This shows how the PARTITION BY clause can be used to perform calculations within subsets of your data.
Common Table Expressions (CTEs)
A common table expression (CTE) provides the significant advantage of being able to reference itself, thereby creating a recursive CTE.
Copy
WITH monthly_revenue AS (
SELECT DATE_TRUNC('month', start_date) as month,
SUM(price) as revenue
FROM subscriptions
GROUP BY month
)
SELECT *
FROM monthly_revenue
ORDER BY month;
Output (assuming we only had data for January and February 2023):
Correlated Subqueries
A correlated subquery is a subquery that uses values from the outer query. In other words, it depends on the outer query.
Copy
SELECT u.user_id,
(SELECT COUNT(*)
FROM subscriptions s
WHERE s.user_id = u.user_id) as subscription_count
FROM users u;
Output:
PIVOT
Pivoting is a common technique in data processing, it transforms unique values from one column into multiple columns in the output, and performs aggregations where they are required on any remaining column values.
Not all databases support PIVOT. PostgreSQL, which we're using here, doesn't have a built-in PIVOT function, but we can create a pivot table using a combination of SQL commands.
Copy
SELECT
user_id,
COALESCE(SUM(price FILTER (WHERE DATE_TRUNC('month', start_date) = '2023-01-01')), 0) as jan_revenue,
COALESCE(SUM(price FILTER (WHERE DATE_TRUNC('month', start_date) = '2023-02-01')), 0) as feb_revenue
FROM subscriptions
GROUP BY user_id;
Output:
These examples demonstrate some of the more complex techniques you can use with SQL. They can be combined and modified in a multitude of ways to perform intricate data analysis tasks.
With all that in place, let’s start using some of these techniques together in a way that a data analyst tasked with understanding revenue, growth, and churn might use them.
Revenue Analysis
Firstly, let's tackle the revenue analysis. For example, we want to find out the total revenue in January 2023.
Copy
SELECT SUM(price) as total_revenue
FROM subscriptions
WHERE start_date >= '2023-01-01' AND start_date < '2023-02-01';
This SQL statement is doing a sum aggregation on the price column of the subscriptions that started in January 2023.
Growth Analysis
Let's do some growth analysis. We want to know the growth of new users per month.
Copy
SELECT DATE_TRUNC('month', sign_up_date) as month, COUNT(*) as new_users
FROM users
GROUP BY month
ORDER BY month;
This statement uses the `DATE_TRUNC` function to group the users by the month they signed up in, then counts how many users there are in each group.
Churn Analysis
Churn analysis is slightly more complicated. For this example, let's define churn as a user not renewing their subscription at the end of a period.
Copy
WITH user_months AS (
SELECT
user_id,
DATE_TRUNC('month', start_date) as start_month,
DATE_TRUNC('month', end_date) as end_month
FROM subscriptions
),
churned_users AS (
SELECT
user_id,
COALESCE(LAG(end_month) OVER (PARTITION BY user_id ORDER BY end_month), start_month) + INTERVAL '1 month' as churn_month
FROM user_months
WHERE end_month IS NOT NULL
)
SELECT
churn_month,
COUNT(DISTINCT user_id) as churned_users
FROM churned_users
GROUP BY churn_month
ORDER BY churn_month;
This script uses a couple of advanced SQL concepts:
Firstly, we create a Common Table Expression (CTE) called user_months to select each user's start_month and end_month from the subscriptions table.
Then we create a second CTE churned_users where we use the LAG function to look at the previous end_month for each user. If there is no previousend_month, it means this is the user's first subscription, so we use the start_month instead. This CTE gives us the month each user churned.
Finally, we select the churn_month and count the number of distinct users who churned in each month.
From this, we might see:
This is just the start. Given the way you can chain SQL commands together and the amount of ways to aggregate or group data, there are a ton of possibilities for data analysis in SQL.
Stored Procedures
Obviously you aren’t writing your Python code from scratch each time. You save it.
The same goes for SQL. Stored procedures are prepared SQL code that you can save and reuse over and over again.
If there is a complex query or a piece of script that you find yourself using often, you can save it as a stored procedure, and then call it to execute it whenever you need it. This can be particularly useful for complex business processes that are run regularly, such as monthly reporting, data cleansing, or data insertion processes.
Some advantages of using stored procedures are:
Performance
: Stored procedures are parsed and optimized as soon as they are created. When you call a stored procedure for the second time, it runs faster because the database server has a cached plan for executing the query.
Security
: Stored procedures provide an extra layer of security, as you can grant permissions to users to execute the stored procedure, instead of giving permissions on the underlying tables.
Reduced network traffic
: If you have a complex query that involves multiple round-trips to the server, encapsulating it in a stored procedure would result in only one trip, reducing network traffic.
Maintenance
: You can write a stored procedure once, and call it in any program where you need to perform that function. If there are changes required, you would only need to update the stored procedure and not all the individual SQL statements.
Stored procedures help to encapsulate and optimize logic that is regularly applied to your data. For our SaaS company dataset, we might have stored procedures to calculate the running total of subscription prices per user:
Copy
CREATE OR REPLACE PROCEDURE calculate_running_total(IN in_user_id INT)
LANGUAGE plpgsql
AS $$
BEGIN
RETURN QUERY
SELECT user_id,
start_date,
price,
SUM(price) OVER (PARTITION BY user_id ORDER BY start_date) as running_total
FROM subscriptions
WHERE user_id = in_user_id;
END; $$
The stored procedure is mostly just SQL, with some commands around it. Let’s go through those:
CREATE OR REPLACE PROCEDURE calculate_running_total(IN in_user_id INT)
: This line is creating a new stored procedure named calculate_running_total. The OR REPLACE part means that if a procedure with the same name already exists, it should be replaced with this new procedure. IN in_user_id INT is defining an input parameter named in_user_id of type INT for the procedure.
LANGUAGE plpgsql
: This specifies that the procedure will be written in the PL/pgSQL language, which is a procedural language for the PostgreSQL database system. The exact syntax to create and call stored procedures can vary between different SQL database systems.
AS $$
: This starts the definition of the procedure. In PostgreSQL, you can use $$ to denote the start and end of a function body.
BEGIN
: This keyword marks the beginning of the body of the procedure.
RETURN QUERY
: This tells PostgreSQL that the procedure will return the result of a query.
END
;: This keyword marks the end of the body of the procedure.
$$:
This marks the end of the definition of the procedure.
To call this stored procedure for a specific user (for example, user with ID 1), you would use the `CALL` statement:
CALL calculate_running_total(1);
Which would return:
Here’s an example of a stored procedure to get the monthly revenue:
Copy
CREATE OR REPLACE PROCEDURE get_monthly_revenue()
LANGUAGE plpgsql
AS $$
BEGIN
RETURN QUERY
WITH monthly_revenue AS (
SELECT DATE_TRUNC('month', start_date) as month,
SUM(price) as revenue
FROM subscriptions
GROUP BY month
)
SELECT *
FROM monthly_revenue
ORDER BY month;
END; $$
To call this stored procedure, you would use the `CALL` statement:
Copy
CALL get_monthly_revenue();
Query Optimization
Query optimization is a critical aspect of database management and usage. An unoptimized query can consume excessive resources and return results slowly, impacting both server performance and user experience.
Let’s take a look at some of the queries we’ve written so far and how we might optimize them.
Reducing the number of columns in the SELECT clause
If you're only interested in the number of subscriptions per user, there's no need to select all columns from the subscriptions table:
Copy
SELECT u.user_id,
(SELECT COUNT(*)
FROM subscriptions s
WHERE s.user_id = u.user_id) as subscription_count
FROM users u;
In this case, the subquery only counts the rows in the `subscriptions` table where user_id matches the user_id from the outer query, so there's no need to fetch the full row data.
Using a WHERE clause to limit the number of rows returned
In our earlier example for the running total per user, if you're only interested in the running total for a specific user, you can add a WHERE clause to limit the number of rows returned:
Copy
SELECT user_id,
start_date,
price,
SUM(price) OVER (PARTITION BY user_id ORDER BY start_date) as running_total
FROM subscriptions
WHERE user_id = 1;
Using appropriate indexes to speed up window function queries
In our previous example:
Copy
SELECT user_id,
start_date,
price,
SUM(price) OVER (PARTITION BY user_id ORDER BY start_date) as running_total
FROM subscriptions;
An index on user_id and start_date would likely improve performance. (Though too many indexes can slow down INSERT, UPDATE, DELETE operations, so
horses for courses
).
CTEs
We’ve used CTEs above and they are primarily a way to make your SQL cleaner and more readable. But, in some cases, they can be used to force the database to evaluate subqueries in a specific order, which can be used to your advantage if you understand the data and database system well.
Correlated Subqueries
Correlated subqueries can often be slow because they require the database to execute the subquery individually for each row in the outer query. If possible, it's often faster to rewrite a correlated subquery as a JOIN:
Copy
SELECT u.user_id, COUNT(s.user_id) as subscription_count
FROM users u
LEFT JOIN subscriptions s ON u.user_id = s.user_id
GROUP BY u.user_id;
This query returns the same result as the correlated subquery example but may perform better, especially on large datasets, because it eliminates the need for a separate subquery for each user.
Here's some overall tips to optimize your SQL queries:
Use Indexes
: Indexes significantly speed up data retrieval. They work similarly to an index in a book (that's why it's called an "index"). However, they can also slow down data-insertion and updating, so they are a trade-off.
Avoid SELECT *
: When possible, avoid using `SELECT *` in your queries. Specify the exact fields you need to reduce the amount of data that needs to be retrieved and sent.
Use WHERE Instead of HAVING
: When filtering data, use a `WHERE` clause instead of `HAVING` when possible. `WHERE` filters before data is grouped, while `HAVING` filters after, making `WHERE` more efficient.
Use LIMIT
: If you only need a certain number of rows, use the `LIMIT` clause to reduce the amount of data that needs to be retrieved.
Minimize Subqueries
: Subqueries can often be replaced with a `JOIN`, which is usually more efficient.
Use EXPLAIN
: Most SQL databases have an `EXPLAIN` statement that can provide insight into how the SQL server plans to execute the query. This can help you identify parts of your query that are inefficient.
Avoid Complex Calculations in WHERE Clause
: Calculations in a `WHERE` clause can prevent the use of indexes and slow down the query. If possible, precalculate values and store them in the database.
Normalize Your Database
: Normalization reduces data redundancy and improves data integrity, however, in some complex query cases, denormalization might help to reduce join operations and improve query performance.
Use UNION ALL Instead of UNION
: If you don't care about removing duplicate rows, `UNION ALL` is faster than `UNION`.
Query optimization is a subset of what might be called performance tuning. Performance tuning in SQL is all about making your queries run as fast and efficiently as possible. When working with large databases or complex queries, performance tuning can save a significant amount of time and resources, making data analysis faster and more efficient. Apart from query optimization, here are some other areas to consider when tuning SQL for data analysis:
Database Design Optimization: Proper database design can also enhance performance. This includes things like normalization (which reduces data redundancy), appropriate use of data types, and partitioning large tables.
Server Tuning: This involves adjusting the settings of the database and SQL server to maximize performance. This could include things like increasing buffer sizes, optimizing thread usage, or adjusting cache settings.
Hardware Optimization: Finally, performance can be improved by upgrading the server hardware. This could include adding more memory (RAM), using faster storage devices (like SSDs), or adding more CPU cores.
SQL performance tuning is crucial, especially when dealing with large data sets. A well-tuned SQL query can retrieve and process data much faster, making the analysis process more efficient and timely. It's important to remember that performance tuning is a continuous process. As data grows and changes, what was once an optimized system may need further adjustments.
Better performance from your data analysis using SQL
You shouldn’t see SQL as just a way to read and write data from your database. SQL is an incredibly powerful language that can really increase the performance of your data analysis. Because you are performing the analysis directly in the database, you get efficient calls and less overhead. SQL data analysis can also help you prep your data for more complex analysis offline with powerful language like Python and R.
So it’s worth learning those few core commands and getting to understand aggregation and calculation directly on the data. Data analysis in SQL will help you understand your data better and give you a head start on your analysis.
You can use SQL directly within
Hex
. Head over to our
use cases
to see it in action.
Share:
twitter
linkedin
Here at Hex, we're creating a platform that makes it easy to build and share interactive data products that can help teams be more impactful.
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
