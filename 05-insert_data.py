import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()

      
sql = "INSERT INTO movies(name , plot) VALUES(%s , %s)"      # pass the following values data using format string %s
data = ("Harry Potter2" , 'magic Movie2')


mycursor.execute(sql , data)

myconn.commit()                               # you must "commit" changes of you edit database


print('data inserted ')
print(mycursor.lastrowid)

