---
title: "How to start a Go project in 2018"
url: "https://boyter.org/posts/how-to-start-go-project-2018/"
fetched_at: 2026-05-05T07:01:59.580884+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# How to start a Go project in 2018

Source: https://boyter.org/posts/how-to-start-go-project-2018/

This post is fairly old. See the updated version
Starting a Go project in 2023
Getting started with a Go project in 2018 is frankly a little more painful then getting anything else started IMHO. With that here is what I have been doing to get started.
The first thing to do is download and install Go. I would suggest always installing from the Go website itself
https://golang.org/
and following the instructions for your OS of choice.
The next step is the one that trips a lot of new players up. You need to either set your $GOPATH or be aware of what it is. Setting it has not been a requirement for a while as it defaults to your home directory like so
~/go/
but it can be quite handy to set it anyway. Reasons you may want to set it yourself include,
You can control there it goes beyond it being ~/go/
For Windows it allows you to share the directory between the WSL and Windows
Also for Windows you can set it to C:\Go\ to avoid the long path name issues
You can set it to another drive
You can set it to be shared among multiple users
The reason it is needed at all is because of how Go organizes dependencies. From the official documentation
$GOPATH must be set to get, build and install packages outside the standard Go tree.
. It’s easiest to think of the $GOPATH as being a workspace that contains all of your projects and dependencies. So long as all your go code lives inside it you are going to have an easier time working with go.
If you look in the $GOPATH directory you will see three directories,
bin
pkg
and
src
. The
bin
directory is where installed binaries that have a
main
package are placed after you run
go install
. If you install a project without a
main
package it is moved into the
pkg
directory. Lastly
src
which is where you should do all your development work.
You can check your go environment variables with the command
go env
.
One other thing I do is I update my machines path to point to the
bin
directory of my $GOPATH,
export PATH=$PATH:$(go env GOPATH)/bin
so that I can install anything I am working on quickly and have it available everywhere. For example,
$GOPATH
├── bin
│   ├── caire
│   ├── dep
│   ├── gocloc
│   ├── gocode.exe
│   ├── lc
│   ├── lc.exe
│   ├── license-detector
│   ├── scc
│   ├── scc.exe
│   └── waveform
The above is what my $GOPATH looks like and with the exported path I can run
scc
,
gocloc
and
lc
anywhere I want. I go a little further than most and have my GOPATH shared between Windows and Linux using the WSL so I can work on the same code-base in either, hence the .exe files in the above. To do that you just need to do a symlink inside the WSL to the Windows directory.
Go dependencies are a little odd the first time you run into them. I suspect this is because Google runs a mono-repo and as such the decisions around it were made with that in mind.
When you use the command
go get github.com/boyter/scc/
what happens is that a copy of the github repository is cloned into your
$GOPATH/src/github/boyter/scc/
directory. Go get works with other source control systems as well so you are not limited to git.
To start a new project there a few options. The first is to create a repository then
go get
it and then hack away in your editor of choice. The second is to create the directory manually then clone into it yourself. So long as the path matches your repository endpoints you are going to have a good time.
For example imagine you are working on a client site who have their own bitbucket instance at
bitbucket.code.company-name.com.au
and you want to clone a repository inside that has a clone URL of
https://username@bitbucket.code.company-name.com.au/scm/code/random-code.git
the code would be checked out if you run
go get
would be,
$GOPATH/src/bitbucket.code.company-name.com.au/scm/code/random-code
Searching
To search for anything about Go in your search engine of choice use the word
golang
rather than
go
when searching. For example to search for how to open a file I would search for
golang open file
.
Building / Installing
For commands which have
package main
go build   builds the command and leaves the result in the current working directory.
go install builds the command in a temporary directory then moves it to $GOPATH/bin.
For packages
go build   builds your package then discards the results.
go install builds then installs the package in your $GOPATH/pkg directory.
If you want to cross compile, that is build on Linux for Windows or vice versa you can set what architecture your want to target and the OS through environment variables. You can view your defaults in
go env
but to change them you would do something like,
GOOS=darwin GOARCH=amd64 go build
GOOS=windows GOARCH=amd64 go build
GOOS=linux GOARCH=amd64 go build
Unit Testing
To run all the unit tests for your code (with caching there is no reason to not run them all anymore) you should run the following which will run all the unit tests
go test ./…
To run benchmarks run the below inside the directory where the benchmark is. Say you have
./processor/
inside your project with a benchmark file inside there go to that directory and run,
go test –bench .
To create a test file you need only create a file with
_test
as a suffix in the name. For example to create a file test you may call the file
file_test.go
.
If you want to run an individual test you can do so,
go test ./… -run NameOfTest
Which will attempt to any test in all packages that have the name
NameOfTest
. Keep in mind that the argument
NameOfTest
supports regular expressions so its possible to target groups of tests assuming you name them well.
If you find yourself wanting or needing to run tests ignoring the cache you can do the following,
GOCACHE=off go test ./…
The standard practice with Go tests is to put them next to the file you are testing. However this is not actually required. So long as you can import the code (that is it is made exposed with an uppercase prefix) you can put the tests anywhere you like. This of course means you cannot test the private code which some consider an anti-pattern anyway.
Dependencies
By default
go get
makes your dependencies global. As such if another project does a
go get
to update the code you may end up being unable to build your own code. This I believe was a deliberate design choice by Google as they work in a mono-repo and with quick build times they can make global re-factors easier.
If you are reading this you are most likely not Google and the thought of someone updating something and you not being able to build your code again scares the crap out of you. If you want to manage them locally so you can lock down the version using the
vendor
directory and
dep
https://golang.github.io/dep/
Inside the root of your go project dependencies are checked to exist inside the
vendor
directory before looking at
$GOPATH
. As such if you place your dependencies in there they will be the ones your code builds and links against. To move them into the location is thankfully simple. Install
dep
then run
dep ensure
which will inspect your code and move what is required into
vendor
. Check the
dep
docs for details on how to update/remove dependencies. Keep in mind that
dep
will place a
Gopkg.lock
and
Gopkg.toml
file in the root path for tracking these.
When you have your vendor dependencies setup you can commit the contents of the
vendor
folder and then anyone can build your project without issue so long as they have a compatible compiler.
Multiple Main Entry Points
There are times where you want to potentially have multiple entry points into an application by having multiple
main.go
files in the main package. One way to achieve this is to have shared code in one repository, and then import it into others. However this can be cumbersome when you want to use vendor imports.
One common pattern for this is to have a directory inside the root of the application and place your main.go files in there. For example,
SRC
├── cmd
│   ├── commandline
│   │   └── main.go
│   ├── webhttp
│   │   └── main.go
│   ├── convert1.0-2.0
│   │   └── main.go
Then each entry point can import from the root package and you can compile and run multiple entry points into your application. Assuming your application lives in
http://github.com/name/mycode
you would need to import like so in each application,
package
main
import
(
"github.com/name/mycode"
)
With the above you can now call into code exposed by the repository package in the root.
OS Specific Code
Occasionally you will require code in your application that will not compile or run on different operating systems. The most common way to deal with this is to have the following structure in your application,
main_darwin.go
main_linux.go
main_windows.go
Assuming that the above just contained definitions for line breaks on multiple operating systems EG
const LineBreak = "\n\r"
or
const LineBreak = "\n"
the you can import and refer to
LineBreak
however you wish. The same technique will work for functions or anything else you wish to include.
Docker
Using the above techniques you can run inside Docker using multiple entry points easily. A sample dockerfile to achieve this is below using code from our hypothetical repository at
https://username@bitbucket.code.company-name.com.au/scm/code/random-code.git
The below would build and run the main application,
FROM golang:1.10

