import pandas as pd 
# 데이터 개수 확인 
# 각 열의 데이터 개수
# info() : 각 열의 데이터 개수 정보 출력 , but 반환 x  사용 x 
# df.count() : 각열의 데이터 개수를 시리즈 객체로 반환 
df = pd.read_csv('예제/part3/auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.count())
print('\n')
# 타입 : 시리즈 
print(type(df.count()))

# 각 열의 고유값 개수 : df['열이름'].value_counts()
# 고유값 : 행 인덱스 , 고유값 개수 : 데이터 값
unique_values = df['origin'].value_counts()
print(unique_values)
print('\n')
print(type(unique_values))