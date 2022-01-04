# 조건을 적용하여 화면을 그리드로 분할
# FacetGrid(data = , col = , row = )
# 각 서브플롯에 적용할 그래프 종류를 map() 메소드를 이용해 그리드 객체에 전달

import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

# 그리드 분할 col = who (탑승객 구분 man/ woman/ child ) row = 'survived' (0,1)
g = sns.FacetGrid(data = titanic, col ='who', row ='survived')
# 그래프 적용
g = g.map(plt.hist, 'age') 
plt.show()
