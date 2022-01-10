# merge() : 두 df 병합 , 기준 열 or index = 'key'
# pd.merge(df_left, df_right, how = 'inner', on =None (기본값))
# on = None : 두 df 에 공통으로 속하는 모든열을 기준(키)로 병합  - 키
# how = 'inner' 기준이 되는 열의 데이터가 양 df의 교집합일 경우에만 추출 - 기준 열의 값

import pandas as pd 
 
# 디스플레이 설정 변경
pd.set_option('display.max_columns', 10)                  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)                 # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)   # 유니코드 사용 너비 조정

# 주식 데이터를 가져와서 데이터프레임 만들기
df1 = pd.read_excel('예제/part6/stock price.xlsx', engine= 'openpyxl')  
df2 = pd.read_excel('예제/part6/stock valuation.xlsx', engine= 'openpyxl')

print(df1,'\n')  #주가 정보 
print(df2)       #주식 가치 평가 지표 

# 병합 merge()
merge_inner = pd.merge(df1, df2)  
print(merge_inner)  # id 기준 , 공통 데이터 (교집합)들만 inner 

# 병합 merge() : id 기준 , 합집합 how = 'outer' : id 열 데이터 전부 
merge_outer = pd.merge(df1,df2, on = 'id', how = 'outer')
print(merge_outer)

#how = 'left' : 왼쪽 df 의 키 열에 속하는 데이터 값을 기준으로 병합 'stock_name'
# left_on / right_on : df에 각각 다르게 키 지정 -> 기준키 아닌 공통 열(id) -> id_x / id_y 로 표시됨
merge_left = pd.merge(df1,df2, how= 'left',
                      left_on='stock_name', right_on='name')
print(merge_left)

# how = 'left' : 오른쪽 df 키 'name' 기준 
merge_right = pd.merge(df1,df2, how= 'right',
                      left_on='stock_name', right_on='name')
print(merge_right)


# merge() & 불린 인덱싱 
# 주가 50000인 종목 찾고, 해당 종목의 밸류에이션 지표 
price = df1['price'] < 50000
price = df1[price]
print(price.head(), '\n')

value = pd.merge(price,df2)  # id 기준 , id 값 교집합 
print(value)