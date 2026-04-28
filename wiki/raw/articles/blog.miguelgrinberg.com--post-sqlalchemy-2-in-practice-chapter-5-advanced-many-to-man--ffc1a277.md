---
title: "SQLAlchemy 2 In Practice - Chapter 5 - Advanced Many-To-Many Relationships"
url: "https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-5---advanced-many-to-many-relationships"
fetched_at: 2026-04-28T07:02:06.562355+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# SQLAlchemy 2 In Practice - Chapter 5 - Advanced Many-To-Many Relationships

Source: https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-5---advanced-many-to-many-relationships

This is the fifth chapter of my
SQLAlchemy 2 in Practice
book. If you'd like to support my work, I encourage you to buy this book, either directly from
my store
or on
Amazon
. Thank you!
You have now learned the design blocks used in relational databases. Sometimes, however, these building blocks have to be "tweaked" a bit to achieve a desired goal. This chapter is dedicated to exploring a very useful variation on the many-to-many relationship.
For your reference, here is a summary of the book contents:
Many-To-Many Relationships with Additional Data
In this section you are going to add the RetroFun ordering subsystem to the database, which includes customers and orders. The next diagram shows how the new tables and relationships fit in the existing database.
The new
customers
and
orders
tables have a one-to-many relationship between them, with customers on the "one" side. The
products
and
orders
tables have a many-to-many relationship, with the
orders_items
table as the join table. But the join table in this relationship has additional columns besides the two foreign keys.
This join table in this relationship effectively represents each line item in an order, with references to the order and the product. But this isn't sufficient, the relationship also needs to define a quantity and a unit price for the sale.
Having additional data in the join table complicates things. The many-to-many relationship between products and countries did not have any extra columns, and that allowed SQLAlchemy to take full control to insert or delete entries from this table as needed. When there are additional columns, how would SQLAlchemy know what to write in those extra columns when it needs to insert a new item?
Many-to-many relationships with extra columns in the join table need to use a less automatic workflow with SQLAlchemy, because the application has to provide values for the additional columns that are part of the relationship when two entities are linked.
As a first step to implement orders for RetroFun, the application can be expanded with the
Customer
and
Order
models, and a one-to-many relationship between them. These are added at the bottom of
models.py
.
models.py
: Orders and customers
from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy.orm WriteOnlyMapped

# ...

class Order(Model):
    __tablename__ = 'orders'

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(default=datetime.utcnow,
                                                index=True)
    customer_id: Mapped[UUID] = mapped_column(ForeignKey('customers.id'),
                                              index=True)

    customer: Mapped['Customer'] = relationship(back_populates='orders')

    def __repr__(self):
        return f'Order({self.id.hex})'


class Customer(Model):
    __tablename__ = 'customers'

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    address: Mapped[Optional[str]] = mapped_column(String(128))
    phone: Mapped[Optional[str]] = mapped_column(String(32))

    orders: WriteOnlyMapped['Order'] = relationship(back_populates='customer')

    def __repr__(self):
        return f'Customer({self.id.hex}, "{self.name}")'
