---
title: "SQLAlchemy 2 In Practice - Chapter 4 - Many-To-Many Relationships"
url: "https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-4---many-to-many-relationships"
fetched_at: 2026-04-30T07:01:20.075648+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# SQLAlchemy 2 In Practice - Chapter 4 - Many-To-Many Relationships

Source: https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-4---many-to-many-relationships

This is the fourth chapter of my
SQLAlchemy 2 in Practice
book. If you'd like to support my work, I encourage you to buy this book, either directly from
my store
or on
Amazon
. Thank you!
Continuing with the topic of relationships, this chapter is dedicated to the
many-to-many
type, which as its name implies, is used when it is not possible to identify any of the sides as a "one" side.
For your reference, here is a summary of the book contents:
In this chapter you are going to learn how to implement a many-to-many relationship between the
products
table and a new
countries
table.
What Is a Many-To-Many Relationship?
The best way to understand the purpose of many-to-many relationships is with an actual example. Start a Python shell and obtain a list of countries, removing duplicates with the
distinct()
clause. Here is how to do it:
>>> from db import Session
>>> from models import Product
>>> from sqlalchemy import select
>>> session = Session()
>>> q = select(Product.country).order_by(Product.country).distinct()
>>> session.scalars(q).all()
['Australia', 'Belgium', 'Brazil', 'Bulgaria', 'China', 'Croatia', 'Czechoslovakia',
'East Germany', 'France', 'Germany', 'Hong Kong', 'Hungary', 'Japan', 'Netherlands',
'New Zealand', 'Norway', 'Portugal', 'Portugal/Poland', 'Romania', 'Serbia', 'Sweden',
'Taiwan', 'UK', 'USA', 'USA/UK/Portugal', 'USSR']
Looking through the list of countries, you can probably recognize two problematic entries. It appears that some products were made jointly by the USA, UK and Portugal, and others were made by Portugal and Poland. From these two occurrences it now seems that the format of the
country
column in the CSV data file should be interpreted as a list of countries separated by slashes and not as a single country.
This presents a new challenge, because there are products that need to be associated with a list of countries, and most countries will very likely have a list of associated products.
In a standard one-to-many relationship, the "many" side adds a foreign key that points to the "one" side, and this is sufficient to establish the relationship. When trying to create a relationship between products and countries, a foreign key to a new
countries
table in the
products
table does not work, because that would only allow a single country to be linked to each product. A foreign key to the product in the
countries
table also fails to work, as that would limit each country to be associated with a single product.
It seems in a many-to-many relationship there is no place to insert a foreign key, right?
How Many-To-Many Relationships Work
The trick to be able to implement a many-to-many relationship requires some out-of-the-box thinking. Instead of a single one-to-many relationship, two one-to-many relationships are needed to fully represent these complex relationships.
Since it is impossible to build a direct many-to-many relationship between the two tables, a third table, called the
join table
is added. Then each side establishes a one-to-many relationship to the join table, which means that foreign keys referencing the two tables are added to it. Below is a diagram of the database structure with the many-to-many relationship between products and countries added.
Here the
products_countries
table is the join table, which records the foreign keys of each pair of associated product and country. A common naming convention for join tables is to use the names of the two entities that are part of the relationship.
As an example, for a product that was created jointly by three countries, there's going to be three entries in the join table that have the
product_id
foreign key set to the product, each having
country_id
set to one of the countries. And coming from the other side, for a country in which seven products have been created there's going to be that number of entries with
country_id
set to the country, each linking it to one of the products.
A Simple Many-To-Many Relationship Implementation
Managing all the foreign keys in the join table of a many-to-many relationship might seem like a nightmare, but here once again SQLAlchemy does most of the hard work.
The first step in implementing this relationship is creating the join table. This table is going to be managed by SQLAlchemy, so all the behavior provided by the Declarative Base class from SQLAlchemy is unnecessary. Instead, this table can be created using the
Table
class from SQLAlchemy Core. To make it easy to reference this table in the
Product
and the yet to be created
Country
models the join table should be added above the model classes in
models.py
.
models.py
: Products and countries join table
from sqlalchemy import Table, Column

