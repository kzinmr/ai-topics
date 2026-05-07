---
title: "SQLAlchemy 2 In Practice - Chapter 7: Asynchronous SQLAlchemy"
url: "https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-7-asynchronous-sqlalchemy"
fetched_at: 2026-05-07T07:01:38.505313+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# SQLAlchemy 2 In Practice - Chapter 7: Asynchronous SQLAlchemy

Source: https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-7-asynchronous-sqlalchemy

This is the seventh chapter of my
SQLAlchemy 2 in Practice
book. If you'd like to support my work, I encourage you to buy this book, either directly from
my store
or on
Amazon
. Thank you!
Starting with release 1.4, SQLAlchemy includes support for asynchronous programming with the
asyncio
package, for both the Core and ORM modules. This is an exciting improvement that brings the power of SQLAlchemy to modern applications such as those written with the FastAPI web framework.
For your reference, here is a summary of the book contents:
In this chapter you are going to learn how the asynchronous support in SQLAlchemy works by adapting all the work done in previous chapters to the asynchronous model.
How is Async Different?
The asynchronous programming paradigm introduces some differences in the execution model of an application.
One of the aspects that make asynchronous programming difficult is what has been brilliantly described as
function coloring
, which is a metaphor for the limitations Python and other languages have in regard to the mixing of synchronous and asynchronous code.
In short, function coloring means that asynchronous applications should avoid long-running synchronous functions because these are
blocking
and prevent concurrency. As a result of this limitation, a web application that uses SQLAlchemy needs asynchronous code in all of its layers, which from top to bottom may include:
Web server
Web framework
Route logic
SQLAlchemy session
SQLAlchemy engine
Database driver
While it is obvious that an asynchronous web application needs a server and a framework that are also asynchronous, the requirement extends to the lower layers as well. That means that any application functions that use SQLAlchemy asynchronously must be
async
functions, and the session and engine objects have to be replaced with asynchronous equivalents. Finally, the database driver must also be designed to work asynchronously.
Another important difference is related to implicit database activity. SQLAlchemy ORM is a high-level database framework that sometimes decides on its own to issue database queries. The best example of this are the relationship attributes that are configured with the default lazy loader, which implicitly run a database query to obtain the results the first time they are accessed.
These implicit behaviors cannot exist in an asynchronous application due to the function coloring limitations of the asynchronous model. All asynchronous database activity must happen inside functions that are asynchronous.
Asynchronous Database Drivers
Starting from the bottom of the stack, to be able to use SQLAlchemy in an asynchronous application you must use a compatible database driver. None of the regular database drivers mentioned earlier in the book can be used asynchronously.
The following sections discuss what options are available for the three major open-source databases. If you are not using any of these databases, you can find your
database dialect
in the SQLAlchemy documentation, where you can look for asynchronous driver options.
SQLite
The
sqlite
module that comes with the Python interpreter does not support the asynchronous model. To be able to work with SQLite from asynchronous code, SQLAlchemy supports the
aiosqlite
third-party package, which needs to be installed into your virtual environment as follows:
(venv) $ pip install aiosqlite
The database connection URL given to SQLAlchemy needs to be modified to reflect the use of this driver. As you recall, database URLs specify the dialect and the driver in the scheme portion of the URL separated by a
+
sign. Below is an example URL for the
aiosqlite
driver:
DATABASE_URL=sqlite+aiosqlite:///retrofun.sqlite
MySQL
When using MySQL or MariaDB, SQLAlchemy 2.0 supports two asynchronous drivers:
aiomysql
and
asyncmy
.
You have to install the chosen package into your virtual environment. For example, here is how to install
aiomysql
:
(venv) $ pip install aiomysql
Then the dialect portion of the database connection URL must be changed to reflect the driver in use. Example:
DATABASE_URL=mysql+aiomysql://retrofun:my-password@localhost:3306/retrofun
PostgreSQL
For PostgreSQL, the
asyncpg
driver is currently the only asynchronous option.
As with all the other databases, the package needs to be installed:
(venv) $ pip install asyncpg
Your database connection URL must have
asyncpg
in the dialect part. For example:
DATABASE_URL=postgresql+asyncpg://retrofun:my-password@localhost:5432/retrofun
Engines, Metadata and Sessions
SQLAlchemy comes with an
asynchronous extension
that provides alternative engine and session objects. These have the same interfaces as the regular ones you used in previous chapters, but its methods are awaitable.
Below you can see a version of
db.py
that is appropriate for an asynchronous application. If you intend to run this code on your computer, you can create a new project directory for the asynchronous code, so that you can keep the code from previous chapters available in case you need it.
db.py
: Asynchronous engine, metadata and sessions
import os
from dotenv import load_dotenv
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
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

