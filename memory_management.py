import json
import psutil
import sys
from report_signatures import TimeStampGenerator


class MemoryManager:
    @staticmethod
    # Function to retrieve and print memory statistics
    def memory_statistics():
        try:
            # System memory usage statistics
            v_memory = psutil.virtual_memory()
            # System swap memory statistics
            s_memory = psutil.swap_memory()

            statistics = {
                'Memory Usage Statistics': {
                    'System Memory': {
                        'Total': f'{v_memory.total / (1024 ** 3):.2f} GB',
                        'Available': f'{v_memory.available / (1024 ** 3):.2f} GB',
                        'Percentage': f'{v_memory.percent} %',
                        'Used': f'{v_memory.used / (1024 ** 3):.2f} GB',
                        'Free': f'{v_memory.free / (1024 ** 3):.2f} GB'
                    },
                    'THRESHOLD': f'{"Warning: Available memory is below the threshold of 100MB." if v_memory.available <= (100 * 1024 * 1024) else "Available memory is sufficient."}',
                    'Swap Memory': {
                        'Total': f'{s_memory.total / (1024 ** 3):.2f} GB',
                        'Used': f'{s_memory.used / (1024 ** 3):.2f} GB',
                        'Free': f'{s_memory.free / (1024 ** 3):.2f} GB',
                        'Percentage': f'{s_memory.percent} %',
                        'System IN': f'{s_memory.sin / (1024 ** 3):.2f} GB',
                        'System OUT': f'{s_memory.sout / (1024 ** 3):.2f} GB'
                    },
                    'Generated Time & Date': f'{TimeStampGenerator().generate_report()}'
                }
            }

            result = json.dumps(statistics, indent=4)
            json_output = json.loads(result)
            return json_output  # Return the JSON output as a string
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
