import mysql.connector
def connect():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Mohan@$436",
        database="librare"
    )
    return conn
if (connect()):
    print("connection established")
else:
    print("not")