engine = create_async_engine(os.environ['DATABASE_URL'])
Session = async_sessionmaker(engine, expire_on_commit=False)
As you see, there aren't that many differences from the synchronous version. Instead of
create_engine()
this version uses
create_async_engine()
, and instead of
sessionmaker
it uses
async_sessionmaker
.
The only other difference is the
expire_on_commit=False
option configured for the session. This disables a default SQLAlchemy behavior that marks models as
expired
after the session is committed. Models that are marked as expired are implicitly refreshed from a database query when any of its attributes are accessed again. Since implicit database activity cannot occur in an asynchronous application, expired objects should not be used. The
expire_on_commit=False
option makes sure no models will ever be marked as expired as a result of a commit.
The disadvantage of not having expired models is that when using long-lived sessions that are committed several times, models will be assumed to always be updated and will never be refreshed from the database. In a situation where the database can be modified by different processes this can cause the long-lived session to end up with stale models. To avoid this problem the application can use shorter sessions, or it can also manually
expunge
objects from the session and load them again to ensure their freshness. The
session.expunge()
and
session.expunge_all()
methods can be used to remove models from the session as necessary, and the
session.refresh()
can be used to explicitly update an object from the database.
One interesting aspect of the asynchronous support is that the
MetaData
instance does not have an asynchronous version. This is of particular importance when the
create_all()
and
drop_all()
functions are used, because these do not have awaitable versions. SQLAlchemy provides a
run_sync()
method that can be used to run synchronous database code such as these functions and await them, as shown below:
async with engine.begin() as connection:
    await connection.run_sync(Model.metadata.drop_all)
    await connection.run_sync(Model.metadata.create_all)
Relationships Loaders
For the most part, model definitions do not need to change for an asynchronous application. The one are that needs to be carefully checked is the configuration of the relationship loaders.
You have seen that many of the
relationship()
attributes in the model classes use a lazy loading mechanism that queries the relationship from the database the first time an attribute is accessed. You have also seen that the
lazy
argument, the
options()
query clause, and the
WriteOnlyMapped
typing hint can all be used to change this behavior. The default lazy behavior, which maps to
lazy='select'
or
options(lazyload(...))
, is incompatible with asynchronous applications, so it has to be changed to a loader with a more predictable behavior.
But what to use instead? Here is once again the table that shows all the available loaders, categorized by when the database is accessed:
When
Loaders
Lazy load
select
(default),
dynamic
(legacy)
Eager load
joined
,
selectin
,
subquery
,
immediate
Explicit load
write_only
(SQLAlchemy 2.0 and up),
noload
,
raise
,
raise_on_sql
The lazy loaders are out, so the main choice you have to make for each relationship object is if it should be loaded eagerly along with its parent model or explicitly only when and if needed. Once you decide which of the two makes most sense you can look at the different options each method offers. Some relationships were already changed from the lazy default to
write_only
, and those do not need to change since this loader never issues implicit database queries.
A safe choice is to change all the lazy loading relationships to
lazy='raise'
, so that they raise an error if SQLAlchemy would need to lazy load them. With this in place, the application can explicitly pass one of the eager loaders in an
options()
clause as an explicit override when a relationship needs to be loaded.
Another option is to pick appropriate loaders for all relationships to avoid any possibility of relationships being lazy loaded. This is how all the relationships in the RetroFun database will be changed to avoid implicit database queries:
The "one" side relationships will use the
joined
eager loader. If the relationship is not optional, the
innerjoin=True
option will be added to tell SQLAlchemy to use an inner join, which is often more efficient than the default left outer join this loader uses.
The "many" relationships that use the
write_only
loader will not be changed, as these are compatible with asynchronous code.
The remaining "many" relationships will use the
selectin
eager loader, which often performs better than
joined
when there are multiple items in the relationship.
The following code block shows all the updates that need to be made to the relationships. No other changes need to be made in
models.py
beyond that. If you intend to try the asynchronous solution, copy the
models.py
from the previous chapter to the directory where you are building the asynchronous project and edit the relationships as shown below.
models.py
: Asynchronous-friendly relationships
# ...

