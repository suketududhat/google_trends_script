import pandas as pd
from pytrends.request import TrendReq
import plotly.express as px

pytrends = TrendReq(hl='en-US', tz=360)

# build payload

kw_list = ["machine learning"]  # list of keywords to get data

pytrends.build_payload(kw_list, cat=0, timeframe='2021-01-01 2021-12-31')

# 1 Interest over Time
data = pytrends.interest_over_time()
data = data.reset_index()

# fig = px.line(data, x="date", y=['machine learning'], title='Keyword Web Search Interest Over Time')
# fig.show()

by_region = pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=True)
# print(by_region.head(10))
print(data.head())

