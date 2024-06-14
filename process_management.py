import psutil
from report_signatures import TimeStampGenerator
import sys


class ProcessManager:
    def __init__(self):
        self.process_list = None

    def get_process_list(self):
        try:
            self.process_list = psutil.pids()
        except Exception as e:
            print(f"Error retrieving process list: {e}")
            sys.exit(1)

    def get_process_info(self):
        process_info_list = []
        try:
            for process_id in self.process_list:
                process = psutil.Process(process_id)
                process_info = process.as_dict(attrs=['pid', 'name'])
                process_info_list.append(process_info)
        except psutil.NoSuchProcess as e:
            print(f"Error getting process info: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
        return process_info_list

    def manage_processes(self):
        print('----- System Processes Statistics -----\n')
        self.get_process_list()
        if not self.process_list:
            print("No processes found.")
            return
        process_info_list = self.get_process_info()
        for process_info in process_info_list:
            print(process_info)
        TimeStampGenerator.generate_report()


if __name__ == "__main__":
    process_manager = ProcessManager()
    process_manager.manage_processes()
    sys.exit(0)
