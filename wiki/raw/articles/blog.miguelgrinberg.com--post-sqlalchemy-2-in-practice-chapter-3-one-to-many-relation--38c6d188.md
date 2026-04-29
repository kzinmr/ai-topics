---
title: "SQLAlchemy 2 In Practice - Chapter 3 - One-To-Many Relationships"
url: "https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-3---one-to-many-relationships"
fetched_at: 2026-04-29T07:01:26.540582+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# SQLAlchemy 2 In Practice - Chapter 3 - One-To-Many Relationships

Source: https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-3---one-to-many-relationships

This is the third chapter of my
SQLAlchemy 2 in Practice
book. If you'd like to support my work, I encourage you to buy this book, either directly from
my store
or on
Amazon
. Thank you!
In the previous chapter you learned how to execute a variety of queries on the
products
table. Interestingly, some of those queries were designed to obtain product manufacturers and not products, and this required duplicates to be removed by grouping the results.
For your reference, here is a summary of the book contents:
In many situations, grouping is a great solution, especially when aggregation functions are used to calculate information about each group that is not directly stored in the database. There are cases, however, in which the duplication that occurs when storing secondary data in the same table as the primary entity is problematic, as the table may grow much larger than it needs to be, and spelling differences in the duplicated data could produce incorrect grouped results.
In this chapter you are going to learn how to eliminate duplication by creating multiple related tables using one of the fundamental patterns in relational database design: the
one-to-many
relationship.
When to Use a Relationship
You may be wondering what makes the
manufacturer
column of the
Product
model a good candidate to move to its own separate model class and database table. There isn't a definitive answer on this, just that some entities are intuitively first-class and there is no doubt that they should be independent, while others cannot be identified so easily, and it may require one or more iterations on the database design before the benefit of creating a separate table becomes clear.
As an example, if the RetroFun database had to be extended to store orders from customers, nobody would disagree that these should be stored in their own table. But each order will need customer information. Should customers be in their own table or stored as additional columns with the order? For a business in which it is highly unlikely for customers to make repeat orders you may consider the simpler approach of storing customer details directly with the orders, but for most businesses keeping customer information separately is likely more convenient. Database design decisions aren't absolute and should be made with the needs of the application in mind.
As a rule of thumb, when you find that information is being duplicated, you should consider the benefits of removing this duplication through the addition of a new table and a relationship. In the case of the
manufacturer
column, a separate table means that each company name will exist only once, so there will never be a risk of a spelling mistake affecting how products are grouped. Having the manufacturers in their own table would also make it possible to rename a company name or add other details such as the company address and phone number, and all these changes will have to be made only once and will be immediately accessible to all related products.
What about the other attributes of the
Product
model?
The
country
column is definitely a candidate for a relationship, as with this column once again there is duplication of country names. If grouping by country is desired, then countries would have to be entered with the exact same spelling in every occurrence to be grouped correctly. For example, "United States" and "united states" would be grouped separately because of the case difference.
The
year
column, on the other side, is just numbers, so initially it would not appear as if removing duplication can make a significant improvement. And looking at the contents of the
cpu
field in many of the products it is clear that the field is written as descriptive text and not as a reference to an entity, so it is also not a good candidate to relocate to a separate table, at least if kept in the current format.
In this chapter, you are going to learn how to move the manufacturers into a separate table, and how to build a relationship between products and manufacturers to preserve the information of which company built which product. Applying a similar change to the countries presents additional challenges that will be discussed in the next chapter, so for now only the manufacturer will be addressed.
One-To-Many Relationship Implementation
Relational databases create links between entities stored in different tables through
relationships
. There are two main types of relationships:
Relational database literature will also mention two additional relationship types: the many-to-one and the one-to-one, which are special forms of the one-to-many type.
A one-to-many relationship describes a situation in which two tables A and B are related in such a way that an entry in table A can be linked to any number of entries in table B, but each entry in table B is linked to at most one entry from A. In this scenario table A is the "one" and table B is the "many" of the relationship.
This pattern fits the relationship between computer manufacturers and their computer products. A manufacturer can produce many computer models, and each of these computer models was built by only one manufacturer. So the manufacturer is the "one" and the products are the "many".
The first step when defining a relationship is to create database tables (or models, when using SQLAlchemy ORM) for the two entities involved. The database in its current state has a
products
table, and now it needs a
manufacturers
table. Add a
Manufacturer
model at the bottom of
models.py
to represent manufacturers:
models.py
: Manufacturers model
class Manufacturer(Model):
    __tablename__ = 'manufacturers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, unique=True)

    def __repr__(self):
        return f'Manufacturer({self.id}, "{self.name}")'
