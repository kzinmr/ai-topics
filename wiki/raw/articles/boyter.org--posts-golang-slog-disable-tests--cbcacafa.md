---
title: "Disable Slog Messages in Go Tests"
url: "https://boyter.org/posts/golang-slog-disable-tests/"
fetched_at: 2026-05-05T07:01:54.712301+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Disable Slog Messages in Go Tests

Source: https://boyter.org/posts/golang-slog-disable-tests/

Disable Slog Messages in Go Tests
2024/12/08
(222 words)
As much as I like
ZeroLog
for Go logging Slog being added to the standard library fits in with my rule of avoiding 3rd party packages when they are not entirely required hence I have started moving anything I work on over to it.
One thing I find especially annoying however is log messages inside tests. As such here is a quick code snippet which turns off all slog outputs, but only for tests. Stick it into any
_test.go
file to disable logging outputs for that package.
// A no-op handler that discards all log messages.
type
noopHandler
struct
{}
func
(
h
*
noopHandler
)
Enabled
(
context
.
Context
,
slog
.
Level
)
bool
{
return
false
}
func
(
h
*
noopHandler
)
Handle
(
context
.
Context
,
slog
.
Record
)
error
{
return
nil
}
func
(
h
*
noopHandler
)
WithAttrs
([]
slog
.
Attr
)
slog
.
Handler
{
return
h
}
func
(
h
*
noopHandler
)
WithGroup
(
string
)
slog
.
Handler
{
return
h
}
// TestMain runs before any tests and applies globally for all tests in the package.
func
TestMain
(
m
*
testing
.
M
) {
slog
.
SetDefault
(
slog
.
New
(
&
noopHandler
{}))
exitVal
:=
m
.
Run
()
os
.
Exit
(
exitVal
)
}
EDIT
The nice thing about doing things in public is excellent people can show you better ways to achive things! Anton x’ed/tweeted responded with this
https://x.com/ohmypy/status/1866078171340185706
which allows you to condense the above into the below,
// TestMain runs before any tests and applies globally for all tests in the package.
func
TestMain
(
m
*
testing
.
M
) {
slog
.
SetDefault
(
slog
.
New
(
slog
.
NewTextHandler
(
io
.
Discard
,
nil
)))
exitVal
:=
m
.
Run
()
os
.
Exit
(
exitVal
)
}
