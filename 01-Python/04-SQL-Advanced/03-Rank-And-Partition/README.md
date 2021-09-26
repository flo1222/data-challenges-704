## Background & Objectives

In this section, we will cover the SQL `PARTITION BY` clause and its difference with `GROUP BY` in a `SELECT` statement.

## Specs

### Bucketing The Movie Duration

First. What is a bucket?

To **'bin'** (or **'bucket'**) the range of values — that is, divide the entire range of values into a series of intervals, and then count how many values fall into each interval. The bins are usually specified as consecutive, non-overlapping intervals of a variable. The bins (intervals) must be adjacent, and are often (but not required to be) of equal size" - https://en.wikipedia.org/wiki/Histogram

👉 Implement `movie_duration_buckets()` to get the buckets of the movie duration of our database!

A bucket contain a **count** of all the movies with a duration in the **range** of the bucket.

For example, the bucket **30** will contain the count of all the movies with a duration between **0 min** and **30 min**.

Or an other way to see it is:
- The value for bucket **30** should be equal to `SELECT COUNT(*) FROM movies WHERE minutes < 30;`

Hint 💡 :

```python
movie_duration_buckets(db)
=> [(30, 292), (60, 764), (90, 1362), [...],(690, 2), (900, 1), (1020, 1)]
```

### Partition By Directors

The SQL `PARTITION BY` clause can be used with the:
- OVER clause: to specify the column on which we need to perform an aggregation
- RANK clause: to have a row number of each row.

In the previous example, we used `GROUP BY` with the Minutes column to bucket our data. Let's switch to a similar scenario with the SQL `PARTITION BY`.

👉 Implement the function `longest_movies_by_director()` to rank the movies of each director by duration.

Each rows returned by the query should look like:

`('Movie Title', 'Director Name', movie_duration (ex: 120), rank (ex:2))`

The **longest movie** by a director should have the **rank 1** and the **shortest** should have the **last rank**.

The results should then be sort by director's name.

Note that the function takes a **second argument**, **first_letter** which should be used in you query to select only the director names starting with the letter provided.

We expect a result like:

```python
longest_movies_by_director(db, "X")
=> [
      ('Of Gods and Men', 'Xavier Beauvois', 122, 1),
      ('Laurence Anyways', 'Xavier Dolan', 168, 1),
      ('Mommy', 'Xavier Dolan', 139, 2),
      ('Tom at the Farm', 'Xavier Dolan', 102, 3),
      [...]
      ('Hitman', 'Xavier Gens', 100, 3)
    ]
```

### Top-3 longest movies

👉 Implement the function `top_3_longest()` to find the top-3 longest movies by director. 👌

Here you will **build on** the request you created in the last exercise in order to **select** only the **first 3 longest movies by director**.

We expect a result like:

```python
longest_movies_by_director(db, "X")
=> [
      ('Of Gods and Men', 'Xavier Beauvois', 122, 1),
      ('Laurence Anyways', 'Xavier Dolan', 168, 1),
      ('Mommy', 'Xavier Dolan', 139, 2),
      ('Tom at the Farm', 'Xavier Dolan', 102, 3),
        [...]
    ]
```

