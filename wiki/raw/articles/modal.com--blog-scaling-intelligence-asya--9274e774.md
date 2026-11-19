---
title: "Building new research tools for Maya epigraphy on Modal"
url: "https://modal.com/blog/scaling-intelligence-asya"
fetched_at: 2026-11-19T10:03:58.660251+00:00
source: "Modal Blog"
tags: [blog, raw]
---

# Building new research tools for Maya epigraphy on Modal

Source: https://modal.com/blog/scaling-intelligence-asya

Miguel Novelo grew up surrounded by Maya glyphs carved into stone across Mexico's Yucatán peninsula, printed in books, and painted on ceramics. For centuries, Maya scribes used this writing system to record histories, trace the movements of the heavens, and keep calendars. For most of his life, he saw them only as drawings.
"I never thought I could understand them," he says.
Expand image
Close
Novelo is an artist and lecturer at Stanford, where he teaches a course called World Building: Video, Sound, and Space. His grandmother taught him Maya as a child, and decades later, when she learned he wanted to go deeper, she pulled out her books and handed him a Spanish-to-Maya dictionary. That gift set him on a path that led to
(Φ ᆺ Φ) asya
, his commissioned work for
Scaling Intelligence
, the exhibition Modal presented with Gray Area this fall.
The piece invites visitors to draw in a bed of sand and watch their marks become glyphs in a growing, collective codex. Behind the piece is a larger ambition: using AI and cloud compute to build tools that could change how researchers read one of the world's great writing systems.
How
asya
came to be
The project's roots go back to Novelo's research on the cenotes and landscapes of the Yucatán. It took shape in INFRAMUNDO, his first institutional solo exhibition, a four-month show at the Institute of Contemporary Art San José, where he brought AI and interactive projection together with Maya culture.
For that show, he wanted to use one specific glyph from a cosmic plate found at Calakmul, in Campeche. He spent six hours one Sunday trying to understand it, working from his grandmother's dictionary, books from his uncle and grandparents, sources from the Stanford library, and AI models. And at the end of the day he made a break through and was finally able to understand the glyph—a black cenote or black well.
"That was a mind-blowing moment," he says. "I've seen these drawings my entire life." Six hours, he points out, is nothing compared to what the same work might have taken him without all the tools he had at his disposal. "It could be a lifetime just to get there."
Novelo learned early that you can't upload a photo of a glyph and ask a model to translate it. Out of the box, models tend to give what he calls "a very average positive answer," which is rarely useful to an artist with a specific point of view.
So he starts by giving the model context: the glyphs themselves, their history, the scholarly books that discuss their translations, and personal knowledge that isn't documented online. With that grounding, the model can start recognizing patterns, and Novelo can check each step against his sources to make sure he's on the right path.
"There are so many threads, and AI is able to see those threads faster than me and find those connections," he says.
He also works across several models, because each one approaches a problem differently. He describes them as having different ontologies, different senses of what is what. The models bring speed and breadth. Novelo brings the knowledge that comes from his family, his ties to the Yucatán, and his research.
Writing in sand
At Gray Area,
(Φ ᆺ Φ) asya
centers on a sculpture of Asya, the Siamese cat of Yuri Knorozov, the Soviet linguist whose work in the 1950s laid the foundation for deciphering Maya script. Visitors trace shapes and words in a bed of sand and the system processes each drawing, renders it as a new glyph, and adds it to a cumulative codex projected on scrim. Over the course of the exhibition, the codex grows into a collective text.
Expand image
Close
The piece follows the philosophy Novelo teaches in his world-building class: give people many ways in, so no one needs to know Maya history to connect with the work. That is also why he works in installations. "I'm going to get you through the aesthetics, through the story, through the tactility, through the sound, through the visuals," he says. "There's always something that's going to get you."
At its heart, the piece is about leaving a trace. Maya glyphs survived because they were carved into stone, while Spanish colonizers burned the books written in the language. That attempted erasure is one reason there is no Rosetta Stone for Maya script. Drawing in sand, a geological material, connects each visitor to that same impulse to leave something behind.
Building his own models on Modal
Novelo used Modal to build a fast pipeline that turns 2D glyph images into 3D models. He started with roughly 100 Maya syllabic signs, drawn from a dataset assembled by Benjamin Gonzalez through the Maya Corpus project. Those syllables can represent much of the spoken Maya language. In the gallery, visitors' drawings fed the same process, and Novelo plans to use the drawings collected during the show to keep refining it.
The bigger reason compute matters is independence. General-purpose large language models aren't trained on the grassroots knowledge that lives in the Yucatán, so Novelo can't rely on them alone. What he needs are smaller, specialized models that understand both what glyphs look like and the context around them.
"Otherwise I have to rely on corporate large language models to do the specific things I want to do," he says. "They don’t have a complete understanding of Maya culture and language."
With access to Modal, building those models became something he could start now. "Only having access to this, I can dream about this," he says. Without it, he estimates the same work could take years.
An "IRL LLM" of epigraphers
The exhibition also put Novelo in touch with leading epigraphers, including Gonzalez and the Liga de Epigrafistas de México. Epigraphers work to read and understand inscriptions, helping make the histories preserved in Maya glyphs accessible to people today. Every two weeks, the group meets to read glyphs that haven't been studied much. Forty to fifty people look at one glyph together and offer what they know. Novelo calls it "an IRL LLM situation," where everyone chimes in until a reading takes shape.
Working from a single photograph, he can generate a 3D model of a carving so the group can relight it, rotate it, and look closer. Modeling one by hand used to take him about a week and now it takes a fraction of that time.
The longer-term goal is a tool for researchers, scientists, and anyone interested in Maya glyphs, one that doesn't exist today. Novelo is especially interested in depth: how the depth and style of a carving might reveal a kind of syntax that flat images miss. Testing that idea means digitizing a large number of carvings in 3D and training models to find patterns across them.
"We now have all the foundations and the technologies to do it," he says.
The power of language and time
Some people argue that AI has no place near Indigenous writing systems, and that cultural knowledge should be protected and kept within the communities it belongs to. When asked, Novelo acknowledges the concern. He approaches the question through Maya history, where attempts at erasure have made the survival and transmission of knowledge especially important. For him, helping more people understand the language is part of keeping that knowledge alive.
"Maya culture was intended to be erased completely," he says. He describes its history as one of resistance, continuity, and international collaboration, and sees that collaboration as part of what has kept it alive. He also acknowledges the need for respect and repair, from artifacts scattered in museums around the world to tourism that takes from local communities.
For Novelo, the strength is in language. "The more Maya speakers, the more people understand," he says. Knorozov himself cracked the script from Leningrad, working from printed reproductions across the divisions of the Cold War.
The more he studies Maya cosmovision, the more it shapes how he thinks about technology. He thinks about cycles, about what happens when technologies die, and about the resources and waste they leave behind. He wants to think in thousands of years, rather than the next quarter.
Miguel will be bringing his piece to
Minnesota Street Project
in January.
Scaling Intelligence
was presented by Gray Area and Modal, curated by Wade Wallerstein, with exhibition design by Seabrook Gubbins. Glyph data comes from the Maya Hieroglyphic Database, accessed through Maya Corpus by Benjamin Gonzalez.
