# 데이터 프레임 '결합' : join()
# join(): 두 df의 '행 인덱스'를 기준으로 결합 (on = keys : 열 기준으로 결합)
# df1.join(df2, how ='left') : df1의 행 인덱스 기준으로 결합 
# how = outer inner left right ...

import pandas as pd 

# 디스플레이 설정 변경
pd.set_option('display.max_columns', 10)                  # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)                 # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True)   # 유니코드 사용 너비 조정

# 주식 데이터 
df1 = pd.read_excel('예제/part6/stock price.xlsx', index_col= 'id')  
df2 = pd.read_excel('예제/part6/stock valuation.xlsx', index_col = 'id')

print(df1, '\n')
print(df2, '\n')
# 데이터 프레임 결합 
df3 = df1.join(df2,how = 'left')
print(df3)

# 교집합 결합 inner
df4 = df1.join(df2, how ='inner')
print(df4)