import mysql
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="GYM"
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
    try:
        cursor.execute("INSERT INTO login (username, Password) VALUES (%s, %s)", arg)
        con.commit()
        return True
    except:
        return False