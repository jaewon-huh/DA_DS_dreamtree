# 중복 데이터 처리 : 관측값(레코드) 중복 
# 중복 데이터 확인 
import pandas as pd
df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                  'c2':[1, 1, 1, 2, 2],
                  'c3':[1, 1, 2, 2, 2]})
print(df)
print('\n')

# 데이터프레임 전체 행 데이터 중에서 중복값 찾기
df_dup = df.duplicated() # .duplicated() : 이전 행들과 비교하여 중복하는 행이면 T
print(df_dup)
print('\n')

# 특정 열에서 중복 데이터 찾기 
col_dup = df['c2'].duplicated()
print(col_dup)

# 중복 데이터 제거 : drop_duplicates()
df2 = df.drop_duplicates()
print(df2)
print('\n')
# subset=
df3 = df.drop_duplicates(subset=['c2','c3'])
print(df3)