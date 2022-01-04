# 막대 그리프 barplot()
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

# 그래프 생성
sns.barplot(x='sex', y='survived', 
            data = titanic, ax =ax1)
# hue옵션 추가
sns.barplot(x='sex', y='survived', hue='class',
            data = titanic, ax =ax2)
# hue 옵션 + 누적 출력            
sns.barplot(x='sex', y='survived', hue='class', dodge= False, 
            data = titanic, ax =ax3)

ax1.set_title('titianic survived - sex')
ax2.set_title('titianic survived - sex/class')
ax3.set_title('titianic survived - sex/class(Stacked)')

plt.show()