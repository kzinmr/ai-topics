---
title: "Natural Language Processing in Python | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/natural-language-processing-python/"
scraped: "2026-05-10T01:29:49.784582+00:00"
lastmod: "2023-04-04"
type: "sitemap"
---

# Natural Language Processing in Python | Hex 

**Source**: [https://hex.tech/blog/natural-language-processing-python/](https://hex.tech/blog/natural-language-processing-python/)

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
Natural Language Processing in Python
Using computers to programmatically understand and interpret human language
Andrew Tate
Data
April 4, 2023
Share:
twitter
linkedin
In this article
Using the NLTK library in Python
Using Python with online models for natural language processing
From Tokenization to Understanding: The NLP Toolbox
Get started for free
knowledge
This tutorial walks through the key components of natural language processing in Python. For an example of a published project using NLP, check out
this project in our gallery
.
Human language doesn’t come naturally to computers. Machines are more the ones-and-zeros type of folks. Not that there’s anything wrong with that.
But it
would
be extremely helpful if they could understand human language. We’d be able to talk to them, get them to answer questions, and for them to organize, summarize, and synthesize all the information we humans have generated up to now.
Natural Language Processing, or NLP, is about doing just that. NLP is a field for developing algorithms and models that can accurately parse, analyze, and manipulate textual (and spoken) data. Core NLP tasks are things like tokenization, parsing, and sentiment analysis. Advanced NLP techniques also involve natural language
understanding
, which focuses on extracting meaning from text, and natural language
generation
, which involves producing coherent, contextually appropriate responses or narratives.
We can do all of this stuff in Python, and for the simpler tasks we can make use of Python libraries built to understand natural language. For more advanced tasks, we can use online models trained on huge data sets, and call these models from within Python.
Let’s start by using some Python libraries to do basic text processing.
Using the NLTK library in Python
Let’s start with something simple– counting words. This may seem super basic, but a lot of NLP algorithms start from fairly simple concepts like word frequency and build from there.
We’re going to use what is the ‘core’ NLP library for Python, the Natural Language Toolkit,
NLTK
.
We’ll set up our environment first. This helps isolate and organize our NLP project. (If you’re following along in a Hex project, you don’t need to do any of this— nltk is already installed for you).
Copy
python3 -m venv env
source env/bin/activate
Then we can install our library:
Copy
pip install nltk
Once installed, we’re going to import the library and some specific functions:
Copy
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
nltk.download('punkt')  # Download the Punkt tokenizer
Well get to what each of these functions does in a second. First let’s get some text to analyze:
Copy
text = "Natural Language Processing is the process of extracting information from human language."
The first step is to “tokenize” the text. Tokenization is just splitting the text into ‘tokens.’ This usually, but not always, means individual words. Here we’re explicitly using
word_tokenize
and the
Punkt
tokenizer, so we are looking to get individual words:
Copy
# Tokenize the text
tokens = word_tokenize(text)
Here we get:
Copy
print(tokens)
['Natural', 'Language', 'Processing', 'is', 'the', 'process', 'of', 'extracting', 'information', 'from', 'human', 'language', '.']
This is a common first step across almost all natural language processing. Languages are made up of words, so getting down to that fundamental level is a key step.
Once we have the words/tokens, we want to count the frequency of each:
Copy
# Count word frequencies
fdist = FreqDist(tokens)
# Print the word frequencies
print(fdist)
N = 3
top_words = fdist.most_common(N)
print(f"Top {N} words: {top_words}")
Top 3 words: [('Natural', 1), ('Language', 1), ('Processing', 1)]
So, in this case, all the words are only used once in our example text. But if we tried to analyze longer pieces of text we’d find more interesting word frequencies.
Let’s combine our NLTK library with the ability to get some text from the web. For this we’ll use the
BeautifulSoup
and
requests
libraries. (Again, if you’re using Hex, these are already installed and you can skip this step.)
Copy
pip install beautifulsoup4 requests
We’ll do all our imports first. We’ll get the NLTK functions, as well as requests and BeautifulSoup:
Copy
import requests
from bs4 import BeautifulSoup
import nltkfrom nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
nltk.download("punkt")
nltk.download("stopwords")
We’re going to use requests to fetch the data for the Taylor Swift Wikipedia page, and then use BeautifulSoup, an HTML parser, to extract the actual text from the HTML:
Copy
# Download the Wikipedia page
url = "https://en.wikipedia.org/wiki/Taylor_Swift"
response = requests.get(url)
html_content = response.text
# Extract the text using Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")
text = soup.get_text()
Now we have a variable containing all the text from that page we can start processing it. Again, the first step is to tokenize the text into individual words. But here we also have two other steps.
The first is to change all the words into lower case. NLP algorithms will treat capitalized words and lower case words as different, when we want them to be the same for analysis. Changing all the text into lower-case makes sure ‘Taylor’ and ‘taylor’ are counted as the same.
Then we remove ‘stop words.’ IN NLP, stop words are the very common words used in the language you are analyzing. In English, these are words like ‘the’, ‘and’, ‘of’, ‘it’ and so on. If we counted these, they would always be at the top of any frequency distribution (for other types of analysis, such as topic modeling or sentiment analysis, you normally keep these in as they can change the context of the sentence).
Copy
# Tokenize the text
tokens = word_tokenize(text)
# Convert tokens to lowercase and remove non-alphabetic characters
tokens = [token.lower() for token in tokens if token.isalpha()]
# Remove stopwords
stop_words = set(stopwords.words("english"))
filtered_tokens = [token for token in tokens if token not in stop_words]
So we end up with
filtered_tokens
to work from, where all the tokens are lower-case and all stop words removed.
We can then run the same analysis as above:
Copy
# Count word frequencies
fdist = FreqDist(filtered_tokens)
# Print the most frequent words
N = 10
top_words = fdist.most_common(N)
print(f"\nTop {N} words:")
for word, frequency in top_words:
print(f"{word}: {frequency}")
The output:
Copy
Top 10 words:
swift: 911
taylor: 680
retrieved: 647
original: 339
archived: 322
music: 229
november: 203
october: 187
billboard: 175
december: 171
This starts to show some of the limitations of these NLP techniques. It’s clear that ‘swift’ and ‘taylor’ should be top words in this document. But why ‘retrieved’ or ‘archived?’ Does Taylor Swift moonlight as a librarian?
No, its because the footnotes of any Wikipedia article is full of lines like:
_
"Taylor Swift No. 1 on iTunes"
.
Great American Country
. December 19, 2007. Archived from
the original
on March 3, 2012. Retrieved July 5, 2010._
There are over 600 on Taylor’s page. These algorithms don’t know these words are irrelevant to the main content of this document. When you are doing analysis like this, you have to already have a certain context about the documents so you can add words like this to your stoplist, or to iterate with your analysis as you get to understand the documents. This is why
cleaning and preparing your text data is so important in natural language processing
.
Let’s move on to a couple of more sophisticated analyses in natural language processing.
First, sentiment analysis. Sentiment analysis is a natural language processing technique used to determine the sentiment or emotion expressed in text, such as positive, negative, or neutral emotion. It involves analyzing patterns, such as word choice, syntax, and context to identify and extract subjective information.
We can do this with NLTK. First, we’ll import NLTK, the
SentimentIntensityAnalyzer function, and the vader_lexicon
. Vadar (Valence Aware Dictionary and sEntiment Reasoner), is a model of emotional text. It knows words like ‘love’ have a positive sentiment, but also knows that the phrase ‘does not love’ has a negative sentiment:
Copy
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# Download the VADER lexicon
nltk.download('vader_lexicon')
# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
Let’s give it a sentence to analyze. The type of thing you see on social media all the time:
Copy
# Example text
text = "I absolutely love Hex! It's fantastic."
Now we can perform the analysis.
polarity_scores
gives a positive or negative score depending on whether the text has a positive or negative sentiment.
Copy
# Perform sentiment analysis
sentiment_scores = sia.polarity_scores(text)
# Interpret sentiment scores
compound_score = sentiment_scores['compound']
if compound_score >= 0.05:
sentiment = "Positive"
elif compound_score <= -0.05:
sentiment = "Negative"
else:
sentiment = "Neutral"
# Print the sentiment scores
print(sentiment_scores)
print("Sentiment:", sentiment)
{'neg': 0.0, 'neu': 0.264, 'pos': 0.736, 'compound': 0.855}
Sentiment: Positive
We can see that the positive score for this is 0.736, and the compound score (a normalized version of the sum of the valences with some other parameters). So it’s positive.
If we input the text “I absolutely hate Hex! It's terrible.” we get:
Copy
{'neg': 0.711, 'neu': 0.289, 'pos': 0.0, 'compound': -0.8118}
Sentiment: Negative
You can imagine how a company might hook their Twitter feed up to sentiment analysis like this, looking for product mentions and how customers are feeling about their products.
You can see some sentiment analysis in action here using
Hex and Huggingface
.
A final analysis we can look at is topic modeling. Topic modeling is a machine learning technique that you can use to discover latent themes or topics within some documents. It does this by identifying patterns in word usage, and then clusters similar documents based on their content.
We’ll use a different library for this, Gensim. Gensim comes from what the library was initially supposed to do. GENerate SIMilar lists of documents:
Gensim started off as a collection of Python scripts for the Czech Digital Mathematics Library
dml.cz
project, back in 2008. The scripts served to generate a short list of the most similar math articles to a given article.
-
What is Gensim
First, we’ll install Gensim using pip:
Copy
pip install gensim
Then we’ll import all our functions:
Copy
import gensim
from gensim import corpora
from gensim.models import LdaModel
from pprint import pprint
Then set up our ‘documents.’ Here, each document is only a single sentence long, but these could be full documents, like the math papers it was originally built for, or Wikipedia pages of the world’s top pop stars:
Copy
# Example corpus
documents = [
"The economy is working better than ever",
"A new study shows that people are happier",
"The latest sports news reports the winning team",
"Advances in technology are improving our daily lives",
"Economic growth is expected to continue",
"Fans are excited about the upcoming sports event"
]
The first step is to preprocess the data. Like with NLTK, this is about tokenizing the data into words and storing them (literally called a ‘bag of words’ in NLP):
Copy
# Pre-process and tokenize the text
def preprocess(text):
return gensim.utils.simple_preprocess(text, deacc=True, min_len=3)
tokens = [preprocess(doc) for doc in documents]
# Create a dictionary and a bag-of-words representation for each document
dictionary = corpora.Dictionary(tokens)
corpus = [dictionary.doc2bow(token) for token in tokens]
Then we’ll do the analysis. Gensim uses an unsupervised machine learning algorithm called Latent Dirichlet Allocation (LDA) to find the topics in the documents. LDA assumes each document is a mixture of topics, and each topic is a distribution over words. LDA uses
Dirichlet distributions
as the priors for Bayesian inference to estimate these distributions. The result is a set of topics, where each topic is really a set of words and the probabilities those words will be found in those topics.
Copy
# Train the LDA model
num_topics = 2
lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=20, random_state=42)
# Show the topics
pprint(lda_model.print_topics())
Which outputs:
Copy
[(0,
'0.105*"the" + 0.058*"sports" + 0.035*"team" + 0.035*"latest" + '
'0.035*"reports" + 0.035*"news" + 0.035*"winning" + 0.035*"working" + '
'0.035*"ever" + 0.035*"than"'),
(1,
'0.082*"are" + 0.048*"improving" + 0.048*"people" + 0.048*"study" + '
'0.048*"shows" + 0.048*"happier" + 0.048*"advances" + 0.048*"new" + '
'0.048*"lives" + 0.048*"technology"')]
So topic 0 seems to be about sports, working, and winning, and topic 1 is about improvement and technology. You can just about see how the LDA has extracted these from each of the documents.
People use this type of topic modeling to extract information from documents and do content analysis like keyword finding. It can also help to organize and summarize large collections of text.
Using Python with online models for natural language processing
There’s a Skynet-sized elephant in the room as we talk about natural language processing.
AI.
The last three years have seen an effective paradigm shift in how people process natural language. Whereas it used to be only libraries such as NLTK and Gensim used, now the shift has turned to Large Language Models (LLMs) trained and deployed online.
Why describe what LLMs are when we can just get the currently best known LLM,
ChatGPT
, to do that itself.
Can you describe what you are to a knowledgeable audience?
“Certainly! I am ChatGPT, a highly advanced artificial intelligence language model developed by OpenAI. I am based on the GPT-4 architecture, which is a generative pre-trained transformer model designed for natural language understanding and generation tasks. My primary function is to engage in meaningful and coherent conversations with users, providing useful information and answering questions on a wide range of topics.
As a knowledgeable audience, you might appreciate a deeper understanding of my inner workings. I am built upon the foundation of a deep learning framework called Transformers. These models are known for their ability to handle long-range dependencies and parallelization, which is crucial for processing large amounts of text data. I was trained on a vast corpus of text, which helps me generate contextually relevant and grammatically accurate responses to user inputs.
Some of the key characteristics of GPT-4 and, by extension, ChatGPT are:
Scalability: GPT-4 has an even larger architecture than its predecessors, with billions of parameters that enable it to understand and generate highly nuanced and context-aware responses.
Transfer learning: I can generalize my knowledge and capabilities across different domains, thanks to my pre-training on a diverse range of text data sources.
Fine-tuning: In order to adapt my responses to specific use cases, I can be fine-tuned on smaller datasets that cater to particular topics, industries, or conversational styles.
Self-attention mechanism: This is a core component of the Transformer architecture, allowing me to weigh the importance of different words and phrases in a given context, which ultimately leads to more accurate and contextually relevant responses.
While my capabilities are extensive, it's important to remember that I am still an AI model, and my knowledge is limited to the training data I've been exposed to, which has a cutoff date of September 2021.”
You can use GPT with Python through the OpenAI API. Though you can’t yet use the latest model, GPT-4, GPT-3 is available.
First, install the OpenAI Python library. As before, this package is available in the Hex standard environment.
Copy
pip install openai
Then we’ll import the library and add our API key (you have to sign up for an account
here
. Keep in mind that using the OpenAI API may incur costs, so be cautious with the number of requests you make.)
Copy
import openai
# Replace 'your_api_key' with the actual API key you obtained from OpenAIopenai.api_key = "your_api_key"
After that, we’re going to create a function called
topics_text
to handle our requests. This function is a wrapper around our API call to OpenAI. The parameters we need to send to OpenAI are:
Engine. This is the model within OpenAI that we are going to use. In this case, that is their latest model,
text-davinci-002.
Prompt. This is the heart of the OpenAI API call. The prompt is what you are telling the model to do. Here, we’re going to mimic our topic modeling above, so our prompt is “
Can you tell me the topics that these sentences are about
” followed by the text we’re going to pass into our function (that you’ll see below)
Max_tokens. THis is the maximum number of tokens we want in the response. As we said above, this roughly corresponds to words, so we won’t get more than 100 words in the response back.
N. The number of responses we want. Just one here.
Stop. If we want the model to stop generating text when it produces a certain word or phrase, we can add that here.
Temperature. This is kind of a creativity score for the model. The closer to 0 it is, the more deterministic the output (basically, it will always produce the same output). The closer to 1, the more the model will produce random answers.
We’ll then return the response from the API from the function:
Copy
def topics_text(text, model="text-davinci-002", max_tokens=100):
prompt = f"Can you tell me the topics that these sentences are about:\n\n{text}\n"
response = openai.Completion.create(
engine=model,
prompt=prompt,
max_tokens=max_tokens,
n=1,
stop=None,
temperature=0.5,
)
return response.choices[0].text.strip()
Here’s the text we’ll add. It’s the same as in the Gensim topic modeling example above.
Copy
# Documents for topic modeling
text = """
"The economy is working better than ever",
"A new study shows that people are happier",
"The latest sports news reports the winning team",
"Advances in technology are improving our daily lives",
"Economic growth is expected to continue",
"Fans are excited about the upcoming sports event",
"""
Then we’ll print the response:
Copy
topics = topics_text(text)
print("Topics:")
print(topics)
Which outputs:
Copy
The economy, happiness, sports, technology, economic growth, and sports fans.
So with this API call we’ve completed an NLP task, topic modeling. GPT-3 has analyzed those documents and told us what they are about. The output is also more human readable than the Gensim version.
Here’s another version, this time we’re asking it to summarize some text for us:
Copy
import openai
openai.api_key = "your_api_key"
def summarize_text(text, model="text-davinci-002", max_tokens=100):
prompt = f"Please provide a brief summary of the following text:\n\n{text}\n"
response = openai.Completion.create(
engine=model,
prompt=prompt,
max_tokens=max_tokens,
n=1,
stop=None,
temperature=0.5,
)
return response.choices[0].text.strip()
# Example text to summarize
text = """
The history of artificial intelligence (AI) dates back to antiquity, with myths, stories, and rumors of artificial beings endowed with intelligence or consciousness by master craftsmen. However, the field of AI research was founded on the claim that human intelligence can be so precisely described that a machine can be made to simulate it. This raises philosophical arguments about the nature of the mind and the ethics of creating artificial beings endowed with human-like intelligence. These issues have been explored by myth, fiction, and philosophy since antiquity.
"""
summary = summarize_text(text)
print("\nSummarized text:")
print(summary)
Which outputs:
Copy
Summarized text:The history of artificial intelligence (AI) dates back to antiquity. AI research was founded on the claim that human intelligence can be so precisely described that a machine can be made to simulate it. This raises philosophical arguments about the nature of the mind and the ethics of creating artificial beings endowed with human-like intelligence. These issues have been explored by myth, fiction, and philosophy since antiquity.
Though some tasks are still best performed with the NLP-specific libraries, the ability to train and use these LLMs means you can almost instantly perform a lot of sophisticated NLP tasks such as sentiment analysis, text summarization, and question answering.
From Tokenization to Understanding: The NLP Toolbox
There’s never been a better time to learn about NLP and be involved in the field. There is still a lot of basic work to be done with libraries such as NLTK, Gensim, and SpaCy. If you have a particular corpus of work you need to do close analysis on, these libraries will still perform rigorously.
But you also now have access to the best language model of all time via a single API call. Python is the go-to language for both traditional and modern natural language processing. Learning the basics but also having AI API call knowledge, means you’ll be able to do pretty much anything within the field.
GPT (and the other LLMs coming online) are capable of performing tasks that even five years ago would have been impossible within NLP. What will be possible five years from now?
Share:
twitter
linkedin
This is something we think a lot about at Hex, where we're creating a platform that makes it easy to build and share interactive data products which can help teams be more impactful.

If this is is interesting, click below to get started, or to check out opportunities to join our team.
✨ Get started for free
👩‍💻 Open roles
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
