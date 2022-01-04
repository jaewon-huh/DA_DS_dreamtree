# 누락 데이터 치환 :fillna()
import seaborn as sns

df = sns.load_dataset('titanic')

print(df['age'].head(10))
print('\n')

# age의 누락 값을 나이의 평균으로 바구기 
mean_age = df['age'].mean(axis=0) # age 열의 평균 계산 (NaN값 제외)
df['age'].fillna(mean_age, inplace =True)

print(df['age'].head(10))
print('\n')
# 승선도시 embark_town 누락 값을 최빈값으로 바꾸기 
print(df['embark_town'][825:830])
print('\n')
# 최빈값 
most_freq = df['embark_town'].value_counts(dropna= True).idxmax()
print(most_freq)
print('\n')

df['embark_town'].fillna(most_freq, inplace = True)
print(df['embark_town'][825:830])    
# 누락데이터가 NaN 으로 표시 되지 않은 경우 df.replace('?' , np.nan , inplace = True)

# 이웃하고 있는 값으로 바꾸기 
# 직전 행의 값 : method ='ffill' , 다음 행의 값 : method ='bfill'
