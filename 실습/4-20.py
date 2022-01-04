# 히트맵 : sns.heatmap() 
# 2개의 범주형 변수를 각각 x,y축에 놓고 데이터를 매트릭스 형태로 분류

import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

print(titanic.head())
print('\n')
print(titanic.info())
# 891개명 / 15 columns
sns.set_style('darkgrid')

# df를 피벗 테이블로 정리 
table = titanic.pivot_table(index= ['sex'], columns =['class'], aggfunc ='size') # 데이터 값의 크기를 기준으로 집계 
print(table)

# 히트맵
sns.heatmap(table,
            annot = True, fmt="d",  # annot : 데이터 값 표시 여부 , fmt : 정수형 포멧 digit
            cmap='YlGnBu',          # 컬러 맵
            linewidth=.5,           # 구분 선
            cbar=False)             # 컬러 바 표시 여부

plt.show()