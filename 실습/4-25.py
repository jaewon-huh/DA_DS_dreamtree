# 조인트 그래프  : jointplot()
# 산점도를 기본으로 표시하고 x-y 축에 각 변수에 대한 히스토그램

import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

sns.set_style('whitegrid')

# 조인트 그래프 - jointplot()
j1 = sns.jointplot(x= 'fare', y = 'age', data = titanic)
# 회귀선 추가 
j2 = sns.jointplot(x= 'fare', y = 'age', kind ='reg', data = titanic)
# 육각 그래프
j3 = sns.jointplot(x= 'fare', y = 'age', kind = 'hex', data = titanic)
# 커널 밀집 그래프 
j4 = sns.jointplot(x= 'fare', y = 'age', kind = 'kde', data = titanic)

j1.fig.suptitle('titanic fare - scatter', size = 15)
j2.fig.suptitle('titanic fare - reg', size = 15)
j3.fig.suptitle('titanic fare - hex', size = 15)
j4.fig.suptitle('titanic fare - kde', size = 15)

plt.show()