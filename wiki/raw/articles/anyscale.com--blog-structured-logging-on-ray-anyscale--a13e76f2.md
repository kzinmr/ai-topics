---
title: "Structured Logging with Ray on Anyscale"
url: "https://anyscale.com/blog/structured-logging-on-ray-anyscale"
fetched_at: 2026-10-05T10:08:36.764415+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# Structured Logging with Ray on Anyscale

Source: https://anyscale.com/blog/structured-logging-on-ray-anyscale

Link
Summary
Learn how Anyscale’s new structured logging boosts developer productivity when building AI applications like model training, model serving, or data preprocessing.
Link
The Problem
Current logging practices with Ray present several challenges that hinder efficient log management and analysis.
Link
Key Challenges:
Unstructured Logs:
Currently, Ray defaults to using Python’s logging library. While convenient, this often results in unstructured logs, complicating indexing and querying. To search logs, users must write complicated regular expressions, slowing down development time.
Integration Challenges:
By default, Ray does not ship logs to external storage. In practice, this means that users must implement their own log processing systems. The lack of structured logging poses integration challenges with many existing log viewing solutions.
Link
Solution: Structured Logging, Now Available on Anysale
To address these issues, we’re excited to introduce structured logging on Anyscale
Link
How It Works
Logging Configuration:
Users can now configure the Python logging library to output logs in a structured JSON format. This setup standardizes log entries, making them easier to handle.
Integration with Processing Systems:
Seamlessly integrate structured logs with log management and analysis tools like the ELK Stack (Elasticsearch, Logstash, Kibana) or Datadog. These tools automatically recognize the Ray logging JSON format, simplifying log ingestion and analysis.
Link
Key Benefits of Structured Logging on Anyscale
Ease of Parsing:
We’ve implemented structured logging in JSON because these files  are easier to parse programmatically, reducing reliance on complex regular expressions.
Enhanced Querying:
Structured logs facilitate better indexing and querying, simplifying log analysis.
Improved Log Management:
Standardized log format makes integration with existing log processing systems more efficient.
Link
Enhanced Log Viewing, available with Anyscale
Structured logging resolves historical issues to improve debuggability and integrations with the ML Ecosystem. We’ve also introduced the Anyscale Log Viewer for enhanced functionality, making it easier to monitor and debug applications out of the box.
Additional Benefits with Anyscale’s Log Viewer:
Automatically Enhanced Structured Logging:
Structured logs by default include searchable attributes like actor ID, node instance ID, timestamp, component name (serve applications), and request ID (serve applications) to speed up debugging even more
Centralized Log Viewing:
The log viewer is set up by default, providing a way to view logs in a centralized UI with useful attributes for easy access and analysis.
Scalability:
Search across millions of logs and thousands of nodes with the Anyscale Log Viewer.
Filtering
: Toggle through different log levels or components in the log viewing UI.
Context:
The log viewer provides additional context including surrounding lines in the UI, so you can more effectively identify and resolve errors.
By leveraging Anyscale's new log viewing features, you can take full advantage of structured logging, making application monitoring and debugging more efficient and effective.
Structured Log Viewing optimizes debugging and searching logs while simplifying integrations
Structured Log Viewing
Link
How to Get Started with Structured Logging on Anyscale
Structured logging is enabled by default on Anyscale Services. To get started, simply deploy your Ray Serve application on Anyscale.
To enable structured logging manually, check out the
Structured Logging page on Anyscale docs
.
Try it Today
