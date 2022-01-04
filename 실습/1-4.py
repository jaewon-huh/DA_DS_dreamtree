# 데이터 프레임 
# 시리즈- 열벡터 / df = 2차원 벡터, 행렬(matrix)
import pandas as pd 
dict_data = {'c0':[1,2,3], 'c1' :[4,5,6],'c2' :[7,8,9],'c3' :[10,11,12]}
# 딕 -> df  변환 
df = pd.DataFrame(dict_data)
print(type(df))
print('\n')
print(df)