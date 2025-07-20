from db import connect
def librarian_menu():
    while True:
        print("""\nLibrarary menu
              1.Insert_book
              2.View_library
              3.Update_library
              4.Delete_book""")
        ch = int(input("Enter the choice (1 - 4) : "))
        if ch == 1:
            insert_book()
        elif ch == 2:
            view_library()
        elif ch == 3:
            update_library()
        elif ch == 4:
            delete_book()
            break
        else:
            print("it is not possible")
def insert_book():
    conn = connect()
    cursor = conn.cursor()
    book_id = int(input("Enter the book_id: "))
    stock = int(input("Enter the no.of book: "))
    available = input("Enter the availablity type (yes/no) = ")
    query = "insert into librarian(book_id,stock,available)values(%s,%s,%s)"
    values = (book_id,stock,available)
    cursor.execute(query,values)
    conn.commit()
    print(f"{book_id} Book is inserted into library successfully")  
def view_library():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("select * from librarian")
    for row in cursor.fetchall():
        print(row)
    conn.close()
    print("\nHere is the entire library")
def update_library():
    conn = connect()
    cursor = conn.cursor()
    book_id = int(input("Enter the book_id:- "))
    stock = int(input("Enter the no.of book:- "))
    available = input("Enter the availablity type (yes/no) = ")
    cursor.execute("Update librarian set stock=%s,available=%s where book_id = %s",(stock,available,book_id))
    conn.commit()
    print(f"{book_id} Book is updated successfully")
def delete_book():
    conn = connect()
    cursor = conn.cursor()
    book_id = int(input("Enter the book_id to delete: "))
    cursor.execute("SELECT * FROM librarian WHERE book_id = %s", (book_id,))
    book = cursor.fetchone()
    if book:
        confirm = input(f"Are you sure you want to delete book with ID {book_id}? (yes/no): ").lower()
        if confirm == 'yes':
            cursor.execute("DELETE FROM librarian WHERE book_id = %s", (book_id,))
            conn.commit()
            print("Book deleted from the library successfully.")
        else:
            print("Not delete cancelled.")
    else:
        print("Book not found.")
    conn.close()
librarian_menu()