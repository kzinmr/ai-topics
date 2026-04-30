---
title: "SQLAlchemy 2 In Practice - Chapter 2 - Database Tables"
url: "https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-1---database-tables"
fetched_at: 2026-04-30T07:01:20.575458+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# SQLAlchemy 2 In Practice - Chapter 2 - Database Tables

Source: https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-1---database-tables

This is the second chapter of my
SQLAlchemy 2 in Practice
book. If you'd like to support my work, I encourage you to buy this book, either directly from
my store
or on
Amazon
. Thank you!
This chapter provides an overview of the most basic usage of the
SQLAlchemy
library to create, update and query database tables.
For your reference, here is a summary of the book contents:
SQLAlchemy Core and SQLAlchemy ORM
The SQLAlchemy library is divided into two modules called Core and ORM (short for Object-Relational Mapping).
The Core module contains the database integration logic for all the supported database dialects, a collection of classes to describe database tables, and a fairly sophisticated system for generating SQL statements using Python language constructs.
The ORM module introduces a layer of abstraction between the Python application and the database that allows many database operations to be automatically derived from actions performed on Python objects.
An application can choose to use SQLAlchemy Core exclusively, or it can combine elements from Core and ORM. In this book you will learn to use a combined approach.
The Database Engine
SQLAlchemy uses "engine" objects to manage connections to a database, both for Core and ORM applications. The
create_engine()
function constructs an engine given a database URL. Below you can see an updated version of the
db.py
file you created in the previous chapter, showing how to create an engine object from a
DATABASE_URL
environment variable imported from the
.env
file:
db.py
: Create a SQLAlchemy engine object
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

engine = create_engine(os.environ['DATABASE_URL'])
The
create_engine()
function can be passed additional keyword arguments to configure the engine. Interesting options include:
echo=True
, to have SQLAlchemy log every SQL statement issued to the database. This is a very useful option when debugging.
pool_size=<N>
, to specify a custom size for the connection pool SQLAlchemy maintains (the default is a pool size of up to 5 simultaneous connections).
max_overflow=<N>
, the maximum number of connections above the pool size that can be created during usage spikes (the default is 10).
future=True
, to tell SQLAlchemy 1.4 to use the newer 2.0 based APIs.
Consult the
documentation for create_engine()
to see the complete list of options that are available.
Models
When using the ORM module, database tables are defined in the application as Python classes. The application must create a parent class for all these classes, where settings that are common to all the tables can be configured. This parent class, which SQLAlchemy calls the
declarative base
class, is often named
Model
, or in some cases
Base
. The collection of subclasses of the
Model
class represent the structure or schema of the database, and are generally referred to as the "models" of the application.
The
Model
class must inherit from SQLAlchemy's
DeclarativeBase
class. Here is an updated version of
db.py
that defines
Model
as an empty class, without any custom settings:
db.py
: Create a declarative base class
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


class Model(DeclarativeBase):
    pass


load_dotenv()

engine = create_engine(os.environ['DATABASE_URL'])
To help keep things nicely organized, the models for the application you are going to build with the help of this book are going to be stored in their own file, which will be called
models.py
file. The next code example shows a first implementation of a model for a
products
database table:
models.py
: Product model class
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from db import Model


class Product(Model):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64))
    manufacturer: Mapped[str] = mapped_column(String(64))
    year: Mapped[int]
    country: Mapped[str] = mapped_column(String(32))
    cpu: Mapped[str] = mapped_column(String(32))

    def __repr__(self):
        return f'Product({self.id}, "{self.name}")'
