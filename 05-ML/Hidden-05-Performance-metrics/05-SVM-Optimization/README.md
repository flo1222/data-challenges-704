Now that you know the most important parameters of an SVM (Kernel, Gamma, C), you need to find out which combination optimizes your model.

Good news, you don't have to grid search each combination one after the other. GridSearchCV does it for you. You just need to combine all parameters within one dictionary.