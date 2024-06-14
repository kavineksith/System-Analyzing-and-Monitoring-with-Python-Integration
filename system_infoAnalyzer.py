import os  # importing os, platform and sys library
import platform
import sys
from report_signatures import TimeStampGenerator  # importing date-time stamp generator library


class SystemInformation:
    def __init__(self):
        pass

    def system_info(self):
        try:
            # Retrieving basic system information using platform and os modules
            os_name = os.name.upper()
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
            print(f'System Platform : {system_architecture}')
            print(f'OS Architecture : {os_architecture}')
        except RuntimeError as re:
            print("Error fetching system information: ", re)
        except Exception as e:
            raise RuntimeError("An error occurred: ", e)

    def systemInformation(self):
        print('----- System Information Overview -----\n')
        self.system_info()
        TimeStampGenerator().generate_report()


if __name__ == "__main__":
    sys_information = SystemInformation()
    sys_information.systemInformation()
    sys.exit(0)
