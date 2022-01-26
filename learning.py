import time
import pandas as pd
from pytrends.request import TrendReq
# import plotly.express as px

pytrends = TrendReq(hl='en-US', tz=360)

# build payload
df = pd.read_excel(r'C:\Users\suk2d\PycharmProjects\google_trends_script\data\interest_by_region.xlsx')
kw_list = ['Intel', 'AMD']  # list of keywords to get data
# timeframe = input('Enter range of years (YYYY-YYYY): ')
timeframe = [2015, 2016]
# timeframe = timeframe.split(sep='-')
# start_date = timeframe[0] + '-01-01'
# end_date = timeframe[1] + '-12-31'
# timeframe = start_date + ' ' + end_date

if timeframe[0] != timeframe[1]:
    start = int(timeframe[0])
    end = int(timeframe[1])
    while start <= end:
        start_date = str(start) + '-01-01'
        end_date = str(start + 1) + '-12-31'
        timeframe = str(start_date + ' ' + end_date)
        pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='US')
        by_region = pytrends.interest_by_region(resolution='REGION', inc_low_vol=True, inc_geo_code=True)
        by_region.geoCode = by_region.geoCode.str[-2:]
        df = pd.concat([df, by_region], axis=1)
        print(timeframe)
        start += 1
        time.sleep(5)
else:
    print('False')
df.to_excel(r'C:\Users\suk2d\PycharmProjects\google_trends_script\data\interest_by_region.xlsx', index=False)

# pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='US')

# 1 Interest over Time
# data = pytrends.interest_over_time()
# data = data.reset_index()
# print(data.head())

# fig = px.line(data, x="date", y=['machine learning'], title='Keyword Web Search Interest Over Time')
# fig.show()

#
# print(by_region.head())

