---
title: "SQLAlchemy 2 In Practice - Solutions to the Exercises"
url: "https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---solutions-to-the-exercises"
fetched_at: 2026-05-28T07:00:51.047313+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# SQLAlchemy 2 In Practice - Solutions to the Exercises

Source: https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---solutions-to-the-exercises

To conclude with my
SQLAlchemy 2 in Practice
series, this article contains the solutions to all the exercises. If you'd like to support my work, I encourage you to buy this book, either directly from
my store
or on
Amazon
. Thank you!
For your reference, here is a summary of the book contents:
Chapter 2
1. The first three products in alphabetical order built in the year 1983.
>>> q = (select(Product)
        .where(Product.year == 1983)
        .order_by(Product.name)
        .limit(3))
>>> session.scalars(q).all()
[Product(17, "Apple IIe"), Product(85, "Aquarius"), Product(26, "Atari 1200XL")]
2. Products that use the "Z80" CPU or any of its clones. Assume that all products based on this CPU have the word "Z80" in the
cpu
column.
>>> q = (select(Product)
        .where(Product.cpu.like('%Z80%')))
>>> session.scalars(q).all()
[ ... 63 results ... ]
3. Products that use either the "Z80" or the "6502" CPUs, or any of its clones, built before 1990, sorted alphabetically by name.
>>> q = (select(Product)
        .where(
            or_(Product.cpu.like('%Z80%'), Product.cpu.like('%6502%')),
            Product.year < 1990)
        .order_by(Product.name))
>>> session.scalars(q).all()
[ ... 90 results ... ]
4. The manufacturers that built products in the 1980s.
>>> q = (select(Product.manufacturer)
        .where(Product.year.between(1980, 1989))
        .distinct())
>>> session.scalars(q).all()
[ ... 65 results ... ]
5. Manufacturers whose names start with the letter "T", sorted alphabetically.
>>> q = (select(Product.manufacturer)
        .where(Product.manufacturer.like('T%'))
        .order_by(Product.manufacturer)
        .distinct())
>>> session.scalars(q).all()
['Tangerine Computer Systems', 'Technosys', 'Tesla', 'Texas Instruments',
'Thomson', 'Timex Sinclair', 'Tomy', 'Tsinghua University']
6. The first and last years in which products have been built in Croatia, along with the number of products built.
>>> q = select(
        func.min(Product.year), func.max(Product.year),
        func.count(Product.id)
    ).where(Product.country == 'Croatia')
>>> session.execute(q).first()
(1981, 1984, 4)
7. The number of products that were built each year. The results should start from the year with the most products, to the year with the least. Years in which no products were built do not need to be included.
>>> product_count = func.count(Product.id).label(None)
>>> q = (select(Product.year, product_count)
        .group_by(Product.year)
        .order_by(product_count.desc()))
>>> session.execute(q).all()
[(1983, 24), (1984, 21), (1985, 21), (1982, 17), (1986, 11), (1980, 10),
(1979, 9), (1977, 7), (1987, 6), (1981, 6), (1990, 5), (1989, 4), (1988, 2),
(1978, 2), (1969, 1), (1995, 1), (1992, 1), (1991, 1)]
8. The number of manufacturers in the United States (note that the
country
field for these products is set to
USA
)
>>> q = (select(func.count(Product.manufacturer.distinct()))
        .where(Product.country == 'USA'))
>>> session.scalar(q)
17
Chapter 3
1. The list of products made by IBM and Texas Instruments.
>>> q = (select(Product)
        .join(Product.manufacturer)
        .where(or_(
            Manufacturer.name == 'IBM',
            Manufacturer.name == 'Texas Instruments')))
>>> session.scalars(q).all()
[Product(75, "PCjr"), Product(76, "IBM PS/1"), Product(132, "TI-99/4"),
Product(133, "TI-99/4A")]
Another solution using the
in_()
operator on the column:
>>> q = (select(Product)
        .join(Product.manufacturer)
        .where(Manufacturer.name.in_(['IBM', 'Texas Instruments'])))
2. Manufacturers that operate in Brazil.
>>> q = (select(Manufacturer)
        .join(Manufacturer.products)
        .where(Product.country == 'Brazil')
        .distinct())
>>> session.scalars(q).all()
[Manufacturer(32, "Gradiente"), Manufacturer(46, "Comércio de Componentes Eletrônicos"),
Manufacturer(47, "Microdigital Eletronica"), Manufacturer(59, "Prológica")]
Another solution using
group_by()
instead of
distinct()
:
>>> q = (select(Manufacturer)
        .join(Manufacturer.products)
        .where(Product.country == 'Brazil')
        .group_by(Manufacturer))
