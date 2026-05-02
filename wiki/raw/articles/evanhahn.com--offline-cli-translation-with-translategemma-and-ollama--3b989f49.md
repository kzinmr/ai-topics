---
title: "Offline command line translation with TranslateGemma + Ollama"
url: "https://evanhahn.com/offline-cli-translation-with-translategemma-and-ollama/"
fetched_at: 2026-05-02T07:00:43.429660+00:00
source: "evanhahn.com"
tags: [blog, raw]
---

# Offline command line translation with TranslateGemma + Ollama

Source: https://evanhahn.com/offline-cli-translation-with-translategemma-and-ollama/

Offline command line translation with TranslateGemma + Ollama
I wrote a simple script that translates text at the command line, completely offline. Here’s an example of how it works on my computer:
echo
'¿Cómo estás?'
| translate
# => How are you?
It combines a few tools:
Here’s the pseudocode of how it works:
source = read_stdin()
# Uses Efficient Language Detector
source_language = detect_language(source)
# Uses JavaScript's `navigator.language`
target_language = get_system_language()
# Uses Ollama + TranslateGemma
return
translate(source, source_language, target_language)
I built this because I couldn’t find anyone else who had done it. It’s written in Deno for my specific needs—for example, it only translates text into your system’s language—but could easily be adapted if you need something else.
I like that I can do offline, private, automatic translation. It’s imperfect, but useful for me!
Here’s the source code.
