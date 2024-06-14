import os
import psutil
import platform
import datetime
from report_signatures import TimeStampGenerator
import sys


class SystemInfo:
    def __init__(self):
        pass

    def get_os_info(self):
        try:
            os_name = os.name
            os_platform = platform.system()
            os_release = platform.release()
            return os_name, os_platform, os_release
        except Exception as e:
            raise RuntimeError("Error fetching OS information:", e)

    def check_reboot(self):
        try:
            location = os.path.exists('run/reboot-required')
            return "Pending Reboot." if location else "No pending Reboot."
        except Exception as e:
            raise RuntimeError("Error checking reboot status:", e)

    def get_boot_time(self):
        try:
            boot_time = psutil.boot_time()
            return boot_time
        except Exception as e:
            raise RuntimeError("Error fetching boot time:", e)

    def get_users(self):
        try:
            users = psutil.users()
            return [value[0] for value in users]
        except Exception as e:
            raise RuntimeError("Error fetching user profiles:", e)


def system_report():
    try:
        system_info = SystemInfo()

        print('----- System Info Statistics -----\n')
        print(' -- Reboot Status -- ')
        print(f'Status : {system_info.check_reboot()}')
        print('\n -- System BootTime Analysis -- ')
        boot_time = system_info.get_boot_time()
        print("System Boot Time : {} seconds.".format(boot_time))
        print('System Boot Time : {}'.format(datetime.datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")))
        print('\n -- System Users List -- ')
        users = system_info.get_users()
        for user in users:
            print("Users : {}".format(user))

        TimeStampGenerator.generate_report()
    except RuntimeError as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    system_report()
    sys.exit(0)