There are a few new things in these models. The following sections cover them one by one.
UUID Primary Keys
The most important difference in these two new models is that their
id
columns are defined with the
UUID
type instead of the
int
keys used in all the previous models.
Note:
Support for the
UUID
type was introduced in SQLAlchemy 2.0. The
documentation
includes an implementation of a custom UUID type that can be used with older releases.
The problem with the auto-incrementing integer primary keys used earlier is that when they are included in URLs or emails, they indirectly allow people to estimate the size of the database tables they reference. Most business will probably prefer to keep the number of customers or orders they have private, so using integer keys for these tables is not a good idea.
A way to avoid giving away this type of information is to switch away from numeric primary keys. The new models define
id
as a
UUID
, which is a 16 byte binary sequence. There are several types of UUIDs and one in particular, called
UUID4
, is a good choice for primary keys. In case you are not familiar with UUID4 support in Python, the following Python session shows how to generate them and print them:
>>> from uuid import uuid4
>>> id = uuid4()
>>> id.bytes
b'kF\xf8\xe9o\x94MM\xad\xfe\x15\xe1\xeb\xb1\xd0\xac'
>>> id.hex
'6b46f8e96f944d4dadfe15e1ebb1d0ac'
Unfortunately SQLAlchemy can only manage integer primary keys automatically. To avoid having to remember to create and assign a UUID4 to each new
Order
or
Customer
instance that is added, the
id
columns in these two models are given a
default
argument, which automatically assigns values to them if the application doesn't.
The
default
argument can be set to a constant value or to a callable, such as a function. If it is set to a callable, SQLAlchemy will call it every time it needs to give a default value to a column. The
id
columns above pass the
uuid4
function as default, so that each new item gets its own newly generated UUID4. When passing functions as default column values it is important to remember to not include the
()
after the function name. SQLAlchemy needs the reference to the function itself, so that it can call it when a value needs to be generated.
The
__repr__()
methods in both classes use the
hex
attribute of the
UUID
object to decode the binary UUID4 into a printable hexadecimal string for debugging, as shown in the Python example above.
The one-to-many relationship between customers and orders is established by adding a foreign key on the "many" side, which in this case is the
Order
model. This is the
customer_id
column, which is also given a
UUID
type to match the type of
Customer.id
.
Date and Time Columns
The
Order
model features a
timestamp
column declared with a
datetime
type. In the same way as with the
UUID
type, SQLAlchemy automatically maps Python
datetime
objects to the appropriate type in the database.
The
timestamp
column also has a
default
argument. Passing
datetime.utcnow
as a default will make SQLAlchemy call
datetime.utcnow()
each time a new order is added to the database. This effectively means that the
timestamp
column can be left unassigned when adding an order, and the current date and time will be automatically set during the commit operation. Once again the
()
are not included in the
default
argument so that SQLAlchemy receives a reference to the function, without calling it.
When working with date and time values in a database it is important to maintain a uniform timezone. The most sane approach is to store all timestamps in the UTC timezone, and for that reason the default is set to
utcnow
instead of
now
. The application can convert UTC timestamps retrieved from the database to the timezone of the client when they are presented to the user. For web applications this is often done in the web browser, which has access to the user's timezone.
Write-Only Relationships
The relationship attributes on these models are configured similarly to the relationship between manufacturers and products. The
Order.customer
relationship uses the default lazy evaluation, but the
Customer.orders
relationship has a new definition:
orders: WriteOnlyMapped['Order'] = relationship(back_populates='customer')
The
WriteOnlyMapped
typing hint is used here to define a relationship configured with the
lazy='write_only'
option. When typing isn't used or desired, the
lazy
argument can be given in the
relationship()
call.
Why is this relationship different? In general, lazy evaluation of relationships makes sense only in certain cases. Relationships that load a "one" side, such as
Order.customer
that may only be casually used are perfect to evaluate lazily, and so are those that are expected to have a short number of elements, such as the
Product.countries
relationship from the previous chapter.
The reason why
Customer.orders
is defined as a
write_only
relationship is that a lazily evaluated one isn't very useful for it. This could potentially be a long relationship for repeat customers, and getting the entire collection of orders from a customer as a list is unlikely to be very useful. What would work for this relationship is to have a way to request only some of the customer's orders, such as the most recent one, or the orders made in the last month. But a lazily loaded relationship does not provide a way to define any filters that can configure a range of elements to retrieve.
What makes the
write_only
loader convenient is that it does not attempt to load the relationship, it just generates a query object that you can execute yourself, possibly after adding filters, sorting or any other option you may need. The relationship object also has
add()
,
add_all()
and
remove()
methods that can be used to add or remove elements from the relationship.
How does a
write_only
relationship work in practice? You will see this relationship in action later in this chapter.
Association Object Pattern
The next step is to create the many-to-many relationship between the
Order
and
Product
models, which will define the contents of each order. For a simple many-to-many relationship with extra columns the join table can be created as a
Table
instance and given to SQLAlchemy to manage. Because this relationship needs extra data, the join table is created as a
Model
subclass, to allow the application to manage the additional columns. SQLAlchemy calls this alternative method to define a many-to-many relationship the
Association Object Pattern
.
Below you can see the new join table, which is added at the bottom of
models.py
.
models.py
: Order item model
class OrderItem(Model):
    __tablename__ = 'orders_items'

    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'),
                                            primary_key=True)
    order_id: Mapped[UUID] = mapped_column(ForeignKey('orders.id'),
                                           primary_key=True)
    unit_price: Mapped[float]
    quantity: Mapped[int]
The primary key of the
OrderItem
model is made up of the two foreign key columns, similar to what was done in the simpler many-to-many relationship of the previous chapter. By not having the
Optional
typing hint, both keys are required (non-nullable in database jargon), which means that if a product or an order are deleted, any entries in this table referencing the deleted item must be removed.
The model class has two additional columns to store the unit price and quantity of the ordered product, which are necessary to have all the information associated with the purchase.
Now comes the interesting part. The simpler many-to-many relationship between products and countries used the
secondary
argument to
relationship
on both models, and this was enough for SQLAlchemy to know what to do. Unfortunately,
secondary
cannot be used in this case because the application cannot give up control of the join table because of the extra columns.
The solution that makes this work can be derived from the fact that a many-to-many relationship can be thought of as two one-to-many relationships, or more accurately, as a one-to-many relationship between the first model and the join table, and a many-to-one relationship between the join table and the second model. It turns out that if you think about the two halves of this relationship separately, then there is no need to rely on the
secondary
argument.
Below you can see how the two sides of the many-to-many relationship can be implemented using one-to-many relationship objects.
models.py
: Decomposed many-to-many relationship
class Product(Model):
    # ...
    order_items: WriteOnlyMapped['OrderItem'] = relationship(
        back_populates='product')
    # ...

