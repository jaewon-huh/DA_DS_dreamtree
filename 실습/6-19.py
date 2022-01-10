# 피벗 : pd.pivot_table()
# 4가지 구성요소 (행 인덱스 , 열 인덱스 , 데이터 값, 데이터 집계함수)에 적용할 df 열을 각각 지정 

import pandas as pd
import seaborn as sns

# IPyhton 디스플레이 설정 변경 
pd.set_option('display.max_columns', 10)    # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20)    # 출력할 열의 너비

# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]
print(df.head(),'\n')

# 피벗 테이블 
pdf1 = pd.pivot_table(df,                       # 데이터 프레임 
                      index= 'class',           # 행 인덱스 열 
                      columns= 'sex',           # 열 위치의 열
                      values= 'age',            # 데이터로 사용할 열
                      aggfunc= 'mean')        # 데이터 집계 함수 
print(pdf1.head())
# 나이 평균 
pdf2 = pd.pivot_table(df,                       # 데이터 프레임 
                      index= 'class',           # 행 인덱스 열 
                      columns= 'sex',           # 열 위치의 열
                      values= 'survived',       # 데이터로 사용할 열
                      aggfunc= ['mean', 'sum']) # 데이터 집계 함수 
print(pdf2.head())
# mean() : 생존율 , sum() : 생존자 수 

# 인자 각각 2개 이상의 열을 입력 
pdf3 = pd.pivot_table(df,                       # 데이터 프레임 
                      index= ['class', 'sex'],  # 행 인덱스 열 
                      columns= 'survived',      # 열 위치의 열
                      values= ['age','fare'],   # 데이터로 사용할 열
                      aggfunc= ['mean', 'max']) # 데이터 집계 함수 
print(pdf3.head(),'\n')
print(pdf3.index)
print(pdf3.columns, '\n')
# levels labels names 속성 
# 행 2중구조 , 열 3중구조 mean & max - age & fare - survived

# xs 인덱서 사용  
# 행인덱스 first인 승객 
print(pdf3.xs('First'), '\n') 
# 행 인덱스가 (first , female) 튜플
print(pdf3.xs(('First', 'female')), '\n')
# 행 인덱스 레벨을 직접 지정 levels =  : sex 레벨 중 남성 승객
print(pdf3.xs('male', level = 'sex'), '\n')
# 행 인덱스 레벨 0 에서 Second를 가져오고 행인덱스 레벨 1 sex에서 male
print(pdf3.xs(('Second', 'male'), level = [0,'sex'] ), '\n')

# 열 인덱스 접근 axis = 1
print(pdf3.xs('mean', axis = 1), '\n')
# 열 인덱스 레벨 0- mean / 레벨 1  -age
print(pdf3.xs(('mean', 'age'), axis =1 ), '\n')
# 열 인덱스 레벨 직접 지정 
print(pdf3.xs(1, level= 'survived' , axis =1 ), '\n')
# 열 인덱스 레벨 0 - max / 레벨 1 fare , 레벨 2 = survived 0
print(pdf3.xs(('max','fare', 0) , level=[0,1,2], axis= 1))