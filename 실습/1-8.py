import pandas as pd 
# 원소 선택 
# df.loc[행인덱스, 열이름]
# df.iloc[행번호, 열번호]
# 1행 2열 선택 , 2행 1열 선택 -> Series 반환
# 2이상 행 , 2이상 열 선택 -> df 반환 

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
# set_index() : 이름 열을 새로운 행 인덱스로 지정 
df.set_index('이름', inplace=True)
print(df)
print('\n')

# df의 원소 1개 출력 (서준의 음악성적)
a = df.loc['서준','음악']
b = df.iloc[0,2]
print(a)
print(b)
print('\n')

# 2개 이상의 원소 출력 (서준의 음악,체육 성적)

c = df.loc['서준',['음악','체육']]
print(c)
print('\n')
d = df.loc['서준','음악':'체육']
print(d)
print('\n')
e = df.iloc[0,[2,3]]
print(e)
print('\n')
f = df.iloc[0,2:4]
print(f)


# 2개 이상의 행과 열 선택 - df로 반환 (서준 우현의 음악, 체육점수)
print('<df.loc를 이용해 df 선택>')
g = df.loc[['서준','우현'], ['음악','체육']]
print(g)
h = df.loc['서준':'우현', '음악':'체육']
print(h)
print('\n')

print('<df.iloc를 이용해 df 선택>')
i = df.iloc[[0,1], [2,3]]
print(i)
j = df.iloc[ 0:2, 2:]
print(j)
# 모든 행에 대해 찾기 df.iloc[ : ,['음악','체육] ] / df.iloc[ : , 1:3]