---
title: "Debugging on Prod"
url: "https://idiallo.com/blog/debugging-on-prod"
fetched_at: 2026-06-17T07:01:20.854732+00:00
source: "idiallo.com"
tags: [blog, raw]
---

# Debugging on Prod

Source: https://idiallo.com/blog/debugging-on-prod

The worst type of bug is one that only happens on prod. And only on prod. If you checked this blog in the past few weeks, you might have encountered a big fat 500 error.
I'd had the same design for 10 years, and I wanted something fresh. But who can redesign without also improving the underlying code? I deleted a whole bunch of things: old templates that were never used,
post.new7.old.php
, a pile of unused CSS. I just had to.
I deployed a first version and all the pages worked just fine. But then I got cocky. I decided to also improve the underlying code using GitHub Copilot. I was vigilant at first, reviewing every single line of generated code. None of it was complex really, just refactoring functions and the like. But along the way, I got lazy. I let the AI update deprecated functions on its own.
The next time I deployed, the website returned a 500 error. When I checked the logs, nothing came back. No errors. I looked at running processes and noticed several PHP processes pinned at 100%. I reverted the code, but the server was still stuck. I restarted the web server, restarted PHP-FPM, and neither helped. The only thing that worked was restarting the whole machine.
I ran the same code on my own machine and it worked fine. That's when I noticed I was running an older version of PHP on prod: PHP 8.3 vs. PHP 8.4 locally. No problem, I thought, and upgraded prod, which of course failed to fix anything. I waited for nighttime, redeployed the broken code, and debugged line by line until I found that Copilot had gone out of its way to "update" code in the Markdown library I use. If you know anything about Markdown, you know it's complex. This particular change was causing infinite recursion while parsing Markdown. I had no intention of reading through all that code to figure out exactly how it was failing, so I just reverted it.
I redeployed and the problem seemed solved. Then I got an email: "Your website is down," a reader wrote in the middle of the night. While my American readers are asleep, Europeans are up bright and early reading my blog, for some reason (thank you, really).
So debugging live on production was not an option. I reverted to the old code again. But how was the website still failing after I'd fixed the Markdown issue? And worse, it still worked fine locally. Just in case, I upgraded that very old Markdown library to something cooler and more modern:
Parsedown
.
That didn't solve it either. The moment I deployed, the entire website failed, including pages that don't even use Markdown. Now it was personal. How do you debug a website that only fails in prod? I had a few tricks up my sleeve.
First, I wrote a bash script to quickly switch between versions of the website. All it really did was flip a symlink between the "latest" folder and another folder I chose arbitrarily.
> ln -s /path/to/latest/working/version current
> ln -s /path/to/selected/version current
Since I run PHP and every request is short-lived, I could switch to the broken version, debug, then switch back to the working version almost instantly. It's not like I have millions of readers hammering my server.
This method worked, but it was slow, and it exposed internal information to the thousands of RSS readers scouring my website. Between 30,000 and 60,000 RSS reader requests hit the site daily. I couldn't afford to expose debugging code to that much traffic.
So I used a second method: an even better way to debug live on prod without breaking URLs or throwing 500 errors at unsuspecting RSS readers. What if I ran both versions of the site simultaneously? Visit the regular domain and you'd get the latest working version. Visit a custom subdomain and you'd get the broken version.
I achieved this by creating a new Apache configuration pointing to the latest (broken) path. This way, I had all the time in the world to debug the issue right on prod, without interfering with regular traffic.
I eventually found the root cause. It was an orchestrated failure. Locally, I ran PHP directly. On prod, I ran PHP-FPM. Why the difference? Because Apache on prod runs HTTP/2 that requires an SSL connection, which I didn't need locally, and serving PHP over HTTP/2 requires PHP-FPM. PHP-FPM is essentially a process manager for your PHP instances. That explained the difference between the two setups, but not the actual cause of the bug.
The real issue was in my caching mechanism. When a page is served from cache, I set the header:
X-FROM-CACHE: 1
That's just a custom header. When the page isn't from cache, I set the value to
0
. Here's the code that sets the headers:
public function process() {
    foreach ($this->header as $key => $value) {
        if (!empty($value)) {
            header("$key: $value");
        } else {
            header("$key");
        }
    }
}
Now, what can go wrong here? When a page isn't served from cache,
$value
is set to
0
. You see it now, don't you?
0 == empty()
evaluates to
true
in PHP. So whenever a page wasn't served from cache, or the first time a page was hit after a deployment cleared the cache, this code ran instead:
header("X-FROM-CACHE");
That's an invalid header. So why did it fail on prod but not locally? Because Apache silently ignores invalid headers, but PHP-FPM doesn't. It throws a 500 error:
malformed header from script 'index.php': Bad header:
Error parsing script headers
AH01075: Error dispatching request to :
Headers need to follow the key-value rules defined in the internet standards (RFC 9110). Removing the condition and always using
header("$key: $value")
solved the problem.
The blog engine runs on multiple machines I own locally. I never had to worry about the setup because both apache and php are tolerant to mistakes. In a talk, Rasmus Lerdorf once said that PHP works better when you don't know what you are doing. The header condition has its uses. For example, if you want to set that a page is 404 you can return:
header("HTTP/1.0 404 Not Found");
But I don't use this in my case. While copilot was of some help, it's a reminder that LLM generated code is to be treated with scrutiny. It reinforces my belief that I can never
truly become a 10x engineer
, because the more code I generate the more I have to review. And the more I trust it, the more likely it will bite my behind.
