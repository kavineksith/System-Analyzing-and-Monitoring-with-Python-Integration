# System Analyzing and Monitoring API Documentation

## Overview
This Python script provides comprehensive system monitoring capabilities, offering insights into various aspects of system performance and configuration. It covers functionalities such as battery usage statistics, CPU usage, disk management, memory usage, network statistics, process management, system information overview, and more. The script utilizes the `psutil` library for accessing system-related information and generating reports with date-time stamps.

## Features
- **Battery Usage Statistics**: Displays battery percentage, power connectivity status, and remaining battery time.
- **CPU Usage Monitoring**: Provides CPU usage percentage, processor cores count, system CPU times statistics, CPU frequencies, and CPU stats.
- **Disk Management**: Offers storage overall report, storage statistics report, and storage level checker.
- **Memory Usage Statistics**: Presents system memory usage statistics including total memory, available memory, percentage used, and swap memory statistics.
- **Network Usage Statistics**: Shows network connectivity status, network traffic analysis, and extra information about network packets.
- **Process Management**: Lists system process IDs and their names.
- **System Information Overview**: Retrieves basic system information such as operating system details, processor identity, machine type, and more.

## Script Components

### 1. Various Monitoring Functions
- **Battery Management**: Displays battery usage statistics including percentage, power status, and remaining time.
- **CPU Management**: Monitors CPU usage, CPU times, CPU frequencies, and CPU stats.
- **Disk Management**: Manages storage including storage reports and storage level checking.
- **Memory Management**: Provides memory usage statistics including system memory and swap memory.
- **Network Management**: Offers network connectivity status, network traffic analysis, and extra network information.
- **Process Management**: Lists system processes and their IDs.
- **System Information**: Retrieves basic system information such as OS details, processor identity, and more.

### 2. Utility Functions
- **ConvertTime**: Converts seconds to a standard time format.
- **BatteryStatus**: Checks power connectivity status (plugged or unplugged).
- **CheckCpu**: Checks CPU load and returns status (normal or too high).

### 3. Main Functionality
- Orchestrates the execution of monitoring functions and report generation.
- Provides an entry point for executing the script.

## Dependencies
- Python 3.x
- `psutil` library for accessing system-related information
- `os` library for system-specific functions
- `platform` library for accessing system platform information
- `datetime` library for date-time operations
- `socket` library for network-related operations
- `report_signatures` module for generating reports with date-time stamps

## Usage
1. **Execution**: Run the script using Python 3.x.
2. **Monitoring**: View the output to monitor various system aspects such as battery usage, CPU usage, memory usage, network statistics, etc.
3. **Reports**: Reports are generated with date-time stamps for reference.

## Conclusion
The System Monitoring script offers a comprehensive solution for monitoring various aspects of system performance and configuration. With its extensive functionalities and user-friendly interface, it serves as a valuable tool for system administrators, developers, and enthusiasts to gain insights into system behavior and make informed decisions regarding system management and optimization.

*with seamless integration with databases and APIs for tailored solutions that can be upgradable or customizable to meet user requirements.*

## **License**
This project is licensed under the MIT License. See the [LICENSE](https://github.com/kavineksith/System-Analyzing-and-Monitoring-API/blob/main/LICENSE) file for details.

### **Disclaimer:**
Kindly note that this project is developed solely for educational purposes, not intended for industrial use, as its sole intention lies within the realm of education. We emphatically underscore that this endeavor is not sanctioned for industrial application. It is imperative to bear in mind that any utilization of this project for commercial endeavors falls outside the intended scope and responsibility of its creators. Thus, we explicitly disclaim any liability or accountability for such usage.
