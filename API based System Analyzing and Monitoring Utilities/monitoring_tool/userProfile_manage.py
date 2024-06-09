import psutil, datetime, sys # importing psutil, datetime and sys library
from report_signatures import generated_report # importing date-time stamp generator library
from insert_queries import valuesManagement # importing sql query executor custom function
from deviceIdentity import deviceIdentify # getting device_name of user device

# Check System BootTime
def systemBootTime(time):
    return datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d %H:%M:%S")

# User Profiles Management
def UserStatusManagement():
    for value in psutil.users():
        print(f'{value[0]} {value[1]} {value[2]} {systemBootTime(value[3])} {value[4]}')
        userName = value[0]
        terminal = value[1]
        host = value[2]
        startedTime = systemBootTime(value[3])
        processID = value[4]
        
        timeStamp = generated_report()[0]
        dateStamp = generated_report()[1]

        UM_query = '''INSERT INTO UserManagement(
            UserProfile,
            Termial,
            Host,
            StartedBootTime,
            ProcessID,
            reportGeneratedTime,
            reportGeneratedDate,
            DeviceIdentity
            )VALUES(?,?,?,?,?,?,?,?)'''
        
        UM_values = [userName, terminal, host, startedTime, processID, timeStamp, dateStamp, deviceIdentify()]

        valuesManagement(UM_query, UM_values)

if __name__ == "__main__":
    UserStatusManagement()
    sys.exit(0)
