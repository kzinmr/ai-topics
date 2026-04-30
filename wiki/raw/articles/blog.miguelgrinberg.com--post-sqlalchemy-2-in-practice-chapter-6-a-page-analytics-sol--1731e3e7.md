---
title: "SQLAlchemy 2 In Practice - Chapter 6: A Page Analytics Solution"
url: "https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-6-a-page-analytics-solution"
fetched_at: 2026-04-30T07:01:19.754515+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# SQLAlchemy 2 In Practice - Chapter 6: A Page Analytics Solution

Source: https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-6-a-page-analytics-solution

This is the sixth chapter of my
SQLAlchemy 2 in Practice
book. If you'd like to support my work, I encourage you to buy this book, either directly from
my store
or on
Amazon
. Thank you!
The goal of this chapter is to use the concepts you have learned to build a web traffic analytics solution. This will serve as reinforcement of the techniques demonstrated in previous chapters as well as an example of a more complex and realistic database design.
For your reference, here is a summary of the book contents:
Part 1: Blog Articles and Authors
Like many companies in the real world, RetroFun has a blog, in which authors post articles intended to promote sales. In this section you will expand the database to keep track of the articles that are published in the company blog, with the purpose of later tracking web traffic to them.
The code block that follows adds models for blog articles and authors.
models.py
: Blog articles and authors
class Product(Model):
    # ...
    blog_articles: WriteOnlyMapped['BlogArticle'] = relationship(
        back_populates='product')
    # ...


class BlogArticle(Model):
    __tablename__ = 'blog_articles'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(128), index=True)
    author_id: Mapped[int] = mapped_column(ForeignKey('blog_authors.id'),
                                           index=True)
    product_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('products.id'), index=True)
    timestamp: Mapped[datetime] = mapped_column(default=datetime.utcnow,
                                                index=True)

    author: Mapped['BlogAuthor'] = relationship(back_populates='articles')
    product: Mapped[Optional['Product']] = relationship(
        back_populates='blog_articles')

    def __repr__(self):
        return f'BlogArticle({self.id}, "{self.title}")'


class BlogAuthor(Model):
    __tablename__ = 'blog_authors'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True)

    articles: WriteOnlyMapped['BlogArticle'] = relationship(
      back_populates='author')

    def __repr__(self):
        return f'BlogAuthor({self.id}, "{self.name}")'
The
BlogArticle
model maintains a title, foreign keys to an author and a product, and the publication date. The
BlogAuthor
model just stores the author's name. For these two models the primary keys are standard auto-incrementing integers.
There are two new one-to-many relationships introduced with this change. One is from authors to articles, managed by the
BlogAuthor.articles
and
BlogArticle.author
attributes, and the other is from products to articles, managed by
Product.articles
and
BlogArticle.product
.
The
BlogArticle.product_id
foreign key is the first in this project that has been defined as optional, meaning that a blog article is not required to be linked to a product. The idea is that the company blog is going to feature a variety of articles, some specifically related to a product (such as a review), while others that are more general. The
BlogArticle.product
relationship object is also typed as optional, because its value will be
None
when
product_id
is not set.
Part 2: Blog Sessions and Views
In this second phase of this implementation, blog users and sessions are introduced. Each visitor to the blog will be considered a "blog user", regardless of being a known customer or an anonymous visitor.
The assumption is that the RetroFun website will use cookies or a similar mechanism to keep track of its visitors. Each time a user enters the blog a new session will be created for the user, and all the blog articles that the user views during that visit will be recorded under that session. The next code block shows the definition of the
BlogUser
and
BlogSession
models.
models.py
: Blog users and sessions
class Customer(Model):
    # ...
    blog_users: WriteOnlyMapped['BlogUser'] = relationship(
        back_populates='customer')
    # ...


class BlogUser(Model):
    __tablename__ = 'blog_users'

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    customer_id: Mapped[Optional[UUID]] = mapped_column(
        ForeignKey('customers.id'), index=True)

    customer: Mapped[Optional['Customer']] = relationship(
        back_populates='blog_users')
    sessions: WriteOnlyMapped['BlogSession'] = relationship(
        back_populates='user')

    def __repr__(self):
        return f'BlogUser({self.id.hex})'


class BlogSession(Model):
    __tablename__ = 'blog_sessions'

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey('blog_users.id'),
                                          index=True)

    user: Mapped['BlogUser'] = relationship(back_populates='sessions')

    def __repr__(self):
        return f'BlogSession({self.id.hex})'
