#!/usr/bin/python3
"""
    script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = BINARY '{}'\
                    ORDER BY id ASC".format(sys.argv[4]))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
