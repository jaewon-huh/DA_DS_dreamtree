# 함수 매핑 
# df 원소에 함수 매핑 : applymap(매핑 함수 )
import seaborn as sns

# 타이타닉 데이터에서 age, fare 열 선택 df 
titanic = sns.load_dataset('titanic')
df = titanic.loc[ : ,['age','fare']]
print(df.head())
print('\n')
# 함수 정의 
def add_10(n) :
    return n +10

# df에 applymap() 으로 add_10() 함수 매핑 
df_map = df.applymap(add_10)
print(df_map.head())