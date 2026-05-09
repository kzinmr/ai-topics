---
title: "jyn514/babashka-flower-talk: A talk I gave at Babashka Conf 2026 in Amsterdam, about Flower."
url: "https://jyn.dev/talks/flower/"
fetched_at: 2026-05-09T07:01:09.651926+00:00
source: "jyn.dev"
tags: [blog, raw]
---

# jyn514/babashka-flower-talk: A talk I gave at Babashka Conf 2026 in Amsterdam, about Flower.

Source: https://jyn.dev/talks/flower/

Flower: an SSG with a Clojure template language
Written for
Babashka-conf 2026
.
Excalifont
is MIT licensed by
https://excalidraw.com
.
Run once
Install
typst
.
Install
pympress
Run
typst compile main.typ --font-path etc && pympress -t 25 main.pdf
IDE integration
Install
tinymist
.
Run
tinymist --log-filter=tinymist_project::compiler=info preview main.typ --font-path etc --preview-mode=slide
Or, optionally, run
pympress main.pdf
with the below config:
nvim
vim.lsp
.
config
(
'tinymist'
,
{
cmd
=
{
"tinymist"
},
filetypes
=
{
"typst"
},
settings
=
{
exportPdf
=
"onSave"
,
}
})
For live cursor tracking, use this config:
nvim
require
(
'lazy'
).
setup
{
"chomosuke/typst-preview.nvim"
,
ft
=
'typst'
,
version
=
'~1.4'
,
}
vim.api
.
nvim_create_autocmd
(
"FileType"
,
{
pattern
=
"typst"
,
callback
=
function
(
opts
)
if
string.match
(
opts.file
,
"main.typ$"
)
then
vim.cmd
.
TypstPreview
(
"slide"
)
end
end
})
