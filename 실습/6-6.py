# 열 재구성
# 열 순서 변경 : 열 이름 순서 정리 - 리스트 - df에서 열을 다시 선택 
# df[재구성한 열 이름의 리스트]
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[0:4, 'survived': 'age']  # 마지막 범위의 값 포함 
print(df, '\n')

# 열 이름 배열 리스트 
columns = list(df.columns.values)
print(columns, '\n')

# 리스트 정렬 (알파벳 순) : sorted()
columns_sorted = sorted(columns)
# df에서 열을 다시 선택 
df_sorted = df[columns_sorted]
print(df_sorted, '\n')

# reversed() -> list() 
columns_reversed = list(reversed(columns))
# df에서 열을 다시 선택 
df_reversed = df[columns_reversed]
print(df_reversed, '\n')

# 사용자가 정의한 임의 순서대로 
columns_customed = ['pclass', 'sex', 'survived', 'age']
df_customed = df[columns_customed]
print(df_customed)