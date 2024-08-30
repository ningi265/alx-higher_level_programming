#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
             host="localhost",
             port=3306,
             user=sys.argv[1],
             passwd=sys.argv[2],
             db=sys.argv[3]
             )
    arg = sys.argv[4]
    cur = db.cursor()
    query = "SELECT * FROM cities as c\
             INNER JOIN states as s\
             ON c.state_id=s.id\
             ORDER BY c.id"
    cur.execute(query)
    query_row = cur.fetchall()
    print(", ".join([row[2] for row in query_row if row[4] == arg]))
    cur.close()
    db.close()
