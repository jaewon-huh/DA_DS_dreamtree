# 그룹 연산 
# 적용 : 데이터 집계 - 변환 - 필터링
# 그룹 객체 필터링 : filter(조건식 함수)

import pandas as pd
import seaborn as sns 

# titanic 데이터 
titanic = sns.load_dataset('titanic')
df = titanic.loc[ : ,['age','sex', 'class', 'fare', 'survived']]

#  class 열 기준으로 분할 (first / second / third)
grouped = df.groupby(['class'])

# 데이터 개수가 200개 이상인 그룹만 필터링
grouped_filter = grouped.filter(lambda x : len(x) >= 200)
print(grouped_filter.head(),'\n')
print(type(grouped_filter))

# age 열의 평균값이 30보다 작은 그룹만 선택 
average =  grouped.age.mean()
print(average)

age_filter = grouped.filter(lambda x : x.age.mean() < 30)
print(age_filter.tail(),'\n')
print(type(age_filter))
