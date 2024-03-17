#!/usr/bin/python3
"""
Lists all states from the database
Takes as arguments: mysql username, mysql password, database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # database connection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # Execute queries with SQL
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
