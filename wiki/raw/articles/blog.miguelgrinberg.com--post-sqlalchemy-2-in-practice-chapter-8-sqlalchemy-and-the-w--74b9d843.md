---
title: "SQLAlchemy 2 In Practice - Chapter 8: SQLAlchemy and the Web"
url: "https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-8-sqlalchemy-and-the-web"
fetched_at: 2026-05-17T07:01:25.708103+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# SQLAlchemy 2 In Practice - Chapter 8: SQLAlchemy and the Web

Source: https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-8-sqlalchemy-and-the-web

This is the eighth and final chapter of my
SQLAlchemy 2 in Practice
book. If you'd like to support my work, I encourage you to buy this book, either directly from
my store
or on
Amazon
. Thank you!
Whether you are building a traditional web application, or a web API that works alongside a web front end or smartphone app, SQLAlchemy is one of the best choices to add database support to a Python web server. In this chapter two example integrations with
Flask
and
FastAPI
will be demonstrated. These are two of the most popular Python web frameworks and should serve as examples even if you use another web framework.
For your reference, here is a summary of the book contents:
General Integration Approach
If you are looking for the easiest method to integrate SQLAlchemy into a web application, then you should consider not using an integration at all.
Following the structure presented in this book, you can add the
db.py
and
models.py
modules to your application and then use the session context manager to include database functionality in every place where it is needed. This is, in fact, the technique that was used in all the importer scripts that were presented in previous chapters.
This approach is suitable not only for web applications but for any other types of Python applications, and it has the advantage that it does not require any additional dependencies or extensions.
SQLAlchemy Integration Techniques
While the no-integration option suggested in the previous section should work just fine with a lot of projects, you may prefer to use a solution that encapsulates and simplifies the database functions in a way that is convenient for your chosen web framework. The sections that follow discuss some implementation details that should be considered.
Disambiguation of SQLAlchemy Imports
One aspect of SQLAlchemy that is sometimes tedious is that it exports many classes and functions. Consider the SQLAlchemy imports used in the
models.py
module from the previous chapter:
from sqlalchemy import String, Text, ForeignKey, Table, Column
from sqlalchemy.orm import Mapped, WriteOnlyMapped, mapped_column, relationship
If you need to run database queries, then you have to import
Session
, the
select()
function and a few additional symbols, depending on your needs.
Having these long lists of imports in an application has two disadvantages. First, it is time-consuming to maintain these import lists at the top of every module that needs to use the database, but more importantly, some imports with fairly generic names such as
select
may collide with symbols from other dependencies or from the application itself.
A useful technique that addresses these two concerns is to
namespace
all the imports by only importing the parent modules. For a SQLAlchemy ORM application there are usually two parent modules,
sqlalchemy
and
sqlalchemy.orm
, so these can be imported directly:
import sqlalchemy
import sqlalchemy.orm
When doing this, all the symbols can be accessed through their parent, for example
sqlalchemy.select
or
sqlalchemy.orm.relationship
. To avoid the long names, the imports can be renamed to shorter prefixes:
import sqlalchemy as sa
import sqlalchemy.orm as so
Now the symbols are prefixed with
sa.
and
so.
for SQLAlchemy Core and ORM respectively. Here is how the
Order
model looks when using this style:
class Product(Model):
    __tablename__ = 'products'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(
        sa.String(64), index=True, unique=True)
    manufacturer_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey('manufacturers.id'), index=True)
    year: so.Mapped[int] = so.mapped_column(index=True)
    cpu: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32))

    manufacturer: so.Mapped['Manufacturer'] = so.relationship(
        back_populates='products')
    countries: so.Mapped[list['Country']] = so.relationship(
        secondary=ProductCountry, back_populates='products')
    order_items: so.WriteOnlyMapped['OrderItem'] = so.relationship(
        back_populates='product')
    product_reviews: so.WriteOnlyMapped['ProductReview'] = so.relationship(
        back_populates='product')
    blog_articles: so.WriteOnlyMapped['BlogArticle'] = so.relationship(
        back_populates='product')

    def __repr__(self):
        return f'Product({self.id}, "{self.name}")'
