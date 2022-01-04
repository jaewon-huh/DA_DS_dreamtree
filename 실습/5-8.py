# 범주형 변수 더미변수로 변환 0/1 : F/T , get_dummies()
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

# horsepower을 저출력 / 중출력 / 고출력으로 구분 -> 4개의 경계값 필요 
# np.histogram() 
count, bin_dividers = np.histogram(df['horsepower'], bins=3) # bins - 구간 개수
# count = 각 구간에 속하는 값 개수 / bin_dividers = 경계 값 
print(bin_dividers)
print('\n')

bin_names = ['저출력', '보통출력', '고출력']
# pd.cut() 함수로 각 데이터를 3개의 bin에 할당 
df['hp_bin'] = pd.cut(x= df['horsepower'],   # 데이터 : 1차원
                      bins =bin_dividers,    # 구간을 나눌 기준 : 리스트
                      labels= bin_names,     # 구간에 대해 레이블을 명시
                      include_lowest= True)  # 첫 경계값을 포함한다

# hp_bin 열의 범주형 데이터를 더미 변수로 변환 : pd.get_dummies() 
# 해당 특성이 존재하면 1 , 아니면 0
horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15))