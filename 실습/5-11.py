# 각 열의 데이터 중 최대값과 최소값을 뺀 값으로 나누는 방법

import pandas as pd
import numpy as np

# UCL 자동차 연비 데이터 셋
df = pd.read_csv('예제/part5/auto-mpg.csv', header= None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 

# horsepower 열 데이터 : 마력 
df['horsepower'].replace('?' , np.nan , inplace = True)
df.dropna(subset = ['horsepower'], axis = 0, inplace =True)
df['horsepower'] = df['horsepower'].astype('float') # 실수형으로 변환

# horsepower 열의 최대값확인 
print(df.horsepower.describe()) # max 230 / min 104
print('\n') 

# 데이터 - 최소값 : 분자 / 최대값 - 최소값 : 분모
min_x = df.horsepower - df.horsepower.min()
min_max = df.horsepower.max() - df.horsepower.min()
df.horsepower = min_x /min_max

print(df.horsepower.head())
print('\n')
print(df.horsepower.describe())