# 그룹 연산
# 적용 : 데이터 집계 - 변환 - 필터링
# agg() : 함수 정의 / 그룹별로 연산 결과를 집계하여 반환 
# 데이터 변환 : transform( 매핑함수)  - 그룹 연산의 결과를 원본 df와 같은 형태로 변형하여 정리 
import pandas as pd
import seaborn as sns 

# titanic 데이터 
titanic = sns.load_dataset('titanic')
df = titanic.loc[ : ,['age','sex', 'class', 'fare', 'survived']]

#  class 열 기준으로 분할 (first / second / third)
grouped = df.groupby(['class'])

# 그룹 별 age 열의 평균 
age_mean = grouped.age.mean()
print(age_mean, '\n')
# 그룹별 age 열의 표준편차
age_std = grouped.age.std()
print(age_std, '\n') 
# 그룹별 age 열을 iteration 으로 z-score 을 계산하여 출력 
# z스코어  : 측정 단위가 다른것과 환산하여 직접적인 비교를 가능하게 하는 방법
# x- m / std
for key, group in grouped.age :  # key : 1st , 2nd, 3rd
    group_zscore = (group - age_mean.loc[key])/age_std.loc[key]
    print('*origin : ', key)
    print(group_zscore.head(3), '\n')

print('transform-----------')
# transform() 로 age열의 z-score
def z_score(x) :
    return (x- x.mean()) / x.std()
age_zscore = grouped.age.transform(z_score)
print(age_zscore.loc[[1,9,0]],'\n')  # 1,2,3 그룹의 첫 데이터 확인 (변환결과)
print(len(age_zscore),'\n')
print(age_zscore.loc[0:9], '\n')
print(type(age_zscore))  #본래 age 행 시리즈 