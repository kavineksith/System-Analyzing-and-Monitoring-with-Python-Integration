import psutil, sys # importing psutil and sys library
from report_signatures import generated_report # importing date-time stamp generator library
from insert_queries import valuesManagement # importing sql query executor custom function
from deviceIdentity import deviceIdentify # getting device_name of user device

# System memory usage statistics
def virtualMemoryManagement():
    v_memory = psutil.virtual_memory()

    THRESHOLD = 100 * 1024 * 1024  # Compulsory THRESHOLD value should be 100MB
    THRESHOLD_Status = "Sufficient" if (v_memory.available <= THRESHOLD) else "Insufficient"

    TotalMemory = v_memory.total / (1024 ** 3)
    AvailableMemory = v_memory.available / (1024 ** 3)
    UsedMemory = v_memory.used / (1024 ** 3)
    FreeMemory = v_memory.free / (1024 ** 3)
    MemoryPercentage = v_memory.percent
    timeStamp = generated_report()[0] # calling to time stamp function
    dateStamp = generated_report()[1] # calling to date stamp function

    VM_query = '''INSERT INTO virtualMemoryManagement(
        TotalMemory,
        AvailableMemory,
        UsedMemory,
        FreeMemory,
        MemoryPercentage,
        THRESHOLD_Status,
        reportGeneratedTime,
        reportGeneratedDate,
        DeviceIdentity
    )'''

    VM_values = [TotalMemory, AvailableMemory, UsedMemory, FreeMemory, MemoryPercentage, THRESHOLD_Status, timeStamp, dateStamp, deviceIdentify()]

    valuesManagement(VM_query, VM_values)

# System swap memory statistics
def swapMemoryManagement():
    s_memory = psutil.swap_memory()

    S_TotalMemory = s_memory.total / (1024 ** 3)
    S_UsedMemory = s_memory.used / (1024 ** 3)
    S_FreeMemory =s_memory.free / (1024 ** 3)
    S_MemoryPercentage = s_memory.percent
    S_SystemInMemory = s_memory.sin / (1024 ** 3)
    S_SystemOutMemory = s_memory.sout / (1024 ** 3)
    timeStamp = generated_report()[0] # calling to time stamp function
    dateStamp = generated_report()[1] # calling to date stamp function

    SM_query = '''INSERT INTO swapMemoryManagement(
        TotalMemory,
        UsedMemory,
        FreeMemory,
        MemoryPercentage,
        SystemInMemory,
        SystemOutMemory,
        reportGeneratedTime,
        reportGeneratedDate,
        DeviceIdentity
    )'''

    SM_values = [S_TotalMemory, S_UsedMemory, S_FreeMemory, S_MemoryPercentage, S_SystemInMemory, S_SystemOutMemory, timeStamp, dateStamp, deviceIdentify()]

    valuesManagement(SM_query, SM_values)

def memoryManagement():
    virtualMemoryManagement()
    swapMemoryManagement()

if __name__ == "__main__":
    memoryManagement()
    sys.exit(0)