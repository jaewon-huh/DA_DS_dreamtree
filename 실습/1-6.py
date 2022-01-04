import pandas as pd 
# 행 / 열 삭제 
# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장 
exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print('Df')
print(df)
print('\n')
 
# 행 삭제 df.drop(행인덱스 or 배열 ,axis = 0 (디폴트 ))
# 1개의 행 
df2 = df[:]
df2.drop('우현', inplace=True)
print('Df- 우현 행 삭제 ')
print(df2)
print('\n')

# 2개의 행 
df3 = df[:]
df3.drop(['우현', '인아'], axis=0, inplace=True) 
print('Df- 우현, 인아 행 삭제 ')
print(df3)
print('\n')

# 열 삭제 df.drop(열이름 or 배열, axis = 1 (필수 ))
df4 = df.copy()
df4.drop('수학', axis=1, inplace=True)
print('Df- 수학 열 삭제 ')
print(df4)
print('\n')

# 데이터프레임 df를 복제하여 변수 df5에 저장. df5의 2개 열(column)을 삭제
df5 = df.copy()
df5.drop(['영어', '음악'], axis=1, inplace=True)
print('Df- 영어,음악 열 삭제 ')
print(df5)
