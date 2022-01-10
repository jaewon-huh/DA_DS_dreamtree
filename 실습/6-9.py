# 필터링 : inin() 메소드 -> 특정 값을 가진 행들을 추출 
# df 열 객체.isin(추출값의 리스트)
import pandas as pd 
import seaborn as sns

titanic = sns.load_dataset('titanic')

# 디스플레이 설정 변경 - 출력할 최대 열의 개수 
pd.set_option('display.max_columns', 10 )

# 함께 탑승한 형제 or 배우자의 수가 3,4,5 인 승객 
mask3 = titanic['sibsp'] == 3
mask4 = titanic['sibsp'] == 4
mask5 = titanic['sibsp'] == 5

df_boolean = titanic[mask3 | mask4 | mask5]  #  = titanic.loc[ , ]
print(df_boolean.head(), '\n')

# isin() 활용 : df['열'].isin(추출값 리스트 )
isin_filter = titanic['sibsp'].isin([3,4,5])
df_isin = titanic[isin_filter]
print(df_isin.head())