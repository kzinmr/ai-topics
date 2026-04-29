---
title: "SQLAlchemy 2 In Practice - Chapter 1 - Database Setup"
url: "https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-1---database-setup"
fetched_at: 2026-04-29T07:01:26.923700+00:00
source: "miguelgrinberg.com"
tags: [blog, raw]
---

# SQLAlchemy 2 In Practice - Chapter 1 - Database Setup

Source: https://blog.miguelgrinberg.com/post/sqlalchemy-2-in-practice---chapter-1---database-setup

Welcome! This is the start of a journey which I hope will provide you with many new tricks to improve how you work with relational databases in your Python applications. Given that this is a hands-on book, this first chapter is dedicated to help you set up your system with a database, so that you can run all the examples and exercises.
This is the first chapter of my
SQLAlchemy 2 in Practice
book. If you'd like to support my work, I encourage you to buy this book, either directly from
my store
or on
Amazon
. Thank you!
For your reference, here is a summary of the book contents:
Project Directory
Your first task is to create a project directory where you will store files associated with the project featured in this book.
Open a terminal or command prompt, find a suitable parent directory and create a directory there. Then change into that directory.
$ mkdir retrofun
$ cd retrofun
Note:
"RetroFun" is the name of the fictional company for which the database project featured in this book is for.
Python and SQLAlchemy Installation
As is standard in Python projects, you should create a Python
virtual environment
where all the dependencies can be installed. The command to do this is:
$ python -m venv venv
The
python -m venv
portion is what tells Python to create the virtual environment, by running the
venv
module that is part of the Python standard library. The second and final
venv
included in the command is the name I have chosen for the virtual environment. You are welcome to use a different name if you prefer.
After this command completes, your project will have a subdirectory named
venv
, containing a private copy of your Python interpreter.
Whenever you are ready to start working on this project, you have to tell your terminal session that you want to use the virtual environment. This action is called "activating" the virtual environment.
If you are using a UNIX based shell such as
bash
, regardless of operating system, the activation command is:
$ source venv/bin/activate
If you are using a Command Prompt on Microsoft Windows, the activation command is different:
$ venv\Scripts\activate
Finally, if you are using a PowerShell terminal the following is the activation command:
$ venv\Scripts\activate.ps1
Regardless of the activation command that you use, your shell prompt should change to indicate that the virtual environment has been activated. The prompt should look more or less as follows:
(venv) $ _
Note:
Virtual environment activations only affect the shell session in which they are issued. If you have multiple terminals open, the activation command must be given for each terminal session. Activations must be issued again after a computer reboot or restart.
You can now install
SQLAlchemy
in the virtual environment:
(venv) $ pip install sqlalchemy
Version 2.0 or newer of SQLAlchemy is required for the code featured in this book.
Database Choices
The code featured in this book is generic enough to be used with any relational database system supported by SQLAlchemy. The code examples have been tested against three popular open-source databases:
If you are interested in a particular database system, and it is not in the list above, then you should ensure that
SQLAlchemy supports it
, either through a built-in or a third-party integration.
If, on the other side, you have no particular preference, then my recommendation is that you start with SQLite, which is by far the easiest to set up and manage. Since the code uses common features present in all the database systems, you can switch to a different database when and if needed.
Have you made a decision? Now it is time to create a brand-new database for use with this book. If you have your preferred set of tools to do this you are welcome to use them, but in case you need some guidance, the sections that follow offer step-by-step instructions for the three databases listed above.
SQLite Database Installation
SQLite is a C-language library that implements a small, fast and self-contained relational database engine. This database is particularly interesting because it does not require a separate server process to run.
The SQLite library is bundled with the Python interpreter, so support for this database is available to use in Python and SQLAlchemy without installing any additional software or performing any configuration.
If you would like to have a tool that you can use to inspect and manage SQLite databases outside of Python and SQLAlchemy, you can download the
sqlite3
command-line shell for your operating system from the official
SQLite download page
.
MySQL Database Set Up
MySQL is an open-source relational database owned by Oracle Corporation. Unlike SQLite, this database includes server and client components, both of which need to be installed.
MySQL Server
If you have access to a running MySQL server, then you can just create a new database and database user and skip to the client section below. The installation instructions in this section demonstrate how to install a server along with the popular
phpMyAdmin
management application.
If you don't already have access to a MySQL installation, the easiest way to get one up and running is to use Docker. If you would like to follow the instructions below to install MySQL, first install
Docker Desktop
.
Copy the following definitions to a file named
docker-compose.yml
in your project directory:
version: '3'

