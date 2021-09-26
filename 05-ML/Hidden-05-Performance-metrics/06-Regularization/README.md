In this exercise, you will use polynomial regression and see the effect of regularization. You will use polynomial regression. It is exactly like linear regression, but with new features created as polynomials of the original feature. For instance, if your dataset looks like this:

```python
array([[3],
       [2],
       [2],
       [6]])
```
You can create a new feature which is just, for instance, the data raised at the power of two:

```python
array([[ 3,  9],
       [ 2,  4],
       [ 2,  4],
       [ 6, 36]])
```

These new features will interpreted as if they were independent. Then, you can use the linear regression algorithm as usual.


Here, we use polynomial regression to illustrate a case of overfitting. Add polynomials to your dataset is like adding new features, and adding new features is prone to overfitting. For this reason, the regularization technics that you will use here can be applied when you encounter overfitting in a real dataset.

Let's start by opening the notebook `06-Regularization.ipynb`.
