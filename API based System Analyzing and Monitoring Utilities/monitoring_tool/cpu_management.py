import psutil, sys # importing psutil and sys library
from report_signatures import generated_report # importing date-time stamp generator library
from insert_queries import valuesManagement # importing sql query executor custom function
from deviceIdentity import deviceIdentify # getting device_name of user device

# Time Conveter from seconds
def convertTime(seconds): 
	minutes, seconds = divmod(seconds, 60) 
	hours, minutes = divmod(minutes, 60) 
	return '%d:%02d:%02d' % (hours, minutes, seconds)

# CPU Usage Management
def cpuUsageMonitor():
    CPUUsage = psutil.cpu_percent(interval=1, percpu=False)
    ProcessorCount = psutil.cpu_count(logical=True)
    
    cpu_time = psutil.cpu_times(percpu=False)
    userTimeDuration = convertTime(cpu_time[0])
    systemTimeDuration = convertTime(cpu_time[1])
    IDLETimeDuration = convertTime(cpu_time[2])
    InterruptTimeDuration = convertTime(cpu_time[3])
    DPCTimeDuration = convertTime(cpu_time[4])

    cpu_time_precent = psutil.cpu_times_percent(interval=1, percpu=False)
    userDurationPrecentage = cpu_time_precent[0]
    systemDurationPrecentage = cpu_time_precent[1]
    IDLEDurationPrecentage = cpu_time_precent[2]
    InterruptDurationPrecentage = cpu_time_precent[3]
    DPCDurationPrecentage = cpu_time_precent[4]
    
    cpu_frequents = psutil.cpu_freq(percpu=False)
    CPUCurrentFrequency = cpu_frequents.current
    CPUMinimumFrequency = cpu_frequents.min
    CPUMaximumFrequency = cpu_frequents.max

    cpu_stats = psutil.cpu_stats()
    ContextSwitches = cpu_stats.ctx_switches
    Interrupts = cpu_stats.interrupts
    SoftwareInterrupts = cpu_stats.soft_interrupts
    SystemCalls = cpu_stats.syscalls

    # CPU Load Indicator
    cpu_usage = psutil.cpu_percent(1)
    CPUStatus = "Normal" if (cpu_usage < 75) else "High"

    timeStamp = generated_report()[0]
    dateStamp = generated_report()[1]

    CM_query = '''INSERT INTO CPUManagementStatistics(
    CPUUsage,
    ProcessorCount,
    userTimeDuration,
    systemTimeDuration,
    IDLETimeDuration,
    InterruptTimeDuration,
    DPCTimeDuration,
    userDurationPrecentage,
    systemDurationPrecentage,
    IDLEDurationPrecentage,
    InterruptDurationPrecentage,
    DPCDurationPrecentage,
    CPUCurrentFrequency,
    CPUMinimumFrequency,
    CPUMaximumFrequency,
    ContextSwitches,
    Interrupts,
    SoftwareInterrupts,
    SystemCalls,
    CPUStatus
    reportGeneratedTime,
    reportGeneratedDate,
    DeviceIdentity
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

    CM_values = [CPUUsage, ProcessorCount, userTimeDuration, systemTimeDuration, IDLETimeDuration, InterruptTimeDuration, DPCTimeDuration, userDurationPrecentage, systemDurationPrecentage, IDLEDurationPrecentage, InterruptDurationPrecentage, DPCDurationPrecentage, CPUCurrentFrequency, CPUMinimumFrequency, CPUMaximumFrequency, ContextSwitches, Interrupts, SoftwareInterrupts, SystemCalls, CPUStatus, timeStamp, dateStamp, deviceIdentify()]

    valuesManagement(CM_query, CM_values)

if __name__ == "__main__":
    cpuUsageMonitor()
    sys.exit(0)