---
title: "Feature Engineering in Data Science: A Complete Guide"
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/what-is-feature-engineering-in-data-science/"
scraped: "2026-06-23T06:00:30.868777+00:00"
lastmod: "2026-05-21"
type: "sitemap"
---

# Feature Engineering in Data Science: A Complete Guide

**Source**: [https://hex.tech/blog/what-is-feature-engineering-in-data-science/](https://hex.tech/blog/what-is-feature-engineering-in-data-science/)

Skip to main content
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
📊
AI analytics use case:
how Mercor unlocked $100M in revenue
🪩
Come hang at Club Hex:
June 16-17 at Databricks Data + AI Summit
🤯
Generative data apps:
Gorgeous, interactive dashboards and apps you can build with just a prompt
📖
State of Data Teams 2026
discover key insights from data leaders
🙏
It's just "Hex"!
Not "HEX" or "Hex dot tech"
Blog
Feature engineering in data science: A complete guide
You've swapped algorithms three times and accuracy hasn't moved. The problem almost certainly isn't the model.
The Hex Team
Data
May 21, 2026
Share:
twitter
linkedin
In this article
What is feature engineering?
Feature engineering techniques by data type
Pitfalls that quietly destroy model performance
Automated feature engineering
Where feature engineering is heading
Shipping models that actually work
Frequently asked questions
Get started for free
You've built the model, tuned the hyperparameters, and the accuracy is mediocre. So you swap in a different algorithm. Still mediocre. You try a third. Same story.
Then a colleague suggests computing the ratio of two existing columns, a feature that captures something neither column says on its own. Accuracy jumps four points. No algorithmic change. Just a better input.
Feature engineering is the work that happens between raw data and model training, where you shape what the model actually sees. It's often the difference between a model that technically runs and one that actually works. Getting the features right consistently matters more than choosing the most complex algorithm.
What is feature engineering?
Feature engineering is
feature representation
as trainable values in the feature vector. In practice, that means selecting which variables matter, changing existing variables through scaling or encoding, and creating entirely new variables from what you already have.
If you have house prices and square footage in separate columns, neither alone tells the model much about relative value. But divide price by area to get price-per-square-foot, and you've created a feature that encodes domain understanding not explicit in either raw variable.
Feature engineering sits between data acquisition and model training in the ML pipeline. Raw data is rarely suitable for direct consumption by algorithms, which makes this step essential. A
scikit-learn study
on cyclical time features showed that applying spline-based feature engineering reduced prediction error from approximately 14% to approximately 10% of maximum demand, attributable solely to how the features were represented, not to any model architecture change.
The
CRISP-DM framework
, a widely used framework for data mining, is often associated with the observation that data preparation can account for a large share of project time, commonly cited in the 60% to 80% range. Feature engineering often makes up a meaningful part of that work. It's the work that doesn't feel glamorous and still consistently determines whether your model ships or stalls.
Feature engineering techniques by data type
Numerical, categorical, datetime, and text data each need different approaches.
Numerical features
If you're feeding numerical data into linear models, SVMs, neural networks, or PCA, you'll probably need to rescale it first.
Scikit-learn preprocessing
is direct about this: many estimators behave poorly if individual features don't roughly resemble standard normally distributed data.
Standardization
(StandardScaler) centers features to mean 0 and variance 1. It's your default choice for most distance-based and gradient-based algorithms. Just know that outliers remain influential after scaling.
Min-Max scaling
(MinMaxScaler) bounds values to a fixed range like [0, 1]. Useful when your model needs bounded inputs, neural network input layers, for instance, but a single extreme value can compress everything else into a narrow band.
Log transformation
tames right-skewed distributions like income or transaction amounts. Use
np.log1p()
when zeros are present in your data:
Copy
import numpy as np
Copy
skew_features = ['LotFrontage', 'LotArea', '1stFlrSF', 'GrLivArea', 'SalePrice']
Copy
for col in skew_features:
Copy
df[col] = np.log(df[col])
Binning
(pd.cut(), pd.qcut())
converts continuous features into discrete intervals, helpful when the relationship between a variable and target is step-like rather than smooth. The downside is that all variation within a bin disappears entirely.
Polynomial features
(
PolynomialFeatures
) generate cross-feature products and powers, letting linear models capture non-linear relationships. But feature count
grows rapidly with polynomial degree
, so regularization is often essential to prevent overfitting.
Categorical features
One-hot encoding
creates a binary column per category. It's the safe default for nominal (unordered) categories with low cardinality, but if you have hundreds of categories, dimensionality explodes fast. Scikit-learn's
OneHotEncoder
supports
min_frequency
and
max_categories
parameters to aggregate rare categories, a practical control most people overlook.
Ordinal encoding
maps categories to integers in a specified order. If there's a natural ranking (Low < Medium < High), this works fine. Apply it to nominal categories, though, and you've introduced a false ordinal relationship that can mislead distance-based and linear models.
Target encoding
replaces each category with a statistic of the target variable, typically the mean for regression or the positive-class probability for classification. It handles high-cardinality features without dimensionality explosion, but needs cross-validation or smoothing to prevent target leakage. More on that risk shortly.
Datetime features
Extract datetime components:
Copy
df['hour'] = df['datetime_col'].dt.hour
Copy
df['dayofweek'] = df['datetime_col'].dt.dayofweek
Copy
df['quarter'] = df['datetime_col'].dt.quarter
Copy
df['is_month_end'] = df['datetime_col'].dt.is_month_end
Raw integer extraction doesn't preserve cyclicality. A model treating month as an integer can't infer that December and January are adjacent points in a cycle. Sine/cosine encoding solves this by mapping cyclical features into two-dimensional space where boundary values stay close:
Copy
# Convert datetime to seconds, then encode cyclicality
Copy
# day = 86400 (seconds in one day)
Copy
day = 86400
Copy
timestamp_s = df['datetime_col'].astype(np.int64) // 10**9
Copy
df['Day_sin'] = np.sin(timestamp_s * (2 * np.pi / day))
Copy
df['Day_cos'] = np.cos(timestamp_s * (2 * np.pi / day))
Time-since features
, days since last purchase, account age, time since last login, are often useful recency signals in predictive systems.
Text features
Text needs the most processing to become something a model can work with.
TF-IDF
(
TfidfVectorizer
) weights term counts by how rare they are across your corpus. Common words get down-weighted while rare, informative ones float to the top. It works well for document classification but it doesn't account for words that share similar meanings.
Word embeddings
solve this by encoding semantic relationships in dense vectors. Pre-trained models from
gensim
or
sentence-transformers
capture contextual meaning, but they're computationally heavier and may not cover domain-specific vocabulary well.
For very large vocabularies or streaming data,
feature hashing
(
HashingVectorizer
) maps tokens to a fixed-size vector using a hash function, trading the ability to recover feature names for memory efficiency.
Interaction and derived features
Sometimes the signal lives in the relationship between two variables, not in either one alone. Price-per-square-foot, debt-to-income ratio, click-through rate, these are all manual combinations informed by domain knowledge. Libraries like
feature-engine
provide
MathFeatures
and
RelativeFeatures
to formalize these operations in reproducible pipelines.
Binary indicator features (
is_weekend
,
is_first_purchase
) can also be surprisingly effective when a threshold crossing is more predictive than the raw value.
Pitfalls that quietly destroy model performance
Feature engineering mistakes don't always surface as obvious errors. They surface as models that look great during development and fall apart in production.
Data leakage
Data leakage is the highest-severity concern in feature engineering. It produces training metrics that look strong but collapse entirely in production because the model was trained with information it can't have at prediction time.
The most common form is fitting preprocessing changes on the full dataset before splitting. If you fit a
StandardScaler
on all rows, including test rows, your model has already "seen" test set statistics during training. The fix is straightforward but easy to get wrong:
Copy
# CORRECT: fit only on training data
Copy
X_train, X_test, y_train, y_test = train_test_split(X, y)
Copy
scaler = StandardScaler()
Copy
scaler.fit(X_train)
Copy
X_train_scaled = scaler.transform(X_train)
Copy
X_test_scaled = scaler.transform(X_test)
Temporal leakage
is equally dangerous: using random train-test splits on time-ordered data can include future observations in the training set. For time-series data, always use time-based splits and walk-forward validation.
The universal enforcement rule is
split first, then engineer features.
Any imputation, normalization, or encoding must be fit on training data only.
Missing values handled in the wrong order
Imputing before the train-test split is another form of leakage. The correct sequence is to split first, analyze the missingness mechanism using training data only, fit the imputer on the training set, then change both sets without refitting.
A practical tip many people miss is adding a binary indicator feature encoding whether the original value was absent. The
missingness signal
can be predictive, and silently replacing it with a mean throws that signal away.
Too many engineered features
As the number of features increases, available training data becomes sparse relative to the feature space. Watch for training accuracy substantially exceeding validation accuracy, or feature importance scores spread thinly with no clear leaders.
For regularized models (Ridge, Lasso, SVMs), high feature counts aren't inherently problematic. Regularization is often a more robust first response than aggressive manual pruning.
Non-reproducible feature pipelines
Ad-hoc notebook changes, mutable data sources, and library version drift all create silent production drift.
Wrap all transformers in scikit-learn
Pipeline
objects. Pipelines encapsulate every
fit
call, can be serialized with the model artifact, and ensure cross-validation folds get properly isolated changes. When your team works in
collaborative notebooks
with built-in version history, pipeline discipline and real-time collaboration help catch these issues before they reach production.
Automated feature engineering
Automated feature engineering tools generate candidate features programmatically, applying mathematical operations and aggregations across your data without manual specification. Feature engineering consumes an estimated 50–70% of project time in data science workflows, so even partial automation pays off quickly.
Featuretools
and its Deep Feature Synthesis (DFS) algorithm generate features by applying primitives, aggregation functions like
COUNT, MEAN, SUM
and transform functions like
MONTH
,
HOUR
, across relationships in multi-table datasets. It's particularly strong for relational and transactional data. The "deep" part refers to stacking primitives: DFS can automatically generate something like
MODE(sessions.device)
. DFS is combinatorial rather than insight-driven, though. It generates candidates.
tsfresh
handles time series specifically, automatically extracting
more than 1,200 features
from time series data, statistical measures, complexity estimates, trend analyses, and then filtering for relevance using hypothesis tests.
A 2025 study from Erasmus University Rotterdam found that combining automated feature engineering with AutoML increased accuracy by an average of
0.54% compared to AutoML alone
. That might sound small, but critically, AutoFE never significantly
hurt
performance across the evaluated datasets. It either helped or was neutral.
Automated tools generate what can be computed, while practitioners decide what matters. Featuretools supports
seed features
, manually crafted domain-informed features that DFS then stacks upon, as the primary mechanism for injecting domain knowledge into automated generation. The best results come from combining automated candidate generation with practitioner judgment.
This played out at
Figma's analytics team
, where researcher Rie McGwier used Hex's Notebook Agent to compress the learning curve from weeks to hours while building NPS and Product Health programs, focusing on strategy and domain interpretation while the agent handled the mechanical work of writing queries and generating charts.
Once features are validated and ready for deployment, the next challenge is managing them at scale. In production ML, feature stores are used to manage the storage and serving of feature data, with a critical capability:
point-in-time retrieval
that prevents data leakage by ensuring training data only includes feature values available at each example's label time.
Where feature engineering is heading
Feature engineering's character is shifting, though it isn't going away.
For unstructured data (images, audio, text), deep learning models can automatically learn to extract relevant features from raw inputs through neural network layers. For tabular and structured data, traditional feature construction still remains a major part of the workflow.
LLM embeddings are one concrete pattern for classical models. You generate embeddings using a pre-trained language model, then use those dense vectors as feature inputs to downstream models. In practice, choosing the embedding model becomes part of the broader feature-design decision. For high-cardinality categorical variables specifically, entity embeddings learned during neural network training can be extracted and reused as feature representations.
Feature versioning and dependency tracking become more important as teams reuse shared features and embeddings across models. A change to an embedding model affects every downstream consumer, and teams benefit from infrastructure that makes those dependencies visible.
Shipping models that actually work
Feature engineering is where domain knowledge meets
warehouse architecture
. The techniques themselves, scaling, encoding, creating interaction terms, aren't complicated individually. The hard part is applying them correctly: splitting before changing data, wrapping everything in pipelines, validating that automated candidates actually make domain sense, and keeping the whole thing reproducible as your team grows.
What separates good feature engineering from great feature engineering is understanding the problem you're solving. Automated tools can generate hundreds of candidate features from your relational data, and a practitioner who understands the business context will spot the features that actually matter, the ones grounded in how the system actually works. That intuition compounds over time, which is why the iteration cycle of hypothesize, test, and validate is where practitioners create the real value. Tools don't replace that loop; the best ones make it faster.
The teams that move fastest tend to work in environments where the iteration loop is tight, where you can explore a feature idea in a notebook environment, validate it against SQL queries, and share the result with a colleague without switching tools or exporting files.
Hex
brings SQL, Python, and version history into one workspace, so you can go from feature hypothesis to validated pipeline to
data apps
without the tool sprawl that slows everything down. That keeps
multi-modal analytics
connected to the actual work of testing features, reviewing code, and publishing results others can use.
The work gets more interesting when you're spending time on the features themselves rather than the infrastructure around them.
Sign up for Hex
or
request a demo
to see how it fits your workflow.
Frequently asked questions
How does feature engineering differ from feature selection?
Feature engineering and feature selection are complementary but move in opposite directions. Feature engineering creates new variables, changing, combining, or deriving features from raw data to give the model more meaningful inputs. Feature selection reduces the number of predictors to simplify the model and improve generalization. The correct workflow order is engineer first, then select, then train. Performing selection before engineering can eliminate raw features that would have been valuable inputs to derived features. In practice, the number of features to include can often be treated as a hyperparameter and optimized jointly with other model parameters through cross-validation.
Do tree-based models need the same feature engineering as linear models?
No, and understanding the difference saves significant effort. Tree-based models (Random Forest, XGBoost, LightGBM) split on thresholds, making them invariant to monotonic changes like scaling and normalization. You can skip
StandardScaler
and
MinMaxScaler
entirely for these algorithms. Linear models, SVMs, and neural networks are a different story.
Scikit-learn preprocessing
notes that many estimators behave poorly if individual features aren't roughly on the same scale, so preprocessing is essential. That said, tree-based models still benefit substantially from well-constructed derived features: domain-informed ratios, interaction terms, and time-since variables can improve test error. The practical rule is to skip scaling for trees, but not feature creation, and for linear models, do both.
How do you know when you've done enough feature engineering?
There's no universal stopping rule, but several signals help. One practical heuristic is to add features one at a time and stop when test loss no longer improves. If additional features begin hurting accuracy, you've likely introduced redundant or correlated predictors. Cross-validation stability is particularly reliable. If a feature helps in some folds but not others, it's probably fitting noise rather than capturing a generalizable pattern. One practical guideline is to favor the least complex treatment that improves performance without degrading calibration or fairness. Iterating in an environment where you can quickly test hypotheses and compare cross-validation results, like a collaborative notebook, helps shorten the feedback loop between "I think this feature matters" and "here's the evidence."
Share:
twitter
linkedin
Get "The Data Leader’s Guide to Agentic Analytics"  — a practical roadmap for understanding and implementing AI to accelerate your data team.
Download
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