Both users and sessions use UUID primary keys, because in a web application these identifiers may be stored in cookies that may be potentially visible to visitors. As explained previously, using auto-incrementing numeric identifiers is not recommended in cases where public exposure may give away the size of the underlying database tables.
Two one-to-many relationships are also introduced. One is between blog users and blog sessions, and the other between customers and blog users. The thinking behind these two relationships is based on the assumption that the RetroFun website will be able to "remember" users across different visits. A possible implementation for the user tracking logic could be as follows:
When a visitor enters the website for the first time, a new blog user is created and its identifier is stored in a cookie on the client's browser. A blog session is also started, and linked to the blog user.
When a visitor enters the website and a blog user cookie is found, only a new session is created, and linked to the blog user found in the cookie.
On any page visit to the blog, if the user is also logged in to the RetroFun website as a customer, a link between the customer and the blog user is stored.
The
BlogUser.customer_id
foreign key that supports the link between customers and blog users is defined as optional, because many blog users will not be customers. There is also the possibility that a customer visits the blog without being logged in, and in that case they will not be recognized. The important aspect of this solution is that the RetroFun website should make an effort to match blog users to customers, as this will allow for more interesting reports to be generated, as you will see later.
It may not be immediately clear why the relationship between customers and blog users is defined as a one-to-many, instead of a one-to-one. The reason is that a person will not always be represented by a single blog user in the RetroFun database. For example, when an anonymous visitor opens the website on their phone and later on their laptop, there will be two different blog users created. If later this user makes a purchase and becomes a customer, the intention is that eventually this customer will be linked to both blog users, so that their behavior both on the phone and the laptop can be analyzed.
What's left to do is to create an association between blog articles and sessions, which would record which articles were viewed under a session by a user, so in simpler words, a table that record page views. The RetroFun website would insert an entry into this table whenever a blog user visits a blog article. Thinking about this new table, it is clear that it is a join table for a many-to-many relationship between articles and sessions, because an article can be viewed in many sessions, and a session can have many articles viewed.
models.py
: Blog views
class BlogArticle(Model):
    # ...
    views: WriteOnlyMapped['BlogView'] = relationship(back_populates='article')
    # ...


class BlogSession(Model):
    # ...
    views: WriteOnlyMapped['BlogView'] = relationship(back_populates='session')
    # ...


class BlogView(Model):
    __tablename__ = 'blog_views'

    id: Mapped[int] = mapped_column(primary_key=True)
    article_id: Mapped[int] = mapped_column(ForeignKey('blog_articles.id'))
    session_id: Mapped[UUID] = mapped_column(ForeignKey('blog_sessions.id'))
    timestamp: Mapped[datetime] = mapped_column(default=datetime.utcnow,
                                                index=True)

    article: Mapped['BlogArticle'] = relationship(back_populates='views')
    session: Mapped['BlogSession'] = relationship(back_populates='views')
For this relationship, it is useful to store the date and time of the page view, which means that the advanced association object style has to be used.
This relationship presents an interesting problem that did not exist in any of the previous many-to-many relationships. A user may view a given article two or more times, all in the context of a single web session, for example, by refreshing the page in the browser, which means it should be possible to have two or more
BlogView
entries that have the same article and session foreign keys.
As you recall, many-to-many relationships set the two foreign keys as a compound primary key for the join table, which prevents duplicate records. Preventing duplicates is useful in many situations, but for this particular relationship duplicates should be allowed so that all page views can be accurately counted. The tweak that is made to allow the duplicates is to use a standard numeric auto-incremented
id
as primary key instead of a compound primary key made up of the two foreign keys.
To help you keep track of the current database structure, here is a diagram showing all the tables and relationships up to this point.
Believe it or not, this is all it takes to have storage for a basic page analytics solution. Now it's time to migrate the database so that all these changes are recorded and applied:
(venv) $ alembic revision --autogenerate -m "blog integration"
(venv) $ alembic upgrade head
Importer Scripts
As with all previous tables, it is useful to add some data so that it is possible to experiment with queries. Here is a script that imports articles and authors from a CSV file:
import_articles.py
: Article importer script
import csv
from datetime import datetime
from sqlalchemy import select, delete
from db import Session
from models import BlogArticle, BlogAuthor, Product, BlogView, BlogSession, \
    BlogUser


def main():
    with Session() as session:
        with session.begin():
            session.execute(delete(BlogView))
            session.execute(delete(BlogSession))
            session.execute(delete(BlogUser))
            session.execute(delete(BlogArticle))
            session.execute(delete(BlogAuthor))

    with Session() as session:
        with session.begin():
            all_authors = {}
            all_products = {}

            with open('articles.csv') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    author = all_authors.get(row['author'])
                    if author is None:
                        author = BlogAuthor(name=row['author'])
                        all_authors[author.name] = author

                    product = None
                    if row['product']:
                        product = all_products.get(row['product'])
                        if product is None:
                            product = session.scalar(select(Product).where(
                                Product.name == row['product']))
                            all_products[product.name] = product

                    article = BlogArticle(
                        title=row['title'],
                        author=author,
                        product=product,
                        timestamp=datetime.strptime(
                            row['timestamp'], '%Y-%m-%d %H:%M:%S'
                        ),
                    )
                    session.add(article)


if __name__ == '__main__':
    main()
