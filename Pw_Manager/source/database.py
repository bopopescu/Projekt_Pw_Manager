import mysql.connector

global mydb
def mysql_connect():
  mydb = mysql.connector.connect(
    host="",
    user="",
    password=""
  )
  return mydb


def create_cursor(mydb):
  mycursor = mydb.cursor()

  return mycursor

def create_database(mycursor, db_name):
 try:
    mycursor.execute("CREATE DATABASE " + db_name)
 except:
    print("Database " + db_name + " exists already")

def create_table(db_name, table_name):
    mydb = mysql.connector.connect(
      host="",
      user="",
      password="",
      database = db_name
    )
    mycursor = create_cursor(mydb)

    try:
      mycursor.execute("CREATE TABLE " + table_name + " (id INT AUTO_INCREMENT PRIMARY KEY, Username VARCHAR(255), Password VARCHAR(255))")
    except:
      print("Table " + table_name + " exists already")

    return mydb

def insert_table(mydb, mycursor, table_name, acc):
    sqlformula = "INSERT INTO " + table_name + " (Username, Password) VALUES (%s, %s)"
    mycursor.execute(sqlformula, acc)
    mydb.commit()

mydb = mysql_connect()
print(mydb)

mycursor = create_cursor(mydb)
db_name = "storage_db"
create_database(mycursor, db_name)
table_name = "accounts"
mydb = create_table(db_name, table_name)
mycursor = create_cursor(mydb)
acc = ("user123", "psw123")
insert_table(mydb, mycursor, table_name, acc)
#


