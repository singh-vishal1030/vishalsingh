import pymysql as p


def connect():
    return p.connect(host="localhost",user="root",password="",database="Author",port=3306)


def insert(t):
    con=connect()
    cur=con.cursor()
    sql="insert into author values (%s,%s,%s,%s)"
    cur.execute(sql,t)
    con.commit()
    con.close()


def checkauthor(email):
    con=connect()
    cur=con.cursor()
    sql="select Email_id,Password from author where Email_id=%s"
    cur.execute(sql,email)
    data=cur.fetchall()        
    con.commit()
    con.close()
    return data   

def activeauthor(email):
    con=connect()
    cur=con.cursor()
    delete="DELETE FROM active_author_user"
    cur.execute(delete)
    active_user="insert into active_author_user values (%s)"
    cur.execute(active_user,email)        
    con.commit()
    con.close()

def getactiveauthor():
    con=connect()
    cur=con.cursor()
    sql="select Email_id from active_author_user"
    cur.execute(sql)
    data=cur.fetchall()        
    con.commit()
    con.close()
    return data   
    
