import mysql.connector

# connect database
def get_connection():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="my@sql",
    database="expense_manager",
    use_pure=True
    )


if __name__ == '__main__':
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                    userID varchar(100) PRIMARY KEY,
                    username varchar(100) NOT NULL,
                    password varchar(100) NOT NULL,
                    admin_name varchar(100) NOT NULL,
                    user_status varchar(100) NOT NULL,
                    is_admin varchar(100) NOT NULL,
                    date datetime default now())""")

    cursor.close()
    conn.close()

if __name__ == '__main__':
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS expense(
                    userID varchar(100),
                    date date NOT NULL,
                    product_name varchar(100) NOT NULL,
                    quantity int NOT NULL,
                    expense float NOT NULL,
                    FOREIGN KEY (userID) REFERENCES users(userID))""")

    cursor.close()
    conn.close()

# # conn = get_connection()
# # cursor = conn.cursor()
# # cursor.execute("INSERT INTO expenseTable_users VALUES (?, ?, ?, ?, ?, ?)", ("amit113920", "113920", "Amit Kumar", "enabled", "yes", "2PM-03/09/2020"))
# # conn.commit()

# # conn = get_connection()
# # cursor = conn.cursor()
# # cursor.execute("DELETE FROM EMA_users")
# # conn.commit()