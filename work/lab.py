# test web
from flask import Flask, request
from flask import render_template
import pymysql

conn = pymysql.connect(host="cc104.mysql.local", user="root",password="iii",charset="utf8")


# database
# new database
cur = conn.cursor()
try:
    cur.execute('''CREATE DATABASE lab2;''')
except:
    print ("database exists")
cur.close()


# new table
connlab = pymysql.connect(user="root", host="cc104.mysql.local", passwd="iii", db="lab2",  charset="utf8")
cur = connlab.cursor()
try:
    cur.execute('''CREATE TABLE name (
                        id integer UNSIGNED AUTO_INCREMENT,
                        name varchar(20),
                        PRIMARY KEY(id)
                    )DEFAULT CHARSET=utf8;
                ''')
except:
    print ("table exists")
cur.close()

# add data
def add_data(add):
    # add data
    cur = connlab.cursor()
    sql = '''INSERT INTO name (name) VALUES (%s);''' 
    data = (repr(add))
    cur.execute(sql % data)
    conn.commit()
    cur.close()

# show data
def showdata():
    cur2 = connlab.cursor()
    cur2.execute('''select * from name;''')
    return str(cur2.fetchall())
    cur2.close()



# web
app = Flask(__name__)

#網頁執行/say_hello時，會導至index.html
@app.route('/say_hello',methods=['GET'])
def getdata():
    return render_template('index.html')

#index.html按下submit時，會取得前端傳來的username，並回傳"Hello! "+name
@app.route('/say_hello',methods=['POST'])
def submit():
    if request.form['aaa'] == "Submit":
        name = request.form.get('username') 
        add_data(name)
        return render_template('index2.html',user_template=name )
    elif request.form['aaa'] == "return" :
        return render_template('index.html')
    elif request.form['aaa'] == "database" :
        ans = showdata()
        return render_template('index3.html',user_template=ans )
    
    

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')