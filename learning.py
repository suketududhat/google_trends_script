import os
import time
import pandas as pd
from pytrends.request import TrendReq
# import plotly.express as px

pytrends = TrendReq(hl='en-US', tz=360)

# build payload
df = pd.read_excel(r'C:\Users\suk2d\PycharmProjects\google_trends_script\data\interest_by_region.xlsx')
df_geoIndex = pd.read_excel(r'C:\Users\suk2d\PycharmProjects\google_trends_script\data\geocode_index.xlsx')
dates = []
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
        end_date = str(start) + '-12-31'
        timeframe = str(start_date + ' ' + end_date)
        pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='US')
        by_region = pytrends.interest_by_region(resolution='REGION', inc_low_vol=True, inc_geo_code=True)
        by_region.geoCode = by_region.geoCode.str[-2:]
        # by_region = by_region.reset_index().set_index(['geoName', 'geoCode'])  # removes index (state, code)
        year_start = [start]
        df_year = pd.DataFrame(year_start)
        df_geoIndex['Year'] = pd.concat([df_year]*51, ignore_index=True)
        # df_year = pd.concat([df_year]*51, ignore_index=True)
        # df_year = pd.concat([df_year, df_geoIndex])
        # print(df_geoIndex)
        df1 = pd.concat([df_geoIndex, by_region])
        df2 = pd.concat([df1, by_region], axis=0)  # axis=1 concatenates as columns; 0 concatenates as rows
        print(timeframe)
        start += 1
        time.sleep(5)
else:
    print('False')
df2.to_excel(r'C:\Users\suk2d\PycharmProjects\google_trends_script\data\interest_by_region.xlsx', index=False)
os.system(r'start "excel" "C:\Users\suk2d\PycharmProjects\google_trends_script\data\interest_by_region.xlsx"')

# pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='US')

# 1 Interest over Time
# data = pytrends.interest_over_time()
# data = data.reset_index()
# print(data.head())

# fig = px.line(data, x="date", y=['machine learning'], title='Keyword Web Search Interest Over Time')
# fig.show()

#
# print(by_region.head())
