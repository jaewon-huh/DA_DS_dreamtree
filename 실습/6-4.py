# 시리즈 객체에 함수 매핑 
# df 각 행에 함수 매핑 : df.apply(함수 , axis = 1)
import seaborn as sns

# 타이타닉 데이터에서 age, fare 열 선택 df 
titanic = sns.load_dataset('titanic')
df = titanic.loc[ : ,['age','fare']]
df['ten'] = 10 
print(df.head())
print('\n')

# 함수 
def add_two_obj(a,b) :
    return a + b

# apply(axis = 1)
df['add'] = df.apply(lambda x : add_two_obj(x['age'], x['ten']), axis =1)
# x = df / a = x['age'] / b = x['ten']
print(df.head())