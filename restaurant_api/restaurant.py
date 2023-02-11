from io import BytesIO

from flask import Flask, request, make_response
from datetime import datetime
import csv
import pandas as pd

data = """item_name | timestring
dosa | 17:00-21:00,7:00-10:00,10:45-12:0
vada | 18:45-22:00,6:30-11:00,09:55-13:0"""

def item_availability():
    if request.method == 'POST':
        df = pd.read_csv(data, delimiter='|')
        # print(df)
        response_dict = {}
        # user_time = request.get_cookie('time')
        user_time = datetime.now().strftime('%H:%M')
        # for i in range(len(df)):
        #     for j in df.iloc[i, 0]:
        #         times = df.iloc[i,1].split(',')
        #         for time in times:
        #             if user_time > time.split('-')[0] and user_time < time.split('-')[1]:
        #                 response_dict[df.iloc[i, 0]] = 'available'
        #             else:
        #                 response_dict[df.iloc[i, 0]] = 'not_available'
        # print(response_dict.items())
        return "Done"
    else:
        return "Wrong Method"
