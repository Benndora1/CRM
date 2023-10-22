import mysql.connector


dataBase =  mysql.connector.connect(
    host = 'localhost',
    port = '3316',
    user = 'root',
    passwd = '19949064'
)


#prepare a cursoer object

cursorObject = dataBase.cursor()


# create a database

cursorObject.execute("CREATE DATABASE elderco")

print("All Done")