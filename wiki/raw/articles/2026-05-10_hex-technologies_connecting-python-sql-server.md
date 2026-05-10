---
title: "Connecting to and querying SQL Server with Python | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/connecting-python-sql-server/"
scraped: "2026-05-10T01:28:53.793843+00:00"
lastmod: "2023-04-28"
type: "sitemap"
---

# Connecting to and querying SQL Server with Python | Hex 

**Source**: [https://hex.tech/blog/connecting-python-sql-server/](https://hex.tech/blog/connecting-python-sql-server/)

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
Connecting to and querying SQL Server with Python
Leverage Python’s versatility and SQL Server’s robustness with the pyodbc library to easily connect and interact with your database
Andrew Tate
Further reading
April 28, 2023
Share:
twitter
linkedin
In this article
Installing the pyodbc library to connect to SQL Server
Building a Python connection to SQL server
Creating tables and loading data using Python and SQL Server
Running queries in Python with pyodbc and SQL Server
The power of Python and SQL Server combined
Get started for free
There’s an adage, "Amateurs talk strategy. Professionals talk logistics." In the database world that might be "Amateurs talk noSQL. Professionals talk SQL Server."
In the
2022 StackOverflow Developer Survey
, 28.77% of professional developers were using Microsoft SQL Server, only beaten by MySQL, PostgreSQL, and SQLite. If your company is in the Microsoft and Azure ecosystem, then SQL Server is going to be your likely choice of database. Even if not, SQL Server has extensive tooling and good performance and scalability, making it an optimum choice for growing teams.
Here we want to take you through how you can use Python to connect to SQL Server and take advantage of the database for storage while using Python for analysis.
Installing the pyodbc library to connect to SQL Server
You just need one library to connect to SQL server using Python:
pyodbc
. This library isn’t specific to SQL server. Instead it provides an ODBC (Open Database Connectivity) interface for connecting to various databases. Though the ODBC standard was first built by Microsoft so works natively with their products, you can also use it with MySQL, PostgreSQL, and a ton of other databases.
Even though we’re only going to be installing one library, we’ll still go ahead and set up a virtual environment to compartmentalize our project:
Copy
python -m venv env
source env/bin/activate
Now we can install
pyodbc
. If you are on Windows, this is straightforward:
Copy
pip install pyodbc
If you are using macOS, it might be straightforward. If it isn’t already installed, you’ll need unixODBC which you can install through homebrew and set the linkers:
Copy
brew install unixodbc
export LDFLAGS="-L/opt/homebrew/Cellar/unixodbc/[your version]/lib"
export CPPFLAGS="-I/opt/homebrew/Cellar/unixodbc/[your version]/include"
Where [your version] is the version of unixODBC you have (you can use
odbcinst -j
to find the version).
And if you’re using Apple Silicon, the basic pip install won’t work. Instead you need to build the library from source rather than using the binary wheel most Python packages come with:
Copy
pip install --no-binary :all: pyodbc
Installing on Linux depends on the flavor of Linux you’re rocking. Check out the install options
here
for more information.
Building a Python connection to SQL server
Whew, okay. With that done, you can connect using
pyodbc
to your SQL server. Here we’re going to be using an SQL Server instance on Azure. This will be a common setup for production usage of SQL Server. We’ll create a
sql_server_connect.py
file in our project folder and import
pyodbc
:
Copy
#sql_server_connect.py
import pyodbc
You then set up all the parameters for your connection. You’ll need your server name, database name, username, password, and driver version (which, if you just installed, is probably going to be 18):
Copy
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'
driver = '{ODBC Driver 18 for SQL Server}'
You can get all of this from your Azure SQL portal. Click on ‘Connection strings’ and then choose ‘ODBC’ and all of this information will be shown:
Azure SQL Portal configuration
We then need to create a connection string with this information:
Copy
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
Then we can use this string with the
connect
method to open a connection to our SQL server database:
Copy
conn = pyodbc.connect(connection_string)
If you run all of this so far with:
Copy
python sql_server_connect.py
You should return nothing. The code will just run and end. That’s because we’re opening the connection but not doing anything with it. We need to create a table, add some data, and then query that data.
Before we do that though, let’s add a line to the skeleton of our code for good management:
Copy
conn.close()
It's considered a best practice to close connections explicitly once you're done using them. Not doing so means you might hit connection limits of the database or continue to use up resources no longer needed.
Protip: using the same Python structure to open and close files, the with statement will automatically close the connection when exiting the block, even if an exception occurs:
Copy
with pyodbc.connect(connection_string) as conn:
cursor = conn.cursor()
# Perform your database operations here
# Connection is automatically closed when leaving the 'with' block
In that block we see a cursor object being created. Cursors are objects that manage the execution and fetching of results from SQL queries. Whenever you are connecting to a database through Python (or other languages) you need to create a cursor to start interacting with the database, executing queries, and retrieving data from result sets.
Right, now we can connect to SQL Server, create a cursor for interaction, then close the connection. But we have no tables and no data.
Creating tables and loading data using Python and SQL Server
Let’s create a table and load in some data. We’ll set up a table of customers of a SaaS company. We’ll want fields for their first and last names, email address, a unique ID, and row ID, and a signup date. The names and email address will be text fields, the IDs will be integers, and the sign up date will be modeled as a date.
To create a table like this we’ll create a string with the SQL inside. With
pyodbc
we aren ’t using Python abstractions for different SQL statements. Instead, we have a single
execute
method and then write SQL in a string within that :
Copy
create_table_query = '''
CREATE TABLE customers (
id INT PRIMARY KEY,
first_name VARCHAR(255),
last_name VARCHAR(255),
email VARCHAR(255),
UID INT,
sign_up_date DATE
)
'''cursor.execute(create_table_query)
conn.commit()
This SQL statement creates a
customers
table with each of the fields we want. We call
execute
to execute it, and then
commit
commits the transaction.
If we then try to fetch data from this table:
Copy
query = 'SELECT * FROM customers'
cursor.execute(query)
print(cursor.fetchall())
We get:
Copy
[]
Nothing! We’ve created a table but haven’t populated it with any data yet. So let’s do that. Adding data using the same as creating the table, but with a different SQL statement:
Copy
insert_data_query = '''
INSERT INTO customers (id, first_name, last_name, email, UID, sign_up_date)
VALUES (1,"Jami","Armin","
[email protected]
",54084,"2022-12-27")
'''
cursor.execute(insert_data_query)
conn.commit()
Here we’re using the
insert into … values …
SQL statement to add each of the values to their corresponding fields. This time when we try to select everything from the table we get:
Copy
[(1, 'Jami', 'Armin', '
[email protected]
', 54084, datetime.date(2022, 12, 27))]
Because we’re working in Python,
pyodbc
returns a tuple (here within an array). You can then reference any value using the column name as the key:
Copy
query = 'SELECT * FROM customers'
cursor.execute(query)
customer = cursor.fetchall()
print(customer[0].first_name)
#output
Jami
You don’t want to add customers one by one. So we can add values in bulk. The most efficient way to do this is to use the
executemany
method. We’ll read all our data in from a CSV and then add it to our table:
Copy
with open('data.csv', 'r') as f:
reader = csv.reader(f)
customer_list = list(reader)
insert_multiple_data_query = '''
INSERT INTO customers (id, first_name, last_name, email, UID, sign_up_date)
VALUES (?, ?, ?, ?, ?, ?)
'''
cursor.executemany(insert_multiple_data_query, customer_list)
conn.commit()
This will iterate through our list and add each entry. If we see what’s in the table now, we get a long list of all our customers:
Copy
query = 'SELECT * FROM customers'
cursor.execute(query)
customers = cursor.fetchall()
print(customers)
#output
[
(1, 'Jami', 'Armin', '
[email protected]
', 54084, datetime.date(2022, 12, 27)),
(2, 'Martha', 'Emms', '
[email protected]
', 63089, datetime.date(2022, 7, 1)),
(3, 'Susanna', 'Broek', '
[email protected]
', 93850, datetime.date(2022, 11, 2)),
(4, 'Jenelle', 'Douthwaite', '
[email protected]
', 19979, datetime.date(2022, 7, 23)),
(5, 'Enid', 'Bartol', '
[email protected]
', 10234, datetime.date(2023, 2, 10)),
(6, 'Jennifer', 'Yellop', '
[email protected]
', 46414, datetime.date(2022, 6, 6)),
(7, 'Tiffie', 'Chant', '
[email protected]
', 16753, datetime.date(2022, 5, 4)),
(8, 'Nils', 'Dollard', '
[email protected]
', 24553, datetime.date(2023, 2, 10)),
(9, 'Rollins', 'Risbridge', '
[email protected]
', 14210, datetime.date(2022, 9, 29)),
(10, 'Maggi', 'Crudge', '
[email protected]
', 77741, datetime.date(2022, 12, 9)),
...
]
All this data was generated using
Mockaroo
, a great tool for getting realistic datasets for testing databases.
Running queries in Python with pyodbc and SQL Server
Now you’re free to manipulate your data however you like. With just this table, we can do filtering with a WHERE clause:
Copy
query = "SELECT * FROM customers WHERE first_name = 'jami'"
cursor.execute(query)
customers = cursor.fetchall()
print(customers)
#output
[(1, 'Jami', 'Armin', '
[email protected]
', 54084, datetime.date(2022, 12, 27))]
Or we can sort results using an ORDER BY clause:
Copy
query = "SELECT * FROM customers ORDER BY UID ASC"
cursor.execute(query)
customers = cursor.fetchall()
print(customers)
#output
[
(932, 'Fleming', 'Jeanel', '
[email protected]
', 70, datetime.date(2022, 5, 16)),
(13, 'Arline', 'Dannett', '
[email protected]
', 194, datetime.date(2023, 4, 4)),
(418, 'Silva', 'Falck', '
[email protected]
', 211, datetime.date(2022, 11, 21)),
(875, 'Rosalinde', 'Gherardini', '
[email protected]
', 385, datetime.date(2022, 4, 29)),
(921, 'Lorianne', 'Fray', '
[email protected]
', 446, datetime.date(2022, 4, 28)),
(685, 'Zia', 'Olivey', '
[email protected]
', 608, datetime.date(2022, 9, 18)),
(371, 'Tana', 'Durbann', '
[email protected]
', 661, datetime.date(2022, 5, 6)),
(185, 'Brennen', 'Rodmell', '
[email protected]
', 803, datetime.date(2022, 10, 31)),
(937, 'Giselbert', 'Down', '
[email protected]
', 813, datetime.date(2022, 9, 2)),
(256, 'Kristen', 'Duddan', '
[email protected]
', 941, datetime.date(2023, 2, 3)),
...
]
Or we can perform subqueries:
Copy
query = '''
SELECT first_name, UID
FROM customers
WHERE first_name IN (
SELECT DISTINCT first_name
FROM customers
WHERE UID < 200
)
'''
cursor.execute(query)
customers = cursor.fetchall()
print(customers)
#output
[('Arline', 194), ('Fleming', 70)]
If you have other tables you can do joins and unions and all the good stuff as well. Ultimately, you are just writing SQL within an easy-to-use Python wrapper.
The power of Python and SQL Server combined
One of the serious benefits of using Python with SQL is that you are free to choose where you want to do any transformations. You can do them directly in SQL or you can just pipe out all the data to Python and manipulate the data using another Python library (especially helpful when you have numeric data as you can use numPy).
Share:
twitter
linkedin
PS: This is exactly what Hex helps out with— letting you access your data from a database or data warehouse using SQL, and then seamlessly switching to Python to manipulate and analyze that data. Try it out today, completely free.
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
