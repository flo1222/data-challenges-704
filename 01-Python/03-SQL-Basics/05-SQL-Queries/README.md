## Background & Objectives

Now it's time for something more complex. We'll be using `JOIN` queries to read data from multiple tables. To acquire instant Jedi skills in `JOIN` queries, [read this](http://stackoverflow.com/questions/17946221/sql-join-and-different-types-of-joins) - the picture is really helpful.
## Specs

Complete the code in `sql_queries.py`. Each method takes a `db` argument, which is a Cursor Object
on which you can call the `execute` method. Exactly like in the previous exercise.

### Detailed Tracks

- Implement `detailed_movies` to get all the movies title with the corresponding director name and genre name.
- Your output should be a list of tuples. **Hint:** you will have to use one `JOIN` sql statement.

This method should return a list of movies. Each element of this list would be a tuple: first element being the movies title, second element the movie's genre name, third element the movie director name.

### Statistics

For each genre of movie, find the stats, i.e. the number of movies and the average movie length (in minutes).

The method should return a dictionary of statistics:

```python
results = stats_on(db, "Action,Adventure,Comedy")
print(results)
=> {
    'genre': 'Action,Adventure,Comedy',
    'number_of_movies': 153,
    'avg_length': 100.98
}
```

### Top 5

Find the top 5 directors that made the most movies in a given genre. This method should return a list of tuples with the director name and the number of movies of the given genre for each director.

```python
results = top_five_artists(db, "Action,Adventure,Comedy")
print(type(results[0]))
=> [
    ('Robert Rodriguez', 5),
    ('Jonathan Frakes', 4),
    ('Anthony C. Ferrante', 3),
    ('Barry Sonnenfeld', 3),
    ('Jackie Chan', 3)
]
```
