import psutil
from report_signatures import TimeStampGenerator
import sys


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
            print(f'Total CPU Usage : {self.cpu_usage} %')

            # Retrieve total processor cores count
            self.cpu_count = psutil.cpu_count(logical=True)
            print(f'Total Processor Cores Count : {self.cpu_count}')

            # Retrieve system CPU times statistics as time durations
            self.cpu_time = psutil.cpu_times(percpu=False)
            print('System CPU Times Statistics as Time Durations')
            print(
                f'User : {TimeStampGenerator().convertTime(self.cpu_time[0])} | System : {TimeStampGenerator().convertTime(self.cpu_time[1])} | IDLE : {TimeStampGenerator().convertTime(self.cpu_time[2])} | Interrupt : {TimeStampGenerator().convertTime(self.cpu_time[3])} | DPC : {TimeStampGenerator().convertTime(self.cpu_time[4])}')

            # Retrieve system CPU times statistics as percentages
            self.cpu_time_percentages = psutil.cpu_times_percent(interval=1, percpu=False)
            print('System CPU Times Statistics as Percentages')
            print(
                f'User : {self.cpu_time_percentages[0]} % | System : {self.cpu_time_percentages[1]} % | IDLE : {self.cpu_time_percentages[2]} % | Interrupt : {self.cpu_time_percentages[3]} % | DPC : {self.cpu_time_percentages[4]} %')

            # Retrieve current, min, and max CPU frequencies
            self.cpu_frequents = psutil.cpu_freq(percpu=False)
            print(
                f'Current : {self.cpu_frequents.current} Mhz | Min : {self.cpu_frequents.min} Mhz | Max : {self.cpu_frequents.max} Mhz')

            # Retrieve CPU stats
            self.cpu_stats = psutil.cpu_stats()
            print(
                f'Context Switches : {self.cpu_stats.ctx_switches} | Interrupts : {self.cpu_stats.interrupts} | Software Interrupts : {self.cpu_stats.soft_interrupts} | System Calls : {self.cpu_stats.syscalls}')
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    # Function to check CPU load
    def check_cpu_load(self):
        try:
            cpu_usage = psutil.cpu_percent(1)
            if cpu_usage < 75:
                return "CPU load normal."
            else:
                return "CPU load too high."
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    # Function to manage CPU statistics
    def manage_cpu(self):
        try:
            print('----- CPU Usage Statistics -----\n')
            self.monitor_cpu()
            print(f"\n{'-' * 32}")

            # Check CPU load status
            print(f'Status : {self.check_cpu_load()}')
            print(f"{'-' * 32}\n")

            # Generate timestamp report
            TimeStampGenerator().generate_report()
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    cpu_manager = CPUManager()
    cpu_manager.manage_cpu()
    sys.exit(0)