If you have used older versions of SQLAlchemy, you may find the above model definition to be significantly different. In version 2.0, SQLAlchemy introduced an integration with Python type hints, and that is the reason why the currently recommended syntax for column definition has changed from older releases.
As indicated above, all application model classes must inherit from the
Model
declarative base class, which is imported from
db.py
.
Model subclasses are configured using class attributes. The
__tablename__
attribute defines the name of the database table the class represents. A very common naming convention for database tables is to use the plural form of the entity in lowercase, so in this case the table is given the
products
name. This contrasts with the convention used for the model class names, which prefers the singular form in camel case.
The remaining attributes defined in the class represent the columns of the table. The
Mapped[t]
type declaration is used to define each column, with
t
being the Python type assigned to the column, such as
int
,
str
, or
datetime
. For simple columns such as
year
above, this is all that is necessary. If the column needs to be given additional options, it is assigned to a
mapped_column()
constructor that provides those options.
In the
Product
model defined above, an option is used to identify the
id
column as a primary key, which means that the values in this column must uniquely identify each item stored in the table. Without any additional configuration, SQLAlchemy configures integer primary key columns with auto-incrementing numbers starting from 1. You will later learn other ways to define primary keys.
The remaining columns describe the attributes that products have. For columns that are of type
str
, a maximum length is added with a supplementary
String()
option. Not all databases require a length to be given for string columns, but it is best to always include a length just in case.
The
__repr__()
method included in this class is a special method that tells Python how an object of this class should be printed. Adding this method is optional, but it is useful as an aid when debugging or when trying things out in a Python shell, which is something you will often while working with this book.
To create an instance of a model class, a standard class constructor is used, passing the values for the model's attributes as keyword arguments. For example:
c64 = Product(name='Commodore 64', manufacturer='Commodore')
The above example initializes a new
Product
instance. SQLAlchemy provides a default constructor for all model classes that accepts value assignments for its columns. In this particular example, all the attributes of
c64
except
name
and
manufacturer
will be set to
None
, because they were not assigned a value when the object was created. Even though this object is a model instance, at this point it is just a plain Python object that is not stored or associated with any database.
Note:
The concept of model classes is available only for applications that use the ORM module. When using Core, instances of the
Table
class are used to represent database tables.
Database Metadata
SQLAlchemy maintains the definitions of all the tables that make up a database in an object of class
MetaData
. For convenience, it initializes the declarative base class with a
metadata
attribute that has a default
MetaData
object. For the
Model
class, the metadata instance is available as
Model.metadata
. When a model class such as
Product
is defined, SQLAlchemy creates a corresponding table definition in this attribute.
The default
MetaData
configuration has one important limitation that is bound to cause problems when projects reach certain size or level of complexity. This is related to the
naming_convention
option, which tells SQLAlchemy how to name indexes and constraints it creates on a database. You will learn what these are later in this chapter, but for now, just consider that in the same way as tables, indexes and constraints need to have a name.
The default naming convention used in the
MetaData
object provides a naming rule for indexes, but not for constraints, so SQLAlchemy initializes all constraints without an explicit name, which results in them having arbitrary names chosen by the database. This is a problem if at some point a constraint needs to be modified or deleted, since SQLAlchemy wouldn't immediately know how to address the constraint by its name. To avoid this potential complication down the road, the
Model
declarative base can be initialized with a more complete set of naming conventions, as shown below:
db.py
: Configure naming conventions for indexes and constraints
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import DeclarativeBase


class Model(DeclarativeBase):
    metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    })


load_dotenv()

engine = create_engine(os.environ['DATABASE_URL'])
The
MetaData
object has a
create_all()
method that has significant importance, as it creates all the database tables associated with the defined models. Here is an example usage:
Model.metadata.create_all(engine)
Here the
create_all()
method will issue SQL statements to the database represented by
engine
to create the database tables referenced by all the models. Following the code examples from previous sections, this call would create a
products
table, which is defined by the
Product
model.
An important limitation of
create_all()
is that it only creates tables that don't already exist in the database, which means that when a model class is changed, this method cannot be used to transfer the change to the corresponding database table.
A workaround that can be used to modify an existing table is to remove the old and outdated version of the table from the database before calling
create_all()
again. As a convenience, the
MetaData
object also has a
drop_all()
method, which removes all the tables from the database. The following example refreshes all the tables to their latest definitions:
Model.metadata.drop_all(engine)
Model.metadata.create_all(engine)
Unfortunately updating a database in this way is only practical for small tests or while prototyping, because
drop_all()
not only deletes the tables but also all the data stored in them. You will later learn how to use
Alembic
to manage updates to the database in a much more effective way through
migration scripts
.
Note:
When using Core, the database metadata object must be manually created by the application.
Sessions
Another important entity in ORM-based applications is the
session
. A session object maintains the list of new, read, modified and deleted model instances.
Changes that accumulate in a session are passed on to the database in the context of a database transaction when the session is
flushed
, which is an operation that in most cases is automatically issued by SQLAlchemy when it is needed. A flush operation writes the changes to the database, but keeps the database transaction open.
When the session is
committed
, the corresponding database transaction is committed as well, causing all the changes to be permanently written to the database.
Database transactions are one of the most important benefits of relational databases, designed to maintain the integrity of the data. The changes that are committed as part of a transaction are written as an atomic operation, so errors or unexpected interruptions will never result in partial or incomplete data being written. If an error or failure occurs while a session is active, a
rollback
operation on the session will roll the transaction back, and all the changes made up until that point in that session will be undone.
The following example shows how the
c64
object created in the previous section can be added to a database session and committed:
from sqlalchemy.orm import Session

with Session(engine) as session:
    try:
        session.add(c64)
        session.commit()
    except:
        session.rollback()
        raise
    print(c64)
The best way to manage a database session is to create it as a context manager. This ensures that the session is properly closed and disposed of at the end.
The session is initialized with the
engine
object. As with the engine, the
future=True
option can be used with SQLAlchemy 1.4 to configure the session to use 2.0 style APIs.
Session objects are designed to accumulate changes until they are either committed or rolled back. The
add()
method is used to insert a new object into the session. The
try
/
except
block ensures that the session is always committed or rolled back. If an error occurs while the session is being used or committed, the
except
section does the roll back, guaranteeing that all the partial changes that could not be committed are discarded.
As mentioned earlier, SQLAlchemy configures integer primary key columns to be auto-incrementing by default. When the session is flushed, which usually happens during a
commit()
call, the database will assign the next available number to the
id
attribute of the new item, or 1 if this is the first entry added. Any other attributes in the model object that were not set will be recorded with a
NULL
value in the database.
The print statement after the
try
/
except
block is designed to show the newly assigned
id
value, as implemented in the
__repr__()
method of the
Product
class.
SQLAlchemy provides more concise ways to work with sessions. A normal application will have lots of places in which sessions need to be created, and it may be inconvenient to have to pass the engine and other options in every one of them. The
sessionmaker
factory function provides a way to create a customized
Session
class that has all the options incorporated:
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)