class Order(Model):
    # ...
    order_items: Mapped[list['OrderItem']] = relationship(
        back_populates='order')
    # ...

class OrderItem(Model):
    # ...
    product: Mapped['Product'] = relationship(back_populates='order_items')
    order: Mapped['Order'] = relationship(back_populates='order_items')
    # ...
The result is that four relationship attributes are added, two for each one-to-many half of the many-to-many relationship. An
Order
instance can use its
order_items
relationship attribute to get the list of line items included in the order. Each element in the list returned by this relationship is going to be an instance of the
OrderItem
join table model, which provides access to the product, unit price and quantity.
Looking at the relationship from the product side, the
order_items
relationship attribute for a product represents the list of purchases, also instances of
OrderItem
, each providing a reference to the order (which in turn links to the customer), the unit price and quantity. Because a product is likely to have been sold many times, this part of the relationship is defined with the
write_only
loader, which would allow the application to query this list with filters, sorting options and pagination.
A New Database Migration
Now that the changes that implement customers and orders in
models.py
are complete, it is time to migrate the database, so that it receives these changes. Create a second database migration with the following command:
(venv) $ alembic revision --autogenerate -m "customers and orders"
After making sure that the generated migration script includes the three new tables, apply it to the database:
(venv) $ alembic upgrade head
At this point the database should be ready to accept customers and orders.
How to Create an Order
Many-to-many relationships with additional columns are extremely powerful, but they have the downside that they require more work compared to the simpler kind, since the join table has to be managed by the application.
How do you create an order with this solution? Here are the steps:
First, create a
Customer
instance, or load an existing one if this is a repeat customer.
Next, create an
Order
instance and associate it with the customer, either by passing the
customer
argument in the constructor, or by calling
add()
on the
Customer.orders
relationship.
For each line item in the order, create an
OrderItem
instance with the product, unit price and quantity, and append it to the order's
order_items
relationship.
If you prefer to see this in terms of actual code, the following session writes an order with two items in it:
>>> # import all the necessary things and create a session
>>> from models import Product, Customer, Order, OrderItem
>>> from db import Session
>>> session = Session()

>>> # create a new customer
>>> c = Customer(name='Jane Smith')

>>> # create a new order, add it to the customer and to the database session
>>> o = Order()
>>> c.orders.add(o)
>>> session.add(o)

>>> # add the first line item in the order: product #45 for $45.50
>>> p1 = session.get(Product, 45)
>>> o.order_items.append(OrderItem(product=p1, unit_price=45.5, quantity=1))

>>> # add the second line item: 2 of product #82 for $37 each
>>> p2 = session.get(Product, 82)
>>> o.order_items.append(OrderItem(product=p2, unit_price=37, quantity=2))

>>> # write the order (along with the customer and order items) to the database
>>> session.commit()

>>> # check the UUID and the timestamp defaults assigned to the new order
>>> o.id
UUID('a73c6aad-8ba9-4550-ac2f-1fcc9285cddc')
>>> o.timestamp
datetime.datetime(2023, 2, 24, 19, 52, 47, 293727)
Something that is worth noticing is that the methods used to add and remove items from a relationship are not always the same. For relationships that present themselves as standard Python lists, the
append()
and
remove()
methods are used. You can see how the
Order.order_items
relationship is used with
append()
in the example above.
Relationships that use the
write_only
loader do not follow list semantics because the related items are never loaded directly. These relationships are of type
WriteOnlyCollection
, and have
add()
and
delete()
methods. The above example uses
add()
on the
Customer.orders
relationship.
Deletions
As in previous relationships, it is important to understand what happens when an entity is deleted. If a
Product
or
Order
entity that is referenced in at least one
OrderItem
entry is deleted, SQLAlchemy will attempt to write a
NULL
in the invalidated foreign key of the
OrderItem
instance. Both foreign keys in this model are intentionally defined as required (non-nullable), so this attempt will fail. This was not a concern with the products and countries relationship because the
secondary
option of the relationship ensures that elements are removed from the join table when one of the linked entities is deleted.
There are two options to deal with this problem on many-to-many relationships that do not make use of the
secondary
option. One possible solution is to implement a "delete" cascade similar to the one configured in the
Manufacturer.products
relationship, which would automatically delete orphaned
OrderItem
entries, similarly to what SQLAlchemy does on
secondary
type relationships. Another option is to assume that products or orders cannot be deleted when there are
OrderItem
instances that reference them.
The second option is essentially a "do nothing" option, because SQLAlchemy returns an error when a product or an order are deleted. Making the foreign keys in the join table required is a convenient method to ensure that products or orders can only be deleted if there are no
OrderItem
instances pointing to them. To be able to delete an order, the application first needs to delete all the
OrderItem
entities associated with it, and only then the
Order
entity can be removed. For this relationship, this is the approach that will be taken.
Can
OrderItem
instances be deleted? Since no other entity in the database has foreign keys pointing to them, these entities can be deleted safely without any risk of database integrity errors. The
OrderItem
entities can be deleted from either side of the relationship, by removing the instances from the corresponding
order_items
relationship in the
Order
or
Product
models. Here is an example:
>>> # this assumes "oi" has the OrderItem instance to delete,

