# pylint: disable=C0103
"""Module docstring"""

def directors_count(db):
    ''' Function that uses 'db' to execute an SQL query against the database.
    Return directors count in database.'''
    rows = db.execute("select count(*) from directors")
    count = rows.fetchone()[0]
    return count


def sorted_directors(db):
    ''' Function that returns a list of directors' names sorted alphabetically '''
    rows = db.execute("select name from directors order by name asc")
    names = rows.fetchall()
    directors_list = []
    for name in names:
        directors_list.append(name[0])
    return directors_list


def love_movies(db):
    ''' TO-DO: return a list of movies with love in the title, sorted
    alphabetically '''
    rows = db.execute("select title from movies where title LIKE '%love%' order by title asc")
    titles = rows.fetchall()
    movie_list = []
    for title in titles:
        movie_list.append(title[0])
    return movie_list


def directors_with_name(db, name):
    ''' TO-DO: count number of director with this name '''
    t = (f'%{name}%',)
    rows = db.execute("select count(*) from directors where name LIKE ?", t)
    count = rows.fetchone()[0]
    print(count)
    return count
# directors_with_name(db, "Tarantino")

def long_movies(db, min_length):
    ''' Functions that returns a list of movie titles
    verifying: minutes > min_length, sorted by length (ascending)'''
    t = (min_length,)
    query = "select title from movies where minutes > ?  order by minutes asc"
    rows = db.execute(query, t)
    titles = rows.fetchall()
    movie_list = []
    for title in titles:
        movie_list.append(title[0])
    print(movie_list)
    return movie_list
