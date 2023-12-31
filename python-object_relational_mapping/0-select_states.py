#!/usr/bin/python3
''' Script for connect to a database '''
import sys
import MySQLdb


if __name__ == "__main__":
    
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cur.fetchall()]
    cur.close()
    db.close()