services:
  db:
    image: mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: changethis!
    ports:
      - "3306:3306"
    volumes:
      - db-data:/var/lib/mysql
  admin:
    image: phpmyadmin
    restart: always
    environment:
      - PMA_ARBITRARY=1
    ports:
      - 8080:80
volumes:
  db-data:
This Docker Compose configuration file starts a service called
db
that runs a MySQL server connected to port 3306 of your computer, plus a second service called
admin
that runs phpMyAdmin on port 8080. The database storage is configured on a separate volume called
db-data
, to make it possible to upgrade the database container without losing data.
Note the
MYSQL_ROOT_PASSWORD
line, which has the value
changethis!
. This line defines the administrator password for the MySQL server. Edit this line to set a secure password of your liking.
Once you have this file saved in your project directory, return to the terminal and run the following command to start your MySQL server:
$ docker-compose up -d
The first time you run this command it will take a while, as Docker has to download the MySQL and phpMyAdmin container images from the Docker Hub repository. Once the images are downloaded, it should take a few seconds for the containers to be launched, and at that point MySQL should be deployed on your computer and ready to be used.
You can open the phpMyAdmin database management tool by typing
http://localhost:8080
in the address bar of your web browser.
To log in, enter the following credentials:
Server:
db
Username:
root
Password: the root password that you entered in the
docker-compose.yml
file
Once you access the phpMyAdmin interface, click on the "Databases" tab. Near the top you should see the "Create Database" section.
Enter a name for the new database, such as
retrofun
and click the "Create" button.
A good practice when creating a new database is to also define a user specifically assigned to it. Using the root database user for day-to-day operations is too risky, because this account is too powerful and should only be used for important administration tasks.
Click on the "Privileges" tab for the new database. Near the bottom of the page there is a section titled "New" with an "Add user account" link. Click it to create a new user.
For the username you can choose any name that you like, but a naming convention that I find useful is to use the same name for the database and the user, so in this case it would be
retrofun
. Leave the host set to "%", then enter a password for the new user.
Confirm that the "Grant all privileges on database retrofun" option is enabled, and then scroll all the way to the bottom of the page and click the "Go" button to create the user. This user will have full access to the database, but it will not be able to access or create other databases, which is a good security principle to follow.
From now on, you can log in to phpMyAdmin using the user you just created, and your view of the database server will be constrained to only what's relevant to manage this particular database.
If you'd like to stop the MySQL server, you can do so with this command, issued from the directory in which you have your
docker-compose.yml
file:
$ docker-compose down
To start the server again, repeat the "up" command as before:
$ docker-compose up -d
Stopping and restarting the server as shown above does not cause any data loss.
MySQL Client
To access your MySQL database you have to install a Python client, sometimes also called driver. There are several
MySQL drivers for Python
that can be used here, so as before, you should use your favorite if you have one.
If you need a recommendation, my driver of choice is
pymysql
, which you can install into your Python virtual environment as follows:
(venv) $ pip install pymysql cryptography
The
cryptography
package installed above is an optional dependency of
pymysql
that is needed to perform authentication against the MySQL database.
Congratulations! You now have a complete set up, including a blank MySQL database that is ready to be used. If you followed the installation procedure described above, the connection settings for your database are:
Hostname:
localhost
(but use
db
as hostname to connect from the phpMyAdmin container)
Port: 3306
Database:
retrofun
Username:
retrofun
Password: the password that you selected for the user
Python driver:
pymysql
PostgreSQL Database Set Up
PostgreSQL (often shortened to Postgres) is yet another major open-source relational database system, similar to MySQL in the sense that it also requires separate server and client.
PostgreSQL Server
If you have access to a PostgreSQL server then you can create a database and user to use with this book and skip to the next section to set up your client.
This section provides instructions to install PostgreSQL in your computer, along with the
pgAdmin
administration application. These instructions are based on Docker containers, and are compatible with the three major operating systems. The easiest way to install Docker and Docker Compose on your computer is through
Docker Desktop
.
Copy the following Docker Compose configuration file to a file named
docker-compose.yml
in your project directory:
version: '3'

