# 데이터 표준화 
# 단위환산 : 마일, 야드 , 온스 -> meter,평,gram

import pandas as pd 

# UCL 자동차 연비 데이터 셋
df = pd.read_csv('예제/part5/auto-mpg.csv', header= None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name'] 
print(df.head(3))    
print('\n')

# mpg(mile per gallon) -> kpl(kilometer per liter)
mpg_to_kpl = 1.60934/3.78541 # (km/L)
df['kpl'] = df['mpg'] * mpg_to_kpl
df['kpl'] = df['kpl'].round(2)
print(df.head(3))    
