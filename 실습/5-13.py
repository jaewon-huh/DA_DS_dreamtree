# Timestamp 를 Period로 변환 : to_period(freq ='')
import pandas as pd 
dates = ['2019-01-01', '2020-03-01', '2021-06-01']

# 문자형 데이터를 timestamp로 변환
ts_dates = pd.to_datetime(dates)
print(ts_dates)
print('\n')

# timestamp -> Period 로 변환
pr_day= ts_dates.to_period(freq ='D')
print(pr_day)
pr_month= ts_dates.to_period(freq ='M')
print(pr_month)
pr_year= ts_dates.to_period(freq ='A')
print(pr_year)

# freq 옵션 : D / W / M(월말) ,MS(월초)/ Q(분기말), QS(분기초)/ A, AS / H / T / S ...