>>> # delete the OrderItem from an Order instance "o"
>>> o.order_items.remove(oi)
>>> session.commit()

>>> # delete the OrderItem from a Product instance "p"
>>> p.order_items.delete(oi)
>>> session.commit()
An Order Importer Script
To make it possible to run queries and experiment with a database full of orders, the following script imports a large number of randomly generated orders from a CSV file. Copy the following code to a file named
import_orders.py
in the project directory.
import_orders.py
: Import customers and orders from a CSV file
import csv
from datetime import datetime
from sqlalchemy import select, delete
from db import Session
from models import Product, Customer, Order, OrderItem


def main():
    with Session() as session:
        with session.begin():
            session.execute(delete(OrderItem))
            session.execute(delete(Order))
            session.execute(delete(Customer))

    with Session() as session:
        with session.begin():
            with open('orders.csv') as f:
                reader = csv.DictReader(f)
                all_customers = {}
                all_products = {}

                for row in reader:
                    if row['name'] not in all_customers:
                        c = Customer(name=row['name'], address=row['address'],
                                     phone=row['phone'])
                        all_customers[row['name']] = c
                    o = Order(
                        timestamp=datetime.strptime(row['timestamp'],
                                                    '%Y-%m-%d %H:%M:%S'))
                    all_customers[row['name']].orders.add(o)
                    session.add(o)

                    product = all_products.get(row['product1'])
                    if product is None:
                        product = session.scalar(select(Product).where(
                            Product.name == row['product1']))
                        all_products[row['product1']] = product
                    o.order_items.append(OrderItem(
                        product=product,
                        unit_price=float(row['unit_price1']),
                        quantity=int(row['quantity1'])))

                    if row['product2']:
                        product = all_products.get(row['product2'])
                        if product is None:
                            product = session.scalar(select(Product).where(
                                Product.name == row['product2']))
                            all_products[row['product2']] = product
                        o.order_items.append(OrderItem(
                            product=product,
                            unit_price=float(row['unit_price2']),
                            quantity=int(row['quantity2'])))

                    if row['product3']:
                        product = all_products.get(row['product3'])
                        if product is None:
                            product = session.scalar(select(Product).where(
                                Product.name == row['product3']))
                            all_products[row['product3']] = product
                        o.order_items.append(OrderItem(
                            product=product,
                            unit_price=float(row['unit_price3']),
                            quantity=int(row['quantity3'])))


if __name__ == '__main__':
    main()
A lot of the techniques used in this script are similar to those used in the product importer script. The first session block deletes all orders and customers to start from clean tables. Then in the second session block the CSV file is read and processed row by row.
Each line in the data file has information for an order, with the following fields:
name
: the customer's name.
address
: the customer's address.
phone
: the customer's phone number.
timestamp
: the date and time of the order.
product1
,
unit_price1
and
quantity1
: the first line item in this order.
product2
,
unit_price2
and
quantity2
: the second line item in this order, or a "0" value for
quantity2
to indicate that there is no second line item in this order.
product3
,
unit_price3
and
quantity3
: the third line item in this order, or a "0" value for
quantity3
to indicate that there is no third line item in this order.
The
all_customers
dictionary keeps track of the
Customer
instances that are created as orders are being read from the file, while the
all_products
dictionary maintains a cache of products that were loaded from the database, to reduce the number of queries issued.
An
Order
instance is created and linked to the customer. The
timestamp
attribute is explicitly set to the date and time imported from the CSV file, to prevent the
default
clause in this model from setting the timestamps of all the orders to the time at which the script is running.
To complete the order, one, two or three
OrderItem
instances are created and appended to it. For each order item, the product is loaded from the database with a query if it hasn't been seen before, or from the
all_products
cache when it is found there.
Before you run this script, a copy of the
orders.csv
file must be placed in the project directory. You can download this file from the book's
GitHub repository
.
Run the following command to execute the script and import all the orders:
(venv) $ python import_orders.py
This script should take a few seconds to import the orders.
Queries
With a database full of customers and orders, it is now possible to create a large variety of interesting queries. To begin, import all the needed classes and functions into a brand-new Python shell, and also create a database session:
>>> from sqlalchemy import select, func
>>> from db import Session
>>> from models import Product, Customer, Order, OrderItem
>>> session = Session()
Let's try out the new
write_only
relationship. The next query grabs a customer by name, then accesses the
orders
relationship attribute:
>>> c = session.scalar(
        select(Customer)
            .where(Customer.name == 'John Butler'))
