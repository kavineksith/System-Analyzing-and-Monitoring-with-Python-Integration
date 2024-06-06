import psutil
import socket
from report_signatures import generated_report
import sys

def network_connectivity():
    try:
        socket.gethostbyname('www.google.com')
        print("PC is conntected to internet.")
    except:
        print("PC isn't conntected to internet.")

def network_traffic():
    network = psutil.net_io_counters()
    print(f'Send : {network.bytes_sent / (1024**2):.2f} Mbps | Received : {network.bytes_recv / (1024**2):.2f} Mbps')
    print('Extra Information about Network')
    print(f'Packets Sent : {network.packets_sent} | Packet Received : {network.packets_recv}')
    print(f'ErrorIn : {network.errin} | ErrorOut : {network.errout} | DropIn : {network.dropin} | DropOut : {network.dropout}')

def networkManagement():
    print('----- Network Usage Statistics -----\n')
    print(' -- Network Connectivty -- ')
    network_connectivity()
    print('\n -- Network Traffic Analysis -- ')
    network_traffic()
    generated_report()

if __name__ == "__main__":
    networkManagement()
    sys.exit(0)