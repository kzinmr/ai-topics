---
title: "Clang ♥ bash -- better auto completion is coming to bash"
url: "https://blog.llvm.org/2017/09/clang-bash-better-auto-completion-is.html"
fetched_at: 2026-05-05T07:01:38.263005+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# Clang ♥ bash -- better auto completion is coming to bash

Source: https://blog.llvm.org/2017/09/clang-bash-better-auto-completion-is.html

Clang ♥ bash -- better auto completion is coming to bash
By Yuka Takahashi
Sep 19, 2017
#GSoC
,
#Clang
3 minute read
Compilers are complex pieces of software and have a multitude of command-line options to fine tune parameters. Clang is no exception: it has 447 command-line options. It’s nearly impossible to memorize all these options and their correct spellings, that's where shell completion can be very handy. When you type in the first few characters of a flag and hit tab, it will autocomplete the rest for you.
Background
However, such a autocompletion feature is not available yet, as there's no easy way to get a complete list of the options Clang supports. For example, bash doesn’t have any autocompletion support for Clang, and despite some shells like zsh having a script for command-line autocompletion, they use hard coded lists of command-line options, and are not automatically updated when a new option is added to Clang. These shells also can’t autocomplete arguments which some flags take (-std=[tab] for instance).
This is the problem we were working to solve during this year’s Google Summer of Code. We’re adding a feature to Clang so that we can implement a complete, exact command-line option completion which is highly portable for any shell. To start with, we'll provide a completion script for bash which uses this feature.
Implementation
Clang now has a new command line option called
--autocomplete
. This flag receives the incomplete user input from the shell and then queries the internal data structures of the current Clang binary, and returns a list of possible completions. With this API, we can always get an accurate list of options and values any time, on any newer versions of Clang.
We built an autocompletion using this in bash for the first implementation. You can find its source code
here
. Also,
here
is the sample for Qt text entry autocompletion to give an example how to use this API from an UI application as seen below:
You can always complete one flag at a time. So if you want to use the API, you have to select the flag that the user is currently typing. Then just pass this flag to the --autocomplete flag in the selected clang binary. So in the case below all flags start with `-tr` are displayed with their descriptions behind them (separated from the flag with a tab character).
The API also supports completing the values of flags. If you have a flag for which value completion is supported, you can also provide an incomplete value behind the flag separated by a comma to get completion for this:
If you provide nothing after the comma, the list of the all possible values for this flag is displayed.
How to get it
This feature is available for use now with LLVM/clang 5.0 and we’ll also be adding this feature to the standard bash completion package. Make sure you have the latest clang version on your machine, and source
this script
. If want to make the change permanent, just source it from your
.bashrc
and enjoy typing your clang invocations!
