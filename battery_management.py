import psutil # importing psutil library
from report_signatures import generated_report # importing date-time stamp generator library
import sys # importing sys library

# convert seconds to standard time format and return that value to main function
def convertTime(seconds): 
	minutes, seconds = divmod(seconds, 60) 
	hours, minutes = divmod(minutes, 60) 
	return '%d:%02d:%02d' % (hours, minutes, seconds)

# checking power connectivity status
def battery_status(status):
	if status == True:
		return 'Plugged..!!'
	else:
		return 'Unplugged..!!' 

def batteryManagement():
	battery = psutil.sensors_battery() # assign battery variable to psutil battery function
	print('----- Battery Usage Statistics -----\n')
	print(f"{'-'*32}\n")
	print('Battery percentage : {} %'.format(battery.percent)) # percentage of battery
	print('Power plugged in : {}'.format(battery_status(battery.power_plugged))) # power connectivity status
	print('Battery left : {}'.format(convertTime(battery.secsleft))) # remaining time of battery
	print(f"\n{'-'*32}")
	generated_report() # calling to date-time stamp function

if __name__ == "__main__":
	batteryManagement()
	sys.exit(0)
	
