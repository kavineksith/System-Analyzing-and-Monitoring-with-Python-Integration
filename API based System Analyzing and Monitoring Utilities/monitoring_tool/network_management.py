import psutil, socket, sys # importing psutil, socket and sys library
from report_signatures import generated_report # importing date-time stamp generator library
from insert_queries import valuesManagement # importing sql query executor custom function
from deviceIdentity import deviceIdentify # getting device_name of user device

def network_connectivity():
    try:
        socket.gethostbyname('www.google.com')
        return 'Conntected.'
    except:
        return 'Not conntected.'

def networkManagement():
    network = psutil.net_io_counters()

    network_sendSpeed = network.bytes_sent / (1024**2)
    network_downSpeed = network.bytes_recv / (1024**2)
    packets_send = network.packets_sent
    packets_received = network.packets_recv
    network_errorIn = network.errin
    network_errorOut = network.errout
    network_dropIn = network.dropin
    network_dropOut = network.dropout
    timeStamp = generated_report()[0]
    dateStamp = generated_report()[1]

    NM_query = '''INSERT INTO networkManagement(
        networkConnectivity,
        sendSpeed,
        downSpeed,
        packetsSend,
        packetsReceive,
        networkerrorIn,
        networkerrorOut,
        networkdropIn,
        networkdropOut,
        reportGeneratedTime,
        reportGeneratedDate,
        DeviceIdentity
        )VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'''
    
    NM_values = [network_connectivity(), network_sendSpeed, network_downSpeed, packets_send, packets_received, network_errorIn, network_errorOut, network_dropIn, network_dropOut, timeStamp, dateStamp, deviceIdentify()]

    valuesManagement(NM_query, NM_values)

if __name__ == "__main__":
    networkManagement()
    sys.exit(0)