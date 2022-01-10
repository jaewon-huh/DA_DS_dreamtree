# 함수 매핑 
# 시리즈 원소에 함수 매핑 : apply(매핑 함수 )
import seaborn as sns

# 타이타닉 데이터에서 age, fare 열 선택 df 
titanic = sns.load_dataset('titanic')
df = titanic.loc[ : ,['age','fare']]
df['ten'] = 10 # 10을 값으로 갖는 열 추가 
print(df.head())

# 함수 정의 
def add_10(n) :
    return n +10

def add_two_obj(a,b) :
    return a+b

print(add_10(10))
print(add_two_obj(10,10))

# apply() 메소드 : series.apply(매핑함수)
sr1 = df['age'].apply(add_10)  # add_10(n) : n = df['age']
print(sr1.head())
print('\n')

sr2 = df['age'].apply(add_two_obj, b=10)  # add_two_obj(a,b) : a = df['age']
print(sr2.head())
print('\n')
# 람다 
sr3 = df['age'].apply(lambda x : x+10)
print(sr3.head())
