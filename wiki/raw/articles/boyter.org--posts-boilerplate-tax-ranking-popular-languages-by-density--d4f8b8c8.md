---
title: "Boilerplate Tax - Ranking popular programming languages by density"
url: "https://boyter.org/posts/boilerplate-tax-ranking-popular-languages-by-density/"
fetched_at: 2026-05-05T07:01:53.837256+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Boilerplate Tax - Ranking popular programming languages by density

Source: https://boyter.org/posts/boilerplate-tax-ranking-popular-languages-by-density/

I was looking through
Google Scholar
the other day looking for references to
scc
since I had previously had people reach out to me about how they were using it for their thesis (It’s not narcissism, its research I swear!). I was curious to see how it was being used. One thing that I noticed was how researchers were using it to measure size of projects. A valid use case IMHO. However I was surprised about the lack of use of some of the more interesting features in
scc
.
A while ago I wrote about a new code measurement in
scc
called
ULOC (Unique Lines of Code)
. In the interests of respecting your time here is the relevant quote from it,
In my opinion, the number this produces should be a better estimate of the complexity of a project. Compared to SLOC, not only are blank lines discounted, but so are close-brace lines and other repetitive code such as common includes. On the other hand, ULOC counts comments, which require just as much maintenance as the code around them does, while avoiding inflating the result with license headers which appear in every file, for example.
This is a measure that has been in
scc
for about 2 years now, and yet not used once. Which probably makes sense as I finished that post with,
Anyway is this useful? I have no idea.
What I really needed was to calculate ULOC over a lot of repositories. I could then objectively say what is a normal value or not. For example we all know Go has more boilerplate repetition than Rust, but by how much?
I didn’t want to run it over millions of repositories, but how about the top 1,000 or so? A brief search turned up this GitHub repository
https://github.com/EvanLi/Github-Ranking/
which contains the top 100 repositories for different languages! Perfect. I cloned it down and it looks like it would be perfect for this test.
Turn’s out
scc
is not in the top 100 most starred GitHub repositories… sadge…
Even better since it has the repositories grouped by language I can narrow down to just that language avoiding all noise. Note that this has some issues because for C/C++ I would not be looking at the headers, but considering headers with a lot of logic are likely header import libraries that seemed acceptable.
In the interests of time, I turned to Google Gemini to generate a simple python script to do the work for me. Since I knew exactly what I wanted I could spec out a close to one shot prompt of what I needed.
I need a Python script.

It is going to do the following. Accept an argument to a directory. Look through that directory for .md markdown files. It needs to extract the name of the file minus the extension, so `java.md` would become `java`. It then opens each file and looks through each line to find github repositories, the format looks like this,

