# Device Information Management Table Query
DeviceInformation_query = '''CREATE TABLE DeviceInformation (
    DMid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    DeviceName TEXT NOT NULL,
    OperatingSystem TEXT NOT NULL,
    OSReleaseSericePackVersion TEXT NOT NULL,
    ProcessorIdentity TEXT NOT NULL,
    MachineType TEXT NOT NULL,
    SystemPlatform TEXT NOT NULL,
    OSArchitecture TEXT NOT NULL,
    RebootStatus TEXT NOT NULL,
    SystemBootTime TEXT NOT NULL,
    reportGeneratedTime TEXT NOT NULL,
    reportGeneratedDate TEXT NOT NULL
    )'''

# Battery Management Table Query
batteryManagement_query = '''CREATE TABLE batteryManagement (
    BMid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    batteryPrecentage INTEGER NOT NULL, 
    powerConnectivity TEXT NOT NULL,
    remainingBatteryTime TEXT NOT NULL,
    reportGeneratedTime TEXT NOT NULL,
    reportGeneratedDate TEXT NOT NULL,
    DeviceIdentity TEXT NOT NULL,
    FOREIGN KEY (DeviceIdentity) REFERENCES DeviceInformation(DeviceName)
    )'''

# CPU Management Table Query
CPUManagement_query = '''CREATE TABLE CPUManagementStatistics(
    CPUStatusID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
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
    DeviceIdentity,
    FOREIGN KEY (DeviceIdentity) REFERENCES DeviceInformation(DeviceName)
    )'''

# Disk Management Table Queries (IF NOT EXISTS)
PartitionsManagementTable_query = '''CREATE TABLE PartitionsManagementTable (
    PMTid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    device TEXT NOT NULL,
    mount_point TEXT NOT NULL,
    file_system_type TEXT NOT NULL,
    opts TEXT NOT NULL,
    max_file TEXT NOT NULL,
    max_path TEXT NOT NULL,
    reportGeneratedTime TEXT NOT NULL,
    reportGeneratedDate TEXT NOT NULL,
    DeviceIdentity TEXT NOT NULL,
    FOREIGN KEY (DeviceIdentity) REFERENCES DeviceInformation(DeviceName)
    )'''

PartitionsAnalyzedReports_query = '''CREATE TABLE PartitionsAnalyzedReports (
    PARid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    total_gb REAL NOT NULL,
    used_gb REAL NOT NULL,
    free_gb REAL NOT NULL,
    percent_used REAL NOT NULL,
    percent_free REAL NOT NULL,
    storage_status TEXT NOT NULL,
    reportGeneratedTime TEXT NOT NULL,
    reportGeneratedDate TEXT NOT NULL,
    DeviceIdentity TEXT NOT NULL,
    Partition TEXT NOT NULL,
    FOREIGN KEY (DeviceIdentity) REFERENCES DeviceInformation(DeviceName),
    FOREIGN KEY (Partition) REFERENCES PartitionsManagementTable(device)
    )'''

# Memory Management Table Queries
virtualMemoryManagement_query = '''CREATE TABLE virtualMemoryManagement (
    VMid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    TotalMemory TEXT NOT NULL,
    AvailableMemory TEXT NOT NULL,
    UsedMemory TEXT NOT NULL,
    FreeMemory TEXT NOT NULL,
    MemoryPercentage TEXT NOT NULL,
    THRESHOLD_Status TEXT NOT NULL,
    reportGeneratedTime TEXT NOT NULL,
    reportGeneratedDate TEXT NOT NULL,
    DeviceIdentity TEXT NOT NULL,
    FOREIGN KEY (DeviceIdentity) REFERENCES DeviceInformation(DeviceName)
    )'''

swapMemoryManagement_query = '''CREATE TABLE swapMemoryManagement (
    SMid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    TotalMemory TEXT NOT NULL,
    UsedMemory TEXT NOT NULL,
    FreeMemory TEXT NOT NULL,
    MemoryPercentage TEXT NOT NULL,
    SystemInMemory TEXT NOT NULL,
    SystemOutMemory TEXT NOT NULL,
    reportGeneratedTime TEXT NOT NULL,
    reportGeneratedDate TEXT NOT NULL,
    DeviceIdentity TEXT NOT NULL,
    FOREIGN KEY (DeviceIdentity) REFERENCES DeviceInformation(DeviceName)
    )'''

# Network Management Table Query
networkManagement_query = '''CREATE TABLE networkManagement (
    NMid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    networkConnectivity TEXT NOT NULL,
    sendSpeed TEXT NOT NULL,
    downSpeed TEXT NOT NULL,
    packetsSend TEXT NOT NULL,
    packetsReceive TEXT NOT NULL,
    networkerrorIn TEXT NOT NULL,
    networkerrorOut TEXT NOT NULL,
    networkdropIn TEXT NOT NULL,
    networkdropOut TEXT NOT NULL,
    reportGeneratedTime TEXT NOT NULL,
    reportGeneratedDate TEXT NOT NULL,
    DeviceIdentity TEXT NOT NULL,
    FOREIGN KEY (DeviceIdentity) REFERENCES DeviceInformation(DeviceName)
    )'''

# User Management Table Query
UserManagement_query = '''CREATE TABLE UserManagement (
    UMid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    UserProfile TEXT NOT NULL,
    Termial TEXT NOT NULL,
    Host TEXT NOT NULL,
    StartedBootTime TEXT NOT NULL,
    ProcessID TEXT NOT NULL,
    reportGeneratedTime TEXT NOT NULL,
    reportGeneratedDate TEXT NOT NULL,
    DeviceIdentity TEXT NOT NULL,
    FOREIGN KEY (DeviceIdentity) REFERENCES DeviceInformation(DeviceName)
    )'''