services:
  db:
    image: postgres
    restart: always
    environment:
      POSTGRES_PASSWORD: changethis!
    ports:
      - "5432:5432"
    volumes:
      - db-data:/var/lib/postgresql/data
  admin:
    image: dpage/pgadmin4
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@example.com
      PGADMIN_DEFAULT_PASSWORD: changethis!
    ports:
      - 8080:80
    volumes:
      - admin-data:/var/lib/pgadmin
volumes:
  db-data:
  admin-data:
This configuration file defines a service called
db
with the PostgreSQL server running on port 5432 of your computer, and a second service called
admin
that runs pgAdmin on port 8080. Both services require storage, so two volumes are also created for them. Using separate volumes for storage allows the data to persist if the containers are stopped and restarted.
There are three lines in the above configuration that need to be reviewed and edited:
Change
POSTGRES_PASSWORD
to the PostgreSQL administrator password of your liking.
Change
PGADMIN_DEFAULT_EMAIL
to your own email address (used only to log in).
Change
PGADMIN_DEFAULT_PASSWORD
to the pgAdmin administrator password of your liking.
Once you have the
docker-compose.yml
file ready, you can start the services with the following command:
$ docker-compose up -d
The first time you run this command Docker will have to download the Docker images for PostgreSQL and pgAdmin, so that may take a while. Once these images are downloaded, starting the services should take just a few seconds.
After the above command completes, give your computer a minute or two to get everything started and then connect to pgAdmin by typing
http://localhost:8080
on the address bar of your web browser.
You can log in to the administration interface with the email and password that you selected for the
PGADMIN_DEFAULT_EMAIL
and
PGADMIN_DEFAULT_PASSWORD
settings in your
docker-compose.yml
configuration file.
The first task is to tell pgAdmin about the PostgreSQL server. Click the "Add New Server" icon to do this. In the "General" tab, enter a name for the server such as
db
in the "Name" field.
Then in the "Connection" tab, set "Host name" to
db
, which is the name of the PostgreSQL service as defined in the Docker Compose configuration. Leave the "Port" and "Maintenance Database" settings with their default values. Change "Username" to
postgres
, and write the password that you entered for the
POSTGRES_PASSWORD
setting in the "Password" field. You can enable the "Save password?" option if you don't want to have to re-enter the password in the future.
After you click the "Save" button, pgAdmin will add the server to the left sidebar, and will start showing you live statistics about its operation.
The next step is to create a brand-new database that you can use to run the examples in this book. As with MySQL, it is a good practice to create a dedicated user for each database. To create the user, right-click on the
db
name in the sidebar and select "Create", and then "Login/Group Role...".
In the "General" tab, enter a name for the new user, such as
retrofun
.
Switch to the "Definition" tab, and enter a password for the user. Then switch to the "Privileges" tab.
This user should have the "Can login?" and "Inherit rights from the parent roles?" options enabled. To increase security it is best to have all other privileges disabled, as they are not needed.
Click the "Save" button to add the user.
Then right-click on the database on the left once again, then select "Create", and then pick "Database...".
Give the new database a name, such as also
retrofun
. Naming the user and the database the same is a naming convention that I find convenient, since each user will be dedicated to only one database. The owner of the database should be the
postgres
user, which is the administrator.
Click "Save" to create your new database.
The next step is to configure the privileges of the
retrofun
user so that it can have full access to the new database. In the left sidebar, expand the tree view starting from the
db
server and continuing on to "Databases", the
retrofun
database, "Schemas", and finally "public".
Right-click on the
public
schema and select "Properties...". Then select the "Security" tab.
Click the "+" in the "Privileges" table to add a new entry. Under "Grantee", select the
retrofun
user. In the "Privileges" column check the "ALL" option to give the user full access to the schema.
Click "Save" to store the new privileges.
To stop the PostgreSQL server you can issue the following command from the directory in which you have your
docker-compose.yml
file:
$ docker-compose down
To start the server again, repeat the "up" command as before:
$ docker-compose up -d
Thanks to the data being stored in standalone volumes, you can freely stop and restart the server without losing any data.
PostgreSQL Client
The final step is to install a PostgreSQL driver for Python. SQLAlchemy supports a few
PostgreSQL drivers
, and you can choose any of them if you have a preference.
A driver that is extremely popular and has proven to be very stable is
psycopg2
, which you can install with this command:
(venv) $ pip install psycopg2-binary
To connect to your database from Python you will later need to know the connection details. If you followed the instructions above, then these are:
Hostname:
localhost
(but use
db
as hostname to connect from the pgAdmin container)
Port: 5432
Database:
retrofun
Username:
retrofun
Password: the password that you selected for the user
Python driver:
psycopg2
Database Connection URLs
When using SQLAlchemy, a database to connect to is represented by a URL that has the following structure:
{dialect}{+driver}://{username}:{password}@{hostname}:{port}/{database}
URLs for MySQL and PostgreSQL are built using
mysql
or
postgresql
as dialect respectively, plus the connection details for your database.
The following examples assume that the user password is
my-password
:
# MySQL with pymysql
url = 'mysql+pymysql://retrofun:my-password@localhost:3306/retrofun'