3. Products that have a manufacturer that has the word "Research" in their name.
>>> q = (select(Product)
        .join(Product.manufacturer)
        .where(Manufacturer.name.like('%Research%')))
>>> session.scalars(q).all()
[Product(125, "ZX80"), Product(126, "ZX81"), Product(127, "ZX Spectrum"),
Product(128, "Sinclair QL")]
4. Manufacturers that made products based on the Z80 CPU or any of its clones.
>>> q = (select(Manufacturer)
        .join(Manufacturer.products)
        .where(Product.cpu.like('%Z80%'))
        .distinct())
>>> session.scalars(q).all()
[ ... 39 results ... ]
5. Manufacturers that made products that are not based on the 6502 CPU or any of its clones.
>>> q = (select(Manufacturer)
        .join(Manufacturer.products)
        .where(not_(Product.cpu.like('%8502%')))
        .distinct())
>>> session.scalars(q).all()
[ ... 76 results ... ]
6. Manufacturers and the year they went to market with their first product, sorted by the year.
>>> first_year = func.min(Product.year).label(None)
>>> q = (select(Manufacturer, first_year)
        .join(Manufacturer.products)
        .group_by(Manufacturer)
        .order_by(first_year))
>>> session.execute(q).all()
[ ... 76 results ... ]
7. Manufacturers that have 3 to 5 products in the catalog.
>>> q = (select(Manufacturer)
        .join(Manufacturer.products)
        .group_by(Manufacturer)
        .having(func.count(Product.id).between(3, 5)))
>>> session.scalars(q).all()
[Manufacturer(54, "Tangerine Computer Systems"), Manufacturer(63, "Sinclair Research"),
Manufacturer(60, "VEB Robotron"), Manufacturer(62, "Sharp"),
Manufacturer(44, "Memotech"), Manufacturer(9, "Atari Corporation"),
Manufacturer(57, "Pravetz"), Manufacturer(20, "Didaktik"), Manufacturer(56, "Philips")]
8. Manufacturers that operated for more than 5 years.
>>> q = (select(Manufacturer)
        .join(Manufacturer.products)
        .group_by(Manufacturer)
        .having(func.max(Product.year) - func.min(Product.year) > 5))
>>> session.scalars(q).all()
[Manufacturer(34, "IBM"), Manufacturer(52, "Radio Shack"),
Manufacturer(14, "Commodore"), Manufacturer(2, "Amstrad"), Manufacturer(62, "Sharp"),
Manufacturer(9, "Atari Corporation"), Manufacturer(30, "Fujitsu"),
Manufacturer(1, "Acorn Computers Ltd"), Manufacturer(5, "Apple Computer"),
Manufacturer(8, "Atari, Inc.")]
Chapter 4
1. Products that were made in UK or USA.
>>> q = (select(Product)
        .join(Product.countries)
        .where(Country.name.in_(['UK', 'USA']))
        .distinct())
Note: The
distinct()
clause is needed in this query to eliminate duplicates for products made jointly by the two countries.
2. Products not made in UK or USA. Products that were made in UK and/or USA jointly with other countries should be included in the query results.
>>> q = (select(Product)
        .join(Product.countries)
        .where(not_(Country.name.in_(['UK', 'USA'])))
        .distinct())
>>> session.scalars(q).all()
[ ... 70 results ... ]
An alternative solution without the
in_()
operator:
>>> q = (select(Product)
        .join(Product.countries)
        .where(Country.name != 'UK', Country.name != 'USA')
        .distinct())
3. Countries with products based on the Z80 CPU or any of its clones.
>>> q = (select(Country)
        .join(Country.products)
        .where(Product.cpu.like('%Z80%'))
        .distinct())
>>> session.scalars(q).all()
[Country(11, "Japan"), Country(12, "Brazil"), Country(7, "Belgium"),
Country(24, "Hungary"), Country(16, "Australia"), Country(4, "Netherlands"),
Country(1, "UK"), Country(3, "USA"), Country(25, "Norway"),
Country(21, "East Germany"), Country(5, "Romania"), Country(22, "Portugal"),
Country(6, "Hong Kong"), Country(9, "USSR"), Country(14, "Sweden"),
Country(8, "Czechoslovakia"), Country(23, "Poland")]
4. Countries that had products made in the 1970s in alphabetical order.
>>> q = (select(Country)
        .join(Country.products)
        .where(Product.year.between(1970, 1979))
        .order_by(Country.name)
        .distinct())