class Product(Model):
    # ...
    manufacturer: Mapped['Manufacturer'] = relationship(
        lazy='joined', innerjoin=True, back_populates='products')
    countries: Mapped[list['Country']] = relationship(
        lazy='selectin', secondary=ProductCountry, back_populates='products')
    order_items: WriteOnlyMapped['OrderItem'] = relationship(
        back_populates='product')
    product_reviews: WriteOnlyMapped['ProductReview'] = relationship(
        back_populates='product')
    blog_articles: WriteOnlyMapped['BlogArticle'] = relationship(
        back_populates='product')
    # ...


class Manufacturer(Model):
    # ...
    products: Mapped[list['Product']] = relationship(
        lazy='selectin', cascade='all, delete-orphan',
        back_populates='manufacturer')
    # ...


class Country(Model):
    # ...
    products: Mapped[list['Product']] = relationship(
        lazy='selectin', secondary=ProductCountry,
        back_populates='countries')
    # ...


class Order(Model):
    # ...
    customer: Mapped['Customer'] = relationship(
        lazy='joined', innerjoin=True, back_populates='orders')
    order_items: Mapped[list['OrderItem']] = relationship(
        lazy='selectin', back_populates='order')
    # ...


class Customer(Model):
    # ...
    orders: WriteOnlyMapped['Order'] = relationship(back_populates='customer')
    product_reviews: WriteOnlyMapped['ProductReview'] = relationship(
        back_populates='customer')
    blog_users: WriteOnlyMapped['BlogUser'] = relationship(
        back_populates='customer')
    # ...


class OrderItem(Model):
    # ...
    product: Mapped['Product'] = relationship(
        lazy='joined', innerjoin=True, back_populates='order_items')
    order: Mapped['Order'] = relationship(
        lazy='joined', innerjoin=True, back_populates='order_items')
    # ...


class ProductReview(Model):
    # ...
    product: Mapped['Product'] = relationship(
        lazy='joined', innerjoin=True, back_populates='product_reviews')
    customer: Mapped['Customer'] = relationship(
        lazy='joined', innerjoin=True, back_populates='product_reviews')
    # ...


class BlogArticle(Model):
    # ...
    author: Mapped['BlogAuthor'] = relationship(
        lazy='joined', innerjoin=True, back_populates='articles')
    product: Mapped[Optional['Product']] = relationship(
        lazy='joined', back_populates='blog_articles')
    views: WriteOnlyMapped['BlogView'] = relationship(back_populates='article')
    language: Mapped[Optional['Language']] = relationship(
        lazy='joined', back_populates='blog_articles')
    translation_of: Mapped[Optional['BlogArticle']] = relationship(
        lazy='joined', remote_side=id, back_populates='translations')
    translations: Mapped[list['BlogArticle']] = relationship(
        lazy='selectin', back_populates='translation_of')
    # ...


class BlogAuthor(Model):
    # ...
    articles: WriteOnlyMapped['BlogArticle'] = relationship(
        back_populates='author')
    # ...


class BlogUser(Model):
    # ...
    customer: Mapped[Optional['Customer']] = relationship(
        lazy='joined', back_populates='blog_users')
    sessions: WriteOnlyMapped['BlogSession'] = relationship(
        back_populates='user')
    # ...


class BlogSession(Model):
    # ...
    user: Mapped['BlogUser'] = relationship(
        lazy='joined', innerjoin=True, back_populates='sessions')
    views: WriteOnlyMapped['BlogView'] = relationship(back_populates='session')
    # ...


