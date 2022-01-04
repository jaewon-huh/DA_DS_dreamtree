# 범주형 데이터의 산점도 
# stripplot() : 데이터 분산 미고려
# swarmplot() : 데이터 분산 고려 

import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

# 891개명 / 15 columns
sns.set_style('whitegrid')

# 그래프 객체 생성 
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# 이산형 변수의 분포 
sns.stripplot(x='class', y = 'age', 
              ax = ax1, data = titanic)
# 데이터 분산 고려 
sns.swarmplot(x='class', y = 'age', hue= 'sex',
              ax = ax2, data = titanic)
# hue = 범주형 변수 : 범주 따라 다르게 시각화 
ax1.set_title('Strip plot') 
ax2.set_title('Strip plot') 

plt.show()            
