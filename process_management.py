# import json
import psutil
import sys
from report_signatures import TimeStampGenerator


class ProcessManager:
    def __init__(self):
        self.process_list = None

    def get_process_list(self):
        try:
            self.process_list = [{'pid': pid} for pid in psutil.pids()]
            return self.process_list
        except Exception as e:
            print(f"Error retrieving process list: {e}")
            sys.exit(1)

    def get_process_info(self):
        process_info_list = []
        try:
            for process in self.process_list:
                process_id = process['pid']
                process = psutil.Process(process_id)
                process_info = process.as_dict(attrs=['pid', 'name'])
                process_info_list.append(process_info)

            return process_info_list
        except psutil.NoSuchProcess as e:
            print(f"Error retrieving process info: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    def manage_processes(self):
        try:
            # System Processes Statistics
            process_list = self.get_process_list()
            process_info = self.get_process_info()

            # Check if process_list is a string, if not convert it to a string
            if not isinstance(process_list, str):
                process_list = ", ".join(map(str, process_list))

            statistics = {
                'System Processes Statistics': {
                    'Process List': process_list,
                    'Process Info': process_info,
                    'Generated Time & Date': f'{TimeStampGenerator().generate_report()}'
                }
            }

            return statistics

            # json_output = json.dumps(statistics, indent=4)
            # print(json_output)  # Return the JSON output as a string
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


# def save_to_json():
#     try:
#         process_manager = ProcessManager()
#         # process_manager.manage_processes()
#         statistics = process_manager.manage_processes()
#
#         with open("./disk_statistics.json", 'w', encoding='utf-8') as json_file:
#             json.dump(statistics, json_file, indent=4, ensure_ascii=False)
#     except Exception as e:
#         print(f"Error saving JSON data: {e}")
#
#
# save_to_json()
