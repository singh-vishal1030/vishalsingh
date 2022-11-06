import pymysql as p


def connect():
    return p.connect(host="localhost",user="root",password="",database="Author",port=3306)


def showdata():
    con=connect()
    cur=con.cursor()
    sql="select * from post"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def showspecificdata(email):
    con=connect()
    cur=con.cursor()
    sql="select * from post where created_by=%s"
    cur.execute(sql,email)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data
