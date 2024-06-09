from datetime import date
import time

# getting the processing time
def time_stamp():
    time_now = time.localtime()
    current_time = time.strftime('%H:%M:%S', time_now)
    return current_time

# getting the processing data
def date_stamp():
    date_today = date.today()
    current_day = date_today.strftime('%d/%m/%Y')
    return current_day

# displaying the processed time and data
def generated_report():
    # print(f'Generated Time & Date : {time_stamp()} | {date_stamp()}')
    return (time_stamp(),date_stamp())

if __name__ == "__main__":
    generated_report()