with Session() as session:
    # ...
Having to wrap all the database logic in a
try
/
except
block can also become very tedious. In the next example, an inner context manager started with the
begin()
method replaces the exception handling:
with Session() as session:
    with session.begin():
        session.add(c64)
    print(c64)
The context manager created by
session.begin()
implements the
try
/
except
logic internally. It automatically commits the session at the end, and if there are any raised exceptions, it rolls the session back as before. In all cases the session is properly closed by the outer context manager.
Given that the application will need easy access to session objects, it makes sense to also define the base
Session
class in
db.py
. Here is the complete version of this file that you will use through most of this book:
db.py
: Create a session class
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Model(DeclarativeBase):
    metadata = MetaData(naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    })


load_dotenv()

engine = create_engine(os.environ['DATABASE_URL'])
Session = sessionmaker(engine)
Note:
Session objects are available only for applications that use the ORM module. When using Core, database transactions have to be manually managed by issuing appropriate SQL statements through an engine connection.
A First SQLALchemy Application
The previous sections in this chapter provide an overview of the most important components of a SQLAlchemy ORM application, which are:
the engine
the models
the database metadata
the session
Now it is time to see how these components are used in a complete application.
As mentioned in the Preface, all the examples in this book are designed around the needs of a made-up company called RetroFun that sells vintage home computers. The first complete script combines many of the snippets presented earlier into an application that imports the catalog of products offered by RetroFun from a CSV file and populates a
products
database table with them.
Copy the code below into a file named
import_products.py
, in the same directory as
db.py
and
models.py
.
import_products.py
: Import products from CSV file
import csv
from db import Model, Session, engine
from models import Product


def main():
    Model.metadata.drop_all(engine)  # warning: this deletes all data!
    Model.metadata.create_all(engine)

    with Session() as session:
        with session.begin():
            with open('products.csv') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row['year'] = int(row['year'])
                    product = Product(**row)
                    session.add(product)


if __name__ == '__main__':
    main()
The application imports the
Model
and
Session
classes and the
engine
instance from
db.py
. It also imports the
Product
model class from
models.py
.
The
main()
function is where all the database operations are issued. First the
drop_all()
and
create_all()
methods of the metadata object are invoked. These ensure that the
products
table is recreated from scratch to match the definitions of the
Product
model.
Next, a database session is started using the double context manager method, so that all the changes made in the session are automatically committed atomically at the end.
What's left is the importing logic, which starts with a third context manager dedicated to opening the CSV file that contains the data to import. Using a context manager when opening a file is very convenient, as this ensures that the file is automatically closed at the end.
Python includes a
csv
module in its standard library. The
DictReader
class from this module is used to read rows from the CSV file one at a time in a for-loop. Each row is returned as a dictionary, where the keys are the column names, which are given in the first line of the CSV file. The values for all columns are returned as strings. The CSV column names were carefully chosen to match the names of the attributes of the
Product
model, but the
year
field has to be manually converted to an integer to match the
Product
model definition.
A
Product
model instance is created directly by passing the contents of each row dictionary as
keyword arguments
. Each of these product model instances is then added to the database session.
When the for-loop that iterates over the rows of the CSV file exits, the
session.begin()
context manager will flush and commit the session, and the outer context manager will then close the session. The flush operation will write all the products imported from the CSV file to a database transaction, and the commit operation will then make these changes permanent. If an error occurs during this process, the session will be rolled back and nothing will be written to the database.
Are you ready to try this application? Make sure you have
import_products.py
,
db.py
and
models.py
in your project directory. You should also have a
.env
file in this directory with a
DATABASE_URL
variable configured with an active database according to the instructions in Chapter 1.
You will also need to have a copy of a file called
products.csv
with all the product data in the project directory. This file can be downloaded from the book's
GitHub repository
.
Make sure your Python virtual environment is activated, and then run the script as follows:
(venv) $ python import_products.py
There shouldn't be any output, but when the script ends you should have a populated
products
table in your database. If you have a database administration tool to inspect your database, feel free to review the new table with it.
Queries
With a populated table in your database, this is the perfect time to begin to learn how to issue some queries. If you have used SQLAlchemy in the past, be aware that starting with version 1.4, SQLAlchemy introduced significant changes in how ORM queries are constructed. The legacy query implementation you may be familiar with is still available, but in this book only the new query style is used. The SQLAlchemy documentation refers to the new query style as the "2.0 query style", but this style of queries can also be used in the 1.4 releases when the engine and session objects are created with the
future=True
option.
The easiest way to work with your new database is to open a Python shell, from where you can issue queries interactively. You can import the engine object and the model and session classes as follows:
>>> from db import Session
>>> from models import Product
You can then create a session:
>>> session = Session()
This is a different way of creating a session that does not use a context manager. The context manager approach to sessions is very convenient in an application, but it gets in the way when working interactively in the Python prompt, so a direct creation is better in this context.
Query Definition
Relational databases use the
SELECT
keyword to implement queries. SQLAlchemy provides a
select()
function with similar functionality. The simplest query is the one that returns all the elements in a table. Here is how to define a query that retrieves all the products stored in the database:
>>> from sqlalchemy import select
>>> q = select(Product)
The
select()
function takes as arguments the items that need to be retrieved. When a model class is given as an argument, SQLAlchemy ORM retrieves all the attributes of the model and transparently returns Python objects.
Sometimes it is useful to see what is the SQL code that will be sent to the database when this query is executed. The SQL code associated with a SQLAlchemy query object can be seen when the query is printed:
>>> print(q)
SELECT products.id, products.name, products.manufacturer, products.year,
products.country, products.cpu
FROM products
Here you can see how the
Product
class passed in the
select()
function was transformed into a
SELECT
statement that retrieves all the attributes of the table.
Query Execution
After a query object is created, it has to be given to the session, which will send it to the database driver to execute through a connection maintained by the engine. The most generic way to do this is to use the
execute()
method of the session:
>>> r = session.execute(q)
>>> list(r)
[(Product(1, "Acorn Atom"),), (Product(2, "BBC Micro"),), ..., (Product(149, "GEM 1000"),)]
The
execute()
method returns a results object. This is an iterable object that retrieves the query results. In the above exercise the iterable was converted to a list to force all the results to be retrieved and displayed. Your terminal will show a long list of products.
The
all()
method on the results object returned by
execute()
achieves the same effect as the conversion done by
list()
:
>>> session.execute(q).all()
[(Product(1, "Acorn Atom"),), (Product(2, "BBC Micro"),), ..., (Product(149, "GEM 1000"),)]
In addition to
all()
, the results object has other methods that retrieve the first result of a query, which is a very common need:
first()
returns the first result row, or
None
if there are no results. If there are any more rows in the result set, they are discarded.
one()
returns the first and only result. If there are zero or more than one result rows, an exception is raised.
one_or_none()
returns the first and only result, or
None
if there are no results. If there are two or more result rows, an exception is raised.
Having the results as an iterable is very efficient, as SQLAlchemy only retrieves the rows as they are needed, which means that for a query that returns a very large number of results you don't have to retrieve all the results into a list, and instead can process results as they are loaded. In an application, you would normally iterate over the results in a for-loop:
>>> r = session.execute(q)
>>> for row in r:
        print(row)
