import os, platform, sys # importing os, platform and sys library
from report_signatures import generated_report # importing date-time stamp generator library

def system_info():
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

    print(f'Device Name : {device_name}')
    print(f'Operating System : {os_platform} {os_name} {os_release} {os_architecture} {os_edition}')
    print(f'OS Release and Service Pack Version : {sys_platform}')
    print(f'Processor Identity : {device_processor}')
    print(f'Machine Type : {machine_type}')
    print(f'System Platfrom : {system_architecture}')
    print(f'OS Architecture : {os_architecture}')

def systemInformation():
    print('----- System Information Overview -----\n')
    system_info()
    generated_report()

if __name__ == "__main__":
    systemInformation()
    sys.exit(0)
