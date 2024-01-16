#!/usr/bin/python3
""" script that takes in the name of a state as an argument
and lists all cities of that state, using the database """
import MySQLdb
import sys

from sys import argv
"retrieves mySQL usernme,passwrd &database from commndline"

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    connection = MySQLdb.connect(
            user=mysql_username,
            passwd=mysql_password,
            database=database_name,
            host='localhost',
            port=3306
    )
    cursor = connection.cursor()
    query = """
        SELECT cities.id, cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC;
    """
    cursor.execute(query, (state_name_searched,))

    results = cursor.fetchall()
    results = [row[1] for row in results]

    print(', '.join(results))

    cursor.close()
    connection.close()