>>> c
Customer(14a4d407bca54a69a0118715b664032a, "John Butler")
>>> c.orders
<sqlalchemy.orm.writeonly.WriteOnlyCollection object at 0x10ae1be20>
As you see, this type of relationship does not present itself as a list. But this
WriteOnlyCollection
object has a
select()
method that returns a query that retrieves the related objects when it is executed:
>>> session.scalars(c.orders.select()).all()
[Order(2971e3d105aa4394822c227da3f4a743), ..., Order(6e5214f6af744d02bea74a6228dec725)]
You can craft the same query by hand, but by having the
write_only
relationship this query is generated by SQLAlchemy. And because this is a query, it can be extended with additional clauses, unlike the list-type relationships you've seen before. Here are some examples of that:
>>> # sort the orders from newer to older
>>> session.scalars(
        c.orders.select()
            .order_by(Order.timestamp.desc())
    ).all()
[Order(4cbd2174ee6a4f52bc89a65ff74942d2), ..., Order(6e5214f6af744d02bea74a6228dec725)]

>>> # get one order at most
>>> session.scalar(
        c.orders.select()
            .limit(1))
Order(2971e3d105aa4394822c227da3f4a743)
Note that all these queries that print orders will show different primary key values on your own system, since the UUIDs are randomly generated when the orders are imported.
How many customers and orders are there in the system? The following queries obtain these counts:
>>> session.scalar(select(func.count(Customer.id)))
2754
>>> session.scalar(select(func.count(Order.id)))
4728
Each
OrderItem
instance contains the product's unit price and the quantity for a line item of an order, but they do not include the total price for the item, which needs to be calculated. The next query lists the three highest order item amounts, along with the product ordered.
>>> item_total = (OrderItem.unit_price * OrderItem.quantity).label(None)
>>> q = (select(item_total, Product)
            .join(Product.order_items)
            .order_by(item_total.desc())
            .limit(3))
>>> session.execute(q).all()
[(385.95000000000005, Product(127, "ZX Spectrum")), (283.16, Product(127, "ZX Spectrum")),
(259.98, Product(127, "ZX Spectrum"))]
To solve this query the price calculation needs to be made by multiplying the product's unit price by the quantity ordered. This is expressed by the
item_total
variable, which stores a labeled version of this calculation.
Note that the amounts returned by the query above may have very small variations depending on which database and database version you use. This happens due to the inaccurate nature of floating point math.
The requirements for this query are to list the order item's total price and the product, so those are the two arguments given to
select()
. Since these two arguments come from different tables in the database, a join is required. The
Product.order_items
argument to
join()
tells SQLAlchemy that this query will join the left-side entity, which is
Product
, with the right-side entity, which is
OrderItem
. It would be equivalent to use
Order.order_items
, the reverse relationship, and then the position of the tables in the join will be swapped, but the results would be the same.
The most interesting part of this query is that SQLAlchemy understands that the multiplication of the two columns stored in
item_total
is meant to be executed in the query instead of in the Python process. This can cause some confusion, as it is a somewhat "magical" behavior of SQLAlchemy. The columns attributes have their own custom implementation of the mathematical operators that do not really perform any calculations but instead transfer the operations to the SQL query, so that they are executed by the database.
If you are curious to see what is the SQL that is generated from this query, go ahead and print the query:
>>> print(q)
SELECT orders_items.unit_price * orders_items.quantity AS anon_1,
  products.id, products.name, products.manufacturer_id, products.year, products.cpu
FROM products JOIN orders_items ON products.id = orders_items.product_id
  ORDER BY anon_1 DESC LIMIT :param_1
This was an interesting query with some new challenges, but in reality it isn't very useful to look at individual order items, because these are part of an order, and orders can have many order items that were purchased together. A much more useful query would consider the total sale price of an order, adding all the order items. The next query finds the three most expensive orders, considering all their items combined. This may appear to be much harder to do, but the query is surprisingly similar to the one above:
>>> order_total = func.sum(OrderItem.unit_price * OrderItem.quantity).label(None)
>>> q = (select(Order, order_total)
            .join(Order.order_items)
            .group_by(Order)
            .order_by(order_total.desc())
            .limit(3))
