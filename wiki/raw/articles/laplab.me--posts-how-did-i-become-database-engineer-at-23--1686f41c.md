---
title: "How Did I Become Database Engineer at 23"
url: "https://laplab.me/posts/how-did-i-become-database-engineer-at-23/"
fetched_at: 2026-05-05T07:01:24.597926+00:00
source: "Nikita Lapkov (laplab)"
tags: [blog, raw]
---

# How Did I Become Database Engineer at 23

Source: https://laplab.me/posts/how-did-i-become-database-engineer-at-23/

Disclaimer:
When reading this post, please keep in mind that you are likely to come from a very different cultural background than me. Russians approach life in their own way and some things might seem strange. Still, this was my path and I would like to share it.
My name is Nikita, I am 23 years old Software Engineer working on query execution at MongoDB. I would like to share how I ended up here. This is the first time I write post with personal information online, so things feel kinda strange. Let’s go!
How I got interested in programming
The year is 2013. I am 14 years old, studying in the 8th grade at school. My father and I are walking around the school building, talking about stuff. During our conversation, dad tells me that there is a new elective course opening up at school teaching basic programming and asks if I would like to try it out. I had no idea what programming is at the moment. My computer knowledge was just enough to browse internet and open “StarCraft II: Wings of Liberty” on my laptop. My dad told me that I can just try a few lessons and drop out if I do not like it. I agreed not suspecting how significantly my life will change because of this decision.
The elective course turned out to be training students to participate in programming contests called olympiads. Olympiad movement among school students is
huge
in Russia. There is an olympiad for almost every school subject: physics, maths, programming, biology, geography, you name it. The most prestigious olympiads are organised by government, but there are also quite a few olympiads organised by universities and private people. The main reason students participate in olympiads is to get fast track into university. Each university decides which olympiads they accept, giving the winners of these olympiads a chance to apply without making 100/100 score at the state exams. This way, universities get top talent and school students get a chance to stand out of enourmous competition of people applying through state exams. So not only this elective course would introduce me to programming, but it would also tremendously increase my chances of getting into the best universities in the country.
Me with a medal from one of the olympiads.
Programming olympiads in Russia usually mean that each student is assigned to a restricted computer with IDE, compiler, browser and nothing else. Then students would be given 4-5 hours to solve 4-6 coding tasks. In terms of Leetcode, it would be something like 1 “Easy” task, 2-4 “Medium” tasks and 1-2 “Hard” tasks. For each of them, student must submit code into the testing system, which would run it against a hidden set of tests and report “PASS” (+100 points) or “FAIL” (0 points). Some tasks would accept partial solutions, meaning that you can get 50 points out of 100 for solving only a simple case of the task.
Since students have no idea which tasks will be given in advance, we studied a bunch of generic algorithms at my school’s elective course and solved some tasks to learn how to apply these algorithms. Boy, did I suck at it. I was the youngest student in my group. Each other student would not only be older, but also have quite good training from math olympiads. These classes were a very humbling experience for me because I was top of my class at every other school subject. But every time I would come to this programming course, I would just hit a brick wall.
There was one thing I was better at than my classmates, though. It was
coding
the tasks. Coming up with the algorithm was very hard, but as soon as I understood what needs to be done, the code would just naturally come to me. I knew exactly when to use
std::vector
,
std::map
or
std::unordered_set
and what time complexities they would give me. At the team programming contests (where students solve tasks in teams of 3), I was always the one writing the code.
Year 2014, my team after one of the programming contests (I am second from the right). We have each won Amazon Kindle Paperwhite, the device I use to this day.
15 years old web developer
2014 was a crazy year for me. I won a contest from Google, participated in my first hackathon and got my first freelance job. But let me tell this story in order.
Learning web development
Back in 2013, when I was just starting with competitive programming, one of my school teachers asked me if I want to try to build websites. I had absolutely zero knowledge of web technologies, but this idea got my interest. I googled random HTML tutorial website (thank you,
wisdomweb.ru
!) and written a one-line HTML page. I have opened this page in the browser and there it was, “Hello world!” with “world” in bold. My mind was blown away by how easy it was and how you can instantly see the result. Unlike programming contests, you do not need to spend 2 hours coding your algorithm just to see “PASS” in the testing system. I finished the rest of the HTML course in less than 1 week.
I moved on to CSS and JavaScript courses. Everything was so intuitive and easy after C++ and algorithms, I just could not stop myself. My academic and programming contests performance was not great at the time, but I did not care. Then I moved to jQuery, my first JavaScript framework, and my mind was blown away once again. I would spend hours playing with JavaScript-backed animation methods, thinking about all cool websites I could create with it.
jQuery tutorial example I remember myself spending the most time on. The code makes the element fold and unfold, upwards and downwards. I found it very exciting at the time.
By the winter of 2013, I have finished all frontend courses on this website and it was time to move to the backend. I came to my elective course teacher with the ultimate question: Should I learn PHP or ASP.NET? My teacher suggested PHP and I immediately dived into it. My whole mind was completely occupied with web development. I would pay minimal possible attention to other lessons. During informatics lessons, I would be secretly reading PHP documentation and making websites instead of working on assignments. During my elective course, I would constantly talk to my classmates about how cool web technologies are.
In the beginning of 2014, I got my first pet project working. It was a web app using PHP, MySQL, Apache and jQuery that queried the testing system we used for practice in the elective course and displayed your progress charts. It was sending the requests using cURL and extracting data from HTML pages using RegEx. This was before I knew any kind of source control, so the code to this project is lost forever.
Up to this point I was writing all my projects without any particular structure. Extracting reusable code into functions and putting them into a separate file
utils.php
looked like the pinnacle of code organisation to me. This was until I learned three magic letters: MVC (model-view-controller). These three letters introduced me to the world of MVC frameworks, which separated data management, bussiness logic and HTML pages. It looked extremely complicated to me at the time, but very intriguing! I have learned my first PHP framework called
CodeIgniter
and once again, my world was blown away by how organised and natural the code felt in this model.
Contest from Google
There was a huge investment in Russian IT industry from Google in 2014. The company started “Forward with Google” campaign, which included a bunch of offline events stimulating interest in the industry. One of such events was a contest called “Digital Generation Google”. This was a nation-wide competition of “internet projects” made by school students. An “internet project” could be anything hosted on the web: YouTube channel, Tumblr blog, custom website, etc. Top 16 projects are selected by the jury to attend offline presentation event in Moscow, where one winner is choosen. The website for this contest is long gone, but there are some pages cached in the
web archive
.
Website of the competition. The title in Russian reads “You are lucky to be born in the age of the Internet!”. An interesting choice of words.
There was one ambitious project idea I wanted to implement for quite some time. In my math classes,
WolframAlpha
was quite a popular tool to help solving some non-trivial problems. In a lot of cases, WolframAlpha can straight up give you a solution to the calculus equation. If not, it usually highlights some interesting properties you did not see before. I did not like calculus, but I really liked geometry. How about I create WolframAlpha for geometry problems? I had this idea in my head for quite some time, so when my teachers came to me to suggest participating in Google’s contests, I immediately agreed and proposed my geometry project.
Now, the idea to create any kind of WolframAlpha clone is ambitious enough. Creating WolframAlpha clone for the field of spatial problems is even more ambitious, especially for 15 year old. What I am really grateful for to my math teachers is that when I pitched them this idea, they did not tell me it was impossible. They took me quite seriously and we discussed how the scope of the project can be reduced to actually make it until the submission deadline. In the end, we agreed that there will be some extremely basic syntax to describe geometry problems setups in terms of triangles and segments. Once the problem is described, system will try to find some very basic properties, such as which segments are equal to which and maybe some very basic derivation from that (like if triangle has two equal sides, the respective angles are also equal). A much smaller goal and much more realistic to achieve in a few months.
It was time to choose the technological stack. I picked the technologies I already knew to some extent: jQuery + HTML + CSS for frontend and PHP + CodeIgniter for backend. I also decided to write the “problem solving” part in PHP, where I used some very basic OOP techniques to abstract geometry concepts and RegExes to parse the problem description from the user. As I write it, this sounds like a mess, but I had no idea how to do things differently. I named my project “Geser”, after one of the characters of my favorite book at the time:
Night Watch
.
After a few months of hard work, the project was ready and I submitted it for jury evaluation. It was not even close to WolframAlpha in terms of functionality, but it looked pretty cool in the end and responded to some very basic problem statements. I was ecstatic that the Google itself would check out my very own website!
Photo of my entry to the contest from
web archive
. I thought that the owl looked pretty cool, so I tooked it as a logo from some random website.
A couple of weeks later I got a call from an unknown number:
[caller] Hi, is this Nikita Lapkov?
[me] Um, yeah, who is that?
[caller] Hey, my name is Dimitri, I am a software engineer from Google. Would you mind if we talk to you about your internet project?
Imagine how 15 year old feels when a guy from Google calls them. It turns out, they wanted to check that I was actually the guy who wrote the code. We discussed a bunch of technical stuff like which programming language did I use, how did I parse the user query, etc. After all the questions, Dimitri thanked me for my time and ended the call. My heart was pounding like hammer and I spent the next hour trying to process what just happened to me.
After some time, I got an email that my project was selected in the top 16 to be presented in the offline event in Moscow. This was
huge
for me. First of all, Google itself deemed my project worthy! Second of all, I was going to visit the capital! Third of all, I could be selected as a winner of the whole contest!
The offline event was pretty cool. Google rented a very fancy art space, invited a bunch of famous Russian bloggers and scientific writers as the jury. All 16 projects were presented by their makers and one was selected as the winner. Unfortunately, it was not my project, but there was a moment there, which I will remember for a long time. One of the jury was a journalist from Russian version of
Popular Mechanics
magazine. PopMech was my favourite technical-ish magazine at the time and I would see the name of this journalist under almost every cool article published there. After the winner was selected, he came to me and said: “You know, I voted for your project to be the winner.” This was the highest praise I could hope for.
The photo is a little bit all over the place, but I am the guy in a blue shirt on the right. Source:
Official Google Russia blog
First hackathon
I read a lot about hackathons happening in the capital and it was my dream to participate in one myself. 48 hours of non-stop coding without school interruptions - what more somebody could wish for? As a part of the same “With Google” campaign, Google organised a bunch of hackathons in different cities of Russia and it turned out that my home town, Krasnoyarsk, was on the list! This was really surprising because Krasnoyarsk had almost no technical events at the time and a hackathon from Google was a huge deal. I signed up and waited impatiently until the June of 2014.
The event itself was hosted in the hotel, where about 100 software developers would participate in the hackathon, guided by about 10 experts from Moscow. I was really intimidated when I arrived to the building. Most of the participants were 10 years older than me and got this “cool hacker” vibe about themselves. I was nervously going around rooms attempting to join one conversation group or another. There were even people wearing
Google Glass
, which looked like a cyberpunk gadget from the future at the time.
When it was time to do team building, I pitched myself to some guy who was proposing to do some retail website. The details of the product were really fuzzy for me and honestly I did not care. Before this, I was always working on my projects alone. It was the first time in my life I worked with other software developers on something together. I was really hyped and the whole 48 hours without sleep went like nothing for me.
Me pitching myself to my future team lead. I am the guy on the left. Source:
Hackathon website
.
My main area of expertise at the time was backend, but we already had a more experienced backend developer on the team. It was this time our team leader asked: “Remember these guys with Google Glass? How about we make an app for it?” Now, the retail app for Google Glass does not make any sense really, but I was excited to try out this cyberpunk technology! I spent the whole hackathon wrestling with Google APIs and in the end I even managed to get an order notification sent to the actual Google Glass. We made my app a part of our final presentation, where team leader would make an order in live and the notification would be sent to the linked Google Glass. Unfortunately, my code failed with exception during the presentation (of course it did). But hey - it was my first hackathon.
In the end, I was so happy I got a chance to participate in this event. I realised that I am not alone and that there is a community of like-minded people who also like to code. I got a glimpse of what the software development is in the wild and exchanged contacts with a bunch of folks. Also, people had “500 Server error” look on their faces when I said that I am 15 years old, which was really funny.
Me and my hackathon team. I am the guy in the grey jacket. Source:
Hackathon website
.
First contract
In the end of 2014, I had a problem with my smartphone. Previously, I asked my parents to buy me a Windows Phone, which was really hyped and seemed like a cool gadget to me at the time. After using it for a year I realised that my phone was getting slower with each day and what is worse, nobody was releasing any apps for it! I came to my parents to ask if they could buy me an Android instead. My father replied: “It was your choice to buy a Windows Phone a year ago. We cannot buy you a new smartphone every year. What we can do, however, is cover half of the cost of your next phone. The remaining half you need to earn yourself.” This was really annoying. I knew that I will need at least 12k rubles (somewhere around 200 euro / dollars) for a more or less decent Android phone. How on Earth am I supposed to earn this much at the age of 15?
I had some experience with web development in PHP at the time, so I decided to try and find a freelance job in this industry. I registered on the first freelance website I could find and filled out my profile. There were two form fields which I spent a lot of time thinking about - age and hour rate. It was clear to me that nobody would hire a 15 year old. Even 18 year old did not seem enough for my taste, so I entered 25 (which is kind of funny because I am still younger than that). The hour rate was also a tough one, since I have never put a price tag on my work. After much consideration, I decided to be bold and put a high rate of 250 rubles per hour (somewhere around 4 euro / dollar). The priced seemed too high to me at the time, but I decided that anything lower would require too much time to save for my new smartphone. The profile is done, now it is time to wait.
Screenshot from my freelance profile, cached in one of the search engines. “Nikita Lapkov, Backend developer” - has a ring to it, right? I remember I asked my father to take a “serious” picture of me for this, where I could look like a 25 year old. Given the image resolution, I think it worked.
A couple of weeks later I was messaged with a job offer! Some no-name construction company needed a fullstack developer to implement a web app for searching their product database. Basically, they had a MySQL database with some items and I needed to implement a PHP backend to perform very basic full-text search in two variants: (a) using MySQL
LIKE
statement; (b) using Sphinx index. I needed to also implement frontend with UI to query this backend.
I replied that I am interested and they asked me to visit their office to sign a contract. Now, this is the hard part. How do I convince some construction company that they can trust a school student to implement a production system? I came with this to my father and he offered to go there with me and try to talk them into it.
The construction company turned out to be 3 people sitting in some cubicle. They did not actually construct anything, they just kept a database of various construction materials from different providers. A search system was mainly for these 3 people to avoid using some SQL admin panel when searching for items. They were very surprised to see me as their future contractor, but overall the atmosphere at this meeting was very friendly. My father vouched for me and since this system was a low-risk quality of life improvement, they agreed to give this job to me. We agreed on me getting 5k rubles (somewhere around 80 euro / dollar) for implementing the whole thing.
I was able to finish the job in 2 weeks. In the end, I had a jQuery-backed frontend, which sent requests to the backend through AJAX, displaying loader gif while waiting for response. Backend was just querying MySQL and Sphinx index using their respective libraries and returned the results. My clients were very happy with the result and paid my fee in full. It was the first time in my life I earned money with my work. I felt very proud of myself.
Unfortunately, the company is not active anymore and they turned off their website, together with my search UI. But you can still find it in the
web archive
. It is funny to read the frontend code after all these years, containing comments like
// !!!
and ignoring code style half of the time.
Frontend of my search web application from the web archive. Attentive eye can notice Bootstrap v3.0 being used, which I though was the future of the web UI at the time.
Before we parted with my client, the head of the company asked me a question: “How can I motivate my grandson to work like you do? He is about your age and all he does is playing video games!” I did not find what to say to him at the time, but retrospectively I have an answer to this question: “Don’t.” Children should not be working at this age, they should be playing video games and enjoying their time with friends. By putting them into a situation where they need to grow faster than they normally would, you take away their childhood. Did I learn valuable skills and experience in the process? Sure. Was the cost for these skills justified? Absolutely not.
Next part
2014 sure was a loaded piece of toast. This post turned out to be quite large, so I will split it in two parts. Second part will be about how I got my first part-time job, went to the university and almost decided to go into Machine Learning research before getting into databases. Stay tuned!
