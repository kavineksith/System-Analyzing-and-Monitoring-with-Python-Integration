import psutil
from report_signatures import TimeStampGenerator
import sys


class BatteryManager:
    def __init__(self):
        self.battery = None

    # Function to determine power connectivity status
    def battery_status(self, status):
        return 'Plugged..!!' if status else 'Unplugged..!!'

    # Function to retrieve battery information
    def get_battery_info(self):
        try:
            self.battery = psutil.sensors_battery()  # Attempt to retrieve battery information
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)  # Exit program with error code 1 if battery retrieval fails

    # Function to print battery statistics
    def print_battery_stats(self):
        if not self.battery:
            print("Error: Failed to retrieve battery information.")
            sys.exit(1)  # Exit program with error code 1 if battery information is not available

        print('----- Battery Usage Statistics -----\n')
        print(f"{'-' * 32}\n")
        print('Battery percentage : {} %'.format(self.battery.percent))
        print('Power plugged in : {}'.format(self.battery_status(self.battery.power_plugged)))

        if self.battery.power_plugged:
            print('Charging status: {}'.format("Charging" if self.battery.percent < 100 else "Fully Charged"))
        else:
            try:
                status = TimeStampGenerator().convertTime(self.battery.secsleft)
                print(f'Battery left: {status}')
            except Exception as e:
                print(f"Error: {e}")  # Print error message if timestamp conversion fails

        print(f"\n{'-' * 32}")
        TimeStampGenerator().generate_report()  # Generate timestamp report


if __name__ == "__main__":
    battery_manager = BatteryManager()  # Create BatteryManager object
    battery_manager.get_battery_info()  # Retrieve battery information
    battery_manager.print_battery_stats()  # Print battery statistics
    sys.exit(0)  # Exit program with success code 0
