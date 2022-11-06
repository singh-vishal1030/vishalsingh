import pymysql as p


def connect():
    return p.connect(host="localhost",user="root",password="",database="Author",port=3306)


def postinsert(p):
    con=connect()
    cur=con.cursor()
    sql="insert into post values (%s,%s,%s,%s)"
    cur.execute(sql,p)
    con.commit()
    con.close()








