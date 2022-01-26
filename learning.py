import os
import time
import pandas as pd
from pytrends.request import TrendReq
# import plotly.express as px

pytrends = TrendReq(hl='en-US', tz=360)

# build payload
# df = pd.read_excel(r'.\data\interest_by_region.xlsx')
df_geoIndex = pd.read_excel(r'.\data\geocode_index.xlsx')
df = pd.read_excel(r'.\data\interest_by_region.xlsx')
# writer = pd.ExcelWriter(r'.\data\interest_by_region.xlsx', engine='xlsxwriter')
dates = []
kw_list = ['Intel', 'AMD']  # list of keywords to get data
# timeframe = input('Enter range of years (YYYY-YYYY): ')
input_timeframe = [2015, 2016]
# timeframe = timeframe.split(sep='-')
# start_date = timeframe[0] + '-01-01'
# end_date = timeframe[1] + '-12-31'
# timeframe = start_date + ' ' + end_date


def yearly_trends_fetch(timeframe):
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
