import psutil
from report_signatures import generated_report
import sys

def memoryStatistics():
    # System memory usage statistics
    v_memory = psutil.virtual_memory()
    print(f'Total : {v_memory.total / (1024 ** 3):.2f} GB, Available : {v_memory.available / (1024 ** 3):.2f} GB, Prcent : {v_memory.percent} %, Used : {v_memory.used / (1024 ** 3):.2f} GB, Free : {v_memory.free / (1024 ** 3):.2f} GB')

    THRESHOLD = 100 * 1024 * 1024  # Compulsory THRESHOLD value should be 100MB
    if v_memory.available <= THRESHOLD:
        print("warning, available memory below threshold.")

    # System swap memory statistics
    s_memory = psutil.swap_memory()
    print(f'Total : {s_memory.total / (1024 ** 3):.2f} GB, Used : {s_memory.used / (1024 ** 3):.2f} GB, Free : {s_memory.free / (1024 ** 3):.2f} GB, Prcent : {s_memory.percent} %, System IN : {s_memory.sin / (1024 ** 3):.2f} GB, System OUT : {s_memory.sout / (1024 ** 3):.2f} GB')

def memoryManagement():
    print('----- Memory Usage Statistics -----\n')
    memoryStatistics()
    generated_report()

if __name__ == "__main__":
    memoryManagement()
    sys.exit(0)