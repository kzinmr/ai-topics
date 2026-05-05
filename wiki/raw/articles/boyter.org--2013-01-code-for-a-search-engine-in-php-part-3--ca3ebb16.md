---
title: "Code a Search Engine in PHP Part 3"
url: "https://boyter.org/2013/01/code-for-a-search-engine-in-php-part-3/"
fetched_at: 2026-05-05T07:02:05.119699+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Code a Search Engine in PHP Part 3

Source: https://boyter.org/2013/01/code-for-a-search-engine-in-php-part-3/

[Are you really interested in learning how to Write a Search Engine from Scratch? Click this link and register your interest for my book about how to do so.][1]
This is part 3 of a 5 part series.
[Part 1][2] – [Part 2][3] – [Part 3][4] – [Part 4][5] – [Part 5][6] – [Downloads/Code][7]
At this point I had a large chunk of the web sitting on my disk waiting to be indexed. The first thing we need to think about is what are we going to index. Since we are dealing with HTML files we have marked up content can can pick to a certain extent what we want to index on. For our search im going to index on the title and the meta description tags. Titles are still a part of search engine ranking algorithms as many people search for things like “Yahoo” and “Facebook” and the title/URL usually contains this information. The meta description had fallen out of favor with being something search engines use these days due to being gamed, but since its unlikely the top 1 million are going to be doing this I am going to use it as well. These two terms should work fairly well at our scale and ensure our index isn’t too massive. We can always add the rest of page content at a later point.
Our first step is to loop over all of the downloaded documents, process them somehow IE extract the content we want to index and then add them into our index. Having a look at Google we can see that all we really need is the Title, Meta Description and URL to serve up a result. Lets build our documents such that they represent the above. A sample would be something like the below,```
$document = array(’
http://search.yahoo.com//
’,
‘Yahoo! Search - Web Search’,
‘The search engine that helps you find exactly what you’re looking for. Find the most relevant information, video, images, and answers from all across the Web.’);
This when stored allows us to display things nicely on the page similar to Google's results. To accommodate this lets change add.php to perform the above. The below is what I came up with.```
foreach(new RecursiveIteratorIterator (new RecursiveDirectoryIterator ('./crawler/documents/')) as $x) {
 $filename = $x->getPathname();
 if(is_file($filename)) {
  $handle = fopen($filename, 'r');
  $contents = fread($handle, filesize($filename));
  fclose($handle);
  $unserialized = unserialize($contents);

  $url = $unserialized[0];
  $content = $unserialized[1];

  // Try to extract out the title. Using a regex because its easy
  // however not correct, see http://stackoverflow.com/questions/1732348/regex-match-open-tags-except-xhtml-self-contained-tags/1732454#1732454 for more details
  preg_match_all('/&lt;title.*?>.*?&lt;\/title>/i',$content, $matches);
  $title = trim(strip_tags($matches[0][0]));

  // Turns out PHP has a function for extracting meta tags for us, the only
  // catch is that it works on files, so we fake a file by creating one using
  // base64 encode and string concaternation
  $tmp = get_meta_tags("data://$mime;base64,".base64_encode($content));
  $desc = trim($tmp['description']);

  // This is the rest of the content. We try to clean it somewhat using
  // the custom function html2text which works 90% of the tiem
  $content = trim(strip_tags(html2txt($content)));

  // If values arent set lets try to set them here. Start with desc
  // using content and then try the title using desc
  if($desc == '' && $content != '') {
   $desc = substr($content,0,200).'...';
  }
  if($title == '' && $desc != '') {
   $title = substr($desc,0,50).'...';
  }

  // If we dont have a title, then we dont have desc or content
  // so lets not add it to the index
  if($title != '') {
   $toindex[] = array($url, $title, $desc);
  }
 }
}
This needs some explaining. The foreach essentially recursively iterates over our crawled documents. We point at the directory where they live rather then copy them somewhere (why should be bother moving them?). We then check that we are looking at a file, and if so open it up, unserialize the contents and extract the URL and the content. We then go about parsing out the stuff we want. Firstly the title which we extract using a simple regex. Keep in mind parsing HTML with regex is a very bad idea. Thankfully on this sample set it works well enough that we can get away with it. Ideally we should use a XML parser. The next thing we pull out is the meta tags IE description. Thankfully this functionality already exists in PHP. Lastly we stuff the stripped content into a variable. The next step we check if there is anything missing, and assuming we have a title add it to our list to index. The final step of course would be to actually index everything.
The next thing we need to do is modify our indexer. I created a new indexer called indexer based on the slightlynaieveindexer. The only real change other then the name at this point is inside the cleanDocument function as the below.```
public function _cleanDocument($document) {
$contents = $document[0].’ ‘.$document[1].’ ‘.$document[2];
$cleandocument = strip_tags(strtolower($contents));
$cleandocument = preg_replace(’/\W/i’,’ ‘,$cleandocument);
$cleandocument = preg_replace(’/\s\s+/’, ’ ‘, $cleandocument);
if($cleandocument != ‘’){
return explode(’ ‘,trim($cleandocument));
}
return array();
}
The change is that we concatenate the 3 passed in fields URL, Title, Description and then build our concordance based on that.

So with that all done running it about 5000 documents works without to many issues. I modified search.php at this point to look like the below,```
echo '&lt;ul style="list-style:none;">';
foreach($search->dosearch($_GET['q']) as $result) {
 ?>
 &lt;li>
  &lt;a href="&lt;?php echo $result[0][0]; ?>">&lt;?php echo $result[0][1]; ?>&lt;/a>&lt;br>
  &lt;a style="color:#093; text-decoration:none;" href="&lt;?php echo $result[0][0]; ?>">&lt;?php echo $result[0][0]; ?>&lt;/a>
  &lt;p>&lt;?php echo $result[0][2]; ?>&lt;/p>
 &lt;/li>
 &lt;?php
}
echo '&lt;/ul>';
which displays the results in a similar manner to Google. Of course we still have the same issue where if you search for something like “the” you get 5000 links on the page. Lets fix this issue.
There are a few things to keep in mind with this. When you search for a term you essentially load that term’s list of documents into memory. This can take some time because you are loading a file from disk and processing it. One thing you can do to speed this up is only read the top 1000 or so documents from the file. This is slightly problematic however when it comes to ranking. If someone searches for “Yahoo” and the Yahoo homepage is document 1001 in your documents it will never appear in your results. One possible solution is to sort the documents in the index by rank against the term. IE we know that the Yahoo homepage will rank very highly for the term “Yahoo” so lets make it first in line. This way when we pull back 1000 results we know that Yahoo will be at the top. While we are at it we should probably split the terms into separate folders as well. The new index we will call multifolderindex. Changing the index to work like this is very simple. We just modify the getFilePathName like so,```
public function _getFilePathName($name) {
$md5 = md5($name);
$one = substr($md5,0,2);
mkdir(INDEXLOCATION.$one.’/’);
return INDEXLOCATION.$one.’/’.$name.SINGLEINDEX_DOCUMENTFILEEXTENTION;
}
Which then creates the folders (if required) and returns the location correctly. Nothing complex there. The other change is to limit the number of documents pulled back for each search. To do so we edit getDocuments and add the following,```
$count++;
if($count == 200) {
 break;
}
With the variable $count initialized with 0 outside the loop we now cut down on the processing time in a large way. In the future this should be passed in as an offset so we can step though results IE get deeper results, but it should be fine for the moment.
*NB*
For the final implementation I upped this number to 10,000 and got good results.
No in order for the above changes to work we when need to modify the indexer to presort our documents before passing them off to be saved. This is simple, we just pass in our existing ranker function have it rank the documents and we are done. The line to modify is inside index in our indexer,```
foreach($documenthash as $key => $value) {
usort($value, array($this->ranker, ‘rankDocuments’));
$this->index->storeDocuments($key,$value);
}
Of course we need to add ranker into the constructor as well. Now when the index hits disk it will already be presorted in favor of documents which have the word more then other documents. Later on we will adjust this to allow for the word being in the title or the URL and rank based on that. Since we are modifying a lot of stuff lets make things by default an AND engine. This involves the following change in our search class.```
function dosearch($searchterms) {
 $indresult = array(); // AND results 
 $indorresult = array(); // OR results IE everything

 $interlists = array();

 foreach($this->_cleanSearchTerms($searchterms) as $term) {

  $ind = $this->index->getDocuments($term);
  if($ind != null) {
   $tmp = array();
   foreach($ind as $i) {
    $indorresult[$i[0]] = $i[0];
    $tmp[] = $i[0];
   }
   $interlists[] = $tmp;
  }
 }

 // Get the intersection of the lists
 $indresult = $interlists[0];
 foreach($interlists as $lst) {
  $indresult = array_intersect($indresult, $lst);
 }

 $doc = array();
 $count = 0;
 foreach($indresult as $i) {
  $doc[] = $this->documentstore->getDocument($i);
  $count++;
  if($count == 20) {
   break;
  }
 }
 if($count != 20) { // If we dont have enough results to AND default to OR
  foreach($indorresult as $i) {
   $tmp = $this->documentstore->getDocument($i);
   if(!in_array($tmp, $doc)) { # not already in there
    $doc[] = $tmp;
    $count++;
    if($count == 20) {
     break;
    }
   }
  }
 }

 return $doc;
}
There is a lot going on in there but essentially we build the list as before (the OR list) but also keep each set desperately. We then take each one of those sets and get the intersection of them all. This is used as the top results, and assuming we don’t find enough revert to OR logic. Just something to keep in mind its actually easier to get AND logic when you sort lists by Id’s. You can just step through each list popping id’s on either side till you find enough intersecting results.
The final thing to update before testing is to move the document store over to a multi folder document store. Thankfully changing this one is pretty easy as well as the design is similar to the multi folder index, all we need do is update the getFilePathName method, which looks like the following.```
public function _getFilePathName($name) {
$md5 = md5($name);
$one = substr($md5,0,2);
mkdir(DOCUMENTLOCATION.$one.’/’);
return DOCUMENTLOCATION.$one.’/’.$name.DOCUMENTSTORE_DOCUMENTFILEEXTENTION;
}
### INITIAL RESULTS

With that done the document store and index are good enough to try some much larger searches. At the time I had about 20,000 documents that I could index, so I indexed the lot and had a few tests. A few thoughts from this.

1. When searching for things like "what the internet is talking about right now" the results are very slow to return.
  
2. When searching for things like the above we don't get the result we would expect which would be Digg.com
  
3. The ranking can still be pretty stupid at times for example "reverse image search" ranks emailfinder.com above tineye.com
  
4. There is a lot of porn results returned which are rather annoying, for example "flat"

All of the above need to be resolved before we can say that this implementation works well and will be the focus of Part 4.

You can download what we have from here.

[PHPSearch\_Implementation\_3.zip][8]

 [1]: https://leanpub.com/creatingasearchenginefromscratch
 [2]: http://www.boyter.org/2013/01/code-for-a-search-engine-in-php-part-1/"
 [3]: http://www.boyter.org/2013/01/code-for-a-search-engine-in-php-part-2/
 [4]: http://www.boyter.org/2013/01/code-for-a-search-engine-in-php-part-3/
 [5]: http://www.boyter.org/2013/01/code-for-a-search-engine-in-php-part-4/
 [6]: http://www.boyter.org/2013/01/code-for-a-search-engine-in-php-part-5/
 [7]: http://www.boyter.org/2013/01/code-for-a-search-engine-in-php-part-5/#downloads
 [8]: http://www.boyter.org/wp-content/uploads/2013/01/PHPSearch_Implementation_3.zip
