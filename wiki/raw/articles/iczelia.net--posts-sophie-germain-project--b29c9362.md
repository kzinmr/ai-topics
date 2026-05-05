---
title: "The Sophie Germain Prime Project"
url: "https://iczelia.net/posts/sophie-germain-project/"
fetched_at: 2026-05-05T07:01:18.991023+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# The Sophie Germain Prime Project

Source: https://iczelia.net/posts/sophie-germain-project/

Introduction
⌗
The
Sophie Germain Prime Project
primarily aims to collect, analyse and distribute Sophie Germain primes.
I have started this project in order to facilitate research on the Blum-Blum-Shub random number generator and related cryptographic algorithms (like the Blum-Goldwasser cryptosystem). Large Sophie Germain primes (as big as 4096 bits) are
used in the BBS generator
to fulfill elementary security requirements; unfortunately they also take a long and generally unpredictable amount of time to find.
Users may submit primes to the project, which will be verified and stored in a database. The project also provides a web interface to search for Sophie Germain primes satisfying given criteria, statistics on the currently recorded primes. There are plans to create periodic torrent dumps of the database.
The project is open to technical and theoretical contributions, which can be submitted to me via e-mail. Alternative means of hosting the project are also welcome from parties interested in donating the server space and bandwidth.
Roadmap for the project
⌗
The following technical enhancements are planned:
A more efficient backend for the database, recording more information about the primes such as their record date and submitter.
Set up a separate hosting platform for the project, which will allow for more efficient data distribution and backups.
Set up a way for clients to download database dump (perhaps via Torrent).
