---
title: "Code a Search Engine in PHP Part 1"
url: "https://boyter.org/2013/01/code-for-a-search-engine-in-php-part-1/"
fetched_at: 2026-05-05T07:02:05.327688+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Code a Search Engine in PHP Part 1

Source: https://boyter.org/2013/01/code-for-a-search-engine-in-php-part-1/

[Are you really interested in learning how to Write a Search Engine from Scratch? Click this link and register your interest for my book about how to do so.][1]
This is part 1 of a 5 part series.
[Part 1][2] – [Part 2][3] – [Part 3][4] – [Part 4][5] – [Part 5][6] – [Downloads/Code][7]
I imagine that if you have landed on this page you probably have an interest in search and search engines. Not only that, you have probably read the following [Why Writing Your Own Search Engine is Hard by Anna Patterson (of Cuil fame) http://queue.acm.org/detail.cfm?id=988407][8] If not, go read it and come back here. I have always had an interest in search and indexing I thought I would take the time to write a simple indexer as a way of testing if I had actually learnt anything.
Ok let’s do it. Let’s write a small search engine. By small I mean let’s make it so we can index about a million documents and search on them. I say only a million because you can pretty easily download this number of documents and store them on a single machine these days.
First things first let’s state our goals so we know what we are aiming for.
WebCrawler, indexer and document storage capable of handling 1 million or so documents.
Use test driven development to help enforce good design and modular code.
Have ability to have multiple strategies for things like the index, documentstore, search etc…
Have something I am willing to show off in terms of code.
To start what we need is some thought and design. I suspect that pretty much any search engine you name started with some simple ideas which were then executed on. First thing I am going to choose is what language I’m going to write things in. I considered doing this in Java, C# or Python, but in the end decided to go with PHP for a few reasons. The first being that there isn’t really an existing implementation out there for PHP and more importantly I want to use this as a way of proving I have some PHP skills.
A search engine really only has a few parts. A crawler to pull external documents down ready to be indexed, an index which is where the documents are stored in an inverted tree and a documentstore for keeping the documents.
For the WebCrawler I am just going to use a very simple FOR(X) GET X; simple PHP script. This should be more than enough to get us started indexing. There are other crawlers out there writing in PHP such as Sphider, but really we only need something simple.
For the actual implementation of the index and documentstore I’m going to build the following parts with each designed to be independent of others.
index – This is going to handle creating and reading the “fast” lookups.
documentstore – This is going to handle the management of documents.
indexer – This is going to be responsible for taking a document, breaking it apart and passing it off to the index and possibly documentstore for storage.
search – This is going to be responsible for parsing the query, querying the index and documentstore to get the results
ranker – This is going to be responsible for ranking the results somehow and will be used by search to order results
That should be pretty much all we need to download a portion of the web, start indexing and serve up some results.
THE CRAWLER
In order to crawl you need to come up with a list of URL’s. There are a few common ways to do this. The first is to seed your crawler with a few links which contain lots of other links (eg Yahoo, Digg, Slashdot, HackerNews) crawl them and harvest as you go. Another is to download a list of millions of URL’s and use that. Off the top of my head I can think of two, the first being DMOZ.org. You can download their human created list of URL’s for free. The other is to download [this list from Quantcast of the top 1 million websites][9]. For this im going to go with the Quantcast option simply because for basic searches such as “Youtube” “Yahoo Finance” it should have the results we need.
Downloading the file shows it to be in the following format,
# Quantcast Top Million U.S. Web Sites
# Rankings estimated as of Nov 27, 2012
# Copyright 2012 Quantcast Corporation
# This data is subject to terms of use described at <http://www.quantcast.com/docs/measurement-tos>
Rank    Site
1       google.com
2       youtube.com
3       facebook.com
4       msn.com
5       twitter.com
6       yahoo.com
7       amazon.com
8       wikipedia.org
9       microsoft.com
10      huffingtonpost.com
Since we are only interested in the actual sites lets write a simple parser to pull the correct data out. Its a fairly simple script really,
$file_handle = fopen("Quantcast-Top-Million.txt", "r");

while (!feof($file_handle)) {
 $line = fgets($file_handle);
 if(preg_match('/^\d+/',$line)) { # if it starts with some amount of digits
  $tmp = explode("\t",$line);
  $rank = trim($tmp[0]);
  $url = trim($tmp[1]);
  if($url != 'Hidden profile') { # Hidden profile appears sometimes just ignore then
   echo $rank.' http://'.$url."/\n";
  }
 }
}
fclose($file_handle);
All the above does is read in the file line by line, checks if it starts with a digit IE 0-9 and if so splits the line based on tabs and prints out the rank and the url. We keep the rank because that may be useful down the line when indexing. Using some basic shell scripting we can run it like so
php parse_quantcast.php > urllist.txt
It takes a few minutes to run but at the end we have our seed crawl list, which should be almost the same size as the inital file. I wanted to see what we were working with following this step and ran a few checks on the file,
wc -l urllist.txt
995941 urllist.txt

cat urllist.txt | sort | uniq | wc -l
995941
So there are 995941 lines in the file, and there are 995941 unique lines in there as well so a unique URL for each line. Perfect.
The other option using the DMOZ data can be parsed using the following steps. Go download the content (about 300meg) unpack it and you can begin collecting the links. I did look into using grep’s -o functionality but couldn’t get it to accept a regex allowing me to pull out just the links I wanted. I was then going to write a parser in PHP but since Python just eats these sort ot jobs, in end I used a small Python script,
grep "http" content.rdf.u8 | python parse.py | sort | uniq > urllist.txt
Where parse.py is just the following,
import re
import sys

match = re.compile("""http.*\"""")

for line in sys.stdin:
 t = match.findall(line)
 if len(t) != 0:
  print t[0].replace('"','')
The above DMOZ data gives about 4 million unique urls to crawl and use. Sadly a lot of the stuff in there is no longer current or points to sites people aren’t interested in so I will stick with the quantcast list.
DOWNLOADING
Downloading the data is going to take a while, so be prepared for a long wait. You can write a very simple crawler in PHP simply by using a file_get_contents and sticking in a url. I like simple, so lets do that.
$file_handle = fopen("urllist.txt", "r");

while (!feof($file_handle)) {
 $url = trim(fgets($file_handle));
 $content = file_get_contents($url);
 $document = array($url,$content);
 $serialized = serialize($document);
 $fp = fopen('./documents/'.md5($url), 'w');
 fwrite($fp, $serialized);
 fclose($fp);
}
fclose($file_handle);
The above essentially is a stupid singlethreaded crawler. It just loops over each url in the file, pulls down the content and saves it to disk. The only thing of note here is that it stores the url and the content in a document because we might want to use the URL for ranking and because its helpful to know where the document came from. One thing to keep in mind about the above is you may run into filesystem limits when trying to store a million documents in one folder.
At this point I quickly found is that the crawler is going to take forever to download even a small portion of the web. The reason being it is single threaded. We can fix this pretty easily with some xargs and command line fu. Another issue is that dropping about a million files into a single directory as I mentioned before is probably a bad plan. So I am going to use the hash of the file to spread it out over directories. This would also make it easier to shard in the future should the need arise.
*NB*
Be careful when using hashes with URL’s. While the square root of the number
http://www.skrenta.com/2007/08/md5_tutorial.html
of URL’s is still a lot bigger then the current web size if you do get a collision you are going to get pages about Britney Spears when you were expecting pages about Bugzilla. Its probably a non issue in our case, but for billions of pages I would opt for a much larger hashing algorithm such as SHA 256 or avoid it altogether.
First we change the crawler to be the below.
$url = trim($argv[1]);

$md5 = md5($url);
$one = substr($md5,0,2);
$two = substr($md5,2,2);

if(!file_exists('./documents/'.$one.'/'.$two.'/'.$md5)) {
 echo 'Downloading - '.$url."\r\n";
 $content = file_get_contents($url);
 $document = array($url,$content);
 $serialized = serialize($document);
 mkdir('./documents/'.$one.'/');
 mkdir('./documents/'.$one.'/'.$two.'/');
 $fp = fopen('./documents/'.$one.'/'.$two.'/'.$md5, 'w');
 fwrite($fp, $serialized);
 fclose($fp);
}
This simply checks for the arguments its supplied and expects the first argument (the one following the filename itself) to be the URL its going to download. It then hashes the URL so we know the filename and which directories need to be created. We then check if the file and save location exists, and if it dosn’t we then crawl the site, create the directories and save the content to disk.
Then with the following,
cat urllist.txt | xargs -L1 -P32 php crawler.php
We have a 32 process crawler. You can spawn more process’s if you wish, just increase the -P32 to whatever number you prefer. Because a crawler spends most of its time making external connections waiting on network you can bump the number quite high, certainly 100 or so on a single core machine should be fine, however that may crash your router (like it did to mine) so be careful and keep an eye on it. After crashing my router a few times I ran the process on a proper server and let it run over a day or so.
Run it for a few days or however long it takes and you will have a large chunk of web data sitting on your disk ready for indexing.
You may want to split the urllist using “split -l 10000” or some other line size and pull down each one separately. This might also be an idea if you are sharing your internet connection and don’t want to saturate it totally for days on end.
One thing to keep in mind with this is that dumping a million documents all over the disk is terribly inefficient. You should be laying down the documents in large files and keeping the locations of said documents. This makes processing much faster as you can access the disk in a long seek (although for a SSD this is probably a moot point). For a real search engine IE billions of documents do not do the above. However for something small scale this is perfectly fine.
With that done I think we can cross off the crawler. Real world crawling of course isn’t quite that simple. Eventually you need to consider refreshing your content, finding new links, avoiding overtaxing servers (which might have multiple domains on it), avoiding crawling admin pages which have delete links, improving performance (caching DNS lookups) etc… but for our purposes to refresh the index you can just re-crawl things the same way, and for a small portion of the web it should be fine.
THE INDEX
When I approach things in a test driven development manner I like to use a bottom up approach. It makes sense to me to begin with the feature that is least coupled to everything else. The standard search engine index is usually an inverted index of which there are two main types. The first is a record level index which contains a list of references to documents for each word/key. The second is a full inverted index which includes the locations/positions of each word in the document. For the sake of simplicity I am going to build the first. This means we cannot do a fast proximity search for terms, but we can always add this later.
I decided that the index I was going to create should only have a few very simple responsibilities. The first is that it needs to store its contents to disk and retrieve them. It also needs to be able to clear itself when we decide to regenerate things. The last thing that would be useful is to have it validate documents that its storing. With these simple tasks defined I wrote the following interface,
interface iindex {
 public function storeDocuments($name,array $documents);
 public function getDocuments($name);
 public function clearIndex();
 public function validateDocument(array $document);
}
which does pretty much every task I require. The reason for the interface is that I can write unit tests against just the interfaces without worrying about the implementation, and if required change how the backend works. Now we have what we are going to code against we need to have a long think about how we are going to implement this.
For storing the documents I decided to go with the simplest thing that could possibly work which is a single folder index where each index file is stored in a separate file in a single directory. The documents in the index will be represented by 3 integers in an array like so,
array(inta,intb,intc);
This gives us enough space to store a document id for lookups, and another two spaces to store a simple pre-rank, word count or possibly use some bit logic to store 32 or so signals when indexing (more on this in the indexing part). This means that each single document we are going to store requires 12 bytes. Lets assume that a document contains about 500 unique keywords and we can use some simple math to guess the size of the index,
((12 x 1,000,000 x 500) / 1024) / 1024 = 5722 Megabytes
almost 6 gigabytes which isn’t an outlandish size, and certainly easily stored on a single machine. Even if we double the index and even the assumed number of unique keywords we are still looking at less than 30 gigabytes which is easily done. Keep in mind however that we are writing a very slow index solution at this point and its unlikely that it will scale to this size. We will adjust it later to cope with this size.
So having defined the interface and how the documents look on disk lets look into implementing this. Im not going to refer to the tests here, but suffice to say the whole thing was developed using them in your standard TDD approach. The first method I think we needed to tackle is validatedocument.
define('SINGLEINDEX_DOCUMENTCOUNT', 3);

public function validateDocument(array $document=null) {
 if(!is_array($document)) {
  return false;
 }
 if(count($document) != SINGLEINDEX_DOCUMENTCOUNT) {
  return false;
 }
 for($i=0; $i &lt; SINGLEINDEX_DOCUMENTCOUNT;$i++) {
  if(!is_int($document[$i]) || $document[$i] &lt; 0) {
   return false;
  }
 }
 return true;
}
Essentially this is what I have come up. Basically it just checks that the document supplied is an array and that it contains 3 integers which are greater then zero. The next function we need is storeDocuments.
public function storeDocuments($name, array $documents = null) {
 if($name === null || $documents === null || trim($name) == '') {
  return false;
 }
 if(!is_string($name) || !is_array($documents)) {
  return false;
 }
 foreach($documents as $doc) {
  if(!$this->validateDocument($doc)){
   return false;
  }
 }
 $fp = fopen($this->_getFilePathName($name),'w');
 foreach($documents as $doc) {
  $bindata1 = pack('i',intval($doc[0]));
  $bindata2 = pack('i',intval($doc[1]));
  $bindata3 = pack('i',intval($doc[2]));
  fwrite($fp,$bindata1);
  fwrite($fp,$bindata2);
  fwrite($fp,$bindata3);
 }
 fclose($fp);
 return true;
}
The above is what I came up with. It takes in an name (the word we are storing) and an array of documents to store. Essentially all its doing is writing the integers (4 bytes each) to a binary file. The only unusual thing happening is the new method _getFilePathName which when supplied a name (the word we are storing) returns a string which contains where the index is to be stored and its name. This function just looks like this,
public function_getFilePathName($name) {
 return INDEXLOCATION.$name.SINGLEINDEX_DOCUMENTFILEEXTENTION;
}
Where INDEXLOCATION needs to be defined somewhere (enforced in the constructor) and the file extention is in the index file. The reason for the INDEXLOCATION to be defined outside this file is that we don’t want to work it out ourselves but have the developer using this code define where the index should live.
The next method we need is to get a document list, getDocuments.
public function getDocuments($name) {
 if(!file_exists($this->_getFilePathName($name))) {
  return array();
 }
 $fp = fopen($this->_getFilePathName($name),'r');
 $filesize = filesize($this->_getFilePathName($name));
 if($filesize%SINGLEINDEX_DOCUMENTBYTESIZE != 0) {
  throw new Exception('Filesize not correct index is corrupt!');
 }
 $ret = array();
 for($i=0;$i&lt;$filesize/SINGLEINDEX_DOCUMENTBYTESIZE;$i++) {
  $bindata1 = fread($fp,SINGLEINDEX_DOCUMENTINTEGERBYTESIZE);
  $bindata2 = fread($fp,SINGLEINDEX_DOCUMENTINTEGERBYTESIZE);
  $bindata3 = fread($fp,SINGLEINDEX_DOCUMENTINTEGERBYTESIZE);
  $data1 = unpack('i',$bindata1);
  $data2 = unpack('i',$bindata2);
  $data3 = unpack('i',$bindata3);
  $ret[] = array($data1[1],
      $data2[1],
      $data3[1]);
 }
 fclose($fp);
 return $ret;
}
Its actually more complex then the write function because we need to know the number of bytes to get. An integer on a 32 bit x86 system in PHP is 4 bytes. So a document consists of 12 bytes since we said it would have 3 integers. We then just suck it all into a large array and return the whole thing. I did add a simple naive corrupt index check here just to make sure that we don’t have any unexpected issues caused by bad writes. Of course this just means it will throw corrupt errors which isn’t much better.
The last method defined is the clear index. This is the simplest function to write in this case and looks like the below,
public function clearIndex() {
 $fp = opendir(INDEXLOCATION);
 while(false !== ($file = readdir($fp))) {
  if(is_file(INDEXLOCATION.$file)){
   unlink(INDEXLOCATION.$file);
  }
 }
}
It just loops over each file in the index directory and deletes them all. Simple stuff really.
Phew! not too much code with the whole file just being over 100 lines, and provides us something that will store an index and pull it back for us. I actually ended up writing 300 lines of test code to really stress this logic and make sure everything works as expected and it seems pretty solid. Some of the tests are pure unit tests and a lot actually write through to disk. Not pure unit tests, but since they are pretty fast we can consider them unit enough. Besides without mocking the file-system this class would be pretty stupid to test otherwise.
THE DOCUMENT STORE
The document store is a somewhat unusual beast in that odds are if you are going to index things you probably already have what you wanted stored somewhere. The most obvious case being documents in a database, or documents that already exist. This means we really do need an interface so we can change the underlying structure of the document store as we go on without having to rewrite things over and over. Hence I came up with the following,
interface idocumentstore {
 public function storeDocument(array $document);
 public function getDocument($documentid);
 public function clearDocuments();
}
Nice and simple. Store a document which is just an array of values and returns a document id, get a document by id and clear all the documents stored. The implementation is similar to index store above and the key parts included below. For testing purposes I created a very simple single folder document store file. I will use this implementation to get everything working at first and then hook into our crawlers downloaded documents.
storeDocument

$docid = $this->_getNextDocumentId();
$serialized = serialize($document);
$fp = fopen($this->_getFilePathName($docid), 'a');
fwrite($fp, $serialized);
fclose($fp);
return $docid;
getDocument

$filename = $this->_getFilePathName($documentid);
if (!file_exists($filename)) {
 return null;
}
$handle = fopen($filename, 'r');
$contents = fread($handle, filesize($filename));
fclose($handle);
$unserialized = unserialize($contents);
return $unserialized;
clearDocuments
$fp = opendir(DOCUMENTLOCATION);
while(false !== ($file = readdir($fp))) {
 if(is_file(DOCUMENTLOCATION.$file)){
  unlink(DOCUMENTLOCATION.$file);
 }
}
Each one is pretty simple to follow through. Store document just serialises the document to disk. Get document unserialises it and clear deletes every document in the documentstore. Odds are we will want a database version down the line as this is massively inefficient but for the moment this should serve us well.
THE INDEXER
The next step in building our search is to create an indexer. Essentially it takes in a document, breaks it apart and feeds it into the index, and possibly the document store depending on your implementation. A simple interface like the following should get us going,
interface iindexer {
 public function index(array $documents);
}
With that defined lets build a naive indexer. We are going to take in a list of documents, save it to disk, clean them up, split by spaces, build a concordance (list of words and how often they occur in the document) and the use this to feed into our indexer and our document store.
public function index(array $documents) {
 if(!is_array($documents)) {
  return false;
 }
 foreach($documents as $document) {
  $id = $this->documentstore->storeDocument(array($document));
  $con = $this->_concordance($this->_cleanDocument($document));
  foreach($con as $word => $count) {
   $ind = $this->index->getDocuments($word);
   if(count($ind) == 0) {
    $this->index->storeDocuments($word,array(array($id,$count,0)));
   }
   else {
    $ind[] = array($id,0,0);
    $this->index->storeDocuments($word,$ind);
   }
  }
 }
 return true;
}
Pretty simple and does exactly what we have just mentioned. We take in an array of documents look over them, store them and create our concordance then for each word add them to our index with the document id and the count of the document.
INDEXING
Now that we have the ability to store and index some documents lets throw some code together which actually does so. The first thing is to set everything up and then pass in some documents to index.
set_time_limit(0);
define('INDEXLOCATION',dirname(**FILE**).'/index/');
define('DOCUMENTLOCATION',dirname(**FILE**).'/documents/');

include_once('./classes/naieveindexer.class.php');
include_once('./classes/singlefolderindex.class.php');
include_once('./classes/singlefolderdocumentstore.class.php');

$index = new singlefolderindex();
$docstore = new singlefolderdocumentstore();
$indexer = new naieveindexer($index,$docstore);
The first thing we do is set the time limit to unlimited as the indexing might take a long time. Then we define where the index and the documents are going to live to avoid the errors being throw further down the line. If you are following along you will need to allow whatever user php is running under to have the ability to at least write to these directories. The next 3 lines are including the relevant classes and the last 3 are setting the index document store and indexer up.
With that done we can finally add some documents to be indexed.
$indexer->index(array('Setting the AuthzUserAuthoritative directive explicitly to Off allows for user authorization to be passed on to lower level modules (as defined in the modules.c files) if there is no user matching the supplied userID.'));
$indexer->index(array('The Allow directive affects which hosts can access an area of the server. Access can be controlled by hostname, IP address, IP address range, or by other characteristics of the client request captured in environment variables.'));
$indexer->index(array('This directive allows access to the server to be restricted based on hostname, IP address, or environment variables. The arguments for the Deny directive are identical to the arguments for the Allow directive.'));
$indexer->index(array('The Order directive, along with the Allow and Deny directives, controls a three-pass access control system. The first pass processes either all Allow or all Deny directives, as specified by the Order directive. The second pass parses the rest of the directives (Deny or Allow). The third pass applies to all requests which do not match either of the first two.'));
$indexer->index(array('The AuthDBDUserPWQuery specifies an SQL query to look up a password for a specified user.  The users ID will be passed as a single string parameter when the SQL query is executed.  It may be referenced within the query statement using a %s format specifier.'));
$indexer->index(array('The AuthDBDUserRealmQuery specifies an SQL query to look up a password for a specified user and realm. The users ID and the realm, in that order, will be passed as string parameters when the SQL query is executed.  They may be referenced within the query statement using %s format specifiers.'));
The above are just some Apache directives taken from this list [http://searchcode.com/lists/list-of-apache-directives][10]. If you have a look in the folders defined, those being documents and index you can see the the documents actually being stored. At this point we can pat ourselves on the back for a job well done or we can knuckle down and write the search class so we can actually see if it works. Lets go with the latter.
SEARCHING
Searching requires a relatively simple implementation. So simple in fact we only require a single method.
interface isearch {
 public function dosearch($searchterms);
}
Of course the actual implementation can get pretty hairy. The reason for this is that a search is actually more complex then it first appears. Take for example the following search term “cool stuff”. When someone searches for “cool stuff” they are expecting that a list of documents containing the words cool and stuff will appear in a list. What is actually happening under the hood however is a lot more work. The search term firstly needs to be parsed into a query. In the case of a default AND engine you need to find all documents containing the word “cool”, and then all documents containing the word “stuff”, get the intersection of those documents, rank them in order of relevance and return them to the user.
Sticking to keeping it very simple we are going to do the following. Clean up the search term (removing characters that have no meaning), break it into individual works separated by spaces and then for each term just return all the documents that match. No ranking, or AND logic which makes things much simpler to work with. So we will effectively end up with an OR logic search engine.
public function dosearch($searchterms) {
 $doc = array();
 foreach($this->_cleanSearchTerms($searchterms) as $term) {
  $ind = $this->index->getDocuments($term);
  if($ind != null) {
   foreach($ind as $i) {
    $doc[] = $this->documentstore->getDocument($i[0]);
   }
  }
 }
 return $doc;
}

public function _cleanSearchTerms($searchterms) {
 $cleansearchterms = strtolower($searchterms);
 $cleansearchterms = preg_replace('/\W/i',' ',$cleansearchterms);
 $cleansearchterms = preg_replace('/\s\s+/', ' ', $cleansearchterms);
 return explode(' ',trim($cleansearchterms));
}
The function _cleanSearchTerms takes in the terms, removes all non A-Z 0-9 characters using a regex and then removes all duplicate spaces. It then splits it up by a single space and returns the array. We then just loop over each of the terms query the index for the matching documents, then for each document that matches fetch it from the document store and finally return the list. It means we will get duplicate results where you have terms that are in the same document however.
With the ability to search lets plug it into a simple PHP page and actually display the results.
define('INDEXLOCATION',dirname(**FILE**).'/index/');
define('DOCUMENTLOCATION',dirname(**FILE**).'/documents/');

include_once('./classes/naieveindexer.class.php');
include_once('./classes/naievesearch.class.php');
include_once('./classes/singlefolderindex.class.php');
include_once('./classes/singlefolderdocumentstore.class.php');

$index = new singlefolderindex();
$docstore = new singlefolderdocumentstore();
$indexer = new naieveindexer($index,$docstore);
$search = new naievesearch($index,$docstore);

echo '&lt;ul>';
foreach($search->dosearch($_GET['q']) as $result) {
 echo '&lt;li>'.$result[0].'&lt;/li>';
}
echo '&lt;/ul>';
Nothing fancy here, just set everything up, then do a search through our new function and loop over the results. A sample search for “AuthzUserAuthoritative” gives back the correct result, whereas searching for “user” gives back the 3 expected results.
Hurray! At this point we have done it. We have a minimalist implementation of a search engine. I did some further tests and discovered that this actually holds together to about 50,000 documents. Searches are still reasonably quick at this level however indexing a single document took minutes which is hardly optimal. For the moment however we can index 1,000 or so documents while we work on getting the search to have some additional functionality such as ranking.
RANKER
The ranking of search results is the core of search engines secret sauce. Nobody with the knowledge how how it works really discusses how Google and Bing rank things.
*NB*
ProCog has an open algorithm, see here
http://procog.com/help/rank_details
We know they use many signals such as page speed, keywords links, title etc… but the details are still a mystery. Thankfully there are many published methods of ranking which we can explore. Any sort of search on this and you will turn up papers on things like BM25 and Vector Spaces. Once again we are going to take the simplest approach and just use the number of words in the document. So if you search for “cat” a document with two “cat” words in it will be ranked higher then one with a single instance of “cat”. We are already storing this information in the index so it should be fairly simple the implement. Later we will look some more complex ways of ranking.
Essentially the ranker can be very simple as it only needs to provide a function which we can plug into PHP’s usort function.
interface iranker {
 public function rankDocuments($document,$document2);
}
The implementation is pretty simple really,```
public function rankDocuments($document,$document2) {
if(!is_array($document) || !is_array($document2)) {
throw new Exception(‘Document(s) not array!’);
}
if(count($document) != 3 || count($document2) != 3) {
throw new Exception(‘Document not correct format!’);
}
if( $document[1] == $document2[1] ) {
return 0;
}
if( $document[1] <= $document2[1] ) {
return 1;
}
return -1;
}
All we do is validate the input then based on the wordcount (which we kept in the second location of each document) we return 1 -1 or 0. This is then fed into usort like the following,
usort($results, array($this->ranker, ‘rankDocuments’));
Which sorts the $results in place. With that we can add it to our naievesearch implementation and see how it all works together. At line 21 of our search naievesearch implementation we just insert the following,

```usort($ind, array($this->ranker, 'rankDocuments'));```

We can now go to our search page and see how things look. A sample search for the word "order" returns two documents with the first containing two instances of the word order and the second only one. Trying again with the word "the" has the same result with the first result having the word "the" 7 times compared to the last result with 4 instances of the word "the".

### INITIAL RESULTS

The nice thing at this point is we actually have a fully functioning search index written in pure PHP. In theory this should be good to integrate at this point with any small website. In its present form the search should hold up to less then 10,000 documents without too many issues. My thinking is that read/write time of each of the index shards during the indexing process would be the main bottleneck in its present form. If you indexed as you add things however IE don't do it in batch this indexer might serve to a much larger size. Other problems are that the ranking algorithm is fairly crude and that duplicate results are returned where two keywords match the same document. So while you could use this on a live site you wouldn't want to.

I did a quick test of this implementation using 5000 posts from various RSS feeds to see how things fared. While searches remain reasonably quick the index time became slower and slower as it progressed. Chucking it through a profiler showed my previous assumption to be correct and that a lot of time is spent reading/writing shards. This makes the implementation totally unpractical for indexing more then say 10,000 documents, its just too slow.

Of course this isn't what we set out to do. The goal was to index one million documents and search on them.

Over the next few steps we will profile the application, work out where the performance issues lie and then work on improving our implementation so that we can index and serve queries on a million documents. To start we will run things through a profiler and see what can be improved.

You can download a copy of the application as it currently stands here.

[PHPSearch\_Implementation\_1.zip][11]

This is the end of Part 1. In Part 2 we are going to see if we can improve some of the main issues and index up-to 100,000 documents.

**\*NB\*** I stopped developing the unit tests at this point mostly due to time pressures caused by family life. I still wanted to release the whole article though and something had to give.

 [1]: https://leanpub.com/creatingasearchenginefromscratch
 [2]: http://www.boyter.org/2013/01/code-for-a-search-engine-in-php-part-1/"
 [3]: http://www.boyter.org/2013/01/code-for-a-search-engine-in-php-part-2/
 [4]: http://www.boyter.org/2013/01/code-for-a-search-engine-in-php-part-3/
 [5]: http://www.boyter.org/2013/01/code-for-a-search-engine-in-php-part-4/
 [6]: http://www.boyter.org/2013/01/code-for-a-search-engine-in-php-part-5/
 [7]: http://www.boyter.org/2013/01/code-for-a-search-engine-in-php-part-5/#downloads
 [8]: http://queue.acm.org/detail.cfm?id=988407
 [9]: http://ak.quantcast.com/quantcast-top-million.zip
 [11]: http://www.boyter.org/wp-content/uploads/2013/01/PHPSearch_Implementation_1.zip
