import pandas as pd
# 원소 값 변경 df '선택(일부, 원소)' = 새로운 값
# df 선택 -> df.loc[행인덱스, 열이름] / df.iloc[행번호, 열번호] 
exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)

# '이름' 열을 새로운 인덱스로 지정하고, df 객체에 변경사항 반영
df.set_index('이름', inplace=True)
print(df)
print('\n')

# 서준의 체육점수를 80점으로 변경 
df.iloc[0,3] = 80 # df.iloc[0][3] = 80
print(df)
df.loc['서준', '체육'] = 100 # df.loc['서준']['체육'] = 100
print(df)
print('\n')
# 서준의 체육, 음악 점수를 80, 20점으로 변경
df.iloc[0, 2:] = 80 ,20 
print(df)