---
title: "Giving your Go apps Tigris superpowers"
url: "https://www.tigrisdata.com/blog/storage-sdk-go/"
fetched_at: 2026-06-05T07:01:41.338630+00:00
source: "xeiaso.net"
tags: [blog, raw]
---

# Giving your Go apps Tigris superpowers

Source: https://www.tigrisdata.com/blog/storage-sdk-go/

If you use Go for your web services and want to take advantage of Tigris'
advanced features like
bucket forking
,
snapshots
, and
object renaming
,
normally your code has to look like this:
func
WithRename
(
)
func
(
*
s3
.
Options
)
{
return
func
(
options
*
s3
.
Options
)
{
options
.
APIOptions
=
append
(
options
.
APIOptions
,
http
.
AddHeaderValue
(
"X-Tigris-Rename"
,
"true"
)
)
}
}
_
,
err
=
client
.
CopyObject
(
ctx
,
&
s3
.
CopyObjectInput
{
Bucket
:
aws
.
String
(
bucketName
)
,
CopySource
:
aws
.
String
(
bucketName
+
"/"
+
keyName
)
,
Key
:
aws
.
String
(
targetName
)
,
}
,
WithRename
(
)
)
if
err
!=
nil
{
log
.
Fatalf
(
"Unable to rename object. Here's why: %v"
,
err
)
}
With the new SDK, it looks like this:
_
,
err
:=
client
.
RenameObject
(
ctx
,
&
s3
.
CopyObjectInput
{
Bucket
:
aws
.
String
(
bucketName
)
,
CopySource
:
aws
.
String
(
bucketName
+
"/"
+
keyName
)
,
Key
:
aws
.
String
(
targetName
)
,
}
)
if
err
!=
nil
{
log
.
Fatalf
(
"Unable to rename object. Here's why: %v"
,
err
)
}
The
Go Storage SDK
fixes this. It gives you dedicated methods for Tigris features, in two modes:
If you want to get started with it today,
go get
it:
go get github.com/tigrisdata/storage-go@latest
An SDK so nice we did it twice
​
One of the best ways to think about Tigris is that it's like S3, but more.
Tigris handles global replication for you. Tigris handles
migrating your data for you
.
Tigris also lets you snapshot, fork, and
download bundles of objects all at once
.
These operations extend S3, so the SDK extends the S3 client. Here's what you
get:
As Tigris gets more features, we plan to just add more methods.
This mode is designed to be a
drop-in replacement
for your existing S3 client
to make migration trivial. When I moved some of my own projects over from the
AWS S3 library to package storage, it took about 30 seconds at most. Everything
compiled normally, everything worked as expected, and I got access to the extra
features I needed. Win/win/win!
But wait, there's more
​
Honestly, we could have stopped there, but we didn't. Alongside this I also
added
package simplestorage
:
a brand new interface to object storage. Most of the time your apps end up using
a single bucket. Why should you have to pass the bucket name every time you do
anything? Take a gander at how easy it is to copy a file from Tigris to your
local filesystem:
client
,
err
:=
simplestorage
.
New
(
ctx
)
if
err
!=
nil
{
panic
(
err
)
}
obj
,
err
:=
client
.
Get
(
ctx
,
"my/key"
)
if
err
!=
nil
{
panic
(
err
)
}
defer
obj
.
Body
.
Close
(
)
slog
.
Info
(
"object metadata"
,
"key"
,
"my/key"
,
"size"
,
obj
.
Size
,
"content-type"
,
obj
.
ContentType
,
)
fout
,
err
:=
os
.
Create
(
"./var/object-data"
)
if
err
!=
nil
{
panic
(
err
)
}
defer
fout
.
Close
(
)
io
.
Copy
(
fout
,
obj
.
Body
)
The bucket name and credentials were inferred from environment variables:
TIGRIS_STORAGE_BUCKET
: The default bucket to operate on.
TIGRIS_STORAGE_ACCESS_KEY_ID
: The access key ID for your app's
keypair
.
TIGRIS_STORAGE_SECRET_ACCESS_KEY
: The secret access key for your app's
keypair
.
If you don't want to change the environment variable names, simplestorage will
use the standard
AWS configuration resolution flow
you're already used to.
Forked buckets work with the
For
method:
newBucket
,
err
:=
client
.
ForkBucket
(
"my-bucket"
,
"my-agents-bucket"
)
if
err
!=
nil
{
panic
(
err
)
}
newBucketClient
:=
client
.
For
(
newBucket
.
Name
)
The main innovation here is reducing cognitive load so that you can focus on
what you're doing with your buckets instead of plumbing the minutiae of your
object storage API being automatically generated from Java classes. There's also
nothing stopping you from using this with AWS S3 or another object storage
provider like
Hetzner object storage
:
s3Client
,
err
:=
simplestorage
.
New
(
ctx
,
simplestorage
.
WithRegion
(
"fsn1"
)
,
simplestorage
.
WithEndpoint
(
"https://fsn1.your-objectstorage.com"
)
,
simplestorage
.
WithAccessKeypair
(
accessKeyID
,
secretAccessKey
)
,
)
if
err
!=
nil
{
panic
(
err
)
}
Advanced Tigris features like bucket forking will not work (Hetzner doesn't
implement our extensions to the S3 API), but basic object manipulation will work
just fine.
Note that any
object
manipulation functions will use the client's default
bucket, but any
bucket
manipulation functions require you to spell out the
bucket's name just to be sure you're operating on the right bucket.
Get
go
-ing today
​
If you want to try this out, install it in your Go project with
go get
:
go get github.com/tigrisdata/storage-go@latest
Please give us feedback
in the storage-go repo
. We want to
make this the best way to use Tigris for Go developers and your feedback can
only make it better.
Ready to supercharge your Go apps?
The Go Storage SDK gives you first-class access to bucket forking, snapshots, and more — with less boilerplate than raw S3 calls.
