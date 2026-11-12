import sqlite3 as sql


def create_connection():
    connection = sql.connect("finance.db")
    connection.row_factory = sql.Row
    return connection


def create_table():
    connection = create_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            type TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()



def insertTransaction(description, amount, category, type, date):

    connection = create_connection()

    connection.execute("""
        INSERT INTO transactions
        (description, amount, category, type, date)
        VALUES (?, ?, ?, ?, ?)
    """, (description, amount, category, type, date))

    connection.commit()
    connection.close()



def getTransaction():
    connection = create_connection()

    transactions =  connection.execute("""
        SELECT * FROM transactions
        ORDER BY date DESC
        """).fetchall()
    
    connection.close()

    return transactions

def deleteTransaction(transactionID):
    connection = create_connection()

    connection.execute("""
        DELETE FROM transactions
        WHERE id = ?
    """, (transactionID,))

    connection.commit()
    connection.close()