(Product(1, "Acorn Atom"),)
(Product(2, "BBC Micro"),)
  ...
(Product(149, "GEM 1000"),)
Note the structure of each result. Here is the first one, isolated from the rest:
(Product(1, "Acorn Atom"),)
This isn't a simple
Product
instance. SQLAlchemy returns each result as a tuple, because queries can sometimes return multiple values per row (you will see examples of this shortly). Since SQLAlchemy does not know how many results per row are expected, it always returns each row as a tuple. This query returns a single value per row, so each tuple has a single element in it.
If you know that you will be receiving a single value per row, then you can use the
scalars()
convenience method to execute the query:
>>> session.scalars(q).all()
[Product(1, "Acorn Atom"), Product(2, "BBC Micro"), ..., Product(149, "GEM 1000")]
With
scalars()
, SQLAlchemy returns a different "results" object that only iterates over the first value of each result row. If the query returned multiple values per row, then the additional values in each row are discarded. The
all()
,
first()
,
one()
and
one_or_none()
methods are also available on the results object returned by
scalars()
.
Also as a convenience, there are some additional query execution methods that combine
scalars()
with
first()
,
one()
and
one_or_none()
. Given a query
q
, these are the additional methods:
scalar(q)
is the same as
scalars(q).first()
and returns the first value of the first result row, or
None
if the query has no results.
scalar_one(q)
is the same as
scalars(q).one()
and returns the first value of the only result row, or raises an exception if there are zero or more than one result.
scalar_one_or_none(q)
is the same as
scalars(q).one_or_none()
and returns the first value of the only result row or
None
if there are no results. It raises an exception if there are two or more results.
The next example shows a compact way to get the first value of the first result row:
>>> r = session.scalar(q)
>>> r
Product(1, "Acorn Atom")
Filters
A query that only includes a
select()
statement returns all available items, which is sometimes useful, but not very often. There are many situations in which an application may want to retrieve just a subset of all the items, possibly the items that fulfill some criteria.
The application can retrieve all the results as shown above and then discard the ones that aren't of interest, but this can be very inefficient, especially for very large tables. Databases are designed to perform filtering and return only the desired results in ways that are much more efficient than what the application can do on its own.
With SQLAlchemy, a filter can be added to a query object with the
where()
clause. The following example shows how to retrieve only products made by Commodore. Feel free to try this query out in your Python session.
>>> q = select(Product).where(Product.manufacturer == 'Commodore')
>>> session.scalars(q).all()
[Product(39, "PET"), Product(40, "VIC-20"), ..., Product(48, "Amiga")]
SQLAlchemy implements a highly sophisticated solution for defining filters that combines the class attributes of model classes with standard Python operators such as
==
. The example that follows uses the
>=
operator in a query that retrieves all products made after 1990:
>>> q = select(Product).where(Product.year >= 1990)
Try executing this query with
session.scalars()
to see which products are returned.
The
where()
statement can be given multiple times to specify multiple conditions. The next example retrieves products made by Commodore only in 1980:
>>> q = (select(Product)
            .where(Product.manufacturer == 'Commodore')
            .where(Product.year == 1980))
