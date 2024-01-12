#!/usr/bin/python3
""" script that lists all states from database: hbtn_0e_0_usa"""

import MySQLdb
import sys

from sys import argv
"retrieves mySQL usernme,passwrd &database from commndline"

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    connection = MySQLdb.connect(
            user=mysql_username,
            passwd=mysql_password,
            database=database_name,
            host='localhost',
            port=3306
    )
    cursor = connection.cursor()
    cursor.execute("""
        SELECT states.id, states.name
        FROM states
        WHERE name LIKE 'N%'
        ORDER BY states.id ASC;
        """)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()
