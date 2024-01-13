#!/usr/bin/python3
""" script that takes args and displays all values in states table
of hbtn_0e_0_usa where name matches the arg """

import MySQLdb
import sys

from sys import argv
"importing argv is not relevant since sys is imported"
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
        SELECT states.id, states.name
        FROM states
        WHERE name = %s
        ORDER BY states.id ASC;
        """.format(state_name_searched)
    cursor.execute(query, (state_name_searched,))
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()
