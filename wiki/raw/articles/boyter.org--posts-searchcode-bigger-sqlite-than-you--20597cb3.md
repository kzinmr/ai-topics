---
title: "searchcode.com’s SQLite database is probably 6 terabytes bigger than yours"
url: "https://boyter.org/posts/searchcode-bigger-sqlite-than-you/"
fetched_at: 2026-05-05T07:01:54.603418+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# searchcode.com’s SQLite database is probably 6 terabytes bigger than yours

Source: https://boyter.org/posts/searchcode-bigger-sqlite-than-you/

searchcode.com’s SQLite database is probably one of the largest in the world, at least for a public facing website. It’s actual size is 6.4 TB. Which is probably 6 terabytes bigger than yours.
-rw-r--r-- 1 searchcode searchcode 6.4T Feb 17 04:30 searchcode.db
At least, I think its bigger. I have no evidence to the contrary, being by far the largest I have ever heard of. Poking around the internet did not find anyone talking publicly about anything bigger. The largest I could find using any search or LLM was 1 TB (without source), and a few people on HN and Reddit claiming to be working with SQLite database’s around the size of 10’s of gigabytes.
However lack of evidence does not mean such as thing does not exist, and so if you do have a larger database please let me know, either by mocking me on some comment section somewhere, or by direct abuse using my email below and I will be appropriately scolded.
Probably more interesting is why searchcode.com has such a large SQLite database. For those who don’t know
https://searchcode.com/
is my side/desperately needs to pay for itself/ passion project, which as the name suggests is a place to search source code. It has multiple sources including, github, bitbucket, codeplex, sourceforge, gitlab and 300+ languages. I have written about it a lot, which probably one of the more interesting posts about building its own index
https://boyter.org/posts/how-i-built-my-own-index-for-searchcode/
searchcode.com itself is now officially a ship of Theseus project, as every part I started with has now been replaced. A brief history,
First version released using PHP, CodeIgniter, MySQL, Memcached, Apache2 and Sphinx search
Rewritten using Python, Django, MySQL, Memcached, Sphinx search, Nginx and RabbitMQ
Never publicly released version using Java, MySQL, Memcached, Nginx and Sphinx search
Start of Covid 19 rewritten using Go, MySQL, Redis, Caddy and Manticore search
Replaced Manticore search with
custom index
now the stack consists Go, MySQL, Redis and Caddy
As of a few days ago Go, SQLite, Caddy
The constant between everything till now was the use of MySQL as the storage layer. The reasons for using it initially was it was there, I knew how to work it and it would scale along with my needs fairly well. So what changed? If you look at my previous choices you will see there is in general a move to reducing the number of dependencies. The older and more crusty I get the more I appreciate having a single binary I can just deploy. Single binary deploys are very simple to reason about.
So why SQLite? Well mostly because you can compile it directly into the binary, so I can have my single binary deploy. No need to install any dependencies. Why not write my own? I am not confident enough in my abilities to write something like this myself, at least not in any reasonable time frame. While I may be crazy enough to write my own index engine, I am not crazy enough to write my own storage persistence layer.
Looking at embedded databases I had previously used and played around with embedded Go databases such as
bbolt
but they never worked at the sort of scale I was expecting to deal with, and since the data I was working with was already mostly relational I wanted to stay in the SQL world.
SQLite has not been totally fault free however. Previously I had used it and ended up with the dreaded
"database is locked"
error till I found a blog mentioning the best solution in Go is to have two connections. The first being limited to the number of CPU’s for reading and another with a single connection for writing. Something like the below achieves this, and ensures you still have excellent read performance while avoiding the aforementioned error.
dbRead
,
_
:=
connectSqliteDb
(
"dbname.db"
)
defer
dbRead
.
Close
()
dbRead
.
SetMaxOpenConns
(
runtime
.
NumCPU
())
dbWrite
,
_
:=
connectSqliteDb
(
"dbname.db"
)
defer
dbWrite
.
Close
()
dbWrite
.
SetMaxOpenConns
(
1
)
The other issues I had previously had was cross compiling with CGO. I use a ARM Mac for personal development, for the battery life to and performance. However I deploy to Linux instances. Cross compiling such a thing in Go is trivial till you add in CGO and it becomes a major pain in the backside. Thankfully pure Go versions of SQLite exist such as
https://modernc.org/sqlite
which resolves the issue, at the expense of some performance.
With the above issues resolved first on some other projects, on August 13 2024 I started work on the conversion from MySQL to SQLite. Converting over to SQLite allowed me to start by improving database access by using
SQLC
. For those curious, you write SQL queries, and it converts them into type safe code you can then call. It’s an amazing tool and gets close to the C# Entity Framework level of productivity. I wrote something similar to it a long time ago in PHP but SQLC is a much better executed version of the idea.
Converting over to SQLite was actually fairly simple as a result and I had a proof of concept working locally in a week or two. However I then needed to start looking into the migration and thats where a lot of the pain started.
I had always known that storing code in a database was going to be problematic, simply because of the quantity of content. As a result I had used MySQL’s
compress
and
uncompress
functions when storing any code. Not the most ideal solution but it did crunch down the database enough that I could store it on SSD’s most of the time. However SQLite does not have such a function unless you pay (
PRAGMA compression = 'zip';
) or look to some 3rd party plugin.
I looked around and found the following
https://phiresky.github.io/blog/2022/sqlite-zstd/
which looked promising, but given that it came with the warning
I wouldn't trust it with my data (yet).
and that I would have needed to use a CGO version of SQLite.
I was discussing the issue on the TechZing podcast discord when someone mentioned that while they had not tried compression in SQLite themselves but that I might want to consider compression on the filesystem level. Some searching around showed that this could be very viable option,
https://news.ycombinator.com/item?id=29148198
https://trunc.org/learning/compressing-sqlite-with-zfs
.
So I got to work on a few linux VM’s with attached disks. Fiddling around with mounting disks with different filesystems in Linux is not something I had done since ReiserFS was a thing (I since discovered it has been removed from the kernel). I started looking at ZFS, since thats the only filesystem I knew supported compression. Knowing nothing about ZFS I was suggested to look at BTRFS since it should in theory be simpler and turned out to be trivial to setup with zstd compression.
Initial tests on a subset of the data showed a pretty drastic compression ratio.
$ compsize /mnt/btrfs-partition
Processed 1 file, 150753 regular extents (150753 refs), 0 inline.
Type       Perc     Disk Usage   Uncompressed Referenced  
TOTAL       20%      3.8G          18G          18G
none       100%       71M          71M          71M
zstd        20%      3.7G          18G          18G
With that done, I exported the entirety of searchcode’s database in preparation of the migration. This was done using a custom Go program hooking into both the previously written SQL logic and the new SQLC code. The conversion was surprisingly easy, with the only thing to keep in mind using transactions around batches of SQLite inserts to maintain insert performance.
I explicitly coded it to back off when the system was under load and after several days had an output 6.4TB SQLite file. This had me worried at first, since as mentioned I could not find any example of anyone working with SQLite at this level. As such I double checked my indexes and then ran the queries searchcode needs against it in a loop to establish all returned quickly. In fact most returned faster than the MySQL instance I was replacing, which stands to reason given I was replacing the network transfer that was happening previously.
With all of the above done I had one last thing to consider. Should I replace the server? searchcode.com was running on an older AMD 5950x. Still a powerful CPU, but I do like to replace the hardware every few years to get as much performance as possible. So I had a look around and decided to upgrade, to a new server. A real server. One with more cores, more RAM, ECC ram, and faster disks such as this from Hetzner
https://www.hetzner.com/dedicated-rootserver/ex130-r/
which interestingly turned out to be an Intel CPU. As such searchcode is now running on a Intel(R) Xeon(R) Gold 5412U with 256 GB of RAM. The increase in RAM allows me to grow the index by some factor (at least 2x) as well as improve it’t false positive match rates by tweaking the bloom filters.
I ordered and with it setup a day later, started migration over the network (this took a day or two) after setting up the new box box with the BRFS partition. Sadly the data turned out to be less compressible than my tests first suggested, but it still fits nicely into the storage I have for it with a fair amount of room to grow, albeit less than I had hoped for.
$ compsize /mnt/data/searchcode.db
Processed 1 file, 16481352 regular extents (16481360 refs), 0 inline.
Type       Perc     Disk Usage   Uncompressed Referenced  
TOTAL       76%      4.8T         6.3T         6.3T
none       100%      4.3T         4.3T         4.3T
zstd        23%      470G         1.9T         1.9T
So with everything setup and ready to do I flipped over the DNS entries to the new server and observed. Nothing appeared to go amiss, and so I left the updated DNS records in place. If you visit
https://searchcode.com/
you should be using the brand new code with SQLite backend. This post is already pretty long so I am not going to go through the new functionality that was released, instead saving it for another post.
As for SQLite? Well so far it appears to be working fine? While the schema searchcode uses is fairly simple, avoiding joins where possible and properly indexed I would not have expected SQLite to cope as well as it has. In fact making searchcode.com live with it was a giant leap of faith in it. I had no examples to follow were it to have issues, and while I had not done anything obviously wrong I was still deeply worried about hitting some unexpected issues. So far however this does not seem to be the case, with everything compared to the previous instance being much faster, from searches, to fetching pages and all of the backend processes that run.
As I write/publish this indexing is still happening, with the cores nicely indexing away, proving that the index I wrote scales nicely, even if it does abuse the poor garbage collector by allocating memory all over the place as the following log output indicates
memoryusage::Alloc = 69731 MB::TotalAlloc = 196538564 MB::Sys = 89425 MB::tNumGC = 48080
. Watching all 48 cores light up however always fills my heart with joy. There really is something about watching the blinkenlights.
So whats next? Well the plan is to double down on searchcode.com this year. I want to expand it out, and get it back to a state of paying for itself, and then to some level of profitability, and expand it out further. I have a heap of ideas on how to do that which will be running though over the coming weeks. I also want to start to focus on other services besides github to index, since they have their own nice search already. If you are running a 3rd party code hosting service, contact me as id love to explore this with you.
