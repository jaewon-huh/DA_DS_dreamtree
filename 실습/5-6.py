# 자료형 변환 
# 숫자가 문자형 -> (int or float)

from re import T
import pandas as pd 
import numpy as np
# UCL 자동차 연비 데이터 셋
df = pd.read_csv('예제/part5/auto-mpg.csv', header= None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 
print(df.dtypes)
print('\n')
# 마력 horsepower 자료형이 문자형 
print(df['horsepower'].unique()) # 고유값 확인 - > '?' 가 섞여 있음 
print('\n')

# 1. '?' 값을 NaN 값으로 변환 및 행 삭제 2. 자료형 변환 :astype()
df['horsepower'].replace('?' , np.nan , inplace = True)
df.dropna(subset = ['horsepower'], axis = 0, inplace =True)
df['horsepower'] = df['horsepower'].astype('float')

print(df['horsepower'].dtypes)
print('\n')

# origin 열 데이터 1,2,3 = USA ,EU ,JPN : replace()
print(df['origin'].unique())
df['origin'].replace({1:'USA', 2: 'EU', 3 : 'JPN'}, inplace = True)
print(df['origin'].unique())
print(df['origin'].dtypes)
print('\n')
# origin 범주형 데이터 
df['origin'] = df['origin'].astype('category')
print(df['origin'].dtypes)
# 다시 문자열로 df['origin'].astype('str')
print('\n')
# 'moder year' : 모델 출시 연도 - 숫자  , 연도는 시간의 순서의 의미 ,숫자상 의미 x
print(df['model year'].sample(3))
df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))