# 필터링 : 특정 조건식을 만족하는 원소만 따로 추출 
# 불린 인덱싱 : df[불린 시리즈]
import seaborn as sns

titanic = sns.load_dataset('titanic')

# 나이가 10대(10~19) 인 승객만 선택 
mask1 =  (titanic['age'] >= 10) & (titanic['age'] < 20)
df_teenage = titanic.loc[mask1, : ] 
print(df_teenage.head()) 

# 나이가 10세 미만이고 여성 
mask2 = (titanic['age'] < 10) & (titanic['sex'] == 'female')
df_female_under10 = titanic.loc[mask2, : ]
print(df_female_under10.head(), '\n')

# 나이가 10세 미만 또는 60세 이상인 승객의 sex,age, alone 열 만 선택 
mask3 = (titanic['age'] < 10) | (titanic['age'] >= 60)  # | : or
df_under10_morethan60 = titanic.loc[mask3, ['age','sex','alone'] ]
print(df_under10_morethan60.head(), '\n')

# 나이가 10세 미만 또는 60세 이상인 승객이면서 여성 
mask4 = ((titanic['age'] < 10) | (titanic['age'] >= 60)) & (titanic['sex'] == 'female')
df_under10_morethan60_female = titanic.loc[mask4, :]
print(df_under10_morethan60_female.head())