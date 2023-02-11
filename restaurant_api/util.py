import datetime


class CustomUtils:
    @staticmethod
    def daypart_comparison(user_time, begin_time, end_time):
        begin_time = datetime.datetime.strptime(begin_time, "%H:%M")
        end_time = datetime.datetime.strptime(end_time, "%H:%M")
        user_time = datetime.datetime.strptime(user_time, "%H:%M")
        return True if begin_time < user_time < end_time else False
