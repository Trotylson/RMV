import sqlite3
from datetime import date

conn = sqlite3.connect('rmv.db')
c = conn.cursor()

def createOrDrop(order):
    if order == 'insert':
        c.execute('''CREATE TABLE IF NOT EXISTS rmvResults(Date TIMESTAMP, RMV REAL)''')
    elif order == 'drop': 
        c.execute("DROP TABLE rmvResults")

def insertTo(Rmv):
    insertQuery = """INSERT INTO rmvResults VALUES(?,?)"""
    c.execute(insertQuery, (date.today(), Rmv))
    conn.commit()

def closeDb():
    conn.close()

def showDatabase():
    for row in c.execute('SELECT * FROM rmvResults'):
        print (row)
