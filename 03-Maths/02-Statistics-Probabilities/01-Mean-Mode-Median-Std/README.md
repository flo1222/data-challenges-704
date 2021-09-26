## Background

In this challenge, we will learn the concepts of Mean, Mode, Median and Standard Deviation. In the file `basic_functions.py` there are four functions to implement. Each one of those functions will implement one of the aforementioned concepts.

## The Mean and Variance
The sample **mean** (mu) is the average and is computed as the sum of all the observed outcomes from the sample divided by the total number of events. Here's the formula:

$\mu = \frac{1}{N}\sum_{i=0}^{N}x_i$

The **standard deviation** (sigma) on the other hand is a statistical metric that describes the spread of the data, or how far the values are from the mean. Here's the formula:

$\sigma = \sqrt{\frac{\sum_{i=0}^N(x_i - \mu)^2}{N - 1}}$

Thanks to these definitions, implement the functions `my_mean(samples)` and `my_standard_deviation(samples)` in the file `basic_functions.py`. These functions take a list as parameters and return the mean and the standard deviation respectively.

## The Median

The median is the value separating the higher half from the lower half of a data sample (a population or a probability distribution). For a dataset, it may be interpreted as the **"middle" value**. For example, in the dataset `{1, 3, 3, 6, 7, 8, 9}`, the median is 6, the fourth largest, and also the fourth smallest, number in the sample. Note that the values in the sample are ordered.

One problem when using the mean, is that it often does not depict the typical outcome. If one element from the sample is very far from the rest of the sample (i.e. also called outliers), then the mean will be affected by this "unusual" data. That's why, in some cases, we use **the Median**.

Read this [wikipedia article](https://en.wikipedia.org/wiki/Median) to see how the **median** is computed.

Implement in the file `basic_functions.py` the function `my_median(samples)`. The function takes a list as a parameter and return the median of the list.

## The Mode

The mode of a set of data values is the value that appears most often. In other words, it is the value that is most likely to be sampled.

Read this [wikipedia article](https://en.wikipedia.org/wiki/Mode_(statistics)) to see how the **mode** is computed.

Implement in the file `basic_functions.py` the function `my_mode(samples)`.
