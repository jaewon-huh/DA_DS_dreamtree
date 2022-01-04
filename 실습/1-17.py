import pandas as pd 
# 시리즈 vs 시리즈 -> 시리즈 모든 인덱스에 대해 같은 인덱스를 가진 원소끼리 계산 
# Series1 + 연산자(+,-,*,/) + Series2 
student1 = pd.Series({'국어':100, '영어':80, '수학':90})
student2 = pd.Series({'수학' : 80 ,'국어': 90, '영어': 80 }) 
print(student1)
print('\n')
print(student2)
print('\n')

add = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(add)
print('/n')
result = pd.DataFrame([add,subtraction,multiplication,division],
                        index= ['덧셈','뺄셈','곱셈','나눗셈'])
print(result)


print(' ------------------------------ ')

# 두시리즈의 원소 개수나 두 인덱스의 값이 다를 때 -> 규칙 맞지 않는 것은 NaN 처리 

# 판다스 객체의 산술연산 - 프로세스 
# 1 - 행/열 인덱스를 기준으로 모든 원소 정렬 
# 2 - 동일한 위치의 원소끼리 1:1 대응 
# 3 - 일대일 대응 되는 원소끼리 연산 (대응 x - NaN)
import numpy as np
student3 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student4 = pd.Series({'수학':80, '국어':90})

print(student3)
print('\n')
print(student4)
print('\n')

# 두 학생의 과목별 점수로 사칙연산 수행 (시리즈 vs. 시리즈)
addition2 = student3 + student4               #덧셈
subtraction2 = student3 - student4            #뺄셈
multiplication2 = student3 * student4         #곱셈
division2 = student3 / student4               #나눗셈
print(type(division))
print('\n')

# 사칙연산 결과를 데이터프레임으로 합치기 (시리즈 -> 데이터프레임)
result2 = pd.DataFrame([addition2, subtraction2, multiplication2, division2], 
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result2)
print('\n')
# 국어 - st3의 값 Nan 이라 Nan / 수학 - 모두 인덱스 및 값 존재 / 영어 - st4 영어 인덱스 x 
print('-------Series.add(Series2, fill_values=0) -----------')
# Series.연산(fill_values = 0) 을 이용해 누락 데이터 대신 0을 넣음 
sr_add = student3.add(student4, fill_value=0)
sr_sub = student3.sub(student4, fill_value=0)
sr_mul = student3.mul(student4, fill_value=0)
sr_div = student3.div(student4, fill_value=0)

result3 =pd.DataFrame([sr_add,sr_sub,sr_mul,sr_div],
                    index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result3)