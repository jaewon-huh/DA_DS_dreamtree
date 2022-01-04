# 박스플롯 / 바이올린 그래프 
# 박스플롯 : 범주형 데이터 분포와 주요 통계지표 boxplot()
# 박스플롯만으로 데이터 분산정도 알기 어렵 
# 커널 밀도 함수 그래프를 y축에 추가 -> 바이올린 그래프 violinplot()

import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

# 891개명 / 15 columns
sns.set_style('whitegrid')

# 그래프 객체 생성 (4개의 axe)
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

# 타이타닉 생존자의 분포 (나이별) 
# no / yes , age - 연속형 , hue = 성별 
sns.boxplot(x='alive', y ='age',
            data= titanic, ax =ax1)
sns.boxplot(x='alive', y ='age', hue= 'sex',
            data= titanic, ax =ax2)
# 생존자와 사망자의 분포

sns.violinplot(x='alive', y ='age',
               data= titanic, ax =ax3)
sns.violinplot(x='alive', y ='age', hue= 'sex',
               data= titanic, ax =ax4)
# 생존자와 사망자의 분포 , 분산까지 알 수 있음             
plt.show()