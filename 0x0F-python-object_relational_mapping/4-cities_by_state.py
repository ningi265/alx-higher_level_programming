#!/usr/bin/python3
"""  a script that lists all cities from the database hbtn_0e_4_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
             port=3306,
             host="localhost",
             user=sys.argv[1],
             passwd=sys.argv[2],
             db=sys.argv[3]
             )
    cur = db.cursor()
    query = "select cities.id, cities.name, states.name from\
    cities inner join states on cities.state_id = states.id"
    cur.execute(query)
    query_row = cur.fetchall()
    for row in query_row:
        print(row)
