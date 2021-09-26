## Objectives of the week

We will analyze a dataset provided by an e-commerce marketplace called [Olist](https://www.olist.com) to answer the CEO's question:

> How to increase customer satisfaction (so as to increase profit margin) while maintaining a healthy order volume?

## About Olist 🇧🇷

<img src="https://raw.githubusercontent.com/lewagon/data-images/master/best-practices/olist.png" width="500"/>

Olist is a leading e-commerce service that connects merchants to main marketplaces in Brazil. They provide a wide range of offers from inventory management, dealing with reviews and customer contacts to logistic services.

Olist charges sellers a monthly fee. This fee is progressive with the volume of orders.

Here are the seller and customer workflows:

**Seller:**

- Seller joins Olist
- Seller upload products catalogue
- Seller gets notified when a product is sold
- Seller hands over an item to the logistic carrier

👉 Note that multiple sellers can be involved in one customer order!

**Customer:**

- Browses products on marketplaces
- Purchases products from Olist.store
- Gets an expected date for delivery
- Customer receives the order
- Customer leaves a review about the order

👉 A review can be left as soon as the order is sent, meaning that a customer can leave a review for a product he did not receive yet!

## Dataset

The dataset consists of 100k orders from 2016 and 2018 that were made on Olist store, available as csv on [Kaggle](https://www.kaggle.com/olistbr/brazilian-ecommerce)

✅ Download the 9 datasets and store them in your `~/code/<user.github_nickname>/data-challenges/04-Decision-Science/data/csv` folder.

## Setup

### 1 - Project Structure
Go to your local `04-Decision-Science` folder.
This will be your project structure for the week.

```bash
.
├── 01-Project-Setup             # your notebooks & analyses, day-by-day
├── 02-Statistical-Inference
├── 03-Linear-Regression
├── 04-Logistic-Regression
├── 05-Communicate
|
├── data                        # Your data source (git ignored)
|   ├── csv
|   |   ├── olist_customers_dataset.csv
|   |   └── olist_orders_dataset.csv
|   |   └── ...
|   ├── README.md   # database documentation
|
├── olist                       # Your data-processing logic
|   ├── data.py
|   ├── product.py
|   ├── seller.py
|   ├── utils.py
|   └── __init__.py.   # turns your folder into a "package"
```

### 2 - Edit the `PYTHONPATH`

Add `olist` path to your `PYTHONPATH`.

This will allow you to easily import modules defined in `olist` in your notebooks throughout the week.

**For macOS, Linux and Windows WSL2:**

Open your terminal and navigate to your home directory by running:

```bash
cd
```

Now you'll need to open your `.zshrc` file. As you might have noticed the file starts with a dot which means it's a hidden file. To be able to see this file in your terminal you'll need to run the command below:

```bash
ls -a
```

the flag `-a` will allow you to see hidden files. You can open the file using either `vim` or sublime text or any other text editor

```bash
# with vim
vim .zshrc

# sublime text
st .zshrc
```

Now in your terminal run:
```bash
cd ~/code/<user.github_nickname>/data-challenges/04-Decision-Science && echo "export PYTHONPATH=\"$(pwd):\$PYTHONPATH\""
```

👉 Copy the output line at the bottom of your `~/.zshrc` file.

⚠️ Restart all your terminal windows to take into account this change.

**For Windows without WSL2:**

Open a Git Bash terminal and run:
```bash
cd ~/code/<user.github_nickname>/data-challenges/04-Decision-Science && explorer.exe .
```
This will open the folder in Windows file explorer.
Click in the folder tree bar:
<img src="https://raw.githubusercontent.com/lewagon/data-images/master/decision-science/pythonpath.jpg" width="500"/>

This will highlight the path to that folder, copy it.

Click on `Control Panel → System and Security → System > Advanced system settings → Environment Variables`

Under System variables, click on **New**
    Variable name: `PYTHONPATH`
    Variable value: the path you copied above

It should look like this:
<img src="https://raw.githubusercontent.com/lewagon/data-images/master/decision-science/pythonpath_var.jpg" width="500"/>

Click on **OK**
Restart your Git Bash terminal.

### 🔥 Check your setup

Go to your `01-Project-Setup` folder and run an `ipython` session:

```bash
cd ~/code/<user.github_nickname>/data-challenges/04-Decision-Science/01-Project-Setup
ipython
```

Then type the following to check that the setup phase from the previous exercise worked:

```python
from olist.data import Olist
Olist().ping()
# => pong
```

If you get something else than `pong`, raise a ticket to get some help from a TA. You might have a problem with the `$PYTHONPATH`.