This script uses the same techniques used in previous importers to create
BlogArticle
and
BlogAuthor
entries in the database, so it should be self-explanatory.
The
articles.csv
file referenced in the script must be copied to the project directory. You can download this file from the book's
GitHub repository
. Note that the article titles and author names used in this data file were created with a fake data generator, so they are not real.
Run the following command to execute the script and import the articles and authors into the database:
(venv) $ python import_articles.py
The next script imports page views, along with blog users and sessions. Here is the code for it:
import_views.py
: Blog page views importer script
import csv
from datetime import datetime
from uuid import UUID
from sqlalchemy import select, delete
from db import Session
from models import BlogArticle, BlogUser, BlogView, BlogSession, Customer


def main():
    with Session() as session:
        with session.begin():
            session.execute(delete(BlogView))
            session.execute(delete(BlogSession))
            session.execute(delete(BlogUser))

    with Session() as session:
        all_articles = {}
        all_customers = {}
        all_blog_users = {}
        all_blog_sessions = {}

        with open('views.csv') as f:
            reader = csv.DictReader(f)

            i = 0
            for row in reader:
                user = all_blog_users.get(row['user'])
                if user is None:
                    customer = None
                    if row['customer']:
                        customer = all_customers.get(row['customer'])
                        if customer is None:
                            customer = session.scalar(select(Customer).where(
                                Customer.name == row['customer']))
                            all_customers[customer.name] = customer

                    user_id = UUID(row['user'])
                    user = BlogUser(id=user_id, customer=customer)
                    session.add(user)
                    all_blog_users[row['user']] = user

                blog_session = all_blog_sessions.get(row['session'])
                if blog_session is None:
                    session_id = UUID(row['session'])
                    blog_session = BlogSession(id=session_id, user=user)
                    session.add(blog_session)
                    all_blog_sessions[row['session']] = blog_session

                article = all_articles.get(row['title'])
                if article is None:
                    article = session.scalar(select(BlogArticle).where(
                        BlogArticle.title == row['title']))
                    all_articles[article.title] = article

                view = BlogView(
                    article=article,
                    session=blog_session,
                    timestamp=datetime.strptime(
                        row['timestamp'], '%Y-%m-%d %H:%M:%S'),
                )
                session.add(view)

                i += 1
                if i % 100 == 0:
                    print(i)
                    session.commit()
            print(i)
            session.commit()


if __name__ == '__main__':
    main()
This importer uses the database session in a way that is different from the previous ones. The reason for the change is that a page view table is likely to hold a much larger volume of data than other tables. To reflect this reality, the CSV file with example data is significantly larger, enough that accumulating all the imported data into a single database session that is committed at the end is highly impractical.
Instead of relying on the
session.begin()
context manager that commits at the end, this importer keeps a count of imported rows and issues explicit commits every 100 rows. The logic that achieves this uses a counter. Here is the code specific to this isolated from the rest:
i = 0
            for row in reader:

                # ... import the row

                i += 1
                if i % 100 == 0:
                    print(i)
                    session.commit()
            print(i)
            session.commit()
The
print(i)
statement will print 100, 200, etc. to the terminal, to show progress. The second print and commit at the bottom ensure that the final set of rows that were imported right before the loop exited are also stored.
Download the
views.csv
file from the book's
GitHub repository
. As mentioned above, this is a fairly large data file (about 19MB), so it may take some time to download depending on your connection speed.
Run the importer as follows:
(venv) $ python import_views.py
Once the import process starts you will start seeing multiples of 100 printing to the terminal. This is a fairly large data file, so it will take a few minutes for the script to go through the entire CSV file, which has about 138,000 rows.
Page Analytics Queries
With all this new information in the database, there are a number of very interesting queries that can be made. Open a new Python session, import all the required dependencies, and create a new database session:
>>> from datetime import datetime
>>> from sqlalchemy import select, func
>>> from db import Session
>>> from models import BlogArticle, BlogView, Product
>>> session = Session()
To start with the obvious, you may want to know the total number of pages viewed over a specific period of time. The next query calculates total page views in November 2022:
>>> q = (select(func.count(BlogView.id))
            .where(BlogView.timestamp.between(
                datetime(2022, 11, 1), datetime(2022, 12, 1))))
>>> session.scalar(q)
4034
The query that follows shows the ranking of blog articles from most to least viewed, also for the month of November 2022:
>>> page_views = func.count(BlogView.id).label(None)
>>> q = (select(BlogArticle.title, page_views)
            .join(BlogArticle.views)
            .where(BlogView.timestamp.between(
                datetime(2022, 11, 1), datetime(2022, 12, 1)))
            .group_by(BlogArticle)
            .order_by(page_views.desc(), BlogArticle.title))
>>> session.execute(q).all()
[('Boy itself fish traditional', 57), ..., , ('Still defense foreign social', 1)]
If you were to add all the views reported by this query, the total would come up to 4034, which makes perfect sense since this and the previous queries are retrieving exactly the same page views, just organized in different ways.
As you recall, articles can be associated with a specific product in the
BlogArticle.product
relationship. This makes it possible to navigate across relationships and get a report of page views associated with each product:
>>> page_views = func.count(BlogView.id).label(None)
>>> q = (select(Product.name, page_views)
            .join(Product.blog_articles)
            .join(BlogArticle.views)
            .where(BlogView.timestamp.between(
                datetime(2022, 11, 1), datetime(2022, 12, 1)))
            .group_by(Product)
            .order_by(page_views.desc()))
