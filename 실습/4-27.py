# 이변수 데이터의 분포 : pairplot()
# 인자로 전달되는 df의 열을 두개씩 짝 지을 수 있는 모든 조합에 대해 표현

import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
titanic.info()
sns.set_style('whitegrid')

# 분석 데이터 선택
titanic_pair = titanic[['age', 'pclass', 'fare']]
# 그리드 나누기 
g = sns.pairplot(titanic_pair) # 3x3
plt.show()
# 같은 변수 끼리는 히스토그램 / 다른 변수간에는 산점도 