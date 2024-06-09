import psutil
import sys
import sqlite3

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database: {db_file}")
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_process_table(conn):
    """ Create a process table if it does not exist """
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS processes (
                            pid INTEGER PRIMARY KEY,
                            name TEXT
                            )''')
        print("Process table created successfully.")
    except sqlite3.Error as e:
        print(e)

def insert_process_info(conn, process_info):
    """ Insert process information into the processes table """
    try:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO processes (pid, name) VALUES (?, ?)''', (process_info['pid'], process_info['name']))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def process_management(conn):
    """ Retrieve process information and insert into the SQLite database """
    for process in psutil.process_iter():
        try:
            process_info = process.as_dict(attrs=['pid', 'name'])
        except psutil.NoSuchProcess:
            message = "No Such Process Founded...!!"
            insert_process_info(conn, message)
        else:
            insert_process_info(conn, process_info)

if __name__ == "__main__":
    # Connect to the SQLite database
    db_file = "processes.db"
    conn = create_connection(db_file)
    if conn is not None:
        # Create process table
        create_process_table(conn)
        # Perform process management and insert into the database
        process_management(conn)
        # Close the database connection
        conn.close()
        print("Database connection closed.")
    else:
        print("Error: Unable to connect to the SQLite database.")
    sys.exit(0)

