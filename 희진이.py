import datetime

class day_cal:
    def __init__(self):
        self.day = datetime.datetime.now()

    def calculator(self, end_day):
        dt_today = self.day
        dt_end = datetime.datetime(int(end_day.split('-')[0]), int(end_day.split('-')[1]), int(end_day.split('-')[2]))
        td = dt_end - dt_today
        return td.days