import psutil
import socket
from report_signatures import TimeStampGenerator
import sys


class NetworkManager:
    def __init__(self):
        pass

    # Function to check network connectivity
    def check_network_connectivity(self):
        try:
            socket.gethostbyname('www.google.com')
            print("PC is connected to the internet.")
        except socket.gaierror:
            print("PC isn't connected to the internet.")
        finally:
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).close()

    # Function to monitor network traffic
    def monitor_network_traffic(self):
        try:
            network = psutil.net_io_counters()
            print(
                f'Send : {network.bytes_sent / (1024 ** 2):.2f} Mbps | Received : {network.bytes_recv / (1024 ** 2):.2f} Mbps')
            print('Extra Information about Network')
            print(f'Packets Sent : {network.packets_sent} | Packet Received : {network.packets_recv}')
            print(
                f'ErrorIn : {network.errin} | ErrorOut : {network.errout} | DropIn : {network.dropin} | DropOut : {network.dropout}')
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    # Function to manage network statistics
    def manage_network(self):
        try:
            print('----- Network Usage Statistics -----\n')
            print(' -- Network Connectivity -- ')
            self.check_network_connectivity()
            print('\n -- Network Traffic Analysis -- ')
            self.monitor_network_traffic()
            TimeStampGenerator().generate_report()
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)


if __name__ == "__main__":
    network_manager = NetworkManager()
    network_manager.manage_network()
    sys.exit(0)
