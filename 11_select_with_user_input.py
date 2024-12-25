import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()

sql = " SELECT * FROM movies WHERE name=%s "        # get user as format string
data = ('vikins',)                                  # user input, ',' is set because the execute command expects tuple not string, so it is a formating wise only

mycursor.execute(sql , data)



result = mycursor.fetchall()

print(result)





