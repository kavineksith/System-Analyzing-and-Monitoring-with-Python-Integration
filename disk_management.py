import psutil
from report_signatures import TimeStampGenerator
import sys


class DiskManager:
    def __init__(self):
        self.partitions = []

    # Function to generate storage overall report
    def generate_overall_report(self):
        try:
            print('\n---- Storage Overall Report ----\n')
            local_partitions = psutil.disk_partitions()
            for partition in local_partitions:
                print('Device : {}, MountPoint : {}, FileSystem Type : {}, OPTS : {}, MaxFile : {}, MaxPath : {}'.format(partition[0], partition[1], partition[2], partition[3], partition[4], partition[5]))
                self.partitions.append(partition[0])
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    # Function to generate storage statistics report
    def generate_statistics_report(self):
        try:
            print('\n---- Storage Statistics Report ----\n')
            for partition in self.partitions:
                usage = psutil.disk_usage(partition)
                print("Local Disk : '{}'".format(partition))
                print(f'Total : {usage.total / (1024 ** 3):.2f} GB , Used : {usage.used / (1024 ** 3):.2f} GB , Free : {usage.free / (1024 ** 3):.2f} GB')
                print(f'Percentages : Used Space - {usage.percent} %, Free Space - {(usage.free / usage.total * 100):.1f} %')
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    # Function to check storage level
    def check_storage_level(self):
        try:
            print('\n---- Storage Level Checker ----\n')
            for partition in self.partitions:
                disk = psutil.disk_usage(partition)
                free_percentage = disk.free / disk.total * 100
                free_gigabytes = disk.free / 2 ** 30
                minimum_gigabytes = 2
                minimum_percentage = 10

                if free_percentage < minimum_percentage or free_gigabytes < minimum_gigabytes:
                    print("{} - Storage isn't sufficient.".format(partition))
                else:
                    print("{} - Storage is sufficient.".format(partition))
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    # Function to manage disk statistics
    def manage_disk(self):
        try:
            self.generate_overall_report()
            self.generate_statistics_report()
            self.check_storage_level()
            TimeStampGenerator().generate_report()
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    disk_manager = DiskManager()
    disk_manager.manage_disk()
    sys.exit(0)
