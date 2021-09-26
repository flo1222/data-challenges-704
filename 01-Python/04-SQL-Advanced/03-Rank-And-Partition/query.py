# pylint:disable=C0111,C0103

def movie_duration_buckets(db):
    request = '''
            select  
                cast(round((m.minutes/30+1)*30,0) as int) as bucket,
                count(*) as count
            from movies m 
            group by bucket
        '''
    db.execute(request)
    results = db.fetchall()
    return results[1:]

def longest_movies_by_director(db, first_letter):
    request = '''
            select 
                m.title,
                d.name,
                m.minutes,
                RANK() OVER (
                    PARTITION BY m.director_id 
                    ORDER BY m.minutes desc 
                ) AS order_rank
            from movies m 
            join directors d on m.director_id = d.id 
            where d.name like ?
            order by d.name 
        '''
    letter = f'{first_letter}%'
    print(letter)
    db.execute(request,(letter,))
    results = db.fetchall()
    return results


def top_3_longest(db, first_letter):
    request = '''
            select *
            from
                (select 
                    m.title,
                    d.name,
                    m.minutes,
                    RANK() OVER (
                        PARTITION BY m.director_id 
                        ORDER BY m.minutes desc 
                    ) AS m_rank
                from movies m 
                join directors d on m.director_id = d.id 
                where d.name like ?
                order by d.name 
                )
            where m_rank < 4
        '''
    letter = f'{first_letter}%'
    print(letter)
    db.execute(request,(letter,))
    results = db.fetchall()
    return results

# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
#   $ python school.py
# import sqlite3
# conn = sqlite3.connect('db/movies.sqlite')
# db = conn.cursor()
# print(top_3_longest(db, "X"))
