---
title: "Selecting a character set for MySQL and MariaDB clients"
url: "https://smalldatum.blogspot.com/2026/03/selecting-character-set-for-mysql-and.html"
fetched_at: 2026-05-05T07:01:16.809610+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# Selecting a character set for MySQL and MariaDB clients

Source: https://smalldatum.blogspot.com/2026/03/selecting-character-set-for-mysql-and.html

MySQL and MariaDB have many character-set related options, perhaps too many:
character_set_client
character_set_connection
character_set_database
character_set_filesystem
character_set_results
character_set_server
character_set_system
This is a topic that I don't know much about and I am still far from an expert. My focus has been other DBMS topics. But I spent time recently on this topic while explaining what looked like a performance regression, but really was just a new release of MySQL using a charset that is less CPU-efficient than the previous charset that was used.
Debugging
The intial sequence to understand what was going on was:
mysql -e 'SHOW GLOBAL VARIABLES like "character_set_%"
mysql -e 'SHOW SESSION VARIABLES like "character_set_%"
run "SHOW SESSION VARIABLES" from my benchmark client
Note:
the output from steps 1 and 2 was different
with SHOW GLOBAL VARIABLES I got character_set_client =latin1 but with SHOW SESSION VARIABLES I got character_set_client =utf8mb3. This happens. One reason is that some MySQL client binaries autodetect the charset based on the value of LANG or LC_TYPE from your Linux env. Another reason is that if autodetection isn't done then the clients can use the default charset that was set at compile time. That charset is then passed to the server during connection handshake (see thd_init_client_charset). So it is likely that character_set_client as displayed by SHOW GLOBAL VARIABLES isn't what your client will use.
the output from steps 2 and 3 was different
autodetection is only done when mysql_options() is called with a certain flag (see below). And that is not done by the MySQL driver in sysbench, nor is it done by Python's MySQLdb. So my benchmark clients are likely selecting the default charset and don't do autodetection. And that default is determined by the version of the MySQL client library, meaning that default can change over the years. For the source that implements this, search for MYSQL_AUTODETECT_CHARSET_NAME and read sql-common/client.c.
The following enables autodetection and should be called before calling mysql_real_connect():
mysql_options(...,
MYSQL_SET_CHARSET_NAME,
MYSQL_AUTODETECT_CHARSET_NAME);
Note that adding the following into my.cnf isn't a workaround for clients that don't do autodetect.
[client]
default-character-set=...
Notes
These are from my usage of MySQL 5.7.44, 8.0.45 and 8.4.8 along with MariaDB 10.6.25, 10.11.16 and 11.4.10. All were compiled from source as was sysbench. I installed MySQLdb and the MySQL client library via apt for Ubuntu 24.04.
The values for character_set_client, character_set_results and character_set_connection were measured via the MySQL command-line client running SHOW GLOBAL VARIABLES and SHOW SESSION VARIABLES and then the benchmark clients running SHOW SESSION VARIABLES.
The reason for sharing this is to explain the many possible values your session might use for character_set_client, character_set_results and character_set_connection. And using the wrong value might waste CPU.
What per-session values are used for character_set_client|results|connection?
* my.cnf has character_set_server=latin1
* per SHOW GLOBAL VARIABLES each is set to =latin1
* values below measured via SHOW SESSION VARIABLES
Values for character_set_client|results|connection
... with "mysql" command line client
... this is easy to change with --default-character-set command line option or equivalent option in my.cnf
dbms
5.7.44          utf8
8.0.45          utf8mb4
8.4.8           utf8mb4
10.6.25         utf8mb3
10.11.16        utf8mb3
11.4.10         utf8mb3
Values for character_set_client|results|connection
... with sysbench
client library version
dbms            5.7     8.0     8.4     10.6    10.11   11.4
5.7.44          latin1  latin1  latin1  NA      NA      NA
8.0.45          latin1  utf8mb4 utf8mb4 NA      NA      NA
8.4.8           latin1  utf8mb4 utf8mb4 NA      NA      NA
10.6.25         latin1  latin1  latin1  utf8mb4 utf8mb4 utf8mb4
10.11.16        latin1  latin1  latin1  utf8mb4 utf8mb4 utf8mb4
11.4.10         latin1  utf8mb4 utf8mb4 utf8mb4 utf8mb4 utf8mb4
Values for character_set_client|results|connection
... with insert benchmark (Python MySQLdb and /lib/x86_64-linux-gnu/libmysqlclient.so.21
... I am not what version is libmysqlclient.so.21, this is on Ubuntu 24.04
dbms
5.7.44          latin1
8.0.45          utf8mb4
8.4.8           utf8mb4
10.6.25         latin1
10.11.16        latin1
11.4.10         utf8mb4