>>> session.execute(q).all()
[(Order(a3e5d5187a7d420a8086dec947721a1c), 463.99),
(Order(4b659023464b43688f4eb49cc19cc787), 461.51),
(Order(8731df42c5fb45e7a90232d67dab3f9a), 443.3)]
The trick to make this query work is to use grouping, along with the
sum()
aggregation function. The query retrieves orders joined with their order items, and the results are grouped by the order, so that all the order items belonging to an order are collapsed into one result that can be aggregated.
The
item_total
calculation used in the previous query is replaced with
order_total
here, which applies the same multiplication to each order item, but given that the items in this query are grouped, they can be added together with the
sum()
function to obtain the order's grand total.
Note that depending on which database you are using and due to variations in the database drivers, the results of the
func.sum()
aggregation function may be returned as
decimal objects
, which represent numbers more accurately than the standard floating point arithmetic.
The next query finds the five products that sold the most units:
>>> units = func.sum(OrderItem.quantity).label(None)
>>> q = (select(Product, units)
            .join(Product.order_items)
            .group_by(Product)
            .order_by(units.desc())
            .limit(5))
>>> session.execute(q).all()
[(Product(41, "Commodore 64"), 2023), (Product(48, "Amiga"), 1578),
(Product(127, "ZX Spectrum"), 1004), (Product(16, "Apple II"), 600),
(Product(2, "BBC Micro"), 209)]
For this query, a labeled expression is created on the sum of the quantities of all the grouped order items. The query retrieves products joined with order items and groups the items by product.
Here once again you may see the sums reported as instances of the
Decimal
class from Python.
The one thing that is missing in the queries above is date ranges. Normally a business wants to calculate their sales statistics during a specific period such as a month or a quarter. The query above that returns the highest priced orders can be constrained to operate within a date range with an added
between()
condition in a
where()
clause. Here is how to calculate the top 3 orders in November 2022:
>>> from datetime import datetime
>>> order_total = func.sum(OrderItem.unit_price * OrderItem.quantity).label(None)
>>> q = (select(Order, order_total)
            .join(Order.order_items)
            .where(Order.timestamp.between(
                datetime(2022, 11, 1), datetime(2022, 12, 1)))
            .group_by(Order)
            .order_by(order_total.desc())
            .limit(3))
>>> session.execute(q).all()
[(Order(2cfeb68e0bed4fe7b0f3bbe707f194ee), 335.09000000000003),
(Order(5b02a2f26aa8499a96da008d3cff99f0), 318.48),
(Order(d53530d88c9f4f45b960bdddf1b89a40), 305.57)]
For the query that calculated the five best-selling products, there is a small complication when adding a date range, because that query does not use the
Order
model, which has the order timestamps. To be able to filter by date, this query needs an additional join between
OrderItem
and
Order
, which effectively means that the full many-to-many relationship between products and orders will be used.
>>> units = func.sum(OrderItem.quantity).label(None)
>>> q = (select(Product, units)
            .join(Product.order_items)
            .join(OrderItem.order)
            .where(Order.timestamp.between(
                datetime(2022, 11, 1), datetime(2022, 12, 1)))
            .group_by(Product)
            .order_by(units.desc())
            .limit(5))
>>> session.execute(q).all()
[(Product(41, "Commodore 64"), 157), (Product(48, "Amiga"), 139),
(Product(127, "ZX Spectrum"), 65), (Product(16, "Apple II"), 46),
(Product(2, "BBC Micro"), 23)]
Note how this many-to-many relationship, which was built using the association object pattern, needs explicit joins for its two legs, while the simpler relationship between products and countries that is based on the relationship's
secondary
argument SQLAlchemy automatically issues the two joins to the database from a single
join()
clause. This is another small convenience that is lost when manually managing the many-to-many relationship.
Many of the previous queries used a
between()
filter on the order timestamp to constrain the results to a particular period of time. Another common query pattern when working with timestamps is to obtain results grouped by some unit of time such as day, month, quarter or year. This is harder to do because the timestamps need to be transformed into something that can be used in a
group_by()
clause, so that all the results from each interval can be aggregated.
The following query extracts the year and the month from order timestamps using the
extract()
function, and then groups by them to calculate the total number of units sold monthly during the year 2022.
>>> month = func.extract('month', Order.timestamp).label(None)
>>> year = func.extract('year', Order.timestamp).label(None)
>>> units = func.sum(OrderItem.quantity).label(None)
>>> q = (select(year, month, units)
            .join(OrderItem)
            .where(Order.timestamp.between(
                datetime(2022, 1, 1), datetime(2023, 1, 1)))
            .group_by(year, month)
            .order_by(year, month))
