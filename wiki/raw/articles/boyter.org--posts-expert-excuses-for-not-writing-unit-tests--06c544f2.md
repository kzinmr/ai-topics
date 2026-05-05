---
title: "Expert Excuses for Not Writing Unit Tests"
url: "https://boyter.org/posts/expert-excuses-for-not-writing-unit-tests/"
fetched_at: 2026-05-05T07:01:59.198501+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Expert Excuses for Not Writing Unit Tests

Source: https://boyter.org/posts/expert-excuses-for-not-writing-unit-tests/

A while back I collected all of the fake Orly book covers I could find an posted them online
https://boyter.org/2016/04/collection-orly-book-covers/
I also mentioned that I was seriously considering writing content for the “Expert Excuses for Not Writing Unit Tests” one. I think I had this idea at the time that it was something I could potentially sell or use to raise my profile. Since I am not a comedy writer there is a market of about 0 people in the universe who would pay for content like this. I have no idea what I was thinking.
Anyway I did write some content, which I have cleaned up and included below.
Or if you like you can get it here in a nice PDF or EBook format. It is free, (or you can kick me some cash if you like)
https://leanpub.com/expertexcusesfornotwritingunittests
and perfect for dropping into the company chat without context and see what sort of a fuss you can kick up.
Expert Excuses for Not Writing Unit Tests
Management has cracked it. “We need to improve code quality! Start writing unit-tests!” they cry. The problem is that you are a ninja 10x programmer and have no need for this. Management clearly does not understand on what level you operate on. However sometimes you need to play the system to get what you need. What follows is a brief document to help with this.
This is going to sound strange but in this goal Wally of Dilbert Fame
https://en.wikipedia.org/wiki/Wally_(Dilbert)
must be your inspiration. His whole goal is to avoid doing any work, and as such a lot of the techniques apply to avoiding writing unit tests.
The Promise of Bad Tests
The first line of defense against unit testing is to fight before the decision to write them is even made. If you can win this argument you are ahead of anything else. If you are starting from an existing code-base you are in the enviable position have being able to have a few additional arguments.
Lets discuss a few ways you can help support your argument.
Testing leads to bad design
A lot of arguments point out that testing can lead to a better design. Use this against itself. It can always produce a crappy design all about accommodating the tests and not the requirements. If you have clearly specified roles be sure to point out this is is taking work away from the architects and project leads. For languages such as Java/C# use the argument that if you want to test then every method needs to be public which opens up a new class of bugs and makes your interfaces unclean.
Point out that giving someone a brush does not make them an artist and as such giving someone nunit does not make them understand software architecture and design patterns.
Adding of cost
Point out that code has cost. The more lines of code (LoC) the greater the cost. Its worthwhile pointing out that the business pays for functionality not tests. Remember to reference the COCOMO model
https://en.wikipedia.org/wiki/COCOMO
when talking about LoC and cost, and never mention what it actually is.
Measuring programming progress by lines of code is like measuring aircraft building progress by weight. - Bill Gates
Use this argument.
Many studies do show a correlation between LoC and the overall cost and length of development, and between LoC and number of defects. So while it may not be a precise indication of progress, it is not a completely useless metric. The lower your LoC measurement is, the better off you are in terms of defect counts.
For a tool to calculate this for you try
https://github.com/boyter/scc/
which will also give you a COCOMO estimation. Be sure to run it over projects that have tests and see how much additional cost the tests add. Do this internally if you can with projects that have tests and point out that the tests add some percentage of cost. If you can cherry pick projects to make this look worse the better off you will be.
If someone challenges that the project with tests was more successful point out using the same model that the project cost more. More money spent means more quality to most people. If you mix metaphors and ideas here you can also impress and confuse people to the point they will be afraid to challenge you further.
For example say someone suggests that project Z has tests and as such tests are valuable. A good response to would be “A Ferrari costs more than a Kia”, and that having a larger QA budget would be more effective.
Be sure to point out that adding tests means writing more code which takes longer, which also impacts cost.
Also be sure to point out that while tests are being written (especially for existing projects) that nobody will be fixing bugs. This is usually enough of an argument to stop everything dead in its tracks.
Faking It
So management is coming down hard on you or your team is all brain-washed. The rule has been changed and now you must write tests against some metric or stupid PR system to enforce it. What do you do now? The first thing to do is start faking your tests as quickly as possible. Don’t worry. A few days of creative code should help you.
Auto Generating
If you have any code that is generated somehow you want to hook into this process as quickly as possible. There is a land grab afoot and you need to own this process. Modify the code ASAP and ensure that the next git blame is all yours. A good way to achieve this is to switch the newlines from unix to windows and back, or apply an aggressive code linter. If neither are possible comment the code extensively (with slightly wrong comments!) so it looks like you know the most about it.
With the land grab over time to work.
Modify your generator process to generate tests to verify the generated code. Be creative with this but play the long con. You want initially to generate just a few tests. This is especially important if someone has setup a CI/CD system. As time goes on have the code generate more and more tests. Firstly this shows progress to the metrics you are likely being measured by and secondly it makes you look like a test champion.
Now you begin.
Slowly add enough tests to start impacting the test cycle. You want to gradually make it slower and slower to run the tests. You need to do this as the test suite increases to ensure it feels natural. With this in place wait till there is an important deadline. Now is the time to strike. Deliberately slow the tests down. Keep doing this until the build process is so slow it is unbearable. This has a twofold effect. The first is you should be able to score a sweet upgrade on your machine. The second is that the tests will no longer be run locally. This is excellent news as everyone will begin to check in code without running their own tests as well. Once this becomes the norm, you want to start to introduce subtle bugs. Be sure to blame the process, as had you been able to run the application quickly and verify your changes manually this would never have happened.
Sow seeds of self doubt.
Learning From Volkswagen and Diesel-gate
Volkswagen intentionally programmed turbocharged direct injection diesel engines to activate certain emissions controls only during laboratory emissions testing. Genius. We can learn from this and make our tests pass always when under a tested condition. The best part is that this already exists! See
https://github.com/hmlb/phpunit-vw
for PHP and
https://github.com/auchenberg/volkswagen
for JavaScript. If this does not exist for your framework of choice read the code and implement it. If asked say you are working on code to determine what CI the code is running in which sounds reasonable.
Remember this needs to be a long con.
Leave the fix in place for a few weeks/months and then pull it. Better yet remove it a few days before that critical production release. Everyone will be scrambling to patch the code and fix the tests. With your coffee cup in hand politely suggest that you skip the pipeline and push straight into production. After all the code was working yesterday right? If the exception is made then you are almost there. Just repeat a few times until skipping the testing pipeline is the normal work-flow. Keep track of how often this is done, and start reporting it after it has happened a few times.
Shifting Blame
It might come to pass that since you are being forced to test you may become accountable for software quality. You must shoot down this argument as quickly as possible. If you are ever held accountable you are sunk. Lets go through various lines of shifting the blame.
Its QA’s problem
If you have a QA department then play office politics to get them defensive about their jobs. Casually drop into conversations that if you have tests they won’t be required. If you don’t have one then point out that that a proper QA process can catch 99.99% percent of errors. Cite The Write the Right Stuff to help with this argument
http://www.fastcompany.com/28121/they-write-right-stuff
Blaming other team members
If you have a junior on your team or someone who is not a rock-star ninja casually drop their name into failures. This is where you can learn from Dilbert’s Wally. Remember you need to keep your insults hidden so they appear to be compliments.
For example “Barry is really working hard testing that dead code, such dedication!”. Be sure to assist them a lot, and even pair program with them. You want git blame to point at them a lot of the time. Then when anything fails you can point out politely that a lot of the bugs seem to come from some individuals.
This works especially well with CI/CD systems where you can have their name next to every failed build. Then you come and save the day on your machine and suddenly every green build is from you.
Blaming the technology
For whatever framework you are using check their bug reports. There are bound to be quite a few. This can help support your arguments. After all if the tools you are using are buggy how can you be expected to rely on them? If this allows you to create your own so much the better. Be sure to own that project and introduce your own bugs. Blame all issues on the technology itself or on bugs in the language/framework implementation. Also remember to record the really nasty framework bugs and blame them later for random errors.
How to test the tests?
Argue that you cant test the tests so how can you be sure they actually work? The argument requires some preparation however as someone may point out that mutation testing covers this.
The counter argument depends on if they are able to quote what percentage of tests this should help with. If not point out that mutation testing is only 50% effective, at which point it might as well be guessing. If they quote with a number such as “Mutation testing catches errors in 70% of the tests” use the counter argument (using you best Homer Simpson impression) “Oh, people can come up with statistics to prove anything. 14% of people know that.”.
If they persist fall back on the argument that proper QA and design processes catch 99.99% of errors and cite NASA as a source using this article The Write the Right Stuff to help with this argument
http://www.fastcompany.com/28121/they-write-right-stuff
and suggest hiring in the QA department.
If you need to fall back to why your technology sucks search for “Why langage/framework/technology sucks”. If you want a head start check out
https://wiki.theory.org/YourLanguageSucks
for good arguments for most languages.
Using a duck typed language? Awesome! Blame it. Be sure to point out how the lack of typing is causing things to fail everywhere and your tests become increasingly flaky.
Using a static language? Great! Point out how everything is rigid making it impossible to test. Using Java or C#? Excellent. Make everything final, private and never use an interface. This should make it impossible to test and whats more you can prove it.
Blaming the process
This is the best argument ever if you have a process driven company. If things aren’t working, blame the process. Do it loudly and insist on many meetings about problems in the process. For full marks complain loudly outside of these meetings about how long they are taking too long and if you could just side step everything it would be done by now.
Remember that when attacking the process you need to attack everything in it. If part of the process is requirements gathering insist that developers should be involved with the business analyst and project manager. If part of the process is QA insist that the project manager needs to be involved as they are a key stakeholder. At every step try to include as many people as possible. This will slow down development and increase costs.
As this happens stakeholders will start to complain about the escalating project costs and time-lines. You can then smoothly suggest dropping writing the tests. Use your previous arguments about doubling up on QA’s costs and the increased costs to help.
Blaming the requirements
I’m only as good as my requirements!
Fluid requirements are your ally. The more often the requirements change the more cost you can allocate to changing tests to meet the new requirements, of course you didn’t write any, so use this time for chilling by the water cooler or getting another coffee. Tell anyone who asks you are networking and discussing how to improve quality without increasing costs.
Blame a lower level, OS / Hardware
The average user will never notice the difference. If you are using a language such as Java blame the runtime environment. A good source to check for things to blame are the release notes. Jot down any promising bug and report all of them as being related to it. This makes you look highly productive and an active go getter! Remember hardware bugs are solid gold. If you ever find one horde it and introduce it into all your tests. It will pay dividends later.
Its worth it to remember the chain of things that it takes to run your code. You can probably blame almost any portion of the chain knowing nobody can ever prove otherwise.
For example, if you are using Java here is a standard chain of components you can attribute blame to.
Your Glorious Code -> Java Compiler -> JVM -> JVM Compiler -> Operating System -> Operating System Compiler -> Hardware Software -> Hardware Software Compiler -> Hardware
This is even easier when you are in the “cloud”. You have a few additional layers to attribute blame to.
Undermining Managers
Reading into Reports.
If your manager is worth squat they will be pulling reports from somewhere about bug counts, test coverage, tests run, successful test, successful builds etc… game them. Ensure to mark all bugs as requirement or process issues. Most bug trackers don’t report via email closed issues. Update them after the fact to obscure the cause to something unrelated to the tests.
The best part is that if they use these reports to measure performance you can game them. Open and Close 50 bug tickets a day and outperform everyone by a mile. Whatever tool you are using to track this likely has an API. You can single handedly become the most important person on every available metric if you get creative.
Creating Diversions and Ruining Work-flows
Introducing subtle bugs.
Read the art of writing unmaintainable code. Apply it. This will not only make things harder to fix ensuring you have a job for life but also make writing tests after the fact impossible for the double whammy. The harder the code is to maintain the harder it is to add tests. Be creative when doing this! A personal favorite,
for(int j=0;j<array_len;j+=8){
  total += array[j+0];
  total += array[j+1];
  total += array[j+2]; /*Main body of
  total += array[j+3];* loop is unrolled
  total += array[j+4];  *for greater speed.
  total += array[j+5];*/
  total += array[j+6];
  total += array[j+7];
}
Are you able to spot the issue with this code?
Some users will use use syntax highlighters (the fools!) which may defeat the above. However ALL syntax highlighters have weaknesses. With some creative code you can trick the highlighter, and leave your bug hidden.
Remember to double down on something like the above. Write MANY unit tests which test the code but do not find the bug. Use this as ammunition later when it is discovered. Point out that following the process did nothing, and you spent all your time writing tests rather then actually testing anything.
This is unlikely, but if you code ever does fail (someone else’s fault of course!) remember to swallow the error and if you are forced to report on it use a message such as
"Error: Something went wrong ¯\_(ツ)_/¯"
. Never ever return or print the stack trace. Also be sure to reuse the error as much as possible, with slight variations. For example,
"Error: Something went wrong ¯\_(ツ)_/¯"
"Error: Soemthing went wrong ¯\_(ツ)_/¯"
"Error Something went wrong ¯\_(ツ)_/¯"
"Error: Something went wrong ¯_(ツ)_/¯"
"Error: Something went wong ¯\_(ツ)_/¯"
Use the above randomly through your code to really make it hard to track things down. If you really want to help with this use emoji and other character sets that editors and terminals have issues with.
HANDY TIP:
iTerm and Terminal on macOS have issues with displaying a lot of characters such as those in the
https://github.com/minimaxir/big-list-of-naughty-strings/
so be sure to include those in your errors and test suites to crash your fellow developers terminals!
Some argue that the above is too easy to search for using your code search tool of choice. Keep in mind these should appear in every possible file for best effect. If however you have a smaller codebase you may want to try spitting out an empty string or the same string for every error, where the same string is something very simple such as the below.
Test Failing? Delete it
If you ever find a failing test delete it. You are a 10x developer and don’t have time to fix other peoples dodgy code. Make sure to mention that it was flaky or no longer relevant in the commit comment. Make sure at any stand up or meeting you point out how much of a hero you are for cleaning up other peoples mess. Challenge anyone who suggests otherwise by asking what they have fixed recently.
If you get pushed for details then start muting the tests. This can usually be done inside your CI system or in the code itself. A mixture of both is the best solution especially if the tests are in the same file. Remember that you want someone to look in many places to diagnose any issue and determine why a test did not capture the failure. Make it as hard as possible to debug as you can. You want to have an incentive for others to delete and mute tests themselves.
Keep track of the number of muted and deleted tests. When it reaches some threshold you can use that as an argument to drop them totally.
Introducing Unreliability
So the team has pushed ahead, and nothing is working. Your new position is to make the tests unreliable. Then you want to expand out and point out that if the goal is to have 100% reliable code you need 100% test coverage. This sounds counter intuitive and against your goal, but you have to remember that its not an easy metric to get. It will cost a lot of time, slow development down and more importantly introduce flaky tests.
Arguments to achieve this are,
The goal is to have 100% reliable code
therefore
If our goal is 100% reliable why do we shoot for less than 100% test coverage?
leading to a test suite that is unreliable
If they are unreliable why even have them?
and
If we have tests why do we still have bugs?
How to write flaky tests
Flaky tests undermine confidence in the test suite and will result in the tests being muted or ignored. Either way you win. Leave temp files around, connections open, forked processes running and generally anything you can think of that will introduce failure conditions into your tests.
The best flaky tests however are those that fail apparently randomly, and never repeat themselves.
Take the following example,
def
writeheartbeat
():
file
=
open(
'/tmp/website_heartbeat.txt'
,
'w+'
)
file
.
writelines(str(datetime
.
now()))
f
.
close()
And the corresponding tests
def
testheatbeatmissing
():
exists
=
os
.
path
.
isfile(
'/tmp/website_heartbeat.txt'
)
assertFalse(exists)
def
testheatbeatexists
():
writeheartbeat()
exists
=
os
.
path
.
isfile(
'/tmp/website_heartbeat.txt'
)
assertTrue(exists)
The problem with the above is simple. Assuming the tests run in order everything should be fine for the first test run. However on the second run the first test will assume that the heartbeat file will be missing, however as it would have been created from the previous run this test will now begin to fail! Better yet, if the tests run out of order or someone reorganizes them such that the second becomes the first it will start to fail every time. Even if you introduce a clean up task to delete the file if that ever fails perhaps you left the file handle open? You will have a flaky test. Be creative with this! The more external dependencies you have the harder it will be to test correctly.
Also note that the above is written to only work on unix style operating systems. This is another advantage you can use! Write some tests so they are unix specific, then in another file write them to be windows specific. If challenged point out that you use X in production so the tests should be specific to that, and when the other style is picked up mention landing a contract with a new customer who uses the other OS.
For further marks have another test which changes the permissions of the file, or better yet multiple. Remove write access. Change the owner. Make the file immutable. Attempt to rename it to reserved windows file names such as CON. All of which will cause random fails after multiple runs.
If you have concurrent code then launch concurrent tests. These Heisenbug’s are your greatest ally in creating a flaky test suite.
HANDY TIP:
The use of docker and other container layers in CI/CD allows you to get really creative. Build a layer that adds 3000 new users and watch the image size blow up to hundreds of gigabytes which will likely crash the build agent. Say you were testing how the application performs when running against files with multiple owners.
What not to test
If you are forced to write tests you can start by being selective. Tests for setters and getters not only make you
look good from a metrics point of view, but for dynamic languages you can go to town testing all sorts of stuff. Be sure that your method expecting an integer fails gracefully when passed an array. With a little creativity you can auto generate most of these. For everything else follow the following rules.
Never test any error case because your code is naturally error free
Never test return codes because it never happens and slows the test suite down
Never test anything that requires you to mock. After all mocking is the work of the devil and a anti-pattern.
Only test for success under ideal situations. You code is a perfect snowflake.
Only write integration tests and make them as flaky as possible to further your cause. See how to write flaky tests.
List of Generic Fall-back Excuses
For any piece of code the following excuses are usually applicable. Feel free to use any at random or in order. Remember to cycle though them over time to avoid your excuses being picked up.
The code is too complex to unit test.
The code is too simple to unit test.
There’s no point unit testing code that doesn’t change.
This is a destructive process, so it cannot be unit tested.
Unit tests won’t tell me if this code actually works.
That code is side effect free so there is no need to test it.
It would be too slow to test that code due to the dependencies.
I can test this more quickly manually.
The client is paying for a deliverable not unit tests.
Thats QA’s problem.
Unit tests are just assertions in disguise.
Unit testing was a staple of the FORTRAN days.
Unit testing is not about finding bugs.
Measuring programming progress by lines of code is like measuring aircraft building progress by weight. - Bill Gates
There is an exception to every rule, and we must of course be flexible.
Never ascribe to malice, that which can be explained by incompetence. - Napoleon
Testing is for communists.
Unit tests cause autism.
I am the only developer on the project.
It’s an internal only tool.
The sole user of this is me.
Unit tests are anti-agile.
HANDY TIP:
Lead the narrative. If you challenge other peoples test writing using the above, not only are you not writing tests but you will be seen as the test expert without doing anything.
