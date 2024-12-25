import mysql.connector          # import package

# Establish Connection:
myconn = mysql.connector.connect(       # pass connection credentials to "connect" method
    host = 'localhost',                 # install mysql locally
    user = 'root',
    passwd = "toor",
    # database = "dbname"                    # Not required 
)

# setup a connection tunnel:
mycursor = myconn.cursor()                  # setup a connection tunnel between connector library and mysql to start passing commands

# execute commands against DB:
mycursor.execute("QUERY.......")