# PostgreSQL with psycopg2
url = 'postgresql+psycopg2://retrofun:my-password@localhost:5432/retrofun'
Database URLs for SQLite are a bit different, because this is an in-process database without the concept of users or servers. For this database, the dialect name is
sqlite
and the driver can be omitted. The username, password, hostname and port are also omitted, since they do not have any meaning for this database. Finally, instead of a database name, a path to the database file is given.
The following examples show some possible database URLs for a SQLite database named
retrofun.sqlite
:
# database file in the current directory
url = 'sqlite:///retrofun.sqlite'

# database file in /home/miguel/retrofun directory
url = 'sqlite:////home/miguel/retrofun/retrofun.sqlite'

# database file in C:\users\miguel\retrofun directory (Microsoft Windows)
url = 'sqlite:///c:\\users\\miguel\\retrofun\\retrofun.sqlite'
If you look at these URLs carefully, you may think that they have too many forward slashes right after the
sqlite:
prefix, but these are all correct.
The first example uses a relative location (the current directory) for the database file. In this URL, the first two forward slashes are part of the
sqlite://
URL prefix, and the third slash is the one that comes after the username, password, hostname and port, only in this case these four are empty so only the slash separator needs to be included.
In the second example there are four forward slashes after the dialect and driver. The first three slashes have the same purpose as in the first example. The fourth slash is the start of an absolute path for the SQLite database file, which in this example is
/home/miguel/retrofun/retrofun.sqlite
.
The third and final example shows how an absolute path can be given when using the Microsoft Windows operating system. Here what follows the three forward slashes is an absolute path that starts with a disk drive and uses backslashes as path component separators. Python strings need the backslash character to be escaped by entering a second backslash.
The SQLite database provides one additional option: an in-memory database. This is useful for temporary databases, such as those used in unit tests. With an in-memory database, all the data is kept in the memory of the process, without persistence. This option is not going to be used in this book, but it is useful to be aware of it.
url = 'sqlite://'
In all the examples in this book, the database URL will be configured externally, in an environment variable named
DATABASE_URL
. To avoid having to set this variable in every shell session, create a file named
.env
(a dot followed by
env
, often called a "dotenv" file), open it in your text editor, and write the database URL that you would like to use in it as follows:
DATABASE_URL=sqlite:///retrofun.sqlite
The above example configures a SQLite database named
retrofun.sqlite
in the current directory.
The
python-dotenv
package allows an application to read variables from a
.env
file. Install it with
pip
:
(venv) $ pip install python-dotenv
Below you can see an example of how to read the
DATABASE_URL
variable from a Python program. Copy this code to a file named
db.py
in the project directory to try it out on your computer.
db.py
: Display the database URL
import os
from dotenv import load_dotenv

load_dotenv()

print('Database URL:', os.environ['DATABASE_URL'])
Run this example to ensure that you have configured your database URL correctly:
(venv) $ python db.py
Database URL: sqlite:///retrofun.sqlite
Proceed to
Chapter 2
.
Thank you for visiting my blog! If you enjoyed this article, please consider supporting my work and keeping me caffeinated with a small one-time donation through
Buy me a coffee
. Thanks!
