# 히스토 그램  : 변수가 하나인 단변수 데이터의 빈도수 
# plot(kind ='hist')

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('classic') # 스타일 서식

df = pd.read_csv('예제/part4/auto-mpg.csv', header= None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 연비(mpg) 열에 대한 히스토그램 그리기
df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(10, 5))

# 그래프 꾸미기
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()