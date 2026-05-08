---
title: "Article previews in RSS"
url: "https://entropicthoughts.com/article-previews-in-rss"
fetched_at: 2026-05-08T07:01:36.748602+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Article previews in RSS

Source: https://entropicthoughts.com/article-previews-in-rss

Since about
three years past time immemorial
, the
rss
feed for this site has
been very anaemic. It had article titles and dates, and that was it. Many
readers have requested that I include the full article in the feed, or at least
a preview, but I’ve always put it off because it has sounded difficult to
accomplish technically.
The way the
rss
feed for this site is generated is in two steps:
First a little loop in Emacs Lisp runs through the first few items of a
sorted and filtered list of files belonging to this project. This loop
constructs an org-element syntax tree for the
rss
feed, and renders it out
to a temporary file as an Org mode file.
Then the regular Org exporting framework takes over and exports that file as
an
rss
file using the ox-rss backend.
Article contents are not involved anywhere in this process! The feed is built
entirely from file metadata. Any time I’ve pondered adding contents, I’ve balked
at the complexity of the problem:
Should the feed contents contain sidenotes?
Should it evaluate code blocks, e.g. to produce figures?
How do I differentiate internal links from images, such that each work
appropriately?
Will some part of the article structure be difficult to mirror in the rather
limited
rss
format?
It’s not that I couldn’t solve all these problems, but I don’t want to take the
time for it, because it would be a lot of time.
Yesterday I decided to simplify the problem: no internal links, no images, no code
evaluation, etc. Just the first four basic elements of the article, like
paragraphs, tables, and lists. Getting those from an article at a file path
is possible with something like this.
In[1]:
(
defun
tw-get-teaser-contents
(source-path)
"Get org-element data of early parts of SOURCE-PATH."
(
with-temp-buffer
;;
Load file contents into Org mode.
(insert-file-contents source-path)
    (org-mode)
;;
Take the first four elements ...
(seq-take
;;
... from a subset of the full parse sequence.
(org-element-map (org-element-parse-buffer)
         '(paragraph src-block quote-block plain-list)
       #'identity
       nil nil '(quote-block plain-list))
     4)))
Then we have to strip some difficulties (internal links), performance problems
(code block evaluation), and non-essentials (sidenotes) from this. There are
good ways to do it, but I discovered a roundabout way to do it instead. First I
created an export backend for a limited subset of
html
.
1
The code I’m
actually running for this is a smidge more complicated to be able to handle my
excessive use of small caps, etc. But the principle is there..
In[2]:
;;
Custom backend for lo-fi RSS-embedded HTML.
(org-export-define-derived-backend 'teaser-html 'html
:translate-alist
'((link . (
lambda
(_ contents _) (
or
contents
""
))
    (footnote-reference . (
lambda
(_ _ _)
""
)))))
This can be used to produce an
rss
friendly rendering of the teaser contents.
In[3]:
(
defun
tw-get-teaser-html
(path)
"Get HTML representing teaser for Org file at PATH."
;;
Don't syntax highlight code in RSS.
(
let
((org-html-htmlize-output-type nil))
;;
Practically unbind function to prevent code block
;;
evaluation without disrupting other babel processing.
;;
;;
This uses cl-letf rather than advice in order to
;;
revert the change when control leaves this function.
(
cl-letf
(((symbol-function 'org-babel-execute-src-block)
               (
lambda
(
&rest
_)
""
)))
      (org-export-string-as
;;
Render data back as Org source markup.
(mapconcat #'org-element-interpret-data
                  (tw-get-teaser-contents path)
"\n\n"
)
;;
Then export that as limited HTML.
'teaser-html t '(
:with-footnotes
nil)))))
Now we have lo-fi
html
, but the source for the
rss
file is an org-element
syntax tree, so we have to embed the article preview as an
html
export block
in the syntax tree.
In[4]:
(
defun
tw-feed-summary
(path)
  (org-element-create 'export-block
    (list
:type
"HTML"
:value
(tw-get-teaser-html path))))
This produces an org-element node that can then be inserted into the Org
document that makes up the
rss
feed.
There is still one problem remaining after this. The ox-rss export backend
installs an output filter that prettifies the
xml
of the
rss
file by, among
other things, running
indent-region
on the entire buffer.
2
A clever trick
for figuring out where a function is called is to run
(debug-on-entry
'indent-region)
and then look at the stack trace. Press
c
to continue in the
debugger. Then
cancel-debug-on-entry
for the same function stops it from
entering the debugger all the time.
This does not respect indentation in the
cdata
blocks – including code blocks where indentation really matters! This
does not appear configurable, but we can override the function that does this to
do nothing instead.
In[5]:
(advice-add 'org-rss-final-function
:override
(
lambda
(contents _ _) contents))
There! That’s it, I think. It was far from trivial (it took a few hours to get
right, after all), but also easier than I would have thought.
But also, this is terrible, terrible code. I’m sure there is a neat way to do
it, but what I’ve done is not it. Think about it: this code parses an Org
document, keeps some parts of it, renders it back to Org, exports that to
html
, embeds that in another Org file, then exports that
once again
to a
html
-derived format. Back and forth, back and forth.
When people ask me to share the code I have written to patch up Org to make this
site the way I want, I tell them they would be better off reading the Emacs
manual and the code for Org, because of shit like this. I don’t know this stuff
very well, so I just wing it. It doesn’t turn out nice. I don’t want anyone
to think they are learning anything from it!
