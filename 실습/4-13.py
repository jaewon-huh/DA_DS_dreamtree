# 2축 그래프 그리기 
# 기존 축 : 막대그래프 / 보조 축 : 선그래프 그리기
# 보조축  ax2 = ax1.twinx() : 쌍둥이 객체 생성후 ax2에 선그래프 

import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager,rc
font_path = "예제/part4/malgun.ttf" # 폰트 파일 위치 
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font_name)

plt.style.use('ggplot')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 부호 출력 설정 

# 북한 발전량 데이터 
df = pd.read_excel('예제/part4/남북한발전전력량.xlsx', convert_float= True)
df = df.loc[5:9]
df.drop('전력량 (억㎾h)', axis='columns', inplace=True)
df.set_index('발전 전력별', inplace=True)
df = df.T 
# 증감률 계산
df = df.rename(columns= {'합계' : '총발전량'})
df['총발전량 - 1년'] = df['총발전량'].shift(1)  # '총발전량' 열 데이터를 1행씩 뒤로 이동시킴
print(df.head())
df['증감률'] = ((df['총발전량'] / df['총발전량 - 1년'])- 1) * 100

# 2축 그래프 그리기 
# ax 1 : 수력, 화력 열 값을 쌓은 세로형 막대 그래프 
ax1 = df[['수력','화력']].plot(kind='bar', figsize =(20,10), width = 0.7, stacked = True)
ax2= ax1.twinx()
# ax2 : df.index x축 / df.증감률을 y축으로 하는 점 선그래프 
ax2.plot(df.index, df.증감률 , ls ='--',
         marker ='o', markersize = 20, 
         color ='red', label ='전년대비 증감률(%)')

ax1.set_ylim(0,500)
ax2.set_ylim(-50,50)

ax1.set_xlabel('연도', size=20)
ax1.set_ylabel('발전량(억 KWh)')
ax2.set_ylabel('전년 대비 증감율(%)')

plt.title('북한 전력 발전량 (1990 ~ 2016)', size=30)
ax1.legend(loc='upper left')

plt.show()