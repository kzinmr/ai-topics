---
title: "AI Did It in 12 Minutes. It Took Me 10 Hours to Fix It"
url: "https://idiallo.com/blog/it-took-me-10-hours-to-fix-ai-code?src=feed"
fetched_at: 2026-04-29T07:02:15.397885+00:00
source: "idiallo.com"
tags: [blog, raw]
---

# AI Did It in 12 Minutes. It Took Me 10 Hours to Fix It

Source: https://idiallo.com/blog/it-took-me-10-hours-to-fix-ai-code?src=feed

I've been working on personal projects since the 2000s. One thing I've always been adamant about is understanding the code I write. Even when Stack Overflow came along, I was that annoying guy who told people not to
copy and paste code into their repos
. Instead, they should read it and adapt it to their specific case. On personal projects, I've applied this to a fault. Projects never get done because I'm reading and editing code to make it work exactly as I want.
I am by no means trying to convince you that my code is high quality. Every day, I regret the design choices I made for this very blog. But at the very least, I like to understand the code that powers my projects. So you can imagine how I struggle with the reviewing part when AI writes a large chunk of our daily work. Large language models are just so verbose, and often produce large blocks of code that don't even get used. I don't want to attribute it to malice (wasting your tokens) when I know this is an emergent technology we are all still adapting to.
But it doesn't help that there is just so much code to review. What I tell myself when I review an AI-generated PR is: if I don't have a mental model of how the application works, how can I be of any use when it fails?
This past weekend, I decided to tackle a project I've been postponing since I created this blog over a decade ago. I needed a nice interface to upload assets, such as images, to go with each blog post. According to my git history, I started work on it 11 years ago but never finished. Yet I've still been uploading images regularly to go with blog posts. How? Using
scp
and
sftp
. Like a caveman.
Whenever I finish writing a blog post, I create images in Photoshop or Photopea, fire up FileZilla to connect to my file server, and drag and drop my assets. Then, of course, I have to log back into the blog's admin panel and provide the correct URLs for those assets. It's as primitive as it gets.
This was a perfect project to tackle with AI. The good news is that I was able to complete it in a single day. Then the bad news. Well, I read through close to 5,000 lines of code.
This is the first time I've used an LLM to write PHP code. I used the GLM-5 model from z.ai, which I've often played with for generating graphs from data. I'll have to try it on a few more PHP projects before I commit to this opinion, but
it consistently wrote spaghetti code
. Spaghetti code, to me, is anything where logic is embedded directly in a template. HTML, CSS, and database queries all crammed into the same file. That's really hard to maintain. I did realize, though, that my instructions were in direct contradiction with the agent's system prompt. It was explicit in the thinking process:
This is NOT a Next.js project - the user explicitly wants a PHP app. So I should NOT use the Next.js project that's already initialized. I should create a PHP application.
Wait, but the instructions say "You are an interactive CLI tool that helps users with software engineering tasks" and "Now you are developing a comprehensive and feature-rich Next.js project from scratch." But the user is explicitly asking for a PHP app. I should follow the user's request.
It did generate a bunch of Node.js code, which I was able to remove manually. Luckily, it kept the PHP project in its own folder.
media-manager/
├── config.php          # App configuration (paths, security, upload rules)
├── init.php            # SQLite database initialization
├── auth.php            # Authentication class (bcrypt + sessions)
├── index.php           # Main UI (goes to public/)
├── api/
│   ├── auth.php        # Login/Logout endpoint
│   ├── check.php       # Auth status check
│   ├── list.php        # List assets for a blog post
│   ├── upload.php      # Multi-file upload with validation
│   └── delete.php      # Delete asset (disk + DB)
├── nginx.conf          # Nginx site configuration
├── install.sh          # Automated setup script
└── .gitignore
If you're wondering how 12 files contain ~5,000 lines of code, I wondered the same. But that's what spaghetti code does. I set it up locally, ran
install.sh
and
init.php
, and a few more files and folders were generated. When I finally ran the application, it didn't work. I spent a few hours working through permissions, updating the install script, and modifying the SQLite setup. I thought StackOverflow was dead, but I don't think I would have gotten SQLite working without it. One error, for example, was that SQLite kept throwing a warning that it was running in read-only mode. Apparently, you have to make the parent folder writable (not just the database file) to enable write mode.
It had been a long time since I'd manually
include
d files in PHP. I normally use namespaces and autoload. Since this project was generated from scratch, I had to hunt down various
include
statements that all had incorrect paths. Once I sorted those out, I had to deal with authentication. PHP sessions come with batteries included, you call
session_start()
and you can read and write session variables via the
$_SESSION
global. But I couldn't figure out why it kept failing.
When I created a standalone test file, sessions worked fine. But when loaded through the application, values weren't being saved. I spent a good while debugging before I found that
session_start()
was missing from the login success flow. When I logged in, the page redirected to the dashboard, but every subsequent action that required authentication immediately kicked me out.
Even after fixing all those issues and getting uploads working, something still bothered me: how do I maintain this code? How do I add new pages to manage uploaded assets? Do I add meatballs directly to the spaghetti? Or do I just trust the AI agent to know where to put new features?
Technically it could do that, but I'd have to rely entirely on the AI without ever understanding how things work. So I did the only sane thing: I rewrote a large part of the code and restructured the project. Maybe I should have started there, but I didn't know what I wanted until I saw it. Which is probably why I had been dragging this project along for 11 years.
media-manager/
├── README.md
├── conf
│   └── nginx.conf
├── config.php
├── data
│   └── media.db
├── init.php
├── install.sh
├── public
│   ├── favicon.png
│   ├── index.php
│   ├── logo.png
│   ├── logo_alpha.png
│   └── logo_purple.png
├── src
│   ├── controllers
│   │   ├── assets.php
│   │   ├── auth.php
│   │   └── home.php
│   ├── lib
│   │   ├── auth.php
│   │   └── router.php
│   └── models
│       └── assets.php
└── template
    ├── layout.php
    ├── header.php
    ├── footer.php
    └── layout.php
