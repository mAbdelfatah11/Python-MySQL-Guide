

## ---------------
# Create Database
mycursor.execute("CREATE DATABASE mydatabase")      # pass commands

# Create Table
mycursor.execute("CREATE TABLE movies ( name VARCHAR(100), plot VARCHAR(500))")

# Insert Into:

sql = "INSERT INTO movies( name, plot) VALUES(%s, %s)"      # pass the following values data using format string %s
data = ("first film","second film")
mycursor.execute( sql, data)

myconn.commit()             # you must "commit" changes of you edit database

print(mycursor.rowcount)    # number of lines affected "added or deleted"