>>> session.scalars(q).all()
[Country(11, "Japan"), Country(14, "Sweden"), Country(3, "USA")]
5. The 5 countries with the most products. If there is a tie, the query should select countries in alphabetical order.
>>> product_count = func.count(Product.id).label(None)
>>> q = (select(Country, product_count)
        .join(Country.products)
        .group_by(Country)
        .order_by(product_count.desc(), Country.name)
        .limit(5))
>>> session.execute(q).all()
[(Country(3, "USA"), 51), (Country(1, "UK"), 36), (Country(11, "Japan"), 12),
(Country(6, "Hong Kong"), 6), (Country(22, "Portugal"), 6)]
6. Manufacturers that have more than 3 products in UK or USA.
>>> product_count = func.count(Product.id.distinct()).label(None)
>>> q = (select(Manufacturer, product_count)
        .join(Manufacturer.products)
        .join(Product.countries)
        .where(Country.name.in_(['UK', 'USA']))
        .group_by(Manufacturer)
        .having(product_count > 3))
>>> session.execute(q).all()
[(Manufacturer(1, "Acorn Computers Ltd"), 6), (Manufacturer(2, "Amstrad"), 7),
(Manufacturer(5, "Apple Computer"), 6), (Manufacturer(8, "Atari, Inc."), 7),
(Manufacturer(14, "Commodore"), 10), (Manufacturer(52, "Radio Shack"), 6),
(Manufacturer(63, "Sinclair Research"), 4), (Manufacturer(70, "Timex Sinclair"), 4)]
7. Manufacturers that have products in more than one country.
>>> country_count = func.count(Country.id.distinct()).label(None)
>>> q = (select(Manufacturer, country_count)
        .join(Manufacturer.products)
        .join(Product.countries)
        .group_by(Manufacturer)
        .having(country_count > 1))
>>> session.execute(q).all()
[(Manufacturer(70, "Timex Sinclair"), 4)]
8. Products made jointly in UK and USA.
>>> q = (select(Product)
        .join(Product.countries)
        .where(Country.name.in_(['UK', 'USA']))
        .group_by(Product)
        .having(func.count(Country.id) > 1))
>>> session.execute(q).all()
[(Product(138, "Timex Sinclair 1000"),), (Product(139, "Timex Sinclair 1500"),),
(Product(140, "Timex Sinclair 2048"),), (Product(142, "Timex Computer 2068"),)]
Note: the trick that makes this query work is that the
where()
clause filters any products not made in the two countries of interest, so after grouping by product any product with a row count of two must have been linked to both countries.
Chapter 5
1. Orders above $300 in descending ordered by the sale amount from highest to lowest.
order_total = func.sum(OrderItem.unit_price * OrderItem.quantity).label(None)
q = (select(Order, order_total)
        .join(Order.order_items)
        .group_by(Order)
        .having(order_total > 300)
        .order_by(order_total.desc()))
>>> session.execute(q).all()
[ ... 50 results ... ]
2. Orders that include one or more ZX81 computers.
q = (select(Order)
        .join(Order.order_items)
        .join(OrderItem.product)
        .where(Product.name == 'ZX81'))
>>> session.scalars(q).all()
[ ... 3 results ... ]
A possibly more efficient solution with two queries, but one less join:
>>> zx81 = session.scalar(
        select(Product)
            .where(Product.name == 'ZX81'))
>>> q = (select(Order)
        .join(Order.order_items)
        .where(OrderItem.product == zx81))
3. Orders that include a product made by Amstrad.
>>> q = (select(Order)
        .join(Order.order_items)
        .join(OrderItem.product)
        .join(Product.manufacturer)
        .where(Manufacturer.name == 'Amstrad')
        .distinct())
>>> session.scalars(q).all()
[ ... 30 results ... ]
An alternative version with one less join:
>>> amstrad = session.scalar(
        select(Manufacturer)
            .where(Manufacturer.name == 'Amstrad'))
>>> q = (select(Order)
        .join(Order.order_items)
        .join(OrderItem.product)
        .where(Product.manufacturer == amstrad)
        .distinct())
Note:
distinct()
is necessary here to remove duplicates from orders that have two or more line items with products by this manufacturer.
4. Orders made on the 25th of December 2022 with two or more line items.
>>> q = (select(Order)
        .join(Order.order_items)
        .where(Order.timestamp.between(
            datetime(2022, 12, 25), datetime(2022, 12, 26)))
        .group_by(Order)
        .having(func.count(Order.id) >= 2))
