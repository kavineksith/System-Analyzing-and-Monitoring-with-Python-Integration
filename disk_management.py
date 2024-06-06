import psutil
from report_signatures import generated_report
import sys

def diskManagement():
    partitions = []
    print('\n---- Storage Overall Report ----\n')

    # Storage Overall Report
    local_partitions = psutil.disk_partitions()
    for partition in local_partitions:
        print('Device : {}, MountPoint : {}, FileSystem Type : {}, OPTS : {}, MaxFile : {}, MaxPath : {}'.format(partition[0],partition[1],partition[2],partition[3],partition[4],partition[5]))
        partitions.append(partition[0])

    print('\n---- Storage Statistics Report ----\n')

    # Storage Statistics Report
    for partition in partitions:
        usage = psutil.disk_usage(partition)
        print("Local Disk : '{}'".format(partition))
        print(f'Total : {usage.total / (1024 ** 3):.2f} GB , Used : {usage.used / (1024 ** 3):.2f} GB , Free : {usage.free / (1024 ** 3):.2f} GB')
        print(f'Precentages : Used Space - {usage.percent} %, Free Space - {(usage.free / usage.total * 100):.1f} %')

    print('\n---- Storage Level Checker ----\n')

    # Storage Level Checker
    for partition in partitions:
        disk = psutil.disk_usage(partition)
        free_precentage = disk.free / disk.total * 100
        free_gigabytes = disk.free / 2 **30
        minimum_gigabytes = 2
        minimum_precentage = 10

        if free_precentage < minimum_precentage or free_gigabytes < minimum_gigabytes:
            print("{} - Storage isn't sufficent.".format(partition))
        else:
            print("{} - Storage is sufficent.".format(partition))
    
    generated_report()

if __name__ == "__main__":
    diskManagement()
    sys.exit(0)