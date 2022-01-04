from numpy import mat
import pandas as pd 
# 행 선택 
# loc['a':'c'] : 인덱스 이름 기준 
# iloc[0:2]  : 정수형 위치 인덱스 (범위 끝 제외)

exam_data = {'수학' : [ 90, 80, 70], '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100], '체육' : [ 100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)       # 데이터프레임 출력
print('\n')

# 행 인덱스를 사용하여 행 1개를 선택
label1 = df.loc['서준']    # loc 인덱서 활용
position1 = df.iloc[0]     # iloc 인덱서 활용
print(label1)
print('\n')
print(position1)
print('\n')

# 행 인덱스를 사용하여 2개 이상의 행 선택
label2 = df.loc[['서준', '우현']]
position2 = df.iloc[[0, 1]]
print(label2)
print('\n')
print(position2)
print('\n')

# 행 인덱스의 범위를 지정하여 행 선택
label3 = df.loc['서준':'우현']
position3 = df.iloc[0:1]
print(label3)
print('\n')
print(position3)
print('\n')


# 열 선택 df['열이름'] or df.열이름 
print('열 선택 입니다')
# 1개의 열 선택 - > 시리즈 객체 
# 수학 열 선택 df[' ']
math1 = df['수학']
print(math1)
print(type(math1))
print('\n')
# 영어 열 선택 df.
eng1 = df.영어
print(eng1)
print(type(eng1))

# 2개 이상의 열 선택 
print('두개 이상의 열 선택')

# '음악', '체육' 점수 데이터를 선택. 변수 music_gym 에 저장
music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym))
print('\n')

# '수학' 점수 데이터만 선택. 변수 math2에 저장
math2 = df[['수학']] # 2중 대괄호 -> 1개의 열 df로 반환 
print(math2)
print(type(math2))