Model Serialization
A need that is specific to web applications and web-based APIs is to send models to clients that request them. To be sent over the network, these entities have to be
serialized
, which is a process that converts the Python model instance from its internal binary representation to a string or byte sequence that can be transmitted and then reconstructed on the other side.
The most commonly used serialization format is
JavaScript Object Notation
or JSON (pronounced "Jason"). Here is how a
Product
entity from the RetroFun database might look once serialized to the JSON format:
{
  "id": 41,
  "name": "Commodore 64",
  "manufacturer": {
    "id": 14,
    "name": "Commodore"
  },
  "countries": [
    {
      "id": 3,
      "name": "USA"
    }
  ],
  "year": 1982,
  "cpu": "6510"
}
The JSON format is similar in syntax to Python dictionaries, lists and primitive types such as integers and strings. In fact, the
json
module from the Python standard library can render a Python dictionary with the above structure to the corresponding JSON serialized representation, which is returned as a string that can be sent in the response to a client.
The reverse process to serialization is called
deserialization
. In the case of JSON, it is carried out by a JSON decoder. There are JSON decoders for all languages and technology stacks, so when the client receives a response string from the server with the above contents, it can decode it into a format that is convenient. In the case of JavaScript running in the browser, the
JSON.parse()
function converts a JSON payload into a structure based on JavaScript objects, arrays and primitive types.
Looking at the structure of the above example more closely, you will find that this particular representation not only includes a product, but also some of its relationships, namely the manufacturer and countries of origin, which have their own JSON representations embedded into the parent entity.
Building a serialization system that can easily generate responses that recursively include relationships is actually not too difficult. The basic idea is to add a
to_dict()
method to each model class that returns a dictionary version of the object that can be serialized to the JSON format.
Below you can see the implementation of the
Product
model's
to_dict()
method as an example:
class Product(Model):
    # ...

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'manufacturer': self.manufacturer.to_dict(),
            'year': self.year,
            'cpu': self.cpu,
            'countries': [country.to_dict() for country in self.countries],
        }
This example shows how related objects are embedded into the representation of the parent object by calling their own
to_dict()
methods, which ensures that the logic to serialize an entity is kept in a single place.
Note:
An alternative to the
to_dict()
serialization methods that can be useful with large and complex models is to use a specialized serialization library such as
Marshmallow
.
The Alchemical Package
When working with SQLAlchemy, there are a few objects that need to be created in every project:
An
Engine
instance.
A
MetaData
instance with an explicit naming convention for indexes and constraints.
A
Model
declarative base class.
A
Session
base class associated with the engine.
In the code examples presented in previous chapters all these objects were initialized in the
db.py
module, and this or a similar module would need to be included in every project that integrates SQLAlchemy.
The
Alchemical
package (created and maintained by the author of this book) attempts to simplify the use of SQLAlchemy by encapsulating all the above items into an
Alchemical
instance. You can install Alchemical with
pip
:
(venv) $ pip install alchemical
Consider the following example, which provides the same functionality as the
db.py
module:
import os
from dotenv import load_dotenv
from alchemical import Alchemical

load_dotenv()

