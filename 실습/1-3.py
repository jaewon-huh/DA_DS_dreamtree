# 원소 선택 values
# 인덱스 이름 / 정수형 위치 인덱스 

import pandas as pd
# 튜플 -> 시리즈 
tup_data = ('영인', '1999-12-29', '여', True)
sr= pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
# Series(x, index =) 인덱스 이름을 직접 설정 
print(sr)
print('\n')

print(sr[0])
print(sr['이름'])
print('\n')

# 여러개 원소 선택 - 인덱스 리스트 활용 []
print(sr[[1,2]])
print(sr[['생년월일', '성별']])
print('\n')

# 인덱스 범위 지정 
print(sr[1:3])
print(sr[:'성별'])