ProductCountry = Table(
    'products_countries',
    Model.metadata,
    Column('product_id', ForeignKey('products.id'), primary_key=True,
           nullable=False),
    Column('country_id', ForeignKey('countries.id'), primary_key=True,
           nullable=False),
)
The
Table
constructor takes the table name as first argument, followed by the database metadata instance. The remaining arguments are two
Column
instances for the foreign keys. Because tables use the
Column()
constructor instead of typing hints, the
nullable=False
option is added to make values for these columns required.
Unlike all the other tables derived from models, this table does not have an
id
primary key, and instead declares the two foreign keys as primary keys. When multiple columns are designated as primary keys, SQLAlchemy creates a
composite
primary key. By definition, primary keys are required to be unique, so for this relationship the join table will not allow two rows that have identical foreign key values.
The updated
Product
model and the new
Country
model are shown below:
models.py
: Many-to-many relationship between products and countries
class Product(Model):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    manufacturer_id: Mapped[int] = mapped_column(
        ForeignKey('manufacturers.id'), index=True)
    year: Mapped[int] = mapped_column(index=True)
    cpu: Mapped[Optional[str]] = mapped_column(String(32))

    manufacturer: Mapped['Manufacturer'] = relationship(
        back_populates='products')
    countries: Mapped[list['Country']] = relationship(
        secondary=ProductCountry, back_populates='products')

    def __repr__(self):
        return f'Product({self.id}, "{self.name}")'


class Country(Model):
    __tablename__ = 'countries'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32), index=True, unique=True)

    products: Mapped[list['Product']] = relationship(
        secondary=ProductCountry, back_populates='countries')

    def __repr__(self):
        return f'Country({self.id}, "{self.name}")'
There are two changes in the
Product
model. The
country
column has been removed, since now countries will be stored in a separate table.
Also, similar to the
manufacturer
attribute representing the one-to-many relationship, a
countries
relationship attribute is added to have access to the entities in the other side of the many-to-many relationship, with similar semantics to a list.
The
secondary
argument to
relationship()
tells SQLAlchemy that this relationship is supported by a secondary table (the join table). Note that the join table is referenced directly by its name, so it has to be defined above the model classes. The
secondary
option configures the relationship to work as a many-to-many, with SQLAlchemy automatically adding and removing items from the join table as needed.
The new
Country
model is very similar to the
Manufacturer
model, with just a primary key and a
name
attribute. The
products
relationship on this model represents the reverse view of the many-to-many relationship, and is also initialized with the join table in the
secondary
argument.
As before, the
back_populates
options in the two relationships reference each other, so that SQLAlchemy knows that they are two sides of the same relationship.
Product Importer Script Updates
It's time to make another update to the product importer script, so that countries are properly stored as standalone entities linked to products. The updated script is shown below.
import_products.py
: Import products, manufacturers and countries from CSV file
import csv
from db import Model, Session, engine
from models import Product, Manufacturer, Country


def main():
    Model.metadata.drop_all(engine)  # warning: this deletes all data!
    Model.metadata.create_all(engine)

    with Session() as session:
        with session.begin():
            with open('products.csv') as f:
                reader = csv.DictReader(f)
                all_manufacturers = {}
                all_countries = {}

                for row in reader:
                    row['year'] = int(row['year'])

                    manufacturer = row.pop('manufacturer')
                    countries = row.pop('country').split('/')
                    p = Product(**row)

                    if manufacturer not in all_manufacturers:
                        m = Manufacturer(name=manufacturer)
                        session.add(m)
                        all_manufacturers[manufacturer] = m
                    all_manufacturers[manufacturer].products.append(p)

                    for country in countries:
                        if country not in all_countries:
                            c = Country(name=country)
                            session.add(c)
                            all_countries[country] = c
                        all_countries[country].products.append(p)


if __name__ == '__main__':
    main()
