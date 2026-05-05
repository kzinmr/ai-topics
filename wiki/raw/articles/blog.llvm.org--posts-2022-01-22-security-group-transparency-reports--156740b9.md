---
title: "LLVM security group and 2021 security transparency report"
url: "https://blog.llvm.org/posts/2022-01-22-security-group-transparency-reports/"
fetched_at: 2026-05-05T07:01:37.184763+00:00
source: "LLVM Blog"
tags: [blog, raw]
---

# LLVM security group and 2021 security transparency report

Source: https://blog.llvm.org/posts/2022-01-22-security-group-transparency-reports/

LLVM security group and 2021 security transparency report
By Kristof Beyls
Jan 22, 2022
#security
2 minute read
Over the past few years, the LLVM project has seen the creation of a security
group, which aims to enable responsible disclosure and fixing of
security-related issues affecting the LLVM project.
The
LLVM security group
was established
on the 10th of July 2020 by the act of the
initial
commit
describing
the purpose of the group and the processes it follows. Many of the group’s
processes were still not well-defined enough for the group to operate well.
Over the course of 2021, the key processes were defined well enough to enable
the group to operate reasonably well:
Over the course of 2021, we had 2 people leave the LLVM Security group and 4
people join.
In 2021, the security group received 13 issue reports that were made publicly
visible before 31st of December 2021. The security group judged 2 of these
reports to be security issues:
Both issues were addressed with source changes: #5 in clangd/vscode-clangd, and
#11 in llvm-project. No dedicated LLVM release was made for either.
We believe that with the publishing of the first annual transparency report,
the security group now has implemented all necessary processes for the group to
operate as promised. The group’s processes can be improved further, and we do
expect further improvements to get implemented in 2022. Many of the potential
improvements end up being discussed on the
monthly public call on LLVM’s
security group
.
