import mysql.connector
#this file is to create the database , we can do it directly on mysql
dataBase=mysql.connector.connect(
    host='localhost',
    # if you are running on your computer just change the name and password to your own mysql account
    user='root',
    passwd='Qpalzm@123'
)

cursorObject=dataBase.cursor()
cursorObject.execute("CREATE DATABASE crm_database")
print("All done")