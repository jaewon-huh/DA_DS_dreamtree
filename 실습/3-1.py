# 데이터 살펴보기 df
import pandas as pd 

#read_csv() 함수로 df 생성
df = pd.read_csv('예제/part3/auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 데이터프레임 df의 내용을 일부 확인 
print(df.head())     # 처음 5개의 행
print('\n')
print(df.tail())     # 마지막 5개의 행
print('\n')
print('---------------------------------------')
# df의 모양과 크기 확인: (행의 개수, 열의 개수)를 튜플로 반환 
print(df.shape)
print('\n')

# 데이터프레임 df의 내용 확인 
print(df.info())
print('\n')

# 데이터프레임 df의 자료형 확인  : index 수/ columns / 각 열 정보, 자료형 float , int, object
print(df.dtypes)
print('\n')

# 시리즈(mpg 열)의 자료형 확인 
print(df.mpg.dtypes)
print('\n')

# 데이터프레임 df의 기술통계 정보 확인 
print(df.describe()) # 산술 데이터 만 
print('\n')
print(df.describe(include='all'))
# 문자열 name의 unique (고유값 개수)/ 최빈값 ford pluto / 빈도수 6