With this, the
manufacturer
column from the
Product
model becomes
name
in the new
Manufacturer
model class. The class has its own
id
primary key, and a
__repr__()
implementation to have instances of this class print nicely when debugging. The
name
column has an additional
unique=True
option that adds a
UNIQUE
constraint to the column, because in this table each manufacturer will appear only once.
The
manufacturer
column of
Product
has to be removed, but what can it be replaced with? To establish the relationship, a
manufacturer_id
column is defined in its place:
models.py
: Manufacturer foreign key in Product model
from sqlalchemy import ForeignKey

class Product(Model):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    manufacturer_id: Mapped[int] = mapped_column(
        ForeignKey('manufacturers.id'), index=True)
    year: Mapped[int] = mapped_column(index=True)
    country: Mapped[Optional[str]] = mapped_column(String(32))
    cpu: Mapped[Optional[str]] = mapped_column(String(32))

    def __repr__(self):
        return f'Product({self.id}, "{self.name}")'
The new
manufacturer_id
column is an integer, matching the type of the primary key of the new
Manufacturer
model. Columns that reference primary keys of another table are called
foreign keys
, and are given a foreign key constraint. A good naming convention to follow is to name foreign key columns with the name of the referenced entity followed by the
_id
suffix.
The
ForeignKey
class applies the foreign key constraint to the column. The argument passed to the class indicates what is the primary key target, which can be given as a column object (such as
Manufacturer.id
) or as a string with the format
'<tablename>.<column>'
. Using the string format makes it possible to use forward references to entities that are defined later in the file.
The new
manufacturer_id
column has an index, to help the database navigate this column efficiently. Some databases automatically index foreign key columns, but others do not, so it is best to be explicit and always add an index. It also has the
NOT NULL
constraint, indirectly due to the column's typing hint not including
Optional
. Stating that the foreign key cannot be null ensures that products without a link to a manufacturer are not allowed.
Below you can see a diagram of the database structure with this relationship.
It is useful to remember that one-to-many relationships always follow this style, where the "many" side (products) includes a foreign key column that references the "one" side (manufacturers).
SQLAlchemy Relationships
You now know how one-to-many relationships are implemented in a relational database. But you may be thinking that you will now have to tediously navigate using these primary and foreign keys, and that this can be error-prone, maybe in ways that are more dangerous than having data duplication.
Consider, for example, what an application would need to do to obtain the manufacturer of a given product. When manufacturers were in the
products
table, you could obtain the manufacturer very easily:
>>> p = session.get(Product, 127)
>>> p
Product(127, "ZX Spectrum")
>>> p.manufacturer
'Sinclair Research'
Having the data broken down into separate tables creates a complication, because now a product can only provide access to its
manufacturer_id
attribute, which is a number. Then this number has to be used to load the manufacturer from the new
manufacturers
table.
Fortunately the ORM module of SQLAlchemy provides high-level support for relationships, making most of the work of navigating foreign keys invisible. To gain access to these features, the two model classes involved in a relationship need
relationship
attributes that represent this relationship. Below you can see how these objects are defined for
Product
and
Manufacturer
. Note that these relationship objects are added to each model, without changing any of its existing attributes.
models.py
: Define relationship objects for one-to-many relationship
from sqlalchemy.orm import relationship

class Product(Model):
    # ...
    manufacturer: Mapped['Manufacturer'] = relationship(
        back_populates='products')
    # ...

class Manufacturer(Model):
    # ...
    products: Mapped[list['Product']] = relationship(
        back_populates='manufacturer')
    # ...
