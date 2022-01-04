import pandas as pd 
# 데이터 프레임 연산  : 행/ 열 인덱스 기준 정렬 , 1:1 대응 원소끼리 연산
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())   #첫 5행만 표시
print('\n')
print(type(df))
print('\n')

# 데이터프레임에 숫자 10 더하기
addition = df + 10  
print(addition.head())   #첫 5행만 표시
print('\n')
print(type(addition))
print('\n')

# Df vs Df
print(df.tail()) # last 5
print('\n')
print(addition.tail())
print('\n')

subtraction = addition - df 
print(subtraction.tail())
# 원소가 없거나 nan이면 Nan