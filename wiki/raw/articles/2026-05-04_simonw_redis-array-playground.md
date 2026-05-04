# Tool: Redis Array Playground
**Author:** Simon Willison
**Date:** May 4, 2026
**Source:** https://simonwillison.net/2026/May/4/redis-array/

Salvatore Sanfilippo submitted a PR adding a new data type - arrays - to Redis. The new commands are ARCOUNT, ARDEL, ARDELRANGE, ARGET, ARGETRANGE, ARGREP, ARINFO, ARINSERT, ARLASTITEMS, ARLEN, ARMGET, ARMSET, ARNEXT, AROP, ARRING, ARSCAN, ARSEEK, ARSET.

Simon used Claude Code for web to build an interactive playground for trying out the new commands in a WASM-compiled build of Redis running in the browser. The most interesting new command is ARGREP which can run a server-side grep against a range of values using the newly vendored TRE regex library.

Salvatore wrote more about the AI-assisted development process in "Redis array type: short story of a long development" at antirez.com/news/164.

Related: https://github.com/redis/redis/pull/15162 (PR), https://tools.simonwillison.net/redis-array (playground)
