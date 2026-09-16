---
title: "Tag index for Org mode blog"
url: "https://entropicthoughts.com/tag-index-for-org-mode-blog"
fetched_at: 2026-09-16T10:01:34.658493+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Tag index for Org mode blog

Source: https://entropicthoughts.com/tag-index-for-org-mode-blog

Since people keep asking how this blog is made, and I don’t want to share the
awful, terrible code
that it is taped together with, I’ve decided to start
explaining parts of it piecewise. Generally, any time something breaks and I
have to fix it, I write down what I did and what it connects to.
The most recent issue was the stack limit being blown by a helper function
involved in generating the tag index. I had written it to be explicitly
recursive, which worked fine with a small-ish number of published articles, but
not anymore. The tag index creation follows a similar pattern to the
rss
feed
generation detailed in the previous article.
In[1]:
(
defun
tw-tag-index
(project)
"Generate a tag index page for PROJECT."
(
let*
((filename (concat (project-dir
"src"
"org"
)
"tags.org"
))
;;
Get all publically listed files in this project.
(files (seq-filter (
lambda
(entry) (plist-get entry
:indexed
))
                            (tw-get-all-files project)))
;;
Convert to sorted alist of tag×article pairs.
(all-tags (sort (tw-get-all-file-tags files)
                         (
lambda
(a b) (string< (car a) (car b))))))
    (
with-temp-file
filename
      (insert (concat
"#+TITLE: Tags\n"
;;
Don't show author and publish date.
"#+AUTHOR: \n"
;;
Don't list in public indices.
"#+FILETAGS: :page:\n\n"
;;
Include table of contents.
"#+TOC: headlines:1\n\n"
;;
Then produce headings for each tag.
(org-element-interpret-data
                   (tw-article-entry-headlines all-tags)))))
;;
Return the filename of the created file. I don't
;;
remember why. Maybe it's not necessary.
filename))
First we filter out the articles that should be indexed from a list of all files
in the project. We pass this through the
tw-get-all-file-tags
function, which
produces an
association list
, which is like a dictionary in Emacs
Lisp. Each entry in the association list is a tag paired with a list of articles
that have that tag. That list is sorted alphabetically on the tag name, and then
it gets converted into an Org document that can be exported.
Note the ugly appearing again! We are converting a data structure to an
org-element tree, but then we convert that org-element tree into a string and
insert it into a string also representing an Org document. The right thing to do
would probably have been to construct the entire document as an org-element
tree, and then maybe export this tree without creating a temporary file in
between? But I have hacked this together with limited knowledge and now I’m
unwilling to spend time on it.
The magic that broke in this case was inside
tw-get-all-file-tags
which is
short:
In[2]:
(
defun
tw-get-all-file-tags
(files)
"Get an alist of all tags for FILES, as symbols."
(tw-invert-alist
   (mapcar (
lambda
(file) (cons file (plist-get file
:tags
))) files)))
This creates an association list of file × tags pairs by mapping
cons
over the
files. Then
tw-invert-alist
takes that association list and flips it, to
become an association list of tag × files instead. This last function is what
used to be explicitly recursive and blew the stack, but now it’s fixed.
In[3]:
(
defun
tw-invert-alist
(alist)
"Invert ALIST, turning key-values into value-keys."
(
let
((inverted nil))
;;
For each pair of key×values in alist …
(
dolist
(key-values alist inverted)
      (
let
((key (car key-values)))
;;
… loop through all values …
(
dolist
(value (cdr key-values))
;;
… and store the key under the value
;;
in the inverted list. If the value exists,
;;
store the key in its list, otherwise
;;
add the value and store a singleton list.
(
if
(alist-get value inverted)
              (
push
key (alist-get value inverted))
            (
push
(cons value (list key)) inverted)))))))
In this version it builds the inverted association list iteratively instead.