db = Alchemical(os.environ['DATABASE_URL'])
The
db
object created from the
Alchemical
class contains all the SQLAlchemy items enumerated above. Here is how to access them:
The engine instance is managed internally by the
Alchemical
object and is normally not referenced directly by the application. If necessary, it can be obtained by calling
db.get_engine()
.
The
MetaData
instance is also managed internally without the application needing to reference it. If necessary, it is available as
db.metadata
.
The
db.create_all()
and
db.drop_all()
methods create and destroy the database tables respectively.
The declarative base class is
db.Model
.
The session base class is
db.Session
. To create a session and begin a transaction on it, a single context manager with
db.begin()
can be used instead of the two context managers required by SQLAlchemy.
The
Alchemical
class provides additional features:
Ability to maintain connections to multiple databases, something that is hard to implement manually for projects that use the ORM module.
Simplified support for Alembic database migrations.
Asynchronous support, when imported from the
alchemical.aio
module.
Integration with the Flask web framework, when imported from the
alchemical.flask
module.
An Example Web Application
The
GitHub repository
for this book includes a complete example of a small web application that presents a table of RetroFun orders with support for efficient pagination, sorting, searching and informational tooltips. Implementations for Flask and FastAPI are provided as examples of traditional and asynchronous integrations.
Table Front End
The table featured in the example applications uses the
grid.js
library. This table is configured in "server-side" mode, which means that it obtains data by making requests to the server. This is the most efficient way to configure the table, because only the data that needs to be displayed is requested. Whenever the user clicks on a pagination link, a column sorting header, or types something in the search box, a new request is made to the server to refresh the table with updated information.
Discussing the front end implementation details of this table falls outside the scope of this book, but you can inspect the client-side source code in the
index.html
file included with the two example applications.
What's important to know about the front end is that when the table needs to display new data, a request is issued to the server's
/api/orders
endpoint with the following query string parameters:
start
: the 1-based index of the first element that needs to be displayed.
length
: the number of elements that the table needs.
sort
: a comma-separated list of orderings, where each item starts with a
+
or
-
for ascending or descending order, followed by the field name. For example,
+customer,-total
sorts the list by customer name in ascending order, and secondarily by order total in descending order.
search
: the search string typed by the user in the search field, or an empty string if there is no search requested. If a search string is given, only orders that have a matching customer name or product name are expected to be returned.
Here is an example request URL that the front would issue to get the third page of results with a page size of 10, with orders sorted by their total amount in ascending order and with a search string of
Dylan
:
http://domain.com/api/orders?start=21&length=10&sort=%2Btotal&search=Dylan
Note the value of the
sort
argument, which is
%2Btotal
. Certain characters in URLs have to be escaped, and the
+
is one of them. The encoding uses the hexadecimal ASCII code for the character, with a
%
prefix. A web framework such as Flask or FastAPI handle character escaping transparently, so normally the developer does not need to be concerned with this task.
The role of the
/api.orders
endpoint in the back end is to accept these four query string parameters, execute a database query based on them and return the items requested using the following JSON structure:
{
  "data": [
    { ... order ... },
    { ... order ... },
    ...
  ],
  "total": <n>
}
The
data
section of the response must include an array of orders, each formatted according to its
to_dict()
serialization method. There should be up to
length
orders included in the response. The
total
field should include the total number of entries that satisfy the current search criteria, or the total number of orders when there is no search defined. This is so that the table can show a legend such as "Showing items 31 to 40 of 4798 results".
Database Queries
One of the most important parts of the back end is the logic that generates the queries that solve the request from the client. It's queries in plural, because the expected JSON payload needs one query for the
data
section of the response and another for
total
.
The query for the total is actually the simpler of the two. This query needs to calculate the count of orders that match the search string, or the total count of orders if there is no search string. Only the
search
query string argument is used for this query. The
start
,
length
and
sort
arguments do not have any effect on this calculation.
The
total_orders()
function shown below, which will be part of a
queries.py
module in the example applications, creates this query.
def total_orders(search):
    if not search:
        return sa.select(sa.func.count(Order.id))

    return (
        sa.select(sa.func.count(sa.distinct(Order.id)))
            .join(Order.customer)
            .join(Order.order_items)
            .join(OrderItem.product)
            .where(
                sa.or_(
                    Customer.name.ilike(f'%{search}%'),
                    Product.name.ilike(f'%{search}%'),
                )
            )
    )
