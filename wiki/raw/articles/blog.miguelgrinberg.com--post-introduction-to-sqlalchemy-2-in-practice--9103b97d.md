---
title: "Introduction to SQLAlchemy 2 In Practice"
url: "https://blog.miguelgrinberg.com/post/introduction-to-sqlalchemy-2-in-practice"
fetched_at: 2026-04-30T07:01:20.615713+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# Introduction to SQLAlchemy 2 In Practice

Source: https://blog.miguelgrinberg.com/post/introduction-to-sqlalchemy-2-in-practice

In 2023 I wrote "
SQLAlchemy 2 In Practice
", a book in which I offer an in-depth look at
SQLAlchemy version 2
, still the current version today. SQLAlchemy is, for those who don't know, the most popular database library and Object-Request Mapper (ORM) for Python.
I have a tradition of publishing my books on this blog to read for free, but this is one that I never managed to bring here, and starting today I'm going to work on correcting that. This article includes the Preface of the book. If you are interested, keep an eye out on this blog over the next few weeks, as I will be publishing the eight chapters of the book in order. If you can't wait for the installments, you can
buy the book
in electronic or paper format today, and I will be eternally thankful, as you will be directly supporting my work.
For your reference, here is a summary of the book contents:
Preface to "SQLAlchemy 2 In Practice" (written in 2023)
It was almost eleven years ago in 2012 that I started to write the Flask Mega-Tutorial. Initially published as a collection of blog articles over a period of a year, and later revised into an e-book and a video course, this work allowed an uncountable number of developers to take their first steps into the fascinating world of web development. If I'd ask you to guess which chapter in this tutorial is the most visited on my blog, you'd likely guess correctly that it is Chapter One. But could you guess which chapter is the second-most popular?
Interestingly, the second most-read chapter of the Flask Mega-Tutorial isn't Chapter Two. It is Chapter Four, which includes an introduction to databases and the SQLAlchemy library. If you browse through the hundreds of questions that people have left on my blog for this chapter, you'll realize that there is a common theme. Many of the questions are from developers that need to know how to do something a little more complex than what I present in the article, but are unable to figure out how to do it on their own. Over the years I have written standalone articles about some of the most asked database questions, but with such a vast topic, database questions have never stopped coming.
The book you are now reading is my attempt to address the large database knowledge gap that many developers have. I'm going to follow a similar approach to that of the Flask Mega-Tutorial, in that I will take you on a journey in which you will develop a real-world project that starts small and then evolves and gets more complex as you make progress through the chapters. The difference with the Flask Mega-Tutorial is that in this book the goal is not to create a complete web application but to build a flexible, efficient, real-world relational database, along with its associated processes and scripting, and with a focus on creating efficient queries and reports.
Because SQLAlchemy is an extensive framework with lots of options and ways of doing things, you should not expect this book to teach you every feature and every available trick. While I have made an effort to cover a wide variety of use cases, you should also become familiar with the SQLAlchemy official documentation, which is the ultimate reference from where you can pick up more ideas and techniques. My hope is that after working through this book you will be better prepared to navigate the official documentation and continue your learning process.
In this book you will learn how to work with relational databases in a way that is generic and apt to be applied to any web application framework, or to other types of applications not related to the web. You will even be able to incorporate what you learn in this book into modern asynchronous applications based on the
asyncio
package, such as those you can build with the FastAPI framework.
What You Will Build
The project that you will work on with the help of this book has the goal of supporting many of the aspects of the operation of a fictional vintage home computer store that I'm going to call RetroFun.
RetroFun offers an impressive collection of home computers from the 1980s and 1990s for sale. In this book you will learn how to build some database operations for this made-up company, including:
Maintaining a list of products categorized by several attributes such as year of release, manufacturer, country of origin or CPU.
Keeping track of customers and their orders.
Maintaining star ratings and reviews made by customers.
Tracking page views for articles published on the company's blog.
Generating a lot of reports, both simple and complex, always keeping an eye towards efficiency and performance.
Prerequisites
You should be aware that this isn't a book for the complete beginner. To make the most out of it you should have some previous experience writing Python, and ideally also some basic relational database knowledge. If you have learned to work with databases with my
Flask Mega-Tutorial
, or with any other introductory Python course, you should be at the right level.
I recommend that you don't just read this book, but also work on all the exercises along with me. For this you will need a recent Python interpreter installed on your computer, and a text editor or IDE in which you feel comfortable writing Python code. Basic knowledge of the terminal or command prompt in your operating system would also help.
How To Work With The Example Code
You are encouraged to write and try all the code examples as you read this book. The code has been thoroughly tested using SQLAlchemy 2.0 on the three major open-source databases:
Other databases are likely to work as well, as long as SQLAlchemy has support for them.
The code from this book should work with SQLAlchemy 1.4 with relatively minor changes, but the effort to back port the book examples is left to the reader. Support for SQLAlchemy versions 1.3 and older was not taken into consideration.
I have released the complete source code for this book on a
GitHub repository
. In addition to source code, this repository contains data files that can be used to populate the database you will build. At the appropriate times you will be given instructions on how to use these data files.
Conventions Used In This Book
This book frequently includes commands that you need to type in a terminal session. For these commands, a
$
will be shown as a command prompt. This is a standard prompt for many Linux shells, but may look unfamiliar to Microsoft Windows users. For example:
$ python hello.py
hello
In a lot of the terminal examples, you are going to be required to have an activated
virtual environment
(do not worry if you don't know or remember what this is, you will find out very soon!). For those examples, the prompt will appear as
(venv) $
:
(venv) $ pip install sqlalchemy
You will also need to interact with the Python REPL, or interactive prompt. Examples that show statements that need to be entered in a Python interpreter session will use a
>>>
prompt, as in the following example:
>>> print('hello!')
hello
In all cases, lines that are not prefixed with a
>>>
prompt are output printed by the command right above, and should not be typed.
Many of the statements that you will need to type in the REPL are database queries that are formed by a call to SQLAlchemy's
select()
function followed by an often long sequence of method calls. Here is an example of how these queries might look when typed in a single long line:
>>> q = select(select_expression).method1(expression1).method2(expression2)
These statements can be quite unreadable when shown as above, so the convention used in this book is to show them broken up into multiple lines as follows:
>>> q = (select(select_expression)
        .method1(expression1)
        .method2(expression2))
Note that to be able to break long lines on the periods as shown above, Python requires the entire expression to be enclosed in parentheses. You can collapse these multi-line statements into single-line when you type them in the REPL.
Acknowledgements
This book was inspired by many of the questions I have received over the years from readers of my Flask Mega-Tutorial, so I'm extremely thankful to them for engaging with me and sharing their problems and ideas. To them, I also owe the realization that Python database programming is an area that hasn't been well explored in technical literature or video content.
Writing a technical book is hard, especially when the book is structured as a tutorial with detailed steps that the reader is expected to follow. While I have put a lot of care and attention in creating this content so that readers can have a smooth experience as they move through the chapters, I relied on reviewers to alert me of mistakes and inconsistencies that I inadvertently introduced. I would like to recognize the work of Martin Bell, Rostislav Roznoshchik and my son Dylan Grinberg as technical reviewers.
Finally, I would like to thank Mike Bayer and Federico Caselli. Mike is the creator of SQLAlchemy and Alembic. He and Federico are the current maintainers, and both have been extremely helpful and patient with my questions. Their assistance gave me a greater understanding of the major changes that have been introduced in releases 1.4 and 2.0 of SQLAlchemy. Mike was also kind enough to review the draft of this book and has made some useful suggestions.
Proceed to
Chapter 1
.
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