>>> session.execute(q).all()
[(2022, 1, 505), (2022, 2, 426), (2022, 3, 525), ..., (2022, 12, 564)]
The
extract()
function accepts a unit such as
day
,
week
,
month
,
quarter
or
year
as first argument followed by a
datetime
column, and it returns the requested date or time component. The above example extracts the year and the month as individual result values, and then uses a compound
group_by()
clause that groups by both. Results are then sorted in ascending order by these same two values.
As mentioned earlier, with some databases results that are obtained through a calculation or function are returned as
Decimal
objects. The results printed in the above example came from SQLite, which uses standard int and float numbers. When using MySQL, you will get the same results, but the sums are decimal objects:
[(2022, 1, Decimal('505')), (2022, 2, Decimal('426')), ..., (2022, 12, Decimal('564'))]
When running the same query with PostgreSQL, the results come back in yet another format:
[(Decimal('2022'), Decimal('1'), 505), (Decimal('2022'), Decimal('2'), 426), ...,
Decimal('12'), 564)]
Here the results from the
extract()
function calls are decimal objects, while the sums are returned as integers. These are minor implementation differences between the database engines. When you receive a
Decimal
object you can convert it to a primitive integer type with the
int()
function:
>>> from decimal import Decimal
>>> int(Decimal('2022'))
2022
You can use the
float()
conversion function to convert a decimal object to floating point, but keep in mind that some precision may be lost in the conversion.
More Aggregation Techniques
The next feature you are going to add to the RetroFun database is to support customer written product reviews. A customer review consists of a star rating between 1 and 5 stars, plus an optional written comment.
Thinking about the implementation, a customer review ties a customer to a product, so there is going to be a new relationship between these two models. To decide which type of relationship is appropriate you have to think about the cardinality in each side of the relationship. Given that it is expected that a customer should be able to review many products, and a product can be reviewed by many customers, the relationship type that fits this problem is the many-to-many once again.
The following diagram shows a new
product_reviews
join table connects products and customers.
Should this use the simple many-to-many style from the previous chapter or the more advanced one used above for the orders? The relationship is going to need additional storage for the star rating and the review text, so the advanced solution based on the association object pattern is the correct choice.
Here is the model that represents the join table of this relationship, plus new relationship attributes in the
Product
and
Customer
models:
models.py
: Decomposed many-to-many relationship
from sqlalchemy import Text


class Product(Model):
    # ...
    reviews: WriteOnlyMapped['ProductReview'] = relationship(
        back_populates='product')
    # ...


class Customer(Model):
    # ...
    product_reviews: WriteOnlyMapped['ProductReview'] = relationship(
        back_populates='customer')
    # ...


class ProductReview(Model):
    __tablename__ = 'products_reviews'

    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'),
                                            primary_key=True)
    customer_id: Mapped[UUID] = mapped_column(ForeignKey('customers.id'),
                                              primary_key=True)
    timestamp: Mapped[datetime] = mapped_column(default=datetime.utcnow,
                                                index=True)
    rating: Mapped[int]
    comment: Mapped[Optional[str]] = mapped_column(Text)

    product: Mapped['Product'] = relationship(back_populates='reviews')
    customer: Mapped['Customer'] = relationship(
        back_populates='product_reviews')
This relationship is constructed in a way that is very similar to the one between products and orders. The join table is written as a
Model
subclass, and it contains three additional columns: one that stores the timestamp for the review (with a
default
option that automatically assigns the current time), the numeric rating and a comment. The timestamp and the star rating are required or non-nullable. The comment text is optional, and is given a type of
Text
instead of
String
, which SQLAlchemy uses for a possibly long block of text with unspecified maximum length.
Given that the list of product reviews can be large, the relationship attributes in the
Product
and
Customer
models are both configured with the
write_only
loader. The relationship attributes in the join table map to single entities, so those are set to the default lazy loading mechanism.
The commands to generate a new database migration with these changes and apply it to the database are:
(venv) $ alembic revision --autogenerate -m "product reviews"
(venv) $ alembic upgrade head
As with products and orders, it is useful to have some data in the database to be able to test queries. To that end, the following script imports a batch of product reviews from a CSV file.
import_reviews.py
: Import reviews from CSV file
import csv
from datetime import datetime
from sqlalchemy import select, delete
from db import Session
from models import Product, Customer, ProductReview


def main():
    with Session() as session:
        with session.begin():
            session.execute(delete(ProductReview))

    with Session() as session:
        with session.begin():
            with open('reviews.csv') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    c = session.scalar(select(Customer).where(
                        Customer.name == row['customer']))
                    p = session.scalar(select(Product).where(
                        Product.name == row['product']))
                    r = ProductReview(
                        customer=c,
                        product=p,
                        timestamp=datetime.strptime(row['timestamp'],
                                                    '%Y-%m-%d %H:%M:%S'),
                        rating=int(row['rating']),
                        comment=row['comment'] or None)
                    session.add(r)


