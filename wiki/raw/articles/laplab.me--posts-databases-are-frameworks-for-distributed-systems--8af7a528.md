---
title: "Databases = Frameworks for Distributed Systems"
url: "https://laplab.me/posts/databases-are-frameworks-for-distributed-systems/"
fetched_at: 2026-05-05T07:01:24.686626+00:00
source: "Nikita Lapkov (laplab)"
tags: [blog, raw]
---

# Databases = Frameworks for Distributed Systems

Source: https://laplab.me/posts/databases-are-frameworks-for-distributed-systems/

This article was originally
posted on dev.to
, but it turns out that HackerNews banned this website, so I decided to create my own.
Feel free to join the
discussion on HackerNews
.
Lego of the database world
It is quite common for a distributed database to have the following components:
Distributed Storage
Usually, this component has an interface of a key-value store:
Get(key)
and
Set(key, value)
, where
key
and
value
are some binary strings. This component knows nothing about the data - it can be rows from the table, JSON documents or something else entirely. Usually, this component provides guarantee of “durability”, meaning that data will not be lost in some failure scenario. A common example of such scenario is “less than half of the servers are down”.
Communication between cluster nodes
This component implements some kind of communication protocol to send and receive messages from one node to another.
Computation model
This component executes result to the user’s query. For instance, set of rows requested using SQL.
In classical databases (such as PostreSQL), all of these components are implemented in one single application. Such application manages everything on its own: controls storage, talks with other nodes in the cluster and computes results to SQL queries.
In MapReduce systems (such as Hadoop) and some other databases (such as Google BigQuery), various database components are physically separated. Some of the cluster nodes are reserved exclusively for storage. Other nodes are used only to compute results to SQL queries. If SQL query needs some data, it is transferred from the storage node to the compute node over the network.
Lego of distributed systems
Now let us imagine we want to create a new distributed system - a service to monitor various metrics (like
Prometheus
). Depending on the specific requirements to this system, we are likely to need the following:
Distributed storage with “durability” guarantee
We need to store user’s metrics somewhere and we do not want to loose valuable data because of the datacenter downtime.
Communication between cluster nodes
Monitoring system can be deployed in multiple datacenters to reduce latency and improve fault tolerance. Various instances of our system will need to coordinate with each other.
Computation model
Firstly, our system must accept requests to store new metrics. Secondly, it should respond to requests to read time-series data and generate reports for monitoring graphs.
Writing each of these components is a non-trivial task. Not only we need to write code and tests, but we also need to harden the system in production. The latter often leads to discovery of unexpected bugs and inefficiencies in design.
Now let us go back to the databases. They have all the components we need to build our distributed system. These components are already implemented, tested and hardened by thousands of various workloads. What is more, each of these components could be separated from the database itself and used on its own.
This basically means that databases could be used as frameworks to build new distributed systems.
Disclaimer:
This is a generalization to demonstrate a point. Some databases have a design which does not support using their components on its own or were not designed to be used in a distributed setup. Some distributed systems may not fit into the model described above. As always with Software Engineering, common sense and understanding of system requirements at hand should go first.
Examples
YDB
Image source:
https://ydb.tech/
YDB
is a distributed database developed in
Yandex
. It provides horizontal scalability and strong consistency guarantees.
Under the hood, YDB uses
actor model
. Actor is a unit of concurrency which is able to:
Receive messages from other actors
Send messages to other actors
Launch new actors
Actor is always single-threaded and can only change its internal state. Actors have no concept of shared state, which means that all synchronization is done through message passing. On one hand, there are no more mutexes in the code. On the other hand, you can no longer just write to memory for the other actor to see it.
YDB has a special name for actor - tablet. Tablets are building blocks of YDB. SQL queries execution, transaction coordination, creation of new tablets - each of these tasks is executed by one or more tablets. To use this post terminology, tablets are the
computation model
.
As actors, tablets need to send and receive messages. There is a special system in YDB created just for that - it is called interconnect. Each tablet is given an ID and tablets can send messages to each other using this ID as their postal address. Interconnect is a system for
communication between cluster nodes
.
Lastly, tablets need to store their state somewhere. For instance, tablets representing a shard of SQL table need to store range of table rows assigned to them. YDB has a
distributed storage
, which can store arbitrary binary blobs with “durability” guarantee.
Having all these components makes YDB not only a database, but also a generic distributed computations platform. Distributed system developer can write their own app logic by creating a new kind of tablet and reuse the rest of the system for their own purposes.
Disclaimer:
YDB is advertised as a database solution. No public documentation was announced about using it as a platform for distributed systems.
Image source:
https://www.tarantool.io/
Disclaimer:
I did not contribute to Tarantool, neither did I use it in production.
Tarantool
is an application server for distributed systems written in Lua. Lua applications launched in Tarantool have API access to the following components:
Distributed transactional database. This database supports 2 modes of operation - in-memory and with commits to disk. Second mode makes this component
distributed storage
in this post’s terms.
Communication protocol called SWIM. It allows to send and receive
messages between cluster nodes
.
Since the application server itself makes the
computation model
, we have all components necessary to call Tarantool a generic distributed computations platform.
This does not really sound impressive. It looks like Tarantool was initially created to be such a platform, so no surprise it fits all the criteria. The thing is, Tarantool initially was created as a database, which then quickly developed into a full-grown computational platform. The fact that it only took 2-3 years for that is outstanding, but it also shows how a database solution has evolved into “framework” to build distributed systems.
Conclusion
As serverless market grows larger, more database solutions start to consider modular architecture, where various components of the system are separated. This allows to allocate one instance of such component per serverless tenant, providing clear separation between users. Making database solution modular is also the first step to make various parts of it reusable by non-database application. It is interesting for me to see if in 5-10 years term “database” will slowly evolve into “distributed computations platform”.
