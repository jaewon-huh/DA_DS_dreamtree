# 박스 플롯 : 범주형 데이터의 분포 (최소/ 최대값 , 4/4분위)

import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager,rc
font_path = "예제/part4/malgun.ttf" # 폰트 파일 위치 
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font_name)

plt.style.use('seaborn-poster')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 부호 출력 설정 

df = pd.read_csv('예제/part4/auto-mpg.csv', header= None)

df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 그래프 객체 생성
fig = plt.figure(figsize =(15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# axe 객체에 그래프 그리기
ax1.boxplot(x =[df[df['origin'] ==1]['mpg'], # df['origin'] == 1인 행 , mpg 열 
                df[df['origin'] ==2]['mpg'], 
                df[df['origin'] ==3]['mpg']],
                labels = ['USA', 'EU', 'JAPAN'])

ax2.boxplot(x =[df[df['origin'] ==1]['mpg'], # df['origin'] == 1인 행 , mpg 열 
                df[df['origin'] ==2]['mpg'], 
                df[df['origin'] ==3]['mpg']],
                labels = ['USA', 'EU', 'JAPAN'],
                vert = False) # 수평 그래프     

ax1.set_title('제조국가별 연비 분포 (수직)')  
ax2.set_title('제조국가별 연비 분포 (수평)')

plt.show()

# 파이썬 그래프 갤러리 : python-graph-gallely.com