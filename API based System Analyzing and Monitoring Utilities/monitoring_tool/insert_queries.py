import sqlite3 # importing sqlite3 database library

db_source = './systemDB.db'

def valuesManagement(query, values):
    try:
        connection = sqlite3.connect(db_source)
        cursor = connection.cursor()
        cursor.execute(query, values)
        connection.commit()  # Commit changes to the database
        print('Operation successful...!!')  # Generic success message
    except sqlite3.Error as e:
        print(f"Error: {e}")
        print('Operation failed...!!')  # Print failure message
    finally:
        if connection:
            connection.close()
