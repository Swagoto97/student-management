import sqlite3


def connect():
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, sname text, gph int(10), doa date, fees integer,lstp month,payd date )")
    conn.commit()
    conn.close()

def insert(sname,gph,doa,fees,lstp,payd):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO student VALUES(NULL,?,?,?,?,?,?)",(sname,gph,doa,fees,lstp,payd))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student")
    row=cur.fetchall()
    conn.close()
    return row
def search(sname="",gph="",doa="",fees="",lstp="",payd=""):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student WHERE sname=? OR gph=? OR doa=? OR fees=? OR lstp=? OR payd=?",(sname,gph,doa,fees,lstp,payd))
    row=cur.fetchall()
    conn.close()
    return row
def delete(id):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    conn.commit()
    conn.close()
def update(id,sname,gph,doa,fees,lstp,payd):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("UPDATE student SET sname=?, gph=?,doa=?, fees=?, lstp=?, payd=? WHERE id=?",(sname,gph,doa,fees,lstp,payd,id))
    conn.commit()
    conn.close()

def search_row(id):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM student WHERE id=?",(id,))
    row=cur.fetchall()
    conn.close()
    return row
     
# print(search(sname="Swagoto Sadhukhan"))
# connect()
# print(type(view()))
