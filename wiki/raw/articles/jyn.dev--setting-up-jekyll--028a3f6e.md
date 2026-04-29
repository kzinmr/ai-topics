---
title: "Setting up Jekyll for GitHub Pages"
url: "https://jyn.dev/setting-up-jekyll/"
fetched_at: 2026-04-29T07:02:13.250544+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# Setting up Jekyll for GitHub Pages

Source: https://jyn.dev/setting-up-jekyll/

Jekyll is a wonderful program. The more I use it, the more I like it.
It's customizable, automatically parses markdown, and uses a template system
that makes it very easy to create a consistent style. Its only flaw is that
it depends on
rubygems
.
Jekyll does get a little getting used to, however.
In this article, I'll go over the basics:
Installing
Creating a site
Customizing a site
Creating content
Note that I assume some basic familiarity with
Git
and the commandline, which will be covered in another post.
Installing
If you don't have
rubygems
installed, you'll need it. See also
footnote 1
.
gem
install jekyll
Creating a site
jekyll
new
<
directory
>
cd
$
_
jekyll
serve
Congratulations! Your site is now live
(at
http://localhost:4000
by default).
Customizing your site
"Your awesome title" is a pretty terribly name for a site.
Go ahead and edit it in
_config.yml
.
There's lots of other juicy config to change in there,
quick rundown
here
.
Other things to edit
Jekyll uses
minima
by default; find where it is with
bundle show minima
.
cp
-
r
$
(
bundle
show minima
)
/
*
<
directory
>
CSS:
_sass/minima/
Page layouts:
_layouts/
Headers and footers:
_includes/
404 page:
404.html
Creating content
Jekyll expects a certain format from its templates. I've made an
script
that will handle the metadata automatically.
The content itself can be in one of three formats:
The
source
of my site is also available as an example.
Appendix
If, like me, you got a permissions error -
jyn@debian-thinkpad:/usr/local/src/second-website$
gem install jekyll
ERROR:
While executing gem ... (Errno::EACCES
)
Permission
denied @ dir_s_mkdir - /var/lib/ruby/2.3.0/gem/specs
then you probably installed with a package manager. Unfortunately,
you'll have to reinstall gem; I'm not aware of any way around this.
Since installing on a system-wide basis requires root permissions,
/var/lib/ruby is only read/writable for root.
If you want to edit where gems are stored, you'll have to edit
the rubygem script itself. Find the ruby library (in my case,
/usr/lib/ruby
) and ```sh
cd 2.3.0/rubygems
sed -i "s/File.join Gem.user_home, '.gem'/File.join Gem.user_home, '.local', 'lib', 'gem'/" **
