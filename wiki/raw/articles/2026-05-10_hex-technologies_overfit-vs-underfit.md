---
title: "Overfitting vs Underfitting in ML: Causes, Diagnosis, and Fixes | Hex "
source: "Hex Technologies Blog"
url: "https://hex.tech/blog/overfit-vs-underfit/"
scraped: "2026-05-10T01:29:53.146838+00:00"
lastmod: "2025-12-30"
type: "sitemap"
---

# Overfitting vs Underfitting in ML: Causes, Diagnosis, and Fixes | Hex 

**Source**: [https://hex.tech/blog/overfit-vs-underfit/](https://hex.tech/blog/overfit-vs-underfit/)

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
What is overfitting and underfitting in machine learning?
Recognize when models overfit or underfit, and what to do about it.
The Hex Team
Data
December 30, 2025
Share:
twitter
linkedin
In this article
What is overfitting?
Why overfitting happens
What is underfitting?
Why underfitting happens
The bias-variance tradeoff
Diagnosing overfitting and underfitting
How to fix overfitting
How to fix underfitting
Choosing your next step
Iterating faster on model evaluation
Getting the model fit right
Get started for free
You've trained a model that performs beautifully on your training data. The loss is minimal, the accuracy looks great, and everything seems ready for production. Then you deploy it, and the predictions fall apart on real-world data.
Two problems typically cause this:
Overfitting
means low training error but high validation error. The model memorized your data instead of learning from it.
Underfitting
means high error on both. The model is too simple to capture real patterns.
Both come down to a mismatch between model capacity and data complexity, but they fail in opposite directions. This matters whenever model performance in production diverges from what you saw during training. A churn model that looked great in development but misses actual churners. A fraud detector that flags everything or nothing. An image classifier that works on your test set but fails on slightly different lighting.
If you've ever watched a model ace validation metrics and then fall flat in the real world, you've likely run into one of these problems. Understanding when your model has crossed into either territory — and knowing how to pull it back — is one of the most practical skills in applied
machine learning
(ML).
What is overfitting?
Your model learned the training data too well. It memorized not just the underlying patterns but also the noise, outliers, and spurious correlations unique to that specific dataset. The result: excellent recall of what it's already seen, but poor generalization to new data.
Think of it like a student who memorizes practice problems word-for-word instead of learning the underlying concepts. They'll ace those exact problems again, but struggle when the questions are worded differently. You'll know
overfitting
has occurred when you see a telltale gap between training performance and validation performance: training error drops much lower than validation error, which stays high or starts climbing.
What overfitting looks like in practice:
Your fraud detection model achieves 99% accuracy on your training set. You deploy it, and it catches only 60% of actual fraud cases while flagging legitimate transactions constantly. The model learned the specific patterns of your historical fraud cases rather than generalizable indicators of fraudulent behavior.
Why overfitting happens
Models overfit when there's an imbalance between their capacity and the available data, or when training dynamics push them to memorize rather than generalize.
Too much model capacity
When a model has more parameters than necessary relative to your training examples, it can memorize individual data points rather than find the underlying signal. A neural network with millions of parameters trained on a few thousand examples has enough capacity to encode every quirk and anomaly in that specific dataset.
It's like using a complex equation with dozens of variables to fit just ten data points. You can make it work perfectly, but that equation won't generalize beyond those ten points.
Limited training data diversity
Limited data means the model can't distinguish between genuine patterns and dataset-specific artifacts. A model trained on dog photos mostly taken in parks may learn to use grass as a feature for classification, then fail to recognize dogs photographed indoors.
Without diverse training data showing dogs in many contexts, the model can't separate what actually defines "dog" from incidental details about where the photos happened to be taken.
Training too long
Even with appropriate model complexity, continuing to train after the model has learned the real patterns leads to it picking up noise. The loss keeps decreasing on training data while validation loss increases, and generalization quietly degrades.
During initial epochs, the model learns genuine patterns. But as training continues past that point, it starts fitting itself to random fluctuations with no predictive value. The training curve looks great, but you're actually making the model worse at its real job.
What is underfitting?
Your model is too simple to capture the underlying structure in your data. It misses important patterns and relationships, producing poor predictions on both the training set and new data.
Think of it like trying to describe a symphony using only three musical notes. No matter how you arrange those notes, you can't capture the complexity of the original piece. You'll recognize underfitting when both training and validation errors remain high, showing the model hasn't captured even the basic patterns in your data.
What underfitting looks like in practice:
Your customer lifetime value model uses only purchase frequency as a feature. It predicts roughly the same value for customers who buy frequently, regardless of whether they spend $10 or $10,000 per order. The model lacks the inputs it needs to distinguish high-value from low-value customers.
Why underfitting happens
Models underfit when they lack the capacity or information they need, or when constraints prevent them from learning what's actually there.
Architecture too simple
Using linear regression for data with non-linear relationships, or a shallow decision tree for complex classification, means the model literally cannot represent the true patterns. A straight line can't fit curved data no matter how long you train it.
Missing critical features
If the information your model needs isn't in your features, no architectural sophistication will help. Predicting house prices using only paint color leaves out square footage, location, and number of bedrooms. The model has no access to the information that actually drives the outcome.
Over-regularization
Techniques designed to prevent overfitting can swing too far and prevent the model from learning adequately. Regularization constrains how much the model can adapt to training data, and too much of it is like tying weights to a runner's legs: it prevents them from reaching their actual speed.
Training stopped too early
This one's easy to miss. You stop training before the model has had enough iterations to learn the patterns that are genuinely there. The loss was still dropping, the model was still improving, and you pulled the plug too soon. Same underfitting symptoms, different root cause.
The bias-variance tradeoff
Both overfitting and underfitting connect to a fundamental tension in machine learning, one you've probably heard about if you've taken any ML course.
Bias
is systematic error from wrong assumptions. A model with high bias consistently misses the target in the same direction because it's too simple to capture the true relationship. Linear regression applied to curved data will always underestimate peaks and overestimate troughs.
Variance
is error from sensitivity to training data fluctuations. A model with high variance gives wildly different predictions depending on which training examples it saw. Train it on a slightly different sample and you get a completely different model.
Overfitting means high variance: the model responds to noise, so small changes in training data produce very different predictions. Underfitting means high bias: the model makes strong assumptions that prevent it from capturing true patterns, consistently missing in predictable ways.
The goal is finding the sweet spot where you've reduced bias enough to capture real patterns without increasing variance so much that your model memorizes noise. (Modern deep learning has complicated this picture, as we'll see later.)
Diagnosing overfitting and underfitting
Start by comparing training and validation metrics, then watch how they evolve during training.
Compare training and validation metrics
High error on both training and validation data signals underfitting: the model isn't learning even the patterns in its training data. Low training error but much higher validation error signals overfitting: the model learned the training data, but not in a way that generalizes. The sweet spot is when both metrics converge to similarly low values.
Here's what each scenario typically looks like:
Use learning curves
Learning curves show training and validation scores across training epochs or increasing sample sizes. For overfitting, you'll see training loss continuing to decrease while validation loss plateaus or rises, the classic divergence pattern. For underfitting, both curves stay high and flat, showing the model isn't improving even with more training.
Validate with cross-validation
K-fold cross-validation splits your data into k subsets, training on k-1 and testing on the held-out fold, then rotating. Large variance across folds signals overfitting: the model performs well on some splits but poorly on others. Consistently poor performance across all folds signals underfitting.
How to fix overfitting
Once you've confirmed overfitting, the fix involves constraining your model so it learns patterns instead of noise. Start with the highest-impact techniques and work down based on what your diagnostics reveal:
Regularization first:
Try L2 regularization strengths like 1e-4, 1e-3, and 1e-2 while monitoring validation loss. If overfitting persists at stronger values, your model may need architectural changes instead.
Early stopping second:
Set patience to 5–10 epochs with no validation improvement. Save checkpoints at each improvement so you can recover the best model.
Dropout for neural networks:
Typical starting ranges are 0.3–0.5 for fully connected layers, 0.2–0.3 for convolutional layers. Disable during inference.
Data augmentation when data-limited:
Use domain-appropriate transformations: rotations and flips for images, synonym replacement for text, time stretching for audio.
Cross-validation for tuning:
Use k-fold cross-validation to tune hyperparameters. Large variance across folds confirms overfitting.
Ensembles as a fallback:
Random forests and gradient boosting (XGBoost, LightGBM) tend to reduce variance relative to single models and often outperform them on tabular data.
The key is iterating systematically. Change one thing at a time, watch validation performance, and keep track of what worked.
How to fix underfitting
Where overfitting requires constraints, underfitting requires expansion: more capacity, better information, or fewer restrictions on learning.
Work through these approaches based on what you suspect is limiting your model:
Add model capacity gradually:
Start by adding hidden layers or neurons to neural networks, or move from linear models to polynomial regression or tree-based methods. Logistic regression → random forest often provides the non-linearity needed.
Engineer better features:
Create polynomial features and interaction terms. For time-series, add lag features, rolling statistics, and seasonal components. Domain-specific features often encode patterns the model couldn't learn from raw inputs.
Reduce regularization:
If regularization is too strong, decrease L1/L2 penalty strength progressively (1.0 → 0.1   → 0.01). Lower dropout rates. Extend early stopping patience.
Train longer:
Check whether training loss is still decreasing. If so, the model can still learn. Tune the learning rate; too high causes oscillation, too low makes learning painfully slow.
Use boosting:
XGBoost, LightGBM, and CatBoost sequentially add weak learners that address shortcomings of previous models, iteratively reducing bias.
If underfitting persists after adding capacity, the problem is likely missing features rather than model architecture.
Choosing your next step
You've diagnosed the problem. Here's the decision tree:
High training error, high validation error (underfitting):
Your model is too simple or lacks the right features. Add capacity first. If that doesn't help, engineer better features.
Low training error, high validation error (overfitting):
Your model memorized noise. Add regularization first. If that doesn't help, try early stopping, then data augmentation.
High variance across cross-validation folds (overfitting):
The model is sensitive to which data it sees. Strengthen regularization or use ensembles to reduce variance.
Consistent poor performance across folds (underfitting):
The model fundamentally can't capture the pattern. Increase complexity or improve features.
Iterating faster on model evaluation
The diagnostic process works best when you can iterate quickly. Generating
learning curves
, comparing training and validation convergence, and running k-fold cross-validation all benefit from an environment where you can test hypotheses and share findings without bouncing between tools.
When validation loss starts climbing, spotting that early and pulling in teammates to review prevents wasted compute. Tracking experiments across multiple architectures keeps the team aligned on what's working — everyone sees the same learning curves and can weigh in without recreating analyses from scratch.
Modern deep learning has added interesting wrinkles to this picture.
Research on double descent
shows that massively overparameterized models can sometimes generalize well despite perfectly fitting training data. But for classical ML and most practical applications, the traditional regularization wisdom remains highly relevant.
Getting the model fit right
Overfitting and underfitting are two sides of the same core challenge: matching model capacity to data complexity. Both produce models that fail in production, and neither has a one-size-fits-all fix. Constrain the model when it overfits through regularization and early stopping; expand capacity when it underfits by increasing complexity and improving features.
The iteration matters as much as the techniques. Tracking which regularization strength worked, comparing dropout rates across experiments, and coordinating with teammates on architecture decisions all get easier when your analysis environment isn't fighting you. Hex gives data scientists a
notebook environment
with built-in version control and collaboration, so every experiment is tracked and the work that matters can be published as an
interactive app
for stakeholders who need results, not code.
Sign up for Hex
to iterate on ML models collaboratively, or
request a demo
to see how it works in practice.
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
