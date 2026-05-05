---
title: "Installing voice2json on Ubuntu"
url: "https://boyter.org/posts/installing-voice2json-ubuntu/"
fetched_at: 2026-05-05T07:01:56.983687+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Installing voice2json on Ubuntu

Source: https://boyter.org/posts/installing-voice2json-ubuntu/

I have been playing around with offline non cloud tool replacements for doing things like speech to text and the like. One that I found which looked promising was voice2json which is a command line tool for turning speech intent into text. It can do generic conversion too, but a review of that is not the subject of this post.
Following the instructions from the website
http://voice2json.org/install.html
worked fine up till I tried to run it and got the following issue.
ImportError: libffi.so.6: cannot open shared object file: No such file or directory
I am working on a modern version of ubuntu, and after some searching around and following links the fix turned out to be to download the following package
http://mirrors.kernel.org/ubuntu/pool/main/libf/libffi/libffi6_3.2.1-8_amd64.deb
and then install it
sudo apt install ./libffi6_3.2.1-8_amd64.deb
Problem solved, and I was able to run it.
voice2json transcribe-wav --open < test.wav
With the output working as expected. I did notice it seems to take as long to run as the audio itself is, but thats not a huge issue for my case. Next on my list is to investigate the newish
https://github.com/petewarden/spchcat
