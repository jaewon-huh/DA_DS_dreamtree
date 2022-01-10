# 그룹 연산
# 적용 : 데이터 집계 - 변환 - 필터링 
# 데이터 집계 : 그룹 객체에 다양한 연산 적용 (mean, max , min, sum, count, var, std, info ...)

import pandas as pd
import seaborn as sns 

# titanic 데이터 
titanic = sns.load_dataset('titanic')
df = titanic.loc[ : ,['age','sex', 'class', 'fare', 'survived']]

#  class 열 기준으로 분할 (first / second / third)
grouped = df.groupby(['class'])
# 각 그룹의 표준편차를 집계 
std_all = grouped.std()
print(std_all, '\n')
print(type(std_all), '\n')
std_fare = grouped.fare.std() # 각 그룹 fare 열의 표준편차 -> 시리즈 
print(std_fare,'\n')
print(type(std_fare))

# 집계 연산을 처리하는 사용자 정의 함수를 그룹 객체에 적용 : agg()
# 그룹 객체.agg(매핑함수)
def min_max(x) :
    return x.max() - x.min()
# 집계 적용
agg_minmax = grouped.agg(min_max) # 연산이 가능한 열에 대한 최대값 - 최소값의 차
print(agg_minmax.head(), '\n')

# 여러개의 매핑함수 적용
# 모든열에 여러 함수 매핑 : group객체.agg([함수1, 함수2, 함수3]) 리스트 
# 각 열 마다 다른 함수 매핑 : group객체.agg({'열1' : 함수1, '열2' : 함수 2}) 딕

agg_all = grouped.agg(['min', 'max'])
print(agg_all.head())  # age - min / max , sex- min / max ...
agg_sep = grouped.agg({'fare' : ['min', 'max'], 'age' : 'mean'})
print(agg_sep.head())
# 2개의 함수를 리스트로 입력 -> 함수명을 열 이름에 추가하여 2중 열구조 