Two or more filters can also be given as multiple arguments in a single
where()
for the same result:
>>> q = select(Product).where(Product.manufacturer == 'Commodore', Product.year == 1980)
Combining multiple filters as shown above effectively applies the
AND
logical operator to them. Sometimes a query may need to combine filters with the
OR
operator, which SQLAlchemy offers with the
or_()
function. The next example returns products built before 1970 or after 1990:
>>> from sqlalchemy import or_
>>> q = select(Product).where(or_(Product.year < 1970, Product.year > 1990))
Even though it is implied when passing multiple arguments to the
where()
clause, the
AND
logical operator can also be explicitly given using the
and_()
function. The
NOT
unary operator is also available as the
not_()
function.
Another very useful filter is the
LIKE
operator, which can be used to implement a simple search function. The following example retrieves all products that have the word
Sinclair
in their name:
>>> q = select(Product).where(Product.name.like('%Sinclair%'))
The
like()
method available on column attributes of models accepts a search pattern string and returns all results that match this pattern. The pattern defines the text to search for, expanded with a
%
character as a wildcard that matches zero, one or more characters, and a
_
character to match just one character. Here are a few other example patterns for the
like()
filter:
Sinclair%
(items that start with
Sinclair
)
%Sinclair
(items that end with
Sinclair
)
% Sinclair
(items that end with a space, followed by
Sinclair
)
R__%
(items that start with the letter
R
followed by at least two more characters)
_
(items that are one character long)
The
like()
function is case-sensitive. For case-insensitive searches, you can use the
ilike()
function instead.
A range of items can be requested with a
where()
clause defining two conditions for the lower and upper bounds respectively, but it is more clear to use the
between()
method exposed by column attributes of model classes. The example below returns products that were made in the 1970s:
>>> q = select(Product).where(Product.year.between(1970, 1979))
Have you tried looking at the SQL code generated by some of these queries? Here is how the last one looks:
>>> print(q)
SELECT products.id, products.name, products.manufacturer, products.year,
products.country, products.cpu
FROM products
WHERE products.year BETWEEN :year_1 AND :year_2
Here you can see that the literal values that are defined in query filters are not inserted in the rendered SQL. Instead, they are replaced with placeholder arguments such as the
:year_1
and
:year_2
above. This is a well established security practice that prevents SQL injection attacks, and SQLAlchemy implements it automatically.
For debugging purposes you may want to see the SQL query with the actual literals. While this can be insecure and should not be used to generate SQL statements intended to be executed, the following example shows how to tell SQLAlchemy to render the query along with all the literal parameters:
>>> print(q.compile(compile_kwargs={'literal_binds': True}))
SELECT products.id, products.name, products.manufacturer, products.year,
products.country, products.cpu
FROM products
WHERE products.year BETWEEN 1970 AND 1979
Order of Results
The queries above return the requested data in the order chosen by the database server, but relational databases are able to sort the results very efficiently to provide them in the order that the application finds most convenient. The
order_by()
method can be added to a query to specify the desired order.
The next example retrieves products alphabetically ordered by their names:
>>> q = select(Product).order_by(Product.name)
>>> session.scalars(q).all()
[Product(10, "464 Plus"), Product(11, "6128 Plus"), ..., Product(127, "ZX Spectrum")]
It is also possible to sort in reverse order by calling the
desc()
method on the column attribute given in the
order_by()
clause. The example below returns the products according to their year of manufacture, with the newest products first:
>>> q = select(Product).order_by(Product.year.desc())
>>> session.scalars(q).all()
[Product(6, "A7000"), Product(33, "Falcon"), ..., Product(74, "Honeywell 316")]
There are many situations in which a single ordering criteria is insufficient. For example, in the last example, all the computers that were built in the same year are returned in an arbitrary order. The
order_by()
method accepts multiple arguments, each adding a new level of sorting. The previous example can be improved with a secondary sorting by product name:
>>> q = select(Product).order_by(Product.year.desc(), Product.name.asc())
Note the
asc()
method, which is used to specify ascending order for the product name. Ascending order is the default, so there is no need to include this method, but sometimes it may make the query more clear when the order is explicitly stated.
Access to Individual Columns
In all the example queries so far, the requested data was entire rows out of the
products
table, which the SQLAlchemy ORM maps to instances of the
Product
model class. While querying ORM entities in this way is very common, the
select()
function is very flexible and can work with more granular data as well.
For example, an application may only need to retrieve an individual column. In the next query, only the names of the products are retrieved:
>>> q = select(Product.name)
>>> session.scalars(q).all()
['Acorn Atom', 'BBC Micro', ..., 'GEM 1000']
As discussed earlier, the
select()
function is not limited to retrieving a single value per result row, and it can actually request several in the same query. The following query obtains the name and manufacturer of each product:
>>> q = select(Product.name, Product.manufacturer)
>>> session.execute(q).all()
[('Acorn Atom', 'Acorn Computers Ltd'), ('BBC Micro', 'Acorn Computers Ltd'), ...]
Notice how this example has to be executed with
session.execute()
so that the pair of values in each result row are returned as a tuple.
Aggregation Functions
The
select()
function can also work with SQL functions that are evaluated on the retrieved data on the fly to transform it. A very useful function is
count()
, which replaces all the result rows with a count of how many there are. The next example finds out how many products are stored in the database:
>>> from sqlalchemy import func
>>> q = select(func.count(Product.id))
>>> r = session.scalar(q)
>>> r
149
The
count()
function used above reduces the list of results to a single value, and for that reason the
scalar()
method is used to retrieve it. In this example, using
Product.id
as argument to count results is arbitrary, any column attribute of the
Product
class can be given, and the result would be the same, because the data itself does not matter. There is an alternative form of the above query that does not require picking a random column to get a count of results:
>>> q = select(func.count()).select_from(Product)
>>> r = session.scalar(q)
>>> r
149
In this second form, the
count()
function is given no arguments to indicate that a count of results is desired, without specifying what data to count. When using this format, the
select_from()
method has to be added to configure the table to use in the query, because SQLAlchemy cannot automatically determine it from the arguments given to the
select()
function.
Another pair of useful SQL functions are
min()
and
max()
. The example that follows returns the first and last years in which products in the database were manufactured:
>>> q = select(func.min(Product.year), func.max(Product.year))
>>> r = session.execute(q)
>>> r.first()
(1969, 1995)
This query has to use
execute()
because it retrieves two values per row. The
min()
and
max()
functions reduce the list of results to a single row, so there is no point in using
all()
to retrieve the results as in previous examples. When it is known in advance that there is going to be one result row, the
first()
or
one()
methods are more convenient, with the latter raising an exception for queries that return anything other than a single result row.
Result Grouping
The database in its current form only has products as a first-class entity, but sometimes the application may be interested in a retrieving related data attributes such as the manufacturer. Here is an attempt to obtain a list of computer manufacturers from this table:
>>> q = select(Product.manufacturer).order_by(Product.manufacturer)
>>> session.scalars(q).all()
['Acorn Computers Ltd', 'Acorn Computers Ltd', ..., 'West Computer AS']
But of course, this has a problem. Even though the query retrieves only manufacturers, the queried table has products in it, so each result row corresponds to a product, and manufacturers that have more than one product in the database appear multiple times. Acorn Computers Ltd, the first manufacturer when sorting alphabetically, appears as the first six results because it has six different computer models.
Whenever a database query can return duplicated results, the
distinct()
clause added to it tells the database to combine identical results:
>>> q = select(Product.manufacturer).order_by(Product.manufacturer).distinct()
>>> session.scalars(q).all()
['Acorn Computers Ltd', 'AGAT', ..., 'West Computer AS']
You may be tempted to combine the
distinct()
clause with the
count()
aggregation function to find out how many manufacturers exist in the database. Unfortunately, the
distinct()
clause does not work when using the
count()
aggregation function because the database evaluates the function before
distinct()
. When you need to count unique results, there is a
distinct()
method that can be called on the item being counted, inside the
count()
function:
>>> q = select(func.count(Product.manufacturer.distinct()))
>>> session.scalar(q)
76
Merging results with
distinct()
is limited because two rows of results have to be identical for the database to collapse them into one. For example, this solution would not be able to generate a list of manufacturers along with the first and last years each was active, because adding
Product.year
as a second value would change which results
distinct()
merges together.
The
group_by()
clause offers a result grouping solution that has more flexibility. The query above that returns the list of manufacturers can also be created with
group_by()
as follows:
>>> q = (select(Product.manufacturer)
            .group_by(Product.manufacturer)
            .order_by(Product.manufacturer))
