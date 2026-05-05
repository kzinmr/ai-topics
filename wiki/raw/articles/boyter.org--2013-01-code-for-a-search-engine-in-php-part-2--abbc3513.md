---
title: "Code a Search Engine in PHP Part 2"
url: "https://boyter.org/2013/01/code-for-a-search-engine-in-php-part-2/"
fetched_at: 2026-05-05T07:02:05.238274+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Code a Search Engine in PHP Part 2

Source: https://boyter.org/2013/01/code-for-a-search-engine-in-php-part-2/

Are you really interested in learning how to Write a Search Engine from Scratch? Click this link and register your interest for my book about how to do so.
This is part 2 of a 5 part series.
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
The first implementation has a few issues that are pretty apparent. Chiefly is performance. Secondly it stores the index in a single folder which is loosely related to the first. Finally it shows duplicates in the search results. Lets fix the above and test things again to see how far we can go.
PERFORMANCE
Not sure what video I was watching but it had the following line about performance “Don’t ever guess. You will be wrong. Measure.” In my opinion (whatever that is worth) this is 100% correct. If you aren’t a human compiler/runtime (and if you are why are you reading this?) there is no way you can know what is actually slow in your application. You can guess, and you might be right, but generally its faster to run your application through a profiler and you quite often will be surprised.
One example came when I was profiling
http://searchcode.com/
and trying to get the result templates to load faster. Considering it does all sorts of regex/formatting/etc… I expected the issue to be string processing. What actually turned out to be was a method I was calling to get the root location of the website IE
http://searchcode.com/
it was called many times and ate most of the time. Simply calling it once and storing the value in a variable decreased page load times by about 30% *
PHP actually does have some decent profiling tools even if they can be a pain to setup. My personal choice is to use webgrind because its pretty easy to setup and understand. I did some profiling of the indexing using the following situations.
Empty index. Add/index single document.
100 documents in index. Add/index single document.
1000 documents in index. Add/index single document.
The results showed that most of the time is spent writing things to disk, mostly in the building of the index rather then saving the documents themselves. This is because for each document it loads the index shard from disk, appends to it and then saves it without considering it might need to do it again really soon. This means a single index shard for a common word such as “the” will be loaded and saved to disk once for each document added. When doing 10,000 documents this is a massive bottleneck.
INDEX IMPROVEMENTS
We need to consider how to spend less time writing or reading to disk while building the index. Off hand I can think of a few ways, of which we will have a look at two for the moment.
Keep the index in memory. Save every now and then or once at the end of the indexing process.
This approach has a few issues. The main one being if we are indexing a popular word such as “the” the index is going to get VERY large very quickly and consume all available memory.
Stopwords https://en.wikipedia.org/wiki/Stop_words
would fix this issue for a while, but eventually we are going to need more memory then we can fit in a machine. Sure we could only take this approach for words which are not common and keep the common words using the existing approach, but we won’t get much performance gain as its the frequent reads/writes which are killing performance. That said I think its worth at least trying, as it should be very easy to implement. It may also get us over the million document mark which means we can spend more time focused on cool ranking algorithms.
Flush outputs to disk occasionally, and post process.
This approach is more scale-able, but has the issue that the index is not searchable while we are building it. I think this one is the correct approach though as the previous one will probably run out of steam when we look at indexing a million documents. Essentially we have a two step index process. The first is where we add documents to the index. The process holds a file lock over a file and every now and then pushes more and more of the index to disk. As its a single file, and because we are flushing to disk every now and then performance should be reasonably fast and not constrained by the disk too much. When we have finished adding documents to the disk we run a post process over the new file to build our searchable index. Of course this is all in theory, the only way to be sure is to try it and benchmark. Assuming the first option fails that is.
OPTION 1 A SLIGHTLY NAIVE INDEXER
So in the list of improvements I identified two ways to speed things up and increase our ability to scale. The first being holding the index in memory while processing and flushing it to disk at the end of the process. Thankfully we already catered for this in the design. When we call the indexers index method we don’t have to pass one document, we can actually pass multiple. To implement the in memory saving we just need to change the indexer method to look like the below.```
public function index(array $documents) {
if(!is_array($documents)) {
return false;
}
$documenthash = array(); // so we can process multiple documents faster
foreach($documents as $document) {
// Save the document and get its ID then clean it up for processing
$id = $this->documentstore->storeDocument(array($document));
$con = $this->_concordance($this->_cleanDocument($document));
foreach($con as $word => $count) {
// Get and cache the word if we dont have it
if(!array_key_exists($word,$documenthash)) {
$ind = $this->index->getDocuments($word);
$documenthash[$word] = $ind;
}
if(count($documenthash[$word]) == 0) {
$documenthash[$word] = array(array($id,$count,0));
}
else {
$documenthash[$word][] = array($id,$count,0);
}
}
}
foreach($documenthash as $key => $value) {
$this->index->storeDocuments($key,$value);
}
return true;
}
The changes here are to store all the index shards in memory using $documentcash and then at the end dump them all to disk. This means rather then reading a writing to disk all the time we only do it in a single step per index. Of course it does mean we need to change our additions to the index like the below.```
$indexer->index(
 array(
  'Setting the AuthzUserAuthoritative directive explicitly to Off allows for user authorization to be passed on to lower level modules (as defined in the modules.c files) if there is no user matching the supplied userID.',
  'The Allow directive affects which hosts can access an area of the server. Access can be controlled by hostname, IP address, IP address range, or by other characteristics of the client request captured in environment variables.',
  'This directive allows access to the server to be restricted based on hostname, IP address, or environment variables. The arguments for the Deny directive are identical to the arguments for the Allow directive.',
  'The Order directive, along with the Allow and Deny directives, controls a three-pass access control system. The first pass processes either all Allow or all Deny directives, as specified by the Order directive. The second pass parses the rest of the directives (Deny or Allow). The third pass applies to all requests which do not match either of the first two.',
  'The AuthDBDUserPWQuery specifies an SQL query to look up a password for a specified user.  The users ID will be passed as a single string parameter when the SQL query is executed.  It may be referenced within the query statement using a %s format specifier.',
  'The AuthDBDUserRealmQuery specifies an SQL query to look up a password for a specified user and realm. The users ID and the realm, in that order, will be passed as string parameters when the SQL query is executed.  They may be referenced within the query statement using %s format specifiers.'
 )
);
All of the documents are now indexed in a single step. Of course with such a small case such as our 6 documents the overhead is very little. However when you compare this implementation with 100 or even 10,000 documents its considerably faster. It still slows down as you add more documents however. IE adding 1 document to an index containing 10,000 documents is going to be slower then 1 document to an index with 10.
A few checks of the above showed that we could index 200 documents considerably faster in a single sweep rather then a single document each time. Of course adding the next 200 documents was much slower then the first 200 but there is a huge improvement here. The nice thing is that if we just add 10,000 documents in a single go its just as fast as 1 as the speed penalty is on the initial read and the final write.
The above change is probably enough for us to go and test with. Assuming it holds together to 100,000 documents it could probably hold together to 1,000,000 documents.
BENCHMARKING
So with the above simple fix lets load it up and see how it goes. I ran the following code to input 100,000 documents and it managed to finish in about 20 minutes (on a very under-powered virtual machine running in VirtualBox).```
$toindex = array();
for($j=0;$j<100000; $j++) {
$toindex[] = ‘The AuthDBDUserRealmQuery specifies an SQL query to look up a password for a specified user and realm. The users ID and the realm, in that order, will be passed as string parameters when the SQL query is executed.  They may be referenced within the query statement using %s format specifiers.’;
}
$indexer->index($toindex);
Keep in mind this is saving the documents to disk as well which we will remove in our final version and the performance isn't too bad.

Searches work as well, however you need to add a time limit of 0```set_time_limit(0);```

To avoid hitting timeouts. This is because any search actually then goes on to display 100,000 results.

Im going to say that this totally surprised me. I really did expect that we would have to explore better ways of saving the index to disk. Since it does work however and since its highly likely that it will hold together for the full 1,000,000 documents lets move onto more interesting code.

### A BETTER SEARCH

One of the other issues we have is where duplicate results are returned when searching for more then one term IE a search for "AuthDBDUserRealmQuery SQL" will return the single document which contains AuthDBDUserRealmQuery twice. Lets implement some logic to remove duplicate documents from being returned.

The implementation is basically a copy of naievesearch and we modify the dosearch method like so```
function dosearch($searchterms) {
 $indresult = array();
 foreach($this->_cleanSearchTerms($searchterms) as $term) {

  $ind = $this->index->getDocuments($term);
  if($ind != null) {
   usort($ind, array($this->ranker, 'rankDocuments'));
   foreach($ind as $i) {
    $indresult[$i[0]] = $i[0];
   }
  }
 }

 $doc = array();
 foreach($indresult as $i) {
  $doc[] = $this->documentstore->getDocument($i);
 }

 return $doc;
}
In this case all we need to do loop through each of the results for each term, sort them and add them to a hash based on the id. This ensures we get no duplicate results. Because the sorting takes place for each term however documents are ranked according to their frequency for the first term, then the second etc… Not ideal but good enough for the moment. This also means our engine is still an OR engine by default.
To convert it to an AND engine the logic is similar and fairly simple assuming the lists are sorted. For each document list peek at the top document. If the document id exists in all of the lists that document is a match so remember it. If not pop the smallest id and check of they match. Repeat till you run out of documents (or hit some limit) and then rank and display.
INITIAL RESULTS
At this point everything is going well. We can index 100,000 documents without any major issues. We know that the search holds together at this point, so lets assume that everything should be good for us to hit out 1,000,000 document goal.
PHPSearch_Implementation_2.zip
This is the end of Part 2. In Part 3 we are going to modify out document store to use our downloaded documents, modify out indexer to deal with web documents and finally modify our ranker to rank with a little more intelligence.
