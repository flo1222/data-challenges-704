# Box and Violin
### Introduction

Same principle in this exercise, we are going to **recreate** plots from this [article](https://www.data-to-viz.com/story/OneNumSevCatSubgroupSevObsPerGroup.html).

To learn more **best practices** around Box or Violin plot read these **2 short articles**.

[Box-Plot](https://www.data-to-viz.com/caveat/boxplot.html), [Violin_plot](https://en.wikipedia.org/wiki/Violin_plot)


### Dataset

You will work with the **tips** dataset.

[Download here](https://raw.githubusercontent.com/holtzy/data_to_viz/master/Example_dataset/10_OneNumSevCatSubgroupsSevObs.csv)

### First steps

Create a notebook named `exercise02.ipynb` in the **same folder** as this **README**.
Now you can **import** the necessesary **libraries**.

```python
import numpy as np
import pandas as pd
import matplotlib
%matplotlib inline
import seaborn as sns
```

Then **import** the **dataset** from the CSV you just downloaded.

### Grouped box plot

Start by recreating this plot from the article.
Make sure your plot use the **tip percentage %** on the **Y axis**.
Your plot should present individual data points using **swarmplot**.

It's ok if your plot has different **aesthetics**, this will also be true for the **next exercises of the day**.
<img src="https://www.data-to-viz.com/story/OneNumSevCatSubgroupSevObsPerGroup_files/figure-html/unnamed-chunk-3-1.png" width="760">

### Violin plot

We will recreate the following plot.

<img src="https://www.data-to-viz.com/story/OneNumSevCatSubgroupSevObsPerGroup_files/figure-html/unnamed-chunk-4-1.png" width="760">

Use seaborn violin plot option `split`, to have a violin with, on one side the **female** distribution and on the other side the **male** distribution.

Make sure you have the right **legend**, male and female.

**Example:**

<img src="https://seaborn.pydata.org/_images/seaborn-violinplot-4.png" width="360">
