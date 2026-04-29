---
title: "Jupyter notebooks as e2e tests"
url: "https://rakhim.exotext.com/jupyter-notebooks-as-e2e-tests"
fetched_at: 2026-04-29T07:01:21.391882+00:00
source: "rakhim.exotext.com"
tags: [blog, raw]
---

# Jupyter notebooks as e2e tests

Source: https://rakhim.exotext.com/jupyter-notebooks-as-e2e-tests

Lots of scientific Python libraries are often used within Jupyter notebooks. At work, we develop and maintain plenty of such libraries for quantum computing, and some more higher-level ones include extensive user guides in form of Jupyter notebooks.
Recently, I've been involved in building a new library, and it ended up containing a half dozen notebooks, covering everything from a quick start guide to niche applications and configuration examples. It being a completely new product, we wanted our users to have extensive interactive documentation from the start.
After the alpha stage was behind us, we needed to write e2e tests. I realized that user guide notebooks are essentially that! They already cover every major e2e use case, and we update them religiously. We also render them into HTML docs on release. Sure, they don't cover 100% of cases, and aren't generally parametrized. But if everything in them works, we have a very good indication that the overall release is healthy. (The library is used by another component of the system, and there are separate e2e tests for that component; and there are unit tests everywhere, too.)
To make Jupyter notebooks runnable as e2e tests (both locally and in CI pipelines) we needed to do 2 things:
Make them parametrized so that both users following the guide and pipelines can run them.
Run them automatically.
Point 1 is relevant because the library performs some actions on a remote server (a real quantum computer). So, we made the first cell in each user guide start with reading the URL of the server from the environment (
os.environ['SERVER_URL']
). The user can replace it with a literal string, or set the environment variable in their system. In CI, the environment variable is set by the Gitlab pipeline, and we can even dynamically rotate addresses.
Point 2 can be achieved in two ways. The easiest is to just install
nbclient
and run
jupyter execute <NOTEBOOK.ipynb>
. It can accept multiple files, and it produces no output. If notebooks were executed without errors, the process terminates without errors as well, and can be treated as a successful run by the CI. If there are errors, you'll see the output, which is good for debugging.
If you need to view the output of each executed cell, you can use a combination of
nbconvert
and
jq
(
homepage
).
nbconvert
to execute the notebook and convert the outputs into another notebook, then redirect them to stdout; and
jq
to extract particular parts of the output JSON.
jupyter nbconvert --to notebook --execute  <NOTEBOOK.ipynb> --stdout | jq -r '.cells[] | select(.outputs) | .outputs[] | select(.output_type == "stream") | .text[]'
This is a bit fragile as it relies on a particular structure of the output JSON, and it may change in future Jupyter versions. The example above is suitable for
notebook
version
6.4
and above. However, a failure of execution will not propogate up, the resulting notebook would just contain cells with error output, and
jq
would parse them successfully, rendering the whole run unsuited for continous integration. You'd need to have some separate script to detect the presence/absence of "error" cells, and return the corresponding return code so that CI understands it.
For our purposes, the first way works ok. We only care about potential errors. Overall, by having this setup, we test both the integrity of documentation and of code on each merge request.
Footnotes
Netflix uses notebooks for a variety of interesting purposes, including testing. See
Beyond Interactive: Notebook Innovation at Netflix
.
