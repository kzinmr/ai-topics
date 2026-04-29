---
title: "The Software Essays that Shaped Me"
url: "https://refactoringenglish.com/blog/software-essays-that-shaped-me/"
fetched_at: 2026-04-29T07:01:22.372300+00:00
source: "refactoringenglish.com"
tags: [blog, raw]
---

# The Software Essays that Shaped Me

Source: https://refactoringenglish.com/blog/software-essays-that-shaped-me/

I started reading software blogs before I got my first programming job 20 years ago. At this point, I’ve read thousands of blog posts and essays about software, but only a small handful stuck in my mind and changed the way I think.
“The Joel Test: 12 Steps to Better Code” by Joel Spolsky (2000)
“Parse, don’t validate” by Alexis King (2019)
“No Silver Bullet - Essence and Accident in Software Engineering” by Fred Brooks (1986)
“Choices” by Joel Spolsky (2000)
“Application compatibility layers are there for the customer, not for the program” by Raymond Chen (2010)
“Don’t Put Logic in Tests” by Erik Kuefler (2014)
“A little bit of plain Javascript can do a lot” by Julia Evans (2020)
“Choose Boring Technology” by Dan McKinley (2015)
“I’ve locked myself out of my digital life” by Terence Eden (2022)
Bonus: Brad Fitzpatrick on parsing user input (2009)
Joel Spolsky is the greatest software blogger of all time. His essays have informed so much of my approach to software that it was hard to pick out just one, but “The Joel Test” is my favorite.
The Joel Test is a set of 12 questions that employers can ask themselves to see how well they’re investing in their software team:
Do you use source control?
Can you make a build in one step?
Do you make daily builds?
Do you have a bug database?
Do you fix bugs before writing new code?
Do you have an up-to-date schedule?
Do you have a spec?
Do programmers have quiet working conditions?
Do you use the best tools money can buy?
Do you have testers?
Do new candidates write code during their interview?
Do you do hallway usability testing?
Some of the questions are dated, but the point was never the questions themselves but rather the meta-point of the questions.
Joel was really asking employers:
do you respect developers?
The questions all assess whether an employer prioritizes their developers’ time and focus over things like cheap office space and short-term deadlines.
Joel published this article at the height of the dot-com boom, when skilled developers were a precious resource, but not everyone realized it, including developers themselves.
Joel’s blog always presented programmers as rare, delicate geniuses that employers needed to pursue and pamper. I liked that.
Throughout my career, I sought out employers that scored well on the Joel test, and I’m grateful to Joel for giving me the map to find them.
This essay is about leveraging the type system in Haskell to — wait, wait! Don’t go to sleep.
If you don’t care about type systems or Haskell, I get it. I don’t either. But this essay radically changed the way I think about software. You can use Alexis’ technique outside of Haskell in any language that supports static types (e.g., Go, C++, Rust).
The highly abridged version of the essay is that whenever you validate any data, you should convert it to a new type.
Suppose that your app has a rule limiting usernames to a maximum of 20 alphanumeric characters. The naïve solution would be to define a function that looks like this:
func
validateUsername
(username
string
)
error
{ ... }
With the above function, you run
validateUsername
anytime you receive a username from a user.
The problem with this approach is that your code is unsafe by default. You have to remember to validate every username you receive, so it’s easy to create a code path that accidentally processes a username without validating it. If a nefarious user notices the mistake, they can do tricky things like embed malicious code in the username field or stuff it with a billion characters to exhaust server resources.
Alexis’ solution is to instead use a function like this:
func
parseUsername
(raw
string
) (Username,
error
) { ... }
In the rest of your codebase, instead of passing around a
string
called “username,” you use a custom type:
Username
. The only function that can create a
Username
is
parseUsername
, and it applies validation rules before returning a
Username
instance.
Therefore, if you have a
Username
instance, it must contain a valid username. Otherwise, it couldn’t exist.
You can’t forget to validate a username because untrusted input will always be a
string
, and you can’t pass a
string
to a function that expects a
Username
.
Before Alexis’ essay, I thought type systems were just a fun way to distract language nerds. “Parse, don’t validate” opened my eyes to how valuable compiler features can be in improving an application’s security and reliability.
In college, I read
The Mythical Man-Month
, a collection of essays about software engineering by Fred Brooks, drawing on his experience directing
IBM’s OS/360 project
.
The essays were hit or miss. Some felt too old to be relevant, even in 2002, but the one that stuck with me was, “No Silver Bullet.”
The essay argues that you can divide software work into two categories: essential complexity and accidental complexity.
Essential complexity
is the work that you absolutely have to do, regardless of your tooling and hardware. For example, if you write software that calculates bonuses for salespeople, you have to define formulas for those bonuses and cover all possible edge cases. This work is the same if you have a $5B supercomputer or a $1 microcontroller.
Accidental complexity
is everything else: dealing with memory leaks, waiting for your code to compile, figuring out how to use a third-party library. The better your tooling and hardware resources, the less time you spend on accidental complexity.
Given this model, Brooks concluded that it was impossible for any advancement in tooling or hardware to create a 10x improvement in developer productivity:
How much of what software engineers now do is still devoted to the accidental, as opposed to the essential? Unless it is more than 9/10 of all effort, shrinking all the accidental activities to zero time will not give an order of magnitude improvement.
Throughout my career, people have been trying to find ways to eliminate programmers from software. For a few years, no-code platforms generated buzz by promising non-programmers all the powers of a seasoned web developer.
Brooks’ essay always reassured me that the latest buzzword platforms could never replace developers, as the platforms focused on the accidental, not the essential. Even if the platforms could magically create working code from a functional specification, you still need someone to write the spec:
I believe the hard part of building software to be the specification, design, and testing of this conceptual construct, not the labor of representing it and testing the fidelity of the representation.
Modern AI has thrown a wrench into Brooks’ theory, as it actually
does
reduce essential complexity. You can hand AI an incomplete or contradictory specification, and the AI will fill in the gaps by cribbing from similar specifications.
Even if AI eliminates programming as we know it, Brooks’ essay gives me hope that we’ll still need people to manage essential complexity at whatever level of abstraction that ends up being.
“Choices”
by Joel Spolsky (2000)
🔗
I said
above
that it was hard to pick a single favorite Joel Spolsky essay, which is why I’ve chosen two.
“Choices” is about creating user interfaces and the subtle costs of giving a user power:
Every time you provide an option, you’re asking the user to make a decision.
That means they will have to think about something and decide about it. It’s not necessarily a bad thing, but, in general, you should always try to minimize the number of decisions that people have to make.
As an example, Joel shares a ridiculous dialog that appears in Windows 98 when you try to search the help documentation:
The dialog infuriates Joel because it interrupts the user while they’re trying to get help, and it asks them to make an uninformed decision about database optimization. Windows was shirking a decision and pushing it onto the user.
Joel’s essay focuses on graphical user interfaces, but I think about it wherever people might encounter my code, including on the command-line or other developers calling functions I wrote. Can I make a useful decision on my user’s behalf while still giving them power over things they care about? There are countless times where Joel’s essay has saved me from pushing a decision onto the user that I could make myself.
Raymond Chen is one of the longest-serving developers on the Microsoft Windows team. His blog has thousands of informative, entertaining stories about the history of Windows programming, but the one I think back to most is one about compatibility mode in Windows Vista.
A customer had contacted Raymond’s team with this request:
Hi, we have a program that was originally designed for Windows XP and Windows Server 2003, but we found that it runs into difficulties on Windows Vista. We’ve found that if we set the program into Windows XP compatibility mode, then the program runs fine on Windows Vista. What changes do we need to make to our installer so that when the user runs it on Windows Vista, it automatically runs in Windows XP compatibility mode?
Raymond proceeds to characterize the customer’s request as follows:
I normally toss my garbage on the sidewalk in front of the pet store, and every morning, when they open up, somebody sweeps up the garbage and tosses it into the trash. But the pet store isn’t open on Sundays, so on Sundays, the garbage just sits there. How can I get the pet store to open on Sundays, too?
I loved this analogy. The metaphor was so funny that I didn’t notice until just now that Raymond is in the wrong. He’s making fun of a developer whose sin is expecting Windows not to break their app after a single release.
But as is the case with a lot of Raymond Chen’s writing, it’s so funny and sharp that I can look past the flaws.
Even though I disagree with the specifics, Raymond’s post is an excellent lesson in influencing user behavior.
If you want to nudge the user to do something that helps you, think carefully about the path of least resistance from the user’s perspective, because that’s the path they’ll take.
If you show the user that dumping garbage on the sidewalk completely solves their problem, they’re going to keep dumping their garbage on the sidewalk.
I’ve always loved unit testing and took great pride in my test code. That’s why I was so horrified when this essay
appeared in my bathroom
and revealed that I’d been writing awful tests my whole career.
Erik’s essay shows the following unit test, which has a subtle bug:
@Test
public
void
shouldNavigateToPhotosPage
() {
String baseUrl =
"http://plus.google.com/"
;
Navigator nav =
new
Navigator(baseUrl);
nav.goToPhotosPage();
assertEquals(baseUrl +
"/u/0/photos"
, nav.getCurrentUrl());
}
When I first read the essay, I thought, “That’s exactly how I write unit tests!”
Why duplicate the
http://plus.google.com/
string in two places? Create a single source of truth, just like in production code. I did this all the time, adding helper functions, variables, and loops to eliminate redundancy from my tests.
The problem with the approach above is that it masks a subtle bug. It’s actually asserting that the URL looks like this:
http://plus.google.com//u/0/photos
^^
whoops
Erik’s essay showed me that I shouldn’t treat test code like production code at all. The two have
completely different goals and constraints
.
Good test code should be, above all, clear. Test code doesn’t have its own test code, so the only way to verify correctness is by inspection. A test should make it blindingly obvious to the reader what behavior it asserts. In service of that goal, you can accept redundancy to reduce complexity.
As a software engineer, I was embarrassingly late to the web. For the first 10 years of my career, I only wrote code for desktop apps and backend servers. I never bothered with HTML or JavaScript until 2017.
By the time I got serious about learning frontend development, my impression was that JavaScript was a mess of a language,
hacked together in 10 days
, and it had drastically different behavior in different browsers. If I was going to write web apps, I wanted something modern and sleek to protect me from all of JavaScript’s bile and warts.
So, I tried the popular web frameworks of the day: Angular, React, and Vue. I learned enough Vue to make my way around, but I was still spending an enormous amount of my time on dependency issues and framework gotchas. After all the work these frontend frameworks did to fix JavaScript, web programming still sucked.
Then, I read Julia’s essay and realized I’d been so confident that JavaScript needed fixing that I never gave it a chance.
At the time, I was working on
the prototype of TinyPilot
, which would become my first commercially successful software product. TinyPilot had a web interface that I was planning to implement with Vue, but Julia’s essay inspired me to see how far I could go with plain JavaScript. No framework, no wrapper libraries, no build step, no Node.js, just regular old JavaScript. Okay, not “old” — more like
ES2018
, but you know.
I kept expecting to hit some problem where I’d need to switch to some kind of framework or builder, but it never happened. There were still some gotchas, especially around WebComponents, but it was nothing compared to the suffering I endured with Vue and Angular.
I loved being free of the frameworks. When I had a runtime error, the stack trace wasn’t some minified, transmogrified, tree-shakified fever dream of my code. I was debugging
my code
, exactly as I wrote it. Why hadn’t I tried this sooner?
My biases about JavaScript were wrong. Modern JavaScript is pretty nice. It absorbed a lot of ideas from wrapper libraries, so now you don’t need the wrappers. And browsers got their act together to ensure consistent behavior across platforms and devices.
I haven’t integrated a JavaScript framework or build step into any new project since 2020, and I’ve never looked back. Plain JavaScript gets me 90% of the benefit of frameworks with 5% of the headache.
This is an odd essay to include in this list because I’ve never actually read it.
People have quoted this essay to me, and once I understood the idea, it felt so intuitive that I didn’t need to read it. In my interview with
CoRecursive podcast
host Adam Gordon Bell, he talked about how there are certain non-fiction books where, once you understand the idea,
all you need is the title
. “Choose Boring Technology” is that for me.
Dan’s argument is that when you start a new project, you’re tempted to use cutting-edge technology that has lots of buzz. Google just announced a new database that scales to exabytes, and it’s 40% faster than Postgres at 20% the cost. You’d be an idiot to use Postgres when this sexy new alternative is right there!
In practice, the new technology has bugs and weaknesses, but they’re not obvious to you yet; they’re not obvious to anyone yet. So, when you run into them, you’re stuck. Postgres has its issues, but after 30 years in the field, it has battle-tested solutions for any problem you’re likely to encounter.
Dan concedes that you should use new technologies sometimes but only strategically and in limited quantities. He suggests that every business gets three “innovation tokens” to spend. If you want a flashy new database, you’ll have to spend one of your tokens.
Dan’s essay dovetails naturally with Julia’s essay. I wish I’d read either of them before I wasted all that time with frontend frameworks.
Terence Eden is a delightful and eclectic technology blogger. He writes several new posts each week, but the one that impacted me the most was “I’ve locked myself out of my digital life.”
The article plays out what would happen if lightning struck Terence’s house and destroyed all of his possessions. He keeps his passwords to everything in a password manager, but if all his devices get destroyed, he can’t access his password manager. And he can’t fall back to hardware passkeys because those were in his house, too.
I always felt like I was pretty safe about my data because I store everything on redundant drives, and I have offsite backups on three continents with two vendors.
Terence’s post got me thinking about the many credible threats that could wipe out all of my devices simultaneously: fire, flood, electrical surge, criminal investigation. All of my data is encrypted with passwords that live in my head, so add to that list memory loss, incapacitation, or death.
Online services are bad at helping users recover from disaster. I use several services that assume it’s impossible for me to ever lose my phone, let alone my email account and every digital device in my possession.
Ever since I read Terence’s essay, I’ve been thinking more about which services and devices are critical to me, and how I could recover from a scenario like the one Terence described. The next time I bought a laptop, I set it up at the library to test whether I could recover access to my password manager and critical accounts without any of the devices in my house.
I still could do a better job at digital disaster preparedness, but Terence’s post always echoes in my head whenever I think about how to secure my devices and data. What if everything was suddenly destroyed?
Bonus: Brad Fitzpatrick on parsing user input (2009)
🔗
It’s technically not an essay, but there’s a quote from a software interview I constantly think about.
In 2009, as a result of
Joel Spolsky’s gushing review
, (yes, again with the Joel), I read
Coders at Work
, a collection of interviews with accomplished programmers.
Brad Fitzpatrick
, creator of
LiveJournal
and
Memcached
, appears in the book as one of the interviewees. He was only 28 years old at the time, the youngest programmer in the book and also the sweariest and most entertaining.
In response to a question about ethics in software engineering, Brad goes on an impassioned rant about input validation:
I would like to ask that everyone is consistent on their credit-card forms to like let me put in fucking spaces or hypens. Computers are good at removing that shit. Like don’t tell me how to format my numbers.
-Brad Fitzpatrick, in
Coders at Work
I think back to this quote whenever I try to paste a phone number into a web form, and it whines that parentheses or spaces aren’t allowed. Or worse, it truncates my phone number because of the parentheses, and
also
complains that parentheses aren’t allowed.
Whenever I create input fields in my software and think about unexpected characters, I hear Brad Fitzpatrick say, “Computers are good at removing that shit.”
