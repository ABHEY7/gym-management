def registerUser(data):
    # print(data)
    try:
        # cursor.execute("INSERT INTO `emailtest` (`email`)" "VALUES(%s)", data)
        cursor.execute("INSERT INTO `user` (`email` ,`password` ,`contact` ,`address` ,`name`)" "VALUES(%s ,%s, %s, %s, %s)", data)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def getAllGuards():
    try:
        cursor.execute("SELECT * FROM `user`")
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return False
    
def deleteGuard(id):
    try:
        cursor.execute("DELETE FROM `user` WHERE `id` = %s", id)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
