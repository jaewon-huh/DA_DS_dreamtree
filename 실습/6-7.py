# 열 분리 : 하나의 열이 여러가지 정보를 갖고 있을 때 
# Y-M-D -> Y/M/D (Part 5 시계열 비슷 5-16) , 사람 이름 -> 성 / 이름 
import pandas as pd 

# 주가데이터 
df = pd.read_excel('예제/part6/주가데이터.xlsx')
print(df.head(), '\n')
print(df.dtypes, '\n')

# astype() 으로 연월일 열 문자형 데이터로 변경, split() 분리 
df['연월일'] =df['연월일'].astype('str')
dates = df['연월일'].str.split('-')    # 문자열 '2018-07-02' 를 - 기준으로 split
print(dates.head(), '\n')

# get() 으로 새로운 열 만들기 
df['연'] = dates.str.get(0)  # dates 변수의 원소 리스트의 0번째 인덱스 값 
df['월'] = dates.str.get(1)  
df['일'] = dates.str.get(2) 
print(df.head())

# str.split() -> str.get() 리스트 인덱싱 