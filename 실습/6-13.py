# 그룹 연산 
# 분할(split) : groupby - 적용 : 데이터를 집계, 변환 , 필터링 - 결합
# 그룹 객체 만들기 (분할)

# 1개의 열을 기준으로 그룹화 : df.groupby(기준이 되는 열(리스트))
import pandas as pd
import seaborn as sns 

# titanic 데이터 
titanic = sns.load_dataset('titanic')
df = titanic.loc[ : ,['age','sex', 'class', 'fare', 'survived']]

print('승객수 :' , len(df))
print(df.head(), '\n')
#  class 열 기준으로 분할 (first / second / third)
grouped = df.groupby(['class'])
print(grouped)
# 그룹 객체를 iteration으로 출력 
for key, group in grouped :
    print('*key :', key)
    print('*group :', len(group))
    print(group.head(), '\n')

# 그룹 객체 grouped에 연산 메소드 : mean()
average =  grouped.mean()
print(average)

# get_group() : 특정 그룹만을 선택
group3 = grouped.get_group('Third') # Third 그룹 승객데이터 
print(group3.head())

# 여러 열을 기준으로 그룹화
grouped_two = df.groupby(['class', 'sex'])
# iteration 으로 출력
for key, group in grouped_two :
    print('*key :', key)              
    print('*number : ', len(group))
    print(group.head(), '\n')
# 키가 튜플 형태로 출력 (first, male) (first, female) ... 

# 그룹 객체에 연산 메서드
average_two = grouped_two.mean() 
print(average_two,'\n')  # 멀티 인덱스 (class & sex)
print(type(average_two))

# 특정 그룹만을 선택 get_group (튜플)
group3f = grouped_two.get_group(('Third', 'female')) # Third 그룹 승객데이터 
print(group3f.head())
