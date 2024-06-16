import json
import psutil
import sys
from report_signatures import TimeStampGenerator


class CPUManager:
    def __init__(self):
        self.cpu_usage = None
        self.cpu_count = None
        self.cpu_time = None
        self.cpu_time_percentages = None
        self.cpu_frequents = None
        self.cpu_stats = None

    # Function to monitor CPU usage and related statistics
    def monitor_cpu(self):
        try:
            # Retrieve total CPU usage
            self.cpu_usage = psutil.cpu_percent(interval=1, percpu=False)
            # Retrieve total processor cores count
            self.cpu_count = psutil.cpu_count(logical=True)
            # Retrieve system CPU times statistics as time durations
            self.cpu_time = psutil.cpu_times(percpu=False)
            # Retrieve system CPU times statistics as percentages
            self.cpu_time_percentages = psutil.cpu_times_percent(interval=1, percpu=False)
            # Retrieve current, min, and max CPU frequencies
            self.cpu_frequents = psutil.cpu_freq(percpu=False)
            # Retrieve CPU stats
            self.cpu_stats = psutil.cpu_stats()

            statistics = {
                'CPU Usage Statistics': {
                    'Total CPU Usage': f'{self.cpu_usage} %',
                    'Total Processor Cores Count': f'{self.cpu_count}',
                    'CPU Load Status': f'{"CPU load is normal." if psutil.cpu_percent(1) < 75 else "CPU load is too high."}',
                    'System CPU Time Statistics (Time)': {
                        'User': f'{TimeStampGenerator().convertTime(self.cpu_time[0])}',
                        'System': f'{TimeStampGenerator().convertTime(self.cpu_time[1])}',
                        'IDLE': f'{TimeStampGenerator().convertTime(self.cpu_time[2])}',
                        'Interrupt': f'{TimeStampGenerator().convertTime(self.cpu_time[3])}',
                        'DPC': f'{TimeStampGenerator().convertTime(self.cpu_time[4])}'
                    },
                    'System CPU Time Statistics (Percentages)': {
                        'User': f'{self.cpu_time_percentages[0]} %',
                        'System': f'{self.cpu_time_percentages[1]} %',
                        'IDLE': f'{self.cpu_time_percentages[2]} %',
                        'Interrupt': f'{self.cpu_time_percentages[3]} %',
                        'DPC': f'{self.cpu_time_percentages[4]} %'
                    },
                    'CPU Frequency Statistics': {
                        'Current': f'{self.cpu_frequents.current} Mhz',
                        'Min': f'{self.cpu_frequents.min} Mhz',
                        'Max': f'{self.cpu_frequents.max} Mhz',
                    },
                    'CPU Stats Statistics': {
                        'Context Switches': f'{self.cpu_stats.ctx_switches}',
                        'Interrupts': f'{self.cpu_stats.interrupts}',
                        'Software Interrupts': f'{self.cpu_stats.soft_interrupts}',
                        'System Calls': f'{self.cpu_stats.syscalls}'
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
