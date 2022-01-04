# 파이차트 plot(kind = 'pie)

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')

df = pd.read_csv('예제/part4/auto-mpg.csv', header= None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
print(df.info())
# 데이터 개수 카운트를 위해 값 1을 가진 열 추가 
df['count'] =1 
df_origin = df.groupby('origin').sum() # origin 열 기준으로 그룹화 , 합계 연산
print(df_origin.head())

# 제조국가 값을 실제 지역명으로 변경
df_origin.index = ['USA', 'EU', 'JPN']

# 파이 그래프 그리기 
df_origin['count'].plot(kind ='pie',
                        figsize =(7,5),
                        autopct='%1.1f%%',   # 퍼센트 % 표시
                        startangle=10,       # 파이 조각을 나누는 시작점(각도 표시)
                        colors=['chocolate', 'bisque', 'cadetblue']    # 색상 리스트
                        )

plt.title('Model Origin', size =20)
plt.axis('equal') # 파이 차트의 비율을 같게 조정 
plt.legend(labels = df_origin.index , loc ='upper right')
plt.show()