COPY ./ /go/src/bitbucket.code.company-name.com.au/scm/code/
WORKDIR /go/src/bitbucket.code.company-name.com.au/scm/code/

RUN go build main.go

CMD ["./main"]
The below would build and run from the one of the alternate entry point’s for the application,
FROM golang:1.10

COPY ./ /go/src/bitbucket.code.company-name.com.au/scm/code/
WORKDIR /go/src/bitbucket.code.company-name.com.au/scm/code/cmd/webhttp/

RUN go build main.go

CMD ["./main"]
A few people who have read this post suggested using multi stage docker builds
https://docs.docker.com/develop/develop-images/multistage-build/#use-multi-stage-builds
which works well with Docker 17.05 or higher. More details here
https://medium.com/travis-on-docker/multi-stage-docker-builds-for-creating-tiny-go-images-e0e1867efe5a
An example would be,
FROM golang:1.10
COPY . /go/src/bitbucket.code.company-name.com.au/scm/code
WORKDIR /go/src/bitbucket.code.company-name.com.au/scm/code/
RUN CGO_ENABLED=0 go build main.go

FROM alpine:3.7
RUN apk add --no-cache ca-certificates
COPY --from=0 /go/src/bitbucket.code.company-name.com.au/scm/code/main .
CMD ["./main"]
The result is much smaller images to run your code which is always nice.
Addtional commentary on Hacker News
https://news.ycombinator.com/item?id=17061713
