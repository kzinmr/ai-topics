---
title: "Find blog posts with missing featured images - and missing alt text - without a plugin"
url: "https://shkspr.mobi/blog/2026/05/find-blog-posts-with-missing-featured-images-and-missing-alt-text-without-a-plugin/"
fetched_at: 2026-05-12T07:00:49.184803+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# Find blog posts with missing featured images - and missing alt text - without a plugin

Source: https://shkspr.mobi/blog/2026/05/find-blog-posts-with-missing-featured-images-and-missing-alt-text-without-a-plugin/

WordPress has the concept of "Featured Images". They are the images which show up when you share a blog post on social media or, on some themes, as the "hero" image.
How can you quickly and easily find any posts which
don't
have a featured image?
For this, I use
WP CLI
- it allows you to run complex WordPress actions and queries using the command line.  After you have
installed WP CLI
you can get started.
On the command line, run:
⧉
wp eval 'foreach(get_posts(array("post_type"=>"post","post_status"=>array("publish"),"posts_per_page"=>-1,)) as $post){if(get_the_post_thumbnail($post)==""){$post_type_object=get_post_type_object($post->post_type);$link=admin_url(sprintf($post_type_object->_edit_link . "&action=edit", $post->ID));echo $post->post_date . " " . $link . " " . $post->post_title . "\n";}}'
Here's the code in a slightly more readable format:
⧉
PHP
foreach
(
get_posts
(
array
(
"post_type"
=>
"post"
,
"post_status"
=>
array
(
"publish"
),
"posts_per_page"
=> -1,
       ) 
   )
as
$post
) {
if
(
get_the_post_thumbnail
(
$post
)==
""
) {
$post_type_object
=
get_post_type_object
(
$post
->
post_type
);
$link
=
admin_url
(
sprintf
(
$post_type_object
->
_edit_link
.
"&action=edit"
,
$post
->
ID
) ) ;
echo
$post
->
post_date
.
" "
.
$link
.
" "
.
$post
->
post_title
.
"\n"
;
      } 
}
That will print out:
⧉
2024-05-02 12:34:11 https://example.com/wp-admin/post.php?post=123&action=edit "A post about sausages" 
2023-09-13 20:55:52 https://example.com/wp-admin/post.php?post=456&action=edit "I like cheese"
2021-12-31 15:43:33 https://example.com/wp-admin/post.php?post=789&action=edit "Touching computers"
You can then go and edit each of those posts to add a featured image.
Adding alt text means that people who can't see images will still be able to understand what the picture represents. Here's another one-lines to find all featured images with missing alt text:
⧉
wp eval 'foreach (get_posts(array("post_type"=>"post","post_status"=>array("publish"),"posts_per_page" => -1,)) as $post){if(simplexml_load_string(get_the_post_thumbnail($post))["alt"]==""){$post_type_object=get_post_type_object($post->post_type);$link=admin_url(sprintf($post_type_object->_edit_link . "&action=edit",$post->ID));echo $post->post_date . " " . $link . " " . $post->post_title . "\n";}}'
And, in slightly more readable form:
⧉
PHP
foreach
(
get_posts
(
array
(
"post_type"
=>
"post"
,
"post_status"
=>
array
(
"publish"
),
"posts_per_page"
=> -1,
           ) 
   )
as
$post
) {
if
(
simplexml_load_string
(
get_the_post_thumbnail
(
$post
) )[
"alt"
] ==
""
) {
$post_type_object
=
get_post_type_object
(
$post
->
post_type
);
$link
=
admin_url
(
sprintf
(
$post_type_object
->
_edit_link
.
"&action=edit"
,
$post
->
ID
) ) ;
echo
$post
->
post_date
.
" "
.
$link
.
" "
.
$post
->
post_title
.
"\n"
; 
      } 
}
Again, that lists the datetime of the post, its edit link, and its title.
Now, if you'll excuse me, I have about 873 posts which need updating 🤯