| 1 | [JavaGuide](https://github.com/Snailclimb/JavaGuide) | 153711 | 46107 | Java | 74 | Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发与系统设计。准备后端技术面试，首
选 JavaGuide！ | 2026-01-31T15:55:16Z |
| 2 | [hello-algo](https://github.com/krahets/hello-algo) | 122078 | 14820 | Java | 6 | 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、English、日本語，提供 Python, Java, C++, C, C#, JS, Go, Swift, Rust, Ruby, Kotlin, TS, Dart 等代码实现 | 2026-01-23T10:40:44Z |

It extracts each https link to the repository, and adds .git on the end and saves it to a list.

Once done we then iterate the list doing a few things things.

1. Run a shell command out to git to clone the repository using a shallow clone. It should happen in the /tmp/ directory.
2. Run the scc tool (its installed globally) with arguments `scc -u -a --format sql  | sqlite3 ../ code.db` On the first run it should run `sql` then after run `sql-insert` . We should change to the directory first so we run at its root, but redirect the output one down so it remains
3. Clean up the directory cloned by deleting it

It should then exit the program.
With that done I had a
script
and could get to work. I ran it on my desktop and promptly went to bed. The next morning I had a SQLite database with every calculation. At least I thought I did. It uncovered a bug in
scc
which I have since
resolved
. So I queued up the run again and waited for the result, a 472 MB sqlite file.
So a few queries to know what we are working with.
sqlite> select count(*) from t;
2703656
sqlite> select sum(nCode) from t;
410529727
sqlite> select sum(nBlank) from t;
64972188
sqlite> select sum(nComment) from t;
65967492
sqlite> select count(*) from metadata;
3418
400 million lines of code ought to be enough for any sort of comparison!
My first query was to find out what is the uniqueness percentage across all languages. Uniqueness being take all the lines in a file, throw away anything thats a duplicate with the sum that remains being the unique count.
sqlite> SELECT
    Language,
    SUM(nCode + nComment + nBlank) as Total_Physical_Lines,
    SUM(nUloc) as Total_Unique_Lines,
    ROUND(CAST(SUM(nUloc) AS FLOAT) / SUM(nCode + nComment + nBlank) * 100, 2) as Uniqueness_Percentage
FROM t
WHERE (nCode + nComment + nBlank) > 0
GROUP BY Language
ORDER BY Uniqueness_Percentage DESC;

Shell|1041730|796519|76.46
Clojure|2206584|1670455|75.7
MATLAB|2989986|2164924|72.41
Vim Script|3778425|2724477|72.11
DM|53682824|37744972|70.31
Haskell|6286404|4283395|68.14
Perl|5953028|4038887|67.85
CoffeeScript|548420|371519|67.74
TeX|688517|455517|66.16
Kotlin|10001887|6489270|64.88
Scala|11267790|7281749|64.62
R|1975720|1271846|64.37
LaTeX|559617|358979|64.15
Java|55428466|34815209|62.81
PHP|18955944|11853895|62.53
Julia|2889492|1802993|62.4
Python|20974088|12963942|61.81
Ruby|13991320|8494290|60.71
TypeScript|27889057|16737261|60.01
Objective C|2567016|1534656|59.78
C++|62955292|37198201|59.09
ActionScript|6975719|4114080|58.98
C|64288288|37008874|57.57
Swift|4493217|2581337|57.45
JavaScript|15048799|8626131|57.32
Groovy|3587705|2044644|56.99
Rust|20738501|11777964|56.79
Go|46418301|25911541|55.82
Elixir|3870450|2132232|55.09
Dart|14691026|7846238|53.41
Powershell|2494712|1315880|52.75
C#|40139432|20418679|50.87
HTML|2597758|1238299|47.67
CSS|2160131|977208|45.24
Lua|7333761|2874755|39.2
Interesting. This suggests what we probably knew already, that things like shell scripts are generally bespoke hence having the most uniqueness. However I suspect there are outliers ruining the results here. There is no good reason for Lua to be at the bottom of the list. Lets try again trying to average them out,
sqlite
>
SELECT
Language
,
COUNT
(
DISTINCT
Project)
as
Repo_Count,
ROUND(
AVG
(Project_Dryness),
2
)
as
Dryness
FROM
(
SELECT
Project,
Language
,
-- DRYness = ULOC / (Code + Comment + Blank)
(
CAST
(
SUM
(nUloc)
AS
FLOAT)
/
NULLIF
(
SUM
(nCode
+
nComment
+
nBlank),
0
)
*
100
)
as
Project_Dryness
FROM
t
GROUP
BY
Project,
Language
)
WHERE
Project_Dryness
IS
NOT
NULL
GROUP
BY
Language
ORDER
BY
Dryness
DESC
;
Note that this is applied per file, per repository. This has a few benefits,
It normalizes for project size somewhat
It reduces the influence of massive monorepos
It better isolates language idioms/boilerplate
Language
Repo Count
Dryness
Clojure
100
77.91%
Haskell
99
77.25%
MATLAB
105
75.72%
DM
99
74.41%
Shell
82
72.24%
TeX
62
71.81%
Vim Script
95
70.4%
CoffeeScript
99
70.05%
R
100
68.11%
Python
100
67.78%
Lua
99
67.77%
Kotlin
100
67.72%
Julia
100
67.4%
LaTeX
38
67.23%
Perl
86
67.03%
Scala
99
66.1%
Dart
99
65.79%
ActionScript
98
65.74%
Java
100
65.72%
Groovy
93
64.58%
JavaScript
98
64.52%
Powershell
101
63.73%
TypeScript
100
63.34%
Swift
100
63.28%
Objective C
120
63.15%
HTML
99
62.76%
Ruby
95
62.73%
PHP
100
62.05%
Rust
100
60.5%
C
98
59.71%
C++
100
59.33%
Elixir
100
58.97%
Go
99
58.78%
C#
99
58.4%
CSS
99
58.24%
Much better. This actually fits in what I would expect. Lisp style languages at the top, with scripts and other non reusable things just below. The same thing to the bottom languages which as you would expect have more repetition.
Coffeescript is an interesting case. As it was designed to be terse, it beats out TypeScript when it comes to being concise. You could use this to point out that the modern tooling increased the redundancy of the codebase compared to the terse era of old, as even JavaScript has more unique code.
What strikes me right away is that Java is a lot more DRY than I would have initially guessed! Was is really interesting is that this “proves” that modern doesn’t always mean cleaner or more DRY. The other JVM Languages are interesting too. Java is not as bad as you would first think compared to Groovy, Scala and Kotlin (lets ignore clojure here as its a different programming paradigm). Groovy having less uniqueness probably makes sense given that its used in DevOps scripting a fair bit, and if you have ever used CloudFormation or Terraform are aware how much repetition goes on there. What we can say though is that it looks like Kotlin didn’t just make Java prettier, it made it more dense.
Clojure and indeed all lisp style languages are the final boss of density here though. Almost every line is an expression of business logic. I never really got into it myself, but looking at these results are starting to make me rethink that decision.
If you compare Clojure (77.91%) to C# (58.4%), it seems the average C# developer writes 20% more redundant code every single day just to satisfy the compiler. Even with tools like resharper and LLM’s to help thats not a insignificant amount of effort.
Although I previously claimed
we all know Go has more boilerplate repetition than Rust
(I write blog posts as I go BTW and don’t revise statements like that as results come in) but as it turns out they are almost identical in their redundancy footprint. Looking at the data suggests they are much closer than you think.
The Go Zealot: “Go is simple!” “Yes, so simple you write the same thing over and over.”
The Rust Zealot: “Rust is perfectly expressive!” “Yes, but you spend 40% of your time in setup code and trait impls.”
So there it is. The dryness in order against each language. A baseline I can add to the scc repository as an example of what is considered average across very popular repositories.
Interpreting Dryness,

- 75% (High Density): Very terse, expressive code. Every line counts. (Example: Clojure, Haskell)
- 60% - 70% (Standard): A healthy balance of logic and structural ceremony. (Example: Java, Python)
- < 55% (High Boilerplate): High repetition. Likely due to mandatory error handling, auto-generated code, or verbose configuration. (Example: C#, CSS)
We spent decades building modern languages like Go, Rust, and TypeScript to solve some of the language mistakes of old. For some cases this is a huge success. But according to the data, if you want the highest ratio of human thought to keystrokes, the winner is the 60 year old concept, Lisp running as a modern JVM language Clojure.
But perhaps the main take away is progress in a lot of languages is measured by more noise to signal.
Food for thought there. Then again, perhaps LLM’s make this all moot now anyway.
Want to do this yourself? Feel free to improve on the results! I’ll link back to you, just contact me.
