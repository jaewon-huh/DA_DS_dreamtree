# 시리즈 인덱스 
# 인덱스 구조 : Index 인덱스 이름/ 정수형 위치 인덱스 - 데이터 값 values
import pandas as pd 

list_data = ['2021-12-29', 3.14 , 'ABC', 100 , True]
sr = pd.Series(list_data)
print(sr)
print('\n')
# idx / val 
idx = sr.index
val = sr.values
print(idx)
print(val)