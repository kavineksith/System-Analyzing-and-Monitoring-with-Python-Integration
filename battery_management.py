import json
import psutil  # importing psutil library
from report_signatures import TimeStampGenerator  # importing generate_report and convert time library functions
import sys  # importing sys library


class BatteryManager:
    @staticmethod
    def batteryManagement():
        try:
            # Battery Usage Statistics
            battery = psutil.sensors_battery()  # assign battery variable to psutil battery function

            statistics = {
                'Battery Usage Statistics': {
                    'Battery Percentage': f'{battery.percent} %',
                    'Power Connectivity': 'Power Connected' if battery.power_plugged else 'Power Disconnected',
                    'Battery Remaining Time': TimeStampGenerator.convertTime(battery.secsleft),
                    'Generated Time & Date': TimeStampGenerator().generate_report()
                }
            }

            result = json.dumps(statistics, indent=4)
            json_output = json.loads(result)
            return json_output  # Return the JSON output as a string
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
