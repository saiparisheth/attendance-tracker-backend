from flask import jsonify
import sqlite3
data={"name":"sai","rollno":"69","apply":"leave","nofhours":"3","startdate":"55","enddate":"66","reason":"summa"}
def organize(data):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()


    #cursor.execute("""Create table form (id text, name text)""")
    #cursor.execute("""Create table form (data text)""")
    #cursor.execute("""INSERT INTO form VALUES (? , ?)""", (data['id'], data['name']))
    cursor.execute('INSERT INTO form VALUES ("{}")'.format(data))
    #cursor.execute("SELECT * FROM form ")
    #print(cursor.fetchall())

    conn.commit()
    conn.close()

def givedata():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()


    #cursor.execute("""Create table form (id text, name text)""")
    #cursor.execute("""INSERT INTO form VALUES (? , ?)""", (data['id'], data['name']))
    cursor.execute("SELECT * FROM form ")
    formvalues=cursor.fetchall()
    conn.commit()
    conn.close()
    return [i[0] for i in formvalues]


conn = sqlite3.connect('data.db')
cursor = conn.cursor()
#cursor.execute("""Create table form (data text)""")
#cursor.execute('INSERT INTO form VALUES ("{}")'.format(data))
conn.commit()
conn.close()
