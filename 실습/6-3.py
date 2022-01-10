# 시리즈 객체에 함수 매핑 
# df 각 열에 함수 매핑 : df.apply(함수 , axis = 0)
import seaborn as sns

# 타이타닉 데이터에서 age, fare 열 선택 df 
titanic = sns.load_dataset('titanic')
df = titanic.loc[ : ,['age','fare']]
print(df.head())
print('\n')

# 함수 정의 
def missing_value(series) :
    return series.isnull()       # T/F 시리즈 반환 : NaN -T 

# apply()
result = df.apply(missing_value, axis = 0)  
print(result.head())         # 열에 매핑하나 df 원소에 매핑하나 뭔 차이?
print('\n')
print(type(result))          # 시리즈 반환 매핑 함수 -> df 반환  (시리즈  + 시리즈 ... -> df)
print('\n')

# 함수 정의 : 시리즈 입력 -> 값을 반환 하는 함수 
def min_max(x):
    return x.max() - x.min()     # 시리즈 최대값 - 최소값 

result2 = df.apply(min_max, axis = 0)
print(result2)
print('\n')
print(type(result2))  