>>> session.execute(q).all()
[('ZX Spectrum', 1096), ('Commodore 64', 1056), ('Apple II', 349),
('TRS-80 Color Computer', 349), ('Amiga', 301), ('BBC Micro', 180), ('TI-99/4A', 133),
('Commodore 128', 77)]
Now this is an interesting query. If you add up all the page views the total is 3541, not 4034 as in the previous queries. Can you guess why?
The
BlogArticle.product_id
foreign key was configured as optional (or "nullable", in database jargon) column. The page views for articles without a product association are not included in this report, because the
join(Product.blog_articles)
clause pairs
Product
instances against
BlogArticle
instances where the product matches in both. The
BlogArticle
instances that have
product_id
(and consequently also the
product
relationship) set to
None
will not match anything on the
Product
side and will be omitted from the join.
A join that only includes matching rows from the two tables is said to be an
inner join
. This is the default join that SQLAlchemy's
join()
method uses, and the only type used in this book so far. But inner joins are not the only type of join that can be used.
Another way to join two tables is with an
outer join
, which also includes entities on each side of the relationship that do not match anything on the other side. Outer joins come in three types:
Full outer join: include unmatched entities of the left and right tables
Left outer join: include unmatched entities of the left table only
Right outer join: include unmatched entities of the right table only
What does this all mean, exactly? The results of a full outer join between blog articles and products are going to combine three different types of records:
Matching blog article and product pairs (these are the results returned by the default inner join query)
Blog articles that have no matching product (the product will be
None
in these results)
Products that have no matching blog articles (the blog article will be
None
in these results)
Note:
Unfortunately support for outer joins is not uniform across databases.
SQLite supports all the outer join types, but full and right outer joins were added in release 3.39.0 from 2022, which isn't widely deployed still. An error will be returned if these types of joins are attempted when using previous releases.
MySQL supports left and right outer joins, but as of April 2023 it does not support full outer joins.
PostgreSQL supports all the outer join types.
SQLAlchemy only implements full and left outer joins. When a right outer join is desired, the tables must be swapped so that a left outer join can be used.
Changing the first join of the previous query to a full outer join will ensure that all the blog articles (which are on the right side in that join) are retrieved, and not just those that can be matched against a product. Then the next join against
BlogView
will not drop any page views. The only change to convert the default inner join to a full outer join is to add a
full=True
argument to the
join()
clause:
>>> q = (select(Product.name, page_views)
            .join(Product.blog_articles, full=True)
            .join(BlogArticle.views)
            .where(BlogView.timestamp.between(
                datetime(2022, 11, 1), datetime(2022, 12, 1)))
            .group_by(Product)
            .order_by(page_views.desc()))
>>> session.execute(q).all()
[('ZX Spectrum', 1096), ('Commodore 64', 1056), (None, 493), ('Apple II', 349),
('TRS-80 Color Computer', 349), ('Amiga', 301), ('BBC Micro', 180), ('TI-99/4A', 133),
('Commodore 128', 77)]
Note how these new results include an item with the product set to
None
containing the 493 page views that were missed in the previous report.
This query could have also used a right outer join, which might even be more efficient, but as noted above, SQLAlchemy does not currently have support for this join type. It was also noted that full outer joins are not implemented by all databases, so depending on your database choice the above query may fail with a database error. In particular, this query would not work with MySQL or with older versions of SQLite.
What can be done when full outer joins are not available? Luckily, this query does not require a full outer join but just a right outer join. The trick is to reverse the join direction and then use a left outer join, which is generated with the
isouter=True
argument added to the
join()
clause. Here is how to do it:
>>> q = (select(Product.name, page_views)
            .join(BlogArticle.product, isouter=True)
            .join(BlogArticle.views)
            .where(BlogView.timestamp.between(
                datetime(2022, 11, 1), datetime(2022, 12, 1)))
            .group_by(Product)
            .order_by(page_views.desc()))