The results are the same, but when using
group_by()
, additional columns can be added to the query, as long as they are aggregated into a single value for each group using a function. The next example obtains the list of manufacturers along with their first and last years of operation, and how many models they produced:
>>> q = (select(
            Product.manufacturer,
            func.min(Product.year),
            func.max(Product.year),
            func.count()
        )
        .group_by(Product.manufacturer)
        .order_by(Product.manufacturer))
>>> session.execute(q).all()
[('Acorn Computers Ltd', 1980, 1995, 6), ..., ('West Computer AS', 1984, 1984, 1)]
When grouping in this way, the database uses functions such as
min()
,
max()
and
count()
to reduce the different values in the groups of entries that are being merged. A query that uses
group_by()
can have result values that are either explicitly referenced in the
group_by()
call, or that are aggregated with a function. Having any other result values would produce an error because it would not be possible to include multiple rows of values in a grouped result row.
Previously you've seen that the
where()
method can be used to filter the set of results returned by a query. The conditions given in
where()
are evaluated before results are grouped, so this clause cannot be used to filter grouped results. Similar to
where()
, the
having()
clause is used to filter the grouped and aggregated results. Below is a query that gets a list of manufacturers that have five or more models, along with the actual number:
>>> q = (select(
            Product.manufacturer,
            func.count()
        )
        .group_by(Product.manufacturer)
        .having(func.count() >= 5)
        .order_by(Product.manufacturer))
