import pymysql

mypass = "myPassword"
mydatabase="db"

con = pymysql.connect(host="localhost",user="myUser",password=mypass,database=mydatabase)
cur = con.cursor()