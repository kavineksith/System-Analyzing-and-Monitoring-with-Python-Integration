import psutil
from report_signatures import TimeStampGenerator
import sys


class MemoryManager:
    def __init__(self):
        pass

    # Function to retrieve and print memory statistics
    def memory_statistics(self):
        try:
            # System memory usage statistics
            v_memory = psutil.virtual_memory()
            print(
                f'Total : {v_memory.total / (1024 ** 3):.2f} GB, Available : {v_memory.available / (1024 ** 3):.2f} GB, Percentage : {v_memory.percent} %, Used : {v_memory.used / (1024 ** 3):.2f} GB, Free : {v_memory.free / (1024 ** 3):.2f} GB')

            THRESHOLD = 100 * 1024 * 1024  # Compulsory THRESHOLD value should be 100MB
            if v_memory.available <= THRESHOLD:
                print("warning, available memory below threshold.")

            # System swap memory statistics
            s_memory = psutil.swap_memory()
            print(
                f'Total : {s_memory.total / (1024 ** 3):.2f} GB, Used : {s_memory.used / (1024 ** 3):.2f} GB, Free : {s_memory.free / (1024 ** 3):.2f} GB, Percentage : {s_memory.percent} %, System IN : {s_memory.sin / (1024 ** 3):.2f} GB, System OUT : {s_memory.sout / (1024 ** 3):.2f} GB')
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    # Function to manage memory statistics
    def manage_memory(self):
        try:
            print('----- Memory Usage Statistics -----\n')
            self.memory_statistics()
            TimeStampGenerator().generate_report()
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    memory_manager = MemoryManager()
    memory_manager.manage_memory()
    sys.exit(0)
