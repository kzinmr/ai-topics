---
title: "How to create your own Jev using Voyage models"
url: "https://blog.voyageai.com/2026/10/27/how-to-create-your-own-jev-using-voyage-models/"
fetched_at: 2026-10-28T10:01:26.619462+00:00
source: "Voyage AI Blog"
tags: [blog, raw]
---

# How to create your own Jev using Voyage models

Source: https://blog.voyageai.com/2026/10/27/how-to-create-your-own-jev-using-voyage-models/

TL;DR
– In this post, we show how to outperform
Jev
using Voyage models for personalized prediction, including imputation, classification, and regression. The model is fit on embeddings of the documents in a MongoDB collection that already have a field (e.g., a movie’s rating) and predicts that field for all remaining documents. Across 50 real-world prediction tasks, adding free & open-source Voyage embeddings of the whole document to the raw fields reduces errors by 37% with voyage-4-nano and by 44% with voyage-json, an experimental model for JSON documents. On the 29 classification tasks, voyage-json makes 48% fewer errors than TypeSafe AI’s Jev (88.3 vs. 77.6 AUROC).
Many MongoDB collections have a field that is set in some documents and missing in others, e.g. a support ticket’s priority may only be set on older tickets. MongoDB documents mix scalar fields with free text, lists, and nested sub-documents. Tabular models need a flat table, so the usual approach is to flatten each document and drop what does not fit, which hurts accuracy. General models like
Jev
label documents directly, without learning from the labeled documents already in the collection. Using Voyage models, you can build your own version that learns from these documents:
Turn each document into a JSON string, leaving out the field to predict
Embed each JSON string with a Voyage model, e.g., voyage-4-nano locally or voyage-4-large through the Voyage API
Fit a prediction model such as XGBoost on the embeddings of the documents where the field is set
Predict the field for the remaining documents and write it back to the collection
How it works
The prediction model takes the embedding of a full JSON document as input, so free text, lists, and nested sub-documents are used along with any scalar fields. To fit the model, you can simply provide documents where the target field is already set. The embeddings only need to be computed once, so testing different prediction models is fast.
A movie (full JSON string) is embedded, and the prediction model turns the embedding into a predicted rating.
The evaluation below uses voyage-4-nano, our open-weight model, which runs locally (on a GPU if one is available). voyage-4-lite, voyage-4, and voyage-4-large are available through the Voyage API and need no GPU. We also report voyage-json, an experimental model that we post-trained from voyage-4-lite for predictions on JSON documents. Any scikit-learn estimator can be fit on the embeddings. We use XGBoost for the movie ratings and ridge regression on the raw fields plus the embedding for the 50 tasks.
The example below builds the movie rating model from our evaluation with pymongo, XGBoost, and voyage-4-large through the Voyage API. It fits the model on movies with a known rating, then saves a predicted rating to each newer movie:
For a field with categories, use xgb.XGBClassifier, whose predict_proba returns a probability for each category. To run voyage-4-nano locally instead, as in our evaluation, load it with sentence-transformers as shown on its
Hugging Face model card
and call encode_document in place of vo.embed.
Evaluation Details
Datasets.
We evaluate on MongoDB’s sample_mflix.movies collection, which is part of the
sample data
available on any Atlas cluster, and on a suite of 50 real-world prediction tasks. For the movies, we fit a model on the 17,527 movies released before 2010 and predict the IMDb rating of the 5,914 movies released from 2010 on. The 50 tasks consist of 7 tasks from MongoDB’s sample data, all 21 tasks of
TextTabBench
, and 22 tasks collected from the web. 29 of them predict a category and 21 predict a number.
Method and Metrics.
For the movies, we embed the title, year, runtime, age rating, genres, cast, directors, and plot of each movie with voyage-4-nano and use XGBoost as the prediction model. The other ratings in the documents (Rotten Tomatoes, Metacritic, awards, IMDb votes) are not used. We report the average error in rating points and the share of movies predicted within one point of their actual rating. For the 50 tasks, we take 5,000 documents per task and split them 80/20 at random, by time, or by group. The target field is masked and the whole document is embedded, and a ridge regression model is fitted on the raw fields plus the embedding. We report AUROC for classification and R² for regression (both × 100), averaged over the tasks and 3 random splits, and count the error as 100 minus the score.
Baselines:
For the movies, we compare against always guessing the average rating of the older movies. For the 50 tasks, we compare against the raw fields alone and six open embedding models from 23M to 8B parameters: all-MiniLM-L6-v2, bge-small-en-v1.5, Qwen3-Embedding-0.6B, Nemotron-3-Embed-1B, Qwen3-Embedding-4B, and Nemotron-3-Embed-8B. On the 29 classification tasks, we also compare against TypeSafe AI’s Jev.
Results
Movie ratings.
On movies released from 2010 on, the model has an average error of 0.68 rating points and predicts 78% of movies within one point of the actual rating, compared with 0.76 and 72% for always guessing the average rating. Once the embeddings were computed, fitting took 79 seconds and predicting the ratings of all 5,914 movies took 8 seconds on 16 CPU threads. Example predictions are in Appendix A.
Movies with a known rating (blue) are used to fit the model, and the model adds a predicted rating (orange) to newer movies.
50 prediction tasks.
The bar chart below shows the average performance over the 50 tasks when each model’s embedding is added to the raw fields, which score 52.1 on their own. Specifically:
voyage-json and voyage-4-nano improve the average to 73.3 and 70.0, which is 44% and 37% fewer errors than the raw fields alone, respectively.
voyage-4-nano outperforms all other open models except Nemotron-3-Embed-8B, which has over 20 times as many parameters.
The 6 open models score between 62.9 and 70.8, or 23% to 39% fewer errors.
Average performance over 50 tasks (AUROC for classification, R² for regression, × 100), with each model’s embedding added to the raw fields.
Comparison with Jev.
On the 29 classification tasks, voyage-json reaches an average AUROC of 88.3, compared with 77.6 for Jev, which is 48% fewer errors. Unlike Jev, this approach needs labeled documents, which only need to be embedded once.
Average AUROC on the 29 classification tasks (× 100).
Community library: mongo-predict
mongo-predict is a community library that wraps these steps for MongoDB. It adds helper methods to pymongo collections that fit a prediction model and store it in the database. A $predict step at the start of an aggregation pipeline then embeds and scores the matching documents in the Python client, and the rest of the pipeline runs on the server as usual. The example below fits the same movie rating model with voyage-4-nano, the default embedding model:
mongo-predict is open source and available on
GitHub
(docs
here
), and its README has more examples and demos on MongoDB’s sample data. It works with MongoDB 5.0 or later, on Atlas or self-managed, and can be installed with pip:
pip install “pymongopredict @ git+https://github.com/mishelsikder/mongo-predict”
Try Voyage models today!
To use Voyage API models, head over to our
docs
to get started and learn more; the first 200M tokens are free.
Follow us on
X (Twitter)
and
LinkedIn
to stay up-to-date with our latest releases.
Appendix A – Example predictions
The table below shows the actual and predicted IMDb ratings for the eight most voted movies released from 2010 on.
Movie
Actual
Predicted
Inception (2010)
8.8
7.7
The Dark Knight Rises (2012)
8.5
7.8
The Avengers (2012)
8.1
6.1
Django Unchained (2012)
8.5
6.8
Interstellar (2014)
8.7
8.0
Shutter Island (2010)
8.1
7.2
The Hunger Games (2012)
7.3
7.4
The Wolf of Wall Street (2013)
8.2
7.5
