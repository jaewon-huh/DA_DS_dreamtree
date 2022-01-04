# 날짜 인덱스 활용 
# timestamp 열 -> 행 인덱스 지정 :  DatetimeIndex 속성으로 변환됨
# Period 열 -> 행 인덱스 지정 :  PeriodIndex 속성으로 변환됨

import pandas as pd 
# 주식 데이터 
df = pd.read_csv('예제/part5/stock-data.csv')
# 문자열 날짜 데이터 -> timestamp 
df['new_Date'] = pd.to_datetime(df['Date']) 
df.set_index('new_Date',inplace =True)

print(df.head())
print('\n')
print(df.index)

# 날짜 인덱스 활용하여 데이터 선택
df_y = df['2018']  # df 중 인덱스 2018년 데이터
print(df_y.head())
print('\n')

df_ym = df.loc['2018-07']  # 2018-07 인 행 
print(df_ym)
print('\n')
df_ym_cols = df.loc['2018-07' , 'Start' : 'High']  # 2018-07 인 행 , start : high 열 
print(df_ym_cols)
print('\n')

df_ymd = df['2018-07-02']  # 인덱스가 '2018-07-02'
print(df_ymd)
print('\n')

df_ymd_range = df['2018-06-20':'2018-06-25']    # 날짜 범위 지정
print(df_ymd_range)
print('\n')

# 시간 간격 계산. 최근 180일 ~ 189일 사이의 값들만 선택하기
today = pd.to_datetime('2018-12-25') # 기준일
df['time_delta'] = today - df.index  # 날짜 차이 ``                                                                                                                                                                                                                                                                                                                             
df.set_index('time_delta', inplace= True) # 행 인덱스 설정 
df_180 = df['180 days' : '189 days'] 
print(df_180)