The
Product
class now has a
manufacturer
attribute that represents the relationship as seen from the "many" side. This attribute is not a column that is physically stored in the database; it is a high-level replacement of
manufacturer_id
that transparently loads the related model object, as you will see soon.
The change in the
Manufacturer
class is also interesting. This class has a new
products
attribute, representing the same relationship but as seen from the "one" side. From this side, a manufacturer can have many related products, so this attribute is a list that is automatically populated with the corresponding product instances.
The typing hints given to the relationship attributes are based on the same
Mapped[x]
type used for columns, but for these the
x
is the model class for the other side of the relationship, either on its own for the "one" side or as a
list
for the "many" side. As in many other cases before, the class names can be given directly, or as a string. Using a string is often necessary to prevent errors when needing to use a forward reference. For consistency, you may opt to always use strings.
The two
relationship()
definitions have
back_populates
arguments, each set to the name of the relationship attribute on the other side. This is so that SQLAlchemy understands that these two attributes represent the two sides of the same relationship.
If these relationships seem confusing do not worry, you will find them much easier to understand soon, once you start using them.
A Revised Importer Application
The changes made to the models mean that the product importer script from the previous chapter has to be updated so that it now imports manufacturers to their own table.
Below is the updated importer script, which is still stored in
import_products.py
. The same CSV file is used.
import_products.py
: Import products and manufacturers from CSV file
import csv
from db import Model, Session, engine
from models import Product, Manufacturer


def main():
    Model.metadata.drop_all(engine)  # warning: this deletes all data!
    Model.metadata.create_all(engine)

    with Session() as session:
        with session.begin():
            with open('products.csv') as f:
                reader = csv.DictReader(f)
                all_manufacturers = {}

                for row in reader:
                    row['year'] = int(row['year'])

                    manufacturer = row.pop('manufacturer')
                    p = Product(**row)

                    if manufacturer not in all_manufacturers:
                        m = Manufacturer(name=manufacturer)
                        session.add(m)
                        all_manufacturers[manufacturer] = m
                    all_manufacturers[manufacturer].products.append(p)


if __name__ == '__main__':
    main()
In this version an
all_manufacturers
dictionary is initialized empty above the CSV import for-loop. For each row of the CSV file that is processed, the
manufacturer
field is extracted from the
row
dictionary before the items in this dictionary are used to initialize the
Product
instance. This is necessary because
manufacturer
isn't a column in the
Product
model anymore.
The manufacturer name is checked for existence in the
all_manufacturers
dictionary. When not found, a new
Manufacturer
object is created and initialized with that name. The new manufacturer object is added to the SQLAlchemy session so that it is later saved, and it is also added to the dictionary, so that repeat appearances of this manufacturer all use the same instance.
In the final line of the loop, the new product is appended to the
products
relationship of the manufacturer, which works similarly to a list. This
products
relationship object, which represents the "many" side, has
append()
and
remove()
methods, allowing applications to add or remove objects from the relationship using the familiar list syntax. SQLAlchemy automatically translates these operations to the corresponding foreign key changes.
In case you are interested in the details, the
append()
call on the
products
relationship attribute achieves two things: first, it links the manufacturer to the product through the
manufacturer_id
foreign key, which will be automatically set when the session is committed; and second, it indirectly includes the new product in the database session, because it is referenced by the manufacturer instance which has been explicitly added before. An explicit
session.add(p)
for the product would not cause any harm, but it isn't necessary. This automatic addition of a child to the session when the parent is already in it is called a
cascade
. You will learn about this and a few other types of cascades more in detail later.
When the session block ends, all the manufacturers and products that are in the session are saved to the database in a single atomic operation.
Ready to try this new importer? Run the script as follows:
(venv) $ python import_products.py
The
drop_all()
call at the start of the
main()
function will destroy the earlier version of the
products
table, and then
create_all()
will create the new
products
and
manufacturers
tables according to the new models.
Note:
Wiping the entire database each time a change is made is somewhat extreme. In the real world a database cannot afford the disruption of having to be recreated entirely from scratch every time a structural change is made.
In a later chapter you will learn how to implement
database migrations
to manage changes in a more reasonable way.
Feel free to inspect the new database using your database administration tool if you like. Note how the
manufacturer_id
column in the
products
table has numbers, and how these numbers can be used to locate the manufacturer in the
manufacturers
table.
If you inspect your tables, you will notice that the
manufacturer
and
products
relationship objects that were defined in the model classes do not exist in the database. These are virtual attributes that are managed by SQLAlchemy and that only exist in the Python objects, so they do not have a representation in the database.
One-To-Many Relationship Queries
You are probably anxious to see how the SQLAlchemy relationship objects are used in queries. Start a Python shell, import the session class and the models, and create a session:
>>> from sqlalchemy import select
>>> from db import Session
>>> from models import Product, Manufacturer
>>> session = Session()
Load the "ZX Spectrum" product:
>>> p = session.scalar(select(Product).where(Product.name == 'ZX Spectrum'))
>>> p
Product(127, "ZX Spectrum")
Who is the manufacturer of this product? In the single table version,
p.manufacturer
would have returned the name as a string. Now there is a relationship object instead of the string column, and this new attribute transparently returns the model instance that represents the linked entity.
>>> p.manufacturer
Manufacturer(63, "Sinclair Research")
As you recall, the actual string name of this company is stored in the
name
attribute of the model. This name is also easily accessible:
>>> p.manufacturer.name
'Sinclair Research'
Did this manufacturer make other computer models? This can be checked by looking at the one-to-many relationship from the manufacturer's side, which returns a list:
>>> p.manufacturer.products
[Product(125, "ZX80"), Product(126, "ZX81"), Product(127, "ZX Spectrum"),
Product(128, "Sinclair QL")]
It is also possible to start navigating the database from a manufacturer. Let's find Texas Instruments by name and then look at the list of products it made:
>>> m = session.scalar(
        select(Manufacturer)
            .where(Manufacturer.name == 'Texas Instruments'))