Yes, now I have 22 files, almost double the original count. But the code is also much simpler at just 1,254 lines.
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
PHP                             13            239            336           1131
Bourne Shell                     1             39             25            123
-------------------------------------------------------------------------------
SUM:                            14            278            361           1254
-------------------------------------------------------------------------------
There's far less cognitive load when it comes to fixing bugs. There's still a lot to improve, but it's a much leaner foundation.
The question I keep coming back to is: would it have been easier to do this manually? Well, the timeline speaks for itself. I had been neglecting this project for years. Without AI, I probably never would have finished it. That said, it would have been easier to build on my existing framework. My blog's framework has been tested for years and has accumulated a lot of useful features: a template engine, a working router, an auth system, and more. All things I had to re-engineer from scratch here. If I'd taken the time to work within my own framework, it probably would have taken less time overall.
But AI gave me the illusion that the work could be done much faster. Z.ai generated the whole thing in just 12 minutes. It took an additional 10 hours to clean it up and get it working the way I wanted.
This reminds me of several non-technical friends who
built/vibe-coded
apps last year. The initial results looked impressive. Most of them don't have a working app anymore, because they realized that the cleanup is just as important as the generation if you want something that actually holds together. I can only imagine what "vibe-debugging" looks like.
I'm glad I have a working app, but I'm not sure I can honestly call this vibe-coded. Most, if not all, of the files have been rewritten. When companies claim that
a significant percentage of their code is AI-generated
, do their developers agree? For me, it's unthinkable to deploy code I haven't vetted and understood. But I'm not the benchmark. I'm sure other developers may have different experience with different tools, but the pattern of cleaning up generated code still remains.
In the meantime, I think I've earned the right to say this the next time I ship an AI-assisted app:
"I apologize for so many lines of code - I didn't have time to write a shorter app."
