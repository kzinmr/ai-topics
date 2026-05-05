---
title: "Licensechecker. A command line application which identifies what software license things are under"
url: "https://boyter.org/2018/03/licensechecker-command-line-application-identifies-software-license/"
fetched_at: 2026-05-05T07:01:59.766957+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Licensechecker. A command line application which identifies what software license things are under

Source: https://boyter.org/2018/03/licensechecker-command-line-application-identifies-software-license/

A simple blog post here to introduce a new command line tool licensechecker (lc), which is similar in purpose to the library Licensee
http://ben.balter.com/licensee/
which attempts to identify what software license(s) code is released under. lc itself is dual licensed under the MIT and Unlicense.
Licensechecker (lc) was designed to be run either on your command line or using your CI tool of choice and produce either CSV, JSON, SPDX, Summary or CLI tabular or progress output with the option to write results to disk. It is reasonably fast and is cross platform with binaries for x64 versions of Linux, macOS and Windows. The build process also ensures that it builds on ARM and i386.
You can find both the binaries and code on [GitHub https://github.com/boyter/lc/][1]
Some time ago I wrote a collection of Python scripts which would when tweaked would scan a file directory and tell you what licenses the files that existed within in were under
http://www.boyter.org/2017/05/identify-software-licenses-python-vector-space-search-ngram-keywords/
Licensechecker has taken the ideas I toyed around in Python and produced a much more battle tested command line application written in Go which is ready for general use. I chose to write it in Go simply because at my current role there is a push to use Go and I have a lack of experience with it.
It is reasonably well tested (always room for improvement), and while there are some easy wins that could be done for performance improvements it is reasonably fast.
Some sample outputs of what it can produce follow.
Example output of licencechecker running against itself in tabular format while ignoring the .git, licenses and vendor directories```$ lc -pbl .git,vendor,licenses -f tabular .
Directory            File                    License                            Confidence  Size
.                    .gitignore              (MIT OR Unlicense)                 100.00%     275B
.                    .travis.yml             (MIT OR Unlicense)                 100.00%     188B
.                    CODE_OF_CONDUCT.md      (MIT OR Unlicense)                 100.00%     3.1K
.                    CONTRIBUTING.md         (MIT OR Unlicense)                 100.00%     1.2K
.                    Gopkg.lock              (MIT OR Unlicense)                 100.00%     1.4K
.                    Gopkg.toml              (MIT OR Unlicense)                 100.00%     972B
.                    LICENSE                 Unlicense AND MIT                  94.83%      1.1K
.                    README.md               (MIT OR Unlicense)                 100.00%     7.5K
.                    UNLICENSE               MIT AND Unlicense                  95.16%      1.2K
.                    database_keywords.json  (MIT OR Unlicense)                 100.00%     3.6M
.                    main.go                 (MIT OR Unlicense)                 100.00%     3.4K
.                    what-we-look-at.md      (MIT OR Unlicense)                 100.00%     3.2K
examples/identifier  LICENSE                 GPL-3.0+ AND MIT                   95.40%      1K
examples/identifier  LICENSE2                MIT AND GPL-3.0+                   99.65%      35K
examples/identifier  has_identifier.py       (MIT OR GPL-3.0+) AND GPL-2.0      100.00%     409B
parsers              constants.go            (MIT OR Unlicense)                 100.00%     4.8M
parsers              formatter.go            (MIT OR Unlicense)                 100.00%     7.8K
parsers              formatter_test.go       (MIT OR Unlicense)                 100.00%     944B
parsers              guesser.go              (MIT OR Unlicense)                 100.00%     9.8K
parsers              guesser_test.go         (MIT OR Unlicense)                 100.00%     3.4K
parsers              helpers.go              (MIT OR Unlicense) AND Apache-2.0  100.00%     2.4K
parsers              helpers_test.go         (MIT OR Unlicense)                 100.00%     1.5K
parsers              structs.go              (MIT OR Unlicense)                 100.00%     679B
scripts              build_database.py       (MIT OR Unlicense)                 100.00%     4.6K
scripts              include.go              (MIT OR Unlicense)                 100.00%     951B
To write out the results to a CSV file```$ lc --format csv -output licences.csv --pathblacklist .git,licenses,vendor .```

Or to a valid SPDX 2.1 file```$ lc -f spdx -o spdx_example.spdx --pbl .git,vendor,licenses -dn licensechecker -pn licensechecker .```

You can specify multiple directories as additional arguments and all results will be merged into a single output```$ lc -f tabular ./examples/identifier ./scripts```

You can also specify files and directories as additional arguments```$ lc -f tabular README.md LICENSE ./examples/identifier
Directory              File               License                        Confidence  Size
                       README.md          NOASSERTION                    100.00%     7.5K
                       LICENSE            MIT                            94.83%      1.1K
./examples/identifier  LICENSE            GPL-3.0+ AND MIT               95.40%      1K
./examples/identifier  LICENSE2           MIT AND GPL-3.0+               99.65%      35K
./examples/identifier  has_identifier.py  (MIT OR GPL-3.0+) AND GPL-2.0  100.00%     428B
What follows is a brief overview of how it currently works.
Licencechecker works by comparing files against the list of licenses supplied by SPDX.org with the addition of the Fair Source License which I needed for my own purposes.
First the command line arguments are checked to see if they refer to file or a folder. The difference between the two is that if it is a folder the whole folder is first scanned to see if it can identify any files which indicate a license. This can be controlled using the argument licensefiles which by default is set to look for filenames which contain the string license, copying or readme. For example the following files would be identified as potentially containing a license.```LICENSE
LICENCE
license.md
COPYING.txt
LICENSE-MIT
COPYRIGHT
UNLICENSE
README.md
These are then taken as potential root licenses under which all other files would be marked against.

If there are multiple root licenses then they are treated using OR as through the project is dual licensed. The check for a root license happens in every folder.

When a candidate for a license is found its contents are checked against a list of unique ngrams for licenses. If there any ngrams matching then each license is checked using a vector space to obtain the fuzzy match value for that license. If the value is over the confidence value set which by default is 85% then it is marked as being a match.

If no license is found using the previous step then the file is checked against all licenses using the fuzzy matching. This is because some licenses do not have any unique ngrams allowing identification. Fuzzy matching only looks at the top portion of the file where license headers are expected to exist.

At the end the matches if any are sorted by and the most likely match is returned as the matching license. As such a license file is considered to only contain a single declared license.

Note that only the most recent root licenses are taken into account, so if a project with a root license of MIT has a sub folder with a root license of GPL-2.0+ files in that root folder will be marked as being GPL-2.0+ and not MIT.

For individual files the file is scanned in the same way but in addition is scanned for any SPDX indicators such as,```SPDX-License-Identifier: GPL-3.0-only
Which will take precedence over any fuzzy matching. The indicators must match known SPDX licenses or they will be disregarded.
When finished the license determined is based on the SDPX identifiers if present, fuzzy matching if over the confidence value and then the root license(s). If multiples match they are treated as an AND.
Take for example,```Directory              File               License                        Confidence  Size
./examples/identifier  has_identifier.py  (MIT OR GPL-3.0+) AND GPL-2.0  100.00%     428B
The root licenses were identified as being both MIT and GPL-3.0+ however inside the code itself it has a GPL-2.0 identifier. As such the license of the file is either MIT AND GPL-2.0 OR GPL-3.0+ OR GPL-2.0. The indicator for the license like this is based on SPDX examples and as specified in the SPDX specification <https://spdx.org/spdx-specification-21-web-version>

Currently licencechecker (lc) does not indicate if a project may be in violation of license requirements. Assuming there is some sort of license compatibility chart in the future this would be something to add at a later point.

There are a few known issues with the current version. License's are fuzzy matched so its possible someone could fork an existing license and have it be a false positive match. The second issue is that license matches are based on licenses from SPDX and as such may miss some licenses.

If you have read this far thanks for your time. Id love you to try licencechecker and report back any bugs. I would also love to hear how you are using it and with permission put a link in the README with your testimonial and link. If you want to contribute back use GitHub issues. As with anything I put online I am happy to get constructive feedback.

 [1]: https://github.com/boyter/lc/
