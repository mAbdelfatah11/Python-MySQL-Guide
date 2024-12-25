import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()

mycursor.execute(" SELECT * FROM movies WHERE name='vikins' ")

result = mycursor.fetchone()        # fetch a single row of data from the result set of a database que

print(result)





