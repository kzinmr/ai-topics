---
title: "Errors in Search"
url: "https://boyter.org/2012/01/errors-in-search/"
fetched_at: 2026-05-05T07:02:05.956279+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Errors in Search

Source: https://boyter.org/2012/01/errors-in-search/

EDIT
– This has now been resolved. All the below searches should work correctly, with the exception of XCompositeGetOverlayWindow. I am adding that to the index to be refreshed sometime in the next month or so.
Well thanks to some sample searches being thrown against the codesearch index I can finally start tuning issues that have cropped up. The main issue I have currently is searches returning no results where you would expect some. Some examples are included below.
[/com.google.gwt.*A/ ext:java][1]
[/sql.append.*se/ ext:java][2]
[/memcpy.*sizeof/][3]
[/com.google.gwt.*AsyncCallback/ ext:java][4]
[/XCompositeGetOverlayWindow/][5]
Most of the problems I found were during my outage window which is good to discover. With the exception of the last query above which returns nothing due to the index not having X.org indexed (yet) all issues are due to a undiscovered bug.
Take the following example,
/memcpy.*sizeof/
The problem is the way which I interpreted the regex. Essentially on the back-end a lot of the regex is expanded out fully for a certain amount of cases and a list of matches are generated. This is to ensure that it can run quickly. Think of it as precaching every possible regex against all lines in all the files. The problem in this case is that I have a unit test case missing. I never included a test which matched the above and because of this there is a bug in the way that is expanded out to match everything. A modified version of the above which does return results is,
[/memcpy.* sizeof/][6]
The above query returns results as would be expected. In fact all of the ones above can be rewritten to work correctly. Such as the below,
[/com.google.gwt.* A/ ext:java][7]
[/sql.append.* se/ ext:java][8]
[/memcpy.* sizeof/][6]
[/com.google.gwt.* AsyncCallback/ ext:java][9]
If you try the above queries you will see they act as expected. I will be updating code shortly to take this case into consideration, and of course post an update here.
[1]:
http://searchco.de/?q=/com
.google.gwt.
A/ ext:java
[2]:
http://searchco.de/?q=/sql
.append.
se/ ext:java
[3]:
http://searchco.de/?q=/memcpy
.
sizeof/
[4]:
http://searchco.de/?q=/com
.google.gwt.
AsyncCallback/ ext:java
[5]:
http://searchco.de/?q=/XCompositeGetOverlayWindow/
[6]:
http://searchco.de/?q=/memcpy
.
sizeof/
[7]:
http://searchco.de/?q=/com
.google.gwt.
A/ ext:java
[8]:
http://searchco.de/?q=/sql
.append.
se/ ext:java
[9]:
http://searchco.de/?q=/com
.google.gwt.
AsyncCallback/ ext:java
