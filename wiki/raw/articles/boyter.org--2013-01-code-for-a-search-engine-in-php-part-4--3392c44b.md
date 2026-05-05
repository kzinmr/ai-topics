---
title: "Code a Search Engine in PHP Part 4"
url: "https://boyter.org/2013/01/code-for-a-search-engine-in-php-part-4/"
fetched_at: 2026-05-05T07:02:05.098218+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Code a Search Engine in PHP Part 4

Source: https://boyter.org/2013/01/code-for-a-search-engine-in-php-part-4/

Are you really interested in learning how to Write a Search Engine from Scratch? Click this link and register your interest for my book about how to do so.
This is part 4 of a 5 part series.
Part 1
–
Part 2
–
Part 3
–
Part 4
–
Part 5
–
Downloads/Code
So previously we had 4 main issues identified. Im going to go with low hanging fruit and add a simple porn filter.
Probably the easiest way to remove porn at this point is to just blacklist it unless someone explicitly asks to see it. I had a quick look at the sort of terms that ranked for porn and came up with the following blacklist, using what I had seen and some terms from here
porn blacklist keyword filter http://www.gnutellaforums.com/limewire-tips-tricks/60590-keywords-filter.html
porn|naked|teens|pussy|sex|nasty|mature|crossdresser|couples|girlfriend|wives|pornstar|cock|fuck|shit|cunt|nude|lesbian|sexy|ass|ladyboy|granny|cum|boob|breast|exposing|milf|erotic|bdsm|live|penis|horny|slut|nudist|upskirt|boobs|tits|amateur|hottest|adult|teen|babe|1yo|2yo|3yo|4yo|5yo|6yo|7yo|8yo|9yo|10yo|11yo|12yo|13yo|14yo|15yo|16yo|17yo|incest|jailbait|kdv|kiddie|kiddy|kinder|Lolita|lsm|mbla|molested|ninfeta|pedo|phat|pjk|pthc|ptsc|premature|preteen|pthc|qsh|qwerty|r@ygold|raped|teensex|yovo|Pr0nStarS|tranny|transvest|XXX|Anal|Asshole|Bangbros|Barely|Blow|Blowjob|Bondage|brazzers|Camera_Phone|Centerfold|Clitoris|Cock|Cum|Cunt|Deepthroat|Diaper|Drilled|EROTRIX|Facial|Femjoy|Fetish|Fisting|fotos|FTV|Fuck|Gangbang|Gay|Handjob|Hardcore|Headjob|hidden_cam|Hustler|Jenna|Lesbo|Masturbat|MILF|nackte|naken|Naturals|Nipple|Nubile|Onlytease|Orgasm|Orgy|Penis|Penthouse|Playboy|Porn|Profileasian|Profileblond|Pussy|Scroops|selfpic|spunky_teens|strapon|strappon|Suck|TeenTraps|tittie|titty|tranny|transvest|twat|vagina|webcam|Whore|XPUSS|Amateur|Blonde|Brunette|Naked|Naughty|Private|Redhead|Sex|Slut|Strips|Teen|Young|wet|girl|video|taboo|nastiest
Keep in mind the above is a VERY agressive filter and will most likely filter out some non porn sites as well.
Chucking this though a simple regex inside the search class allows us to eliminate 99% of the porn results based on my simple tests. The relevent chage is below,```
preg_match_all(SEARCH_PORNFILTER, $document
0
.$document
0
, $matches);
// if they want to see porn, or its not porn
if($seeporn || count($matches[0]) <= 1) {
$doc[] = $document;
$count++;
if($count == SEARCH_DOCUMENTRETURN) {
break;
}
}
Pretty easy, we check if the user wants to see porn and if so just add it otherwise we check using the above blacklist. If there are 2 or more matches in the blacklist then we consider the match porn and ignore it. The seeporn variable is set in the constructor like so,```function dosearch($searchterms,$seeporn=SEARCH_DISPLAYPORN)```

Trying it out on some questionable searches shows that it works fairly well. One example I tried was "sex" and the first few results were,

<http://modernman.com/> Advice and info for men on pop culture, love & sex, cars & gear, men's health & grooming, and more.
  
<http://thefrisky.com/> Celebrity gossip, relationship advice, sex tips and more for real women everywhere!
  
<http://countyjailinmatesearch.com/> The county jail inmate search provides facility addresses, phone numbers and options to lookup inmates, arrest warrants and sex offenders. 1-888-786-5245.

Which looks fairly innocuous to me. **\*NB\*** This isnt implemented as some sort of moral crusade. I am just dealing with an issue that any serious search engine has to overcome at some point. Besides I didn't want to see those results while testing as they can be distracting.

Ok moving on to the other issue which is that w searching for things like "what the internet is talking about right now" the results are very slow to return, and that we don't get the result we would expect which would be Digg.com.

The easiest way to fix this with our current implementation is to improve our ranking algorithm. Because we are preranking documents documents such as Digg will bubble to the top of searches for terms like "what the internet is talking about right now" and should fix the issue.

Ranking however isn't the easiet thing in the world. Google and Bing use hundreds of signals which determine a pages rank. These include terms, page speed, user behaviour, incoming links, how large the site is, terms locations, terms weight in html etc&#8230;. We have almost none of that. However everyone needs to start somewhere so here are a few ideas I had off the top of my head to use as signals.

1. If the URL contains the search term, and how much of the url it is, IE a search for "microsoft" should rank higher for "<http://microsoft.com>" then "<http://trymicrosoftoffice.com/>"

2. If the title contains the search term, and how much of the title it is. IE a search for "google email" will match the title "Gmail: Email from Google" more so then "The Tea Party" which is currently ranking above it.

3. If the meta content contains the search term rank it more highly then those where it just appears in the content.

4. Use the quantcast id as a factor in the ranking.

All of the above look good to me. Lets do the lot. Our ranker interface probably needs to have an additional method added which can rank an individual document based on the term. This is defined in the iranker like so,```public function rankDocument($term, $document);```

And now for the implementation.```
define('RANKER_TITLEWEIGHT', 1000);
define('RANKER_URLWEIGHT', 6000);
define('RANKER_URLWEIGHTLOOSE', 2000);
define('RANKER_TERMWEIGHT', 100);

