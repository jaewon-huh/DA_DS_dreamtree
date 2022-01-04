import pandas as pd
# 인덱스 활용 
# df.set_index([열이름] , '열이름') : 특정 열을 인덱스로 설정 
# 원본 df 변화시키지 않고 새 df 반환

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print('\n')

# 특정 열(column)을 데이터프레임의 행 인덱스(index)로 설정 
ndf = df.set_index(['이름'])
print(ndf)
print('\n')
ndf2 = ndf.set_index('음악') #set_index()로 행 인덱스를 새로 지종하면 기존 행 인덱스는 삭제됨. 
print(ndf2)
print('\n')
ndf3 = ndf.set_index(['수학', '음악']) # 멀티 인덱스 
print(ndf3)
