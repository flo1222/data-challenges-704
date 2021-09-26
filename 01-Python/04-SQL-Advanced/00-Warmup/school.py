# pylint:disable=C0111,C0103

def students_from_city(db, city):
    """return a list of students for a specific birth city"""
    request = '''
        select * 
        from students s
        where s.birth_city = ?
    '''
    # Use ? in your SQL query to inject the city parameter
    db.execute(request, (city,))
    results = db.fetchall()
    return results

# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
#   $ python school.py
# import sqlite3
# conn = sqlite3.connect('db/school.sqlite')
# db = conn.cursor()
# print(students_from_city(db, 'Paris'))
