import os
import time
import pandas as pd
from pytrends.request import TrendReq
# import plotly.express as px

pytrends = TrendReq(hl='en-US', tz=360)

# build payload
<<<<<<< HEAD
# df = pd.read_excel(r'.\data\interest_by_region.xlsx')
df_geoIndex = pd.read_excel(r'.\data\geocode_index.xlsx')
=======
df_geoIndex = pd.read_excel(r'.\data\geocode_index.xlsx')
df = pd.read_excel(r'.\data\interest_by_region.xlsx')
# writer = pd.ExcelWriter(r'.\data\interest_by_region.xlsx', engine='xlsxwriter')
>>>>>>> 04d17ad (Working on how to save multiple years data and eventually combine into one dataframe)
dates = []
kw_list = ['Intel', 'AMD']  # list of keywords to get data
# timeframe = input('Enter range of years (YYYY-YYYY): ')
input_timeframe = [2015, 2016]
# timeframe = timeframe.split(sep='-')
# start_date = timeframe[0] + '-01-01'
# end_date = timeframe[1] + '-12-31'
# timeframe = start_date + ' ' + end_date

<<<<<<< HEAD

def yearly_trends_fetch(timeframe):
    if timeframe[0] != timeframe[1]:
        start = int(timeframe[0])
        end = int(timeframe[1])
        while start <= end:
            # result = []
            # by_region = []
            start_date = str(start) + '-01-01'
            end_date = str(start) + '-12-31'
            timeframe = str(start_date + ' ' + end_date)
            pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='US')
            by_region = pytrends.interest_by_region(resolution='REGION', inc_low_vol=True, inc_geo_code=True)
            by_region.geoCode = by_region.geoCode.str[-2:]
            year_start = [start]
            df_year = pd.DataFrame(year_start)
            df_geoIndex['Year'] = pd.concat([df_year] * 51, ignore_index=True)  # left table for merge
            merge_result = pd.merge(df_geoIndex, by_region, on='geoCode')
            print(merge_result)
            print(timeframe)
            start += 1
            time.sleep(5)
            return merge_result
    else:
        print('False')


def concatenating_yearly_fetch():
    yearly_trends_fetch(input_timeframe)


concatenating_yearly_fetch()

        # if start != start_compare:
        #     result = pd.concat([by_region, merge_result], axis=0)  # axis=1 concatenates as columns;
        #     # 0 concatenates as rows
        # # print(result)




# df2.to_excel(r'.\data\interest_by_region.xlsx', index=False)
# os.system(r'start "excel" ".\data\interest_by_region.xlsx"')
=======
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
        df_year = pd.DataFrame([start])
        df_geoIndex['Year'] = pd.concat([df_year]*51, ignore_index=True)
        by_region = pd.merge(df_geoIndex, by_region, on='geoCode')
        by_region = pd.concat([df, by_region], axis=0, ignore_index=False)
        by_region.to_excel(r'.\data\interest_by_region.xlsx', index=False)
        print(timeframe)
        start += 1
        time.sleep(5)
else:
    print('False')

# by_region.to_excel(writer, index=False, sheet_name=str(start))
# writer.save()
os.system(r'start "excel" ".\data\interest_by_region.xlsx"')
>>>>>>> 04d17ad (Working on how to save multiple years data and eventually combine into one dataframe)

# pytrends.build_payload(kw_list, cat=0, timeframe=timeframe, geo='US')

# 1 Interest over Time
# data = pytrends.interest_over_time()
# data = data.reset_index()
# print(data.head())

# fig = px.line(data, x="date", y=['machine learning'], title='Keyword Web Search Interest Over Time')
# fig.show()

#
# print(by_region.head())
