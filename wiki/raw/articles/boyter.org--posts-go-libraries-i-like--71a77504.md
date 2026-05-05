---
title: "Go Libraries/Packages I Like"
url: "https://boyter.org/posts/go-libraries-i-like/"
fetched_at: 2026-05-05T07:01:55.480537+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Go Libraries/Packages I Like

Source: https://boyter.org/posts/go-libraries-i-like/

Go Libraries/Packages I Like
2023/12/13
(457 words)
In no particular order a list of Go libraries/packages I really like and some reasons why.
zerolog
I know that the changes to slog make it far closer to being what zero log is now, but I still prefer it for my own use.
requests
Anyone who works with python for a while learns about the requests library for making HTTP calls. This is similar but for Go. It has a few sharp edges when dealing with websites that don’t follow standards, but otherwise is amazing. Coupled with the next library in the list you end up with a pretty solid way to call endpoints.
trip
HTTP client middleware that allows automated retries, with backoff’s among other things such as authorization. Coupled with requests it really cleans up your HTTP calls.
lo
If you know of the wonderful underscore.js library then you probably have an idea of what this is. Similar idea, providing a lot of helper functions that allow dealing with some of Go’s sharp edges more easily. It does abstract away things that you might need to know about if you need absolute performance, but for most things it just makes life easier.
templ
HTML template language for Go. There is nothing you can do in this that you cannot in Go templates, but you get compile time checks of the code rather than actually having to run it. It also means you don’t need to worry about embedding template (although this is fairly easy these days anyway). Works really well with HTMX.
gjson
A simple way to get values out of JSON without needing to unmarshall into a struct. Really useful for tests, as well as annoying API’s that have mixed data types.
mux
The inbuilt Go router isn’t horrible, but is painful to use. This one supports path variables, and you can specify which http methods it uses.
sqlc
Generate type safe Go code to access your database. Of all the DB layer abstractions I have used this is best. Its similar to something I wrote in PHP over a decade ago, although much better.
xurls
The number of times I have gone looking for a URL regex only to find it misses some edge case… This solves a lot of that pain, especially when it comes to extracting them out of text.
The below are things I am exploring, but not sold on yet.
mockio
I am fond of saying that there is nothing like Java’s Mockito in Go… however this claims to be something like it. I am still testing it, but it looks promising.
cleanenv
Simple way to deal with env variables.
I fully expect this to be a living document with other useful packages I like added over time.
