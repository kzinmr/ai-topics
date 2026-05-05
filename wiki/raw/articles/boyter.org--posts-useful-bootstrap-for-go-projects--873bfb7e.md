---
title: "Useful bootstrap checklist for Go Projects"
url: "https://boyter.org/posts/useful-bootstrap-for-go-projects/"
fetched_at: 2026-05-05T07:01:57.348064+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Useful bootstrap checklist for Go Projects

Source: https://boyter.org/posts/useful-bootstrap-for-go-projects/

Mostly here because I keep forgetting all the things I want to put into a Go project when I start it. Collected into a list of things I actually need to do, tools to install and how to get things working.
This page is a work in progress and something I will add to as I remember things or discover something new.
Static Analysis
https://golangci-lint.run/usage/install/
Install that and run
golangci-lint run ./...
from the root when checking in.
https://golangci-lint.run/usage/false-positives/
Use the above to mute issues raised such as using
defer
or ignoring json.Marshall errors.
JSON
If JSON is being used and turns up in traces an easy option is to use the following.
import (
    jsoniter "github.com/json-iterator/go"
)

var json = jsoniter.ConfigCompatibleWithStandardLibrary
Run Tests
Remember you need … spread to have them run recursively.
go test ./...
Unique Codes
grep -r uniqueCode . | grep -o '"[a-z0-9]*"' | sort | uniq -c | grep -v '  1 '
Logging
Use zerolog for logging.
https://github.com/rs/zerolog
For every log message use the following format,
log.Error().Str(uniqueCode, "1d0223bc").Err(err).Msg("error with getting user from database")
Where uniqueCode is a constant defined somewhere as
uniqueCode
and then for the value use
date | md5 | cut -c 1-8
to generate a unique code.
This allows for quick finding of the line that produced an error or message.
To confirm that unique codes are in fact unique use the following,
grep -r uniqueCode . | grep -o '"[a-z0-9]*"' | sort | uniq -c | grep -v '   1 '
Which will return values if something is not actually unique.
Setting logging up is pretty simple, with the following,
switch strings.ToLower(config.LogLevel) {
case "debug":
    zerolog.SetGlobalLevel(zerolog.DebugLevel)
case "info":
    zerolog.SetGlobalLevel(zerolog.InfoLevel)
case "error":
    zerolog.SetGlobalLevel(zerolog.ErrorLevel)
default:
    zerolog.SetGlobalLevel(zerolog.InfoLevel)
}
Building
Use the following if targetting ARM Linux
GOOS=linux GOARCH=arm64 go build -ldflags="-s -w"
The build flag is there to reduce the size of the binary.
Router
Use
https://github.com/gorilla/mux
and be sure to set the following,
router := mux.NewRouter().StrictSlash(true)
to ensure that slashes are handled in an expected manner.