>>> m
Manufacturer(66, "Texas Instruments")
>>> m.products
[Product(132, "TI-99/4"), Product(133, "TI-99/4A")]
One of the queries shown in the previous chapter returned product names and manufacturer names side-by-side. This was easy to do when both entities were defined in the same table, but doing this now requires combining information from two tables, an operation that relational databases call a
join
. Here is the query that does this:
>>> q = select(Product.name, Manufacturer.name).join(Product.manufacturer)
>>> session.execute(q).all()
[('Acorn Atom', 'Acorn Computers Ltd'), ..., ('GEM 1000', 'GEM')]
In this query, the
select()
statement names two attributes from different tables. Any time multiple tables are involved in a query, SQLAlchemy needs to know how to join the tables, and that is why the
join()
clause was added. When using the ORM module, the argument to
join()
can be one of the two relationship attributes, and SQLAlchemy figures everything out from it. Since the two relationship objects are linked through the
back_populates
options, in general it does not matter which of the two is given in the
join()
clause. In the example query above, passing
Product.manufacturer
to
join()
means that
Product
will be on the left side of the join, and
Manufacturer
will be on the right. If instead
Manufacturer.products
is passed, then the sides will be reversed, but the results will be the same. Later you will learn about cases in which it does matter what entity is on the left and the right sides of a join.
If you are familiar with how joins are constructed in SQL, you may want to print the query to understand how this is translated to the statement sent to the database:
>>> print(q)
SELECT products.name, manufacturers.name AS name_1
FROM products JOIN manufacturers ON manufacturers.id = products.manufacturer_id
Here you can appreciate how SQLAlchemy ORM defines the join condition on its own thanks to the knowledge it has of the relationship.
Another interesting query from last chapter returned the manufacturers in alphabetical order along with the count of products each made. This also requires a join now that the data is split across two tables:
>>> from sqlalchemy import func
>>> q = (select(
            Manufacturer,
            func.count(Product.id)
        )
        .join(Manufacturer.products)
        .group_by(Manufacturer)
        .order_by(Manufacturer.name))
>>> session.execute(q).all()
[(Manufacturer(1, "Acorn Computers Ltd"), 6), (Manufacturer(24, "AGAT"), 1), ...,
(Manufacturer(75, "West Computer AS"), 1)]
This query isn't the first to have two values per result row, but it is the first in which one of the results is a model and the other isn't. Note the
Manufacturer
model given in the
select()
statement, and again in the
group_by()
. When
group_by()
receives a model class as an argument instead of a single attribute, the grouping is done by all the attributes of the model combined. If you are interested in how this grouping is translated to SQL, you can look at the SQL code for this query:
>>> print(q)
SELECT manufacturers.id, manufacturers.name, count(*) AS count_1
FROM manufacturers JOIN products ON manufacturers.id = products.manufacturer_id
GROUP BY manufacturers.id, manufacturers.name ORDER BY manufacturers.name
I hope you can appreciate how SQLAlchemy greatly simplifies the creation of these queries. Consider that as columns are added or removed from the
manufacturers
table this query will automatically adjust and still be able to group the model as a whole, without any changes needed.
Lazy vs. Eager Relationships
Have you thought about what happens when you access one of these seemingly magical relationship attributes defined in model classes?
A good way to spy on the database activity is to enable the
echo
option in the SQLAlchemy engine object. Open
db.py
in your code editor and add
echo=True
to the
create_engine()
call:
engine = create_engine(os.environ['DATABASE_URL'], echo=True)
Save the change and then open a new Python session. Import all the necessary components again and get the "Texas Instruments" manufacturer as before:
>>> from db import Session
>>> from models import Product, Manufacturer
>>> from sqlalchemy import select
>>> session = Session()
>>> m = session.scalar(
        select(Manufacturer)
            .where(Manufacturer.name == 'Texas Instruments'))