The
main()
function still performs a
drop_all()
followed by a
create_all()
as a quick way to reset the database, but keep in mind that recreating the entire database from scratch to make changes gets less viable the more tables there are in the database. Soon you will learn about how to improve this using database migration scripts.
Following a similar pattern to the importing of the manufacturers, now there is also an
all_countries
dictionary that will maintain the
Country
instances that are added.
In this version, both the
manufacturer
and
country
attributes of the
row
dictionary that is imported for each line of the CSV file are removed. The remaining items in
row
are used to initialize the
Product
instance.
The way the
countries
attribute is extracted is unusual. Instead of store the string value of this field, the string is converted into a list of country names using
split('/')
. Recall that the CSV file uses
/
as a separator when a product belongs to multiple countries.
After the
Product
instance and manufacturer are created, a loop runs over the list of countries the product belongs to, and the product is added to each country with a familiar
append()
method on the
products
relationship of the
Country
model. It should be noted that given that this is a many-to-many relationship, there are two equivalent ways to link a product with a country. In the script above, the product is appended to the country:
all_countries[country].products.append(p)
If preferred, the two entities can be linked from the other side, by appending the country to the product:
p.countries.append(all_countries[country])
Either way, this will tell SQLAlchemy to add an entry to the join table with the foreign keys of the two entities.
Many-To-Many Relationship Queries
As you surely can guess, the
products
and
countries
relationship objects added to the
Country
and
Product
models respectively also simplify the use of the many-to-many relationship in queries.
To try some queries, begin by starting a Python session and importing the needed components:
>>> from db import Session
>>> from models import Product, Manufacturer, Country
>>> from sqlalchemy import select, func
>>> session = Session()
Here is how to get a product and its countries:
>>> p = session.scalar(
        select(Product)
            .where(Product.name == 'Timex Sinclair 1000'))
>>> p
Product(138, "Timex Sinclair 1000")
>>> p.countries
[Country(1, "UK"), Country(3, "USA"), Country(22, "Portugal")]
Here the
countries
relationship uses the default lazy loader, so it implicitly runs a query to get the list of countries when the attribute is accessed for the first time.
Similarly, a country can report its products:
>>> c = session.scalar(
        select(Country)
            .where(Country.name == 'Portugal'))
>>> c
Country(22, "Portugal")
>>> c.products
[Product(138, "Timex Sinclair 1000"), Product(139, "Timex Sinclair 1500"),
Product(140, "Timex Sinclair 2048"), Product(141, "Timex Computer 2048"),
Product(142, "Timex Computer 2068"), Product(143, "Komputer 2086")]
Moving on to something more complex, here is a query that returns all the products that have multiple countries, along with how many countries each has:
>>> country_count = func.count(Country.id).label(None)
>>> q = (select(Product, country_count)
            .join(Product.countries)
            .group_by(Product)
            .having(country_count >= 2)
            .order_by(Product.name))
>>> session.execute(q).all()
[(Product(143, "Komputer 2086"), 2), (Product(142, "Timex Computer 2068"), 3),
(Product(138, "Timex Sinclair 1000"), 3), (Product(139, "Timex Sinclair 1500"), 3),
(Product(140, "Timex Sinclair 2048"), 3)]
This query uses similar techniques as those you've learned when working with the
manufacturer
one-to-many relationship. The query returns two values per result row, the product and the count of countries. The latter is created with a label and stored in the
country_count
variable, so that it can be used in the
select()
and
having()
clauses without repetition.
To count the countries it is necessary to join products with countries. Grouping these results by product collapses the results back to a product per row, but now the second result runs the
count()
aggregation function and replaces the list of countries with how many there are. The
having()
clause filters the grouped results and leaves only those that have two or more countries.
The
join()
method in this query is interesting, because a many-to-many relationship cannot be queried with a single join. In fact, it is not possible in SQL to join the
products
and
countries
tables directly, since there are no common attributes in them that can be used.
In reality, a many-to-many relationship requires a two-step join. First the
products
table is joined with the
products_countries
join table, and then
products_countries
is joined with
countries
. SQLAlchemy does some invisible work here to make this join work.
If you are curious about the internals, below you can see the SQL generated by this query, including the two joins required by the many-to-many relationship:
>>> print(q)
SELECT products.id, products.name, products.manufacturer_id, products.year, products.cpu,
count(*) AS count_1
FROM products
JOIN products_countries AS products_countries_1 ON products.id =
products_countries_1.product_id
JOIN countries ON countries.id = products_countries_1.country_id
GROUP BY products.id, products.name, products.manufacturer_id, products.year, products.cpu
HAVING count(*) >= :param_1 ORDER BY products.name
The one-to-many and many-to-many relationships can be used together, and this opens the door to even more interesting queries. The next query obtains the list of manufacturers that operate in the UK:
>>> q = (select(Manufacturer)
            .join(Manufacturer.products)
            .join(Product.countries)
            .where(Country.name == 'UK')
            .order_by(Manufacturer.name)
            .distinct())
