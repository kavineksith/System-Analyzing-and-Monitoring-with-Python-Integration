import psutil # importing psutil library
import sys # importing sys library
from report_signatures import generated_report # importing date-time stamp generator library
from insert_queries import valuesManagement # importing sql query executor custom function
from deviceIdentity import deviceIdentify # getting device_name of user device

# convert seconds to standard time format and return that value to main function
def convertTime(seconds): 
	minutes, seconds = divmod(seconds, 60) 
	hours, minutes = divmod(minutes, 60) 
	return '%d:%02d:%02d' % (hours, minutes, seconds)

# checking power connectivity status
def battery_status(status):
	if status == True:
		return 'Plugged'
	else:
		return 'Unplugged' 

def batteryManagement():
	battery = psutil.sensors_battery() # assign battery variable to psutil battery function
	batteryPercentage = battery.percent # percentage of battery
	batteryStatus = (battery_status(battery.power_plugged)) # power connectivity status
	remainingTime = convertTime(battery.secsleft) # remaining time of battery
	timeStamp = generated_report()[0] # calling to time stamp function
	dateStamp = generated_report()[1] # calling to date stamp function

	BM_insert_query = '''INSERT INTO batteryManagement(
        batteryPrecentage,
        powerConnectivity,
        remainingBatteryTime,
        reportGeneratedTime,
        reportGeneratedDate,
        DeviceIdentity
    ) VALUES (?,?,?,?,?,?)'''
	
	BM_values_query = [batteryPercentage, batteryStatus, remainingTime, timeStamp, dateStamp, deviceIdentify()]


	valuesManagement(BM_insert_query, BM_values_query)

if __name__ == "__main__":
	batteryManagement()
	sys.exit(0)