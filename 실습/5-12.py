# 시계열 데이터 
# Timestamp : 시점 / Period : 기간

# 문자열을 Timestamp로 변환 : pd.to_datetime() 
import pandas as pd 
# 주식 데이터 
df = pd.read_csv('예제/part5/stock-data.csv')

print(df.head())
print(df.info()) # date : object 타입
print('\n')
# pd.to_datetime()
df['new_Date'] = pd.to_datetime(df['Date']) 
print(df.head())
print('\n')
print(df.info())
print('\n')
print(type(df['new_Date'][0]))
print('\n')
# 'new_Date' 열을 행인덱스로 설정하고 Date열 삭제 
df.set_index('new_Date', inplace= True)
df.drop('Date', axis =1, inplace =True)

print(df.head())
print('\n')
print(df.info())