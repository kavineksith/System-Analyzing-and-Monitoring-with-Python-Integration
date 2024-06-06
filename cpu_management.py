import psutil
from report_signatures import generated_report
import sys

# Time Conveter from seconds
def convertTime(seconds): 
	minutes, seconds = divmod(seconds, 60) 
	hours, minutes = divmod(minutes, 60) 
	return '%d:%02d:%02d' % (hours, minutes, seconds)

# CPU Usage Management
def cpuUsageMonitor():
    cpu_usage = psutil.cpu_percent(interval=1, percpu=False)
    print(f'Total CPU Usage : {cpu_usage} %')
    cpu_count = psutil.cpu_count(logical=True)
    print(f'Total Processor Cores Count : {cpu_count}')
    cpu_time = psutil.cpu_times(percpu=False)
    print('System CPU Times Statistics as Time Durations')
    print(f'User : {convertTime(cpu_time[0])} | System : {convertTime(cpu_time[1])} | IDLE : {convertTime(cpu_time[2])} | Interrupt : {convertTime(cpu_time[3])} | DPC : {convertTime(cpu_time[4])}')
    cpu_time_precent = psutil.cpu_times_percent(interval=1, percpu=False)
    print('System CPU Times Statistics as Precentages')
    print(f'User : {cpu_time_precent[0]} % | System : {cpu_time_precent[1]} % | IDLE : {cpu_time_precent[2]} % | Interrupt : {cpu_time_precent[3]} % | DPC : {cpu_time_precent[4]} %')
    cpu_frequents = psutil.cpu_freq(percpu=False)
    print(f'Current : {cpu_frequents.current} Mhz | Min : {cpu_frequents.min} Mhz | Max : {cpu_frequents.max} Mhz')
    cpu_stats = psutil.cpu_stats()
    print(f'Context Switches : {cpu_stats.ctx_switches} | Interrupts : {cpu_stats.interrupts} | Software Interrupts : {cpu_stats.soft_interrupts} | System Calls : {cpu_stats.syscalls}')

# CPU Load Indicator
def check_cpu():
    cpu_usage = psutil.cpu_percent(1)
    if cpu_usage < 75:
        return "CPU load normal."
    else:
        return "CPU load too high."

def cpuManagement():
    print('----- CPU Usage Statistics -----\n')
    cpuUsageMonitor()
    print(f"\n{'-'*32}")
    print(f'Status : {check_cpu()}')
    print(f"{'-'*32}\n")
    generated_report()

if __name__ == "__main__":
    cpuManagement()
    sys.exit(0)