class BlogView(Model):
    # ...
    article: Mapped['BlogArticle'] = relationship(
        lazy='joined', innerjoin=True, back_populates='views')
    session: Mapped['BlogSession'] = relationship(
        lazy='joined', innerjoin=True, back_populates='views')
    # ...


class Language(Model):
    # ...
    blog_articles: WriteOnlyMapped['BlogArticle'] = relationship(
        back_populates='language')
    # ...
Alembic Configuration
Database migrations is another area that requires some minimal changes when switching to the asynchronous programming model. Alembic uses the concept of
templates
to generate the contents of the migration repositories that it creates with the
init
command, in particular the
env.py
and
alembic.ini
files. The default Alembic template, which you used for the RetroFun database in previous chapters, assumes your database engine and driver are synchronous.
Alembic ships with an asynchronous template that can be used when initializing a migration repository. The command below creates the repository with this template. If you want to try this command, make sure you have the asynchronous versions of
db.py
and
models.py
in a separate directory that does not have a migration repository created.
(venv) $ alembic init -t async migrations
The resulting
env.py
file in the
migrations
subdirectory will have a few minor differences with the one based on the default template.
As you've done before, this file needs to be edited so that Alembic knows about the project's database. The changes are similar to those made in the synchronous version. First, add the imports at the top:
migrations/env.py
: Alembic imports
from db import Model, engine
import models
Then find the line that initializes the
target_metadata
variable and enter the following code in its place:
migrations/env.py
: Configure the project's database into Alembic
target_metadata = Model.metadata
config.set_main_option("sqlalchemy.url", engine.url.render_as_string(
    hide_password=False))
The last change is to enable the batch migration mode. This is especially important if you are using SQLite because this database has limited migration capabilities on its own, but it can be safely enabled for all databases. Find the
context.configure()
call in the
do_run_migrations()
function, and make sure it includes the
render_as_batch=True
option.
migrations/env.py
: Configure batch mode
def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata,
                      run_as_batch=True)

    with context.begin_transaction():
        context.run_migrations()
Now Alembic is fully configured, and you should be able to generate an initial database migration. Before you run the following command, make sure your
.env
file has the
DATABASE_URL
variable configured with an asynchronous database driver as shown above, and also that you have configured a brand-new database and not the same one you've used before.
(venv) $ alembic revision --autogenerate -m "initial migration"
This command will scan your database models and compare them with the still empty database, so the initial database migration is going to include all the tables, indexes and constraints that map to these models.
Now that the migration script is in place, the database can be migrated with it:
(venv) $ alembic upgrade head
Implicit I/O After a Session is Flushed
With the changes made above to the models, almost all implicit database activity is now disabled. There is one remaining implicit situation that occurs when a session that has new objects is flushed.
In the context of a session, a
flush()
operation writes all the outstanding changes that were accumulated in the session to the underlying database transaction, so that they are known to the database. Flushes are often issued automatically by SQLAlchemy because sessions have their
autoflush
option enabled by default, which issues a
flush()
call before a database query to ensure that the query includes results from the session that have not been committed yet.
For the most part, a
flush()
call does not cause issues, but there is one particular situation in which it does. If the session has new objects that have just been added, and these objects have list-style relationship attributes that have not been initialized, then when these objects are flushed the uninitialized relationships will be marked as not loaded, which means that the next time they are accessed a lazy load attempt will be made on them.
This problem is somewhat obscure, so it may be hard to understand how it can affect an application. If you have made all the updates for asynchronous compatibility, you can trigger this error easily in a Python session to understand it better. Start an async-friendly Python session with the following command:
(venv) $ python -m asyncio
The difference between this and just running
python
is that with this command it is possible to use the
await
keyword directly from the prompt. A regular Python session only allows
await
inside functions declared with
async def
.
Here is a simple demonstration of the error after flush:
>>> from db import Session
>>> from models import Customer, Order
>>> session = Session()
>>> c = Customer(name='Susan')  # order_items has not been initialized explicitly
>>> o = Order(customer=c)
>>> session.add(o)
>>> o.order_items  # no error before flush
[]
>>> await session.flush()  # flush marks the order_items relationship as unloaded
>>> o.order_items  # error after flush!
Traceback ...
There are several ways to avoid lazy loading of relationships after the session is flushed:
Use the
write_only
loading mechanism for all the list-style relationships. This loader requires the application to load the relationship explicitly, so it will never trigger a lazy load operation.
Use the
raise
loader for all the list-style relationships and override this loader through an
options()
clause when the relationship needs to be loaded. This solution does not solve the problem, but it will alert you if the application ever attempts to lazy load a relationship with an error that is less cryptic than the one above.
Disable the
autoflush
option in the session, even though this may produce unexpected query results that do not include outstanding changes in the session, because without the flush these would not be known to the database until a
commit()
is issued. If you are interested in trying this out, here is how you can reconfigure the asynchronous session to not issue flushes before queries:
python
  Session = async_sessionmaker(engine, expire_on_commit=False, autoflush=False)