>>> session.scalars(q).all()
[ ... 4 results ... ]
Note that technically the above query will also pick up orders made on the 26th of December at exactly 00:00:00.0, because the
between()
operator is inclusive of the start and end values. A more accurate (and lengthy) query can be built using the
extract()
function:
>>> q = (select(Order)
        .join(Order.order_items)
        .where(
            func.extract('day', Order.timestamp) == 25,
            func.extract('month', Order.timestamp) == 12,
            func.extract('year', Order.timestamp) == 2022)
        .group_by(Order)
        .having(func.count(Order.id) >= 2))
>>> session.scalars(q).all()
5. Customers with their first and last order date and time. Hint: the
min()
and
max()
functions can help with this query.
>>> q = (select(Customer, func.min(Order.timestamp), func.max(Order.timestamp))
        .join(Customer.orders)
        .group_by(Customer))
>>> session.execute(q).all()
[ ... 2754 results ... ]
6. The top 5 manufacturers that had the most sale amounts, sorted by those amounts in descending order.
>>> order_total = func.sum(OrderItem.unit_price * OrderItem.quantity).label(None)
>>> q = (select(Manufacturer, order_total)
        .join(Manufacturer.products)
        .join(Product.order_items)
        .group_by(Manufacturer)
        .order_by(order_total.desc())
        .limit(5))
>>> session.execute(q).all()
[(Manufacturer(14, "Commodore"), 281666.6599999996),
(Manufacturer(63, "Sinclair Research"), 122582.61999999928),
(Manufacturer(5, "Apple Computer"), 34169.33000000025),
(Manufacturer(1, "Acorn Computers Ltd"), 14018.28000000003),
(Manufacturer(8, "Atari, Inc."), 3154.7399999999984)]
7. Products, their average star rating and their review count, sorted by review count in descending order.
>>> product_rating = func.avg(ProductReview.rating).label(None)
>>> review_count = func.count(ProductReview.rating).label(None)
>>> q = (select(Product, product_rating, review_count)
        .join(Product.reviews)
        .group_by(Product)
        .order_by(review_count.desc()))
>>> session.execute(q).all()
[ ... 125 results ... ]
The solution above does not include products that do not have reviews. To include the missing products, the join must be upgraded to a left outer join:
>>> q = (select(Product, product_rating, review_count)
        .join(Product.reviews, isouter=True)
        .group_by(Product)
        .order_by(review_count.desc()))
>>> session.execute(q).all()
[ ... 149 results ... ]
8. Products and their average star rating, but only counting reviews that include a written comment.
>>> product_rating = func.avg(ProductReview.rating).label(None)
>>> q = (select(Product, product_rating)
        .join(Product.reviews)
        .where(ProductReview.comment != None)
        .group_by(Product))
>>> session.execute(q).all()
[ ... 70 results ... ]
9. Average star reviews for the Commodore 64 computer in each month of 2022.
>>> month = func.extract('month', ProductReview.timestamp).label(None)
>>> year = func.extract('year', ProductReview.timestamp).label(None)
>>> product_rating = func.avg(ProductReview.rating).label(None)
>>> q = (select(year, month, product_rating)
        .join(ProductReview.product)
        .where(Product.name == 'Commodore 64')
        .group_by(year, month)
        .order_by(year, month))
>>> session.execute(q).all()
[(2022, 1, 4.294117647058823), (2022, 2, 3.6551724137931036),
(2022, 3, 3.4375), (2022, 4, 3.975609756097561), (2022, 5, 3.317073170731707),
(2022, 6, 3.6774193548387095), (2022, 7, 3.606060606060606),
(2022, 8, 3.973684210526316), (2022, 9, 3.6666666666666665), (2022, 10, 3.9375),
(2022, 11, 3.8958333333333335), (2022, 12, 3.6)]
As in previous exercises, the join can be removed when the product is grabbed in advance:
>>> c64 = session.scalar(select(Product).where(Product.name == 'Commodore 64'))
>>> q = (select(year, month, product_rating)
        .where(ProductReview.product == c64)
        .group_by(year, month)
        .order_by(year, month))
10. Customers with the minimum and maximum star rating they gave to a product, sorted alphabetically by customer name.
>>> min_rating = func.min(ProductReview.rating).label(None)
>>> max_rating = func.max(ProductReview.rating).label(None)
>>> q = (select(Customer, min_rating, max_rating)
        .join(Customer.product_reviews)
        .group_by(Customer)
        .order_by(Customer.name))
>>> session.execute(q).all()
[ ... 931 results ... ]
11. Manufacturers with their average star rating, sorted from highest to lowest rating.
>>> product_rating = func.avg(ProductReview.rating).label(None)
>>> q = (select(Manufacturer, product_rating)
        .join(Manufacturer.products)
        .join(Product.reviews)
        .group_by(Manufacturer)
        .order_by(product_rating.desc()))
