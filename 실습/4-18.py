# seaborn 라이브러리 - 고급 그래프 도구
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')

print(titanic.head())
print('\n')
print(titanic.info())
# 891개명 / 15 columns

# 회귀선이 있는 산점도 
# sns.regplot(data , ax , x = , y= ) 
sns.set_style('darkgrid')

fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# 그래프 그리기 x - age / y - fare
sns.regplot(x= 'age' , y= 'fare',
            data = titanic, # 데이터
            ax = ax1)       # axe 객체 : 1번째 그래프 
            # 그래프 그리기 x - age / y - fare
sns.regplot(x= 'age' , y= 'fare',
            data = titanic, # 데이터
            ax = ax2,       # axe 객체 : 2번째 그래프 
            fit_reg = False)# 회귀선 미표시

plt.show()       