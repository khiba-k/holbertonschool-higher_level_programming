#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = conn.cursor()
    query = """
        SELECT *
        FROM states
        WHERE states.name LIKE BINARY '{}'
        ORDER BY states.id ASC""".format(argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print("({}, '{}')".format(row))
    cur.close()
    conn.close()
