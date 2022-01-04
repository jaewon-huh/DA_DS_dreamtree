import pandas as pd 
# 열 추가 df['열이름'] = 데이터 값 
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print('\n')
# 국어 열 추가 
df['국어'] = 80
print(df)
print('\n')
# 행추가 df.loc['행이름'] = 데이터 값 (or 배열)
print('행 추가입니다.')
df.loc[3] = 0
print(df) 
print('\n')
df.loc[4] = ['재원', 100 ,100, 100 ,100,89]
print(df)
print('\n')

df.loc['행5'] = df.loc[2] # 기존 행을 복사해도 됨 
print(df)