Right after you execute the query with
scalar()
, you will see some activity logged to your terminal. You can see an example of what you might see below, but keep in mind that the output can vary depending on the database that you use.
2023-01-03 18:44:32,185 INFO sqlalchemy.engine.Engine select pg_catalog.version()
2023-01-03 18:44:32,185 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-01-03 18:44:32,188 INFO sqlalchemy.engine.Engine select current_schema()
2023-01-03 18:44:32,188 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-01-03 18:44:32,190 INFO sqlalchemy.engine.Engine show standard_conforming_strings
2023-01-03 18:44:32,190 INFO sqlalchemy.engine.Engine [raw sql] {}
2023-01-03 18:44:32,192 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2023-01-03 18:44:32,197 INFO sqlalchemy.engine.Engine SELECT manufacturers.id,
manufacturers.name
FROM manufacturers
WHERE manufacturers.name = %(name_1)s
2023-01-03 18:44:32,197 INFO sqlalchemy.engine.Engine [generated in 0.00019s]
{'name_1': 'Texas Instruments'}
All the log lines up to and including the
BEGIN
statement are part of the session initialization. The
SELECT
statement is the actual execution of the
scalar()
call, which is followed by a summary line that shows the placeholder values that were used in the query.
This all looks great. Now when you try to access
m
or any of its direct attributes such as
m.name
there is no additional database activity logged, because all the attributes were loaded from the query and are cached in the database session. But see what happens when you try to access the relationship
m.products
:
>>> m
Manufacturer(66, "Texas Instruments")
>>> m.name
'Texas Instruments'
>>> m.products
At this point you are going to see additional database statements appear in the log. SQLAlchemy is running a database query on its own, so that it can provide the list of products that are related to the manufacturer.
2023-01-03 18:46:53,940 INFO sqlalchemy.engine.Engine SELECT products.id AS products_id,
products.name AS products_name, products.manufacturer_id AS products_manufacturer_id,
products.year AS products_year, products.country AS products_country,
products.cpu AS products_cpu
FROM products
WHERE %(param_1)s = products.manufacturer_id
2023-01-03 18:46:53,940 INFO sqlalchemy.engine.Engine [generated in 0.00019s] {'param_1': 66}
If you attempt to access the same relationship a second time, the response will be immediate, as the results are now cached within the context of the database session.
A similar behavior can be observed when navigating the relationship from the other side. Try loading the "ZX Spectrum" product once again:
>>> p = session.get(Product, 127)
The output should include a database query similar to this:
2023-01-03 18:50:42,294 INFO sqlalchemy.engine.Engine SELECT products.id AS products_id,
products.name AS products_name, products.manufacturer_id AS products_manufacturer_id,
products.year AS products_year, products.country AS products_country,
products.cpu AS products_cpu
FROM products
WHERE products.id = %(pk_1)s
2023-01-03 18:50:42,294 INFO sqlalchemy.engine.Engine [generated in 0.00022s] {'pk_1': 127}
You can now access all the attributes of the
Product
model, but the
manufacturer
relationship triggers more database activity:
>>> p.manufacturer
Before the result is printed to the console, another query executes implicitly:
2023-01-03 18:51:30,151 INFO sqlalchemy.engine.Engine SELECT manufacturers.id AS
manufacturers_id,
manufacturers.name AS manufacturers_name
FROM manufacturers
WHERE manufacturers.id = %(pk_1)s
2023-01-03 18:51:30,151 INFO sqlalchemy.engine.Engine [generated in 0.00020s] {'pk_1': 63}
As you see from these examples, SQLAlchemy ORM remembers the session that is in use and sends its own queries to it the first time access to a relationship attribute is made.
When SQLAlchemy works in this way, it is said to use "lazy" loading of relationships. Thanks to this, the application can forget that these attributes are relationships and use them as if they were regular attributes of the model.
While loading relationships lazily sounds great in principle, it has a downside. The fact that database queries are issued implicitly can make the application lose track of how many queries it is sending to the database, and possibly become inefficient if too many implicit queries bog down the database server.
An example of how lazy loading can cause trouble might be useful. Remember the query that returns each product along with its manufacturer? Here it is one more time:
>>> q = select(Product.name, Manufacturer.name).join(Product.manufacturer)
This query is very efficient, since a single database operation returns all the product and manufacturer pairs. A developer that is not aware of the effects of lazy loading might decide to use a different approach to retrieve this same data, taking advantage of the
manufacturer
relationship attribute in a for-loop:
>>> q = select(Product)
>>> for p in session.scalars(q):
        print(p.name, p.manufacturer.name)
