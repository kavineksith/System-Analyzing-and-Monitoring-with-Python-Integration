import sqlite3 # importing sqlite3 database library
from quries import DeviceInformation_query, batteryManagement_query, CPUManagement_query
from quries import networkManagement_query, PartitionsManagementTable_query, PartitionsAnalyzedReports_query
from quries import virtualMemoryManagement_query, swapMemoryManagement_query, UserManagement_query

# SQLite database initialization
db_source = './systemDB.db'
queries = [DeviceInformation_query, batteryManagement_query, CPUManagement_query, networkManagement_query, PartitionsManagementTable_query, PartitionsAnalyzedReports_query, virtualMemoryManagement_query,swapMemoryManagement_query, UserManagement_query]
table_list = ['DeviceInformation', 'batteryManagement', 'CPUManagementStatistics', 'networkManagement', 'PartitionsManagementTable', 'PartitionsAnalyzedReports', 'virtualMemoryManagement', 'swapMemoryManagement', 'UserManagement']

try:
    conncetion = sqlite3.connect(db_source)
    cursor = conncetion.cursor()

    print('Connected to SQLite Database')
    
    # Loop through table_list to check if tables exist
    for table_index, table in enumerate(table_list):
        check_query = f"SELECT EXISTS (SELECT name FROM sqlite_master WHERE type='table' AND name='{table}') AS result"
        cursor.execute(check_query)
        row = cursor.fetchone()
        if row[0] == 1:
            print(f"Table '{table}' already exists")
        else:
            print(f"Table '{table}' does not exist")
            if table_index < len(queries):
                create_query = queries[table_index]
                try:
                    cursor.execute(create_query)
                    conncetion.commit()
                    print(f"Table '{table}' created successfully")
                except sqlite3.Error as e:
                    print(f"Error creating table '{table}': {e}")
            else:
                print(f"No creation query found for table '{table}'")
                
    cursor.close()

except sqlite3.Error as e:
    print(f"Error: {e}")

finally:
    if conncetion:
        conncetion.close()
