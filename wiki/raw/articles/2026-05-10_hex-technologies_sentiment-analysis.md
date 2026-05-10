---
title: "How to build a sentiment analysis model in Python | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/sentiment-analysis/"
scraped: "2026-05-10T01:29:10.107363+00:00"
lastmod: "2022-12-09"
type: "sitemap"
---

# How to build a sentiment analysis model in Python | Hex 

**Source**: [https://hex.tech/blog/sentiment-analysis/](https://hex.tech/blog/sentiment-analysis/)

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
How to build a sentiment analysis model in Python
Learn how to classify the sentiment in a body of text
Gabe Flomo
Further reading
December 9, 2022
Share:
twitter
linkedin
What is sentiment analysis 🤔
Sentiment analysis is a natural language processing (
NLP
) technique that aims to detect/extract the tone or feeling from a body of text. Usually, sentiment is classified as being
positive, negative, or neutral
which gives us a measure of "the level of satisfaction." However, it can easily be used to classify emotion, intention, and even predict user ratings.
Say you're an analyst for a company called
Apricot™
that sells high end computers. It's a Monday and your boss tells you to go through every review ever written about the company and wants you to create a report that showcases the overall satisfaction of your customer base. Having over 50k customer reviews, you wonder how you will ever be able to achieve such a feat! Luckily, you have plenty of data scientist friends to go to for guidance and most of them suggest that you use a sentiment analysis model, however, you have no idea what that is or how it works.
Your lovely data scientist friends wrote you a tutorial to walk you through all of the conceptual and technical aspects of using a sentiment analysis model so that you can make your boss happy. Let's get started!
Copy
from transformers import pipeline
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from collections import Counter
from sklearn.metrics import accuracy_score
Pretrained models with Huggingface 🤗
In machine learning there is a concept called
transfer learning
-- which in short, means using a pre-trained model as the starting point for another task.
Huggingface
is a platform that provides access to thousands of these models so that you don't need to spend time and resources creating models from scratch. They provide over 200 sentiment analysis models that you can download from the
hub
and getting started with them only takes a few lines of code.
Copy
model = pipeline(model = "nlptown/bert-base-multilingual-uncased-sentiment")
The model that we're using is a
BERT model
finetuned for sentiment analysis tasks. For context,
BERT
is a model that achieves state of the art results on most language tasks. Being a
transformer
(no, not the car 😔 ), its structure is fundamentally different from the neural networks previously used for language modeling by adding what's known as
attention
. Without getting to deep into it, attention allows the model to give more weight to the parts of text that are most relevant/important. How does it do this, you ask?? Math.
Dataset 📊
The data comes from
Kaggle
and consists of over 65k cell phone reviews from different companies. The dataset is split into two tables so we will load both of them and join them together to get our "main" dataset.
Copy
reviews = pd.read_csv('reviews.csv')
# rename body to reviews
reviews.rename({'body':'review'}, axis = 1, inplace = True)
items = pd.read_csv('items.csv')
Copy
select brand, R.rating, review from reviews as R
join items as I on R.asin = I.asin
Preprocess data 🔄
Now that we've got our full dataset, some preprocessing is required to prepare our review data for our sentiment analysis model.
The first thing we're going to do is drop all of the rows where there isn't a valid review or company name present.
Copy
dataset = df.dropna(subset = ['brand', 'review'])
The model expects each body of text to be at most 128 characters, so we'll reduce our dataset to only include reviews with a word count of 128 or less. We also find that there are a lot of rows where the brand name is repeated multiple times before observing a different brand. This may lead to selecting reviews from only a few brands and not the others. Therefore, we'll shuffle our dataset to introduce a bit of randomness.
Copy
# filter the dataset to reviews with 128 characters or less
dataset['token_count'] = dataset['review'].apply(lambda review: len(review.split()))
mask = dataset['token_count'] < 128
dataset = dataset.loc[mask]
subset = shuffle(dataset, random_state = 444)[1000:1500]
Predicting sentiment 😄😐🙁
Now that we've got our dataset in a good state, all we need to do is pass our list of reviews to our sentiment model to obtain our predicted ratings.
Copy
reviews = subset['review'].tolist()
# ratings = model(reviews, truncation = True) # This can take up to 2 minutes so we are going to load the predicted ratings from a file
ratings = pd.read_csv('ratings.csv').to_dict(orient = 'records')
The predicted ratings returned from our model are given to us as a list of dictionaries, like the following:
Copy
[{'label': '2 stars', 'score': 0.4741453528404236}]
The following cell will extract both the label and the score for each prediction which we can use to add new columns to our dataframe.
Copy
predicted_rating = [int(r['label'][0]) for r in ratings]
rating_confidence = [round(r['score'] * 100, 2) for r in ratings]
subset['predicted_rating'] = predicted_rating
subset['rating_confidence'] = rating_confidence
subset = subset[['brand', 'review', 'rating', 'predicted_rating','rating_confidence']]
Results ✅
Let's see how well our model does at predicting sentiment as well as how we can use the predictions to learn something about customer satisfaction for each company.
Since our original dataset contains the actual rating for each review, we can calculate an accuracy score to get an idea of how well our model performed. We have also created a way to convert our star ratings into sentiment labels.
Negative
: A rating of 1 or 2
Neutral
: A rating of 3
Positive
: A rating of 4 or 5
Copy
labeler = {
1: 'negative',
2: 'negative',
3: 'neutral',
4: 'positive',
5: 'positive'
}
subset['sentiment'] = subset['predicted_rating'].apply(lambda rating: labeler[rating])
In terms of model performance, the score on the top is the model's accuracy score for predicting the actual review rating. The score on the bottom is the model's accuracy score for predicting overall sentiment.
Now, we can use the results of our model to create a report that showcases the percentage of each sentiment category for all reviews for each company.
knowledge
Note: Although this is a good way to measure performance per company, it is not a good method for understanding how one company may compare to others as there aren't an equal number of observations for each.
Sentiment distribution from NLP: Sentiment analysis
Lastly, we can create a word cloud visualization to give us and idea of the words commonly associated with each sentiment of category.
Most common words by sentiment type from NLP: Sentiment analysis
Conclusion 😌
Congratulations for making it to the end of this tutorial! Here's a cookie as a token of our appreciation 🍪. Today you learned:
What sentiment analysis is
What a pre-trained model is
How to use a pre-trained model for sentiment analysis
We just barely scratched the surface with what pre-trained models can do as well as the applications for sentiment analysis. If interested in going deeper, we suggest looking more into the following topics.
Fine-tuning pre-trained models
(to re-train your own models with less data!)
Emotion detection
This article was influenced by the sentiment analysis article on the
Huggingface website
.
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
