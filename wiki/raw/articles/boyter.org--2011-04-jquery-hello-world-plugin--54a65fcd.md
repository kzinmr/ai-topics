---
title: "jQuery Hello World Plugin"
url: "https://boyter.org/2011/04/jquery-hello-world-plugin/"
fetched_at: 2026-05-05T07:02:06.547070+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# jQuery Hello World Plugin

Source: https://boyter.org/2011/04/jquery-hello-world-plugin/

jQuery Hello World Plugin
2011/04/15
(169 words)
I was doing a simple job test the other day and one of the questions involved creating a simple jQuery plugin. Having never created one myself I had to look into how to do it. I couldn’t find a dead simple hello world plugin example so I thought I would create a simple example here for people to look at.
(
function
(
$
){
$
.
fn
.
HelloWorld
=
function
() {
$
(
this
).
html
(
'Hello World!'
);
};
})(
jQuery
);
The above essentially just attaches a new function called HelloWorld to the basic jQuery object. You can then call it using the below,
$
(document).
ready
(
function
() {
$
(
'body'
).
HelloWorld
();
});
What the above does is calls the HelloWorld function attached to the jQuery object from the body element. This then in turn calls our plugin which then appends “Hello World!” to the body element. The result is you see the test “Hello World!” appear in the body.
You can download the
jQuery hello world plugin
and supporting files here to run it yourself if you feel so inclined.
