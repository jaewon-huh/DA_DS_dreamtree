import pandas as pd 
# 엑셀파일 read : pd.read_excel('파일 경로')
df1 = pd.read_excel('예제/part2/남북한발전전력량.xlsx') # 기본 header = 0 , 0행을 열이름으로 
df2 = pd.read_excel('예제/part2/남북한발전전력량.xlsx', header=None)

print(df1)
print('\n')
print(df2)