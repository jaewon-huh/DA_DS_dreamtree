# 그룹 객체에 함수 매핑 
# apply() : 판다스 객체의 개별원소에 1:1 함수 매핑 
# group 객체 .apply(매핑 함수) 

import pandas as pd
import seaborn as sns 

# titanic 데이터 
titanic = sns.load_dataset('titanic')
df = titanic.loc[ : ,['age','sex', 'class', 'fare', 'survived']]

#  class 열 기준으로 분할 (first / second / third)
grouped = df.groupby(['class'])

# 3개의 그룹에 describe() 함수 적용 
agg_grouped = grouped.apply(lambda x : x.describe())
print(agg_grouped,'\n')

# age 열의 데이터를 z-score로 변환 
def z_score(x) : 
    return (x- x.mean()) / x.std()
age_zscore = grouped.age.apply(z_score)
print(age_zscore.head(), '\n')

# age 열의 평균값이 30보다 작은 그룹 출력 (반복문)
age_filter = grouped.age.apply(lambda x : x.mean() <= 30 )
print(age_filter, '/n')

for x in age_filter.index :   # x : 1st, 2nd ,3rd
    if age_filter[x]  == True : 
        age_filter_df = grouped.get_group(x)  # 특정 그룹만을 선택
        print(age_filter_df.head(), '\n')
# first - F - x / 2nd- T - print / 3rd - T - print