In this exercise, we will dive into the whole machine learning development workflow. A common mistake (and we made it intentionnaly during the previous days) is to learn the parameters of a prediction function and testing it on the same data. What's wrong with that? We can’t fit the model to our training data and hope it would accurately work for the real data it has never seen before.

To avoid that to happen, there are several techniques: we could remove a part of the training data and using it to get predictions from the model trained on rest of the data (= __Holdout Method__). But, by reducing the training data, we risk losing patterns in data set and increase the error. __K-Fold cross validation__ will help us to solve this problem.

In K Fold cross validation, we  split our data into k separated "folds". Then, the Holdout Method is repeated k times, such as each time, one of the k folds will be the test subset and the (k-1) other folds will be used together as the training set.

__Note__ that this method does not depend on the model. In this example, we will use it on a Linear Regression but you could use it on any methods you want (KNN, Logistic Regression,...).

This following image schematize this algorithm.
<img src="https://scikit-learn.org/stable/_images/grid_search_cross_validation.png" style="width:50%;">

The general workflow to apply the Cross Validation is always the same:
1. Instanciate the model from scikit-learn you want to use (LinearRegression for the today exercise);
2. Instanciate the KFold class with the parameters you want;
3. Use the cross_val_score() function to measure the performance of your model.