There are two different implementations for this query, depending on the existence of a search string. When no search string was given, a simple query that returns the total count of orders is used.
When there is a search string, the query is more complex. The
select()
portion still specifies a count, but this time unique orders must be counted, because the joins with customers and products can create duplicate results, as you have seen in many example queries.
Joining
Order
with
Customer
makes the customer names searchable in the query. To also be able to search product names,
Order
is joined with
OrderItem
, which in turn is joined with
Product
. Recall that
OrderItem
is the join table for the many-to-many relationship between orders and products.
With all the joins in place, the search is carried out with a
where()
clause that has two conditions combined with the "or" logical operator. The
ilike()
function is used to run a case-insensitive pattern search of the given search string on the
Customer.name
and
Product.name
columns.
The query that returns a page worth of orders is implemented in a
paginated_orders()
function, shown below.
def paginated_orders(start, length, sort, search):
    # base query to retrieve orders with their total amount
    total = sa.func.sum(OrderItem.quantity * OrderItem.unit_price).label(None)
    q = (
        sa.select(Order, total, Customer)
            .options(so.selectinload(Order.customer))  # only needed for async
            .join(Order.customer)
            .join(Order.order_items)
            .join(OrderItem.product)
            .group_by(Order, Customer)
            .distinct()
    )

    # add search filters
    if search:
        q = q.where(
            sa.or_(
                Customer.name.ilike(f'%{search}%'),
                Product.name.ilike(f'%{search}%'),
            )
        )

    # add sorting
    if sort:
        order = []
        for s in sort.split(','):
            direction = s[0]  # first character is either + or -
            name = s[1:]  # rest of the string is the column name
            if name == 'customer':
                column = Customer.name
            elif name == 'total':
                column = total
            else:
                column = getattr(Order, name)
            if direction == '-':
                column = column.desc()
            order.append(column)
        if not order:
            order = [Order.timestamp.desc()]
        q = q.order_by(*order)

    # add pagination
    q = q.offset(start).limit(length)

    return q
This query takes significant more work to create. One interesting implementation choice in this function is that the query is built in four separate chunks that are appended instead of as a single chain of clauses following the
select()
function call.
The base query obtains orders along with their totals, in a way that is very similar to examples presented in earlier chapters. The join of
Order
with
OrderItem
is necessary to be able to calculate the total, and the joins with
Customer
and
Product
are done here preventively, to enable the search and sort options. The query includes
Customer
in the
select()
and
group_by()
clauses because the application will allow users to sort the data by customer name, otherwise the customers do not need to be retrieved directly. The
.options()
clause is necessary when using asynchronous queries, because the
Order.customer
relationship is configured with
lazy='joined'
in
models.py
, and for queries that use grouping joins that are added implicitly by SQLAlchemy can cause errors when the database does not know how to group the data retrieved by the join.
The second part of the query is conditional on the existence of a search string. This part appends a
where()
clause that is identical to the one used in the query that calculates the total number of orders.
The third part of the query is also conditional, and only used when there is a sort request. The sort string comes as a comma-separated list, so this section splits the value of
sort
into each part and then obtains each column to sort by. Supported columns are
Customer.name
, the
total
label, or else any of the primary columns of the
Order
model, of which only
timestamp
is used in this example. If the column name was given with a
-
as a prefix, then the
desc()
method is called on the sorting attribute to reverse the sort. The list of columns that were collected while parsing the sort string are then included in an
order_by()
clause that is appended to the query.
In the fourth and final section, the pagination
offset()
and
limit()
clauses are added, so that the correct range of results are retrieved.
It is important to note that these two functions just create the queries. The separation between creating and executing queries makes it possible to write these queries in a completely generic way that will work without changes in the Flask and FastAPI examples.
Endpoints
This application needs two endpoints. The root URL will return an HTML page that includes the front end JavaScript code. The front end will be configured to make requests to the
/api/orders
endpoint when it needs to update the items that are displayed as a result of a user action such as clicking a pagination link.
The endpoints need to be coded according to the conventions set in place by the web framework you are using. Both Flask and FastAPI define endpoints as functions decorated with a route decorator. The syntax used by the two implementations is not identical, but it is fairly similar.
The handler for the root URL does not require any database access, as it just needs to return the HTML file with the front end code. The handler for the
/api/orders
endpoint is where the core logic that drives the content of the table is defined. This endpoint must perform the following tasks:
Obtain the
start
,
length
,
sort
and
search
parameters given by the client in the query string of the request URL.
Pass the four parameters to the functions that generate the two database queries.
Execute the two queries in a database session.
Return a JSON response with the appropriate format including the results from the queries.
Flask Routes
The Flask version of the two endpoints, which are stored in the
routes.py
module, is shown below.
from flask import Blueprint, render_template, request
from .models import db
from . import queries

