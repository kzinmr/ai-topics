---
title: "I made a Chrome extension to help avoid playing cheaters in chess"
url: "https://timsh.org/i-made-a-chrome-extension-to-help-avoid-playing-cheaters-in-chess/"
fetched_at: 2026-04-27T07:01:24.059740+00:00
source: "timsh.org"
tags: [blog, raw]
---

# I made a Chrome extension to help avoid playing cheaters in chess

Source: https://timsh.org/i-made-a-chrome-extension-to-help-avoid-playing-cheaters-in-chess/

If you google “chrome extension for cheating in chess”, you’ll find a lot of them. Cheating is so easy, it’s crazy.
If you google “chrome extension to avoid chess cheaters”, you might find this one and a few old apps that show you basic stats.
Think about it!
How to use
Install the extension at Google Store
Check your browser version here: chrome://version.
Only if it’s 126 or lower (highly unlikely if you update Chrome even once a year), go to extension options and turn off the “Auto open popup” setting, and then pin the extension in your browser for better experience. If the version is 127+ — do nothing.
Login to chess.com
Start a game or open any game to see the score of the player on the top — like this one:
https://www.chess.com/game/live/128552032877
If you meet a potential cheater (I consider 30%+ suspicious) — abort the game. Don’t waste your time, rating and nerves on them!
Motivation and idea behind the app
I love chess. I play a lot — this year I played 3630 games, around 10 games a day. I’m quite good — 2200 in rapid, 1900 in blitz, which is a result of thousands of hours of practice and studying.
And the higher I gеt, the more cheaters I see.
The scale of this problem is ridiculous — from my experience, 3/5 matched opponents either cheat or act very very suspicious at the +-2000 level in Rapid. In blitz it’s a little harder to cheat (since you have less time), but still, I would say 1/3 of blitz players at my level cheat.
I know that other people have the same problem. If you’re playing in the lower tier, you might not see it that often, because cheaters climb to the top rating very fast — sometimes in days after creating their account.
But I’m 100% sure that no matter the level you’re at, if you play chess, you have played cheaters in the past. Maybe even a lot of them.
How do you know someone cheated against you?
Well, you can be almost sure after the game, when you check the Game Report or even do self-analysis.
Most cheaters don’t cheat through all the full game to avoid getting 100% accuracy (however, there are lots who doesn’t bother as well).
They first play the opening “by hand”, then they get a position of disadvantage in 10–20 moves (because their rating == level is inflated), and then… they disappear for 30–60 seconds, and make an eyebrow-raising move.
And then every move comes in 2–5 seconds, no matter how counterintuitive it is, and you lose.
You can see this pattern in game review quite clearly: a poorly played opening, couple mistakes or blunders in the middlegame, and then 35 best moves in a row. This is Magnus Carlsen level chess.
Are there any anti-cheating mechanisms on chess.com?
Well, yes! You can report someone and select “Cheating” as a reason, and chess.com team will investigate it. Or maybe not?
I report a lot of people, because I play a lot. It’s sad that you can’t see the history of your reports (maybe I should add it to the extension too), but I report 100+ players every month. 30–50 of them I report after playing and checking the game review.
You know how much of them get banned?
One-two a month.
I played 357 games in last 30 days. 2 of the opponents I reported were banned.
You might say that it’s ok — maybe I’m delusional, I overreact and report everyone who beats me, and it’s good they’re not banned.
Well, I don’t think so.
Lots of people say the same thing —on
Reddit
,
Chess.com Forums
(the private “
Cheating Forum
” is in top 5 of all Chess.com forums), some creators on YouTube as well — like
GothamChess
, #1 chess content creator.
The main argument for me is that Chess.com does not bother to ban even the most reckless cheaters. I’ll provide just 1 example to illustrate the levels of it.
I recently played a game against “SumitGM000”. He started cheating after 5 moves, I felt it. I checked his recent games — he had an 80% winrate (currently 72%).
I texted him “please stop cheating. I know you do”.
Some cheaters actually stop when you accuse them in chat.
This one just texted “lol you can’t take the loss”.
I thought: hm, “…GM000”? What about “…GM00”? and just removed 1 zero in the link:
https://www.chess.com/stats/live/rapid/sumitgm000
.
Surprisingly, there is an account with this username. It was closed for cheating with the last game dated Oct 19, 2024, as you can see.
The account “SumitGM000” was opened the same day. It is still not banned, though I reported it, and I’m sure someone else did too.
UPD: the account was banned the next day after this post was published :)
Ok, ok. So you can’t do nothing about it?
No. You can, to some extent. And that is the purpose of my app.
What you
can
do is abort the game when you’re matched with someone suspicious. How do you know if someone is suspicious?
Before creating the extension, I followed this algorithm:
Check the account creation date — if an account is fresh and has a high rating, it’s quite suspicious.
Check the stats — winrate for the last 30 and 90 days. If it’s above 55% — it’s suspicios, if it’s above 70% — I am absolutely sure that I see a cheater.
Important note: amount of games matters. Obviously, if you played 3 games last month and won all of them, I won’t suspect you. But if you played 200 and won 150 — sorry, I don’t buy it.
Finally, scroll through the recent games and check the accuracies where game review was done. If I see a lot of 90%+ games, it’s a red flag.
So, if I’d see any of these factors — I’d abort the game, report and block this person. I don’t care about false accusations — if you actually don’t cheat, you’ll never get banned. Even if you do, the chances are pretty low as mentioned earlier.
However, there are 2 problems with this approach:
You have 20–60 seconds to do this “research” before making your move, or you lose the game and rating. With 20 seconds you have in blitz, it’s only possible to take a look at something without digging into the stats or recent games, and the red flags might be hidden there.
Sadly, Chess.com has a limitation on the amount of games you can abort, and it’s not transparent — try aborting 2–3–5 games in a row or in one day, and you’ll soon notice that there’s no option to do so anymore.
They say it’s an anti-bot technique, but it makes my playing experience significantly worse: imagine you did the research, seen the red flag, can’t abort the game, and now you either have to play an alleged cheater, or should just resign without playing.
That’s why I decided to create an app that would do the research for me in seconds after the opponent is found.
How it works
It’s quite simple. When the game starts, the extension automatically detects your opponent’s username, then uses it to perform some
chess.com API
requests:
profile data
, such as account age
overall stats
: player rating + how much games were played, won/lost/drawn in each format.
all the games
played last month (if it’s <15th of the month, get the previous month too).
Then these metrics are calculated:
Overall winrate in each format separately
Recent winrate (based on the games from last 15–30 days)
% of games with high accuracy out of games with known accuracy.
It’s 80%+ for ratings below 1500, and 90%+ for 1500+.
Account age [in days].
I tried using other metrics too, but they overcomplicated the resulting model and caused a lot of corner cases.
For example, I tried calculating the variance of time per move, because it’s a widely known indicator of cheating — that no matter how hard the move is, it’s played in consistent time. But it was very hard for me to convert this in some adequately distributed metric, so I gave up.
Risk score model (beware: some math below)
The model itself is very straightforward: it takes the arguments mentioned before and calculates some metrics based on them, and then combines weighted factors to get a score from 0 to 100.
I had to dig into some basic econometrics that I studied in university back in the day to figure it all out, because GPT-s, even o1, are still quite bad at math modelling.
For each of the values, I created a function to bias the model. For example, here’s the formula for the WinRateScore function — I asked GPT to print it out in nice sexy Latex:
Basically, we take w — % of wins in total games played, and n — number of games, and calculate the score based on the assumption that 50% is the “normal” winrate.
If winrate is below 50%, it’s not suspicious at all.
If it’s (50, 60] — a bit suspicious (as you can see, 50 at max).
If it’s (60, 70] — the resulting score will be in (50, 100].
Finally, if it’s 70+ — the score will be 100+.
Let me clarify because I feel that this logic might cause some questions.
Chess.com uses
Glicko system
for rating calculation, which determines your new rating (after playing a game) based on a couple of factors, including the amount of games you play and the difference between your and your opponent’s rating.
I’ll oversimpify it for the purpose of this text — you can check out how it works by following the link above.
If you play a lot, your winrate over a long period of time (big amount of games) should be around 50%.
Why?
Because if you win a lot, you gain rating quite quick, and sooner or later you end up at your current level, where your opponents are equally strong as you.
Once again — it is true when you play a lot of games, which is why I use the Weight(n) factor. But just to illustrate: if you win 50 games against opponents with equal rating (at the time of each game), you’ll gain 400 rating points, which is a lot.
All right, moving on — there’s also HighAccuracyScore function:
It has a similar logic: playing less than 10% of games with high accuracy is quite normal, playing more than 30% (over a big set of games) is very suspicious.
The final score is calculated using this formula:
All of the factors calculated using the formulas above are included in a weighted sum where ∑(w
i)
= 1, multiplied by account age factor, and then normalised by 100 — so if the resulting score is 170, it will still be cut down to 100 to keep the consistency of the score.
Finally, we take the maximum of the scores calculated for rapid, blitz and bullet, and that is the final score you see in the popup!
Couple words regarding the scoring model
All of the mentioned thresholds are set in a
single config file
— if you want to use custom values, you can set them in the config, build your version of the extension locally by following the instructions and github, and be happy.
I tried to include the thresholds in the setting of the extension, but verifying the correct values for each metric turned out to be a real pain in the ass. I honestly don’t believe that anyone will do it — please hit me up using contacts below if you do :)
I don’t think that this model is the best, or most advanced or … anything else. I’m not really a math / DS guy, and I believe that someone reading this might actually have a better model for the risk score in their head right now. Again, let me know if you do.
However, I tested the risk model on more than 200 players by now, and I quite like the result! All people I’m sure about have a very low score (under 10–15%), and those who I’m sure are cheaters have a 90+ score.
However, since the model is made for regular people like me and you, superGMs like Hikaru and Magnus have critical scores — well, I’ll leave it to Kramnik to decide on those guys.
It’s actually insane how good Hikaru is
Further development
I spent quite some time coding and debugging this app, and I hope it will reach some audience and help someone play more comfortably.
If it does, I’ll probably release a few updates, extending the functionality of the extension, he-he.
Here are a few things I would do in the next versions:
History of all scorings
History of all “reports” with a regular check on the status of accounts — for example, once a week
“Abort” counter — maybe I’ll figure out the logic behind the abort limitation, and add functionality to warn users that they should stop playing now, or else they risk to meet a cheater and be unable to abort the game.
Setting thresholds in settings or by uploading your own config — or maybe uploading your own mathematical model — for those 0 people who would do it.
Conclusion
Thanks for reading up until this point!
I hope you will find this app useful. If you do, please share it with your friends or local chess club, and consider leaving a review on Google Web Store:
https://chromewebstore.google.com/detail/chesscom-opponent-risk-sc/oiemcgpbdohnhkplobgndgdhdlbafoeg/reviews/
I believe the situation with cheating in online chess will only get worse with time, so we definitely need to do something about it to keep it enjoyable. If you’re someone from chess.com team — there are lots of things you could and should do, think about it.
I created this app with Cursor, as I usually do, but actually had to rewrite most part by myself since cursor produced some small, but very annoying bugs, and refused to fix them in an adequate amount of time.
The code is available on Github — please consider “starring” it as well, or even submit a PR if you want to add something or report an issue.
https://github.com/tim-sha256/chess.com-anti-cheat/
Contact me if you have any questions or enquiries here:
[email protected]
.