- Ensure that all the list-style relationships are initialized to a value before the session is flushed. This will make SQLAlchemy flush the relationship as well, and preserve their value after the flush.
These solutions all have their pros and cons, so you should evaluate which one provides the most value for your application. The last proposed solution is the one that imposes the least amount of restrictions, as it can work with the
autoflush
option enabled, while also allowing the relationship loaders that use list semantics. So that is the solution that will be implemented for the asynchronous version of the RetroFun database.
The simplest option to initialize a relationship before the session is flushed is to do it explicitly. Continuing with the above example, here is how to create an
Order
model instance and initialize its
Order.order_items
relationship:
>>> await session.rollback()  # clear the errored session state from above
>>> o = Order(customer=c, order_items=[])  # order_items is given an initial value
>>> session.add(o)
>>> await session.flush()
>>> o.order_items  # the initial value is preserved after the flush
[]
To avoid having to remember to initialize relationships every time a new object is created, it is possible to expand the
Model
class to automatically initialize all list-based relationships to an empty list. An implementation of this idea is shown below.
db.py
: Initialize all list relationships
from sqlalchemy import event, inspect

# ...

@event.listens_for(Model, "init", propagate=True)
def init_relationships(tgt, arg, kw):
    mapper = inspect(tgt.__class__)
    for arg in mapper.relationships:
        if arg.collection_class is None and arg.uselist:
            continue  # skip write-only and similar relationships
        if arg.key not in kw:
            kw.setdefault(
                arg.key, None if not arg.uselist else arg.collection_class())
The
init_relationships()
function needs to be added at the bottom of
db.py
. The
@event.listens_for()
decorator added to the function registers the function as a handler that is invoked by SQLAlchemy when the
init
event of
Model
occurs, which means that the function will be called every time a new
Model
instance is created. The
propagate=True
option extends this event handler to all subclasses of
Model
, effectively including this behavior in all the models defined by the application.
The body of the function uses SQLAlchemy's
inspect()
function to perform introspection on the model classes and find all those relationships that need to be initialized.
Note:
The
event
and
inspect
features of SQLAlchemy are not covered in this book beyond the above example. If you are interested in learning more about them, you can find them in the official documentation:
Import Scripts
Before you get to experience the asynchronous database by running some queries, it is necessary to import all the CSV data files, but to be able to do this the import scripts also have to be adapted to work as asynchronous applications.
The general structure of each import script has to change to use
asyncio
. Here is how the scripts will be structured:
import asyncio

async def main():
    # ... import logic here

if __name__ == '__main__':
    asyncio.run(main())
Database sessions use asynchronous context managers, so
with
statements have to be changed to
async with
. Example:
async with Session() as session:
        async with session.begin():
            # ... do database work here
