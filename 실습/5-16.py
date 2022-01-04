# 시계열 데이터 활용 
# 날짜 데이터 분리 : 연 -월 -일 -> 분리 

import pandas as pd 
# 주식 데이터 
df = pd.read_csv('예제/part5/stock-data.csv')
# 문자열 날짜 데이터 -> timestamp 
df['new_Date'] = pd.to_datetime(df['Date']) 
print(df.head())
print('\n')

# 추출 dt.year / dt.month / dt.day
df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df.head())
print('\n')

# timestamp -> period로 변환 , 연-월 or 연도 추출
df['Date_yr'] = df['new_Date'].dt.to_period(freq='A') 
df['Date_m'] = df['new_Date'].dt.to_period(freq='M') 
print(df.head())

# 원하는 열을 행 인덱스로 지정 'Date_m'
df.set_index('Date_m', inplace= True)
print(df.head())