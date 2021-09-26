## Background & Objectives

Now it is time to use python to interact with the `movies` database. For that we will use a library that comes with Python, called **sqlite3**.

The goal of this challenge is to talk to the database **from our Python code**.

## Specs

👉 **IMPORTANT**: Each method takes a `db` argument, which is a connection to the database, on which you can call the `execute` method. This `db` is **built by the test and passed along to the function**. No need to create one yourself to satisfy `make`. Your method will look like this:

```python
def the_method(db):
    results = db.execute("YOUR SQL QUERY")
    results = results.fetchall()
    # results in a list (rows) of list (columns)
    print(results)  # Inspect what you get back! Don't guess!

    # Then you'll need to return something.
    return ?
```

👉 To try your code in **IPython** or in the `queries.py` file, you will need to build `db` yourself.

```python
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')
db = conn.cursor()
rows = db.execute("SELECT * FROM movies LIMIT 3")
rows.fetchall()
# => [('A Trip to the Moon', 13), ('The Great Train Robbery', 11), ('The Birth of a Nation', 195)]
```

Open the file `queries.py` to answer the following questions. Don't forget you can look inside the database by running `sqlite3 data/movies.sqlite` in the Terminal or use DBeaver.

There are five methods to implement:

- How many rows does the `directors` table contain?
- Return the list of all the directors and sort them by name (alphabetically). **Hint:** use the `ORDER BY` SQL filter.
- Find all the movie title that contain "love" **anywhere** in their name, sorted alphabetically. **Hint:** use the `WHERE` and `LIKE` SQL keywords. (bonus question: How could you make sure it's a romance movie ?)
- Count how many directors have a given word in their name. **Hint:** make sure you protect your SQL query from **SQL injection** with [parameter substitution](https://docs.python.org/3.7/library/sqlite3.html)
- Return all the movies that are longer than a given duration and sort them. **Hint:** you can use the comparison operator `>` in SQL.

## Tips

SQL queries tend to get pretty long, especially when you start using `WHERE` or `JOIN`. In Python,
you can use the [triple-quote](https://docs.python.org/3.2/tutorial/introduction.html#strings) syntax to write **multi-line** strings:

```python
# Find the first 3 artists with the letter `Z` in their name.
query = '''
    SELECT * FROM movies
    WHERE title LIKE "%Z%"
    ORDER BY title
    LIMIT 3
'''
rows = db.execute(query)
```

## Tools

- [DBeaver](https://dbeaver.io/)
