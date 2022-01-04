import pandas as pd 
# Json 파일 : 파이썬 딕셔너리와 비슷하게 'key' : 'value'구조 
# read_json('파일경로(이름)')
df1 = pd.read_json('예제\part2/read_json_sample.json')

print(df1)
print(df1.index)