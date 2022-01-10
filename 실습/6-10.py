# 데이터 프레임 합치기 
# concat() / merge() / join()
# pd.concat(df의 리스트) : 기존 df의 형태를 유지하면서 이어 붙이기 
# 옵션 : axis = 0  위아래 행 방향 연결 / join = 'outer' 열 이름 합집합 , 'inner' 교집합 연결

import pandas as pd 

# df 
df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3']},
                    index=[0, 1, 2, 3])
 
df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c3', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5']},
                    index=[2, 3, 4, 5])

print(df1,'\n')
print(df2,'\n')

# 두개의 df 를 행 방향으로 연결
result1 = pd.concat([df1, df2] )  # 열 이름 합집합 -> df1 없는 열 NaN
print(result1, '\n')

# ignore_index = True : 인덱스 무시하고 새로운 인덱스 0~3 + 2~5 -> 0~ 7(8개)
result2 = pd.concat([df1, df2], ignore_index= True)
print(result2, '\n')


# 두개의 df를 열 방향으로 연결 (좌우) : axis= 1
result3 = pd.concat([df1, df2], axis= 1)  # 행 인덱스의 합집합 
print(result3, '\n')

# axis = 1 , join = 'inner'  :  행 인덱스의 교집합 
result3_in = pd.concat([df1, df2], axis= 1, join='inner') 
print(result3_in, '\n')

# df와 시리즈를 열방향으로 연결 = df 에 열 추가
# 시리즈의 이름이 열 이름 & ' 행 인덱스 = 시리즈 인덱스' 다르면 NaN 
# 시리즈 만들기
sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')
sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')

# df1과 sr1을 좌우 열 방향으로 연결하기
result4 = pd.concat([df1, sr1], axis=1)  
print(result4, '\n')

# df2과 sr2을 좌우 열 방향으로 연결하기
result5 = pd.concat([df2, sr2], axis=1, sort=True)  # sr2- index 2 x
print(result5, '\n')

# sr1과 sr3을 좌우 열 방향으로 연결하기 -> df
result6 = pd.concat([sr1, sr3], axis=1)
print(result6, '\n')
# 위 아래 연결 -> 하나의 시리즈 
result7 = pd.concat([sr1, sr3], axis=0)
print(result7, '\n')