>>> session.execute(q).all()
[('Acorn Computers Ltd', 6), ('Amstrad', 7), ..., ('Timex Sinclair', 6)]
You may notice that in this example, the
count()
function appears twice. First it is used in the
select()
part so that it is included in the results, and then a second time in the
having()
method, so that entries can be filtered according to this value.
To ensure that the count of products per manufacturer is written only once, the
label()
method can be used to associate a label to the calculation, and then the label can be used in the two locations it is needed:
>>> num_products = func.count().label(None)
>>> q = (select(
            Product.manufacturer,
            num_products
        )
        .group_by(Product.manufacturer)
        .having(num_products >= 5)
        .order_by(Product.manufacturer))
The argument to the
label()
method is a name for the label, which is generated automatically by SQLAlchemy when given as
None
, ensuring that a unique name is picked. Letting SQLAlchemy pick the name is okay because what matters is that the label instance is assigned to the
num_products
variable, but in any case, if you prefer to also provide a name for the label, that is also allowed:
>>> num_products = func.count().label('num_products')
Pagination
For queries that return a large list of results, a common practice is to limit the number of results returned to some maximum number. The
limit()
method added to a query sets a maximum number of results. In the next query, up to three products are returned in alphabetical order:
>>> q = select(Product).order_by(Product.name).limit(3)
>>> session.scalars(q).all()
[Product(10, "464 Plus"), Product(11, "6128 Plus"), Product(6, "A7000")]
Putting a limit to the number of results is a good practice that prevents queries from retrieving too many results and becoming too large to handle. A common pattern when potentially long queries are issued is to provide
pagination
options, so that the results can be retrieved in chunks. In interactive or web applications users are often given the option to move forward and backwards on the results in increments of a given page size.
Implementing pagination of query results involves setting a page size with the
limit()
method, and indicating at which position to start retrieving results.
The simplest approach to select a start position is to add the
offset()
method to the query. This method sets a start index for the results to retrieve. The example query above could be generalized by adding
offset(0)
to it. A query to retrieve the second page of three results would be done as follows:
>>> q = select(Product).order_by(Product.name).limit(3).offset(3)
>>> session.scalars(q).all()
[Product(131, "Aamber Pegasus"), Product(84, "ABC 80"), Product(5, "Acorn Archimedes")]
Using
offset()
for pagination is often considered problematic, first because in most databases it does not have an efficient implementation, but more importantly because it may provide confusing results for datasets that change often. Continuing with the above examples, if a new product called "AAA" is added to the
products
table after a user viewed the second page of results, when the user requests the third page all the positions would have shifted one place down, and the "Acorn Archimedes" would appear again as the first item when
offset(6)
is requested. Similarly, if a product is deleted, all positions after the deleted item would shift one place up, and a product might be skipped when moving to the next page of results.
A more robust way of specifying where to start returning results is to use the last returned item as a reference. To request the second page of results using this method the query would be:
>>> q = select(Product).order_by(Product.name).where(Product.name > 'A7000').limit(3)
This query returns the same results as above, but has the advantage that items that are inserted or deleted will not cause any results to be repeated or omitted. The disadvantage is that when navigating the list of results backwards things get slightly more complicated. After seeing the second page of results, a query to go back to the first page would look like this:
>>> q = (select(Product)
            .order_by(Product.name.desc())
            .where(Product.name < 'Aamber Pegasus')
            .limit(3))
>>> session.scalars(q).all()
[Product(6, "A7000"), Product(11, "6128 Plus"), Product(10, "464 Plus")]
But this does not look like the first page anymore. The
order_by()
clause had to be reversed with
desc()
so that the query can reference the three items that appear right before the "Aamber Pegasus" product that starts the second page, and this causes the results to be in reverse order. The application will need to reverse these results before they are presented to the user.
Which of the two pagination solutions to use is a decision that needs to be made for each particular case. The
offset()
method is simpler to implement and allows a user to randomly request any page of results, since the offset can be calculated with just a multiplication. If the dataset rarely changes, this may be the best option.
The alternative solution using a
where()
clause is very robust as it will never duplicate or skip any items as the data changes, but that comes at a cost of a more complex implementation. Also, the
where()
solution does not allow random jumps, the user can only move forward or backwards one page at a time.
Obtain an Element by its Primary Key
A particularly useful query is one that retrieves the element in a database table that matches a given primary key value. This query can return one result when the item in question is found, or no results at all when the given key value does not exist. The query will never return more than one result, because primary keys are unique by definition. Using what you learned above, you can already build a query for this purpose. Below is an example query that retrieves the product that has its
id
set to 23:
>>> q = select(Product).where(Product.id == 23)
>>> session.scalar(q)
Product(23, "CT-80")
This is such a common query that SQLAlchemy implements a shortcut for it. The next example shows how to issue the same query as above using the
get()
method of the session object:
>>> session.get(Product, 23)
Product(23, "CT-80")
As with the longer form above, if the given primary key value does not exist in the database table, the return value is
None
.
Indexes
You may be wondering how can the database search information, and do so efficiently. Databases implement a variety of algorithms to navigate the data, and when given a specific query to execute they determine which of those algorithms are applicable and the most efficient to use.
There is one search algorithm that is always available: the
table scan
. A table scan operation consists in evaluating the query filters on all the rows of a table sequentially as the entries are read. This does not seem very efficient, does it?
Table scans are a last resort, an operation that the database will only use when no other option is available, or also when the data to search is small enough that there is no advantage in using a more sophisticated searching algorithm.
Your job as a database designer is to study the queries that the application makes and ensure that the data is properly
indexed
to support more advanced searching options when solving those queries.
When a column is marked as indexed, the database will maintain binary tree structures for the data in that column that allow for very efficient searching and sorting. Looking through the example queries shown in this chapter, searching is done on the following columns of the
products
table:
id
name
manufacturer
year
The
id
column is the table's primary key, which the database automatically indexes, so searches on this column are already optimized. The
name
,
manufacturer
and
year
columns, however, are used in
where()
,
group_by()
and
order_by()
clauses and are currently not indexed, which means that the table will have to be scanned when these columns are in a query.
What about the remaining two columns,
country
and
cpu
? These columns are not referenced in any of the example queries, so based on these queries there is no benefit in indexing them, and in fact, there are costs both in performance and disk space associated with maintaining indexes, so for these two columns it is best to not index them. This decision will need to be re-evaluated if other queries involving these columns are implemented later.
When using SQLAlchemy, a column can be marked as indexed with a
index=True
option added to it in the model definition. Here is the
Product
model class expanded with indexes:
models.py
: indexes added to model
class Product(Model):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True)
    manufacturer: Mapped[str] = mapped_column(String(64), index=True)
    year: Mapped[int] = mapped_column(index=True)
    country: Mapped[str] = mapped_column(String(32))
    cpu: Mapped[str] = mapped_column(String(32))

    def __repr__(self):
        return f'Product({self.id}, "{self.name}")'
