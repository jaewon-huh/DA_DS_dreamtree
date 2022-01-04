import pandas as pd 
# 시리즈 ( 파이썬 딕셔너리와 유사  index - value)

dict_data = {'a' : 1 , 'b' : 2 , 'c' : 3 }
# 판다스 Series() : dict -> Series로 변환
sr = pd.Series(dict_data)
print(type(sr))
print('\n')
print(sr)  # 시리즈 객체 출력 

