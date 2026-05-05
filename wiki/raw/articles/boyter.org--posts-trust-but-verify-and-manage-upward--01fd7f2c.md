---
title: "A lesson on Trust but Verify and Managing Upward"
url: "https://boyter.org/posts/trust-but-verify-and-manage-upward/"
fetched_at: 2026-05-05T07:01:54.214713+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# A lesson on Trust but Verify and Managing Upward

Source: https://boyter.org/posts/trust-but-verify-and-manage-upward/

Previously I had covered the
worst program
I had ever worked on (although that probably needs updating now) and the
worst individual
and
the most incompetent individual
I ever worked with.
I thought it was time to lay out one of my own failures, of which resulted in me adopting
trust by verify
for a all future interactions… at least until I am more familiar with the individual.
This was back when I was working on C#, SQL Server and some ETL processing software the name of which I had forgotten. I had mentioned to my manager at the time that I should probably get more experience using the ETL software because simply because there was so much work there and I had never used it. When a new project came up to build a system for managing HR backend jobs, to deal with vanity and real titles and organizational chart management. Think, renaming titles, organizing organizational hierarchies and the like.
This was expected to have a huge amount of ETL work which I would be doing and as a result a contractor was brought in to do the C# portion. I had done some ground work and given them the instruction to use KendoUI, which was a Telerik jQuery. Seems it still exists
https://www.telerik.com/kendo-jquery-ui
but there is no open source version anymore. A pity because I really liked how it worked… perhaps there is a forked version around somewhere. The other major instruction was to use the following patterns when it came to data access in C#.
public
interface
IUrlRepository
{ IQueryable GetUrl();
void
Save(Url url); }
public
class
UrlRepository
: IUrlRepository
{
public
DbContext _context =
null
;
public
UrlRepository()
{
_context =
new
DbContext();
}
public
IQueryable GetUrl()
{
return
from
u
in
_context.Urls
select
u;
}
public
void
Save(Url url)
{
_context.Urls.AddObject(url);
_context.SaveChanges();
}
}
The reason for the above is that it allows you to perform all your joins in your service layer by adding an extension, Which then allows you to do the following, simple queries or joins
var
url = _urlRepo.GetUrl().OrderByCreateDate();
var
url = _urlRepo.GetUrl().OrderByCreateDate().ByCreatedBy(
"Ben Boyter"
);
var
result =
from
user
in
_userRepo.GetUser()
join
location
in
_locationRepo.GetLocation()
on
user.locationid
equals
location.id && location.name =
"Sydney"
select
user;
Its a really lovely pattern, and to date the best data access pattern I have come across. I wouldn’t trust the SQL that this produces at scale, but when done you get the ability to mock away your database and still test all your joins and filters in memory. Perfect for enterprise level applications.
With those instructions the contractor was off to the races. Progress reports each day were good, with the UI looking good, the components working as expected and everyone celebrating.
One interesting interaction from the contractor was him saying we needed a license for KendoUI. I pointed out it was licensed GPU and actually as a result we didn’t. He pushed back and said we had to make the code open source then, which I responded, it was an internal app, we are not distributing it, and even if we were only the JavaScript would need to have that. The project managers (yes more than one) either believed me or they liked the idea of not having to procure a license, so the matter was dropped.
The application was deployed, with the contractor doing some bug fixes. I would listen in and it seemed like all was well. However in this organization they for whatever reason had a firewall between the developers and the end users most of the time. Why? I have no idea. I don’t think it was to shield the BA’s or PM’s and secure their jobs, but the idea of keeping the people able to actually solve the users problems from the user seems insane to me. I would hear about sporadic bug reports, but these were dealt with by everyone else while I ironed out all of the ETL bugs.
Eventually the contractors contract was over and support duties fell to me. Thats when the bug reports came in.
The app is slow.
Functionality is broken.
The data is wrong.
Now I was surprised by this, after all for several weeks the issues had been worked on? It was then I looked under the hood of the application. Raw SQL being thrown around, no separation of concerns for the backend. It was in short a mess. I tried fixing a few of the bugs and just kept bumping into weird edge cases. At this point I rather strongly suggested that the funnel from PM/BA to me was not working. I wanted to sit with the end users directly and talk to them. Apparently this had to be raised to the powers that be but was eventually given the all clear.
When I meet with them, the room was… tense. I remember them instantly being defensive and hostile towards the PM/BA at the time. The PM ran through the issues. I too had a notebook and was writing everything down when one of the users asked who I was. I said I was the developer and was writing down all of the issues so I could fix them this afternoon. The user in question seemed relieved at this and started talking directly to me. The application had about 7 pages, each providing some level of functionality for adding/deleting and editing records. I listened, recorded and once we finished and left with the PM and BA heard them remark that that went better than they expected.
The PM and BA at this point wanted me to commit to a hard deadline estimated of when it would be done. I said 4 weeks, at which point they said they had already agreed to 2. Given how this was how things was going to work my first job was telling the PM and BA that they were now testers and assigned them pages I had finished to functionally test. Which they dutiful did. This was I suspect the first case of “managing up” I had tried.
The UI was functionally good, which is why nobody had noticed all the issues to this point and so my plan of attack was to rewrite the data access for each page, updating it to the requested repository pattern. This is generally known as the strangler pattern, where I slowly took over and killed the host, replacing the older code with the newer that I had written. I started with the first page, and as I went through it got progressively easier since portions of functionality were shared. One by one each page was finished, with the end users also testing and reporting back that everything worked as expected.
I put in some serious work here, and since I had multiple PM/BA’s and other people coming past my desk to get progress reports, I again managed up and had them all swing by my desk at the same time each day, giving them the update and requesting they ensure nobody else bothered me. As such I was able to meet the deadline they imposed, and had everything more or less resolved in the timeframe given with a day or two to spare, albeit at the cost of some of my sanity.
The last problem was fixing the performance issues. Locally everything worked fine, even with the full production data set, so it did not appear to be a scale issue. In the end the issue was down to the companies location of data center, and the amount of data being returned. I was in Sydney, while the data center was in Atlanta Georgia. As a result there was a 200ms hop of which I could do nothing about, but the contractor had simply turned any response from the database into JSON and returned it. For the list pages this was problematic because there were text descriptions in it, which would bloat the JSON responses to multiple megabytes and never be displayed. A quick transform function for those specific endpoints to filter out the redundant fields and everything was as fast as possible. Loading times for some pages dropped from multiple seconds to about 240ms, of which 200ms or so was transfer time. I did get one tech savvy user using Firebug in firefox to inspect the response and ask about the delay, to which I responded
We either move you to Atlanta, or Atlanta to you
Probably a bit snarky at the time but considering my mental state ill allow myself this small outburst. I think it communicated the point too.
Thankfully the result was fairly well received and I like to think I made some friends with the users. The PM/BA’s also were happy since I in effect saved their face since they were reporting progress up and were able to report success.
However what did I learn?
Well the first was trust by verify. I was pretty green in development at this time, and under the impression contractors, especially highly paid ones that are older than I know what they are doing. This… is not always the case. Like any other group there is a bell curve, where some are brilliant and others are not. My mistake was not verifying what they were doing. In my defense I was learning a new tool at the time, didn’t know I was empowered to verify or check this sort of thing, and assumed the PM/BA would be on top of it.
The other thing I learnt was that managing up is a viable and frankly good thing you should be doing. Top down management probably works well in very hierarchial organizations, but even then you have to empower groups to push back and take the initiative when possible. Even as a lowly ranked employee you have a lot more control than you think you probably do, especially in any organization dominated by middle management. They might call the shots, but you are the one doing the work and they need you.
So why this post? Well I was thinking about one of the more unusual interactions I ever had, which was with some random manager during the above project.
The most unusual interactions with a PM was them coming to me and asking if the unit tests passed. I responded yes, but I had written them so of course they pass?
They just repeated “Did they pass” so I said yes and then went on their way. Never did find out what they did with that information.
Bizarre indeed.
