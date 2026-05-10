---
title: "The Essential Steps in Data Preprocessing for Different Data Formats | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/data-preprocessing-steps-python/"
scraped: "2026-05-10T01:29:52.059251+00:00"
lastmod: "2023-12-01"
type: "sitemap"
---

# The Essential Steps in Data Preprocessing for Different Data Formats | Hex 

**Source**: [https://hex.tech/blog/data-preprocessing-steps-python/](https://hex.tech/blog/data-preprocessing-steps-python/)

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
The Essential Steps in Data Preprocessing for Different Data Formats
Data preprocessing refines raw data for accurate analysis by handling missing values, normalizing and processing data.
Andrew Tate
Further reading
December 1, 2023
Share:
twitter
linkedin
In this article
Preprocessing Structured Data
Preprocessing Textual Data
Preprocessing Temporal Data
Preprocessing Image Data
Getting Your Data Ready
Get started for free
"Garbage In, Garbage Out."
A concept every data analyst is familiar with. You can’t expect to gain any huge insights from a bad dataset. The input data’s quality dictates the output data’s quality.
This underscores the significance of data preprocessing. Data preprocessing is a collection of techniques and procedures to refine raw data into an analyzable format. The initial preprocessing steps can substantially influence the eventual insights or predictive accuracy, whether you're working with structured tabular data, intricate textual data, time-anchored temporal data, or even multimedia datasets. Here we want to provide an overview of the essential data preprocessing steps for
exploratory analysis
, tailored to these different data types, and how to effectively implement them to step up the foundation of any of your analysis.
You can find each of these snippets in a Hex notebook
here
.
Preprocessing Structured Data
Structured data, which you find in relational databases and spreadsheets, consists of clearly defined data types organized into columns and rows. Its tabular nature makes it a common starting point for many data analysis tasks. Preprocessing structured data usually requires handling missing data and converting data into the correct format for analysis.
Handling Missing Values
Null or missing values can distort statistical analyses and lead to biased machine learning model training. One common approach is imputation, where missing values are replaced with statistical measures, like mean or median.
Copy
import pandas as pd
data = pd.read_csv('data_file.csv')
data.fillna(data.mean(), inplace=True)
In this code, the pandas library reads a CSV file into a DataFrame, then the
fillna
method replaces missing values (
NaN
) with the mean of each column. Care should be taken when selecting the imputation strategy, as it can influence the subsequent data analysis outcomes. For datasets with a significant amount of missing data, understanding the nature and pattern of these missing values becomes crucial to avoid inadvertently introducing bias.
Data Normalization
Data normalization is a crucial preprocessing step, especially when features in the dataset have varying scales and ranges. Without normalization, features with larger scales can disproportionately influence the outcome of machine learning algorithms, especially those that rely on distance calculations such as k-means clustering or k-nearest neighbors.
This involves scaling all numeric variables to a standard range, typically between 0 and 1, ensuring that different features contribute equally to model training. Moreover, normalized data often leads to faster convergence during the training process and can improve the generalization capability of some models.
Copy
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
data[['feature1', 'feature2']] = scaler.fit_transform(data[['feature1', 'feature2']])
Here, using the
MinMaxScaler
from
scikit-learn
, we scale 'feature1' and 'feature2' columns. The
fit_transform
function computes the minimum and maximum values of the columns and scales them accordingly.
One-hot Encoding
Handling categorical data is pivotal in the preprocessing pipeline as many machine learning models require numerical input features. Categorical variables, represented as text or discrete numbers, can introduce complexity due to their non-continuous nature and varied cardinalities.
One-hot encoding converts categorical variables into a format that can be provided to machine learning algorithms without losing the inherent categorical information. It represents each unique value of a categorical feature as a separate binary column. This ensures that no unintended ordinal relationships are introduced, as can happen with other encoding methods like label encoding.
Copy
data_encoded = pd.get_dummies(data, columns=['categorical_feature'])
The
get_dummies
function from pandas creates binary columns for each category in ‘categorical_feature' and populates them with ones and zeros based on the original data. By doing this, the transformed dataset retains the categorical information in a structure that's amenable to a wider array of algorithmic treatments without making unwarranted assumptions about the relationships between categories.
Feature Selection
Reducing dimensionality can lead to more efficient computation and can prevent overfitting. One common method is using correlation to eliminate redundant or irrelevant features through
feature selection
.
Copy
correlation_matrix = data.corr().abs()
upper_triangle = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper_triangle.columns if any(upper_triangle[column] > 0.95)]
data.drop(to_drop, axis=1, inplace=True)
This code computes a correlation matrix for the DataFrame and identifies pairs of features with a correlation greater than 0.95. Features from each high-correlation pair are then dropped, leaving behind a reduced set of features.
Preprocessing structured data involves tasks tailored to its tabular nature, addressing issues specific to columns and rows, and ensuring it's primed for rigorous, accurate analysis.
Preprocessing Textual Data
Textual data, often unstructured and derived from various sources like documents, social media, and websites, presents its unique challenges. Preprocessing this type of data is crucial to extract meaningful patterns and relationships and to perform advanced analytical techniques such as
natural language processing
.
Tokenization
Tokenization is a fundamental step in text preprocessing, especially for natural language processing (NLP) tasks. It involves dissecting a string or document into smaller units, such as words, phrases, symbols, or other meaningful elements called tokens. These tokens become the basic units for subsequent analysis and modeling. Precise tokenization is critical for understanding the context and meaning of the text, as it influences the accuracy of feature extraction and the performance of NLP models.
Copy
from nltk.tokenize import word_tokenize
text = "This is an example sentence."
tokens = word_tokenize(text)
Here, we use the
word_tokenize
function from the
nltk
(Natural Language Toolkit) library to split a given sentence into individual words or tokens. This function is sophisticated enough to separate words and punctuation, recognizing various intricacies of English grammar. It provides a foundation for further steps like stemming, lemmatization, and stopword removal, which refine the tokens for tasks such as sentiment analysis, topic modeling, or document classification.
Removing Stop Words
Stop words, like "and", "the", and "is", are common words that may not contribute meaningfully to text analysis. Removing them can improve analysis efficiency and focus.
Copy
from nltk.corpus import stopwords
filtered_tokens = [word for word in tokens if word.lower() not in stopwords.words('english')]
Here, we filter out stop words from our tokenized text using a predefined list of English stop words available in the
nltk
library.
Stemming and Lemmatization
Stemming and lemmatization condense words to their foundational forms. By doing so, they aid in achieving consistency in word representation, which can significantly enhance the performance of downstream tasks like text classification, topic modeling, and
sentiment analysis
.
While both stemming and lemmatization target word reduction, they follow different methodologies:
Stemming uses heuristic processes to clip off word suffixes, leading to a crude reduction, often producing non-real words.
Lemmatization employs linguistic rules, often using lexicon and morphological analysis, to return words to their base or dictionary form, ensuring the resultant word has a meaningful representation.
Copy
from nltk.stem import PorterStemmer, WordNetLemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
Using the
PorterStemmer
and
WordNetLemmatizer
classes from
nltk
, we transform our filtered tokens into their stemmed and lemmatized forms, respectively. The choice between stemming and lemmatization often hinges on the specific requirements of a task, the linguistic richness of the data, and the desired level of word normalization.
Text Vectorization
To analyze text using algorithms, we need to convert it into numerical format. TF-IDF (Term Frequency-Inverse Document Frequency) is a common method that represents text as vectors where each word's weight is adjusted by its frequency across documents.
Copy
from sklearn.feature_extraction.text import TfidfVectorizer
documents = ["This is a sample.", "This document is another example."]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
Here, using
TfidfVectorizer
from
scikit-learn
, we convert a list of documents into a matrix of TF-IDF values, where each row represents a document and each column corresponds to a unique word in the entire corpus.
Preprocessing textual data involves tasks that transform human-readable content into structured, machine-analyzable formats, ready for in-depth data analysis or model training.
Preprocessing Temporal Data
Temporal data, characterized by its association with timestamps or chronological order, often arises in time series analysis, financial modeling, or event logging. Preprocessing for this type of data ensures that time-dependent relationships are effectively captured.
Parsing Date and Time
Converting string representations of dates and times into datetime objects simplifies subsequent time-based operations.
Copy
import pandas as pd
data = pd.DataFrame({'date': ['2023-01-01', '2023-01-02', '2023-01-03']})
data['date'] = pd.to_datetime(data['date'])
Here, we use pandas'
to_datetime
function to convert a column of date strings into datetime objects, allowing for easier time-based indexing and operations.
Handling Time Gaps
In time series data, missing timestamps can lead to inaccurate analysis. It's essential to identify and address these gaps.
Copy
full_date_range = pd.date_range(start=data['date'].min(), end=data['date'].max())
data = data.set_index('date').reindex(full_date_range).reset_index().rename(columns={'index': 'date'})
This code first creates a complete range of dates between the minimum and maximum dates in our dataset. It then reindexes the data based on this complete range, ensuring any missing dates are included as rows with NaN values.
Extracting Time-based Features
For certain analyses, it's beneficial to derive features such as the day of the week, month, or year.
Copy
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data['day_of_week'] = data['date'].dt.dayofweek
Using the datetime accessor (
dt
) in pandas, we extract the year, month, and day of the week from each datetime object in our 'date' column and store them as separate features.
Resampling Time Series Data
For
time series
data analysis, the granularity or frequency at which data points are recorded can be pivotal. Often, raw time series data might be captured at an extremely detailed level, which, while informative, can also be overwhelming and computationally intensive to process.
Resampling offers a solution by allowing analysts and data scientists to adjust the time frame, enabling the examination of data at various levels of granularity, from milliseconds to years. This not only aids in revealing different patterns or behaviors in the data but also optimizes computational resources. The transformation can be accompanied by aggregation methods like sum, mean, or max to provide a consolidated view of the data over the newly defined intervals.
Copy
time_series_data = pd.DataFrame({'date': full_date_range, 'value': range(len(full_date_range))})
resampled_data = time_series_data.set_index('date').resample('M').mean()
In this snippet, we generate a sample time series DataFrame with a hypothetical set of dates and values. By utilizing the
resample
method from pandas, we transform the dataset's granularity to a monthly frequency, computing the average value for each month in the process. Resampling provides flexibility, and different functions can be applied based on the analytical goals, ensuring an appropriate representation of the underlying time series dynamics.
Lag Features
For predictive modeling of time series data, creating lag features (values from previous time steps) can be invaluable.
Copy
data['value_lag1'] = data['value'].shift(1)
By using the
shift
method, we create a new column where each entry is the value from the previous row (i.e., the previous time step).
Preprocessing temporal data necessitates an understanding of the sequential nature of the data and applying methods that respect and utilize this time-based ordering.
Preprocessing Image Data
Image data, consisting of pixels representing visual content, is widely used in domains like computer vision and medical imaging. Preprocessing for images ensures they are in a standardized format and augmented appropriately for better model generalization.
Loading and Resizing
Ensuring images have uniform dimensions is crucial, especially when batch processing or using convolutional neural networks (CNNs).
Copy
from PIL import Image
img_path = "path_to_image.jpg"
img = Image.open(img_path)
img_resized = img.resize((224, 224))
Here, we use the
Image
class from the
PIL
(Python Imaging Library) to load an image from a given path. The
resize
method is then utilized to resize the image to a 224x224 pixel resolution.
Grayscale Conversion
In some analyses, color information might not be necessary. Converting images to grayscale can reduce dimensionality and computational overhead.
Copy
img_gray = img.convert("L")
Using the
convert
method with the "L" mode, we transform the loaded image into a grayscale version, retaining luminance and discarding color information.
Normalization
Scaling pixel values to a range between 0 and 1 can help in stabilizing training and improving convergence in machine learning models.
Copy
import numpy as np
img_array = np.asarray(img_resized)
normalized_array = img_array / 255.0
After converting the image to a numpy array, we divide each pixel value by 255 (the maximum pixel value for an 8-bit image) to normalize the image data.
Edge Detection
Edges in an image represent areas where there are rapid changes in pixel intensity. Edge detection helps identify significant transitions in pixel intensity in an image and can be used as a feature extraction method in various applications. Detecting these edges can be useful for object recognition, segmentation, and other image analysis tasks. One popular method for edge detection is the Sobel operator.
Copy
import cv2
# Load the image using OpenCV
image_cv = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
# Apply Sobel edge detection
sobel_x = cv2.Sobel(image_cv, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image_cv, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = cv2.magnitude(sobel_x, sobel_y)
Here, we use the OpenCV library, a powerful tool for computer vision tasks. The
Sobel
function computes the gradient approximation of the image intensity for the x and y directions separately. The combined gradient magnitude, which represents the edges, is then computed using the
magnitude
function.
This edge-detected image can be used as input for further analysis or as a feature for machine learning tasks.
Getting Your Data Ready
The above might seem like laborious tasks before the fun starts. But really the shouldn’t be termed “preprocessing” as they are an integral part of the entire flow of data analysis. Without doing the above for whichever type of data you are analyzing, you will have poor results.
Starting with these, you end up with higher quality data which leads to higher quality analysis which leads to higher quality insights.
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
