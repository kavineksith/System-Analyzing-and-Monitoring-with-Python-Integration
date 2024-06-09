import socket
import sys
import sqlite3
from report_signatures import generated_report
from insert_queries import valuesManagement
from deviceIdentity import deviceIdentify

if len(sys.argv) != 4:
    print('port_scanner.py ip_address start_port end_port')
    sys.exit(1)

[ip_address, start_port, end_port] = sys.argv[1:]

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

def create_port_scan_table(conn):
    """ Create a port scan table if it does not exist """
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS port_scan (
                            id INTEGER PRIMARY KEY,
                            ip_address TEXT,
                            port INTEGER,
                            status TEXT
                            )''')
        print("Port scan table created successfully.")
    except sqlite3.Error as e:
        print(e)

def insert_scan_result(conn, ip_address, port, status):
    """ Insert scan result into the port_scan table """
    try:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO port_scan (ip_address, port, status) VALUES (?, ?, ?)''', (ip_address, port, status))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def portScanner(conn):
    """ Scan ports and insert results into the SQLite database """
    open_ports = []
    closed_ports = []
    for port in range(int(start_port), int(end_port)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((str(ip_address), port))
        if result == 0:
            open_ports.append(port)
            insert_scan_result(conn, ip_address, port, "open")
        else:
            closed_ports.append(port)
            insert_scan_result(conn, ip_address, port, "closed")
        sock.close()

    print(f'Opened Port List : {open_ports}')
    print(f'Closed Port List : {closed_ports}')

if __name__ == "__main__":
    # Connect to the SQLite database
    db_file = "port_scan_results.db"
    conn = create_connection(db_file)
    if conn is not None:
        # Create port scan table
        create_port_scan_table(conn)
        # Perform port scanning and insert results into the database
        portScanner(conn)
        # Close the database connection
        conn.close()
        print("Database connection closed.")
    else:
        print("Error: Unable to connect to the SQLite database.")
    sys.exit(0)

