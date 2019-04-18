import pymysql
conn = pymysql.connect(host="cc104.mysql.local", user="root",password="iii",charset="utf8")
connlab = pymysql.connect(user="root", host="cc104.mysql.local", passwd="iii", db="lab",  charset="utf8")
#======================================================
# new database
cur = conn.cursor()
try:
    cur.execute('''CREATE DATABASE lab;''')
except:
    print ("database exists")
cur.close()


# new table
connlab = pymysql.connect(user="root", host="cc104.mysql.local", passwd="iii", db="lab",  charset="utf8")
cur = connlab.cursor()
try:
    cur.execute('''CREATE TABLE name (
                        id integer UNSIGNED AUTO_INCREMENT,
                        name varchar(10),
                        PRIMARY KEY(id)
                    )DEFAULT CHARSET=utf8;
                ''')
except:
    print ("table exists")
cur.close()
#======================================================
def add_data(add):
    cur = connlab.cursor()
    sql = '''INSERT INTO name (name) VALUES (%s);''' 
    data = (repr(add))
    cur.execute(sql % data)
    conn.commit()
    cur.close()

def showdata():
    cur = connlab.cursor()
    cur.execute('''select * from name;''')
    print (cur.fetchall() )
    cur.close()
   
#======================================================
add_data("asd")
showdata()