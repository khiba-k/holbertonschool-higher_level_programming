#!/usr/bin/python3
"""
    Script that lists all states from the database.
"""
import MySQLdb
import sys


def connectDb(user, password, db):
    """
        Get connection with the database.
        Args:
            user (str): Username of the user.
            password (str): Password of the user.
            db (str): Database to retrieve.
        Return:
            Connection database.
    """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=db,
        charset="utf8"
    )
    return conn


if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    conn = connectDb(user, password, db)
    cur = conn.cursor()

    query = f"""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN
            states ON states.id = cities.state_id
        ORDER BY cities.id ASC
    """
    cur.execute(query)

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