>>> session.execute(q).all()
[ ... 68 results ... ]
The above solution only reports manufacturers that have at least one product rated. To include manufacturers without any rated products, the joins must be upgraded to left outer:
>>> q = (select(Manufacturer, product_rating)
        .join(Manufacturer.products, isouter=True)
        .join(Product.reviews, isouter=True)
        .group_by(Manufacturer)
        .order_by(product_rating.desc()))
>>> session.execute(q).all()
[ ... 76 results ... ]
12. Product countries with their average star rating, sorted from highest to lowest rating.
>>> product_rating = func.avg(ProductReview.rating).label(None)
>>> q = (select(Country, product_rating)
        .join(Country.products)
        .join(Product.reviews)
        .group_by(Country)
        .order_by(product_rating.desc()))
>>> session.execute(q).all()
[ ... 23 results ... ]
As above, only countries with at least one rated product will be included. To add countries with no ratings, left outer joins must be used:
>>> q = (select(Country, product_rating)
        .join(Country.products, isouter=True)
        .join(Product.reviews, isouter=True)
        .group_by(Country)
        .order_by(product_rating.desc()))
>>> session.execute(q).all()
[ ... 25 results ... ]
Chapter 6
1. Blog posts that have received more than 40 page views in March 2020.
>>> q = (select(BlogArticle)
        .join(BlogArticle.views)
        .where(BlogView.timestamp.between(
            datetime(2020, 3, 1), datetime(2020, 4, 1)))
        .group_by(BlogArticle)
        .having(func.count(BlogView.id) > 50))
>>> session.execute(q).all()
[(BlogArticle(143, "Evening however issue"),)]
2. Blog article with the largest number of translations. In case of a tie, the article that comes first alphabetically should be returned.
>>> TranslatedBlogArticle = aliased(BlogArticle)
>>> q = (select(BlogArticle  , func.count(BlogArticle.id))
        .join(TranslatedBlogArticle.translation_of)
        .group_by(BlogArticle)
        .order_by(func.count(BlogArticle.id).desc(), BlogArticle.title)
        .limit(1))
>>> session.scalar(q)
BlogArticle(63, "Business seven ability cup church similar itself")
3. Page views in March 2022, categorized by language.
>>> page_views = func.count(BlogView.id).label(None)
>>> q = (select(Language, page_views)
        .join(Language.blog_articles)
        .join(BlogArticle.views)
        .where(BlogView.timestamp.between(
            datetime(2022, 3, 1), datetime(2022, 4, 1)))
        .group_by(Language)
        .order_by(page_views.desc()))
>>> session.execute(q).all()
[(Language(1, "English"), 2155), (Language(3, "French"), 512),
(Language(2, "German"), 417), (Language(6, "Portuguese"), 404),
(Language(5, "Spanish"), 305), (Language(4, "Italian"), 283)]
4. Page views by article, only considering content in German.
>>> page_views = func.count(BlogView.id).label(None)
>>> q = (select(BlogArticle, page_views)
        .join(BlogArticle.views)
        .join(BlogArticle.language)
        .where(Language.name == 'German')
        .group_by(BlogArticle)
        .order_by(page_views.desc()))
>>> session.execute(q).all()
[ ... 21 results ... ]
5. Monthly page views between January and December 2022.
>>> month = func.extract('month', BlogView.timestamp).label(None)
>>> year = func.extract('year', BlogView.timestamp).label(None)
>>> page_views = func.count(BlogView.id).label(None)
>>> q = (select(year, month, page_views)
        .where(BlogView.timestamp.between(
            datetime(2022, 1, 1), datetime(2023, 1, 1)))
        .group_by(year, month)
        .order_by(year, month))
>>> session.execute(q).all()
[(2022, 1, 3649), (2022, 2, 3287), (2022, 3, 4076), (2022, 4, 3820),
(2022, 5, 4034), (2022, 6, 3659), (2022, 7, 3900), (2022, 8, 3705),
(2022, 9, 3639), (2022, 10, 4066), (2022, 11, 4034), (2022, 12, 3925)]
6. Daily page views in February 2022.
>>> day = func.extract('day', BlogView.timestamp).label(None)
>>> month = func.extract('month', BlogView.timestamp).label(None)
>>> year = func.extract('year', BlogView.timestamp).label(None)
>>> page_views = func.count(BlogView.id).label(None)
>>> q = (select(year, month, day, page_views)
        .where(BlogView.timestamp.between(
            datetime(2022, 2, 1), datetime(2022, 3, 1)))
        .group_by(year, month, day)
        .order_by(year, month, day))
>>> session.execute(q).all()
[ ... 28 results ... ]
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
