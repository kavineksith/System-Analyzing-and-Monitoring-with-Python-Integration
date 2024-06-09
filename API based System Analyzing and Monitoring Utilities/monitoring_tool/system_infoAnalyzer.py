import os, psutil, platform, datetime, sys # importing os, psutil ,platform, datetime and sys library
from insert_queries import valuesManagement # importing sql query executor custom function
from report_signatures import generated_report # importing date-time stamp generator library

def systemInformation():
    # Retrieving basic system information using platform and os modules
    os_name = (os.name).upper()
    system_architecture = sys.platform
    os_platform = platform.system()
    os_architecture = platform.architecture()[0]
    os_release = platform.release()
    # os_version = platform.version()
    device_processor = platform.processor()
    machine_type = platform.machine()
    sys_platform = platform.platform()
    os_edition = platform.win32_edition()
    device_name = platform.node()

    PC_Name = device_name
    OperatingSystem = f'{os_platform} {os_name} {os_release} {os_architecture} {os_edition}'
    OS_RSP_Version = sys_platform
    ProcessorIdentity = device_processor
    MachineType = machine_type
    SystemPlatfrom = system_architecture
    OSArchitecture = os_architecture

    # Reboot Status Checking
    location = os.path.exists('run/reboot-required')
    reboot_status = "Pending Reboot." if (location == True) else "No pending Reboot."

    # Check System BootTime
    boot_time = psutil.boot_time()
    systemBootTime = datetime.datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")

    timeStamp = generated_report()[0]
    dateStamp = generated_report()[1]

    SI_insert_query = '''INSERT INTO DeviceInformation(
        PCName,
        OperatingSystem,
        OSReleaseSericePackVersion,
        ProcessorIdentity,
        MachineType,
        SystemPlatform,
        OSArchitecture,
        RebootStatus,
        SystemBootTime,
        reportGeneratedTime,
        reportGeneratedDate
        )VALUES(?,?,?,?,?,?,?,?,?,?,?)'''
    
    SI_values_query = (PC_Name, OperatingSystem, OS_RSP_Version, ProcessorIdentity, MachineType, SystemPlatfrom, OSArchitecture, reboot_status, systemBootTime, timeStamp, dateStamp)

    valuesManagement(SI_insert_query, SI_values_query)

if __name__ == "__main__":
    systemInformation()
    sys.exit(0)