# seaborn 히스토그램 / 커널 밀도함수 (그래프와 x 축 사이 면적이 1 )
# 하나의 변수의 데이터 분포 -> sns.distplot()
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

print(titanic.head())
print('\n')
print(titanic.info())
# 891개명 / 15 columns
sns.set_style('darkgrid')

# 그래프 객체 생성
fig = plt.figure(figsize=(15,5))
# 3개의 서브 플롯 생성
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

sns.distplot(titanic['fare'], ax = ax1)
# hist =F
sns.distplot(titanic['fare'], ax= ax2, hist =False)
# kde = F 
sns.distplot(titanic['fare'], ax= ax3, kde =False)

# 제목 
ax1.set_title('titanic fare - hist/kde')
ax2.set_title('titanic fare - kde')
ax3.set_title('titanic fare - hist')

plt.show()