from numpy import result_type, subtract
import pandas as pd 
# 판다스 객체의 산술연산 - 프로세스 
# 1 - 행/열 인덱스를 기준으로 모든 원소 정렬 
# 2 - 동일한 위치의 원소끼리 1:1 대응 
# 3 - 일대일 대응 되는 원소끼리 연산 (대응 x - NaN)
# 시리즈 연산 

# 시리즈 vs 숫자 -> 시리즈 개별 원소에 적용 
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1)
print('\n')

# 학생의 과목별 점수 (시리즈) 를 200으로 나누기
percentage = student1 / 200 
print(percentage)
print('\n')
print(type(percentage))

