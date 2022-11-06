import pymysql as p


def connect():
    return p.connect(host="localhost",user="root",password="",database="Author",port=3306)

def userinsert(u):
    con=connect()
    cur=con.cursor()
    sql="insert into user values (%s,%s,%s,%s)"
    cur.execute(sql,u)
    con.commit()
    con.close()

def checkuser(email):
    con=connect()
    cur=con.cursor()
    sql="select Email_id,Password from user where Email_id=%s"
    cur.execute(sql,email)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data   