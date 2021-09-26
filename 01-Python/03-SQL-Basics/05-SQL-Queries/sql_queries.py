# pylint: disable=C0103, missing-docstring
"""module docstring"""

def detailed_movies(db):
    """return the list of movies with their genre and director."""
    request = """
        select title, genres, directors.name from movies Join directors where movies.director_id = directors.id
    """
    # execute your SQL request
    results = db.execute(request)
    # cursor.fetchall() fetches all the rows of a query result.
    # It returns all the rows as a list of tuples
    results = results.fetchall()
    return results

def stats_on(db, genre_name):
    """For the given genre of movie, return the number of movies and the average
     movie length in minutes (as a stats hash)."""
    request = "select genres, count(*), avg(minutes) from movies where genres = ?"
    t = (genre_name,)
    results = db.execute(request, t)
    # cursor.fetchall() fetches all the rows of a query result.
    # It returns all the rows as a list of tuples
    stat = results.fetchone()
    result = {
            "genre": stat[0],
            "number_of_movies": stat[1],
            "avg_length": round(stat[2], 2)
        }
    print(result)
    return result

def top_five_artists(db, genre_name):
    """return list of top 5 directors with the most movies for a given genre."""
    request = """
        select directors.name, count(*)
        from movies 
        join directors on movies.director_id = directors.id
        where movies.genres = ?
        group by directors.name
        order by count(*) desc, name asc
        limit 5
    """
    t = (genre_name,)
    results = db.execute(request, t)
    top = results.fetchall()
    print(top)
    return top