>>> session.scalars(q).all()
[Manufacturer(1, "Acorn Computers Ltd"), Manufacturer(2, "Amstrad"), ...,
Manufacturer(70, "Timex Sinclair")]
The goal of this query is to return a list of manufacturers, so that is the only model that is added to the
select()
statement. But the query needs access to countries, and countries have no direct connection with manufacturers. The only solution is to navigate the available relationships until a connection is achieved. In this case, first manufacturers are joined with their products, and then products are joined with their countries. The result of this chain of joins is that the query now has access to all the valid (manufacturer, product, country) triplets, and can add filters on any of these, for example to only keep the triplets with UK as the country.
The
distinct()
clause is necessary in this case because many of those triplets that have the country set to UK are going to have the same manufacturer, and unless told otherwise, the database will return all of them as rows, leading to duplicate results.
Grouping also works across a chain of relationships. The next query gets a list of manufacturers that operate in more than one country, along with the country count:
>>> country_count = func.count(Country.id.distinct()).label(None)
>>> q = (select(Manufacturer, country_count)
            .join(Manufacturer.products)
            .join(Product.countries)
            .group_by(Manufacturer)
            .having(country_count >= 2))
>>> session.execute(q).all()
[(Manufacturer(70, "Timex Sinclair"), 4)]
The
country_count
aggregation in this case needs to be expanded with a
distinct()
clause, because a simple count of rows would include duplicate entries that result from the joins.
If you fail to see why joins generate duplicates, an example should help clarify it. Let's assume that company Acme has two products A and B, both made in the USA. The chained join used in the query above would generate the following triplets for this company:
Manufacturer
Product
Country
Acme
A
USA
Acme
B
USA
The
group_by(Manufacturer)
clause in the query would cause these two rows to be collapsed into one, since both have Acme as the manufacturer. A plain
func.count()
function given as the second value in the query would count the number of rows that were merged, which in this example is 2, even though there is a single country at play. The
distinct()
clause asks the database to remove duplicates from the count.
Deleting From Many-To-Many Relationships
Many-to-many relationships that are configured with the
secondary
option have the advantage that SQLAlchemy does all the maintenance work on the join table, and this extends to deletions. When an entity is deleted, SQLAlchemy finds all the entities on the other side of the relationship that linked to it and removes those links.
The following example deletes a country, which makes that country automatically disappear from products that had it listed:
>>> c = session.get(Country, 22)
>>> c
Country(22, "Portugal")
>>> p = session.get(Product, 138)
>>> p
Product(138, "Timex Sinclair 1000")
>>> p.countries
[Country(1, "UK"), Country(3, "USA"), Country(22, "Portugal")]
>>> session.delete(c)
>>> session.commit()
>>> p.countries
[Country(1, "UK"), Country(3, "USA")]
It is also possible to detach entities that are connected through a many-to-many relationship, without deleting any of the entities themselves. The detachment can be issued from either side of the relationship using list semantics:
>>> c = session.get(Country, 1)
>>> c
Country(1, "UK")
>>> p = session.get(Product, 138)
>>> p
Product(138, "Timex Sinclair 1000")
>>> p.countries
[Country(1, "UK"), Country(3, "USA")]
>>> c in p.countries
True
>>> p.countries.remove(c)
>>> session.commit()
>>> p.countries
[Country(3, "USA")]
>>> c in p.countries
False
The above example removes a country from a product. The same result can be obtained by removing the product from the country:
>>> c.products.remove(p)
The one-to-many relationship between manufacturers and their products was configured with a non-nullable foreign key to force all products to have a manufacturer linked, effectively making it impossible for a product to exist without having a manufacturer. With a many-to-many relationship there is no automatic way to enforce that every entity has at least one link to an entity on the other side. The example below removes the only country associated with a product, leaving the product without any related countries:
>>> c = session.get(Country, 1)
>>> c
Country(1, "UK")
>>> p = session.get(Product, 1)
>>> p
Product(1, "Acorn Atom")
>>> p.countries
[Country(1, "UK")]
>>> c.products.remove(p)
>>> session.commit()
>>> p.countries
[]
For a many-to-many relationship for which it is desired that there always is at least one linked entity the application must manually perform validation checks and prevent the last link from being removed.
Database Migrations
The chapters that follow are going to introduce more tables and relationships. Before increasing the complexity of the database it would be a good idea to set up a robust mechanism to make updates, since the
drop_all()
and
create_all()
functions used until this point are very limited in that they require all the data to be re-imported.
Introduction to Alembic
In this section you are going to learn how to use
Alembic
, the database migration tool that is part of the SQLAlchemy family. Install this package in your virtual environment with
pip
:
(venv) $ pip install alembic
The first step to enable database migrations in your project is to create a migration repository with the
alembic init
command:
(venv) $ alembic init migrations
The
migrations
argument is the name of a subdirectory that is created under the project directory, where database migration scripts will be stored. In addition to this subdirectory, an
alembic.ini
file is created in the project directory. For a project that is under source control, the
alembic.ini
file and the entire contents of the
migrations
subdirectory should be treated as source code and maintained along with the application's source files.
The files that are created by the
alembic init
command do not have any initial awareness of what database the project is using. To point Alembic at the project's database, a few simple configuration changes need to be made. There isn't a single way to do this, but for the RetroFun project the most convenient option is to edit the
env.py
file located inside
migrations
.
Open
migrations/env.py
in your code editor. At the top of the file, import
engine
and
Model
from
db.py
and the models:
migrations/env.py
: Import Model and engine
from db import Model, engine
import models
Then locate the line that reads:
target_metadata = None
Replace this line with the following code:
migrations/env.py
: Configure the project's database into Alembic
target_metadata = Model.metadata
config.set_main_option("sqlalchemy.url", engine.url.render_as_string(
    hide_password=False))
