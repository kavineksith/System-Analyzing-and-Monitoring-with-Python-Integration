import datetime  # importing datetime, os, json, platform, sys and psutil libraries
import os
import json
import platform
import sys
import psutil
from report_signatures import TimeStampGenerator  # importing date-time stamp generator library


class SystemInformation:
    @staticmethod
    def check_reboot():
        try:
            location = os.path.exists('run/reboot-required')
            return "Pending Reboot." if location else "No pending Reboot."
        except Exception as e:
            raise RuntimeError("Error checking reboot status:", e)

    @staticmethod
    def get_boot_time():
        try:
            boot_time = psutil.boot_time()
            return boot_time
        except Exception as e:
            raise RuntimeError("Error fetching boot time:", e)

    @staticmethod
    def get_users():
        try:
            users = psutil.users()
            return [value[0] for value in users]
        except Exception as e:
            raise RuntimeError("Error fetching user profiles:", e)

    @staticmethod
    def system_info():
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

            system_users = SystemInformation().get_users()

            # System Info Statistics

            statistics = {
                'System Info Statistics': {
                    'System Information': {
                        'Device Name': f'{device_name}',
                        'Operating System': f'{os_platform} {os_name} {os_release} {os_architecture} {os_edition}',
                        'OS Release and Service Pack Version': f'{sys_platform}',
                        'Processor Identity': f'{device_processor}',
                        'Machine Type': f'{machine_type}',
                        'System Platform': f'{system_architecture}',
                        'OS Architecture': f'{os_architecture}'
                    },
                    'System Boot Information': {
                        'Reboot Status': f'{SystemInformation().check_reboot()}',
                        'System Boot Time (sec)': f'{SystemInformation().get_boot_time()} seconds.',
                        'System Boot Time': f'{datetime.datetime.fromtimestamp(SystemInformation().get_boot_time()).strftime("%Y-%m-%d %H:%M:%S")}'
                    },
                    'System Users List': system_users,
                    'Generated Time & Date': f'{TimeStampGenerator().generate_report()}'
                }
            }

            result = json.dumps(statistics, indent=4)
            json_output = json.loads(result)
            return json_output  # Return the JSON output as a string
        except RuntimeError as re:
            print("Error fetching system information: ", re)
        except Exception as e:
            raise RuntimeError("An error occurred: ", e)
