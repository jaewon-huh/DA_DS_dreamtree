# 멀티 인덱스 : groupby() 에 여러 열을 전달 -> 각 열들이 다중으로 행 인덱스 구성 

from re import T
import pandas as pd
import seaborn as sns 

# titanic 데이터 
titanic = sns.load_dataset('titanic')
df = titanic.loc[ : ,['age','sex', 'class', 'fare', 'survived']]

grouped = df.groupby(['class', 'sex'])
# 그룹 객체에 연산 메소드 
gdf = grouped.mean()
print(gdf,'\n')
print(type(gdf))
# 멀티 인덱스에서 하나의 인덱스만 사용 
print(gdf.loc['First'],'\n')
# 두개 인덱스: 튜플
print(gdf.loc[('First','female')],'\n')
# xs인덱서 : sex 인덱스에서 male 값을 갖는 행 추출 
print(gdf.xs('male', level ='sex'))  # 남성 승객 - 객실 등급별 그룹