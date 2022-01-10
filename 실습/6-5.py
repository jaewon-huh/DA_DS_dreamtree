
# df 객체에 함수 매핑 : df.pipe(매핑함수)
# 매핑함수 리턴값 : df / series / 개별 값
import re
import seaborn as sns

# 타이타닉 데이터에서 age, fare 열 선택 df 
titanic = sns.load_dataset('titanic')
df = titanic.loc[ : ,['age','fare']]

# 함수 정의 
def missing_value(x):
    return x.isnull()   # df 입력 df 반환 (불)

def missing_count(x):
    return missing_value(x).sum() # 시리즈 반환 

def total_number_missing(x) :
    return missing_count(x).sum() # 개별 값 반환 

# pipe() , df 반환 
result_df = df.pipe(missing_value)
print(result_df.head())
print(type(result_df))
print('\n')
# 시리즈 반환 
result_sr = df.pipe(missing_count)
print(result_sr)  # age 열 Nan 값이 177  / fare - 0개  , 각 열의 누락 데이터 개수
print(type(result_sr))
print('\n')

result_value = df.pipe(total_number_missing)
print(result_value) # 각열의 누락 데이터 개수를 합산 177+0 + ... = x 
print(type(result_value))
print('\n')