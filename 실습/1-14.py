import pandas as pd 
# 행인덱스 초기화
# df.reset_index() : 행 인덱스를 정수형 위치 인덱스로 초기화 , (기존 행 인덱스는 열로 이동함! )
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# 초기화 (기존 index r0 r1 r2 가 열로 이동 )
ndf = df.reset_index()
print(ndf)