bp = Blueprint('routes', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/api/orders')
def get_orders():
    start = request.args.get('start')
    length = request.args.get('length')
    sort = request.args.get('sort')
    search = request.args.get('search')

    data_query = queries.paginated_orders(start, length, sort, search)
    total_query = queries.total_orders(search)

    orders = db.session.execute(data_query)
    data = [{**o[0].to_dict(), 'total': o[1]} for o in orders]
    return {
        'data': data,
        'total': db.session.scalar(total_query),
    }
In Flask, it is a common practice to define the routes of the application in
blueprints
. Each blueprint is then registered with the application instance to get its routes included. In this application,
bp
is the only blueprint, with the two endpoints described above implemented in the
index()
and
get_orders()
functions respectively.
The
index()
function uses Flask's
render_template()
function to return the HTML page. The JavaScript logic in this page is going to start sending requests to
/api/orders
to feed the orders table.
The
get_orders()
function is where the table content is generated. First the four parameters are extracted from the query string, which Flask exposes in the
request.args
dictionary. The
data_query
and
total_query
database queries are generated by calling the functions described earlier.
With the Flask integration provided by Alchemical,
db.session
is a somewhat magical attribute that automatically starts a session the first time it is used. This is a common pattern that is used throughout Flask and many of its extensions, so the Flask integration of Alchemical uses it as well. For this reason there is no need to use the
Session
context manager to start a session. Alchemical closes the
db.session
object at the end of the request.
The rest of the
get_orders()
function executes the two queries via
db.session.execute()
and
db.session.scalar()
respectively, and returns a dictionary that is formatted as required by the client. Flask automatically renders dictionaries returned as responses to the JSON format.
The following fragment needs to be studied carefully to fully understand it:
orders = db.session.execute(data_query)
    data = [{**o[0].to_dict(), 'total': o[1]} for o in orders]
The results from executing
data_query
are stored in the
orders
variable. This is a SQLAlchemy results object, which is an iterable. In the second line, a list comprehension iterates over the results and creates the
data
section of the JSON response. Each element in the list of results must be the serialized
Order
model, which can be obtained with the expression
o[0].to_dict()
. But this is insufficient, because the client expects a
total
attribute, which is not part of the
Order
model, to also be included in the order. This total is returned as the second value in each result row, so the returned dictionary for each order is assembled with all the data from the
Order.to_dict()
method, plus the
total
result.
FastAPI Routes
For FastAPI, the endpoints are stored in the
router.py
module of the application, which you can see next.
from fastapi import APIRouter
from fastapi.responses import FileResponse
from .models import db
from . import queries

router = APIRouter()


@router.get('/')
async def index():
    return FileResponse('retrofun/html/index.html')


@router.get('/api/orders')
async def get_orders(start: int, length: int, sort: str = '',
                     search: str = ''):
    data_query = queries.paginated_orders(start, length, sort, search)
    total_query = queries.total_orders(search)

    async with db.Session() as session:
        orders = await session.stream(data_query)
        data = [{**o[0].to_dict(), 'total': o[1]} async for o in orders]
        return {
            'data': data,
            'total': await session.scalar(total_query),
        }
What Flask calls a blueprint FastAPI calls an API router, but aside from the name differences both have the same purpose. Since FastAPI is an asynchronous framework, the handler functions are defined as
async def
functions.
The
index()
function is registered as the handle for the root URL of the application, and just returns the HTML file with the front end code.
The
get_orders()
function handles the
/api/orders
endpoint. With FastAPI, query string parameters are defined as typed arguments to the function, so the four expected query parameters are included in the function declaration. The
start
and
length
parameters are always provided by the client, so there is no need to provide defaults for them, but for
sort
and
search
an empty string default is used, in case the client does not send these arguments.
The queries are generated by calling the two functions discussed earlier, exactly as it was done in the Flask version.
To run the queries, a session is started with a context manager. When using the Alchemical package, the base class for sessions is
db.Session
, with
db
being the
Alchemical
instance.
The queries in this version are issued with
await
, since the database is running in asynchronous mode. The
stream()
method of the session is used instead of
execute()
, so that the results are returned as an asynchronous iterator. The list of orders is transformed into the JSON list of orders using an asynchronous list comprehension, in the same way as it was done in the Flask application.
Flask Back End
All the interesting implementation details have already been discussed, so what is left is the boilerplate and glue code that ties all the parts together. The complete code for this application is available in the
GitHub repository
.
The project has the following structure:
- main.py           # The entry point of the application
- config.py         # Flask configuration variables
- retrofun          # Python package with the application logic
  - __init__.py     # Package initialization (load environment variables)
  - app.py          # The application factory function
  - models.py       # The Alchemical database instance and models
  - queries.py      # The database queries that support the orders table pagination
  - routes.py       # A Flask blueprint with the two routes of the application
  - templates       # Flask templates directory
    - index.html    # The HTML page of the application
- migrations        # The Alembic migrations directory
- alembic.ini       # The Alembic configuration file
- .flaskenv         # Flask-specific environment variables
- .env.template     # Template for the environment variables needed
- requirements.txt  # the dependencies used by this application
The
retrofun
directory is a Python package with the application logic. The
retrofun/queries.py
and
retrofun/routes.py
in this package have been described in earlier sections of this chapter.
The
retrofun/models.py
module defines the Alchemical database instance
db
and all the models, which use the same definitions as in
Chapter 6
, extended with
to_dict()
methods in all the models.
This application has no
db.py
module with database initialization code, because when using Alchemical the database is initialized with a single line of code. Consequently, this initialization has been moved to
models.py
. This is how the database is now initialized in
models.py
:
from alchemical.flask import Alchemical

db = Alchemical()
The
Alchemical
class is imported from the
alchemical.flask
package, so that the Flask integration is used. The database URL is obtained from the
ALCHEMICAL_DATABASE_URL
entry in the Flask configuration, which is defined in the
config.py
module:
import os

ALCHEMICAL_DATABASE_URL = os.environ.get('DATABASE_URL')
The
retrofun/app.py
is where the Flask application instance is initialized, using the application factory pattern. The
db
database instance created in
models.py
functions as a standard Flask extension, so it is initialized in the factory function. Here is how this is done:
from flask import Flask
from .models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    from .routes import bp
    app.register_blueprint(bp)

    return app
The
main.py
module in the top-level directory of the project calls
create_app()
:
from retrofun.app import create_app

app = create_app()
When starting the application with the
flask run
command, the
.flaskenv
file configures
main.py
as the place where the application is defined, and also sets debug mode:
FLASK_APP=main.py
FLASK_DEBUG=true
When a WSGI production web server such as Gunicorn is used, the location of the application instance is given with the notation
main:app
. Here is how to start the web server with Gunicorn:
(venv) $ gunicorn -b :5000 main:app
The
flask
command automatically imports the variables defined in the
.env
file, but other web servers do not. The
retrofun/__init__.py
module calls the
load_dotenv()
function, in case the web server doesn't do it:
from dotenv import load_dotenv

load_dotenv()
The Alembic database migration repository was created by the Alchemical package, so it is slightly different from the one you created using the
alembic init
command. To create a migration repository with Alchemical, the following command is used:
(venv) $ python -m alchemical.alembic.cli init migrations
This is done so that the
alembic.ini
and
migrations/env.py
files are created to be compatible with Alchemical. When creating the repository in this way, the only configuration that needs to be done is to edit the
alchemical_db
value in the
alembic.ini
file:
alchemical_db = retrofun.models:db
The
requirements.txt
file lists all the dependencies that are necessary to run the application. You can install them with the following command:
(venv) $ pip install -r requirements.txt
The project does not include a
.env
file, because the contents of this file depend on the database that you would like to use with the application. A
.env.template
file is included to serve as a template for the real
.env
file. You should create a copy of this file with the name
.env
and then set the value of the
DATABASE_URL
variable to your database. This application is compatible with the database that you created in earlier chapters of this book, so you can test it out with the same database URL.
FastAPI Back End
The FastAPI example is also provided in the
GitHub repository
.
This is the structure of this project:
- retrofun          # Python package with the application logic
  - __init__.py     # Package initialization (load environment variables)
  - app.py          # The FastAPI application instance
  - models.py       # The Alchemical database instance and models
  - queries.py      # The database queries that support the orders table pagination
  - router.py       # An API router with the two routes of the application
  - html            # HTML pages directory
    - index.html    # The HTML page for the application
- migrations        # The Alembic migrations directory
- alembic.ini       # The Alembic configuration file
- .env.template     # Template for the environment variables needed
- requirements.txt  # the dependencies used by this application
As in the Flask version, the
retrofun
directory is a Python package that contains the application logic. Also, similar to the Flask version, the
retrofunc/__init__.py
file imports the environment variables from the
.env
file.
The
retrofun/app.py
module initializes the FastAPI application and registers its routes.
from fastapi import FastAPI
from .router import router

app = FastAPI()
app.include_router(router)
The
retrofun/models.py
module defines the
db
database instance and includes all the models, which match the definitions used in
Chapter 7
for an asynchronous application, with
to_dict()
methods added in each model class. Here is how the Alchemical database instance is defined for this application:
import os
from alchemical.aio import Alchemical

db = Alchemical(os.environ['DATABASE_URL'])
The asynchronous version of
Alchemical
is imported from the
alchemical.aio
package. This version makes all the necessary adjustments designed to prevent implicit database queries.
The
retrofun/queries.py
module is framework-agnostic, so it is exactly what was described earlier in this chapter, and also what was used for the Flask application. The
retrofun/router.py
module defines the two routes of the application, and has also been covered already.
As in the Flask version, the Alembic database migration repository was created to be compatible with the Alchemical package. Instead of using the
alembic init
command to create it, Alchemical provides its own method to create the repository, so that it can insert itself in the configuration.
(venv) $ python -m alchemical.alembic.cli init migrations
For a migration repository created with this command, the only configuration that needs to be made is to edit the
alchemical_db
variable in
alembic.ini
to point to the
db
database instance.
alchemical_db = retrofun.models:db
As in most Python projects, a
requirements.txt
file is included, with the list of all the dependencies that the application needs. These are installed with
pip
as follows:
(venv) $ pip install -r requirements.txt
The
.env
is not included in the code repository because its contents depend on the database you intend to use with the application. A
.env.template
file is included to serve as an example when creating a
.env
file. To configure the project, make a copy of the
.env.template
file with the name
.env
, and then set the value of the
DATABASE_URL
variable appropriately. This project uses the
retrofun
database that you created following this book, so you can point it at the same database, making sure you use an asynchronous database driver.
A Last Word
Congratulations on reaching the end of this book! As with most technical topics, learning SQLAlchemy does not end here, the journey will continue for you as it does for me.
While I did my best to cover a wide variety of use cases and solutions, SQLAlchemy is a very large framework that can't possibly be covered entirely within the tutorial format of this book. The good news is that every little detail of this library is well covered in the official documentation.
I would like to make a special mention of three of the areas that I have not covered, in case you are interested in researching them on your own:
Subqueries and CTEs are standard SQL features that provide two different approaches to create queries that can be issued recursively from other queries. SQLAlchemy ORM has support for both.
SQLAlchemy has a fairly sophisticated event subsystem that allows an application to be notified via callback functions when certain events occur. An event handler was added in the asynchronous version of this book's database, but there are many more ways to take advantage of this feature.
The ORM module has several optional extensions, but only the one that implements asynchronous support received coverage in this book. There are other useful extensions such as Automap (to generate model classes from database schemas), Association Proxy (to simplify navigating through multiple relationships) and Hybrid Attributes (to define model attributes that are evaluated as functions of other attributes) that are well worth investigating.
I wish you the best luck with your SQLAlchemy projects!
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
