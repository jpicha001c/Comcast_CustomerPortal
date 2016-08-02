from flask import Flask
from flask import request
from new_json import reddit_check
from flaskext.mysql import MySQL
from BeautifulSoup import BeautifulSoup
import urllib2
import re
import time
import MySQLdb
app = Flask(__name__)
'''
mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'cx_login'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
#print mysql.connect()
'''
conn = MySQLdb.connect(user="root", passwd="", db="cx_login")

@app.route("/")
def hello():
    return "Welcome to Python Flask App!"

#@app.route("/Authenticate",methods=['GET'])
@app.route("/Authenticate",methods=["GET","POST"])
def Authenticate():
    username = request.args.get('UserName')
    print "---username--",username
    password = request.args.get('Password')
    print "---Pass--",password
    #conn = MySQLdb.connect(user="root", passwd="", db="cx_login")
    cur = conn.cursor()
    #cur.execute("SELECT * FROM cx_user")
    cur.execute("SELECT * from cx_user where userName='" + username + "' and password='" + password + "'")
    data = cur.fetchone()
    print "---",data
    if data is None:
     return "Username or Password is wrong"
    else:
        print "Login successful calling reddit API ..."
        reddit_check()
        return "Logged in successfully"







    cur.close()
    conn.close()


if __name__ == "__main__":
    app.run()