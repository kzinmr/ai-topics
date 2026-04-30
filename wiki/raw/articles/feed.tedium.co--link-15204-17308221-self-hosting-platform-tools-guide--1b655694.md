---
title: "Still Worth Trying In 2026?"
url: "https://feed.tedium.co/link/15204/17308221/self-hosting-platform-tools-guide"
fetched_at: 2026-04-30T07:00:56.433734+00:00
source: "tedium.co"
tags: [blog, raw]
---

# Still Worth Trying In 2026?

Source: https://feed.tedium.co/link/15204/17308221/self-hosting-platform-tools-guide

Today in Tedium:
It’s a tough time to be a financially-conscious computer user. We’re living deep in a RAM crisis, and you’ve probably heard the stories about well-spec’ed computers slowly suffering from a nagging case of Unobtainium. Meanwhile, SaaS just keeps SaaSing, with costs adding up (and tech companies getting bigger) every month. In the past, my recommendation for working around SaaS involved buying a mini PC, loading it up with containers, and using those to get work done. But at a time when a 2-terabyte SSD costs 2.5 to 3 times what it did a year or two ago, does that advice still hold? And I’m a nerd—could it be a decent option for a regular user? With that in mind, I decided to dig in. Does turning a mini PC into a little home server make sense in 2026? Let’s find out, together.
— Ernie @ Tedium
The KAMRUI Hyper H1 Mini Gaming PC, which will help us live our self-hosting dreams today.
We’re reviewing a mini PC
and
diving into the self-hosting landscape. Here’s why
I’m a big fan of mini PCs,
especially of the Ryzen variety, because they are flexible and performant. Often, they are the same chips that appear in laptops (rather than cut-down chips, as seen in many Intel-based cheap desktops), and in a mini PC context, they have a pretty good cost-to-performance ratio.
My life essentially lives on a mini PC with a Ryzen 5600U which has never given me many problems. Really, my grievance is with the software. See, it stumbled into life as a desktop PC that gradually gained a ton of Docker containers, and I am in need of a reconfiguration of my setup. So when I got sent a mini PC for review, it was the perfect opportunity to rethink my self-hosted stack.
The unit I’m testing today is a mini PC from Kamrui called the
Hyper H1 Mini Gaming PC
, which packs 24 gigs of soldered, non-upgradeable RAM and a Ryzen 7 7735HS. (In normal times, soldered RAM would be a bad thing for a mini PC, but given the prices of RAM these days, it feels like a defensive measure.)
AMD’s naming has gotten a bit confusing in recent years, but the 54-watt
7735HS
is essentially the same as the slightly older
Ryzen 7 6800HS
, except with slightly higher headroom. It’s not top of the line, but nice enough.
There are some small quibbles, sure. The chip it’s rocking apparently has a nondescript “Radeon graphics,” which is what Windows calls it. (But on Linux, it self-reports as a Radeon 680M, a decent chip.) I didn’t test for gaming stuff, as it’s not my focus, but the chip is likely good enough for light to moderate games. I’ve tested similar machines in the past and found the 680M to be capable of running titles like the recent
Doom
games without breaking too much of a sweat. If you want a
Silksong
machine, this will more than do it.
While using the machine was overall painless, with half a dozen USB-A ports (take that Apple), I will point out an issue I ran into with its one USB-C port. I have a Thunderbolt dock that has a special chip that can dial down to USB 3.2 speeds, allowing the use of monitors and peripherals on machines without Thunderbolt. And it worked—sometimes. Depending on the OS I was using, the video would drop out randomly. Kamrui confirmed it was a 10GB port capable of display out, which means that a dock like this might give it trouble. But alas, worth a try.
I ran a couple of benchmarks on Windows to get a baseline, and it’s perfectly serviceable. Cinebench put its multicore performance squarely between an Intel Lunar Lake CPU and an Apple M3 processor. That’s not amazing, but for its use case, more than fine.
The use case in question? Self-hosting. For this piece, I’ll be analyzing three tools intended to make self-hosting approachable by more than nerds: Two fairly mature self-hosting distros, Umbrel and Unraid, and a buzzed-about front-end, HomeDock OS. For those playing at home: Umbrel has a slick Mac-like experience, while the similarly polished HomeDock sports a Windows-like interface. Unraid, meanwhile, is more of a standard server-management tool with a million knobs.
But in theory, all should do the same thing. Will they? To test this theory, I’m throwing four separate tests at these tools:
Set up the tool to support
Tailscale
,
a mesh-based secure networking tool, so I can access the machine when I’m out of the house, while preventing others from doing the same. (I’m not always home, and my stuff needs to be accessible; this is the best way I’ve found.)
Install an app from the platform’s app store,
preferably something that I already use and am familiar with, such as a blogging platform or productivity app.
Install an app using
Docker Compose
,
a relatively standard method for installing self-hosted software.
Install a local LLM tool,
because odds are that if you’re buying something for self-hosting with extra headroom like the Kamrui, you may want to dabble in that.
While not spoiling what I found out, I’ll note that being somewhat knowledgeable about self-hosting actually proved a liability in this review. Really.
Quick shout-out to a fave site:
If you’re looking to dig into the self-hosting space, Ethan Sholly’s
Selfh.st
is a great repository that helps the space make sense to normal people—while pointing out emerging trends. Can’t recommend it enough. (Not sponsored, by the way.)
Looks good, but …
Umbrel: From the kiddie pool to the deep end in record time
I wanted to like
Umbrel
more than I did, I think.
Visually, it looks sharp, and it feels like it’s going to be a really painless experience to get going. But the problem is, if you know too much about how self-hosting works before you jump into this, you start asking too many questions.
Among them: Why can’t I change the Docker Compose files without the app resetting that file every time there’s a new version? (What’s the point of even having Docker Compose if you’re just going to delete my tweaks?) Why is it so hard to give this thing https support? And why do you have to set up your own version of the platform’s app store to add your own apps?
That made Umbrel a bewildering experience for me. It’s designed for people who want different things from self-hosting than I do—like bitcoin lockers and Tor connections. It’s a weird dichotomy that speaks to the pages of confused comments I saw in help forums.
If your advanced settings menu has five options, you can’t call it advanced.
Umbrel’s interface starts shallow, but hides a deep learning curve. Its advanced settings page had just a handful of options, not letting you change common defaults but instead pushing you to the terminal for literally everything. As a result, I found myself increasingly frustrated with this otherwise polished tool.
My tests:
» Set up the tool to support Tailscale:
Easy enough to get going (the tool’s in the app store), but it’s unfortunately held back by Umbrel’s tendency to emphasize local access. The result is that you can install it, but with a lot of digging to figure out how to turn on https for the server. As I learned from looking at forums, many folks have been down this exact road before me, and some had given up. (For those who are lost: Use
tailscale serve
on every port you want to access remotely, adding https access as needed.)
Grade:
B-
» Install an app from the platform’s app store:
I chose
Solidtime
, a time-tracking tool that I’ve been leaning into lately. While a slick app, it does an unwittingly excellent job of highlighting the folly of Umbrel’s security approach. Essentially, the local domain is hard-coded into the environment variables used by Docker Compose, and because Solidtime is a Laravel app, you can’t easily change anything. (You have to go into the terminal to update variables, for example.) I ended up breaking the app because I changed my email address in the app, which caused Solidtime to freak out. Solidtime sends a verification email to confirm the change. However, I didn’t have an email set up—and there was no easy way to do so in the interface—so I was unable to log back in. Adding Tailscale to the mix only worsened the problem. If you’re going to offer it in your app store, make it easier to tweak under the hood.
Grade:
D
» Install an app using Docker Compose:
On the plus side, Umbrel does offer a route forward for this in the form of tools like Portainer and
Dockge
. These tools allow you to install and manage your own Docker containers relatively easily, even solving for the environment variable issues that I ran into with Solidtime. I installed Listmonk, an email tool I’ve been using, and in a matter of like five minutes, I had a working server, and a Tailscale command later, it had https. Problem is, this container is not visible to Umbrel, meaning you have to dig into a separate app to find it, sort of defeating the purpose of the clean interface. Overall though, this worked OK.
Grade:
B+
» Install a local LLM tool:
I was ready to try AI on this, raring to go, but … installing
OpenHands
somehow broke Umbrel’s networking entirely. After 45 minutes of troubleshooting, landing repeatedly on unanswered support threads, I don’t have the energy to figure out why it broke. Honestly, I think I’ve made my point.
Grade:
F
When it comes to self-hosting, simple is a trap. You want knobs and standard approaches that match what everyone else is doing. You don’t want to have to painstakingly rebuild your electrical system while the power is still on. Because if something breaks, your house goes up in flames. Umbrel, unfortunately, showed why knobs matter.
Ever wanted to read Tedium
without having those annoying ads all over the site? We have just the plan for you.
Sign up for a $3 monthly membership
on our Ko-Fi, and we promise we can get rid of them. We have the technology. And it beats an ad blocker. (Web-only for now, email coming soon!)
Of the three tools I tried, Unraid had by far the best app store.
Unraid: A hosting tool with knobs
I’ll be honest:
Unraid
is built for much more complex setups than a mini PC with a single drive. It encourages the use of drive formatting techniques like XFS and ZFS. And it doesn’t offer a friendly front page—though, if you want one of those, you can use a dashboard tool like
Homarr
or
Glance
.
But here’s the thing: Unlike Umbrel, it speaks roughly the same language as everything else. (Unraid’s been around for decades; it helped to define that language.) In other words, you are working with the tool, not against it. That leads to fewer fires thanks to robust documentation and a strong community.
The rub is that Unraid is not open-source, but its business model is still weekend-warrior friendly. You just need a $49 one-time license to keep your site going (with tiers that go up as you scale). That paid license comes with support that is likely to come in handy as you break things. Here’s how it went for me:
» Set up the tool to support Tailscale:
Unraid has a deep integration with Tailscale that makes it a great choice if you want as much flexibility as possible. There’s a learning curve—it is admittedly confusing sometimes to determine whether a particular container should have Tailscale off or on—but it’s made up for by the fact that Unraid can manage the tool with scripts. I created a cron tool to turn off ports if the server went offline and vice versa.
Grade:
B+
Hate YAML files for setting up your Docker images? Unraid’s config approach is a pretty nice antidote to that.
» Install an app from the platform’s app store:
I gave BentoPDF, a tool for manipulating everyone’s favorite file format, a spin. It is admittedly not a complex tool (I usually host it on my laptop), but it shows just how easy it is to get something like this set up. While I ran into some initial issues with Tailscale, they were easy to fix.
Grade:
A
» Install an app using Docker Compose:
So, Unraid doesn’t natively support Docker Compose, favoring actual containers instead. But it is more than capable of doing so using a plugin for the task. Case in point: My issues with Solidtime on Umbrel did not follow me to Unraid. I ran into some permissions issues with the folders I needed, and the .env format was a bit prescriptive (Solidtime wanted laravel.env, but I was limited to just .env), but I got it working—and in a much more stable setup than with Umbrel. It was work, but work that made you feel like you were learning something. Big difference.
Grade:
A-
To be fair, Deepseek-R1 has never seen a pizza.
» Install a local LLM tool:
For this one, I went with
Open WebUI
, which is one of the most popular tools of its kind, and downloaded Deepseek-R1 via an Ollama package. This is the part where more performant hardware matters. You’re not winning any land-speed records with this GPU, but Ollama can allocate roughly half the memory on this device (24GB) to the GPU, more than enough to run the 8 billon parameter DeepSeek models. My M1 with 16GB of RAM choked on this model, but this ran it fine once I added the right GPU variables.
Grade:
B
Overall, if you’re willing to pay—and more importantly, learn—Unraid is an excellent experience. And while it may not be built for a mini PC like this, it more than does the job.
Plus, if you want to, say, run a Linux install in a VM, it does the job pretty well.
Proxmox
, a similar tool that
focuses more on VMs
, is also good—but Unraid has a little more flexibility in the container direction. With Umbrel, you felt the limitations of the software right away. With Unraid, there’s still headroom.
9.8
A recent score
on the CVE (Common Vulnerabilities and Exposures) chart received by
ZimaOS
, an emerging commercial fork of the popular CasaOS. While it was
apparently fixed as of version 1.5.4
(I asked for comment from its creator Ice Whale, haven’t heard back), it’s worth pointing out that if Windows or iOS had a 9.8 CVE score on an exploit it would be a major news story. It’s as bad as you can get. As a rule of thumb: Dig around to learn about the security posture of the self-hosting tools you use. You don’t want to get surprised later on.
It’s like having a second OS that lives in your browser, complete with some of the apps you might want in a Linux desktop.
HomeDock OS: The desktop apps are interesting, but …
Honestly, if it was just me,
I would probably stop at Unraid and just move on with my Tailscale-simplified life. But this test needed more than just two entrants. So I dropped in another SSD and decided to install an app-based self-hosting tool that can be used on any distro.
That led me to
HomeDock OS
… which wasn’t the most fun choice for my particular setup.
The long and short of it is that the tool was not built to work with Tailscale. I could work around it (unlike Umbrel, HomeDock’s simply a Linux app), but it was a bit of a nightmare figuring that part out. I thought it was my distro. No, it was really some SSL drama that I eventually figured out with some purpose-built scripting.
It’s too bad, because HomeDock OS is a fascinating project—effectively an OS-like self-hosting experience, complete with windows, in your own browser. Unfortunately, I found myself having to navigate with SSL jank over and over. But unlike Umbrel, it was at least in the wheelhouse of what other tools do.
Eventually I figured it out, and found some interesting design decisions. I just wish it didn’t take me that long to get there.
Anyway, my tests:
» Set up the tool to support Tailscale:
HomeDock OS doesn’t take any steps to support Tailscale out of the box, which is fine if it can play nice with it—or, honestly, give me an https connection at all. And whew, that’s where it struggled. I was never able to get their suggested homedock.local default URL to work, so Tailscale became my best option. I will note that it also supports Wireguard, but that felt like a pretty significant reset as I dug in, so Tailscale it was. (The strategy: install Tailscale’s cert, set the default url to your Tailscale URL, and enable ports as needed.)
Grade:
D
Want to view a web browser inside your web browser? HomeDock can do this.
» Install an app from the platform’s app store:
The novelty of being able to install desktop apps in a self-hosting tool was pretty good, I must admit. (Unraid also had these, but HomeDock puts them front and center of a fairly small app store.) I can see the case for loading up Krita from inside a browser, especially if, say, you’re on a work machine; I’m less convinced about the value of a nested Chromium. But word of warning that you might run into problems with
Selkies
, the remote desktop it relies on. (Because of how my keyboard was set up, I couldn’t bold or italicize anything.) Promising, but needs more work. (A point in its favor: Setting up Syncthing, which isn’t a desktop app, was painless.)
Grade:
B-
» Install an app using Docker Compose:
The format on this is a little weird—you’re essentially importing Docker scripts into its proprietary format, which isn’t really that proprietary, really. Hey, still better than what Umbrel was doing. Honestly, I’d recommend using the supplied
Portainer
rather than building your own app store. You don’t get the nice icons, but you’ll actually get your container working in short order. That was how I got
Penpot
working in a matter of minutes.
Grade:
B-
» Install a local LLM tool:
Given how popular LLM stuff is with self-hosting these days, I admit to being slightly surprised that AI stuff wasn’t all over HomeDock. It had some apps, though, such as
Perplexica
, an open-source take on Perplexity that was recently renamed Vane. I didn’t get amazing results using Deepseek (the Wikipedia page on “
Why did the chicken cross the road?
” was more informative than its answer), but if you want this in your arsenal, it works. (One knock against it: The tool is not packaged with Ollama, requiring a knotty separate download which adds complexity. Save yourself some grief: Just set up Ollama on Portainer.)
Grade:
B-
This one was a bit of a journey, and there are some quirks and weaknesses. I might have skipped the interstitial page when loading an app, and some of Portainer’s functionality should be HomeDock itself. But if you can look past those, HomeDock OS has plenty of potential.
Would I use this over Unraid? No. But given the newness of the tool, less than a year old, it’s worth keeping an eye on.
So, this piece is basically a review of two separate things:
A mini PC and an ideal use case for that mini PC.
How does it check out? Put simply, I think the computer itself is a decent buy for dabblers who want something a class up from a Raspberry Pi but still want the trappings of the x86 ecosystem. You’re not getting top-tier storage or upgradeable memory, but the bevy of USB ports make up for it, and it’s enough RAM to say that you tried out local LLMs.
While it can run something like Plex or Jellyfin, AMD chips are not the best at transcoding, making Intel or Apple a better option for that use case. But LLMs or apps or VMs? They’re still on the table.
Of course, the flipside needs to be called out: A year or two ago, this machine, with its somewhat older AMD processor, likely would have cost $350. Now it’s $569.99 with various discounts. (It’s
currently $489 on Amazon
, with an additional 5% off by using the discount code
KAP3WTLC
. Overall, that’s 19% off with the coupon.) That puts it squarely in Mac Mini territory—but if your use case is light gaming or self-hosting, a mini PC like this is well-suited to those kinds of tasks. (And MacOS adds overhead when you run Docker on it, anyway.)
Not my hand—this is from a promotional video—but let’s say it was.
The Kamrui doesn’t have Apple Silicon, but it does have numerous USB-A ports and a couple of NVMe slots. And if you want to play with LLMs, it’s not a bad way to get your feet wet. (And presuming you use this to run four self-hosted apps that would otherwise cost $10 a month, it starts paying for itself after the first year.)
As for the self-hosting tools: Well … as I said up top, I think if you have a vague idea of what you’re doing, you’re going to hit the ceiling of something like Umbrel almost immediately. And you may run into issues as a new user, too, if the config gods don’t look kindly on your https setup.
If a flashy tool is going to keep your attention, it needs to do something fresh. HomeDock OS’ app focus is novel, but too buggy to recommend at this time. If the integrations pick up and the interface becomes friendlier for just dropping a Docker Compose blurb in a box, it could make sense. (I’m happy to take a second look if they ever bake Tailscale into the interface.)
That leaves us with Unraid. As I mentioned earlier, I didn’t reformat my SSD after finishing my Unraid test—because I think it’s where I’m going to end up, even though it’s the most expensive of the three options. Setup has more of a learning curve, making it a harder road for newbies, but it makes so much more sense if you understand how containers work. (Better the learning curve is at the beginning than buried in the middle.)
I think the fact that the forums are full of people who can actually explain what it’s doing is telling, too. Apologies to the Umbrel experts, but the number of desperate-looking threads with zero responses feels like a problem. With Unraid, you felt like you were running into success stories left and right. If you’re self-hosting for the first time, you want the success story, even if it means going with the uglier interface.
(And there’s something to be said about command lines and yaml files, too. I have managed a lot of my stack by hand in the past. You don’t need any of these tools, really.)
Cosmos Cloud, a tool I already use, is pretty good if you’re looking for an alternative to the three I reviewed here.
I do want to give a quick shout to the tool I already use, however,
Cosmos Cloud
. I have used it for quite a while at this point, and I do think it solves many of the issues with Umbrel and HomeDock OS. But I’ve seen some genuine performance degradation with it as the years have gone on. As a result, I’m at the point where a dedicated tool like Unraid makes more sense for the work I do.
With self-hosting, you know what fits best. My recommendation: Skip the buzzwords and the trendy apps, and go with what works.
--
Thanks again to Kamrui
for sending the machine along. Wanna buy your own?
Check it out on Amazon
and use the code
KAP3WTLC
for an additional 5% discount (making it 19% off its list price). Tell ’em Tedium sent you.
Find this one an interesting read?
Share it with a pal
!
And thanks again to
la machine
for sponsoring. It‘s definitely a device you can self-host.
Editor’s note:
Clarified the discount on the Mini PC; we apologize for any confusion that may have caused.
