from battery_management import BatteryManager
from cpu_management import CPUManager
from disk_management import DiskManager
from memory_management import MemoryManager
from network_management import NetworkManager
from process_management import ProcessManager
from system_infoAnalyzer import SystemInformation
from terminal_clearance import ScreenManager
from methods import control_result_to_json
import sys


class systemAnalyzer:
    @staticmethod
    def all_in_one():
        try:
            cpu_status = CPUManager().monitor_cpu()
            process_status = ProcessManager().manage_processes()
            memory_status = MemoryManager().memory_statistics()
            disk_status = DiskManager().manage_disk()
            network_status = NetworkManager().network_report()
            system_status = SystemInformation().system_info()
            battery_status = BatteryManager().batteryManagement()

            status_list = [cpu_status, process_status, memory_status, disk_status, network_status, system_status,
                           battery_status]

            return status_list

        except Exception as e:
            print(f"Error in generating all-in-one report: {e}")
            return None  # Return None or handle the error as appropriate in this application

    @staticmethod
    def once_status_one_report(token):
        try:
            match token:
                case 0:
                    ScreenManager().clear_screen()
                    systemAnalyzer().reportWizarder()  # Recursively call the method to prompt again
                case 1:
                    return CPUManager().monitor_cpu()
                case 2:
                    return ProcessManager().manage_processes()
                case 3:
                    return MemoryManager().memory_statistics()
                case 4:
                    return DiskManager().manage_disk()
                case 5:
                    return NetworkManager().network_report()
                case 6:
                    return SystemInformation().system_info()
                case 7:
                    return BatteryManager().batteryManagement()
                case _:
                    print('Invalid selection. Please enter a number between 0 and 7.')
                    systemAnalyzer().reportWizarder()  # Recursively call the method to prompt again
        except Exception as e:
            return f'Error executing report: {e}'

    @staticmethod
    def reportWizarder():
        try:
            favor = input('What kind of report do you need today? ').lower()
            if favor.replace(' ', '_') == 'single_report':
                while True:
                    try:
                        report_id = int(input('Enter Report ID (1-7, 0 to clear screen): '))
                        if report_id < 0 or report_id > 7:
                            print('Please enter a number between 1 and 7, or 0 to clear the screen.')
                        else:
                            break  # Exit the loop if a valid report ID is entered
                    except ValueError:
                        print('Invalid input. Please enter a valid number.')

                if report_id == 0:
                    # Clearing the screen and recursively call the method to prompt again
                    ScreenManager().clear_screen()
                    systemAnalyzer().reportWizarder()
                else:
                    statistics = systemAnalyzer().once_status_one_report(report_id)
                    if statistics is None:
                        print(f"Failed to generate report with Report ID {report_id}.")
                    else:
                        control_result_to_json(statistics)
                        print(f"Single report with Report ID {report_id} has been successfully generated and saved.")

            elif favor.replace(' ', '_') == 'all_in_one':
                statistics = systemAnalyzer.all_in_one()
                control_result_to_json(statistics)
                print("All-in-one report has been successfully generated and saved.")

            else:
                print('Invalid choice. Please choose "single_report" or "all_in_one".')
                systemAnalyzer().reportWizarder()  # Recursively call the method to prompt again

        except KeyboardInterrupt:
            print("\nProcess interrupted by the user. Exiting...")
            sys.exit(1)  # Exit with error status

        except ValueError as ve:
            print(f"ValueError: {ve}")
            sys.exit(1)  # Exit with error status

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)  # Exit with error status


if __name__ == "__main__":
    systemAnalyzer().reportWizarder()
    sys.exit(0)
