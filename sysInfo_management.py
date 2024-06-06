import os
import psutil
import platform
import datetime
from report_signatures import generated_report
import sys

def system_info():
    os_name = os.name
    os_platfrom = platform.system()
    os_release = platform.release()

def check_reboot():
    location = os.path.exists('run/reboot-required')
    if location == True:
        return "Pending Reboot."
    else:
        return "No pending Reboot."

def check_bootTime():
    boot_time = psutil.boot_time()
    print("System Boot Time : {} seconds.".format(boot_time))
    print('System Boot Time : {}'.format(datetime.datetime.fromtimestamp(boot_time).strftime("%Y-%m-%d %H:%M:%S")))

def user_profiles():
    users = psutil.users()
    for value in users:
        print("Users : {}".format(value[0]))

def systemReport():
    print('----- System Info Statistics -----\n')
    print(' -- Reboot Status -- ')
    print(f'Status : {check_reboot()}')
    print('\n -- System BootTime Analysis -- ')
    check_bootTime()
    print('\n -- System Users List -- ')
    user_profiles()
    generated_report()

if __name__ == "__main__":
    systemReport()
    sys.exit(0)
