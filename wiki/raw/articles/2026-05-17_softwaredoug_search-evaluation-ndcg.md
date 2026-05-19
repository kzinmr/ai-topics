---
title: "Search Evaluation (NDCG and pals) — Cheat at Search Essentials"
author: Doug Turnbull (softwaredoug.com)
source_url: https://docs.google.com/presentation/d/1WJknXxaim_Z8aiVuQx6wr7W6MAWeaUJK0-NrgcEVQfQ
date_ingested: 2026-05-17
format: google_slides_export
tags: [search, evaluation, ndcg, information-retrieval]
---

# Search Evaluation (NDCG and pals) — Cheat at Search Essentials

**Author**: Doug Turnbull (http://softwaredoug.com)
**Source**: Google Slides

---

     1|Search Evaluation 
     2|(NDCG and pals)
     3|Cheat at Search Essentials
     4|
     5|About me
     6|Share my learnings with others
     7|
     8|Honesty a core value
     9|
    10|Still trying to figure out how search works
    11|http://softwaredoug.com 
    12|(Search since 2013, training + consulting)
    13|
    14|Vector Search + Embeddings
    15|Cheat at Search Essentials
    16|Tomorrow
    17|http://softwaredoug.com/events 
    18|
    19|http://softwaredoug.com/course 
    20|Live training - discount code vectorsrock
    21|Class starts MONDAY
    22|
    23|http://maven.com/softwaredoug/autoresearch 
    24|Just created - one day workshop
    25|
    26|
    27|https://maven.com/search-school/
    28|Tuesday
    29|
    30|This talk - ELI5
    31|How are search results evaluated?
    32|
    33|How should they be evaluated?
    34|
    35|Best practices in industry
    36|https://maven.com/softwaredoug/cheat-at-search?promoCode=ndcgrocks 
    37|
    38|The “Judgment List”
    39|Query
    40|Document
    41|Grade (0-1)
    42|Rambo
    43|Rambo III
    44|0.8
    45|Rambo
    46|First Blood
    47|1.0
    48|Rambo
    49|Forrest Gump
    50|0.01
    51|Rocky
    52|Rocky Balboa
    53|0.9
    54|Rocky
    55|Creed
    56|0.8
    57|Rocky
    58|Rambo
    59|0.5
    60|aka ground truth, relevance labels, judgments, etc etc
    61|
    62|Where do these numbers come from?
    63|Query
    64|Document
    65|Grade (0-1)
    66|Rambo
    67|Rambo III
    68|0.8
    69|Rambo
    70|First Blood
    71|1.0
    72|Rambo
    73|Forrest Gump
    74|0.01
    75|Rocky
    76|Rocky Balboa
    77|0.9
    78|Rocky
    79|Creed
    80|0.8
    81|Rocky
    82|Rambo
    83|0.5
    84|Clicks? Humans? LLMs?
    85|The search team? Aunt Linda?
    86|
    87|Then we get search results…
    88|WTF?
    89|👩🏽‍💻
    90|
    91|Assign a number to each (from our judgments)
    92|0.01
    93|1.0
    94|0.8
    95|
    96|Assign a weight to each position
    97|0.01
    98|1.0
    99|0.8
   100|RANK
   101|DISCOUNT (1/Rank*)
   102|1
   103|1/1
   104|2
   105|1/2
   106|3
   107|1/3
   108|* real formula 1/log2(rank+1), but I’m sticking to easy to do math
   109|
   110|Multiply GRADE * DISCOUNT
   111|GRADE
   112|RANK
   113|DISCOUNT (1/Rank)
   114|GAIN*
   115|0.01
   116|1
   117|1/1 = 1
   118|0.01 * 1 = 0.01
   119|1.0
   120|2
   121|½ = 0.5
   122|1.0 * 0.5 = 0.5
   123|0.8
   124|3
   125|⅓ = 0.333
   126|0.8 * 0.333 = 0.267
   127|* Sometimes (2^grade) -1 is taken
   128|
   129|DCG ~ Discounted Cumulative Gain
   130|GRADE
   131|RANK
   132|DISCOUNT (1/Rank)
   133|GAIN
   134|0.01
   135|1
   136|1/1 = 1
   137|0.01 * 1 = 0.01
   138|1.0
   139|2
   140|½ = 0.5
   141|1.0 * 0.5 = 0.5
   142|0.8
   143|3
   144|⅓ = 0.333
   145|0.8 * 0.333 = 0.267
   146|SUM: 0.777 
   147|“DCG at 3” or “DCG@3
   148|
   149|iDCG ~ IDEAL DCG
   150|GRADE
   151|RANK
   152|DISCOUNT (1/Rank)
   153|GAIN
   154|1.0
   155|1
   156|1/1 = 1
   157|1.0 * 1 = 1.0
   158|0.8
   159|2
   160|½ = 0.5
   161|0.8 * 0.5 = 0.4
   162|0.01
   163|3
   164|⅓ = 0.333
   165|0.01 * 0.333 = 0.0033
   166|SUM: 1.403
   167|“DCG at 3” or “DCG@3
   168|(if we could magically return the right sort order for this query, DCG would be this)
   169|
   170|NDCG ~ Divide DCG by iDCG, forces 0-1
   171|GRADE
   172|RANK
   173|DISCOUNT (1/Rank)
   174|GAIN
   175|0.01
   176|1
   177|1/1 = 1
   178|0.01 * 1 = 0.01
   179|1.0
   180|2
   181|½ = 0.5
   182|1.0 * 0.5 = 0.5
   183|0.8
   184|3
   185|⅓ = 0.333
   186|0.8 * 0.333 = 0.267
   187|0.777 / 1.403 = 0.554
   188|
   189|Search gets a bit better…
   190|GRADE
   191|RANK
   192|DISCOUNT (1/Rank)
   193|GAIN
   194|0.8
   195|1
   196|1/1 = 1
   197|0.8 * 1 = 0.8
   198|0.01
   199|2
   200|½ = 0.5
   201|0.01 * 0.5 = 0.005
   202|1.0
   203|3
   204|⅓ = 0.333
   205|1.0 * 0.333 = 0.333
   206|1.138 / 1.403 = 0.8111
   207|
   208|Goal - Get a metric how good queries are
   209|Queries
   210|How good are they
   211|rambo
   212|0.811
   213|rocky
   214|0.4
   215|Movies with tom cruise
   216|0.5
   217|
   218|Judgments from where?
   219|Run through initial setup of synonym notebook
   220|
   221|https://colab.research.google.com/drive/1aUCvcBa1YdmsbIgYc74jlknl9_iRotp1?authuser=2#scrollTo=h0-Y8MnKZnF1 
   222|
   223|Where do these numbers come from?
   224|GRADE
   225|RANK
   226|DISCOUNT (1/Rank)
   227|GAIN
   228|0.8
   229|1
   230|1/1 = 1
   231|0.8 * 1 = 0.8
   232|0.01
   233|2
   234|½ = 0.5
   235|0.01 * 0.5 = 0.005
   236|1.0
   237|3
   238|⅓ = 0.333
   239|1.0 * 0.333 = 0.333
   240|
   241|Human raters
   242|GRADE
   243|RANK
   244|DISCOUNT (1/Rank)
   245|GAIN
   246|1
   247|1
   248|1/1 = 1
   249|0.8 * 1 = 0.8
   250|0
   251|2
   252|½ = 0.5
   253|0.01 * 0.5 = 0.005
   254|1
   255|3
   256|⅓ = 0.333
   257|1.0 * 0.333 = 0.333
   258|👍
   259|👍
   260|👍
   261|
   262|Human raters - time consuming + fatiguing ⏰
   263|Raters make mistakes
   264|
   265|Human raters - assumed expertise
   266|May need to hire expert raters, not just external crowdsourced raters
   267|
   268|Human raters - explicit preference measure
   269|People don’t want their true, secret, unconscious desires to be show
   270|
   271|Relevance means: appropriateness, query / result interpretation in a public setting
   272|
   273|Search for “cybertruck” get cybertruck reviews
   274|
   275|Clickstream-based
   276|GRADE
   277|RANK
   278|DISCOUNT (1/Rank)
   279|GAIN
   280|0.8
   281|1
   282|1/1 = 1
   283|0.8 * 1 = 0.8
   284|0.01
   285|2
   286|½ = 0.5
   287|0.01 * 0.5 = 0.005
   288|1.0
   289|3
   290|⅓ = 0.333
   291|1.0 * 0.333 = 0.333
   292|Clicks, conversions, etc
   293|
   294|Clickstream - implicit preference measure
   295|Relevance == What people do in private when nobody is looking
   296|
   297|Not just NSFW, but drama, gossip, jokes
   298|
   299|Search for “cybertruck” seek out cybertruck haters
   300|
   301|Clickstream - position biases
   302|Users by default click a bit higher up or have other positional biases in how they scan results
   303|
   304|Clickstream - attractiveness biases
   305|Users just clicking more, the result sells itself better
   306|
   307|Click models -> turning clicks into judgments
   308|…clicked a lot, but higher position, so we discount those clicks…
   309|
   310|Simple click model: COEC (clicks over expected clicks)
   311|Position
   312|Expected Clicks (across all search sessions)
   313|Position Clicks
   314|(“First Blood” for query “Rambo”)
   315|COEC this posn
   316|1
   317|1000
   318|1250
   319|1250 / 1000  = 1.25
   320|2
   321|800
   322|950
   323|950/800 
   324|= 1.875
   325|3
   326|400
   327|650
   328|250/400 
   329|= 1.625
   330|AVG = 1.5833
   331|Goal: find relevance grade for “First Blood” for query Rambo using past sessions its appeared in search results and possibly clicked
   332|
   333|Clickstream-based
   334|GRADE
   335|RANK
   336|DISCOUNT (1/Rank)
   337|GAIN
   338|1
   339|1/1 = 1
   340|2
   341|½ = 0.5
   342|1.5833
   343|3
   344|⅓ = 0.333
   345|COEC Grade
   346|
   347|Query
   348|Document
   349|Rating (0-2)
   350|blue suede couch
   351|🛝
   352|?? 0
   353|blue suede couch
   354|?? 1
   355|blue suede couch
   356|🛋️
   357|2
   358|blue suede couch
   359|1
   360|🧑‍⚖️
   361| LLM Judge
   362|Instant labeling
   363|Search Engine
   364|👨🏽‍💻 Tune more
   365|LLM as a judge
   366|
   367|Query
   368|Document
   369|Rating (0-2)
   370|blue suede couch
   371|🛝
   372|?? 0
   373|blue suede couch
   374|?? 1
   375|blue suede couch
   376|🛋️
   377|2
   378|blue suede couch
   379|1
   380|🧑‍⚖️
   381| LLM Judge
   382|Instant labeling
   383|Search Engine
   384|👨🏽‍💻 Tune more
   385|LLM as a judge
   386|
   387|Keeping the party going
   388|👩🏽‍💻
   389|
   390|
   391|🧑🏼‍💻
   392|
   393|
   394|👨🏿‍💻
   395|Accuracy of LLM judge against labelers
   396|🧑‍⚖️
   397| LLM Judge
   398|Search
   399|Accuracy of search on generated labels
   400|
   401|LLM as a judge
   402|Umbrella (Lin, et. al)
   403|
   404|Given a query and a passage, provide a single integer score (0–3) in this exact format:
   405|
   406|  ##final score: [score]
   407|
   408|Do NOT output anything else or any explanation.
   409|
   410|Scoring criteria:
   411|0 = nothing to do with the query
   412|1 = related but does not answer
   413|2 = somewhat answers (answer may be unclear or buried)
   414|3 = dedicated to the query and contains exact answer
   415|
   416|Important:
   417|- Split the task into steps:
   418|  1. Consider the search intent and how well content matches (M).
   419|  2. Measure the trustworthiness of the passage (T).
   420|  3. Decide final score (O).
   421|- Format output as: ##final score: score
   422|“Chain of thought-y”
   423|Descriptive labels
   424|We now have structured outputs
   425|Focused on passages?
   426|Matters to this domain
   427|
   428|When NDCG goes wrong
   429|Run through initial setup of synonym notebook
   430|
   431|https://colab.research.google.com/drive/1aUCvcBa1YdmsbIgYc74jlknl9_iRotp1?authuser=2#scrollTo=h0-Y8MnKZnF1 
   432|
   433|Problem 1: not enough ratings
   434|GRADE
   435|1.0
   436|0.8
   437|???
   438|Nobody has rated this for “rambo” how can I eval?
   439|
   440|Solution 1 - put a 0 here
   441|Pessimistically assume its irrelevant
   442|GRADE
   443|1.0
   444|0.8
   445|0
   446|
   447|Solution 2 - NDCG-f: analyze labeled results only
   448|Send a filter to search saying “only give me this list of results in the ranking”: 
   449|
   450|q=rambo
   451|
   452|Only return:Rambo III, Rambo II, First Blood, Forrest Gump…
   453|
   454|(anything with a rating we trust)
   455|
   456|NDCG-f is like working within a sample
   457|Objective: within sample of rated results, improve relevance
   458|
   459|
   460|(And your other goal: improve the sample to represent good and bad use cases!)
   461|
   462|Problem 2: “Ideal DCG” is bad (lack of ratings)
   463|GRADE
   464|0.1
   465|0.05
   466|???
   467|Getting NDCG=1 is possible with pretty terrible search results
   468|Ideal Ranking:
   469|
   470|Solutions: better ideal DCGs
   471|GRADE
   472|1.0
   473|1.0
   474|1.0
   475|Max iDCG
   476|GRADE
   477|1.0
   478|0.8
   479|0.7
   480|Global iDCG
   481|GRADE
   482|1.0
   483|0.8
   484|0.01
   485|Local iDCG
   486|(max label everywhere)
   487|(max for all query labels)
   488|(max in retrieved top N)
   489|
   490|Solutions: better ideal DCGs
   491|GRADE
   492|1.0
   493|1.0
   494|1.0
   495|Max iDCG
   496|GRADE
   497|1.0
   498|0.8
   499|0.7
   500|Global iDCG
   501|GRADE
   502|1.0
   503|0.8
   504|0.01
   505|Local iDCG
   506|Measures Recall + Precision + Content
   507|Measures Recall + Precision
   508|Measures Precision in retrieved docs
   509|
   510|Beyond NDCG
   511|Run through initial setup of synonym notebook
   512|
   513|https://colab.research.google.com/drive/1aUCvcBa1YdmsbIgYc74jlknl9_iRotp1?authuser=2#scrollTo=h0-Y8MnKZnF1 
   514|
   515|Action Movies
   516|NDCG doesn’t measure diversity
   517|
   518|Perfect results, not Diverse
   519|
   520|NDCG doesn’t measure UI Quality
   521|
   522|Perfect results, 
   523|
   524|Boring, few clicks, poor ratings
   525|
   526|Bad “perceived relevance”
   527|
   528|NDCG requires painstaking data work
   529|
   530|Clickstream:
   531|
   532|Enough clicks?
   533|
   534|Biases in user clickstream?
   535|
   536|Enough ratings per query?
   537|
   538|Sparsity on long tail
   539|
   540|NDCG requires painstaking data work
   541|
   542|Human:
   543|
   544|What to do when raters disagree?
   545|
   546|Rating enough results per query?
   547|
   548|Rating enough queries? Are they representative?
   549|
   550|Rater education and management?
   551|👍
   552|👍
   553|👍
   554|
   555|NDCG requires interpreting the info need
   556|
   557|What’s the user’s actual intent?
   558|
   559|We don’t have enough labels
   560|Query
   561|Document
   562|Rating (0-2)
   563|blue suede couch
   564|🛝
   565|??
   566|blue suede couch
   567|??
   568|blue suede couch
   569|🛋️
   570|2
   571|blue suede couch
   572|1
   573|No label!
   574|How would we compute something like NDCG?*
   575|* note in research datasets, like WANDS, its assumed unlabeled results are irrelevant. Real life is not this simple!
   576|
   577|NDCG answers narrow questions:
   578|NDCG != ground truth
   579|
   580|NDCG:
   581|
   582|
   583|	Did I impact the queries I expected?
   584|
   585|	Did I impact them positively?
   586|
   587|	Did I impact unexpected queries?
   588|
   589|
   590|You see this experiment result
   591|Experiment goal: improve relevance of searches for movies by name
   592|Query
   593|NDCG
   594|rambo
   595|📈
   596|rocky
   597|📈
   598|movie about squirrels
   599|📈
   600|movie with arnold
   601|📉
   602|Query
   603|NDCG
   604|rambo
   605|📈
   606|rocky
   607|📈
   608|movie about squirrels
   609|(no change)
   610|movie with arnold
   611|(no change)
   612|Which would you ship?
   613|
   614|You see this experiment result
   615|Query
   616|NDCG
   617|rambo
   618|📈
   619|rocky
   620|📈
   621|movie about squirrels
   622|📈
   623|movie with arnold
   624|📉
   625|Query
   626|NDCG
   627|rambo
   628|📈
   629|rocky
   630|📈
   631|movie about squirrels
   632|(no change)
   633|movie with arnold
   634|(no change)
   635|NDCG increases more, but changes unexpected queries, so 👎
   636|NDCG targets the expected queries, so 👍
   637|Experiment goal: improve relevance of searches for movies by name
   638|
   639|You can do this without relevance judgments
   640|Query
   641|NDCG
   642|rambo
   643|(change)
   644|rocky
   645|(change)
   646|movie about squirrels
   647|(change)
   648|movie with arnold
   649|(no change)
   650|Query
   651|NDCG
   652|rambo
   653|(change)
   654|rocky
   655|(change)
   656|movie about squirrels
   657|(no change)
   658|movie with arnold
   659|(no change)
   660|NDCG increases more, but changes unexpected queries, so 👎
   661|NDCG targets the expected queries, so 👍
   662|Experiment goal: improve relevance of searches for movies by name
   663|
   664|Side-by-sides, underrated
   665|Give internal team members / domain experts two results, have them give a preference
   666|Pepsi
   667|Coke
   668|
   669|All backed by A/B tests
   670|Finally, once you make the change you expect, get it into an A/B test
   671|
   672|Take offline as a unit test, that it works as intended
   673|
   674|NOT a true “quality check”
   675|
   676|What should you do?
   677|Run through initial setup of synonym notebook
   678|
   679|https://colab.research.google.com/drive/1aUCvcBa1YdmsbIgYc74jlknl9_iRotp1?authuser=2#scrollTo=h0-Y8MnKZnF1 
   680|
   681|Doug 2010s - let’s methodically test before shipping
   682|🧑🏼‍💻
   683|💡
   684|Big Idea!
   685|🧑🏼‍💻
   686|👨🏽‍💻
   687|Careful Methodical Testing
   688|Prod
   689|Staging
   690|
   691|Doug 2025 - Just ship it
   692|🧑🏼‍💻
   693|💡
   694|Big Idea!
   695|Prod
   696|Just ship it behind feature flag
   697|(Continuous Delivery outside scope of this class, but essential IMO)
   698|
   699|PROD
   700|
   701|“Test in prod or live a lie”
   702| 
   703|Charity Majors
   704|
   705|Don’t build complex lab infra + tooling
   706|Doug’s mistake at many companies
   707|How do I build a great offline testing tool?!?
   708|How do I sample the corpus so it is representative?!?
   709|How do I gather a reasonable set of test queries
   710|How do I ensure my search engine setup matches prod?!?
   711|Are the results presented similar to the actual UI?!?
   712|
   713|A real (painful) search project
   714|Build the perfect click -> eval set
   715|6 months
   716|Actually tune search results
   717|1 month
   718|Project canceled, lack of actual impact delivered
   719|
   720|What I should have done
   721|Ship idea to prod (LGTM)
   722|Ship iteration to prod
   723|Get some side by side preferences
   724|
   725|In parallel to better measurement+continuous delivery
   726|Ship idea to prod (LGTM)
   727|Ship iteration to prod
   728|Get some side by side preferences
   729|clicks
   730|Data Warehouse
   731|Babystep begin to gather query, what was clicked
   732|
   733|Just build ways to analyze features in prod
   734|🧑🏼‍💻
   735|💡
   736|Big Idea!
   737|Prod
   738|Just ship it behind feature flag
   739|Side by side with feature on / off
   740|
   741|You can do “offline” in prod
   742|🧑🏼‍💻
   743|💡
   744|Big Idea!
   745|Prod
   746|Just ship it behind feature flag
   747|NDCG with feature on off
   748|Query
   749|NDCG
   750|rambo
   751|📈
   752|rocky
   753|📈
   754|movie about squirrels
   755|(no change)
   756|movie with arnold
   757|(no change)
   758|
   759|Another failed project
   760|Ship idea to prod (LGTM)
   761|Ship iteration to prod
   762|Get some side by side preferences
   763|clicks
   764|Data Warehouse
   765|Complex black box nobody understands
   766|⁉️
   767|Insights
   768| 🧙🏼
   769|
   770|Underappreciated complexity, team ahead of their skis
   771|👩🏽‍💻
   772|
   773|
   774|👨🏿‍💻
   775|
   776|
   777|🧑🏼‍💻
   778|👩🏽‍💻
   779|
   780|
   781|🧑🏼‍💻
   782|
   783|
   784|👨🏿‍💻
   785|Crowdsourced Labelers
   786|Rater consistency
   787|Rater expertise
   788|Rater quality
   789|“Unknown unkwowns”
   790|Wow this is a lot of work!
   791|
   792|Do the next smart thing
   793|Ship idea to prod (LGTM)
   794|Ship iteration to prod
   795|Get some side by side preferences
   796|clicks
   797|Data Warehouse
   798|💡
   799|I get this!
   800|Well understood metric with limitations
   801|Query-doc click-thru rate
   802|
   803|Other benefits
   804|🧑🏼‍💻
   805|💡
   806|Big Idea!
   807|Prod
   808|Just ship it behind feature flag
   809|Direct shadow traffic to change for perf
   810|Change lives in main 
   811|Can easily turn into A/B test
   812|Can easily be shipped to all users
   813|No weird separate “lab” world
   814|
   815|We have to build the airplane while we fly it
   816|Grug-brained 
   817|evals
   818|ship
   819|analyze
   820|
   821|Grug-brained 
   822|evals
   823|Slightly less grug-brained 
   824|evals
   825|(All while continuously shipping)
   826|