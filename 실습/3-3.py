import pandas as pd 
# 통계 함수 적용 
# mean() 
# df.mean() : 모든 열의 평균 / df['열'].mean() : 특정 열 평균 

df = pd.read_csv('예제/part3/auto-mpg.csv', header=None)
# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

print(df.mean())
print('\n')
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg','weight']].mean())
print('----------------------------------------')
# median() : 중앙값 
print(df.median())
print('\n')
print(df['mpg'].median())
print('----------------------------------------')
# max() : 최대값 / min() : 최소값
print(df.max())
print('\n')
print("mpg_max : {}".format(df['mpg'].max()))
print('----------------------------------------')
print(df.min())
print('\n')
print("mpg_min : {}".format(df['mpg'].min()))

print('----------------------------------------')
# 표준편차 : std()
print(df.std())
print('\n')
print("mpg_std : {}".format(df['mpg'].std()))

print('----------------------------------------')
# 상관계수 : corr()
print(df.corr())
print('\n')
print(df[['mpg','weight']].corr())

