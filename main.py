import mysql.connector
def connect():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Mohan@$436",
        database="score_board"
    )
    return conn
if (connect()):
    print("connection established successfully ")
else:
    print("not")