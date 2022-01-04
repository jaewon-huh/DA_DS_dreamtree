import pandas as pd 
# 행 인덱스를 기준으로 df 정렬  sort_index()
# df.sort_index( , ascending = )
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# 내림차순 정렬 
ndf = df.sort_index(ascending=False)
print(ndf)
print('\n')
# 열인덱스 내림
ndf2 = df.sort_index(axis=1, ascending= False)
print(ndf2)
print('\n') 

# 특정 열기준 정렬 
# df.sort_values(by ='열이름' ,)
print("열이름 정렬 : sort_values() ")
dict_data2 = {'c0':[1,3,2], 'c1':[4,5,6], 'c2':[8,7,9], 'c3':[12,11,10], 'c4':[13,14,15]}
df2 = pd.DataFrame(dict_data2, index=['r0', 'r1', 'r2'])
print(df2)
print('\n')
ndf3 = df2.sort_values(by = 'c1', ascending= False)
print(ndf3)