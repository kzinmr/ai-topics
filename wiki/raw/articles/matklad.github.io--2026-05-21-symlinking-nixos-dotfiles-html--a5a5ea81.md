---
title: "TIL: Symlinking NixOS Dotfiles"
url: "https://matklad.github.io/2026/05/21/symlinking-nixos-dotfiles.html"
fetched_at: 2026-05-22T07:01:12.266573+00:00
source: "matklad.github.io"
tags: [blog, raw]
---

# TIL: Symlinking NixOS Dotfiles

Source: https://matklad.github.io/2026/05/21/symlinking-nixos-dotfiles.html

TIL: Symlinking NixOS Dotfiles
May 21, 2026
The standard answer to managing dotfiles on NixOS is
home-manager
. I’ve never used it, due to two aesthetic and one
          practical objection:
I avoid dependencies, especially in nix, which rivals Python in the
            number of approaches to dependency management.
home-manager installs packages for the current user only, which
            makes sense on non-NixOS systems. But on a single-user desktop
            system, I prefer having just one set of packages.
Having a source of truth for dotfiles be in nix store requires
            rebuilding your system to change config, which gets in the way of
            Emacs-style direct tinkering.
The approach I like is storing dotfiles in the same repository as
flake.nix
/
configuration.nix
and symlinking them in place.
The problem here is that NixOS seemingly doesn’t have a “native” way
          to say that
/a/b/c
should be a symlink to
/c/d/e
. Or has it?
If you
search options
for
symlink
, you’ll learn about
environment.etc
which allows you to configure
          symlinks, but only for things in
/etc
, not your
~/.config
.
For the latter, you can use
gnu stow
or some other dotfile link manager, but the complexity
          of the problem of
just
managing symlinks doesn’t warrant yet
          another dependency. It’s fine to do
this manually
.
But wouldn’t it be nice if this framework for declarative
          configuration of your system allowed you to declaratively configure
          symlinks? Turns out this is possible, in roundabout way. Inaptly-named
systemd-tmpfiles
allows creating symlinks from a declarative
          config, and you can use NixOS to
configure
systemd-tmpfiles
itself (thanks,
Noobz
!).
For example, if I want to symlink
~/dotfiles/git/config
to
.config/git/config
:
{
systemd.tmpfiles.
rules
= [
"L+ /home/matklad/.config/git/config - - - - /home/matklad/dotfiles/git/config"
];
}
No opinion at this point how this compares to a bespoke script or
something more purpose-built
.
