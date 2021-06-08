import mysql.connector

def get_connection():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="my@sql",
    database="expense_manager",
    use_pure=True
    )




# # connect database
# def get_connection():
#     return sqlite3.connect(DB_FILE)

# if __name__ == '__main__':
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
#                     userid TEXT PRIMARY KEY,
#                     password TEXT NOT NULL,
#                     adminName TEXT NOT NULL,
#                     user_status TEXT NOT NULL,
#                     isadmin Text NOT NULL,
#                     date_time TEXT NOT NULL)""")

#     cursor.close()
#     conn.close()

# if __name__ == '__main__':
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""CREATE TABLE IF NOT EXISTS expenseTable_items(
#                     userid TEXT NOT NULL,
#                     date_time TEXT NOT NULL,
#                     title TEXT NOT NULL,
#                     expense REAL NOT NULL,
#                     FOREIGN KEY (userid) REFERENCES expenseTable_users (userid))""")

#     cursor.close()
#     conn.close()

# # conn = get_connection()
# # cursor = conn.cursor()
# # cursor.execute("INSERT INTO expenseTable_users VALUES (?, ?, ?, ?, ?, ?)", ("amit113920", "113920", "Amit Kumar", "enabled", "yes", "2PM-03/09/2020"))
# # conn.commit()

# # conn = get_connection()
# # cursor = conn.cursor()
# # cursor.execute("DELETE FROM EMA_users")
# # conn.commit()