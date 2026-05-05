---
title: "Query Compilation Isn't as Hard as You Think"
url: "https://databasearchitects.blogspot.com/2025/11/query-compilation-isnt-as-hard-as-you.html"
fetched_at: 2026-05-05T07:01:27.564619+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Query Compilation Isn't as Hard as You Think

Source: https://databasearchitects.blogspot.com/2025/11/query-compilation-isnt-as-hard-as-you.html

Query compilation based on the
produce/consume model
has a reputation for delivering high query performance, but also for being more difficult to implement than interpretation-based engines using
vectorized execution
. While it is true that building a production-grade query compiler with low compilation latency requires
substantial infrastructure and tooling effort
what is sometimes overlooked is that the vectorization paradigm is not easy to implement either, but for different reasons.
Vectorization relies on vector-at-a-time rather than tuple-at-a-time processing. High-level operations (e.g., inserting tuples into a relation) must be decomposed into per-attribute vector kernels that are then executed successively. This requires a specific way of thinking and can be quite challenging, depending on the operator. In practice, the consequence is that the range of algorithms that can be realistically implemented in a vectorized engine is limited.
In contrast, compilation is fundamentally simpler and more flexible in terms of the resulting code. It supports tuple-at-a-time processing, which makes it easier to implement complex algorithmic ideas. Developing a query processing algorithm typically involves three steps: First, implement the algorithm manually as a standalone program, i.e., outside the compiling query engine. Second, explore different algorithms, benchmark, and optimize this standalone implementation. Finally, once a good implementation has been found, modify the query compiler to generate code that closely resembles the manually developed version.
At TUM, we use a simple pedagogical query compilation framework called p2c ("plan to C") for teaching query processing. It implements a query compiler that, given a relational operator tree as input, generates the C++ code that computes the query result. The core of the compiler consists of about 600 lines of C++ code and supports the TableScan, Selection, Map, Sort, Aggregation, and Join operators.
The generated code is roughly as fast as single-threaded DuckDB and can be easily inspected and debugged, since it is simply straightforward C++ code. This makes it easy for students to optimize (e.g., by adding faster hash tables or multi-core parallelization) and to extend (e.g., with window functions).
To keep p2c simple, it does not support NULL values or variable-size data types (strings have a fixed maximum length). Compiling to template-heavy C++ results in very high compilation times, making it impractical for production use. At the same time, p2c employs the same core concepts as Hyper and Umbra, making it an excellent starting point for learning about query compilation. Note that this type of compilation to C++ can also serve as an effective prototyping platform for research that explores new query processing ideas.
Find the code for p2c on github:
https://github.com/viktorleis/p2c