>>> session.execute(q).all()
[('ZX Spectrum', 1096), ('Commodore 64', 1056), (None, 493), ('Apple II', 349),
('TRS-80 Color Computer', 349), ('Amiga', 301), ('BBC Micro', 180), ('TI-99/4A', 133),
('Commodore 128', 77)]
In this version of the query, the first join switches from the
Product.blog_articles
relationship to
BlogArticle.product
. These two attributes represent the relationship between products and blog articles from the two sides, so this change effectively reverses the direction of the join, putting blog articles on the left side and products on the right, which makes it possible to use a left outer join to retrieve blog articles with no product matching.
Isn't it interesting that the full and right outer join queries above return the exact same results? When using a full outer join there should have been more data in the results, right? The results include the page view counts for blog articles that are associated with products, and the page views for blog articles that have no associated product. But when using the full outer join, the results should have also included all the products that have no associated blog articles, which should have appeared with zero page views. Why are those missing?
To understand this you have to review the rest of the full outer join version of this query. After the full outer join is performed, there is another join with the
BlogView
entities, and this join is a default inner join. This second join matches pairs of products and articles that resulted from the full outer join to
BlogView
records, using the
BlogArticle.views
relationship as the matching column. Because this is an inner join, all the (
Product
,
None
) pairs returned by the first join are discarded, since the article portion of the pair is
None
and will never match anything on the
BlogView
side.
If the intention is to preserve those products that have no blog views, then the second join must also be upgraded to a full outer join, which will ensure that all the (
Product
,
BlogArticle
,
BlogView
) triplets in which both the article and the view are
None
are kept in the results.
But if the second join is changed to a full outer join, there are going to be some results with a
None
for the
BlogView
entity. The
where()
clause in this query uses
BlogView.timestamp
, so this has to be updated to allow not only the page views that are in the period of interest but also those that are
None
. This can be done with the
or_()
function. Here is the final query:
>>> from sqlalchemy import or_
>>> q = (select(Product.name, page_views)
            .join(Product.blog_articles, full=True)
            .join(BlogArticle.views, full=True)
            .where(or_(
                BlogView.timestamp == None,
                BlogView.timestamp.between(
                    datetime(2022, 11, 1), datetime(2022, 12, 1))))
            .group_by(Product)
            .order_by(page_views.desc(), Product.name))
>>> session.execute(q).all()
[('ZX Spectrum', 1096), ('Commodore 64', 1056), (None, 493), ..., ('ZX80', 0), ('ZX81', 0)]
And this query returns a report of all the products, with their page view counts for the given period, including page views for generic articles not associated with a product and products with no articles written about them or with no blog views. But of course, this complete version requires a full outer join, which isn't available in some databases.
Generating this last query using only left outer joins is difficult, because no matter which way the joins are configured there is always going to be one side of unmatched entities that is not going to come back with the results. A common solution to simulate full outer joins is to run two queries instead of one. The left outer join query used above can be used to get the list of products with their page views, plus the page views for articles without a product assignment. Then a second query can be used to get the list of products that had no blog views, either because they have no content in the blog or because their content hasn't been viewed by anyone. Here is a query that retrieves these:
>>> q2 = (select(Product.name, page_views)
            .join(Product.blog_articles, isouter=True)
            .join(BlogArticle.views, isouter=True)
            .where(or_(
                BlogView.timestamp == None,
                BlogView.timestamp.between(
                    datetime(2022, 11, 1), datetime(2022, 12, 1))))
            .group_by(Product)
            .having(page_views == 0)
            .order_by(Product.name))
>>> session.execute(q2).all()
[('464 Plus', 0), ('6128 Plus', 0), ..., ('ZX80', 0), ('ZX81', 0)]
For this query the products are joined with the blog articles, and the resulting pairs are joined with the blog views. Both joins are left outer joins, which means that products that have no matching blog articles or no matching blog views in the period of interest will be kept in the results. The
having()
clause discards any results that have non-zero page views, since those were already captured by the first query.
You can now combine the results from the two queries in Python, or if you prefer, you can use the
union()
function from SQLAlchemy to have this merge done by the database. Below you can see how to write two queries
q1
and
q2
, which get consolidated into
q
using the union operator:
>>> from sqlalchemy import union
>>> q1 = (select(Product.name, page_views)
            .join(BlogArticle.product, isouter=True)
            .join(BlogArticle.views)
            .where(BlogView.timestamp.between(
                datetime(2022, 11, 1), datetime(2022, 12, 1)))
            .group_by(Product))
>>> q2 = (select(Product.name, page_views)
            .join(Product.blog_articles, isouter=True)
            .join(BlogArticle.views, isouter=True)
            .where(or_(
                BlogView.timestamp == None,
                BlogView.timestamp.between(
                    datetime(2022, 11, 1), datetime(2022, 12, 1))))
            .group_by(Product)
            .having(page_views == 0))
>>> q = union(q1, q2).order_by(page_views.desc(), Product.name)
>>> session.execute(q).all()
[('ZX Spectrum', 1096), ('Commodore 64', 1056), (None, 493), ..., ('ZX80', 0), ('ZX81', 0)]
Once you work with outer joins you will find lots of queries that are improved by upgrading inner joins to one of the outer join types. For example, the query that returns page views by article presented earlier in this chapter did not include the articles that received no page views in the results, because the inner join between blog articles and blog views discarded those articles. Changing this query to use a left outer join preserves the articles without views. Here is the updated query:
>>> page_views = func.count(BlogView.id).label(None)
>>> q = (select(BlogArticle.title, page_views)
            .join(BlogArticle.views, isouter=True)
            .where(or_(
                BlogView.timestamp == None,
                BlogView.timestamp.between(
                    datetime(2022, 11, 1), datetime(2022, 12, 1))))
            .group_by(BlogArticle)
            .order_by(page_views.desc()))
