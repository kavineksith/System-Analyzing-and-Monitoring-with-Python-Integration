import json
import psutil
import socket
import sys
from report_signatures import TimeStampGenerator


class NetworkManager:
    @staticmethod
    # Function to check localhost connectivity
    def check_localhost_connectivity():
        try:
            socket.gethostbyname('127.0.0.1')
            status = "PC is connected to localhost."
        except socket.gaierror:
            status = "PC isn't connected to localhost."
        finally:
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).close()

        return status

    @staticmethod
    # Function to check network connectivity
    def check_network_connectivity():
        try:
            socket.gethostbyname('www.google.com')
            status = "PC is connected to the internet."
        except socket.gaierror:
            status = "PC isn't connected to the internet."
        finally:
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).close()

        return status

    @staticmethod
    # Function to monitor network traffic
    def monitor_network_traffic():
        try:
            network = psutil.net_io_counters()
            return {
                'Network Traffic Information': {
                    'Send': f'{network.bytes_sent / (1024 ** 2):.2f} Mbps',
                    'Received': f'{network.bytes_recv / (1024 ** 2):.2f} Mbps',
                },
                'Extra Information': {
                    'Packets Sent': f'{network.packets_sent}',
                    'Packet Received': f'{network.packets_recv}',
                    'ErrorIn': f'{network.errin}',
                    'ErrorOut': f'{network.errout}',
                    'DropIn': f'{network.dropin}',
                    'DropOut': f'{network.dropout}'
                }
            }
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    @staticmethod
    # Function to manage network statistics
    def network_report():
        try:
            # Network Usage Statistics
            localhost_connectivity = NetworkManager().check_localhost_connectivity()
            network_connectivity = NetworkManager().check_network_connectivity()
            network_traffic = NetworkManager().monitor_network_traffic()

            statistics = {
                'Network Usage Statistics': {
                    'Localhost Connectivity': localhost_connectivity,
                    'Network Connectivity': network_connectivity,
                    'Network Traffic': network_traffic,
                    'Generated Time & Date': f'{TimeStampGenerator().generate_report()}'
                }
            }

            result = json.dumps(statistics, indent=4)
            json_output = json.loads(result)
            return json_output  # Return the JSON output as a string
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
