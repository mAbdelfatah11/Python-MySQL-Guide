import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()

# mycursor.execute(" SELECT * FROM movies")
mycursor.execute(" SELECT name , plot FROM movies")

result = mycursor.fetchall()        # export fetched lines to a variable


print(result[0])

for movie in result :
    print(movie)





