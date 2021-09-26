We're gonna try to classify emails in a dataset into spams.

The first step will be to **load the emails**, then we're gonna need to **clean** them a bit.
The second step will be to **transform text** features into a representation encoding that the machine can understand.
We will use **TF-IDF encoding** here (term frequency inverse document frequency).
And finally, we're gonna use **Multinomial Naive Bayes** to represent our data.

Click this [link](https://wagon-public-datasets.s3.amazonaws.com/Data-Challenges_ML-Day02-Ex03_emails-dataset.pickle) to download the **spam email dataset**. Then put the file in this **exercise folder**.

To start the exercise open `Exercice-Spam.ipynb` in `jupyter notebook`.
