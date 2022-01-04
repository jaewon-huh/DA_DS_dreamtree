import pandas as pd
import matplotlib.pyplot as plt
# 산점도
# plot() method : plot(kind = 'bar' / 'his' / 'box' / 'scatter' / 'pie' ....)

# 자동차 연비
df = pd.read_csv('예제/part3/auto-mpg.csv', header=None)
print(df.head())
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
print('\n')

df.plot.scatter(x='weight', y = 'mpg')
plt.show()