Finally, queries and commits are now executed asynchronously, so they need to be awaited. This means that all the
session.execute()
,
session.scalar()
and
session.commit()
calls in these scripts have to be prepended with
await
.
After making these changes, the scripts will be fully compatible with the
asyncio
support in SQLAlchemy. If you don't want to copy the scripts from the previous chapter and adapt them yourself, you can find the asynchronous versions in the book's
GitHub repository
.
To import all the data you have to run all the importer scripts in order, as shown below:
(venv) $ python import_products.py
(venv) $ python import_orders.py
(venv) $ python import_reviews.py
(venv) $ python import_articles.py
(venv) $ python import_views.py
(venv) $ python import_languages.py
Queries
By now you probably have an idea of how to run many database queries, so what are the changes to run them asynchronously? The good news is that the queries themselves are constructed exactly as before. The query API does not need an asynchronous version because there are no long-running or blocking functions in it.
The
session.execute()
,
session.scalars()
and
session.scalar()
functions, however, have to be awaited as they run asynchronously. In addition, the asynchronous session offers two additional execution methods called
session.stream()
and
session.stream_scalars()
that are demonstrated below.
Start by running a fresh asynchronous Python shell:
(venv) $ python -m asyncio
As discussed above, this will make the entire shell session run inside an
asyncio
loop, giving you the possibility of use
await
directly in the prompt, without having to create a wrapper function.
Now you can import all the needed symbols and manually start a database session:
>>> from sqlalchemy import select
>>> from db import Session
>>> from models import Product, Customer, Order
>>> session = Session()
Start by retrieving the "Commodore 64" product:
>>> c64 = await session.scalar(
        select(Product)
            .where(Product.name == 'Commodore 64'))
>>> c64
Product(41, "Commodore 64")
The
manufacturer
and
countries
relationships in the
Product
model were configured with the
joined
and
selectin
eager loaders respectively, so they were automatically loaded when the query above was issued. This can be confirmed:
>>> c64.manufacturer
Manufacturer(14, "Commodore")
>>> c64.countries
[Country(3, "USA")]
Let's try to get the last customer in alphabetical order:
>>> c = await session.scalar(
        select(Customer)
            .order_by(Customer.name.desc())
            .limit(1))
>>> c
Customer(e084528681ab4cb7bf45413ad6c7ce45, "Zoe Bradley")
All the relationships in the
Customer
model use the
write_only
loader. As you've seen in previous chapters, to get the items in the relationship, the select query returned by the relationship attribute has to be manually executed. The next example gets the last two orders from this customer:
>>> r = await session.scalars(
        c.orders.select()
            .order_by(Order.timestamp.desc())
            .limit(2))
>>> r.all()
[Order(eaf9c1386a514c9781bdd849f7e99787), Order(db2c90dcc4ae4072b12a58496f47f5cf)]
Here, the query to obtain the orders is returned by the
select()
method of the
Customer.orders
relationship attribute. Because this is a query object, it can be expanded with additional clauses before it is executed in the session, giving the most freedom in accessing relationships, especially if they can potentially have many elements.
Streamed Results
As you have seen, the
execute()
and
scalars()
methods return a results object that is a standard, non-asynchronous Python iterable, and this is the case also when using an asynchronous session.
When using standard Python the results object is very efficient, as it only loads one item at a time from the database. However, when using the asynchronous session SQLAlchemy is forced to retrieve the entire list of results from the database before returning the results, because asynchronous activity is not possible inside a standard Python iterable. So these results are not efficient when using asynchronous code, especially for large queries.
The
stream()
and
stream_scalars()
methods were added to provide the same efficient iteration of results in the asynchronous session. These methods function like the original counterparts, with the only difference that they return an asynchronous version of the results object that supports Python's asynchronous iteration protocol. The last query above can be issued more efficiently as a stream:
>>> r = await session.stream_scalars(
        c.orders.select()
            .order_by(Order.timestamp.desc())
            .limit(2))
>>> [order async for order in r]
[Order(eaf9c1386a514c9781bdd849f7e99787), Order(db2c90dcc4ae4072b12a58496f47f5cf)]
Here you can see that the streamed results can be access inside an
async for
loop or list comprehension. The
all()
method is also available for cases that do not benefit from asynchronous iteration.
In general, you should use
stream()
instead of
execute()
when expecting many values per row, and
stream_scalars()
instead of
scalars()
for single value per row queries. The standard
scalar()
,
scalar_one()
and
scalar_or_none()
methods can be used safely in an asynchronous application.
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
