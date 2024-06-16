from datetime import datetime


class TimeStampGenerator:
    def __init__(self):
        pass

    @staticmethod
    def current_time():
        return datetime.now().strftime('%H:%M:%S')

    @staticmethod
    def current_date():
        return datetime.now().strftime('%d/%m/%Y')

    @staticmethod
    def generate_report():
        current_time = TimeStampGenerator.current_time()
        current_date = TimeStampGenerator.current_date()
        return f'{current_time} | {current_date}'

    @staticmethod
    # # convert seconds to standard time format and return that value
    def convertTime(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return '%d:%02d:%02d' % (hours, minutes, seconds)
