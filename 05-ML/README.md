## ML Fundamentals, dataset preparation

First, you’ll learn what we mean by machine learning and what are the fundamental steps in the implementation and deployment cycle of machine learning algorithms.

This module is mostly dedicated to the preprocessing of your dataset - how to have a clean, balanced dataset that is representative of your problem. You’ll discover how to encode your data into vectorized forms that can be used later in your models.

You’ll also discover your first versatile model family - the k-nearest neighbors.

In the end you’ll have a global overview as to what the data scientist job entails in the modeling part, and how to do your feature engineering.

## ML fundamentals

In this module, you’ll discover the two sets of tasks that you’ll have to tackle as a data scientist - regression and classification tasks.

In that context, you will begin to have a first overview as to how to make a choice between the different algorithms that you have at your disposal and the differences between regular programming and machine learning programming.

We’ll discover the split between training and testing phase of the lifecycle of a model and how to use the scikit-learn library to help us with the implementation of all the steps aforementionned.

We’ll also work with the two new fundamental model families - the linear regression and logistic regression.

## Generalisation & Overfitting

This module is dedicated to very important concepts that are the bread and butter of a datascientist modeling daily work.

We want our models to be able to generalise on unseen data flawlessly, and we’ll need specific techniques that will allow us to not overfit and validate performance of our model. On this day specifically we will see what it means to split your dataset between training and testing set.

With those new techniques, we will be able to understand more deeply how to robustly train our models and make sure they’ll be ready to be deployed in production with predictable accuracy.

We’ll discover again another model to add in our toolbelt, the Naive Bayes algorithm, which is very useful under a set of hypothesis.

## Under the hood

Now that we have discovered how machine learning works, how to generalise and not overfit, as well as a few model families that we can use with ease, we need to get a bit more technical.

This module is dedicated to the understanding of how the learning mechanism works. We will go along the iterative optimisation procedure like gradient descent variants, targeting a designed loss function of our choice. For regressions, we’ll study mean squared error, mean absolute error and huber loss. For classifications we’ll mostly see cross entropy & hinge loss.

Understanding how we manage to minimize that loss, how to choose the right loss and all those type of considerations will help us manage better our models and design with more control our algorithms in order to have the best performance possible, for the suited problem we want to solve.

One last trick to add up our sleeve will be to use regularisation methods, which we will cover in detail for our specific use cases.

## Performance metrics

The final module of this week concludes the discovery of fundamental concepts of machine learning. We will see here how to evaluate the performance of our models precisely, and how to manage to choose the right error metric.

In an applied setting, knowing to what to optimise is actually paramount to cover correctly business use case and evaluate feasibility and utility of the use of machine learning technologies. Metrics like precision, recall & f1 score, are very important to use in order to determine business impact.

Next, we will go one step further in the training process by discovering validation methods such as cross validation as well as the tuning of hyperparameters using validation sets.

Finally we will see another powerful supervised learning method called SVM (Support Vector Machines) which is one of the go-to baseline for a large class of tasks.

## Unsupervised learning

This first day of the week covers a family of methods that we haven’t used yet, unsupervised learning methods. We will cover algorithms that are used all the time for exploratory analysis, dimensionality reduction and other compression-type tasks.

Mostly, we’ll see the Principal Component Analysis type of methods that will help us in a linear context and the k-means type of clustering methods that will help us when we will want to discover groups of data without supervision.

This will also be an opportunity to discover big machine learning applications through building a recommender system and an image compression program.

## Ensemble methods

Here we get the final family of methods to complete your toolbelt of models. Ensemble methods are the super power of a data scientist : it allows to combine weak models into a powerful one, without requiring much more computational power!

Those methods that we will discover such as random forest or gradient boosting, are the ones that usually get the best performance from the get go, and are at the top of Kaggle-type competitions. So if you need very good accuracy and performance fast, this will be the day


## Workflow

This module is dedicated to your workflow. Now that we have all the fundamental models, we can safely go back to what it means to build a model from start to finish, with all the common difficulties and challenges that a data scientist will encounter - building baselines, robust feature engineering and all around efficient workflow.

Also we will work now with pipelines, which are powerful tools when you work in real use case that allow you to train and deploy easily end-to-end procedures from start to finish without losing the performance in sight.

## Vision

For this module, we will only focus on one type of data that data scientist encounter quite often : image data. Image observations are a specific type of input that we have to learn how to tackle efficiently. One set of techniques being preprocessing techniques such as normalization, standardization and whitening. More broadly speaking, it entails being comfortable managing high-dimensional variables, and transforming them into manageable input.

We will also tackle secondary question linked to training machine learning models for vision tasks such as convolutions and kernels, rehasping and data augmentation.


## NLP

This full day is dedicated to the main type of data a datascientist usually encounters in practice : unstructured text data. The dedicated field is called NLP (Natural Langage Processing) and this is where we will learn to preprocess our text and learn the right type of encodings for the tasks we want to be able to train for. It mostly has to deal with frequencies or tf-idf of n-grams, bag-of-word type representations, normalization, lemmatization, stemmatization of the words and other type of manipulations that will help us further down the line.

We will also tackle word embeddings and document clustering through LDA, which will help us also explore and understand our dataset when confronted to a corpus of unstructured text documents.
