import mysql
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gym"
)


# create cursor
cursor = con.cursor()

# function for user login
def login(arg):
    try:
        cursor.execute("select * from login where username=%s and Password=%s ", arg)
        return (cursor.fetchone())


    except:
        return False



def register(arg):
    print(arg)
    try:
        cursor.execute("INSERT INTO login (username, password) VALUES (%s, %s)", arg)
        con.commit()
        return True
    except:
        return False
    

  #-------------------------------------------------------------------------------------------------------
def registerUser(data):
    print(data)
    try:
        # cursor.execute("INSERT INTO `emailtest` (`email`)" "VALUES(%s)", data)
        cursor.execute("INSERT INTO `entrybox` (`name` ,`start` ,`adress`,cont)" "VALUES(%s ,%s, %s,%s)", data)
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def getallentry():
    try:
        cursor.execute("SELECT * FROM `entrybox`")
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False
    
def delete_entry(id):
    try:
        cursor.execute("DELETE FROM `user` WHERE `id` = %s", id)
        con.commit()
        return True
    except Exception as e:
        print(e)
        return False
  