if __name__ == '__main__':
    main()
This importer is simpler than the previous ones because it is importing data into a single table, the join table represented by the
ProductReview
model.
For this script, instead of using the
add()
method of the
write_only
relationship, the customer and product instances are assigned directly into each new
ProductReview
object, which achieves the same result.
The
reviews.csv
file must be in the project directory for the above script to work. You can download this file from the book's
GitHub repository
.
Run the next command to import all the reviews:
(venv) $ python import_orders.py
Queries
Now it is time to start a Python shell and run some queries. Start by importing all the necessary functions and classes, and creating a database session:
>>> from sqlalchemy import select, func
>>> from db import Session
>>> from models import Product, Customer, ProductReview
>>> session = Session()
The first query calculates the average of all customer star ratings:
>>> q = select(func.avg(ProductReview.rating))
>>> session.scalar(q)
3.7731384829505914
This query uses the
avg()
aggregation function, which calculates an average of all the input results. Remember that depending on the database that you use the result may be provided as a
Decimal
object instead of a plain number.
Something more useful is to calculate the average rating for a product. The next query obtains the rating for the ZX Spectrum home computer:
>>> p = session.scalar(
        select(Product)
            .where(Product.name == 'ZX Spectrum'))
>>> q = (select(func.avg(ProductReview.rating))
            .where(ProductReview.product == p))
>>> session.scalar(q)
4.0
Note how in this query the
where()
clause uses the
ProductReview.product
relationship to create the condition. The ORM module of SQLAlchemy converts this high-level condition to a more basic and equivalent one using the
ProductReview.product_id
foreign key that can be included in the SQL query.
Another interesting option is to generate a report with the average ratings of all products. The next query does that:
>>> product_rating = func.avg(ProductReview.rating).label(None)
>>> q = (select(Product, product_rating)
            .join(Product.reviews)
            .group_by(Product)
            .order_by(product_rating.desc(), Product.name))
>>> session.execute(q).all()
[(Product(19, "Apple IIc Plus"), 5.0), ..., (Product(138, "Timex Sinclair 1000"), 1.0)]
This query uses the
avg()
function along with grouping, so now the averages apply to the groups instead of the entire result set. The
Product
model is joined with
ProductReview
, so results from both can be requested in the
select()
portion of the query and in the
order_by()
clause, where the results are ordered first by rating from highest to lowest, and then alphabetically by product name.
As you recall, the
comment
column in the
ProductReview
model is optional. The next script generates a list of products with the percentage of its reviews that do not have a written comment.
>>> no_comment_percent = (
        100 - 100 * func.count(ProductReview.comment) / func.count(ProductReview.rating)
    ).label(None)
>>> q = (select(Product.name, no_comment_percent)
            .join(ProductReview.product)
            .group_by(Product)
            .order_by(no_comment_percent.desc(), Product.name))
>>> session.execute(q).all()
[('464 Plus', 100.0), ('Acorn Atom', 100.0), ..., ('ZX81', 0.0)]
The
no_comment_percent
labeled expression calculates the percentage of blank reviews using a clever trick. The
count()
function applied to the
ProductReview.comment
column will return the number of columns in each group that are not
NULL
, and the same function applied to the
ProductReview.rating
column will return the total count of reviews in each product group, because the rating is required and will have a value for every item. To calculate the percentage of blank reviews the percentage of written reviews is calculated as
100.0 * comments / total
, and then this amount is subtracted from 100 to get the percentage of the blank reviews. SQLAlchemy translates the multiplications, divisions and subtractions performed on these columns into the SQL query, so that the calculation is executed by the database.
The query selects the product name and the calculated percentage. It groups the rows by product so that the aggregation expression calculates percentages separately for each product. The results are finally sorted first by the percentage numbers in descending order, and then by product name.
Exercises
It's time to practice on your own. Write queries that return:
Orders above $300 in descending ordered by the sale amount from highest to lowest.
Orders that include one or more ZX81 computers.
Orders that include a product made by Amstrad.
Orders made on the 25th of December 2022 with two or more line items.
Customers with their first and last order date and time. Hint: the
min()
and
max()
functions can help with this query.
The top 5 manufacturers that had the most sale amounts, sorted by those amounts in descending order.
Products, their average star rating and their review count, sorted by review count in descending order.
Products and their average star rating, but only counting reviews that include a written comment.
Average star rating for the Commodore 64 computer in each month of 2022.
Customers with the minimum and maximum star rating they gave to a product, sorted alphabetically by customer name.
Manufacturers with their average star rating, sorted from highest to lowest rating.
Product countries with their average star rating, sorted from highest to lowest rating.
Proceed to
Chapter 6
.
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