public function rankDocument($term, $document) {
 $cleanurl = $this->_cleanString($document[0]);
 $cleantitle = $this->_cleanString($document[1]);
 $cleanmeta = $this->_cleanString($document[2]);
 $rank = $document[3];

 preg_match_all('/ '.$term.' /i', $cleanurl, $urlcount);
 preg_match_all('/'.$term.'/i', $cleanurl, $urlcountloose);
 preg_match_all('/ '.$term.' /i', $cleantitle, $titlecount);
 preg_match_all('/ '.$term.' /i', $cleanmeta, $pagecount);

 $words_in_url    = count($urlcount[0]);
 $words_in_url_loose  = count($urlcountloose[0]);
 $words_in_title   = count($titlecount[0]);
 $words_in_meta    = count($pagecount[0]);

 $weight = (   $words_in_meta * RANKER_TERMWEIGHT
    + $words_in_title * RANKER_TITLEWEIGHT
    + $words_in_url * RANKER_URLWEIGHT
    + $words_in_url_loose * RANKER_URLWEIGHTLOOSE
   );

 // Normalise between 1 and 10 and then invert so
 // top 100 sites are 9.9 something and bottom 100 are 0.1
 $normailise = 10-(1 + ($rank-1)*(10-1)) / (1000000 - 1);
 $newweight = intval($weight * $normailise);

 return $newweight;
}
We just break things up and based on how many terms we find increase the rank. This means that this search is keyword heavy, IE if you want to rank highly for anything just keyword stuff your URL, Title and Meta tags with the term you are targeting. The reason we normalize the URLs is to create a basic pagerank algorithm, except rather then calculate our own page rank we will use the ranks we already know about.
One other thing we can do to speed things up is to add in some stop words, and finally add a stemmer. The first is just a list of words we wont index, such as “AND” “THE” etc… A stemmer is an algorithm to reduce words to their stem. IE searches can be reduced to search since they are pretty much the same. Doing so really cuts down on our index. I took the
stop word list from http://norm.al/2009/04/14/list-of-english-stop-words/
and the
porter stemmer implementation from http://tartarus.org/~martin/PorterStemmer/
Of course all of this ranking means nothing for search terms such as “google mail” as it will just rank based on the last term not both terms so lets add that in. This actually turned out to be a little more complex then expected. Im not going to go through all of the changes required as I want to end these series of articles. You can however look though the code to see what was implemented.
At this point the final step really is to run though getting as much performance out of the system that we can. A few profiling checks shows that most of the time lost is done when stemming. Thankfully we can cache the results of the stem to cut this down in the indexing stage and in the results. You could also save the stemmed words in the indexing portion and trade disk space for cpu burn time. This would increase performance when it comes to searching quite a bit. Another one to consider would be storing the porn flag in the index itself. This would allow us to skip the regex test and just discard the results before pulling them even from disk. Both of the above are something to consider for the future.
So at this point everything is pretty much fine, and works with 100,000 documents. I assumed that everything should be fine. I then ran it over the full million documents and hit… an out of memory error. Essentially during the indexing stage the index filled all the available memory and crashed. Just as a test I tried it on a far more powerful machine with 16 gig of memory and hit the same issue. Obviously this needs to be fixed to reach our goal.
If you remember back in part two I highlighted that this might become and issue and had another solution to indexing out two ways to overcome it,
Flush outputs to disk occasionally, and post process.
Looks like we need to do this to reach our 1 million document goal, which we will do in the next and final step.
PHPSearch_Implementation_4.zip