At first sight, this looks like a simple and safe way to get the same list of pairs, right? Can you guess how many database queries it takes to produce the list in this way?
Run the above for-loop in the Python session that has the
echo
option enabled, and you will see lots of database queries scroll by. The exact number of queries this loop requires is one for the initial query stored in the
q
variable, plus one additional lazy loading query per manufacturer.
There are 76 manufacturers, so the total count is 77 queries, to get the same information that was obtained above with just one!
Relationship Loaders
The good news is that SQLAlchemy offers some options to configure these relationships and make them more useful and efficient based on how they will be used.
SQLAlchemy uses a relationship
loader
to bring one or more related objects into the session. The default loader, which you have seen in action above, is called the
select
loader.
Another available loader is called
joined
. This loader reads the related objects from the database at the same time the parent is retrieved, by extending the main query with a join clause.
The
select
loader is a "lazy" loader, because the database query for the related objects is delayed until the relationship attribute is accessed for the first time. The
joined
loader is an "eager" loader, because the relationship data is requested at the same time the parent object is, no matter if the application wants it or not.
Using the
joined
loader, the for-loop example above would not issue any additional queries beyond the initial one. To enable this loader, the
options()
method can be added to the query as follows:
>>> from sqlalchemy.orm import joinedload
>>> q = select(Product).options(joinedload(Product.manufacturer))
This is telling SQLAlchemy to override the default lazy loading and bring the
manufacturer
relationship into the session using the
joined
loader. Feel free to try the for-loop above with this as the initial query to see the difference.
Instead of choosing the loader explicitly in each query, it is also possible to change the default loader that is used by the relationship. This is done by passing the desired loader in the
lazy
argument. Here is how the
manufacturer
relationship could be made to use the
joined
loader by default:
class Product(Model):
    # ...
    manufacturer: Mapped['Manufacturer'] = relationship(
        lazy='joined', back_populates='products')
    # ...
