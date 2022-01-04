import pandas as pd 
# .csv 파일 읽기
file_path = '예제/part2/read_csv_sample.csv'
df1 = pd.read_csv(file_path) # header = 0 기본값, 0행을 열 이름으로 
print(df1)
print('\n')
# header = 열이름으로 사용할 행을 지정 
df2 = pd.read_csv(file_path, header= None)
print(df2)
print('\n')

df3 = pd.read_csv(file_path, index_col= None) # 행 인덱스 자동으로 0 1 2 ...
print(df3)
print('\n')

df4 = pd.read_csv(file_path, index_col = 'c0') # c0 시리즈를 인덱스로 
print(df4)
print('\n')

# 쉼표 대신 \t 이나 공백으로 텍스트를 구분된 csv -> sep(delimiter) 옵션 사용 