Constraints
Another good database design practice is to assign appropriate
constraints
to columns. The
Product
model already has a constraint called
PRIMARY KEY
, which is enabled on the
id
column with the
primary_key=True
option. This names the
id
column as the primary key of the
products
table.
Besides
PRIMARY KEY
, two other commonly used constraints are
UNIQUE
and
NOT NULL
.
A column that has a
UNIQUE
constraint does not allow duplicated values. In the
Product
model, this would be a good choice for the
name
column, to ensure that there are no two products with the same name.  To add this constraint to a column, the
unique=True
option is used with SQLAlchemy.
The
NOT NULL
constraint prevents a column from ever having an empty or undefined value. This constraint can also be thought of in reverse, by saying that columns that do not have the
NOT NULL
constraint are considered optional. Columns defined with the
Mapped[t]
typing syntax get the
NOT NULL
constraint by default, and to create a column that is allowed to have
NULL
values, the type hint should be changed to
Mapped[Optional[t]]
. The
country
and
cpu
can be considered optional at this point, but as always, this may need to change as the role of these columns is better defined.
Note:
When working with the legacy column definition syntax in SQLAlchemy 1.x versions that is based on the
Column()
constructor, the
nullable=True
option is the default and is used to denote an optional column, while
nullable=False
must be added for columns for which a value is required.
Below you can see an updated
Product
model class, with constraints added.
models.py
: constraints added to model
# ...
from typing import Optional

class Product(Model):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    manufacturer: Mapped[str] = mapped_column(String(64), index=True)
    year: Mapped[int] = mapped_column(index=True)
    country: Mapped[Optional[str]] = mapped_column(String(32))
    cpu: Mapped[Optional[str]] = mapped_column(String(32))

    def __repr__(self):
        return f'Product({self.id}, "{self.name}")'
Deletions
You've seen above that new objects are added to the database using the
add()
method of the session, and that this schedules the new object to be saved to the database in the next commit operation. The session also has a
delete()
method.
If you have left your Python prompt, start a new one and initialize it as before:
>>> from db import Session
>>> from models import Product
>>> session = Session()
Now try deleting a product:
>>> p = session.get(Product, 23)
>>> session.delete(p)
>>> session.commit()
Once a session having deleted objects is committed, these objects are effectively removed and cannot be retrieved anymore.
>>> p = session.get(Product, 23)
>>> print(p)
None
Exercises
Many of the chapters in this book include a list of exercises that can help you solidify the knowledge you acquired in the chapter. Solutions to all exercises are provided at the end of the book.
Before you attempt to solve these exercises, make sure that you have all the products imported. If you are in doubt that you have a complete database you can run the importer script once again:
(venv) $ python import_products.py
Start a Python session and write queries that return the following information:
The first three products in alphabetical order built in the year 1983.
Products that use the "Z80" CPU or any of its clones. Assume that all products based on this CPU have the word "Z80" in the
cpu
column.
Products that use either the "Z80" or the "6502" CPUs, or any of its clones, built before 1990, sorted alphabetically by name.
The manufacturers that built products in the 1980s.
Manufacturers whose names start with the letter "T", sorted alphabetically.
The first and last years in which products have been built in Croatia, along with the number of products built.
The number of products that were built each year. The results should start from the year with the most products, to the year with the least. Years in which no products were built do not need to be included.
The number of manufacturers in the United States (note that the
country
field for these products is set to
USA
)
Proceed to
Chapter 3
.
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
