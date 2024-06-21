#!/usr/bin/python3
"""
This module lists all states with name
starting with N from database hbtn_0e_0_usa.
"""
import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    query = """
    SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    """
    cursor.execute(query, (state_name,))
    result = cursor.fetchone()[0]
    if result is not None:
        print(result)
    else:
        print("")
    cursor.close()
    db.close()
