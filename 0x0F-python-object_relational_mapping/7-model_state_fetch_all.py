#!/usr/bin/python3
"""
script that lists all State objects from database:hbtn_0e_6_usa
"""

import sys
import MySQLdb
from sys import argv
from model_state import Base, State

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
            ORDER BY states.id ASC;
            """)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    connection.close()
