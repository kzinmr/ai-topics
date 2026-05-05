---
title: "Why count lines of code?"
url: "https://boyter.org/posts/why-count-lines-of-code/"
fetched_at: 2026-05-05T07:01:59.395710+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Why count lines of code?

Source: https://boyter.org/posts/why-count-lines-of-code/

A work colleague (let’s call him Owen as that’s his name) asked me the other day
“I dont understand the problem space
scc
et al solve. If you wanted to write a short post, i’d read and share the hell out of it. Basically, it seems like a heap of people can see the need for it, and I’m trying to understand it myself”
Owen is one of the more switched on people I know. As such if he is asking whats the point of tools such as scc, tokei, sloccount, cloc, loc and gocloc then I suspect quite a few other people are asking the same thing.
To quote the hero lead from a few of the tools mentioned.
scc is a very fast accurate code counter with complexity calculations and COCOMO estimates written in pure Go
cloc counts blank lines, comment lines, and physical lines of source code in many programming languages. Given two versions of a code base, cloc can compute differences in blank, comment, and source lines.
“SLOCCount” a set of tools for counting physical Source Lines of Code (SLOC) in a large number of languages of a potentially large set of programs.
Tokei is a program that displays statistics about your code. Tokei will show number of files, total lines within those files and code, comments, and blanks grouped by language.
So what?
I am going to explain personally where I have used these tools. Others may have different experiences but I suspect there will be a lot of overlap.
Here are some testimonials from SLOCCount
“SLOCCount allows me to easily and quickly quantify the source lines of code and variety in languages. Even though these are just two fairly basic aspects of a project, it helps a lot to get a first impression of the size and complexity of projects.” – Auke Jilderda, Philips Research.
“SLOCCount has really helped us a lot in our studies on libre software engineering” – Jesus M. Gonzalez Barahona, Grupo de Sistemas y Comunicaciones, ESCET, Universidad Rey Juan Carlos.
“Thanks for SLOCCount! It’s great… We’re using SLOCs derived from SLOCCount to compare our software to the software it replaces … Keep up the good work” – Sam Tregar
“Wow, using sloccount on the full POPFile source shows that developing it would have cost around $500K in a regular software company. That seems about right given the length of time we’ve been working on it and the number of people involved. Cool tool.” – John Graham Cumming
From some reddit threads
https://www.reddit.com/r/rust/comments/82k9iy/loc_count_lines_of_code_quickly/
https://www.reddit.com/r/programming/comments/59bjoy/a_fast_cloc_replacement_written_in_rust/
https://www.reddit.com/r/rust/comments/3lnxht/tokei_a_cloccount_lines_of_code_tool_built_in_rust/
I found the following,
Been using loc for quite a while now and it’s pretty great. I love being able to update the team on how far along we are converting all java to kotlin.
I just usually use it to see how fast different parts of our codebases are growing. A few months ago in one of our projects we had 70k lines of kotlin, and now we’re at 90k.
It’s just a fun little tool. And yeah as someone pointed out below it shows you rogue languages in a project.
The above comments apply to all of the code counting tools
tokei
,
cloc
,
sloccount
,
gocloc
,
loc
and
scc
.
However
scc
takes the idea a little further than the other tools by including a complexity estimate. Anyone who has worked with Visual Studio and .NET languages for a few years will have eventually discovered that one of the neat things you can do with it is produce cyclomatic complexity
https://en.wikipedia.org/wiki/Cyclomatic_complexity
reports, down to counts per solution/project/namespace/file/class/method.
I always wanted something like that for all languages. While calculating true cyclomatic complexity requires building a AST for each language and processing edges in it, I took a different approach. It is certainly not as accurate as the proper calculation but considerably faster and in all my tests gives a reasonable estimate that should be in line with a proper cyclomatic complexity calculation on a per file level.
What triggered me to do this however was working on an existing project I inherited. The code was in a bad state. But without a tool like
scc
I was unable to see how bad it really was. As such I underestimated how long it took to manage and it ended up exploding in scope, which is something I don’t care to repeat.
To show how it all works I am going to briefly walk through analyzing a project that I know Owen is far more familiar with than myself, Kombusion
https://github.com/KablamoOSS/kombustion
which is a AWS Cloudformation Tool on steroids. I am going to assume that the reader knows nothing about it beyond the name and what it does at this point.
To start lets just get a basic idea of what is in the current repository and the size. This example would work for any of the tools mentioned.
$ scc
-------------------------------------------------------------------------------
Language                 Files     Lines     Code  Comments   Blanks Complexity
-------------------------------------------------------------------------------
Go                        1782    333844   259667     39278    34899      41001
Markdown                    45      5400     4090         0     1310          0
YAML                        34      2021     1830        73      118         15
Assembly                    25       903      680         0      223         25
JSON                        15    319180   319180         0        0          0
Perl                         8      1141      859       140      142        163
Shell                        7       934      560       293       81         77
Protocol Buffers             6       912      693         1      218          0
TOML                         3       127       39        70       18          0
Plain Text                   3       227      190         0       37          0
Makefile                     3        64       47         0       17          8
HTML                         1        27       27         0        0          0
BASH                         1        21       16         2        3          0
C                            1        47       29         7       11          0
Dockerfile                   1        33        6        17       10          0
-------------------------------------------------------------------------------
Total                     1935    664881   587913     39881    37087      41289
-------------------------------------------------------------------------------
Estimated Cost to Develop $21,846,106
Estimated Schedule Effort 49.528242 months
Estimated People Required 52.248735
-------------------------------------------------------------------------------
What is apparent is that the vast majority of the application is written using Go. Knowing this, and that Go likely has a vendor directory which contains all of the requirements. Given that these are libraries which we probably do not want to know too much about lets run
scc
ignoring that directory. Again any of the code counting tools should be able to do this.
$ scc --pbl vendor -co
-------------------------------------------------------------------------------
Language                 Files     Lines     Code  Comments   Blanks Complexity
-------------------------------------------------------------------------------
Go                        1110     43605    34286      2568     6751       4152
Markdown                    20       864      633         0      231          0
YAML                        16      1717     1573        71       73          6
JSON                        14    319087   319087         0        0          0
ASP.NET                      4         9        9         0        0          0
HTML                         1        27       27         0        0          0
Dockerfile                   1        33        6        17       10          0
TOML                         1        59       24        25       10          0
-------------------------------------------------------------------------------
Total                     1167    365401   355645      2681     7075       4158
-------------------------------------------------------------------------------
What we can now see is that compared to the previous run the number of lines has dropped considerably from
333844
to
43605
. This means there is a huge amount of code that this application depends on. We can also see that most of the languages have dropped off the list.
Perhaps most interesting at the moment is that there is a huge amount of JSON in the application. Lets inspect just the JSON to see what it might be. The below will white-list to just JSON files and ignore all the complexity calculations, but with the
--files
flag we can also see each file individually. Again any of the tools mentioned can do this.
$ scc --pbl vendor -wl json --files -c -co
-------------------------------------------------------------------------------
Language                     Files       Lines      Code    Comments     Blanks
-------------------------------------------------------------------------------
JSON                            14      319087    319087           0          0
-------------------------------------------------------------------------------
~te/source/North Virginia.json           25602     25602           0          0
generate/source/Oregon.json              25602     25602           0          0
generate/source/Ireland.json             25602     25602           0          0
generate/source/Ohio.json                23748     23748           0          0
generate/source/Tokyo.json               23745     23745           0          0
generate/source/Sydney.json              23137     23137           0          0
~enerate/source/Frankfurt.json           22725     22725           0          0
generate/source/Seoul.json               22399     22399           0          0
~enerate/source/Singapore.json           21827     21827           0          0
generate/source/London.json              21607     21607           0          0
generate/source/Mumbai.json              21593     21593           0          0
~/source/North California.json           20672     20672           0          0
generate/source/Canada.json              20414     20414           0          0
~enerate/source/Sao Paulo.json           20414     20414           0          0
-------------------------------------------------------------------------------
Total                           14      319087    319087           0          0
-------------------------------------------------------------------------------
Looks like these are generated and region specific. I am going to make a guess at this point that they are checked in AWS cloud-formation definitions.
$ head -n 10 generate/source/Sydney.json
{
  "PropertyTypes": {
    "AWS::ElasticLoadBalancingV2::ListenerCertificate.Certificate": {
      "Documentation": "<http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-certificates.html>",
      "Properties": {
        "CertificateArn": {
          "Documentation": "<http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticloadbalancingv2-listener-certificates.html#cfn-elasticloadbalancingv2-listener-certificates-certificatearn>",
          "PrimitiveType": "String",
          "Required": false,
          "UpdateType": "Mutable"
Looks like the guess was right. Lets continue to explore, but this time lets ignore JSON and focus on Go which is the meat of the application.
This is where
scc
is most useful as we can sort by complexity to find which files are likey to contain the most logic. The below will white-list to Go files sorted by complexity ignoring the vendor directory.
$ scc --pbl vendor -wl go --files -s complexity
-------------------------------------------------------------------------------
Language                 Files     Lines     Code  Comments   Blanks Complexity
-------------------------------------------------------------------------------
Go                        1110     43605    34286      2568     6751       4152
-------------------------------------------------------------------------------
~ternal/genplugin/genplugin.go       398      335         3       60         83
generate/generate.go                 681      573        22       86         81
~al/cloudformation/template.go       277      216        19       42         54
internal/plugins/load.go             211      157        22       32         51
internal/plugins/install.go          284      231        15       38         50
internal/plugins/add.go              220      163        23       34         36
~loudformation/tasks/upsert.go       128      109         6       13         26
From the above we can deduce that there are three files and one group of files that are reasonably complex and worth a look at if we wanted to work with this code-base. Those being  genplugin.go, generate.go, template.go and the files in internal/plugins. We can also make a guess that there are few unit tests for any of the above as I would expect complex test files to appear next to them. They may still be covered by integration tests though perhaps written in another language.
Lets compare the above to
tokei
.
$ tokei --files -e vendor -s lines
-------------------------------------------------------------------------------
Go                   1110        43626        34292         2576         6758
-------------------------------------------------------------------------------
 ./generate/generate.go             689          574           23           92
 |l/genplugin/genplugin.go          399          336            3           60
 |ernal/plugins/install.go          284          231           15           38
 ./pkg/parsers/output.go            281          275            3            3
 |pkg/parsers/resources.go          281          275            3            3
 |oudformation/template.go          277          216           19           42
 |anifest/manifest_test.go          259          168           81           10
 ./internal/plugins/add.go          220          163           23           34
 |internal/plugins/load.go          211          157           22           32
 ./main.go                          176          101           57           18
Ignoring the differences in counts (all of the tools come up with different numbers) you can see that the tools have a difference of opinion when it comes to which files are potentially the most complex.
Looking at
genplugin.go
identified by
scc
as the most complex where two portions caught my eye.
func
getVal
(
v
interface
{},
depth
int
,
append
string
)
string
{
typ
:=
reflect
.
TypeOf
(
v
).
Kind
()
if
typ
==
reflect
.
Int
{
return
fmt
.
Sprint
(
"\""
,
v
,
"\""
,
append
)
}
else
if
typ
==
reflect
.
Bool
{
return
fmt
.
Sprint
(
"\""
,
v
,
"\""
,
append
)
}
else
if
typ
==
reflect
.
String
{
return
fmt
.
Sprint
(
"\""
,
strings
.
Replace
(
strings
.
Replace
(
v
.(
string
),
"\n"
,
"\\n"
,
-
1
),
"\""
,
"\\\""
,
-
1
),
"\""
,
append
)
}
else
if
typ
==
reflect
.
Slice
{
return
printSlice
(
v
.([]
interface
{}),
depth
+
1
,
append
)
}
else
if
typ
==
reflect
.
Map
{
return
printMap
(
v
.(
map
[
interface
{}]
interface
{}),
depth
+
1
,
append
)
}
return
"UNKNOWN_TYPE_"
+
typ
.
String
()
}
and
if
len(
config
.
Parameters
) >
0
{
writeLine
(
buf
,
"// Parse the config data\n"
+
"var config "
+
resname
+
"Config\n"
+
"if err = yaml.Unmarshal([]byte(data), &config); err != nil {\n"
+
"  return\n"
+
"}\n"
+
"\n"
+
"// validate the config\n"
+
"config.Validate()\n\n// defaults\n"
)
for
paramName
,
param
:=
range
config
.
Parameters
{
if
strings
.
HasPrefix
(
param
.
Type
,
"List<"
)
||
param
.
Type
==
"CommaDelimitedList"
{
writeLine
(
buf
,
"param"
+
paramName
+
" := []interface{}{}\n"
+
"if len(config.Properties."
+
paramName
+
") > 0 {\n"
+
"  param"
+
paramName
+
" = config.Properties."
+
paramName
+
"\n"
+
"}\n\n"
)
}
else
{
defaultVal
:=
""
if
param
.
Default
!=
nil
{
defaultVal
=
fmt
.
Sprintf
(
"%v"
,
param
.
Default
)
// ensure it's a string if int is given
}
writeLine
(
buf
,
"param"
+
paramName
+
" := \""
+
defaultVal
+
"\"\n"
+
"if config.Properties."
+
paramName
+
" != nil {\n"
+
"  param"
+
paramName
+
" = *config.Properties."
+
paramName
+
"\n"
+
"}\n\n"
)
}
}
}
I’d say both of those are portions of code I would want to take great care with were I do modify them. Note I have no idea what they are doing, and as such not commenting on the code quality here I am just exploring a code-base I have never looked at before. Its entirely possible this is the simplest way to solve this problem.
Whats nice is that you can use all of the above to get an idea of complex files in any project. For example, the below is an analysis of the source code for searchcodeserver.com
$ scc --wl java --files -s complexity searchcode-server
-------------------------------------------------------------------------------
Language                 Files     Lines     Code  Comments   Blanks Complexity
-------------------------------------------------------------------------------
Java                       131     19445    13913      1716     3816       1107
-------------------------------------------------------------------------------
~e/app/util/SearchCodeLib.java       616      418        90      108        108
~app/service/IndexService.java      1097      798        91      208         96
~/app/service/CodeMatcher.java       325      234        41       50         66
~service/TimeCodeSearcher.java       582      429        49      104         65
~ce/route/ApiRouteService.java       394      293        12       89         63
~de/app/service/Singleton.java       335      245        20       70         53
~rchcode/app/util/Helpers.java       396      299        38       59         52
~e/route/CodeRouteService.java       453      348         9       96         50
Hope that helps Owen with is understanding and whoever else happens to read this article. If you find
scc
useful please let me know either through email, twitter or just a nice comment on github.
