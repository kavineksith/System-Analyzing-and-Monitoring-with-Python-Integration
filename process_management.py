import psutil
from report_signatures import generated_report
import sys

def processManagement():
    print('----- System Processes Statistics -----\n')
    processList = psutil.pids()
    print(f"Process IDs = {processList}")

    for process in psutil.process_iter():
        try:
            processInfo = process.as_dict(attrs=['pid', 'name'])
        except psutil.NoSuchProcess:
            pass
        else:
            print(processInfo)
    
    generated_report()

if __name__ == "__main__":
    processManagement()
    sys.exit(0)