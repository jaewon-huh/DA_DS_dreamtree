import pandas as pd
import matplotlib.pyplot as plt
# 판다스 내장 그래프 도구 
# plot() method : plot(kind = 'bar' / 'his' / 'box' / 'scatter' / 'pie' ....)

# 선 그래프 
df = pd.read_excel('예제/part3/남북한발전전력량.xlsx')
# 남북한 발전 량 합계, 1991~2016
df_ns = df.iloc[[0,5],3:] 
print(df_ns)
df_ns.index = ['South', 'North'] # 인덱스 이름 변경
df_ns.columns = df_ns.columns.map(int) # columns 자료형을 정수로 변경
print('\n')
print(df_ns.head())
print('\n')
# vs code에서는 matplotlib 사용해야함.
plt.plot(df_ns)
plt.show()
print('\n')
# 연도별 발전량 추이 
tdf_ns = df_ns.T # 행렬 전치 
print(tdf_ns.head())
print('\n')
plt.plot(tdf_ns)
plt.show()