>>> session.execute(q).all()
[..., ('Prepare culture part budget star organization there', 0)]]
The updated query reveals that there was only one article in November 2022 that did not receive page views, appearing at the bottom of the list of results with a count of zero views.
To make this query work, not only the join was changed to a left outer join, but also the
where()
clause was expanded to accept
BlogView
results that are
None
, as in the previous query.
Part 3: Multi-Language Blog Articles
Like many companies, RetroFun is interested in selling internationally. To that effect, it creates original blog content in other languages besides English, and it also has a team dedicated to translate successful English blog posts to other languages.
To make the web analytics project even more useful, in this third and last phase of the project you will learn how to expand the database to keep track of the language in which each article is written, and also which articles are translations of other articles instead of original pieces of content. This will lead to many more interesting reports that can be extracted from the data.
The first change adds a
Language
model, plus a one-to-many relationship between languages and blog articles.
models.py
: Blog article languages
class BlogArticle(Model):
    # ...
    language_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('languages.id'), index=True)
    # ...
    language: Mapped[Optional['Language']] = relationship(
        back_populates='blog_articles')
    # ...


class Language(Model):
    __tablename__ = 'languages'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32), index=True, unique=True)

    blog_articles: WriteOnlyMapped['BlogArticle'] = relationship(
        back_populates='language')

    def __repr__(self):
        return f'Language({self.id}, "{self.name}")'
This new one-to-many relationship is very much like previous ones, so it does not present any challenge.
Tracking a relationship between original content and their translations does seem tricky, however. Which relationship type works for this use case? An original article can have many translations, and each translated article can only have one original source. This suggests this is going to be a one-to-many relationship.
What are the two entities of the relationship? Very clearly the "one" side of the relationship is going to be original articles, which are instances of the
BlogArticle
model. What about the "many" side? These are also articles, right? This is the first time in this project where a relationship has the same entity,
BlogArticle
in this case, on both sides. This is called a
self-referential relationship
.
With SQLAlchemy, self-referential relationships need some additional configuration. Below are the changes to the
BlogArticle
model to add this relationship.
models.py
: Blog article translations
class BlogArticle(Model):
    # ...
    translation_of_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey('blog_articles.id'), index=True)
    # ...
    translation_of: Mapped[Optional['BlogArticle']] = relationship(
        remote_side=id, back_populates='translations')
    translations: Mapped[list['BlogArticle']] = relationship(
        back_populates='translation_of')
    # ...
The
translation_of_id
foreign key is defined in the same way as other foreign keys, with the only difference that it references the primary key in the same table.
The two relationship attributes that represent the sides of the relationship now have to be added to the same model class, and this requires some care. SQLAlchemy cannot easily figure out which of the two relationship attributes is which in a self-referential relationship, so the
remote_side
argument is added to the
relationship()
definition that references the "one" side to remove the ambiguity. In this case, the
translation_of
relationship has its
remote_side
argument set to the
id
primary key, and this is enough for SQLAlchemy to understand that this relationship points to the "one" side and consequently the other relationship is the list with the "many" side.
The following diagram shows the database table diagram after the new
translation_of_id
foreign key column is added to the
blog_articles
table. This is the final version of the RetroFun database.
These changes can now be incorporated in a database migration:
(venv) $ alembic revision --autogenerate -m "multi-language support"
(venv) $ alembic upgrade head
The
articles.csv
data file that was used earlier to import articles and authors already includes
language
and
translation_of
columns, which the
import_articles.py
script ignored. With the new multi-language support, a second pass through this file can import this additional information. The
import_languages.py
script shown below does this.
import_languages.py
: Import language and translation relationships
import csv
from sqlalchemy import select
from db import Session
from models import BlogArticle, Language


def main():
    with Session() as session:
        with session.begin():
            all_articles = {}
            all_languages = {}

            with open('articles.csv') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    article = all_articles.get(row['title'])
                    if article is None:
                        article = session.scalar(select(BlogArticle).where(
                            BlogArticle.title == row['title']))
                        all_articles[article.title] = article

                    language = all_languages.get(row['language'])
                    if language is None:
                        language = session.scalar(select(Language).where(
                            Language.name == row['language']))
                        if language is None:
                            language = Language(name=row['language'])
                            session.add(language)
                        all_languages[language.name] = language
                    article.language = language

                    if row['translation_of']:
                        translation_of = all_articles.get(
                            row['translation_of'])
                        if translation_of is None:
                            translation_of = session.scalar(select(
                                BlogArticle).where(BlogArticle.title ==
                                                   row['translation_of']))
                            all_articles[article.title] = article
                        article.translation_of = translation_of


if __name__ == '__main__':
    main()