The
target_metadata
variable is where Alembic expects the metadata instance used by the application. For SQLAlchemy ORM, this instance exists as a
metadata
attribute of the
Model
declarative base class.
The second line inserts a value for the
sqlalchemy.url
option in the Alembic configuration object. This option is where Alembic goes to obtain the URL of the database. Since the application creates an
engine
instance with this URL, the most convenient (though maybe not the most efficient) is to get the URL from this object.
If you open the
alembic.ini
file, you will see that this same
sqlalchemy.url
option is initialized with a placeholder URL. If you prefer, you can enter the URL in this file instead of editing with
config.set_main_option()
in
env.py
. Both set the same configuration variable, but doing it in
env.py
as shown above has the benefit that the database URL does not need to be written in two different places.
There is one more change to make, which is important when using the SQLite database. Scroll down on
env.py
until you find the
run_migrations_online()
function, close to the end of the file. This function makes a
context.configure()
function call that looks like this:
context.configure(
            connection=connection, target_metadata=target_metadata
        )
This call can be used to configure Alembic, and in particular its migration generator. The change shown below enables the
render_as_batch
option.
migrations/env.py
: Configure the migration generator
context.configure(
            connection=connection, target_metadata=target_metadata,
            render_as_batch=True,
        )
The
render_as_batch
option is needed to address migration limitations of the SQLite database. When this option is enabled, if an unsupported migration operation is requested on a SQLite database, Alembic will transparently create a new table with the change, move all the data over and finally delete the outdated table. For other databases this option does not have any effect, so it does not hurt to enable it too, but if you prefer, it is also okay to omit it.
You may have noticed that the
import models
statement added near the top of
env.py
appears to be unnecessary, since none of the model classes are referenced directly. If you are using a code checker, it will likely flag this import as unnecessary. Regardless of your code checking tool tells you, this import statement needs to be in the file. SQLAlchemy only learns about the models in your application when they are imported. If the models are not imported, then these models will not exist in the memory of the Python process, and SQLAlchemy and Alembic will not know about them.
Create a Migration Script
Alembic uses the concept of
migration scripts
to track changes that are made to the database. A migration script contains Python code that makes changes to the live database, without removing any tables or data.
Ready to generate your first database migration? Alembic can auto-generate a migration script by comparing the model classes against their corresponding database tables. For example, if the table referenced by a model class does not exist in the database, Alembic decides that this is a new table that needs to be created in the database, matching the definitions in the model class. If a table that exists in the database is not referenced by any model class in the application, then it decides that the table has to be deleted, and generates the code to do so in the migration script. The goal for the generated migration script is always to make any necessary changes in the database so that it reflects the state of the models.
To generate an initial migration, it is necessary that the database is completely empty, since this is what will make Alembic generate a migration that creates the
products
,
manufacturers
,
countries
and
products_countries
tables. Open a Python shell, and call the
drop_all()
function one last time:
>>> from db import Model, engine
>>> import models
>>> Model.metadata.drop_all(engine)
The
import models
line in the above code is there for the same reason it was included in the
env.py
script, which is to let SQLAlchemy know what the models are.
After running the above statements, the database is going to be completely empty. Now you can generate the first database migration script with the following command:
(venv) $ alembic revision --autogenerate -m "products, manufacturers, countries"
Alembic is going to print some logs to the terminal indicating that it has detected new tables and new indexes. Then at the bottom, it will show the name of the generated migration script, which will have the format
{code}_products_manufacturers_countries.py
, where
{code}
is a unique code that identifies the migration. The rest of the name is created from the description given in the
-m
option.
The generated migration script is a Python module that has two functions
upgrade()
and
downgrade()
. The
upgrade()
function applies changes to make the database match the models, while the
downgrade()
function reverts these changes. Each migration script will have these two functions, making it possible for Alembic to make a chain of upgrades, or a chain of downgrades by calling the corresponding functions in the correct order.
Note:
The method Alembic uses to auto-generate migration scripts is extremely convenient, but is not foolproof, so it is always best to review auto-generated scripts to make sure they are correct.
Database Upgrade
The
alembic revision
command creates a migration script, but it does not execute the script. The RetroFun database is, at this point, still empty. The next command runs the migration script:
(venv) $ alembic upgrade head
With this command, the changes in the
upgrade()
function are executed against the configured database, and now all the tables and indexes are created similarly to the
create_all()
function, but with a more robust solution that will also be able to apply partial changes going forward.
The
alembic
command has many sub-commands including
downgrade
to undo a database migration,
current
to show which migration the database is at,
history
to see the list of migrations, and more. Feel free to review the
Alembic documentation
to learn more about them.
A Migration-Aware Product Importer
The database migration does not have any knowledge of the data that the application wants to store in the tables, so it created all the tables without any data in them. The
import_products.py
script can now be used to insert the products, manufacturers and countries, but the
drop_all()
and
create_all()
function calls at the start of the
main()
function need to be removed, since these conflict with Alembic, which is now in charge of creating and maintaining the database structure.
Instead of dropping and recreating the tables, the importer script will now attempt to delete all the rows in all the tables, so that it can import them again from the CSV file. Here is the updated script:
import_products.py
: Import data without recreating tables
import csv
from sqlalchemy import delete
from db import Session
from models import Product, Manufacturer, Country, ProductCountry


