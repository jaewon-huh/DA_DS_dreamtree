# 누락데이터 -> 이웃하고 있는 값으로 치환
# 직전 행의 값 : method ='ffill' , 다음 행의 값 : method ='bfill'
import seaborn as sns

df = sns.load_dataset('titanic')
print(df['embark_town'][825:830])
print('\n')
# 앞선 행의 값으로 치환  
df['embark_town'].fillna(method = 'ffill', inplace = True)
print(df['embark_town'][825:830])    