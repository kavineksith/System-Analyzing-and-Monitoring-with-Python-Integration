import sys # importing sys library
from report_signatures import generated_report # importing date-time stamp generator library
from insert_queries import valuesManagement # importing sql query executor custom function
from deviceIdentity import deviceIdentify # getting device_name of user device

# Store input parameters
input_labels = ['Cylinders', 'Heads', 'Sectors per Track', 'bytes per Sector']
# Store user given values for corresponding parameters
input_values = []

# Check user input validation
def inputValidator(value):
    if type(value) != int:
        print('please insert numeric data only.')
        status = False
    elif type(value) == int:
        status = True
    else:
        print('please insert the value for inputs.')
        status = False

    return status

# calculating hard disk's storage
def DiskStorageCalculator():
    for label in input_labels:
        value = int(input(f'No. of {label} : '))
        if inputValidator(value) == False:
            sys.exit(1)
        else:
            input_values.append(value)

    total = 1
    for value in input_values:
        total *= value

    return total

def DiskStoragePreview():
    reading_value = (DiskStorageCalculator() / 1024 ** 3) # convert byte value into gigabyte value
    print(f'Total Size of the Disk : {reading_value:.2f} GigaBytes')

if __name__ == "__main__":
    DiskStoragePreview()
    sys.exit(0)