The script reads the rows of
articles.csv
, only looking at the article's
title
,
language
and
translation_of
columns. No articles are inserted in this script, articles are directly loaded from the database by their title, because the assumption is that the
import_articles.py
script has already imported all of them.
For the language support, the script assigns the corresponding
Language
instance to the
BlogArticle.language
attribute, creating new
Language
instances when a language appears for the first time. As before, the
all_languages
dictionary keeps a cache of all the languages added so far for convenience.
The
translation_of
column of the CSV file is empty for original articles, so the script first checks if there is a value for this column. When a value exists it means that the article is translated, and the value of this field is the title of the original article. The translated article is then assigned the original in the
translation_of
self-referential relationship.
Run the script to incorporate the language and translation relationships:
(venv) $ python import_languages.py
Language Queries
The language support adds one more dimension to the queries that can be generated. Open a new Python session and import the usual components needed to experiment:
>>> from datetime import datetime
>>> from sqlalchemy import select, func
>>> from models import Language, BlogArticle, BlogView
>>> from db import Session
>>> session = Session()
First, here is an easy query that returns the number of articles in each language:
>>> q = (select(Language, func.count(BlogArticle.id))
            .join(Language.blog_articles)
            .group_by(Language)
            .order_by(Language.name))
>>> session.execute(q).all()
[(Language(1, "English"), 108), (Language(3, "French"), 25), (Language(2, "German"), 21),
(Language(4, "Italian"), 13), (Language(6, "Portuguese"), 25), (Language(5, "Spanish"), 17)]
These counts are for all the articles, regardless of being original or a translation. The next two queries generate counts for originals and for translations separately:
>>> q = (select(Language, func.count(BlogArticle.id))
            .join(Language.blog_articles)
            .where(BlogArticle.translation_of == None)
            .group_by(Language)
            .order_by(Language.name))
>>> session.execute(q).all()
[(Language(1, "English"), 108), (Language(3, "French"), 11), (Language(2, "German"), 6),
(Language(4, "Italian"), 5), (Language(6, "Portuguese"), 7), (Language(5, "Spanish"), 6)]
>>> q = (select(Language, func.count(BlogArticle.id))
            .join(Language.blog_articles)
            .where(BlogArticle.translation_of != None)
            .group_by(Language)
            .order_by(Language.name))
>>> session.execute(q).all()
[(Language(3, "French"), 14), (Language(2, "German"), 15), (Language(4, "Italian"), 8),
(Language(6, "Portuguese"), 18), (Language(5, "Spanish"), 11)]
These queries use the
BlogArticle.translation_of
relationship to filter the original content from the translations or vice versa because original articles always have this attribute set to
None
.
Note:
When writing expressions for SQLAlchemy that compare against
None
, the comparison has to be done with the
==
and
!=
operators. Many Python developers would prefer to use
is None
or
is not None
, but SQLAlchemy cannot translate these into SQL expressions.
The next query is more tricky. The goal is to generate a report of original articles, each with the number of available translations. The solution is to query for all the pairs of original and translated articles, then group by the original articles and apply a count function to the translation.
>>> from sqlalchemy.orm import aliased
>>> TranslatedBlogArticle = aliased(BlogArticle)
>>> article_count = func.count(TranslatedBlogArticle.id).label(None)
>>> q = (select(BlogArticle, article_count)
            .join(TranslatedBlogArticle.translation_of)
            .group_by(BlogArticle)
            .order_by(article_count.desc(), BlogArticle.title))
>>> session.execute(q).all()
[(BlogArticle(63, "Business seven ability cup church similar itself"), 3), ...,
(BlogArticle(1, "Within across act song"), 1)]
This query uses the
aliased
function, which you haven't seen before. To be able to pair articles with their translations, a join needs to be made on the self-referential
translation_of
relationship. But having the same table on the two sides of a relationship creates a complication, because when both sides have the same table name it is not possible to independently refer to the left or right sides. SQL solves the ambiguity of this situation with
aliases
. Giving one of the sides a new name makes it possible to work with two instances of the same table as if they were different. The
TranslatedBlogArticle
alias created above represents the left-side of the relationship when looking at it as a many-to-one relationship from translated articles into their originals.
So now there is
TranslatedBlogArticle
and
BlogArticle
, and a join is made between them. The
join(TranslatedBlogArticle.translation_of)
expression creates the join with the aliased table on the left, and the original on the right.
To be able to count the translations, the
TranslatedBlogArticle
instances are aggregated with the
count()
function. The counting expression is given a label, so that it can be reused in the
order_by()
clause, as done several times before.
This database design is extremely flexible and allows for even more complex and interesting queries. Let's say that the company wants to have a report of page views per article similar to those generated earlier, but with the additional complication that only original articles should be listed, with the aggregated page view counts that include their translations. For consistency with previous queries this is also going to cover page views in November 2022.
As you recall, the query that returned page views per article joined the
BlogArticle
and
BlogView
models, then grouped by
BlogArticle
and used the
count()
aggregation function to return how many rows were in each group. To be able to include page views of translated articles along with the original article, it is necessary to have a column in every result row that references the original article, and then this column can be used to group the results.
The
BlogArticle.translation_of
relationship has the reference to the original article, but for the original articles themselves this relationship is set to
None
. What this query needs is a column that works as a conditional: when the article is original, it should be a reference to that same article, but when the article is translated the reference should be to the parent article.
The SQL language provides a conditional that can be used to solve this problem, the
CASE
construct, which in SQLAlchemy is available through the
case()
function. Here is a labeled column definition that uses this function:
>>> from sqlalchemy import case
>>> original_id = case(
        (BlogArticle.translation_of == None, BlogArticle.id),
        else_=BlogArticle.translation_of_id).label(None)
