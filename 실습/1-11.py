import pandas as pd 
# 행,열의 위치 바꾸기 (선형대수 전치행렬)
# df.transpose() or df.T : 기존 객체에 새로운 객체를 할당 

exam_data = {'이름' : [ '서준', '우현', '인아'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '음악' : [ 85, 95, 100],
             '체육' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print('\n')

# 데이터프레임 df를 전치하기 (메소드 활용)
df = df.transpose()
print(df)
print('\n')

# 데이터프레임 df를 다시 전치하기 (클래스 속성 활용)
df = df.T
print(df)