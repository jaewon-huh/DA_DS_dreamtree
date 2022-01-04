# 빈도그래프 countplot() : 각 범주에 속하는 데이터의 개수를 막대그래프로

import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

# 891개명 / 15 columns
sns.set_style('whitegrid')

# 그래프 객체 생성 (3개의 axe)
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

# 그래프 표시
# 기본
sns.countplot(x= 'class', palette='Set1',
              data = titanic, ax= ax1)
# hue = who
sns.countplot(x= 'class', hue = 'who', palette='Set2',
              data = titanic, ax= ax2)
# hue = who ,누적출력
sns.countplot(x= 'class', hue ='who', palette='Set3', dodge= False,
              data = titanic, ax= ax3)

# 제목 
ax1.set_title('Titanic Class')
ax2.set_title('Titanic Class - who')
ax3.set_title('Titanic Class - who(stacked)')

plt.show()