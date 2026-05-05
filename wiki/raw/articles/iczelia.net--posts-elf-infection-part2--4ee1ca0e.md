---
title: "A technique for ELF file infection - part 2."
url: "https://iczelia.net/posts/elf-infection-part2/"
fetched_at: 2026-05-05T07:01:21.675734+00:00
source: "Kamila Szewczyk (iczelia)"
tags: [blog, raw]
---

# A technique for ELF file infection - part 2.

Source: https://iczelia.net/posts/elf-infection-part2/

Introduction
⌗
In the previous blog post, I demonstrated a method of infecting ELF files. In this post, I would like to present a slightly improved version with additional features. The previous version of the infection code could only infect a single file, while the new version will be able to find potential host files and infect them automatically.
A good source of potential victim files is the
$PATH
environment variable, which contains a list of directories that may contain executable files. The program will search these directories for ELF files and infect them. The program will also check if the file is already infected to prevent infecting the same file multiple times. In addition, the program will ensure that it only attempts to infect ELF files that it has access to.
To begin, I will embed a marker in the stub to make it easily recognizable and add safety guards in case
execve
fails. I will pass the
argp
argument in
rdi
to the
payload
function so that it can use the
$PATH
to find potential victim files.
For the purposes of the new payload, I will need a random number generator (to determine whether to infect a file or not), a constant variable with the path separator (to append it between the directory name and the file name), and two auxiliary LCG random number generator variables.
Stalking for prey
⌗
The payload will be handling large amounts of stack data, so it must reserve sufficient space to ensure that
argc
,
argv
, or
argp
are not overwritten during the process. This is also an opportune time to initialize the random number generator.
The next part is more involved, as the code must locate the
$PATH
variable in the environment key/value pair table. A simple solution is to iterate until the current envp entry is
NULL
and check the prefix of the current entry. If it is
PATH=
, discard the first 5 bytes (to skip the key name in the string) and save it to a register. This part is relatively straightforward, but it is essential to guard against environment key/value pairs that are shorter than 5 bytes in total to prevent a potential buffer overflow.
Determine a buffer that will hold the final path to the file that will be infected. As I wrote this program and golfed it in advance, I will also load two constants that might appear to be arbitrary (a syscall number and a divider for the probability of infecting a directory).
At this point, the program can now loop through the entries in the
PATH
variable and examine each of them. The loop will continue until it encounters a
NULL
value (indicating that the
PATH
string has been exhausted), and then copies the current path (that is, the string from the current position in the
PATH
variable until the first occurrence of a colon or a NUL terminator, whichever comes first).
There are a few more things to be done with the path. Firstly, it must be null-terminated. Secondly, if the final character in the
PATH
string is a colon, it must be skipped.
After obtaining a valid directory path, the program should now open it. It is crucial to verify the return code, as PATH entries do not have to be valid (they may not point to an existing directory). If the directory is invalid, it must be skipped.
The program will use the fairly low-level system call
getdents
to obtain directory entries in batches. Before proceeding, some entries should be randomly pruned to reduce the number of filesystem operations performed (which helps to remain undetected).
With the file name, it is possible to construct the final buffer with the absolute path to be infected, taking care to address some quirks in the process.
At this point, the program should check if the file is actually accessible for writing and devise a plan for what to do when it is not. The approach here is to try to temporarily alter the permissions of the file in the hope that it grants the necessary write access. If it does not, the file must be skipped. If it does, the program will restore the original permissions later.
If no difficulties were encountered, the file can be infected now with no extra alterations.
Finally, a few fallback labels from the code defined above need to be implemented.
The payload employs a
concat
procedure to join two nul-terminated strings. The implementation is relatively straightforward and is as follows:
An improved infection function
⌗
The improved infection function will have several qualities that make it superior to the previous version. Most notably, the new infection function includes improved ELF file detection and better protection against re-infection. The process begins by opening the target file and reading and verifying the ELF header.
The function will check for the sentinel to determine if the file has already been infected. If the sentinel is present, the infection process should be terminated.
The infection process is not much different from the previous iteration: the code will open the current executable, create a memory-backed file descriptor, and write the infectious stub to it followed by the target file.
After constructing a valid parasitic ELF file, the final step is to rewind both files to the first byte and copy the contents of the memory-backed file descriptor to the target file. An improvement that could be made here is to check whether there is sufficient disk space to append the stub, but this scenario is extremely unlikely to pose an issue, so it is not worth the effort. It could, however, be implemented using
ftruncate
followed by appropriate error checking.
Conclusion
⌗
The new, improved ELF file infector is undoubtedly better than the original, however it still lacks a genuine payload, stealthiness, or code compression. I will discuss these topics in the next essay in the series, please stay tuned!
The following terminal session demonstrates the program’s capabilities. I have artificially created an environment with a single-directory
$PATH
variable that contains two common UNIX programs. I have linked the
date
program to the infector to reduce the amount of text output compared to the previous example using
unzip
.
