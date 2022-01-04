import pandas as pd
import matplotlib.pyplot as plt
# 박스플롯
# plot() method : plot(kind = 'bar' / 'his' / 'box' / 'scatter' / 'pie' ....)
# vscode : df. plot.box() / plt.show()
# 자동차 연비
df = pd.read_csv('예제/part3/auto-mpg.csv', header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

df[['mpg','cylinders']].plot.box()
plt.show()