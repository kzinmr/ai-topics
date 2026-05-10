---
title: "Text cleaning for NLP with Python | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/cleaning-text-data/"
scraped: "2026-05-10T01:29:52.393014+00:00"
lastmod: "2022-12-12"
type: "sitemap"
---

# Text cleaning for NLP with Python | Hex 

**Source**: [https://hex.tech/blog/cleaning-text-data/](https://hex.tech/blog/cleaning-text-data/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🤖
Notebook Agent Act II:
AI tools for data people just got even better
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
🪄
Bringing the magic of AI to data:
agentic analytics tools that actually work
📖
State of Data Teams 2026
discover key insights from data leaders
Platform
chevron-down
Products
Agentic notebooks
Powerful, deep-dive analysis without the silos
Conversational self-serve
The best BI tool isn't just a BI tool
semantic-models
Context Studio
Build trust in data with semantic models and AI governance
cli
Hex CLI
Control your analytics from the terminal
Capabilities
Exploratory analysis
Go from quick question to deep analysis to data app in one place
Embedded analytics
Ship secure, customer-facing data experiences
app-builder
Data apps
Build and share interactive dashboards and reporting
Integrations
Out-of-the-box connections and flexible APIs
magic
AI & agents
Agentic workflows to empower your entire team
Solutions
chevron-down
lightbulb
Explore all solutions
One connected system - infinite data answers
By team
solutions-data-leader
Data leader
Focus your team and scale answers
solutions-product
Product
Build your product with data, not gut feels
solutions-marketing
Marketing
Turn scattered data into clear growth opportunities
solutions-sales
Sales
Clear pipeline. Confident forecasts
solutions-customer-success
Customer success
Create a complete view of customer health
Enterprise
Resources
chevron-down
Get started
integrations
Switching to Hex
A guide to getting started on agentic analytics
Templates
Jumpstart with pre-built projects
Hex Foundations
Video series
help
Docs
Resources and product guides
Changelog
Product updates
Inspiration
Blog
From data teams to data teams
Guides
Learn how to do more with data, together
Events
Learn and connect with peers
Customer stories
Empowering the best data teams
Partners
Learn more about our partnerships
save
Download
The Data Leader's Guide to AI Analytics
A practical roadmap for understanding and implementing AI to accelerate your data team and enable true self-service.
Pricing
Log In
Get started
Blog
Text cleaning for NLP with Python
Learn how to prepare text data for NLP tasks
Gabe Flomo
Data
December 12, 2022
Share:
twitter
linkedin
What is text preprocessing?
Text preprocessing consists of a series of techniques aimed to prepare text for natural language processing (NLP) tasks. Noise in text comes in several forms, such as emojis, punctuations, different cases, and more. The main goal of cleaning text is to reduce the noise in the dataset while still retaining as much relevant information as possible.
Copy
import pandas as pd
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
import numpy as np
import re
from sklearn.utils import shuffle
import string
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
Important terminology 📝
Before we dive in, we need to define some terms that will be used throughout this tutorial.
Document
: A distinct unit of text. This could be a sentence, paragraph, or an article.
Copy
doc1 = "Hello my name is Gabe"
doc2 = "What is your name?"
Corpus
: refers to a collection of texts or documents.
Copy
corpus = [doc1, doc2]
Tokens
: Tokenization is a way of separating a piece of text into smaller units called tokens. Here, tokens can be either words, characters, or subwords (
n-gram characters
).
Copy
document = "Hex is awesome"
tokens = ['Hex', 'is', 'awesome']
Normalizing text ⚖️
Text normalization is the process of converting the case of your text so that it is the same across the entirety of your document. What this looks like is converting
"Hello my name is Gabe"
into
"hello my name is gabe"
. Why is this step so important you ask? Well, in many language modeling tasks, models will make use of an object called the vocabulary, which is the set of unique words in a corpus of documents. So if I have the following:
Copy
corpus = [
'My cats love dogs',
'Cats are my best friends',
]
Then the vocab would be:
Copy
vocab = { "My", "cats", "love", "dogs", "Cats", "are" ,"my", "best", "friends"}
In this example, the same word appears in the vocab more than once because the text hasn't been normalized. After normalization, it'd look something like:
Copy
vocab = { "my", "cats", "love", "dogs", "are", "best", "friends"}
And now we've reduced our vocab by 2 words, however, in a murch larger corpus this could reduce our vocab by hundreds of words!
Copy
normalize = lambda document: document.lower()
sample_text = "This Is some Normalized TEXT"
normalize(sample_text)
Removing unwanted characters 🙅🏽‍♀️
The next step is to remove all of the characters that don't add much value or meaning to our document. This may include punctuation, numbers, emojis, dates, etc. To us humans, punctuation can add a lot of useful information to text. This could be adding structure to language or indicating tone/sentiment. For language models, punctuation doesn't add as much context as it does for people and in most cases just adds extra characters to our vocab that we don't need. Having said that, there are some cases when you would want to keep these characters in your data. For example, in text generation tasks it may be useful to keep the punctuation so that your model can generate text that is grammatically correct.
Here we will define a function that removes the following:
Emojis 😔
User mentions (@gabeflomo)
Hashtags (#Hex)
URLs
Punctuation
Copy
# borrowed from stackoverflow https://stackoverflow.com/a/49146722
def remove_emoji(string):
emoji_pattern = re.compile("["
u"\U0001F600-\U0001F64F"  # emoticons
u"\U0001F300-\U0001F5FF"  # symbols & pictographs
u"\U0001F680-\U0001F6FF"  # transport & map symbols
u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
u"\U00002702-\U000027B0"
u"\U000024C2-\U0001F251"
"]+", flags=re.UNICODE)
return emoji_pattern.sub(r' ', string)
def remove_unwanted(document):
# remove user mentions
document = re.sub("@[A-Za-z0-9_]+"," ", document)
# remove URLS
document = re.sub(r'http\S+', ' ', document)
# remove hashtags
document = re.sub("#[A-Za-z0-9_]+","", document)
# remove emoji's
document = remove_emoji(document)
# remove punctuation
document = re.sub("[^0-9A-Za-z ]", "" , document)
# remove double spaces
document = document.replace('  ',"")
return document.strip()
Copy
sample = "Hello @gabe_flomo 👋🏾, still want us to hit that new sushi spot??? LMK when you're free cuz I can't go this or next weekend since I'll be swimming!!! #sushiBros #rawFish #🍱"
remove_unwanted(sample)
# output
'Hello still want us to hit that new sushi spot LMK when youre free cuz I cant go this or next weekend since Ill be swimming'
Removing stop words ❌
In the context of NLP, a stop word is any word that doesn't add much meaning to a sentence, words like
'and', 'that', 'when'
, and so on. Removing these words reduces the size of our vocab and our dataset while still maintaining all of the relevant information in that document. As mentioned before, not all language modeling tasks find it useful to remove stop words, such as translation or text generation. This is because those tasks still take into account the grammatical structure of each document, and removing certain words may result in the loss of this structure. Depending on the language task, it's important to keep in mind which stop words are being removed from your documents. We won't be going into much depth on this but you can check out
this article
that goes even deeper on how to handle this.
NLTK
is a toolkit for working with NLP in python and provides us with various text processing libraries for common NLP tasks. We will be using the stop words from NLTK to filter our text documents.
Copy
def remove_words(tokens):
stopwords = nltk.corpus.stopwords.words('english') # also supports german, spanish, portuguese, and others!
stopwords = [remove_unwanted(word) for word in stopwords] # remove puntcuation from stopwords
cleaned_tokens = [token for token in tokens if token not in stopwords]
return cleaned_tokens
Lemmatization ✂️
Lemmatization is a common NLP technique and is the process of reducing a word to its root form. This is a useful normalization technique as it removes all tenses from a document and simplifies the text of each document.
Image from GitHub
Copy
lemma = WordNetLemmatizer()
def lemmatize(tokens):
lemmatized_tokens = [lemma.lemmatize(token, pos = 'v') for token in tokens]
return lemmatized_tokens
lemmatize("Should we go walking or swimming".split())
# output
['Should', 'we', 'go', 'walk', 'or', 'swim']
Stemming ✂️
Stemming is very similar to lemmatization in that it aims to reduce words to their root; the difference being that stemming algorithms just chop off a part of the word at the tail end to arrive at the stem of the word. This means that it is useful for reducing words to a simplified form but may not be as accurate as a lemming algorithm.
Image from GitHub
Copy
stem = PorterStemmer()
def stemmer(tokens):
stemmed_tokens = [stem.stem(token) for token in tokens]
return stemmed_tokens
stemmer("I love cats more than dogs".split())
# output
['i', 'love', 'cat', 'more', 'than', 'dog']
Putting it all together 🤝
In this last section, we will combine all of the methods previously used into a single function for simple use. Here we will use the
pipeline
function below to clean all of the tweets contained in this
Kaggle dataset
.
Copy
df = shuffle(pd.read_csv("tweets.csv"), random_state=1111)
documents = df.iloc[:20]
Copy
def pipeline(document, rule = 'lemmatize'):
# first lets normalize the document
document = normalize(document)
# now lets remove unwanted characters
document = remove_unwanted(document)
# create tokens
tokens = document.split()
# remove unwanted words
tokens = remove_words(tokens)
# lemmatize or stem or
if rule == 'lemmatize':
tokens = lemmatize(tokens)
elif rule == 'stem':
tokens = stemmer(tokens)
else:
print(f"{rule} Is an invalid rule. Choices are 'lemmatize' and 'stem'")
return " ".join(tokens)
Copy
sample = "Hello @gabe_flomo 👋🏾, I still want us to hit that new sushi spot??? LMK when you're free cuz I can't go this or next weekend since I'll be swimming!!! #sushiBros #rawFish #🍱"
print(pipeline(sample))
# output"
hello still want us hit new sushi spot lmk free cuz cant go next weekend since ill swim"
Copy
cleaned = documents['text'].apply(lambda doc: pipeline(doc))
Let's compare the uncleaned documents to the cleaned ones!
Copy
for clean, dirty in zip(cleaned[15:20], documents['text'][15:20]):
print(dirty)
print(clean, "\n")
Conclusion 🔮
Congratulations 🎉 you've made it all the way through the tutorial!
Based on the comparison of the first few samples, we can see that our text cleaning pipeline does a pretty good job at cleaning our text documents. It can remove URLs, hashtags, emojis, mentions, and all the other characters/words we wanted removed! There are a few hiccups where it could perform a little better such as merging words that have no space between punctuation, but we will leave improving the function up to you 😊
Share:
twitter
linkedin
See how data teams are using Hex to help their cross-functional teams meet their goals.
Get inspired by more data apps
Request a demo
Made with
🍩
☕
🥟
🍺
🍰
🔮
🔒
🥖
🍷
🛌
💜
🥨
🛹
🍤
🧄
🍞
🥥
⛳
🤞
🔊
🎧
on
🌎
.
Company
Careers
Customers
Solutions
Media kit
Newsroom
Platform
AI and agents
Agentic notebooks
Conversational self-serve
Context Studio
Hex CLI
Exploratory analysis
Embedded analytics
Data apps
Integrations
Changelog
Resources
Pricing
Switching to Hex
Enterprise
Docs
Blog
Events
Templates
Compare
Trust Center
Status
Connect
Contact sales
Request a demo
Technical support
LinkedIn
X (Twitter)
YouTube
©
2026
Hex Technologies Inc.
Privacy policy
Terms & conditions
Modern slavery statement
