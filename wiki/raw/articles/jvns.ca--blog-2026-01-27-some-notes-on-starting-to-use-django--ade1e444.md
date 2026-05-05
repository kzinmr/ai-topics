---
title: "Some notes on starting to use Django"
url: "https://jvns.ca/blog/2026/01/27/some-notes-on-starting-to-use-django/"
fetched_at: 2026-05-05T07:01:46.426179+00:00
source: "Julia Evans (jvns)"
tags: [blog, raw]
---

# Some notes on starting to use Django

Source: https://jvns.ca/blog/2026/01/27/some-notes-on-starting-to-use-django/

Hello! One of my favourite things is starting to learn an
Old Boring Technology that I’ve never tried before but that has been around for
20+ years. It feels really good when every problem I’m ever going to have has
been solved already 1000 times and I can just get stuff done easily.
I’ve thought it would be cool to learn a popular web framework like
Rails or Django or Laravel for a long time, but I’d never really managed to
make it happen. But I started learning Django to make a website a few months
back, I’ve been liking it so far, and here are a few quick notes!
I spent some time
trying to learn Rails
in 2020,
and while it was cool and I really wanted to like Rails (the Ruby community is great!),
I found that if I left my Rails project alone for months, when I came
back to it it was hard for me to remember how to get anything done because
(for example) if it says
resources :topics
in your
routes.rb
, on its own
that doesn’t tell you where the
topics
routes are configured, you need to
remember or look up the convention.
Being able to abandon a project for months or years and then come back to it is
really important to me (that’s how all my projects work!), and Django feels easier
to me because things are more explicit.
In my small Django project it feels like I just have 5 main files (other
than the settings files):
urls.py
,
models.py
,
views.py
,
admin.py
, and
tests.py
, and if I want to know where something else is (like an HTML template)
is then it’s usually explicitly referenced from one of those files.
For this project I wanted to have an admin interface to manually edit or view
some of the data in the database. Django has a really nice built-in admin
interface, and I can customize it with just a little bit of code.
For example, here’s part of one of my admin classes, which sets up which fields
to display in the “list” view,  which field to search on, and how to order them
by default.
@admin.register(Zine)
class ZineAdmin(admin.ModelAdmin):
    list_display = ["name", "publication_date", "free", "slug", "image_preview"]
    search_fields = ["name", "slug"]
    readonly_fields = ["image_preview"]
    ordering = ["-publication_date"]
In the past my attitude has been “ORMs? Who needs them? I can just write my own SQL queries!”.
I’ve been enjoying Django’s ORM so far though, and I think it’s cool how Django
uses
__
to represent a
JOIN
, like this:
Zine.objects
    .exclude(product__order__email_hash=email_hash)
This query involves 5 tables:
zines
,
zine_products
,
products
,
order_products
, and
orders
.
To make this work I just had to tell Django that there’s a
ManyToManyField
relating “orders” and “products”, and another
ManyToManyField
relating
“zines”, and “products”, so that it knows how to connect
zines
,
orders
,
products
.
I definitely
could
write that query, but writing
product__order__email_hash
is
a lot less typing, it feels a lot easier to read, and honestly I think it would
take me a little while to figure out how to construct the query
(which needs to do a few other things than just those joins).
I have zero concern about the performance of my ORM-generated queries so I’m
pretty excited about ORMs for now, though I’m sure I’ll find things to be
frustrated with eventually.
The other great thing about the ORM is migrations!
If I add, delete, or change a field in
models.py
, Django will automatically
generate a migration script like
migrations/0006_delete_imageblob.py
.
I assume that I could edit those scripts if I wanted, but so far I’ve just
been running the generated scripts with no change and it’s been going great. It
really feels like magic.
I’m realizing that being able to do migrations easily is important for me right
now because I’m changing my data model fairly often as I figure out how I want
it to work.
I had a bad habit of
never reading the documentation
but I’ve been really enjoying the parts of Django’s docs that I’ve read so far.
This isn’t by accident: Jacob Kaplan-Moss has a
talk from PyCon 2011
on Django’s documentation culture.
For example the
intro to models
lists the most important common fields you might want to set when using the ORM.
After having a bad experience trying to operate Postgres and not being able to
understand what was going on, I decided to run all of my small websites with
SQLite instead. It’s been going way better, and I love being able to backup by
just doing a
VACUUM INTO
and then copying the resulting single file.
I’ve been following
these instructions
for using SQLite with Django in production.
I think it should be fine because I’m expecting the site to have a few hundred
writes per day at most, much less than
Mess with DNS
which has a lot more of writes and has been working well (though the writes are
split across 3 different SQLite databases).
Django seems to be very “batteries-included”, which I love – if I want CSRF
protection, or a
Content-Security-Policy
, or I want to send email, it’s all
in there!
For example, I wanted to save the emails Django sends to a file in dev mode (so
that it didn’t send real email to real people), which was just a little bit
of configuration.
I just put this
settings/dev.py
:
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "emails"
and then set up the production email like this in
settings/production.py
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.whatever.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "xxxx"
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_API_KEY')
That made me feel like if I want some other basic website feature, there’s
likely to be an easy way to do it built into Django already.
I’m still a bit intimidated by the
settings.py
file: Django’s settings system
works by setting a bunch of global variables in a file, and I feel a bit
stressed about… what if I make a typo in the name of one of those variables?
How will I know? What if I type
WSGI_APPLICATOIN = "config.wsgi.application"
instead of
WSGI_APPLICATION
?
I guess I’ve gotten used to having a Python language server tell me when I’ve
made a typo and so now it feels a bit disorienting when I can’t rely on the
language server support.
I haven’t really successfully used an actual web framework for a project before
(right now almost all of my websites are either a single Go binary or static
sites), so I’m interested in seeing how it goes!
There’s still lots for me to learn about, I still haven’t really gotten into
Django’s form validation tooling or authentication systems.
Thanks to Marco Rogers for convincing me to give ORMs a chance.
(we’re still experimenting with the comments-on-Mastodon system!
Here are the comments on Mastodon
! tell me your favourite Django feature!)
