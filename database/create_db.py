import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()
with open('create_student_table.sql', 'r') as f:
    text = f.read()
cur.executescript(text)
cur.close()
con.close()