The
case()
function accepts one or more tuples as arguments. Each tuple has a condition in the first element, and a value in the second. The result of the case expression takes the value from the first tuple for which the condition evaluates to
True
. The
else_
argument provides a value to use when none of the tuples have a condition that evaluates to
True
.
In the above definition,
case()
has a single condition that checks for the
translation_of
relationship being
None
, which indicates that the article is an original. In that case, the value that will be assigned to that column is the
id
of the article. When the condition is
False
, the
else_
argument provides an alternative value of the column from the
translation_of_id
attribute, which has the
id
of the parent article.
Note:
As much as possible it is preferred to work with ORM entities, but the values used in the
case()
function cannot be set to model entities, and for that reason primary key identifiers are used instead.
Now this
original_id
column can be used in a
group_by()
clause instead of the blog article that was used before.
>>> page_views = func.count(BlogView.id).label(None)
>>> q = (select(original_id, page_views)
            .join(BlogArticle.views)
            .where(BlogView.timestamp.between(
                datetime(2022, 11, 1), datetime(2022, 12, 1)))
            .group_by(original_id)
            .order_by(page_views.desc()))
>>> session.execute(q).all()
[(171, 136), (76, 107), (98, 99), ..., (112, 2), (31, 2), (201, 1)]
And unfortunately this isn't the expected result, right? The query groups by
original_id
values, which are numeric primary key values assigned to
BlogArticle
instances. Using primitive values was required to be able to use the
case()
function, but now it would be ideal to convert these numbers back to the entities they represent.
A nice little trick that can solve this problem is to join the
original_id
column with an aliased instance of
BlogArticle
, which would associate each number with its corresponding
BlogArticle
entity:
>>> OriginalBlogArticle = aliased(BlogArticle)
>>> q = (select(OriginalBlogArticle, page_views)
            .join(BlogArticle.views)
            .join(OriginalBlogArticle, original_id == OriginalBlogArticle.id)
            .where(BlogView.timestamp.between(
                datetime(2022, 11, 1), datetime(2022, 12, 1)))
            .group_by(OriginalBlogArticle)
            .order_by(page_views.desc()))
>>> session.execute(q).all()
[(BlogArticle(171, "Our activity public responsibility represent"), 136), ...,
(BlogArticle(201, "Exist they particular important note kitchen current"), 1)]
Here a second instance of the
BlogArticle
model is created as an alias, and stored with the name
OriginalBlogArticle
. Then an additional
join()
clause is added to the query to join the
original_id
values with it.
The
join()
call is the first that does not have a relationship in its first argument. When a relationship is given, SQLAlchemy can determine all the parameters of the join from it. In this case there is no relationship defined between the
original_id
values and the
OriginalBlogArticle
aliased model, so SQLAlchemy needs more details on how this join has to be carried out. This alternative format of the
join()
clause takes the right-side entity of the join as first argument, and a join condition as second argument. The join condition that was used above ensures that for each value of
original_id
the blog article with the same identifier is matched.
This query could be expanded to also return how many articles were considered for each of the results. For an article that has no translations a 1 would be returned, but for an article with some translations you would know how many articles were aggregated into the page view results.
To do this, a third column needs to be added to the query that counts the number of articles in each group. You have seen that the
count()
function counts rows, so using
count(BlogArticle.id)
would return the same result as the
page_counts
label, since both would count different columns of the same rows, which represent page views and not blog articles. Adding the
distinct()
method to the count eliminates the duplication and returns the correct count of articles:
>>> q = (select(
            OriginalBlogArticle,
            page_views,
            func.count(BlogArticle.id.distinct())
        )
        .join(BlogArticle.views)
        .join(OriginalBlogArticle, original_id == OriginalBlogArticle.id)
        .where(BlogView.timestamp.between(
            datetime(2022, 11, 1), datetime(2022, 12, 1)))
        .group_by(OriginalBlogArticle)
        .order_by(page_views.desc()))
>>> session.execute(q).all()
[(BlogArticle(171, "Our activity public responsibility represent"), 136, 4), ...,
(BlogArticle(201, "Exist they particular important note kitchen current"), 1, 1)]
Exercises
Do you want to practice with some more queries? Write queries that return:
Blog posts that have received more than 40 page views in March 2020.
Blog article with the largest number of translations. In case of a tie, the article that comes first alphabetically should be returned.
Page views in March 2022, categorized by language.
Page views by article, only considering content in German.
Monthly page views between January and December 2022.
Daily page views in February 2022.
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
