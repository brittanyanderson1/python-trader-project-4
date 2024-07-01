import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="AbbaDoo1234!",
  database="tendertraderdb"
)

my_cursor = mydb.cursor()

#my_cursor.execute("CREATE DATABASE tendertraderdb")

#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:

#my_cursor.execute("CREATE TABLE users (first_name VARCHAR(255), last_name VARCHAR(255), email VARCHAR(255), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
#my_cursor.execute("SHOW TABLES")
#for table in my_cursor:
#  print(table[0])
  
#userInfo = "INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)"
#userList1 = ("Brittany", "Anderson", "alyciab143@gmail.com")

#my_cursor.execute(userInfo, userList1)
#mydb.commit()

#userInfo = "INSERT INTO users (first_name, last_name, email) VALUES (%s, %s, %s)"
#userList1 = [("Ike", "Rednose", "ikeshine01@gmail.com"),
#("Jessica", "Jones", "jjmoon@hotmail.com"),
#("Merle", "Dixon", "mdixon@walking.com"),
#]
#my_cursor.executemany(userInfo, userList1)
#mydb.commit()

my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()

for row in result:
  print(row[0])
  
