---
title: "Script dependencies with Nix"
url: "https://entropicthoughts.com/python-dependencies-with-nix"
fetched_at: 2026-10-23T10:01:33.630023+00:00
source: "entropicthoughts.com"
tags: [blog, raw]
---

# Script dependencies with Nix

Source: https://entropicthoughts.com/python-dependencies-with-nix

I imagine that of those reading this article, a small crowd starts murmuring
about
uv
. From what I understand,
uv
does take a lot of the headache out of
managing Python dependencies.
4
I don’t know, honestly. It came around after I
stopped working professionally with Python, so learning and understanding it
would happen in my limited spare time, and now that I have Nix, I think I have
better things to learn and understand.
But it is only for Python.
Nix works
for any dependency, with any language.
If we have an R script we want to manage
the dependencies for, we’d do the exact same thing and use
writeRscriptBin
instead.
The way to find the right helper function is by knowing that they are called
writers
, and then
searching Noogle for them
. By excluding the language from
that search, we can see there are writers for other languages too, like C,
JavaScript, Shell, Haskell, Perl, and more.
But there’s no writer helper function specifically for Emacs Lisp. What if we
have an Emacs Lisp script we want Nix to manage the dependencies of? Then we
can still use the lower level
makeScriptWriter
function. Here’s a generic
example of that:
In[3]:
default
= pkgs.writers.makeScriptWriter
  {
# System dependencies work the same as before.
makeWrapperArgs
= [
"--prefix"
"PATH"
":"
(pkgs.lib.makeBinPath [
        pkgs.some-package-with-executable
      ])
    ];
# Make sure the interpreter is produced with the
# necessary run-time dependencies. Most packaged
# scripting languages support the "withPackages"
# convention for this.
interpreter
=
"
${
(pkgs.interpreter.withPackages (ps: [
      ps.dependency-1
      ps.dependency-2
    ]))
}
/bin/interpreter-binary"
;
  }
"/bin/our-executable-name"
(builtins.readFile
./source-file-path
);
For Emacs Lisp, the interpreter package we’d use would be Emacs. The output path
(
/bin/our-executable-name
) is package relative, so we don’t have to worry
about it clobbering the file system.
Of course, we also have compiled languages, like Ada. Ada also doesn’t have a
ready-made writer function, so we’d use the generic
makeBinWriter
helper,
which takes a
compileScript
argument where we specify how to compile.
In[4]:
default
= pkgs.writers.makeBinWriter
  {
# System dependencies work the same again.
makeWrapperArgs
= [
"--prefix"
"PATH"
":"
(pkgs.lib.makeBinPath [
        pkgs.some-package-with-executable
      ])
    ];
# The compilation script can reference any compiler and
# any libraries in nixpkgs, and they will be managed by
# Nix during the build. Any runtime dependencies will be
# managed by Nix automatically too.
#
# The file we read with readFile is called $contentPath
# in this script, and the output must be written to the
# path in the $out variable.
compileScript
=
''
${
pkgs.some-compiler
}
/bin/compiler-binary \
-o $out $contentPath
''
;
  }
"/bin/our-binary-name"
(builtins.readFile
./source-file-path
);
Although this looks like deep, black magic, it’s not. What’s so neat about Nix
is that it uses regular Unix paths, regular Unix environment variables, and
content hashing to figure out what depends on what and whether an input has
changed, necessitating rebuilding.
