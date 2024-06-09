import psutil, sys # importing psutil and sys library
from report_signatures import generated_report # importing date-time stamp generator library
from insert_queries import valuesManagement # importing sql query executor custom function
from deviceIdentity import deviceIdentify # getting device_name of user device

def diskManagement():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        device = partition.device
        mount_point = partition.mountpoint
        file_system_type = partition.fstype
        opts = partition.opts
        max_file = partition.maxfile
        max_path = partition.maxpath

        usage = psutil.disk_usage(mount_point)
        total_gb = usage.total / (1024 ** 3)
        used_gb = usage.used / (1024 ** 3)
        free_gb = usage.free / (1024 ** 3)
        percent_used = usage.percent
        percent_free = (usage.free / usage.total * 100)

        # Storage Level Checker
        minimum_gb = 2
        minimum_percentage = 10
        storage_status = "Sufficient" if (free_gb >= minimum_gb and percent_free >= minimum_percentage) else "Insufficient"

        timeStamp = generated_report()[0] # calling to time stamp function
        dateStamp = generated_report()[1] # calling to date stamp function
        
        def PartitionsValuesManagement():
            # Insert the partition information into the database
            PMT_query = '''INSERT INTO PartitionsManagementTable (
                device, 
                mount_point, 
                file_system_type, 
                opts, 
                max_file, 
                max_path,
                reportGeneratedTime,
                reportGeneratedDate,
                DeviceIdentity
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''' 
            
            PMT_values = [device, mount_point, file_system_type, opts, max_file, max_path, timeStamp, dateStamp, deviceIdentify()]

            valuesManagement(PMT_query, PMT_values)

        def PartitionsAnalyzedResportsManagement():
            # Insert the partition information into the database
            PAR_query = '''INSERT INTO PartitionsAnalyzedReports (
                device, 
                total_gb, 
                used_gb, 
                free_gb, 
                percent_used, 
                percent_free, 
                storage_status,
                reportGeneratedTime,
                reportGeneratedDate,
                DeviceIdentity
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''' 
            
            PAR_values = [device, total_gb, used_gb, free_gb, percent_used, percent_free, storage_status, timeStamp, dateStamp, deviceIdentify()]

            valuesManagement(PAR_query, PAR_values)

def ReportSelection():
    print('0: Default\n1: PartitionsManagementTable\n2: PartitionsAnalyzedReports')
    category = int(input('Which report do you want to add the database : ? '))
    if category == 1:
        diskManagement.PartitionsValuesManagement()
    elif category == 2:
        diskManagement.PartitionsAnalyzedResportsManagement()
    elif category == 0:
        diskManagement.PartitionsValuesManagement()
        diskManagement.PartitionsAnalyzedResportsManagement()
    else:
        print('Please enter option do want to proceed.')
        sys.exit(1)

if __name__ == "__main__":
    ReportSelection()
    sys.exit(0)
