---
title: "Some of the more annoying Go bugs I have dealt with"
url: "https://boyter.org/posts/more-annoying-go-bugs/"
fetched_at: 2026-05-05T07:01:56.556992+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Some of the more annoying Go bugs I have dealt with

Source: https://boyter.org/posts/more-annoying-go-bugs/

Thought I would write done some of the more annoying/interesting software bugs I have had to deal with recently.
Both were dealing with an archive system where large amounts of video/audio/images are uploaded into, then searchable. It allows the editing of metadata for each type of content, as well sending to external systems.
Problem #1
When a record is being edited a flag “This is being edited” is added to the record and removed on save. However randomly the flag would not be removed, and sometimes additional flags would appear. This was implemented as a “cheap” version of optimistic locking that worked within the application requirements.
Diagnosis
I spent a lot of time looking through this. Then penny dropped when given some additional information “Oh we wanted to put a timestamp in the edit message”.
Tracking back to how this message is created, and we find this code.
var EditedMessage string = time.Now().UTC().Format(time.RFC3339) + ": this record is being edited."
A global variable, assigned on the start of the application. However this also means the time is set only once, on application startup.
Once this was found, and some further questioning resulted in learning “Oh yeah, the time is there but is usually wrong”. Knowing this I was able to walk back what happened.
The time being the same setting was obvious. This was only created once on startup. However this does not explain why they were not being cleared.
Further investigation showed that the removal, worked by doing a string comparison of the message against the message of every flag. This was fine so long as the application was never restarted which would produce a new time. However deployments were not frequent enough to result in this as often as it was seen.
The catch was that multiple containers were running copies of the application behind a load balancer. Without sticky sessions set sometimes you landed on another container running the application. So you might read from one application but save on another. It’s likely they had a different time in the message, since its unlikely they started at 100% the same time.
As a result randomly you could clear flags, but not always, and sometimes when the application was deployed again or a container died you would get more than one. Every problem explained due to the use of a global variable.
Resolution
Changing the EditedMessage global to be a function which returned a new time every time it was called, and then modifying the string comparison to look for “this record is being edited” rather than
==
to know which flags to remove.
Problem #2
Function which allowed pushing to an external system was pushing the files into the root location of a directory rather than a specific folder which was required. This functionality was working previously, and no code changes had been made to the components that dealt with this recently. It was working in production without issue, and running the same code as other places.
Diagnosis
So this was a bit annoying to track down. This functionality has multiple touch points including durable queues, databases and multiple processes to read from and process each.
Looking through the code showed that there were no errors thrown, confirmed by inspecting the logs, and the entries in the database were correct. It was only on learning the next day that there was a database change made, but only in one environment which had the problem that the penny dropped.
The process when determining where to push the file reads from a SQS queue, and then pulls the matching record from the database. The database is where the location is contained, and so I zeroed in on that as the problem.
When code was written, whoever did so ignored the usual error that comes from
rows.Scan
. The code was also written using
select *
. As such when the new column came in the scan broke, but with the error ignored it meant it continued on, and left the struct it was scanning into with the default values. The default for a string being an empty string, so the location was set to empty.
The process then continued, and when determining where it should put the file used the empty string location pulled from the database. As a result all the files were pushed without issue, but landed in the root folder.
Resolution
Change back to explicit
select
targeting just the fields we want to ensure further database changes would not be an issue, and to deal with the scan exception. Additional logging added around this exception as well.
