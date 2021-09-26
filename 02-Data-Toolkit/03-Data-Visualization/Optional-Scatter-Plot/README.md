# Scatter plots
### Introduction

Same principle in this exercise, we are going to **recreate** plots from this [article](https://www.data-to-viz.com/caveat/overplotting.html).

To go further and learn more best practices you can read theses **4 articles**.

[Scatter plots](https://www.data-to-viz.com/graph/scatter.html),
[2D density](https://www.data-to-viz.com/graph/density2d.html)

[Simpson Paradox](https://www.data-to-viz.com/caveat/simpson.html),
[The issue with 3D](https://www.data-to-viz.com/caveat/3d.html)

### Dataset

You will work with the dataset `data/blobs.csv`, located in this exercise folder.

### First steps

Create a notebook named `exercise06.ipynb` in the **same folder** as this **README**.
Now you can **import** the necessesary **libraries**.

```python
import numpy as np
import pandas as pd
import matplotlib
%matplotlib inline
import seaborn as sns
```

Then **import** the **dataset** from the CSV you just downloaded.

### Size and transparency

Increase the **lisibility** of your scatter plot with **smaller dot** and a **lower opacity**.
Create a plot with **both** techniques used at the same time.

<img src="https://i.ibb.co/VVby1Pb/visualize-1255x420.png" width="760">

### Groupes

Recreate this plot and use the `hue` option in seaborn scatter plot to **group by category**.
<img src="https://i.ibb.co/sJ1BZBj/Screen-Shot-2019-10-15-at-20-34-12.png" width="360">

### Faceting and group highlight

Create a **grid** of scatter plot, each group **highlighted**.
<img src="https://i.ibb.co/0Vyr6Nc/Screen-Shot-2019-10-15-at-20-34-17.png" width="760">

### Optional - 3D Plot

Recreate this 3D plot with **Plotly**. Use this documentation page: [https://plot.ly/python/3d-surface-plots/](https://plot.ly/python/3d-surface-plots/)

The difficulty here will be to convert our **scatter plot** to a **density matrix** that will be used by **Plotly**.

Only do this exercise if you are done with the map exercise.
<img src="https://i.ibb.co/2nYn883/Screen-Shot-2019-10-15-at-22-21-50.png" width="760">
