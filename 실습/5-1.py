# 누락 데이터 확인 및 처리 : NAN
import seaborn as sns

df = sns.load_dataset('titanic')
print(df.head())
print(df.info()) # deck data 누락 891- 203 = 688 개

# deck 열의 NaN 개수 확인 
nan_deck = df['deck'].value_counts(dropna =False)
print(nan_deck)
print('\n')

# 누락 데이터 찾는 직접적 방법
# isnull() : 누락 데이터면 T, 아니면 F / notnull() : 유효 데이터면 T, 누락데이터면 F
print(df.head().isnull())
print('\n')
print(df.head().notnull())

# 누락데이터 개수 구하기 
print('------------누락 데이터 개수 ----------------')
print(df.isnull().sum(axis =0)) # 누락이면 1

# 누락 데이터 제거 :  누락 데이터가 들어있는 열 또는 행 삭제 
# 열 삭제 : 누락데이터의 변수 삭제 / 행삭제 : 분석 대상의 관측값(레코드) 삭제 
# for 반복문으로 각 열의 Nan 개수 확인
print('------------for 반복문으로 열의 NaN 개수 ---------------')
missing_df = df.isnull()
for col in df.isnull() : 
    missing_count = missing_df[col].value_counts() # 각열의 Nan 개수 확인 
    try : 
        print(col, ':', missing_count[True]) # NaN의 개수 출력 
    except : 
        print(col, ':', 0)

# deck 열의 누락데이터 삭제하여 분석에서 제외
# dropna() : Remove missing values 
df_thresh = df.dropna(axis =1 , thresh = 500) # NAN 값 500개 이상 모든 열 삭제 
print(df_thresh.columns)

# age 열 NaN 개수 177 , 나이가 데이터 분석에 중요한 변수 -> 나이 데이터가 없는 승객 정보 x (행삭제 )
# subset = array-like : 한정, how = default 'any'/ 'all' : 모든 데이터가 NaN인 경우 삭제
df_age = df.dropna(subset = ['age'], axis = 0, how ='any')
print(len(df_age)) # 891 - 177

