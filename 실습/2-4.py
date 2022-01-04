import pandas as pd
from pandas._libs.tslibs.timedeltas import ints_to_pytimedelta 
# html 웹에서 표 속성 가져오기 
# read.html('웹주소, 파일경로') : html의 <table>태그에서 표 형식의 데이터 찾아 df로 반환 

url = '예제\part2/sample.html'
tables = pd.read_html(url)

# 출력
print(len(tables)) # 표(table)의 개수 
print('\n')
# tables 리스트의 원소들을 iteration 하면서 출력 
for i in range(len(tables)):
    print("tables[%s]" % i) # 제목 출력 %s : add a string inside another string 
    print(tables[i])
    print('\n')

df = tables[1]
df.set_index(['name'], inplace =True) # inplace = T 원본 변수에 적용 / df = df.set_index(['name'])
print(df)