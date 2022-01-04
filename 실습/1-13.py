import pandas as pd 
# 행 인덱스 재배열 
# df.reindex( 새 인덱스 배열)  : 기존 객체 변경하지 않고 df를 반환.
# dic -> df : 키 = 열 , 값 = values
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# 재배열 
new_index = ['r0', 'r1', 'r2','r3','r4']
ndf = df.reindex(new_index) 
print(ndf)
print('\n')
# Nan 채우기 redindex( , fill_value = 값)
ndf2  = df.reindex(new_index, fill_value =0) 
print(ndf2)
print('\n')
#  Nan 채우기 (ndf에 대하여)
ndf.iloc[3:, :] = 0
print(ndf)