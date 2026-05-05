---
title: "Ben E. C. Boyter"
url: "https://boyter.org/2008/09/data-mining/"
fetched_at: 2026-05-05T07:02:08.594756+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Ben E. C. Boyter

Source: https://boyter.org/2008/09/data-mining/

So a quick update. I spent 2 hours or so yesterday working on the netflix data mining. I basically just tidied it up and started testing. I was almost finished and was about to post a blog with results, but decided I wasn’t happy with the results. It turned out there was a bug but that my code which worked out how related users are wasn’t as effective as I thought it would be. See I used the vector space index to calculate how similar users are. The catch being is that it found the users almost 100% similar in almost all cases. I was wondering about this and then realised it was working correctly, and my assumption on how it would work was wrong.
What ended up happening was this,
My user rates the movies like so,
Movie 1:5
Movie 2:4
The one I am comparing to rates them like this,
Movie 1:1
Movie 2:1
Now because the ratings are so different the users should have almost a 0% relation. However it ended up giving a relation of 99% which is obviously wrong. Now there are two ways to improve this. Feed in more movies to check which will increase the distance between the users, or modify the ratings so they are more separate. So 1 = -5, 2 = -2, 3 =0, 4=2, 5=5.
I decided that I would do the second since it means no matter the amount of movies plugged in it should give better results. And the results are…
Im not sure. I haven’t put the code in to do this. I will do it tonight (its a 30 min job) and post the results for a few queries. Essentially the way the queries work is I put in some movies and how I rated them. The program then goes and finds movies which I might like based on that information.
EDIT
I ended up implementing the above and then trying it out on a few queries.
Like Star Trek, Dislike Star Wars
Star Trek: Deep Space Nine: Season 3 0.805184646091
Star Trek: The Next Generation: Season 5 0.77184885453
The Twilight Zone: Vol. 26 0.763825884208
Dark Shadows Reunion 0.735055822124
Red Dwarf: Series 3: Bonus Material 0.667293663415
Dark Command 0.651819605806
Star Trek V: The Final Frontier 0.64808961258
Paul McCartney in Red Square 0.6261076108
Petite Princess Yucie 0.605629573421
P.D. James: A Mind to Murder 0.600064854695
Like Felicity season 1 and 2 but average thoughts about The Simpsons
Significant Others: The Series 1.42238853726
Kiss the Bride 1.05870702711
Bed of Roses 0.933097109352
The Day I Became a Woman 0.81028667654
Boys and Girls 0.808615378794
A Wedding for Bella 0.808054554979
Life as a House 0.754675623402
Madonna: The Drowned World Tour 2001 0.707120938732
He Knew He Was Right 0.700587353357
Moonlight Mile 0.686709180519
Like Futurama
s-Cry-ed 2.84044588442
Dragon Ball Z: World Tournament 2.78294438997
The Incredibles 2.74329078582
SpongeBob SquarePants: Season 3 2.71580396863
Stargate SG-1: Season 5 2.68855190797
The Godfather 2.63290946954
Gantz 2.58889864606
Boogiepop Phantom 2.52610181383
Lain #1: Navi 2.52517642719
Lady Snowblood 2.49056334915
Like Notting Hill, Love Actually and Bridget Jones Diary
Gilmore Girls: Season 3 2.40498354129
Anne of Green Gables: The Sequel 2.31112342646
The Best of Friends: Vol. 2 2.2402363423
The Best of Friends: Season 3 2.23488217277
Always 2.14127558439
Bridget Jones's Diary 2.09806999838
My Fair Lady: Special Edition: Bonus Material 2.09561711275
Sabrina 2.07214029062
Center Stage 2.06699886716
La Femme Nikita: Season 3 2.03411556876
Four Weddings and a Funeral 2.00530788895
Like The Evil Dead and Evil Dead 2
Gantz 2.79699784955
Slayers: Excellent 2.71615415583
Un Chien Andalou 2.63403044096
Dario Argento Collection: Vol. 3: Tenebre 2.62725100592
Red Dwarf: Series 3: Bonus Material 2.58537902316
Dragon Ball: Commander Red Saga 2.52390554678
George Carlin: Personal Favorites 2.52094084529
The Twilight Zone: Vol. 28 2.47219078634
The Godfather 2.45901663416
Godzilla vs. Gigan 2.38644476895
Like Terminator 1,2,3
Baki the Grappler 2.73392438406
Stargate SG-1: Season 4 2.6963074589
Adventures of Batman & Robin: Poison Ivy/The Penguin 2.6838141171
Star Trek: The Next Generation: Season 5 2.6574809937
Red Dwarf: Series 3: Bonus Material 2.61933747059
Dragon Ball Z: Cell Games 2.54598404544
Dragon Ball: Commander Red Saga 2.51716360289
Scrapped Princess 2.51142671664
Fullmetal Alchemist 2.49570656834
Terminator 2: Extreme Edition: Bonus Material 2.49400663766
