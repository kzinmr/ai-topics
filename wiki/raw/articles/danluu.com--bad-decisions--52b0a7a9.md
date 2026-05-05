---
title: "How good are decisions? Evaluating decision quality in domains where evaluation is easy"
url: "https://danluu.com/bad-decisions/"
fetched_at: 2026-05-05T07:01:31.689995+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# How good are decisions? Evaluating decision quality in domains where evaluation is easy

Source: https://danluu.com/bad-decisions/

A statement I commonly hear in tech-utopian circles is that some seeming inefficiency can’t actually be inefficient because the market is efficient and inefficiencies will quickly be eliminated. A contentious example of this is
the claim that companies can’t be discriminating because the market is too competitive to tolerate discrimination
. A less contentious example is that when you see a big company doing something that seems bizarrely inefficient, maybe it’s not inefficient and you just lack the information necessary to understand why the decision was efficient. These kinds of statements are often accompanied by statements about how "incentives matter" or the CEO has "skin in the game" whereas the commentator does not.
Unfortunately, arguments like this are difficult to settle because, even in retrospect, it’s usually not possible to get enough information to determine the precise “value” of a decision. Even in cases where the decision led to an unambiguous success or failure, there are so many factors that led to the result that it’s difficult to figure out precisely why something happened.
In those post, we'll look at two classes of examples where we can see how good people's decisions are and how they respond to easy to obtain data showing that people are making bad decisions. Both classes of examples are from domains where the people making or discussing the decision seem to care a lot about the decision and the data clearly show that the decisions are very poor.
The first class of example comes from sports and the second comes from board games. One nice thing about sports is that they often have detailed play-by-play data and well-defined win criteria which lets us tell, on average, what the expected value of a decision is. In this post, we’ll look at the cost of bad decision making in one sport and then briefly discuss why decision quality in sports might be the same or better as decision quality in other fields. Sports are fertile ground because decision making was non-data driven and generally terrible until fairly recently, so we have over a century of information for major U.S. sports and, for a decent fraction of that time period, fans would write analyses about how poor decision making was and now much it cost teams, which teams would ignore (this has since changed and basically every team has a staff of stats-PhDs or the equivalent looking at data).
Baseball
In
another post, we looked at how "hiring" decisions in sports were total nonsense
. In this post, just because one of the top "rationality community" thought leaders gave the common excuse that that in-game baseball decision making by coaches isn't that costly ("Do bad in-game decisions cost games? Absolutely. But not
that many
games. Maybe they lose you 4 a year out of 162."; the entire post implies this isn't a big deal and it's fine to throw away 4 games), we'll look at how costly bad decision making is and how much teams spend to buy an equivalent number of wins in other ways. However, you could do the same kind of analysis for football, hockey, basketball, etc., and my understanding is that you’d get a roughly similar result in all of those cases.
We’re going to model baseball as a state machine, both because that makes it easy to understand the expected value of particular decisions and because this lets us talk about the value of decisions without having to go over most of the rules of baseball.
We can treat each baseball game as an independent event. In each game, two teams play against each other and the team that scores more runs (points) wins. Each game is split into 9 “innings” and in each inning each team will get one set of chances on offense. In each inning, each team will play until it gets 3 “outs”. Any given play may or may not result in an out.
One chunk of state in our state machine is the number of outs and the inning. The other chunks of state we’re going to track are who’s “on base” and which player is “at bat”. Each teams defines some order of batters for their active players and after each player bats once this repeats in a loop until the team collects 3 outs and the inning is over. The state of who is at bat is saved between innings. Just for example, you might see batters 1-5 bat in the first inning, 6-9 and then 1 again in the second inning, 2- … etc.
When a player is at bat, the player may advance to a base and players who are on base may also advance, depending on what happens. When a player advances 4 bases (that is, through 1B, 2B, 3B, to what would be 4B except that it isn’t called that) a run is scored and the player is removed from the base. As mentioned above, various events may cause a player to be out, in which case they also stop being on base.
An example state from our state machine is:
{1B, 3B; 2 outs}
This says that there’s a player on 1B, a player on 3B, there are two outs. Note that this is independent of the score, who’s actually playing, and the inning.
Another state is:
{--; 0 outs}
With a model like this, if we want to determine the expected value of the above state, we just need to look up the total number of runs across all innings played in a season divided by the number of innings to find the expected number of runs from the state above (ignoring the 9th inning because a quirk of baseball rules distorts statistics from the 9th inning). If we do this, we find that, from the above state, a team will score .555 runs in expectation.
We can then compute the expected number of runs for all of the other states:
0
1
2
bases
outs
--
.555
.297
.117
1B
.953
.573
.251
2B
1.189
.725
.344
3B
1.482
.983
.387
1B,2B
1.573
.971
.466
1B,3B
1.904
1.243
.538
2B,3B
2.052
1.467
.634
1B,2B,3B
2.417
1.650
.815
In this table, each entry is the expected number of runs from the remainder of the inning from some particular state. Each column shows the number of outs and each row shows the state of the bases. The color coding scheme is: the starting state (
.555
runs) has a white background. States with higher run expectation are more blue and states with lower run expectation are more red.
This table and the other stats in this post come from
The Book by Tango et al.
, which mostly discussed baseball between 1999 and 2002. See the appendix if you're curious about how things change if we use a more detailed model.
The state we’re tracking for an inning here is who’s on base and the number of outs. Innings start with nobody on base and no outs.
As above, we see that we start the inning with
.555
runs in expectation. If a play puts someone on 1B without getting an out,  we now have
.953
runs in expectation, i.e., putting someone on first without an out is worth
.953 - .555 = .398
runs.
This immediately gives us the value of some decisions, e.g., trying to “steal”
2B
with no outs and someone on first. If we look at cases where the batter’s state doesn’t change, a successful steal moves us to the
{2B, 0 outs}
state, i.e., it gives us
1.189 - .953 = .236
runs. A failed steal moves us to the
{--, 1 out}
state, i.e., it gives us
.953 - .297 = -.656
runs. To break even, we need to succeed
.656 / .236 = 2.78x
more often than we fail, i.e., we need a
.735
success rate to break even. If we want to compute the average value of a stolen base, we can compute the weighted sum over all states, but for now, let’s just say that it’s possible to do so and that you need something like a
.735
success rate for stolen bases to make sense.
We can then look at the stolen base success rate of teams to see that, in any given season, maybe 5-10 teams are doing better than breakeven, leaving 20-25 teams at breakeven or below (mostly below). If we look at a bad but not historically bad stolen-base team of that era, they might have a .6 success rate. It wouldn’t be unusual for a team from that era to make between 100 and 200 attempts. Just so we can compute an approximation, if we assume they were all attempts from the {1B, 0 outs} state, the average run value per attempt would be .4 * (-.656) + .6 * .236 = -0.12 runs per attempt. Another first-order approximation is that a delta of 10 runs is worth 1 win, so at 100 attempts we have -1.2 wins and at 200 attempts we have -2.4 wins.
If we run the math across actual states instead of using the first order approximation, we see that the average stolen base is worth -.467 runs and the average successful steal is worth .175 runs. In that case, a steal attempt with a .6 success rate is worth .4 * (-.467) + .6 * .175 =  -0.082 runs. With this new approximation, our estimate for the approximate cost in wins of stealing “as normal” vs. having a “no stealing” rule for a team that steals badly and often is .82 to 1.64 wins per season. Note that this underestimates the cost of stealing since getting into position to steal increases the odds of a successful “pickoff”, which we haven’t accounted for. From our state-machine standpoint, a pickoff is almost equivalent to a failed steal, but the analysis necessary to compute the difference in pickoff probability is beyond the scope of this post.
We can also do this for other plays coaches can cause (or prevent). For the “intentional walk”, we see that an intentional walk appears to be worth .102 runs for the opposing team. In 2002, a team that issued “a lot” of intentional walks might have issued 50, resulting in 50 * .102 runs for the opposing team, giving a loss of roughly 5 runs or .5 wins.
If we optimistically assume a “sac bunt” never fails, the cost of a sac bunt is .027 runs per attempt. If we look at the league where pitchers don’t bat, a team that was heavy on sac bunts might’ve done 49 sac bunts (we do this to avoid “pitcher” bunts, which add complexity to the approximation), costing a total of 49 * .027 = 1.32 runs or .132 wins.
Another decision that’s made by a coach is setting the batting order. Players bat (take a turn) in order, 1-9, mod 9. That is, when the 10th “player” is up, we actually go back around and the 1st player bats. At some point the game ends, so not everyone on the team ends up with the same number of “at bats”.
There’s a just-so story that justifies putting the fastest player first, someone with a high “batting average” second, someone pretty good third, your best batter fourth, etc. This story, or something like it, has been standard for over 100 years.
I’m not going to walk through the math for computing a better batting order because I don’t think there’s a short, easy to describe, approximation. It turns out that if we compute the difference between an “optimal” order and a “typical” order justified by the story in the previous paragraph, using an optimal order appears to be worth between 1 and 2 wins per season.
These approximations all leave out important information. In three out of the four cases, we assumed an average player at all times and didn’t look at who was at bat. The information above actually takes this into account to some extent, but not fully. How exactly this differs from a better approximation is a long story and probably too much detail for a post that’s using baseball to talk about decisions outside of baseball, so let’s just say that we have pretty decent but not amazing approximation that says that a coach who makes bad decisions following conventional wisdom that are in the normal range of bad decisions during a baseball season might be able cost their team something like 1 + 1.2 + .5 + .132 = 2.83 wins on these three decisions alone vs. a decision rule that says “never do these actions that, on average, have negative value”. If we compare to a better decision rule such as “do these actions when they have positive value and not when they have negative value” or a manager that generally makes good decisions, let’s conservatively estimate that’s maybe worth 3 wins.
We’ve looked at four decisions (sac bunt, steal, intentional walk, and batting order). But there are a lot of other decisions! Let’s arbitrarily say that if we look at all decisions and not just these four decisions, having a better heuristic for all decisions might be worth 4 or 5 wins per season.
What does 4 or 5 wins per season really mean? One way to look at it is that baseball teams play 162 games, so an “average” team wins 81 games. If we look at the seasons covered, the number of wins that teams that made the playoffs had was {103, 94, 103, 99, 101, 97, 98, 95, 95, 91, 116, 102, 88, 93, 93, 92, 95, 97, 95, 94, 87, 91, 91, 95, 103, 100, 97, 97, 98, 95, 97, 94}. Because of the structure of the system, we can’t name a single number for a season and say that N wins are necessary to make the playoffs and that teams with fewer than N wins won’t make the playoffs, but we can say that 95 wins gives a team decent odds of making the playoffs. 95 - 81 = 14. 5 wins is more than a third of the difference between an average team and a team that makes the playoffs. This a huge deal both in terms of prestige and also direct economic value.
If we want to look at it at the margin instead of on average, the smallest delta in wins between teams that made the playoffs and teams that didn’t in each league was {1, 7, 8, 1, 6, 2, 6, 3}. For teams that are on the edge, a delta of 5 wins wouldn’t always be the difference between a successful season (making playoffs) and an unsuccessful season (not making playoffs), but there are teams within a 5 win delta of making the playoffs in most seasons. If we were actually running a baseball team, we’d want to use a much more fine-grained model, but as a first approximation we can say that in-game decisions are a significant factor in team performance and that, using some kind of computation, we can determine the expected cost of non-optimal decisions.
Another way to look at what 5 wins is worth is to look at what it costs to get a player who’s not a pitcher that’s 5 wins above average (WAA) (we look at non-pitchers because non-pitchers tend to play in every game and pitchers tend to play in parts of some games, making a comparison between pitchers and non-pitchers more complicated). Of the 8 non-pitcher positions (we look at non-pitcher positions because it makes comparisons simpler), there are 30 teams, so we have 240 team-positions pairs. In 2002, of these 240 team-position pairs,
there are two that were >= 5 WAA
, Texas-SS (Alex Rodriguez, paid $22m) and SF-LF (Barry Bonds, paid $15m). If we look at the other seasons in the range of dates we’re looking at, there are either 2 or 3 team-position pairs where a team is able to get >= 5 WAA in a season These aren’t stable across seasons because player performance is volatile, so it’s not as easy as finding someone great and paying them $15m. For example, in 2002, there were 7 non-pitchers paid $14m or more and only two of them we worth 5 WAA or more. For reference, the average total team payroll (teams have 26 players per) in 2002 was $67m, with a minimum of $34m and a max of $126m. At the time a $1m salary for a manager would’ve been considered generous, making a 5 WAA manager an incredible deal.
5 WAA assumes typical decision making lining up with events in a bad, but not worst-case way. A more typical case might be that a manager costs a team 3 wins. In that case, in 2002, there were 25 team-position pairs out of 240 where a single player could make up for the loss caused from management by conventional wisdom. Players who provide that much value and who aren’t locked up in artificially cheap deals with particular teams due to the mechanics of player transfers are still much more expensive than managers.
If we look at how teams have adopted data analysis in order to improve both in-game decision making and team-composition decisions, it’s been a slow, multi-decade, process.
Moneyball
describes part of the shift from using intuition and observation to select players to incorporating statistics into the process. Stats nerds were talking about how you could do this at least since
1971
and no team really took it seriously until the 90s and the ideas didn’t really become mainstream until the mid 2000s, after a bestseller had been published.
If we examine how much teams have improved at the in-game decisions we looked at here, the process has been even slower. It’s still true today that statistics-driven decisions aren’t mainstream. Things are getting better, and if we look at the aggregate cost of the non-optimal decisions mentioned here, the aggregate cost has been getting lower over the past couple decades as intuition-driven decisions slowly converge to more closely match what stats nerds have been saying for decades. For example, if we look at the total number of sac bunts recorded across all teams from 1999 until now, we see:
1999
2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
1604
1628
1607
1633
1626
1731
1620
1651
1540
1526
1635
1544
1667
1479
1383
1343
1200
1025
925
Despite decades of statistical evidence that sac bunts are overused, we didn’t really see a decline across all teams until 2012 or so. Why this is varies on a team-by-team and case-by-case basis, but the fundamental story that’s been repeated over and over again both for statistically-driven team composition and statistically driven in-game decisions is that the people who have the power to make decisions often stick to conventional wisdom instead of using “radical” statistically-driven ideas. There are a number of reasons as to why this happens. One high-level reason is that the change we’re talking about was a cultural change and cultural change is slow. Even as this change was happening and teams that were more data-driven were outperforming relative to their budgets, people anti-data folks ridiculed anyone who was using data. If you were one of the early data folks, you'd have to be
willing to tolerate a lot of the biggest names in the game calling you stupid, as well as fans, friends, etc.
. It doesn’t surprise people when it takes a generation for scientific consensus to shift in the face of this kind of opposition, so why should be baseball be any different?
One specific lower-level reason “obviously” non-optimal decisions can persist for so long is that there’s a lot of noise in team results. You sometimes see a manager make some radical decisions (not necessarily statistics-driven), followed by some poor results, causing management to fire the manager. There’s so much volatility that you can’t really judge players or managers based on small samples, but this doesn’t stop people from doing so. The combination of volatility and skepticism of radical ideas heavily disincentivizes going against conventional wisdom.
Among the many consequences of this noise is the fact that the winner of the "world series" (the baseball championship) is heavily determined by randomness. Whether or not a team makes the playoffs is determined over 162 games, which isn't enough to remove all randomness, but is enough that the result isn't mostly determined by randomness. This isn't true of the playoffs, which are too short for the outcome to be primarily determined by the difference in the quality of teams. Once a team wins the world series, people come up with all kinds of just-so stories to justify why the team should've won, but if we look across all games, we can see that the stories are just stories. This is, perhaps, not so different to listening to people tell you why their startup was successful.
There are metrics we can use that are better predictors of future wins and losses (i.e., are less volatile than wins and losses), but, until recently, convincing people that those metrics were meaningful was also a radical idea.
Board games
That's the baseball example. Now on to the board game example. In this example, we'll look at people who make comments on "modern" board game strategy, by which I mean they comment on strategy for games like Catan, Puerto Rico, Ark Nova, etc.
People often vehemently disagree about what works and what doesn't work. Today, most online discussions of this sort happen on boardgamegeek (BGG), a forum that is, by far, the largest forum for discussing board games. A quirk of these discussions is that people often use the same username on BGG as on boardgamearena (BGA), a online boardgame site where people's ratings (Elos) are tracked and you can see people's Elo ratings.
So, in these discussions, you'll see someone saying that strategy X is dominant. Then someone else will come in and say, no, strategy Y beats strategy X, I win with strategy Y all the time when people do strategy X, etc. If you understand the game, you'll see that the person arguing for X is correct and the person arguing for Y is wrong, and then you'll look up these people's Elos and find that the X-player is a high-ranked player and the Y-player is a low-ranked player.
The thing that's odd about this is, how come the low-ranked players so confidently argue that their position is correct? Not only do they get per-game information indicating that they're wrong (because they often lose), they have a rating that aggregates all of their gameplay and tells them, roughly, how good they are. Despite this rating telling them that they don't know what they're doing in the game, they're utterly convinced that they're strong players who are playing well and that they not only have good strategies, their strategies are good enough that they should be advising much higher rated players on how to play.
When people correct these folks, they often get offended because they're sure that they're good and they'll say things like "I'm a good [game name] player. I win a lot of games", followed by some indignation that their advice isn't taken seriously and/or huffy comments about how people who think strategy X works are all engaging in group think even when these people are playing in the same pool of competitive online players where, if it were true that strategy X players were engaging in incorrect group think, strategy Y players would beat them and have higher ratings. And, as we noted
when we looked at video game skill
, players often express great frustration and anger at losing and not being better at the game, so it's clear that they want to do better and win. But even having a rating that pretty accurately sums on your skill displayed on your screen at all times doesn't seem to be enough to get people to realize that they're, on average, making poor decisions and could easily make better decisions by taking advice from higher-rated players instead of insisting that their losing strategies work.
When looking at the video game Overwatch, we noted that often overestimated their own skill and blamed teammates for losses. But in these kinds of boardgames, people are generally not playing on teams, so there's no one else to blame. And not only is there no teammate to blame, in most games, the most serious rated game format is 1v1 and not some kind of multi-player FFA, so you can't even blame a random person who's not on your team. In general, someone's rating in a 1v1 game is about as accurate as metric as you're going to get for someone's domain-specific decision making skill in any domain.
And yet, people are extremely confident about their own skills despite their low ratings. If you look at board game strategy commentary today, almost all of it is wrong and, when you look up people's ratings, almost all of it comes from people who are low rated in every game they play, who don't appear to understand how to play any game well. Of course there's nothing inherently wrong with playing a game poorly if that's what someone enjoys. The incongruity here comes from people playing poorly, having a well-defined rating that shows that they're playing poorly, be convinced that they're playing well and taking offence when people note that the strategies they advocate for don't work.
Life outside of games
In the world, it's rare to get evidence of the quality of our decision making that's as clear as we see in sports and board games. When making an engineering decision, you almost never have data that's as clean as you do in baseball, nor do you ever have an Elo rating that can basically accurately sum up how good your past decision making is. This makes it much easier to adjust to feedback and make good decisions in sports and board games and yet, we can observe that most decision making in sport and board games in poor. This was true basically forever in sports despite a huge amount of money being on the line, and is true in board games despite people getting quite worked up over them and seeming to care a lot.
If we think about the general version of the baseball decision we examined, what’s happening is that decisions have probabilistic payoffs. There’s very high variance in actual outcomes (wins and losses), so it’s possible to make good decisions and not see the direct effect of them for a long time. Even if there are metrics that give us a better idea of what the “true” value of a decision is, if you’re operating in an environment where your management doesn’t believe in those metrics, you’re going to have a hard time keeping your job (or getting a job in the first place) if you want to do something radical whose value is only demonstrated by some obscure-sounding metric unless they take a chance on you for a year or two. There have been some major phase changes in what metrics are accepted, but they’ve taken decades.
If we look at business or engineering decisions, the situation is much messier. If we look at product or infrastructure success as a “win”, there seems to be much more noise in whether or not a team gets a “win”. Moreover, unlike in baseball, the sort of play-by-play or even game data that would let someone analyze “wins” and “losses” to determine the underlying cause isn’t recorded, so it’s impossible to determine the true value of decisions. And even if the data were available, there are so many more factors that determine whether or not something is a “win” that it’s not clear if we’d be able to determine the expected value of decisions even if we had the data.
We’ve seen that in a field where one can sit down and determine the expected value of decisions, it can take decades for this kind of analysis to influence some important decisions. If we look at fields where it’s more difficult to determine the true value of decisions, how long should we expect it to take for “good” decision making to surface? It seems like it would be a while, perhaps forever, unless there’s something about the structure of baseball and other sports that makes it particularly difficult to remove a poor decision maker and insert a better decision maker.
One might argue that baseball is different because there are a fixed number of teams and it’s quite unusual for a new team to enter the market, but if you look at things like public clouds, operating systems, search engines, car manufacturers, etc., the situation doesn’t look that different. If anything, it appears to be much cheaper to take over a baseball team and replace management (you sometimes see baseball teams sell for roughly a billion dollars) and there are more baseball teams than there are competitive products in the markets we just discussed, at least in the U.S. One might also argue that, if you look at the structure of baseball teams, it’s clear that positions are typically not handed out based on decision-making merit and that
other factors tend to dominate
, but this doesn’t seem obviously more true in baseball than in engineering fields.
This isn’t to say that we expect obviously bad decisions everywhere. You might get that idea if you hung out on baseball stats nerd forums before
Moneyball
was published (and for quite some time after), but if you looked at formula 1 (F1) around the same time, you’d see teams employing PhDs who are experts in economics and game theory to make sure they were making reasonable decisions. This doesn’t mean that F1 teams always make perfect decisions, but they at least avoided making decisions that interested amateurs could identify as inefficient for decades. There are some fields where competition is cutthroat and you have to do rigorous analysis to survive and there are some fields where competition is more sedate. In living memory,
there was a time when training for sports was considered ungentlemanly
and someone who trained with anything resembling modern training techniques would’ve had a huge advantage. Over the past decade or so, we’re seeing the same kind of shift but for statistical techniques in baseball instead of training in various sports.
If we want to look at the quality of decision making, it's too simplistic to say that we expect a firm to make good decisions because they're exposed to markets and there's economic value in making good decisions and people within the firm will probably be rewarded greatly if they make good decisions. You can't even tell if this is happening by asking people if they're making rigorous, data-driven, decisions. If you'd ask people in baseball they were using data in their decisions, they would've said yes throughout the 70s and 80s. Baseball has long been known as a sport where people track all kinds of numbers and then use those numbers. It's just that people didn't backtest their predictions, let alone backtest their predictions with holdouts.
The
paradigm shift
of using data effectively to drive decisions has been hitting different fields at different rates over the past few decades, both inside and outside of sports. Why this change happened in F1 before it happened in baseball is due to a combination of the difference in incentive structure in F1 teams vs. baseball teams and the difference in
institutional culture
. We may take a look at this in a future post, but this turns out to be a fairly complicated issue that requires a lot more background.
Looking at the overall picture, we could view this glass as being half empty (wow, people suck at making easy decisions that they consider very important, so they must be absolutely horrible at making non-easy decisions) or the glass as being half full (wow, you can find good opportunities for improvement in many places, even in areas people claim must be hard due to
econ 101 reasoning
like "they must be making the right call because they're highly incentivized" could trick one into thinking that there aren't easy opportunities available).
Appendix: non-idealities in our baseball analysis
In order to make this a short blog post and not a book, there are a lot of simplifications the approximation we discussed. One major simplification is the idea that all runs are equivalent. This is close enough to true that this is a decent approximation. But there are situations where the approximation isn’t very good, such as when it’s the 9th inning and the game is tied. In that case, a decision that increases the probability of scoring 1 run but decreases the probability of scoring multiple runs is actually the right choice.
This is often given as a justification for a relatively late-game sac bunt. But if we look at the probability of a successful sac bunt, we see that it goes down in later innings. We didn’t talk about how the defense is set up, but defenses can set up in ways that reduce the probability of a successful sac bunt but increase the probability of success of non-bunts and vice versa. Before the last inning, this actually makes sac bunt worse late in the game and not better! If we take all of that into account in the last inning of a tie game, the probability that a sac bunt is a good idea then depends on something else we haven’t discussed, the batter at the plate.
In our simplified model, we computed the expected value in runs across all batters. But at any given time, a particular player is batting. A successful sac bunt advances runners and increases the number of outs by one. The alternative is to let the batter “swing away”, which will result in some random outcome. The better the batter, the higher the probability of an outcome that’s better than the outcome of a sac bunt. To determine the optimal decision, we not only need to know how good the current batter is but how good the subsequent batters are. One common justification for the sac bunt is that pitchers are terrible hitters and they’re not bad at sac bunting because they have so much practice doing it (because they’re terrible hitters), but it turns out that pitchers are also below average sac bunters and that the argument that we should expect pitchers to sac because they’re bad hitters doesn’t hold up if we look at the data in detail.
Another reason to sac bunt (or bunt in general) is that the tendency to sometimes do this induces changes in defense which make non-bunt plays work better.
A full computation should also take into account the number of balls and strikes a current batter has, which is a piece of state we haven’t discussed at all as well as the speed of the batter and the players on base as well as the particular stadium the game is being played in and the opposing pitcher as well as the quality of their defense. All of this can be done, even on a laptop -- this is all “small data” as far as computers are concerned, but walking through the analysis even for one particular decision would be substantially longer than everything in this post combined including this disclaimer. It’s perhaps a little surprising that taking all of these non-idealities into account doesn’t overturn the general result, but it turns out that it doesn’t (it finds that there are many situations in which sac bunts have positive expected value, but that sac bunts were still heavily overused for decades).
There’s a similar situation for intentional walks, where the non-idealities in our analysis appear to support issuing intentional walks. In particular, the two main conventional justifications for an intentional walk are
By walking the current batter, we can set up a “force” or a “double play” (increase the probability of getting one out or two outs in one play). If the game is tied in the last inning, putting another player on base has little downside and has the upside of increasing the probability of allowing zero runs and continuing the tie.
By walking the current batter, we can get to the next, worse batter.
An example situation where people apply the justification in (1) is in the
{1B, 3B; 2 out}
state. The team that’s on defense will lose if the player at
3B
advances one base. The reasoning goes, walking a player and changing the state to
{1B, 2B, 3B; 2 out}
won’t increase the probability that the player at
3B
will score and end the game if the current batter “puts the ball into play”, and putting another player on base increases the probability that the defense will be able to get an out.
The hole in this reasoning is that the batter won’t necessarily put the ball into play. After the state is
{1B, 2B, 3B; 2 out}
, the pitcher may issue an unintentional walk, causing each runner to advance and losing the game. It turns out that being in this state doesn’t affect the the probability of an unintentional walk very much. The pitcher tries very hard to avoid a walk but, at the same time, the batter tries very hard to induce a walk!
On (2), the two situations where the justification tend to be applied are when the current player at bat is good or great, or the current player is batting just before the pitcher. Let’s look at these two separately.
Barry Bonds’s seasons from 2001, 2002, and 2004 were some of the statistically best seasons of all time and are as extreme a case as one can find in modern baseball. If we run our same analysis and account for the quality of the players batting after Bonds, we find that it’s sometimes the correct decision for the opposing team to intentionally walk Bonds, but it was still the case that most situations do not warrant an intentional walk and that Bonds was often intentionally walked in a situation that didn’t warrant an intentional walk. In the case of a batter who is not having one of the statistically best seasons on record in modern baseball, intentional walks are even less good.
In the case of the pitcher batting, doing the same kind of analysis as above also reveals that there are situations where an intentional walk are appropriate (not-late game, {1B, 2B; 2 out}, when the pitcher is not a significantly above average batter for a pitcher). Even though it’s not always the wrong decision to issue an intentional walk, the intentional walk is still grossly overused.
One might argue the fact that our simple analysis has all of these non-idealities that could have invalidated the analysis is a sign that decision making in baseball wasn’t so bad after all, but I don’t think that holds. A first-order approximation that someone could do in an hour or two finds that decision making seems quite bad, on average. If a team was interested in looking at data, that ought to lead them into doing a more detailed analysis that takes into account the conventional-wisdom based critiques of the obvious one-hour analysis. It appears that this wasn’t done, at least not for decades.
The problem is that before people started running the data, all we had to go by were stories. Someone would say "with 2 outs, you should walk the batter before the pitcher to get to the pitcher [in some situations] to get to the pitcher and get the guaranteed out". Someone else might respond "we obviously shouldn't do that late game because the pitcher will get subbed out for a pinch hitter and early game, we shouldn't do it because even if it works and we get the easy out, it sets the other team up to lead off the next inning with their #1 hitter instead of an easy out". Which of these stories is the right story turns out to be an empirical question. The thing that I find most unfortunate is that, after started people running the numbers and the argument became one of stories vs. data, people persisted in sticking with the story-based argument for decades. We see the same thing in business and engineering, but it's arguably more excusable there because decisions in those areas tend to be harder to quantify. Even if you can reduce something to a simple engineering equation, someone can always argue that the engineering decision isn't what really matters and this other business concern that's hard to quantify is the most important thing.
Appendix: possession
Something I find interesting is that statistical analysis in football, baseball, and basketball has found that teams have overwhelmingly undervalued possessions for decades. Baseball doesn't have the concept of possession per se, but if you look at being on offense as "having possession" and getting 3 outs as "losing possession", it's quite similar.
In football, we see that
maintaining possession
is such a big deal that it is usually an error to punt on 4th down, but this hasn't stopped teams from punting by default basically forever. And in basketball, players who shoot a lot with a low shooting percentage were (and arguably still are) overrated.
I don't think this is fundamental -- that possessions are as valuable as they are comes out of the rules of each game. It's arbitrary. I still find it interesting, though.
Appendix: other analysis of management decisions
Bloom et al., Does management matter? Evidence from India
looks at the impact of management interventions and the effect on productivity.
Other work by Bloom
.
DellaVigna et al., Uniform pricing in US retail chains
allegedly finds a significant amount of money left on the table by retail chains (seven percent of profits) and explores why that might happen and what the impacts are.
The upside of work like this vs. sports work is that it attempts to quantify the impact of things outside of a contrived game. The downside is that the studies are on things that are quite messy and it's hard to tell what the study actually means. Just for example, if you look at studies on innovation, economists often use patents as a proxy for innovation and then come to some conclusion based on some variable vs. number of patents. But if you're familiar with engineering patents, you'll know that number of patents is an incredibly poor proxy for innovation. In the hardware world, IBM is known for cranking out a very large number of useless patents (both in the sense of useless for innovation and also in the narrow sense of being useless as a counter-attack in patent lawsuits) and there are some companies that get much more mileage out of filing many fewer patents.
AFAICT, our options here are to know a lot about decisions in a context that's arguably completely irrelevant, or to have ambiguous information and probably know very little about a context that seems relevant to the real world. I'd love to hear about more studies in either camp (or even better, studies that don't have either problem).
Thanks to Leah Hanson, David Turner, Milosz Dan, Andrew Nichols, Justin Blank, @hoverbikes, Kate Murphy, Ben Kuhn, Patrick Collison, and an anonymous commenter for comments/corrections/discussion.