You may be wondering why relationships use
select
as the default loader instead of
joined
, which is, at least in some cases, more efficient. The fact is that it is really difficult to know which loader is best, as this largely depends on the use the application gives to each relationship. The
joined
loader is useful when you know for sure that you'll need to access the related objects, but it may not be the best choice when these objects may or may not be needed, as many objects would be loaded unnecessarily into the session. It is also unlikely to perform well for complex queries or relationships with many items, because the cost of adding a join in those cases can be significant.
To make choosing the best loader even harder, the
select
and
joined
loaders are not the only available options to choose from. Below is the complete list of loaders that can be used:
select
: issues a
select()
statement lazily, when the relationship attribute is accessed for the first time. This is the default behavior. As a query option, this loader can be enabled with the
lazyload()
function.
immediate
: loads the related entities at the same time the parent is loaded with a separate
select()
statement. The only difference between
select
and
immediate
is that the latter issues all the relationship queries up front instead of on demand. As an option, this loader is enabled with the
immediateload()
function.
joined
: loads the related entities at the same time the parent is loaded by extending the parent's query with a join to the related table. Use the
joinedload()
function to enable it explicitly as an option in a query.
subquery
: loads the related entities immediately after the parent, in a single additional query that joins a copy of the original query (transformed into a subquery) with the related table. The option version of this loader is the
subqueryload()
function.
selectin
: loads the related entities immediately after the parent, in a single additional query that specifies the list of primary keys to load with the
IN
operator. As an option, this loader is enabled with the
selectinload()
option.
write_only
: disables the loading of the relationship. This loader is only available in SQLAlchemy 2.0 and later and can only be used in the relationship, so it does not have an option version. This is an important loader that you will learn more about later in this book.
noload
: a somewhat similar option to
write_only
, but less flexible. Recommended in place of
write_only
when using SQLAlchemy 1.4. The option version of this loader is enabled with the
noload()
function.
raise
and
raise_on_sql
: two slightly different modes in which an exception is raised if a relationship needs to be loaded implicitly. These modes can be used to detect application code that triggers implicit I/O operations when these are not desired. The
raiseload()
function is the query option version.
dynamic
: a legacy loader that is incompatible with the new SQLAlchemy query APIs, so it should not be used except with legacy code.
It is expected for many of these options to seem obscure or to not make sense at all at this time. Over time, and as you start working with some of these, their purpose will become more clear. A good way to reduce the complexity of having so many options is to group these loaders according to when they load the relationship. Study the following table:
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
Using this table, the list of choices is reduced to three functional groups, with the loaders within each group only having implementation differences, but operating similarly.
What are the best default loaders for the two relationships in
models.py
? With such a small application it is hard to make a decision. A good reason to change the default lazy loading mechanism is to improve performance when the database server is hit by many small relationship queries. At this early time in the life of this project this isn't a concern, so a sensible decision is to keep using the
select
lazy loader for now and postpone any potential changes until later, when these relationships are used more.
Deletion of Related Objects with a Cascade
You've briefly seen how to delete entities from the database in the previous chapter. In general, deleting from the "many" side of a one-to-many relationship works in the same way and does not present a problem. To try this, grab a product and its manufacturer:
>>> p = session.get(Product, 24)
>>> p
Product(24, "Atari 400")
>>> m = p.manufacturer
>>> m
Manufacturer(8, "Atari, Inc.")
You can now delete the product:
>>> session.delete(p)
>>> session.commit()
And this works well. Deleting the manufacturer, however, is more difficult. Try to do it to see what happens:
>>> session.delete(m)
>>> session.commit()
[ traceback omitted ]
sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) NOT NULL constraint failed: products.manufacturer_id
[SQL: UPDATE products SET manufacturer_id=? WHERE products.id = ?]
[parameters: ((None, 25), (None, 26), (None, 27), (None, 28), (None, 29), (None, 30))]
(Background on this error at: https://sqlalche.me/e/14/gkpj)
If the manufacturer only had the one product deleted above, then the deletion would have worked. But this manufacturer has a few more products, all of which still exist and have their
manufacturer_id
foreign key pointing back at this entry. If the manufacturer is removed then the foreign keys on these products would become invalid. SQLAlchemy recognizes this and attempts to set the foreign keys that are invalidated to
NULL
before deleting the manufacturer. However, the
manufacturer_id
column is not defined as optional, so the attempt to set it to
NULL
fails and produces the above error message.
Note:
When an operation such as a commit fails, the session transitions into an error state and cannot be used anymore until it is rolled back. This does not cause any major problems when using a context manager because sessions are always rolled back on errors and closed on exit, but when managing the session life cycle manually in the Python prompt it is necessary to do the roll back explicitly. Here is how this is done:
>>> session.rollback()
Automatic operations such as the attempt to clear foreign keys of an item that is about to be deleted are called
cascades
, and are not limited to deletions. There are a few other situations in which SQLAlchemy also applies a change to child objects in a relationship as a result of an action performed on the parent object. Recall how in the product importer script, after a
Product
instance was created, it was not explicitly added to the session, because its parent (the
Manufactuer
instance) was already added and the parent's inclusion in the session "cascades" into its children.
The desired cascade behaviors are defined in each relationship object, and in many cases the default is the best configuration. To change cascade options, a string with comma-separated options is given in the
cascade
argument to the
relationship()
call.
Note:
Unfortunately cascades are an area of SQLAlchemy that is particularly complex so only the two most common cascade configurations will be described here. If you are interested in the details of each individual cascade option, consult the
Cascades
section of the SQLAlchemy documentation.
The two most used cascade configurations are the following:
'save-update, merge'
: a conservative cascading behavior that is the default, recommended for most relationships. Since this is the default, there is no need to set these options explicitly. With this configuration, child objects are automatically included in the session if the parent has been added to it. The behavior that sets foreign keys that are invalidated by deletions to
NULL
is actually defined by the absence of the
delete
option in this list.
'all, delete-orphan'
: an alternative, more aggressive cascading configuration that makes most operations done on the parent apply to its children, and in particular will delete children along with their parent. The
all
option causes some confusion because in spite of its name it covers all the cascades except
delete-orphan
, which causes children to also be deleted when they are removed from their relationship and become orphaned, even if their parent remains in the database.
The alternative cascade settings are better suited to the relationship between products and manufacturers. With this change, when a manufacturer is deleted, any products associated with it would be deleted as well. Here is how to reconfigure the relationship to implement this behavior:
models.py
: Change cascade options for products to manufacturer relationship
class Manufacturer(Model):
    # ...
    products: Mapped[list['Product']] = relationship(
        cascade='all, delete-orphan', back_populates='manufacturer')
    # ...
Save this change, and then start a new Python session to try to delete the manufacturer again (if you don't want to continue seeing SQL logs in your sessions, feel free to remove the
echo=True
option in
db.py
).
>>> from db import Session
>>> from models import Product, Manufacturer
>>> session = Session()
>>> m = session.get(Manufacturer, 8)
>>> m
Manufacturer(8, "Atari, Inc.")
>>> session.delete(m)
>>> session.commit()
If you query the list of products again, you will find that all the products that were attached to the deleted Atari, Inc. company have now been deleted along with it.
Detaching Related Objects
Sometimes it is necessary to delete the relationship between two objects, without deleting the objects themselves. This can be thought of a "detach" operation that breaks the link between two objects.
For a one-to-many relationship there are two ways to detach two related objects, depending on the side from which this is done. When doing it from the "one" side, the relationship object presents all the related objects in the "many" side in a format similar to a list. In this case, the
remove()
method on the relationship object can be used to remove an element, following familiar list semantics.
The next example gets a product and its manufacturer, then unlinks them:
>>> p = session.get(Product, 1)
>>> p
Product(1, "Acorn Atom")
>>> m = p.manufacturer
>>> m
Manufacturer(1, "Acorn Computers Ltd")
>>> m.products.remove(p)
>>> session.commit()
After the session is committed, this product is not linked anymore to the manufacturer. But there is an unintended consequence. If you now try to get the product again, it isn't there anymore:
>>> p = session.get(Product, 1)
>>> print(p)
None
Recall that the cascade options used by the
products
relationship object were changed to ensure that products are deleted along with their manufacturer. The
delete-orphan
cascade option that was included in this relationship covers the case of a product becoming an orphan, and it states that the orphaned object should be deleted too.
What would happen if
delete-orphan
wasn't used? Then SQLAlchemy would set the
manufacturer_id
foreign key in the product to
None
to break the link to the parent, but this column cannot accept null values, so the result will be that the commit operation would fail, and the relationship link would not be removed.
For a one-to-many relationship in which it is acceptable to have objects from the "many" side in an orphaned state the foreign key column must be configured as nullable by adding the
Optional
type hint, as this will prevent the error.
Detaching a one-to-many relationship also works from the "many" side:
>>> p = session.get(Product, 2)
>>> p
Product(2, "BBC Micro")
>>> p.manufacturer = None
>>> session.commit()
When starting from the product side, the relationship is broken by setting the parent object to
None
. For this particular relationship, however, orphaned products are not allowed because the
Optional
type hint hasn't been used in the relationship object or the foreign key column, so this operation generates another error from SQLAlchemy.
Exercises
Now is your chance to practice some one-to-many relationship queries. Before starting, run the
import_products.py
script to restore any products or manufacturers you may have deleted. Then open a Python session and write queries that return:
The list of products made by IBM and Texas Instruments.
Manufacturers that operate in Brazil.
Products that have a manufacturer that has the word "Research" in their name.
Manufacturers that made products based on the Z80 CPU or any of its clones.
Manufacturers that made products that are not based on the 6502 CPU or any of its clones.
Manufacturers and the year they went to market with their first product, sorted by the year.
Manufacturers that have 3 to 5 products in the catalog.
Manufacturers that operated for more than 5 years.
Proceed to
Chapter 4
.
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