def main():
    with Session() as session:
        with session.begin():
            session.execute(delete(ProductCountry))
            session.execute(delete(Product))
            session.execute(delete(Manufacturer))
            session.execute(delete(Country))

    with Session() as session:
        with session.begin():
            with open('products.csv') as f:
                reader = csv.DictReader(f)
                all_manufacturers = {}
                all_countries = {}

                for row in reader:
                    row['year'] = int(row['year'])

                    manufacturer = row.pop('manufacturer')
                    countries = row.pop('country').split('/')
                    p = Product(**row)

                    if manufacturer not in all_manufacturers:
                        m = Manufacturer(name=manufacturer)
                        session.add(m)
                        all_manufacturers[manufacturer] = m
                    all_manufacturers[manufacturer].products.append(p)

                    for country in countries:
                        if country not in all_countries:
                            c = Country(name=country)
                            session.add(c)
                            all_countries[country] = c
                        all_countries[country].products.append(p)


if __name__ == '__main__':
    main()
The first session block in the
main()
function makes use of the
delete()
function from SQLAlchemy to delete all the entities in the
products
,
manufacturers
and
countries
tables plus the
products_countries
join table. The rest of the script did not change from the previous version.
You can now run the importer script to load the CSV data one last time:
(venv) $ python import_products.py
Exercises
Ready to create some queries on your own? Write queries that generate:
Products that were made in UK or USA.
Products not made in UK or USA. Products that were made in UK and/or USA jointly with other countries should be included in the query results.
Countries with products based on the Z80 CPU or any of its clones.
Countries that had products made in the 1970s in alphabetical order.
The 5 countries with the most products. If there is a tie, the query should pick the countries in alphabetical order.
Manufacturers that have more than 3 products in UK or USA.
Manufacturers that have products in more than one country.
Products made jointly in UK and USA.
Proceed to
Chapter 5
.
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
